# LAB-CS50-000 — Review 04

**Tentativa revisada:** commit `0274b283ad29dcd16ea611d6b500d156b2c82606`  
**Status:** correção mínima — CPU mode  
**Modo:** Learning Mode

## O que a R3 mostrou

Você já sabe qual **deveria** ser a regra de vidas. O vazamento restante é outro: ao fazer tracing de código defeituoso, seu cérebro está substituindo a condição escrita pela condição desejada.

Nesta rodada, não pense em jogo, vidas, vitória ou derrota. Pense como uma CPU: **se a expressão é verdadeira e o bloco foi alcançado, a instrução dentro dele executa.**

## R4-A — CPU mode, sem domínio

Considere:

```text
x = 2
signal = true

if signal
    x = x - 1
    if x > 0
        output = "RED"
```

Preencha sem alterar o código:

```text
x antes do primeiro if =
signal é verdadeiro ou falso? =
entra no primeiro if? =
x depois de x = x - 1 =
x > 0 é verdadeiro ou falso? =
entra no segundo if? =
output final =
```

Agora troque somente:

```text
signal = false
```

Responda:

```text
x final =
`x > 0` chegou a ser avaliado? =
output recebeu "RED"? =
```

## R4-B — Tradução para o código de vidas

Sem corrigir a condição:

```text
health = 2
hit = true

if hit
    health = health - 1
    if health > 0
        game over
```

Preencha:

```text
health depois do decremento =
health > 0 é verdadeiro ou falso? =
o bloco `game over` executa no código ATUAL? =
```

Só depois escreva uma linha separada:

```text
REGRA DESEJADA PARA GAME OVER: ...
```

## R4-C — Restart exatamente igual ao estado inicial

Estado inicial:

```text
points = 0
lives = 3
speedBug = 1
gameState = "playing"
```

Antes do restart:

```text
points = 6
lives = 1
speedBug = 3
gameState = "playing"
```

Preencha o estado **depois do restart completo**:

```text
points =
lives =
speedBug =
gameState =
```

Depois responda em uma frase:

> O que significa dizer que um restart completo restaura o estado inicial?

## Entrega

Crie `answers-r4.md` sem alterar as tentativas anteriores.

```text
git add .
git commit -m "LAB-CS50-000 R4 enviado"
git push
```

No chat:

`LAB-CS50-000 R4 enviado`
