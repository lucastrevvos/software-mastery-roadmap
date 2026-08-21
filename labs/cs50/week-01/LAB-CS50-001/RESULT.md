# LAB-CS50-001 — Resultado do baseline

**Fonte:** CS50 Week 1 — C + Problem Set 1  
**Baseline concluído em:** 2026-08-21  
**Commit final:** `48fa9acaf7117cbb2838b1ced378b88a19aecb4f`  
**Status:** PASS — retenção pendente

## Resultado por dimensão

- Recall: pass
- Trace: pass
- Rebuild: pass
- Repair: pass
- Transfer: pass

## Evidências principais

- `digitstats.c` reconstruído do zero com `long`, `%`, divisão inteira, `do/while` e `while`.
- Tracing de `for` e condicionais executado corretamente.
- Bugs de atribuição em condição, direção do loop e divisão inteira no cálculo de média identificados/corrigidos ao longo das rodadas.
- `make`, compilador, código-fonte e executável foram separados conceitualmente.
- Divisão inteira antes da atribuição a `float`/`double` foi compreendida e corrigida.
- Conversão implícita e cast explícito foram distinguidos.
- Dinheiro foi modelado em centavos inteiros para evitar imprecisão binária de ponto flutuante.
- Casos de teste do Rebuild foram executados e registrados.

## Histórico

1. Tentativa inicial — `03625d70185e5ef593f42ba2f452e83118ffa8e3`: baseline parcial.
2. R1 — `d1e911e371d7ab645fc4e813b73bf6e92dddd56d`: fechou build pipeline, divisão inteira, testes e representação monetária.
3. R2 — `48fa9acaf7117cbb2838b1ced378b88a19aecb4f`: fechou a distinção entre overflow aritmético, conversão estreitante, conversão implícita e cast explícito.

## Nota de precisão futura

No nível exigido pela Week 1, o modelo de conversão ficou suficiente para o baseline. Em C portátil, porém, valores fora da faixa do tipo de destino não devem ser modelados genericamente como “o compilador simplesmente descarta bits”. O comportamento exato depende da categoria de conversão e das regras da linguagem. Essa precisão será refinada em conteúdo futuro, sem manter o baseline aberto por isso.

## Próximo gate

`RET-CS50-001-D1` — revisão espaçada D+1 em 2026-08-22.
