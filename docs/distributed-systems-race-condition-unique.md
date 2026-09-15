# Checkpoint — Race condition em idempotência persistente

## Experimento
Duas requisições HTTP concorrentes usaram o mesmo `orderId` (`44444444-4444-4444-4444-444444444444`). Um atraso artificial foi inserido entre o `SELECT` e o `INSERT` para ampliar a janela de corrida.

## Logs observados
```text
HTTP PAYMENT REQUEST: 44444444-4444-4444-4444-444444444444
PROCESS PAYMENT: 44444444-4444-4444-4444-444444444444
PAYMENT NOT FOUND - WAITING BEFORE INSERT: 44444444-4444-4444-4444-444444444444
HTTP PAYMENT REQUEST: 44444444-4444-4444-4444-444444444444
PROCESS PAYMENT: 44444444-4444-4444-4444-444444444444
PAYMENT NOT FOUND - WAITING BEFORE INSERT: 44444444-4444-4444-4444-444444444444
DB PAYMENT CREATED: d36ab67c-108a-4cb9-9555-074a01ee7314 44444444-4444-4444-4444-444444444444
ERROR: duplicate key value violates unique constraint "uq_payments_order_id"
PostgreSQL code: 23505
```

## Descoberta
O padrão `SELECT -> if not exists -> INSERT` não é atômico. Duas requisições podem executar o `SELECT` antes de qualquer uma inserir e ambas concluírem que a linha ainda não existe.

## O que protegeu o sistema
A constraint `UNIQUE(order_id)` foi a garantia final de integridade: apenas um registro foi persistido.

## Limitação atual
Embora os dados tenham ficado corretos, uma das requisições recebeu uma exceção de unicidade. Isso mostra a diferença entre proteger o banco e oferecer comportamento idempotente amigável ao cliente.

## Modelo mental
- `SELECT` prévio: otimização/atalho para detectar caso já existente.
- `UNIQUE`: garantia definitiva contra duplicidade.
- Concorrência: exige tratar atomicidade/conflito explicitamente.
- Código PostgreSQL `23505`: unique violation.

## Próximo experimento
Corrigir a corrida com uma operação atômica do PostgreSQL (`INSERT ... ON CONFLICT`) e comparar depois com `pg_advisory_xact_lock`, entendendo trade-offs de cada abordagem.
