# LAB-CS50-001 — Review 02

**Tentativa revisada:** `d1e911e371d7ab645fc4e813b73bf6e92dddd56d`  
**Modo:** Learning Mode  
**Objetivo:** fechar apenas semântica de conversão de tipos em C.

## O que já fechou

Não repita build pipeline, divisão inteira, testes do `digitstats` nem dinheiro em centavos. Esses pontos passaram na R1.

## R2-A — Aritmética versus conversão

Compare dois cenários conceituais:

1. Uma variável inteira já está no maior valor que seu tipo representa e uma soma tenta produzir um valor acima dessa faixa.
2. Um valor já existente em `long` é atribuído a um `int`, mas esse valor não cabe na faixa do `int`.

Para cada um responda:

```text
há operação aritmética? =
há conversão de tipo? =
qual é o fenômeno principal? =
por que os dois casos não devem receber exatamente o mesmo nome? =
```

## R2-B — Implícito versus explícito

Considere:

```c
double price = 19.99;
int a = price;
int b = (int) price;
```

Responda:

1. Qual atribuição usa conversão implícita?
2. Qual usa cast explícito?
3. Qual valor chega em `a` e `b` nesse exemplo?
4. O que acontece com a parte fracionária?
5. Escrever um cast explícito garante que qualquer valor original possa ser representado corretamente pelo tipo de destino? Explique.

## R2-C — Fechamento do Repair

Sem executar primeiro, escreva a saída completa de `broken-r1.c`, linha por linha. Depois execute e compare.

Registre:

```text
previsão =
saída real =
divergiu? =
por que average agora preserva 3.5? =
```

## Entrega

Crie `answers-r2.md`, preserve os arquivos anteriores e depois:

```bash
git add .
git commit -m "LAB-CS50-001 R2 enviado"
git push
```

No chat: `LAB-CS50-001 R2 enviado`
