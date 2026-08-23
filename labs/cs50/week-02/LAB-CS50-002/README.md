# LAB-CS50-002 — CS50 Problem Set 2 / Arrays

**Fonte:** CS50x 2026 — Problem Set 2, associado à Week 2 — Arrays  
**Modo:** Learning Mode  
**Objetivo:** medir se os fundamentos usados no PSet 2 estão disponíveis fora dos enunciados originais, sem copiar soluções de Scrabble, Readability, Caesar ou Substitution.

> Concluir o PSet é evidência externa de prática. Este lab mede domínio independente em Recall, Trace, Rebuild, Repair e Transfer.

## Regras

- Não consulte suas soluções do PSet 2 durante a primeira tentativa.
- Pode usar compilador, mensagens de erro e man pages somente depois de registrar suas previsões nas seções de Trace/Repair.
- Não use ponteiros explicitamente nem conteúdo da Week 4 em diante.
- Preserve esta primeira tentativa; qualquer correção irá para arquivos separados.

Crie `answers.md` para A, B e E. Crie os programas pedidos em `src/`.

---

## A — RECALL

Responda em 1–3 frases cada, sem pesquisar:

1. O que é um array em C e qual problema ele resolve em relação a várias variáveis separadas?
2. Por que o primeiro elemento de um array tem índice `0`?
3. O que acontece conceitualmente se o programa tenta acessar uma posição fora dos limites de um array?
4. Como uma string é representada em C e qual o papel do caractere `\0`?
5. Qual a diferença entre o tamanho lógico de uma string e o espaço necessário para armazená-la como array de `char`?
6. O que representam `argc` e `argv` em `main(int argc, string argv[])`?
7. Por que devemos validar `argc` antes de acessar `argv[1]`?
8. Para que servem funções como `isalpha`, `isupper`, `tolower` ou `toupper`?
9. Explique a relação entre caracteres como `'A'`, `'B'` e números inteiros em C.
10. Coloque na ordem correta e explique brevemente: preprocessing, compiling, assembling, linking.

---

## B — TRACE

Não execute antes de prever.

```c
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    char text[] = "aB3z";
    int letters = 0;
    int uppercase = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            letters++;

            if (isupper(text[i]))
            {
                uppercase++;
            }
        }
    }

    printf("%i %i\n", letters, uppercase);
}
```

Monte uma tabela com:

```text
iteração | i | text[i] | isalpha? | isupper? avaliado? | letters | uppercase
```

Depois responda:

- Qual saída final será impressa?
- Quantas iterações o `for` executa?
- Por que o `3` não incrementa `letters`?
- Se a condição fosse `i <= strlen(text)`, qual posição extra seria alcançada e qual caractere especial existe ali?

Só depois compile para conferir e registre se houve divergência.

---

## C — REBUILD

Do editor vazio, crie:

```text
src/textstats.c
```

O programa deve receber **exatamente um argumento de linha de comando** e imprimir:

- quantidade total de caracteres da string;
- quantidade de letras alfabéticas;
- quantidade de letras maiúsculas;
- quantidade de dígitos.

Exemplo conceitual:

```text
./textstats Ab3-z
chars: 5
letters: 3
uppercase: 1
digits: 1
```

Requisitos:

- valide `argc` antes de acessar `argv[1]`;
- use `strlen` e funções de `<ctype.h>`;
- percorra a string por índice;
- não use arrays auxiliares;
- retorne código diferente de zero quando a quantidade de argumentos estiver incorreta.

Antes de programar, escreva em `answers.md` pseudocódigo de no máximo 8 linhas.

Compile com:

```bash
gcc -Wall -Wextra -Werror src/textstats.c -o textstats
```

Registre pelo menos 4 testes, incluindo execução sem argumento e execução com mais de um argumento.

---

## D — REPAIR

O arquivo `broken.c` deste laboratório contém bugs relacionados a argumentos, limites de array/string e classificação de caracteres.

Procedimento:

1. Antes de editar, escreva em `answers.md` o que você prevê que pode dar errado.
2. Compile e execute com diferentes argumentos.
3. Liste cada bug como `sintoma → causa → correção`.
4. Corrija apenas o necessário.
5. Compile com warnings como erros.
6. Registre a saída final para pelo menos dois argumentos válidos e um caso inválido.

---

## E — TRANSFER

### E1 — Índices e limites

Considere:

```c
int values[4] = {10, 20, 30, 40};
```

- Quais são os índices válidos?
- Por que `values[4]` não representa o quarto elemento?
- Qual padrão de condição de `for` percorre exatamente todos os elementos?

### E2 — String e terminador

Para:

```c
char word[] = "CAT";
```

- Quantos caracteres visíveis existem?
- Quantas posições são necessárias no array?
- O que está armazenado na última posição?

### E3 — Argumentos de linha de comando

Explique a diferença entre executar:

```text
./program
./program hello
./program hello world
```

em termos de `argc` e de quais entradas existem em `argv`.

### E4 — Cifra com preservação de caixa

Você precisa deslocar letras por uma chave `k`, preservando maiúsculas/minúsculas e mantendo caracteres não alfabéticos inalterados.

Sem escrever a solução completa de Caesar/Substitution, descreva o algoritmo em passos e explique onde `% 26` é útil para fazer o alfabeto "dar a volta".

### E5 — Pipeline de build

Um arquivo `program.c` inclui headers e chama uma função de uma biblioteca externa. Explique em qual etapa cada item é resolvido conceitualmente:

- diretivas `#include`;
- tradução de C para assembly;
- tradução de assembly para machine code;
- combinação do seu object code com bibliotecas.

---

# Entrega

Estrutura esperada:

```text
LAB-CS50-002/
├── README.md
├── answers.md
├── broken.c
└── src/
    └── textstats.c
```

Depois:

```bash
git add .
git commit -m "LAB-CS50-002 enviado"
git push
```

No chat:

`LAB-CS50-002 enviado`

## Mastery Gate

Este baseline mede:

- **Recall:** arrays, strings, argumentos e pipeline de build;
- **Trace:** índices, caracteres e fluxo aninhado;
- **Rebuild:** processamento de string + CLI do zero;
- **Repair:** off-by-one, validação de argumentos e classificação de caracteres;
- **Transfer:** limites, terminador nulo, modularidade e criptografia conceitual.
