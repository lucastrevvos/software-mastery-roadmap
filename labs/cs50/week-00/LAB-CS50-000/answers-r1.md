R1-A — Recall cirúrgico

1. Sequencia segue uma linha numerica de instruções. O loop ele se repete até que cumpra sua condição. Sendo verdadeiro/falsa ou/e que o numero definido de repetições seja atingido.

2. a posição do bug caindo de cima pra baixo, pra não precisar repetir o mesmo codigo em todos os scripts e ate mesmo podendo receber por parametro um numero aleatorio, fazendo assim aparecer em qualquer parte do eixo x/y.

3. o evento é "quando a tecla de espaço for pressionada", esse é o evento que dispara a ação, e a ação que é "disparar um tiro", é ação executada ao evento anterior.

R1-B — Trace por estado de entrada e saída

iteração | score no INÍCIO | score < 2 ? | ramo executado | score no FIM
1 | 0| sim | if | 1
2 | 1| sim | if | 2
3 | 2| nao | else | 4
4 | 4| nao | else | 6

1. antes do if score = 2 por nao ser 2 menor que 2 ele vai para o else

R1-C — Rebuild, agora com estrutura

ESTADO INICIAL

- 0 (false)

MOVIMENTO DO JOGADOR

- quando pressionar seta para direita
- então move +x pixel

- quando pressionar seta para esquerda
- então move -x pixel

DISPARO

- quando pressionar space
- então efetuar ação de disparo

COLISÃO TIRO/BUG

- se tiro ocupar o mesmo espaço que bug
- então bug retorna para o topo
- então tiro se esconde
- então tiro retorna para posição inicial

VITÓRIA

- se pontos for maior ou igual a 20
- então mostrar msg de vitoria
- entao reiniciar o jogo

DERROTA

- se lives for menor ou igual a 0
- então mostrar evento de game over
- então reiniciar o jogo

RESTART COMPLETO

- setar todo estado para valores iniciais
- reinciar o jogo

R1-D — Repair por simulação

1. lifes nunca é subtraido com a colisões, logo game over nunca acontece

2. lifes chegar a 0

3. Given: lifes = 3
   When: lifes <= 0
   Then: game over

R1-E — Transfer: ciclo de vida do estado

evento | points | lives | speedBug | gameState
bug eliminado | muda|mantém | muda | mantem
perde uma vida | mantem| muda | mantem | mantem
restart completo | reseta| reseta | reseta|

1. points, lives, speedBug, gameState
2. todos os estados
