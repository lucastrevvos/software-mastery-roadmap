# LAB-CS50-000 — Review 02

**Tentativa revisada:** commit `fe44f3eee057856a097746ddcffa7697f39a4cc4`  
**Status:** correção curta necessária  
**Modo:** Learning Mode — sem consultar solução pronta

## O que a R1 fechou

- ✅ **Loop:** agora o modelo cobre repetição por contagem e por condição.
- ✅ **Abstração:** você reconheceu encapsulamento/reuso e uso de parâmetro.
- ✅ **Evento x ação:** distinção correta no exemplo do disparo.
- ✅ **Trace:** estado de entrada/saída corrigido; a 3ª iteração começa com `score = 2`.
- 🟡 **Rebuild:** a estrutura geral apareceu, mas o estado inicial e a atualização da pontuação ainda não estão explícitos.
- 🔴 **Repair:** a simulação pedida não foi executada e o código foi lido como se `lives` não fosse decrementado.
- 🟡 **Transfer:** ainda falta modelar precisamente quando a velocidade muda e o que persiste ao perder apenas uma vida.

## R2-A — Repair: execute o código, linha por linha

Use **o código original**, sem corrigir nada antes da simulação:

```text
when game starts
    lives = 3

forever
    if bug touches server
        lives = lives - 1
        if lives >= 0
            game over
```

Preencha exatamente:

```text
momento       | lives antes | houve colisão? | lives depois | lives >= 0 ? | game over?
início        |             |                |              |              |
sem colisão   |             |                |              |              |
1ª colisão    |             |                |              |              |
2ª colisão    |             |                |              |              |
3ª colisão    |             |                |              |              |
```

Depois responda:

1. Em qual linha `lives` é alterado?
2. Qual é o comportamento incorreto real do programa?
3. Em palavras, qual deve ser a regra para decidir se acabou o jogo?

Crie **dois testes**, um caso não-terminal e um caso terminal:

```text
TESTE 1
Given: ...
When: ...
Then: lives = ... e game over ...

TESTE 2
Given: ...
When: ...
Then: lives = ... e game over ...
```

## R2-B — Rebuild: somente o que ficou faltando

Não reescreva o jogo inteiro. Complete apenas:

```text
ESTADO INICIAL
points = ...
lives = ...
speedBug = ...
gameState = ...

QUANDO TIRO ATINGE BUG
- points ...
- bug ...
- tiro ...
```

Os valores podem ser os que você escolher; quero verificar se todo estado relevante nasce definido e se a colisão produz todas as mudanças necessárias.

## R2-C — Transfer: ciclo de vida preciso

Regra do problema:

- vence ao eliminar 10 bugs;
- a velocidade aumenta **a cada 3 eliminações**;
- perder uma vida **não** volta a velocidade ao valor inicial;
- restart completo volta o jogo ao estado inicial.

Preencha com `muda`, `mantém` ou `reseta`. Quando disser `muda`, diga **como**.

```text
evento               | points | lives | speedBug | gameState
bug eliminado #1      |        |       |          |
bug eliminado #2      |        |       |          |
bug eliminado #3      |        |       |          |
perde uma vida        |        |       |          |
restart completo      |        |       |          |
```

Depois responda:

1. Quais estados precisam sobreviver à perda de uma vida?
2. Quais estados devem voltar ao valor inicial no restart completo?
3. Por que tratar `perder uma vida` e `restart completo` como a mesma operação criaria bug?

## Entrega R2

Crie `answers-r2.md` nesta pasta, sem alterar as tentativas anteriores.

Depois:

```text
git add .
git commit -m "LAB-CS50-000 R2 enviado"
git push
```

No chat informe apenas:

`LAB-CS50-000 R2 enviado`

Se estes pontos fecharem, o baseline é aprovado e o próximo contato com esses fundamentos será uma revisão espaçada, não outra correção imediata.
