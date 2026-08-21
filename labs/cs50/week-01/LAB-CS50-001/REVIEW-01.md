# LAB-CS50-001 — Review 01

**Tentativa revisada:** commit `03625d70185e5ef593f42ba2f452e83118ffa8e3`  
**Status:** correção direcionada  
**Modo:** Learning Mode

## O que já passou

A primeira tentativa mostrou boa execução de `for`, `if/else`, `%`, `do/while`, `while`, decomposição numérica com `% 10` e `/ 10`, overflow e representação binária de ponto flutuante. O `digitstats.c` também apresenta uma solução funcional para entradas inteiras positivas.

Não repita essas partes.

## Vazamentos desta rodada

1. `make` foi identificado como se fosse o compilador. Precisamos separar ferramenta de build, compilador e executável.
2. No Repair, os bugs de `=` e `i--` foram encontrados, mas `float average = total / people;` permaneceu. O cálculo acontece antes da atribuição ao `float`; portanto, o tipo da variável de destino não corrige automaticamente uma operação já executada com operandos inteiros.
3. O Rebuild não registrou os quatro casos de teste exigidos. Código que parece correto ainda precisa de evidência de verificação.
4. A explicação sobre conversões entre tipos sugeriu que uma conversão para tipo menor necessariamente produz erro de execução. Em C, isso não é um modelo seguro; precisamos distinguir perda de informação, conversão, overflow e erro em runtime.

---

# R1-A — Build pipeline

Sem pesquisar, complete cada papel em uma frase:

```text
hello.c =
make =
compilador (ex.: clang/gcc) =
executável gerado =
```

Depois responda:

> Se eu digitar `make hello`, quem efetivamente traduz C para código executável: `make` ou o compilador? Qual é o papel do outro?

---

# R1-B — Integer division antes da atribuição

Não execute antes de prever:

```c
int total = 11;
int people = 4;
double average = total / people;
```

Responda:

```text
1. valor final de average =
2. em qual operação a parte fracionária é perdida? =
3. por que declarar apenas average como double não basta? =
4. escreva duas correções mínimas diferentes que produzam 2.75 =
```

Agora crie `broken-r1.c` a partir do `broken.c` atual e corrija **somente o problema aritmético restante**. Não reescreva o programa.

Compile:

```bash
gcc -Wall -Wextra -Werror broken-r1.c -o broken-r1
```

Registre a saída completa. O objetivo é justificar cada linha pela execução do código, não pela intenção do programa.

---

# R1-C — Tipos e conversão

Para cada caso, diga o que pode acontecer e por quê. Não responda apenas “dá erro”.

### Caso 1

```c
long big = 3000000000L;
int small = big;
```

### Caso 2

```c
int a = 7;
int b = 2;
double x = a / b;
```

### Caso 3

```c
double price = 19.99;
int whole = price;
```

Em cada caso identifique se a preocupação principal é:

```text
- perda de parte fracionária
- valor fora da faixa do tipo de destino
- divisão inteira antes da conversão
- ou nenhuma das anteriores
```

---

# R1-D — Evidência de teste do Rebuild

Não altere `digitstats.c` se ele já atender ao requisito. Execute e registre esta tabela:

```text
entrada / sequência | quantidade de dígitos | soma dos dígitos | passou?
7                   |                       |                  |
4827                |                       |                  |
1000                |                       |                  |
-5 e depois 42      |                       |                  |
```

Para o último caso, registre também se `-5` foi rejeitado antes de o programa aceitar `42`.

Depois responda em uma frase:

> Por que executar casos de teste faz parte do domínio de programação mesmo quando o código compila sem warnings?

---

# R1-E — Dinheiro sem ponto flutuante

Retome o valor `R$ 9.876.543,21`.

Responda de forma concreta:

```text
tipo escolhido =
valor inteiro realmente armazenado em centavos =
como obter a parte de reais =
como obter os dois dígitos de centavos =
qual erro evitamos ao não usar float/double para o valor monetário interno =
```

---

## Entrega

Crie:

```text
answers-r1.md
broken-r1.c
```

Preserve `answers.md`, `broken.c` e `src/digitstats.c` como evidência da primeira tentativa.

Depois:

```bash
git add .
git commit -m "LAB-CS50-001 R1 enviado"
git push
```

No chat:

`LAB-CS50-001 R1 enviado`
