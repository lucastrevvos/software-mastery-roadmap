# LAB-CS50-000 — Review 05

**Tentativa revisada:** commit `18044f96a7e254437585204e0fdf2097508ab1d4`  
**Status:** guided execution worksheet  
**Modo:** Learning Mode

## Por que mudamos a estratégia

Na R4, o trecho com `health` finalmente foi executado literalmente: `health` virou `1`, `health > 0` foi reconhecido como verdadeiro e o bloco `game over` foi considerado executado. Isso foi avanço real.

O problema reapareceu no exemplo neutro: `x` foi tratado como `1` **antes** da linha `x = x - 1` executar. Depois, mesmo marcando que o segundo `if` não seria executado, `output` acabou recebendo `"RED"`. No restart, o estado anterior ao restart foi copiado em vez de restaurar o estado inicial.

A partir de agora, use esta regra mecânica:

> **Uma variável só muda quando a linha que a altera é executada.**

E esta segunda:

> **Uma instrução dentro de um bloco só executa se o fluxo realmente alcançar esse bloco.**

## Exemplo resolvido — pense como um debugger

```text
01  x = 2
02  signal = true
03  if signal
04      x = x - 1
05      if x > 0
06          output = "RED"
```

Execução:

```text
após linha 01: x = 2
após linha 02: x = 2, signal = true
linha 03: true → entra
após linha 04: x = 1
linha 05: 1 > 0 → true → entra
após linha 06: output = "RED"
```

Observe: `x` não vira `1` antes da linha 04. E `output` só recebe `"RED"` porque a linha 06 foi alcançada.

---

# Reteste R5

Crie `answers-r5.md`.

## R5-A — Breakpoint por linha

Execute exatamente:

```text
01  value = 5
02  enabled = true
03  if enabled
04      value = value - 2
05      if value >= 3
06          result = "GO"
```

Preencha **uma linha de cada vez**:

```text
após linha 01: value =
após linha 02: value = ; enabled =
linha 03: condição = ; entra? =
após linha 04: value =
linha 05: expressão = ; verdadeiro/falso = ; entra? =
após linha 06: result =
```

Agora execute o mesmo código mudando apenas:

```text
enabled = false
```

Responda:

```text
value final =
a linha 04 executou? =
a linha 05 foi avaliada? =
a linha 06 executou? =
result recebeu "GO"? =
```

## R5-B — Estado antes e depois de uma instrução

```text
count = 4
count = count + 3
count = count * 2
```

Preencha:

```text
antes da linha 1: count = indefinido
após linha 1: count =
antes da linha 2: count =
após linha 2: count =
antes da linha 3: count =
após linha 3: count =
```

## R5-C — Restart é uma restauração, não uma descrição

Estado inicial:

```text
score = 0
lives = 2
speed = 1
mode = "playing"
```

Estado imediatamente antes do restart:

```text
score = 8
lives = 1
speed = 4
mode = "paused"
```

Depois de **restart completo**, preencha:

```text
score =
lives =
speed =
mode =
```

Em uma frase, explique a diferença entre **estado antes do restart** e **estado depois do restart**.

## R5-D — Uma última borda lógica

Num sistema em que `health = 0` significa **nenhuma vida restante**, escolha a regra correta para `game over` e explique em uma frase:

```text
A) health < 0
B) health <= 0
C) health > 0
```

## Entrega

```text
git add .
git commit -m "LAB-CS50-000 R5 enviado"
git push
```

No chat:

`LAB-CS50-000 R5 enviado`
