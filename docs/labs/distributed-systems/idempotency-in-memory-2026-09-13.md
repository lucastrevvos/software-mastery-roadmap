# Idempotência em memória — checkpoint

Data: 2026-09-13

## Problema observado

Com retry habilitado, uma primeira tentativa podia criar a cobrança e perder a resposta. O Orders então fazia retry usando o mesmo `orderId`, o que antes gerava duas cobranças com `paymentId` diferentes.

## Solução implementada

Payments passou a manter um `Map` em memória indexado por `orderId`. Antes de criar uma nova cobrança, verifica se aquele `orderId` já foi processado. Se sim, retorna o pagamento anterior em vez de cobrar novamente.

## Evidência observada

```text
orders-1   | Payment attempt 1
payments-1 | Payment attempt: 5f5e60fc-23da-45c4-87e5-d4fb46cad029
payments-1 | CHARGE CREATED: eeed6a62-0c86-46c8-a0b9-47cd2adc163c 5f5e60fc-23da-45c4-87e5-d4fb46cad029
payments-1 | Charge succeeded, but response will be delayed
orders-1   | Attempt 1 failed. Retrying...
orders-1   | Payment attempt 2
payments-1 | Payment attempt: 5f5e60fc-23da-45c4-87e5-d4fb46cad029
payments-1 | IDEMPOTENT HIT: 5f5e60fc-23da-45c4-87e5-d4fb46cad029
```

## Conclusão

O retry repetiu a operação, mas Payments reconheceu o mesmo `orderId` e não criou uma segunda cobrança.

Modelo mental:

```text
retry + efeito colateral
        ↓
risco de duplicação
        ↓
idempotência
        ↓
mesma chave → mesmo resultado
```

## Trade-off descoberto

A solução atual funciona apenas enquanto o processo mantém o `Map` em memória. Ela não é suficiente para restart de container, crash ou múltiplas réplicas de Payments.

Próximo experimento: reiniciar Payments e observar a perda do estado idempotente.
