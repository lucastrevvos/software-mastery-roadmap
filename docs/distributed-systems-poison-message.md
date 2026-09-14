# Checkpoint — Poison message sem DLQ

Data do laboratório: 2026-09-14.

## O que foi executado

O consumidor Payments foi configurado para simular falha permanente e controlar três tentativas em memória.

Fluxo observado:

```text
Orders publicou payment_requested
Payments: PROCESSING FAILED - ATTEMPT 1
Payments: NACK + REQUEUE
Payments: PROCESSING FAILED - ATTEMPT 2
Payments: NACK + REQUEUE
Payments: PROCESSING FAILED - ATTEMPT 3
Payments: MAX ATTEMPTS - NACK WITHOUT REQUEUE
```

Depois, o RabbitMQ mostrou:

```text
payments_queue  0  0  1
```

Isto confirmou que, sem DLX configurada, `nack(message, false, false)` remove a mensagem da fila original e ela não fica disponível para nova tentativa.

## Descoberta

Evitar um loop infinito de requeue não basta. Se a mensagem for rejeitada definitivamente sem DLX, ela pode ser descartada e o problema deixa de ser observável.

Próximo passo: configurar `payments.dlx` + `payments_dead_queue` e repetir a mesma falha para provar que a mensagem problemática vai para quarentena em vez de sumir.
