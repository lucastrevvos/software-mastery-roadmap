Reteste R3

health final = 2
`health > 0` foi avaliado? = sim
game over? = nao

health antes = 2
health depois = 1
`health > 0` = verdadeiro ou falso? verdadeiro
game over? = não

1. nunca
2. quando as vidas chegam a 0
3. reiniciaria os estados

R3-B — Estado sem transições mágicas

evento | points | lives | speedBug | gameState
bug #1 eliminado | 1 | 3 | 1 | playning
bug #2 eliminado | 2 | 3 | 1 | playning
bug #3 eliminado | 3 | 3 | 2 | playning
perde uma vida | 3 | 2 | 2 | playning
restart completo | 0 | 3 | 1 | 0

porque com relação o que muda o estado do game são os estados de lives e points
