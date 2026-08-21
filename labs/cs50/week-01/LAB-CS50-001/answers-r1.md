R1-A — Build pipeline

hello.c = arquivo de codigo fonte
make = ferramenta de automação que decido como e quando chamar o compilador
compilador (ex.: clang/gcc) = o tradutor, ferramenta que converte o texto em C para linguagem de maquina
executável gerado = arquivo binario final. o programa que o SO consegue rodar diretamente

Efetivamente é o compilador. O outro é o maestro que decide como chamar o compilador.

R1-B — Integer division antes da atribuição

1. 2.0
2. na divisão 11/4
3. pq a operação do lado direito acontece primeiro. antes do resultado ser guardado na variavel. então primeiro ele descarta e só dps que o valor 2 é atribuido para double.

double average = (double)total / people

double total = 11;
int people = 4;
double average = total / people;

saida: 3.5

R1-C — Tipos e conversão

Caso 1

Um integer overflow. Valor fora da faixa de destino

Caso 2

A variavel x recebe 3.0 inves de 3.5 a operação ocorre em numeros inteiros, a conversao em double só acontece dps da divisao ja ter descartado o resto.

- divisao inteira antes da conversao

Caso 3

a variavel whole recebe o valor de 19. ao atribuir um floot a uma variavel int, a linguagem faz um truncamento explicito. E descarta tudo que vem apos a virgula

- Perda de parte fracionaria

R1-D — Evidência de teste do Rebuild

entrada / sequência | quantidade de dígitos | soma dos dígitos | passou?
7 | 1 | 7 | sim
4827 | 4 | 21 | sim
1000 | 4 | 1 | sim
-5 e depois 42 | 2 | 6 | sim

-5 produziu o erro esperado.

- O compilador apenas garante a correção sintatica e estrutural do codigo.
  Testes garantem a logica de negocio, assegurnadop que o programa produz as saidas corretas diante s validações de entrada e diferentes limites

R1-E — Dinheiro sem ponto flutuante

tipo escolhido = long
valor inteiro realmente armazenado em centavos =987654321
como obter a parte de reais = Dividindo por 100 com divisão inteira: valor / 100 (resulta em 9876543)
como obter os dois dígitos de centavos = Pegando o resto da divisão por 100: valor % 100 (resulta em 21)
qual erro evitamos ao não usar float/double para o valor monetário interno =Erro de imprecisão binária em ponto flutuante (onde dízimas em base 2 acumulam pequenos arredondamentos e causam perda ou ganho involuntário de centavos).
