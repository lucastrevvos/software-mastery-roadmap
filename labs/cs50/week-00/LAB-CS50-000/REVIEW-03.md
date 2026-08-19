# LAB-CS50-000 — Review 03

**Tentativa revisada:** commit `d6fd21eb13caacf1a38a6c20a94d798b5b03ef8a`  
**Status:** microaula + reteste curto  
**Modo:** Learning Mode

## O que a R2 fechou

- ✅ **Rebuild / estado inicial:** agora `points`, `lives`, `speedBug` e `gameState` nascem explicitamente definidos.
- ✅ **Colisão tiro/bug:** a pontuação é atualizada e os objetos envolvidos têm transições explícitas.
- ✅ **Regra de velocidade:** você representou corretamente aumento somente na 3ª eliminação.
- ✅ **Persistência parcial:** `points` e `speedBug` foram preservados quando uma vida é perdida.
- 🔴 **Execução literal do código:** o bug original ainda foi simulado como se já estivesse corrigido.
- 🟡 **gameState:** houve uma transição de `0` para `1` após a primeira eliminação sem existir uma regra que justificasse essa mudança.

## Microaula — primeiro execute, depois conserte

Debugging tem duas perguntas diferentes:

1. **O que este código realmente faz?**
2. **O que ele deveria fazer?**

Nunca misture as duas durante o tracing.

Considere este exemplo diferente:

```text
coins = 2

if player touches trap
    coins = coins - 1
    if coins >= 0
        show "blocked"
```

Se `player touches trap` for falso, o programa não entra nesse bloco: `coins = coins - 1` não executa e o `if coins >= 0` interno também **não é avaliado**.

Se `player touches trap` for verdadeiro, o programa executa cada linha na ordem. Depois de decrementar, ele testa exatamente a condição que está escrita. Não importa ainda se essa condição faz sentido para a regra do jogo.

O protocolo de debugging será sempre:

```text
TRACE CURRENT CODE
↓
OBSERVE ACTUAL BEHAVIOR
↓
COMPARE WITH EXPECTED BEHAVIOR
↓
FORM HYPOTHESIS
↓
CHANGE CODE
↓
TEST AGAIN
```

### Estado e eventos

Uma variável só deve mudar quando alguma regra do sistema manda mudá-la.

Exemplo: se `gameState = "playing"`, eliminar um bug não muda automaticamente o estado do jogo. Ele continua `"playing"` enquanto não acontecer uma condição de vitória, derrota, pausa etc.

Da mesma forma, **perder uma vida** é uma transição parcial. **Restart completo** é outra operação, que restaura todo o estado inicial.

---

# Reteste R3

Crie `answers-r3.md`.

## R3-A — Execute código que está errado sem corrigi-lo

```text
health = 2

if enemy hits player
    health = health - 1
    if health > 0
        game over
```

### Cenário 1 — nenhum ataque

Preencha:

```text
health final =
`health > 0` foi avaliado? =
game over? =
```

### Cenário 2 — primeiro ataque

Preencha:

```text
health antes =
health depois =
`health > 0` = verdadeiro ou falso?
game over? =
```

Depois responda separadamente:

1. **Comportamento real do código:** quando ocorre `game over`?
2. **Comportamento desejado:** quando deveria ocorrer `game over` num sistema normal de vidas?
3. Qual alteração lógica você faria **depois** de terminar o tracing?

## R3-B — Estado sem transições mágicas

Estado inicial:

```text
points = 0
lives = 3
speedBug = 1
gameState = "playing"
```

Regras:

- eliminar um bug: `points + 1`;
- a cada 3 eliminações: `speedBug + 1`;
- perder uma vida: `lives - 1`;
- enquanto `lives > 0` e `points < 10`, `gameState` continua `"playing"`;
- `points >= 10` → `gameState = "won"`;
- `lives <= 0` → `gameState = "lost"`;
- restart completo → volta exatamente ao estado inicial.

Preencha:

```text
evento              | points | lives | speedBug | gameState
bug #1 eliminado     |        |       |          |
bug #2 eliminado     |        |       |          |
bug #3 eliminado     |        |       |          |
perde uma vida       |        |       |          |
restart completo     |        |       |          |
```

Depois responda:

> Por que `gameState` não deve mudar só porque um bug foi eliminado?

## Entrega

```text
git add .
git commit -m "LAB-CS50-000 R3 enviado"
git push
```

No chat:

`LAB-CS50-000 R3 enviado`
