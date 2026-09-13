# Checkpoint — Retry, idempotência e memória volátil

## Evidências observadas

- Retry recuperou uma falha temporária usando o mesmo `orderId`.
- Sem idempotência, o mesmo `orderId` gerou dois `paymentId` diferentes: cobrança duplicada.
- Com `processedPayments: Map`, a segunda tentativa retornou `IDEMPOTENT HIT` e não criou nova cobrança.
- `docker compose restart payments` reiniciou o processo Node e apagou o `Map` em memória.
- Após o restart, a mesma chave pôde ser processada novamente, provando que memória local não oferece idempotência durável/distribuída.

## Comandos novos

```bash
docker compose restart payments
curl http://localhost:3001/payments/debug
curl -X POST http://localhost:3001/payments \
  -H "Content-Type: application/json" \
  -d '{"orderId":"ORDER-IDEMPOTENCY-001","amount":100}'
```

## Modelo mental

Retry resolve falhas transitórias, mas pode repetir efeitos colaterais. Idempotência evita duplicidade quando a mesma intenção é reenviada. A chave idempotente precisa sobreviver a restart e, em múltiplas réplicas, precisa ser compartilhada entre instâncias; um `Map` local serve para aprender, não como garantia distribuída.

## Próximo passo

Trocar a dependência temporal HTTP por mensageria assíncrona com RabbitMQ. Persistência durável de idempotência será retomada quando introduzirmos banco/Redis e Outbox.
