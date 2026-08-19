# LAB-CS50-000 — Baseline de Fundamentos

**Origem:** CS50x Lecture 0 + Problem Set 0 (Scratch)

**Objetivo:** medir o que ficou da Aula 0 sem confundir conclusão do curso com domínio real.

## Regras

- Learning Mode: não consultar solução pronta antes da tentativa.
- Pode executar/testar suas respostas depois de prever o resultado.
- Quando houver dúvida, registre a hipótese antes de pesquisar.
- Não é necessário decorar sintaxe específica de Scratch.

## Parte A — Recall

Responda em `answers.md`, sem consultar material:

1. O que é um algoritmo?
2. Qual a diferença entre uma sequência de instruções e um loop?
3. O que uma condição permite ao programa decidir?
4. Para que serve uma variável em um programa/jogo?
5. O que significa abstração em programação? Dê um exemplo usando blocos/funções.
6. Qual a diferença entre evento e ação?

## Parte B — Trace

Considere este pseudocódigo:

```text
score = 0
repeat 4 times:
    if score < 2:
        score = score + 1
    else:
        score = score + 2
```

Antes de executar qualquer coisa:

1. Escreva o valor de `score` após cada iteração.
2. Informe o valor final.
3. Explique por que o terceiro ciclo não executa exatamente como o primeiro.

## Parte C — Rebuild

Sem abrir seu projeto antigo, descreva em pseudocódigo uma versão mínima de **Bug vs Developer** com:

- estado inicial;
- movimento do jogador;
- evento de disparo;
- colisão tiro/bug;
- pontuação;
- condição de vitória;
- condição de derrota;
- reinício consistente do jogo.

Depois, implemente uma versão equivalente em Scratch **ou**, se já estiver confortável no freeCodeCamp, em JavaScript simples. A linguagem não é o alvo principal; o fluxo é.

## Parte D — Repair

O jogo abaixo possui um bug lógico:

```text
when game starts
    lives = 3

forever
    if bug touches server
        lives = lives - 1
        if lives >= 0
            game over
```

1. Explique o comportamento incorreto.
2. Identifique a condição correta sem simplesmente escrever "trocar o sinal" — explique o modelo mental.
3. Cite um teste que provaria que a correção funciona.

## Parte E — Transfer

Agora altere o problema:

> O jogador vence ao eliminar 10 bugs, mas a cada 3 eliminações a velocidade dos bugs aumenta. Ao perder uma vida, os bugs não devem voltar à velocidade inicial. No restart completo, devem.

Em `answers.md`:

1. Quais variáveis de estado você criaria?
2. Quais eventos alterariam cada uma?
3. Onde mora o risco de estado inconsistente?
4. Como separaria `perder uma vida` de `reiniciar o jogo`?

## Entrega

Crie dentro desta pasta:

```text
answers.md
solution/   # apenas se fizer implementação
```

Faça commit e push. Depois informe no chat apenas:

`LAB-CS50-000 enviado`

A revisão será feita no GitHub e poderá gerar correções, entradas no Error Ledger e novas revisões espaçadas.
