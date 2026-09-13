# Distributed Systems Lab — Retry

Data do laboratório: 2026-09-13

## Método
Construir → quebrar → observar → explicar.

## Cenário
Dois serviços NestJS em containers Docker:

```text
Orders → HTTP → Payments
```

Orders possui timeout de 2s e agora uma segunda tentativa após falha.

## Experimento executado
Chamamos Orders com `failOnce=true`. Payments mantém um `Set` de `orderId` já falhados para simular uma falha transitória apenas na primeira chamada daquele pedido.

### Logs observados

```text
orders-1    | Payment attempt 1
payments-1  | Payment attempt: 74713802-1dc2-4f8b-977a-2278ce96281a
payments-1  | Simulating temporary failure
orders-1    | Attempt 1 failed. Retrying...
orders-1    | Payment attempt 2
payments-1  | Payment attempt: 74713802-1dc2-4f8b-977a-2278ce96281a
payments-1  | Payment approved
```

O mesmo `orderId` foi usado nas duas tentativas.

## Descoberta
Retry permite recuperar uma operação quando a falha é transitória.

```text
falha temporária
      ↓
retry
      ↓
sucesso
```

## Trade-off

Sem retry:
- uma falha transitória derruba a operação.

Com retry:
- aumenta a chance de sucesso;
- aumenta latência;
- aumenta carga sobre a dependência;
- pode repetir efeitos colaterais.

## Correção importante
Nosso retry atual é pedagógico e repete praticamente qualquer erro da chamada. Em produção, a decisão de retry deve classificar a falha.

Exemplos normalmente candidatos a retry:
- timeout;
- falha de conexão;
- 429, respeitando política de backoff/retry-after;
- 502, 503 e 504 dependendo da operação.

Exemplos normalmente não candidatos a retry automático:
- 400 por entrada inválida;
- 401/403;
- regra de negócio rejeitada;
- erro determinístico que continuará falhando.

## Modelo mental

```text
RETRY NÃO É "tente novamente sempre".

retry = repetir uma operação quando existe chance razoável de a causa ser temporária.
```

## Próximo experimento
Provocar a situação perigosa:

```text
Payments executa a cobrança ✅
resposta não chega ao Orders ❌
Orders interpreta como falha
retry
Payments recebe a mesma operação novamente
```

Pergunta: como impedir que o efeito seja executado duas vezes?

Próximo conceito: **idempotência**.
