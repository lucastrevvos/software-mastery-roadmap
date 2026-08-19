R2-A — Repair: execute o código, linha por linha

momento | lives antes | houve colisão? | lives depois | lives >= 0 ? | game over?
início | 3 | n | 3 | s | n
sem colisão | 3 | n | 3 | s |n
1ª colisão | 3 | s | 2 | s | n
2ª colisão | 2 | s | 1 | s |n
3ª colisão | 1 | s | 0 | s |s

1. nas 3 linhas de colisão
2. lives tem que ser menor ou igual a 0. if 2 >=0 nao deveria dar game over.
3. vidas menor ou igual a zero.

TESTE 1
Given: jogador inicia com 3 vidas
When: bug atinge servidor
Then: lives = 2 e game over = false

TESTE 2
Given: jogador possui 1 vida
When: bug atinge servidor
Then: lives = 0 e game over = true

R2-B — Rebuild: somente o que ficou faltando

ESTADO INICIAL
points = 0
lives = 3
speedBug = 3
gameState = 0

QUANDO TIRO ATINGE BUG

- points = points + 1
- bug = reseta posição
- tiro = reseta posição

R2-C — Transfer: ciclo de vida preciso

evento | points | lives | speedBug | gameState
bug eliminado #1 | 1 | 3 | 3 | 1
bug eliminado #2 | 2 | 3 | 3 | 1
bug eliminado #3 | 3 | 3 | 4 | 1
perde uma vida | 3 | 2 | 4 | 1
restart completo | 0 | 3 | 3 | 0

1. points, speedBug
2. points, lives, speedBug e o gameState
3. perder 1 vida resultaria no reinicio do game
