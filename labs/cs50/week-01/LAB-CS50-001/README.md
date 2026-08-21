# LAB-CS50-001 — CS50 Week 1 / C

**Fonte:** CS50x 2026 — Week 1 C + Problem Set 1  
**Modo:** Learning Mode  
**Objetivo:** medir se os fundamentos da Week 1 estão disponíveis sem depender do enunciado do CS50, de exemplos prontos ou de copiar soluções anteriores.

> Curso concluído não significa domínio. Este lab mede Recall, Trace, Rebuild, Repair e Transfer.

## Regras

- Não consulte soluções do PSet 1, suas submissões anteriores ou respostas de IA durante a primeira tentativa.
- Pode usar `man`, `help50`, compilador e mensagens de erro **somente quando a seção permitir**.
- Antes de executar qualquer trecho de tracing, escreva sua previsão.
- Não use arrays, ponteiros, strings manipuladas manualmente ou conteúdo da Week 2 em diante.
- Preserve esta primeira tentativa; correções futuras irão para arquivos separados.

Crie `answers.md` para A, B e E. Crie os programas pedidos em `src/`.

---

## A — RECALL

Sem consultar material, responda em 1–3 frases cada:

1. Qual a diferença entre **source code** e **machine code**?
2. O que um compilador faz entre esses dois estados?
3. O comando `make hello` é o compilador? Explique o papel de `make` nesse fluxo.
4. Diferencie `=` de `==` em C.
5. Para que serve `const`?
6. Dê um exemplo de situação em que escolher `int`, `long`, `float` ou `double` muda a correção do programa.
7. O que é **integer overflow**?
8. Por que números decimais como `0.1` podem não ser representados exatamente por ponto flutuante?
9. Qual a diferença conceitual entre um loop controlado por condição e um loop controlado por contagem?
10. O que `%` faz quando aplicado a inteiros e por que ele é útil em problemas como Credit?

---

## B — TRACE

**Não rode antes de prever.**

```c
#include <stdio.h>

int main(void)
{
    int x = 3;

    for (int i = 0; i < 4; i++)
    {
        if (i % 2 == 0)
        {
            x = x + i;
        }
        else
        {
            x = x - 1;
        }
    }

    printf("%i\n", x);
}
```

Monte a tabela:

```text
iteração | i | x no início | condição i % 2 == 0 | operação | x no fim
0        |   |             |                      |          |
1        |   |             |                      |          |
2        |   |             |                      |          |
3        |   |             |                      |          |
```

Depois responda:

- Qual valor será impresso?
- Quantas vezes o corpo do `for` executa?
- Qual é o valor de `i` quando o loop termina de executar seu último corpo?
- Sem executar: o que mudaria se a condição fosse `i <= 4`?

Só depois compile um arquivo temporário para conferir sua previsão e registre se houve divergência.

---

## C — REBUILD

Do editor vazio, crie:

```text
src/digitstats.c
```

O programa deve:

1. pedir um inteiro positivo do tipo `long`;
2. rejeitar `0` e negativos, perguntando novamente;
3. calcular **sem converter para string**:
   - quantidade de dígitos;
   - soma dos dígitos;
4. imprimir os dois resultados.

Exemplo conceitual:

```text
input: 4827
quantidade de dígitos: 4
soma dos dígitos: 21
```

Restrições:

- sem arrays;
- sem strings para decompor o número;
- use divisão inteira e `%`;
- o programa precisa funcionar também para um número de um dígito.

Antes de codar, escreva em `answers.md` um pseudocódigo de no máximo 8 linhas.

Compile com warnings habilitados:

```bash
gcc -Wall -Wextra -Werror src/digitstats.c -o digitstats
```

Registre pelo menos 4 casos de teste, incluindo uma entrada inválida.

---

## D — REPAIR

O arquivo `broken.c` deste laboratório contém bugs de fluxo, comparação e aritmética.

Procedimento obrigatório:

1. **Antes de editar**, leia o código e escreva em `answers.md` o comportamento que você prevê.
2. Compile e execute.
3. Liste cada bug separadamente: sintoma → causa → correção.
4. Corrija `broken.c` sem reescrever o programa inteiro.
5. Compile com:

```bash
gcc -Wall -Wextra -Werror broken.c -o broken
```

6. Registre a saída final e explique por que agora ela está correta.

---

## E — TRANSFER

Responda sem pesquisar primeiro:

### E1 — dinheiro

Você precisa representar internamente **R$ 9.876.543,21** e fazer somas/subtrações exatas de centavos.

- Você escolheria `float`, `double`, `int` ou `long`?
- Como representaria o valor?
- Por que sua escolha reduz um tipo específico de erro?

### E2 — overflow

Considere um `int` de 32 bits com máximo `2147483647`.

```c
int x = 2147483647;
x = x + 1;
```

Explique por que esse código é perigoso. Não basta dizer "fica negativo": explique o conceito que está sendo violado.

### E3 — divisão

Preveja antes de rodar:

```c
int a = 7;
int b = 2;
float c = a / b;
```

- Qual valor conceitual chega em `c` e por quê?
- Mostre **duas formas** de obter `3.5` sem mudar o significado matemático do problema.

### E4 — escolha de loop

Explique qual estrutura você escolheria e por quê:

- pedir uma altura até o usuário fornecer um valor entre 1 e 8;
- imprimir exatamente 20 linhas;
- processar dígitos de um número até não restar nenhum.

---

# Entrega

Estrutura esperada:

```text
LAB-CS50-001/
├── README.md
├── answers.md
├── broken.c
└── src/
    └── digitstats.c
```

Depois:

```bash
git add .
git commit -m "LAB-CS50-001 enviado"
git push
```

No chat, envie apenas:

`LAB-CS50-001 enviado`

## Mastery Gate

Este baseline não exige perfeição de primeira. Ele mede:

- **Recall:** vocabulário e mecanismos essenciais;
- **Trace:** estado e fluxo executados literalmente;
- **Rebuild:** programa em C criado do zero;
- **Repair:** bug encontrado por evidência, não por adivinhação;
- **Transfer:** tipos, overflow, divisão e loops aplicados a situações novas.

Se houver vazamentos, criaremos revisões cirúrgicas como no LAB-CS50-000.