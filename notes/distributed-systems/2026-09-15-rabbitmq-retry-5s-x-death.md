# RabbitMQ retry com atraso de 5s — checkpoint comprovado

## Objetivo
Substituir o hot retry (`nack(..., requeue=true)`) por retry assíncrono com atraso controlado pelo RabbitMQ.

## Topologia comprovada

```text
payments_queue
  -- NACK requeue=false --> payments.retry
  --> payments_retry_5s
  -- TTL 5000ms / expired --> payments.return
  --> payments_queue
```

## Evidência observada
Primeira entrega:
- `REDELIVERED: false`
- `X-DEATH: []`
- falha transitória simulada
- envio para a fila de retry às `2026-09-15T19:17:04.337Z`

Retorno após o atraso:
- nova entrega às `2026-09-15T19:17:09.344Z`
- atraso observado de aproximadamente 5 segundos
- `REDELIVERED: false`
- `x-death` registrou:
  - `payments_queue`, reason `rejected`, count 1
  - `payments_retry_5s`, reason `expired`, count 1
- pagamento criado no PostgreSQL
- mensagem confirmada com ACK

## Aprendizado
- `redelivered` não é o contador apropriado para retries baseados em DLX/TTL.
- `x-death` preserva o histórico de dead-lettering e pode substituir contadores locais em memória.
- O atraso não deve ser implementado com `sleep()` dentro do consumer; a fila de retry segura a mensagem enquanto o worker fica livre.
- `nack(message, false, false)` combinado com DLX permite encaminhar a mensagem a uma estratégia de retry em vez de requeue imediato.

## Próximo passo
Eliminar `failureAttempts` em memória e construir backoff real baseado em `x-death`, com sequência planejada:

```text
falha -> retry 5s -> falha -> retry 30s -> falha -> DLQ
```
