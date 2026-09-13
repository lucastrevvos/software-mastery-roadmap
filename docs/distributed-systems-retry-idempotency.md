# Distributed Systems Lab — Retry → duplicidade → idempotência

## Evidência observada

O laboratório confirmou que retry consegue recuperar uma falha transitória usando o mesmo `orderId`.

Fluxo observado:

```text
Orders: Payment attempt 1
Payments: Simulating temporary failure
Orders: Attempt 1 failed. Retrying...
Orders: Payment attempt 2
Payments: Payment approved
```

Trade-off: retry aumenta a chance de sucesso em falhas transitórias, mas também aumenta latência/carga e pode repetir operações com efeito colateral. Em produção, não se deve retryar qualquer erro indiscriminadamente; normalmente retry faz sentido para falhas transitórias como timeout, falha de conexão, 502/503/504 e, dependendo do contrato, 429.

## Experimento da resposta perdida

Foi simulada uma situação em que Payments efetua a cobrança, mas a resposta demora além do timeout de Orders. Orders não consegue saber se a operação foi concluída e faz retry.

Resultado observado após corrigir o código de debug para executar `this.charges.push(payment)`:

```json
[
  {
    "paymentId": "a76ee69d-05a8-4f6d-b3c2-8dc13e1d3b37",
    "orderId": "b7613144-cbe1-4266-9583-05dffd34cfca",
    "amount": 100
  },
  {
    "paymentId": "da928964-a68e-4546-b0db-494b799a1946",
    "orderId": "b7613144-cbe1-4266-9583-05dffd34cfca",
    "amount": 100
  }
]
```

Mesmo `orderId`, dois `paymentId`: a cobrança foi duplicada.

### Correção do diagnóstico

O endpoint `/payments/debug` havia retornado `[]` inicialmente porque o código não estava adicionando a cobrança ao array `charges`. Isso não significava perda de estado do controller. O problema era simplesmente a ausência de:

```ts
this.charges.push(payment);
```

Esse bug de instrumentação reforça uma regra de debugging: validar se o mecanismo usado para observar o sistema está realmente registrando o evento antes de concluir que o estado desapareceu.

## Modelo mental adquirido

```text
Payments executa efeito colateral ✅
        ↓
resposta não chega a Orders ❌
        ↓
Orders vê apenas timeout
        ↓
retry
        ↓
mesma intenção é executada novamente 💀
```

Conclusão: timeout é ambíguo. `Não recebi resposta` não significa `a operação não aconteceu`.

Próximo conceito provocado pelo problema: **idempotência** — repetir a mesma intenção deve produzir apenas um efeito lógico.
