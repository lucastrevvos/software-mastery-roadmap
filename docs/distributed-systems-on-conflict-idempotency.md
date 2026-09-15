# Checkpoint — Idempotência concorrente com PostgreSQL

## Situação anterior

O `PaymentService` fazia um fluxo do tipo:

```text
SELECT por order_id
→ se não existe, INSERT
```

Com duas requisições concorrentes para o mesmo `order_id`, ambas podiam observar "não existe" e depois disputar o `INSERT`. A constraint `UNIQUE(order_id)` preservava a integridade, mas uma das requisições recebia erro PostgreSQL `23505` e o Nest respondia 500.

## Melhoria aplicada

O fluxo foi alterado para uma operação atômica no PostgreSQL:

```sql
INSERT INTO payments (...)
VALUES (...)
ON CONFLICT (order_id)
DO NOTHING
RETURNING ...;
```

Se a linha for inserida, `rowCount = 1`. Se outra requisição concorrente já tiver criado o pagamento, `rowCount = 0`, e o serviço busca e retorna o pagamento existente.

## Experimento executado

Duas requisições concorrentes foram enviadas com o mesmo `orderId`:

```text
66666666-6666-6666-6666-666666666666
```

Logs observados:

```text
HTTP PAYMENT REQUEST: 66666666-6666-6666-6666-666666666666
PROCESS PAYMENT: 66666666-6666-6666-6666-666666666666
DB PAYMENT CREATED: 62fea4c5-aa7c-485a-b4e5-e0b0dd4d0a60 66666666-6666-6666-6666-666666666666

HTTP PAYMENT REQUEST: 66666666-6666-6666-6666-666666666666
PROCESS PAYMENT: 66666666-6666-6666-6666-666666666666
CONCURRENT IDEMPOTENT HIT: 66666666-6666-6666-6666-666666666666
```

## Resultado

A race condition continua existindo no sentido de que duas requisições chegam concorrentes, mas ela é arbitrada atomicamente pelo banco. Não houve violação `23505` nem erro 500. Uma requisição criou o pagamento; a outra reconheceu o resultado já criado e tratou isso como sucesso idempotente.

## Modelo mental

```text
Request A             Request B
   │                      │
   └──── INSERT ──────────┘
          │
      PostgreSQL
          │
   UNIQUE(order_id)
      ↙        ↘
   cria      conflito
    ✅      DO NOTHING
                │
                ▼
        busca existente
                ✅
```

## Insight para entrevista

Uma `UNIQUE` constraint é a garantia final de integridade, mas um padrão `SELECT → INSERT` ainda sofre race condition e pode transformar concorrência esperada em erro 500. Quando a regra cabe numa operação atômica, `INSERT ... ON CONFLICT` evita o check-then-act e permite tratar duplicidade concorrente como sucesso idempotente.

## Relação com RabbitMQ

No consumer RabbitMQ:

- pagamento criado agora → sucesso → ACK;
- pagamento já existente por idempotência → sucesso → ACK;
- falha transitória → retry/NACK conforme estratégia;
- falha permanente após política de retry → NACK sem requeue → DLQ.

Uma mensagem duplicada que já foi processada com sucesso não deve ser tratada automaticamente como erro: para um consumer idempotente, "já estava feito" é um resultado de sucesso.
