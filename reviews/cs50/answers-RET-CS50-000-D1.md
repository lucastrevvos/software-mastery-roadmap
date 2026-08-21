A — Recall

1. uma variavel que altera o estado da aplicação.
2. o evento é a emissão da mensagem permitindo ao não ação que esta relacionada com ele.
3. uma condição inversa a sua inicial.
4. criar um bloco com aquelas instruções que podem ser reaproveitadas posteriormente, recebendo ou não parametros.

B — Trace sem scaffolding

value final = 4
a condição value >= 4 foi avaliada? = sim
status recebeu "READY"? = sim

value final = 6
a condição value >= 4 foi avaliada? = nao
status recebeu "READY"? = nao

C — Estado antes/depois

5
15
15

D — Debug: comportamento real × comportamento desejado

1. ele entra no hit pois é true, health recebe 1 pois 2 - 1 = 1
   ele entra no segundo if pois 1 > 0
   encerrando o gameOver = true

2. encerrar o game
3. if health <= 0

E — Restart completo

score = 0
lives = 3
speed = 1
mode = "playing"

F — Transferência

estado final = "stopped" a terceira falha a errors ser >= 3
