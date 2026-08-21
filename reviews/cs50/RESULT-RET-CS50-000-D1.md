# RESULT — RET-CS50-000-D1

**Origem:** `LAB-CS50-000`  
**Revisão prevista:** 2026-08-20  
**Revisão realizada:** 2026-08-21  
**Commit avaliado:** `0dd2f090e02a985308a35cad444be5725ed2a7b7`  
**Resultado:** retenção parcial

## Retido

- Fluxo condicional aninhado: os ramos com condição verdadeira e falsa foram executados literalmente.
- Debugging comportamento real × comportamento desejado: o código defeituoso de `health` foi interpretado corretamente e a condição desejada `health <= 0` foi recuperada.
- Restart completo: o estado voltou exatamente aos valores iniciais.
- Abstração em bloco/função: conceito recuperado corretamente.

## Vazamentos reabertos

### `ERR-CS50-000-001` — estado antes/depois

Para:

```text
count = 3
count = count + 2
count = count * 3
```

a resposta foi `5, 15, 15`. O estado correto imediatamente após cada linha é `3, 5, 15`.

### `ERR-CS50-000-004` — modelo de loop

A resposta de Recall não recuperou com precisão a ideia de uma regra/condição de parada que possa ser atingida e da progressão necessária do estado de controle.

## Parcial

- Evento × ação: a resposta de Recall ficou semanticamente imprecisa; será retestada sem abrir uma nova entrada no Error Ledger por enquanto.
- Transferência: foi identificado corretamente que a terceira falha muda `mode` para `stopped`, mas o estado final completo (`itemsProcessed=2`, `errors=3`, `mode="stopped"`) não foi informado.

## Próximo gate

`RET-CS50-000-D3`, reancorado para **2026-08-24** por a revisão D+1 ter sido executada um dia após a data prevista.

O próximo gate deve priorizar os vazamentos reabertos, com spot-checks curtos dos conceitos já retidos.
