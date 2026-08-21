## R2-A — Aritmética versus conversão

Cenário 1 (Soma que excede o limite):

há operação aritmética? = Sim (soma de dois valores)

há conversão de tipo? = Não (os operandos e o resultado permanecem no mesmo tipo)

qual é o fenômeno principal? = Integer Overflow (estouro de inteiro por operação aritmética)

por que os dois casos não devem receber exatamente o mesmo nome? = Ocorre durante uma instrução de cálculo da CPU quando a operação estoura a capacidade do registrador/tipo original, alterando o resultado matemático.

Cenário 2 (Atribuição de long para int):

há operação aritmética? = Não (apenas cópia/atribuição de valor)

há conversão de tipo? = Sim (conversão implícita estreitante / narrowing conversion)

qual é o fenômeno principal? = Narrowing / Truncamento de bits por conversão de tipo

por que os dois casos não devem receber exatamente o mesmo nome? = Ocorre no momento da atribuição entre tipos de tamanhos diferentes, onde o compilador descarta os bits superiores para ajustar a largura de memória, sem que nenhuma conta tenha sido feita.

## R2-B — Implícito versus explícito

1. A atribuição int a = price;. O compilador converte o tipo double para int automaticamente, sem intervenção do programador.

2. A atribuição int b = (int) price;. O operador (int) indica explicitamente ao compilador a intenção de converter o valor.

3. O valor 19 chega em ambas as variáveis.

4. A parte fracionária (.99) é inteiramente descartada por truncamento. O C não faz arredondamento (como arredondar para 20); ele simplesmente elimina tudo o que vem após a vírgula.

5. Não. O cast explícito apenas força a conversão e "sinaliza" ao compilador que você assume o risco da operação, mas ele não altera os limites de memória do tipo de destino. Se o valor do tipo original estiver fora do intervalo suportado pelo tipo de destino (por exemplo, fazer (int) 3000000000.0 para um int de 32 bits), ocorrerá truncamento de bits e o resultado será incorreto (estouro/overflow).

## R2-C — Fechamento do Repair

previsão =
1
2
3
average: 3.5

saída real =
1
2
3
average: 3.5

divergiu? = não

por que average agora preserva 3.5? = Porque a variável `total` foi declarada como `double`. Na operação `total / people`, o C promove automaticamente o inteiro `people` para ponto flutuante antes de realizar a divisão, executando uma divisão de ponto flutuante ($7.0 \div 2.0 = 3.5$) em vez de uma divisão inteira.
