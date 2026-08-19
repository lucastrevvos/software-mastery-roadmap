# LAB-CS50-000 — Review 01

**Tentativa revisada:** commit `2f08b6245da9cc4cc6ef73adc055a7ed07986afa`  
**Status:** correção necessária  
**Modo:** Learning Mode — sem consultar solução pronta

## Resultado da tentativa 1

| Dimensão | Estado | Observação |
|---|---|---|
| Recall | 🟡 Parcial | fundamentos reconhecidos, mas alguns modelos mentais ainda estão imprecisos |
| Trace | 🟡 Parcial | sequência final correta; explicação do estado na 3ª iteração precisa ser corrigida |
| Rebuild | 🔴 Pendente | não executado |
| Repair | 🟡 Parcial | direção da condição foi identificada, mas o fluxo aninhado e o teste não foram modelados |
| Transfer | 🟡 Parcial | estados principais identificados; falta separar claramente reset parcial de reset completo |

## O que já está firme

- Você reconhece algoritmo, condição e variável em nível introdutório.
- No tracing, chegou à sequência `1 → 2 → 4 → 6` e ao valor final `6`.
- Percebeu que a condição de `game over` do exercício de Repair está logicamente errada.
- Na transferência, identificou estados relevantes como `points`, `speedBug`, `lives` e `gameState`.

## Rodada R1

Crie **`answers-r1.md`** nesta mesma pasta. Não altere `answers.md`; queremos preservar a tentativa original como evidência.

### R1-A — Recall cirúrgico

Responda novamente apenas estas questões:

1. **Loop:** sua resposta disse que um loop se repete até uma instrução ficar verdadeira/falsa. Mas o laboratório tinha `repeat 4 times`. Reescreva a diferença entre **sequência** e **loop** de uma forma que também explique esse caso.
2. **Abstração:** explique o que estamos escondendo/simplificando quando criamos um bloco ou função. Dê um exemplo concreto inspirado no Bug vs Developer.
3. **Evento x ação:** considere a frase: `quando a tecla de espaço for pressionada → disparar um tiro`. Explique qual parte representa o evento e qual representa a ação, e por quê.

### R1-B — Trace por estado de entrada e saída

Sua sequência `1, 2, 4, 6` está correta. O problema está na explicação da terceira iteração.

Sem mudar a sequência, preencha:

```text
iteração | score no INÍCIO | score < 2 ? | ramo executado | score no FIM
1        |                 |             |                |
2        |                 |             |                |
3        |                 |             |                |
4        |                 |             |                |
```

Depois responda:

> Qual é exatamente o valor de `score` **antes** do `if` na terceira iteração, e por que isso escolhe aquele ramo?

### R1-C — Rebuild, agora com estrutura

O objetivo não é lembrar os blocos exatos do Scratch. Quero verificar se você consegue decompor o jogo.

Escreva pseudocódigo usando **somente esta estrutura**:

```text
ESTADO INICIAL
- ...

MOVIMENTO DO JOGADOR
- quando ...
- então ...

DISPARO
- quando ...
- então ...

COLISÃO TIRO/BUG
- se ...
- então ...

VITÓRIA
- se ...
- então ...

DERROTA
- se ...
- então ...

RESTART COMPLETO
- ...
```

Não precisa implementar em JavaScript nesta rodada. Primeiro quero validar seu modelo de fluxo.

### R1-D — Repair por simulação

Não responda apenas com o operador correto. Simule o código original:

```text
início: lives = 3
sem colisão: lives = ? / game over acontece?
1ª colisão: lives = ? / lives >= 0 é ? / game over acontece?
2ª colisão: lives = ? / lives >= 0 é ? / game over acontece?
3ª colisão: lives = ? / lives >= 0 é ? / game over acontece?
```

Depois escreva:

1. Qual é o comportamento incorreto real?
2. Qual deve ser a regra conceitual para ocorrer `game over`?
3. Crie **um caso de teste** no formato:

```text
Given: ...
When: ...
Then: ...
```

### R1-E — Transfer: ciclo de vida do estado

Preencha a tabela dizendo `muda`, `mantém` ou `reseta` e, quando mudar, diga como:

```text
evento             | points | lives | speedBug | gameState
bug eliminado       |        |       |          |
perde uma vida      |        |       |          |
restart completo    |        |       |          |
```

Depois responda em uma frase para cada uma:

1. O que **não pode resetar** quando perde apenas uma vida?
2. O que **deve resetar** no restart completo?

## Entrega R1

1. Crie `answers-r1.md`.
2. Responda somente aos itens acima.
3. Commit e push.
4. No chat, informe apenas:

`LAB-CS50-000 R1 enviado`

Se a R1 fechar os vazamentos, o baseline será aprovado e entraremos na primeira revisão espaçada. Se algum modelo ainda estiver instável, faremos uma correção ainda mais curta e específica.