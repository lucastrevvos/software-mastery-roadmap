R4-A — CPU mode, sem domínio

x antes do primeiro if = 1
signal é verdadeiro ou falso? = verdadeiro
entra no primeiro if? = sim
x depois de x = x - 1 = 0
x > 0 é verdadeiro ou falso? = falso
entra no segundo if? = nao
output final = "RED"

x final = 2
`x > 0` chegou a ser avaliado? = nao
output recebeu "RED"? = nao

R4-B — Tradução para o código de vidas

health depois do decremento = 1
health > 0 é verdadeiro ou falso? = verdadeiro
o bloco `game over` executa no código ATUAL? = sim

REGRA DESEJADA PARA GAME OVER: health < 0 assim o jogo continuaria pq ele ainda tem vida =)

R4-C — Restart exatamente igual ao estado inicial

points = 6
lives = 1
speedBug = 3
gameState = "playing"

eles retornam para o estado que foram inicializados
