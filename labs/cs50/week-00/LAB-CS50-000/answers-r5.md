R5-A — Breakpoint por linha

após linha 01: value = 5
após linha 02: value = 5 ; enabled = true
linha 03: condição = true ; entra? = sim
após linha 04: value = 3
linha 05: expressão = 3 >= 3; verdadeiro/falso = verdadeiro; entra? = sim
após linha 06: result = "GO"

value final = 5
a linha 04 executou? = nao
a linha 05 foi avaliada? = nao
a linha 06 executou? = nao
result recebeu "GO"? = nao

R5-B — Estado antes e depois de uma instrução

antes da linha 1: count = indefinido
após linha 1: count = 4
antes da linha 2: count = 4
após linha 2: count = 7
antes da linha 3: count = 7
após linha 3: count = 14

R5-C — Restart é uma restauração, não uma descrição

score = 0
lives = 2
speed = 1
mode = "playing"

antes do restart é o estado que se alterou durante o jogo e apos volta ao estado inicial

R5-D — Uma última borda lógica

B)

porque não a chances mais mais continuar o jogo, com vidas abaixo ou igual a zero
