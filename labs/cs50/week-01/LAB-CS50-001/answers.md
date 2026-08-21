A — RECALL

1. sc code é o codigo que produzimos para a maquina entender o algoritmo. mc é o codigo compilado que ela produz.
2. compila para linguagem de baixo nivel que realmente sera executado pelo programa.
3. sim, ele é o comando que mostra ao compilador qual arquivo deve executar
4. = atribui valor. == compara valores
5. criar uma variavel que deve permanecer constante
6. valores que serão armazenados, convertidos em uma variavel de um tipo menor, ira dar erro de execução.
7. é um erro de computação que acontece quando um programa tenta armazenar em uma variável inteira um número maior do que o limite máximo de memória alocado para aquele tipo de dado.
8. O número $0{,}1$ não é representado exatamente porque ele vira uma dízima periódica em binário, e como o padrão IEEE 754 tem um número fixo de bits, ele arredonda a dízima, gerando uma pequena imprecisão.
9. o loop controlado por condição é executado ate que aquela condição seja falsa. já o por contagem, terminado ao atingir o resultado esperado.
10. retorna o que sobra da divisão. É ultimo para poder percorrer os numeros par ou impar, 1 por vez, se tem sobra ou nao.

B — TRACE

iteração | i | x no início | condição i % 2 == 0 | operação | x no fim
0 | 0 | 3 | 0 | 3 + 0 | 3
1 | 1 | 3 | 1 | 3 - 1 | 2
2 | 2 | 2 | 0 | 2 + 2 | 4
3 | 3 | 4 | 1 | 4 - 1 | 3

1. 3
2. 4
3. 3
4. executaria mais uma vez, mudando o valor final de X

C — REBUILD

ALGORITMO Digitstats

VAR
numero, temp: INTEIRO_LONGO
qtd_digitos, soma_digitos, ultimo_digito: INTEIRO

INICIO

    FAÇA
        ESCREVA("Digite um numero inteiro positivo: ")
        LEIA(numero)

        SE (numero <= 0) ENTÃO
            ESCREVA("Número invalido! Digite apenas valores maiores que zero.\n")
        FIM_SE
    ENQUANTO (numero <= 0)

    qtd_digitos <- 0
    soma_digitos <- 0
    temp <- numero

    ENQUANTO (temp > 0) FAÇA
        ultimo_digito <- temp % 10
        soma_digitos <- soma_digitos + ultimo_digito
        qtd_digitos <- qtd_digitos + 1

        temp <- temp / 10
    FIM_ENQUANTO

    ESCREVA("Quantidade de digitos: ", qtd_digitos)
    ESCREVA("Soma dos digitos: ", soma_digitos)

FIM

D — REPAIR

1. o score em if esta recebendo o valor 10 e não comparando com 10.
   no for o I começa com 1 e a da loop reduz, ficando infinitamente, pois sempre sera menor que 3.

2. feito, deu erro.

3. score valor 10 sendo reatribuido dentro de if.
   i sendo decrementando, causando um loop infinito no for.

4. feito.

5. feito.

6. 1
   2
   3
   average: 3.0

contou de 1 a 3 e fez a media 7/2 sendo = 3. Mas comno é float e pedido pra retonar apenas o valor arredondado pra baixo.
Já expliquei acima pq esta correto.

E — TRANSFER

1. long
2. divido por 100 para mostrar as casas decimais para os reais e Mod % 100 para os centavos
3. Ela elimina completamente o erro de representação em ponto flutuante (imprecisão binária).O problema do float e do double:Computadores usam base binária (base 2). Números decimais simples como $0{,}10$ ou $0{,}01$ não possuem representação exata em binário e viram dízimas periódicas binárias. Ao somar ou subtrair valores em float/double, esses pequenos erros de arredondamento se acumulam, gerando resultados bizarros como 9876543.2100000009 ou perdas de centavos em cálculos financeiros.Por que int não é o ideal?Em um sistema de 32 bits (ou no padrão C em muitas arquiteturas), o tipo int tem limite máximo de $2.147.483.647$. Em centavos, isso representa apenas cerca de R$ 21,4 milhões. Qualquer soma que ultrapasse esse teto causará estouro de memória (overflow).A vantagem do long:Com operações puramente inteiras (long ou long long), cada centavo é uma unidade discreta exata. $1 + 1$ sempre será $2$, garantindo precisão matemática absoluta sem dependência de arredondamentos de hardware.

E2 — overflow

O otimizador do compilador é enganado: Como a linguagem C assume que um estouro nunca deveria acontecer, o compilador pode achar que um teste de segurança como if (x + 1 < x) é impossível e apagar essa verificação do programa final.

Falha de segurança e memória: Se essa variável x definir o tamanho de um espaço na memória (como uma lista ou vetor), o sistema pode alocar um espaço minúsculo por erro e tentar gravar muitos dados ali, gerando um Buffer Overflow (uma das brechas mais graves para invasões).

E3 — divisão

1. 3.0

2. converter para float antes de dividir ou fazer a divisão por 2 numeros float.

E4 — escolha de loop

1. do while - pq se trata de uma validação de entrada. Preciso executar o codigo ao menos uma vez para verificar se a condição esta correta

2. for - o numero de repetições é conhecido previamente.

3. while - é uma repetição baseada sem contagem fixa. em que o numero pode começar valendo 0 ou já estar processado de inicio. Garantindo que se o numero inicial nao atender o requisito ele nem começa.
