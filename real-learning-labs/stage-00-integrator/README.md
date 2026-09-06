# Stage 00 — Mini-lab integrador

Você recebeu um pequeno programa Python que deveria carregar clientes de um CSV, gerar um relatório simples e validar um lote sintético.

O estado atual do laboratório contém regressões deliberadas. Seu trabalho não é apenas fazer o programa voltar a funcionar: é investigar e provar o que aconteceu usando as ferramentas do Stage 00.

## Regras

- Trabalhe em uma branch própria, por exemplo `stage-00-fix`.
- Não substitua o programa inteiro por outra implementação.
- Antes de alterar código, registre pelo menos uma hipótese baseada em evidência.
- Use o histórico Git do próprio laboratório como fonte de investigação.
- Pode consultar `--help`, documentação e suas anotações.
- Se pedir ajuda ao ChatGPT durante o lab, peça pistas graduais; não uma solução completa.

## Estado esperado do sistema

Ao final, a execução deve terminar com exit code `0` e produzir um resultado equivalente a:

```text
customers=5 vip=2 duplicates=False
run_finished exit_code=0
```

Além de voltar a funcionar, o trecho de validação do lote sintético deve ter desempenho claramente melhor que o estado regressivo. Não existe um tempo absoluto obrigatório porque o hardware varia: registre uma medição antes e depois e demonstre a melhora.

## Evidências que você deve produzir

Crie um arquivo `INVESTIGATION.md` dentro desta pasta contendo, de forma curta:

1. **Sintoma inicial** — o que aconteceu e qual foi o exit code.
2. **Evidência** — stack trace, logs, bytes, Git ou profiling que sustentou sua hipótese.
3. **Causa 1** — explique a primeira regressão encontrada.
4. **Causa 2** — explique o problema de performance encontrado.
5. **Antes × depois** — medição comparável de performance.
6. **Correção** — por que sua alteração resolve a causa e não só o sintoma.
7. **Reteste** — resultado final e exit code.

## Ferramentas já estudadas que podem ser úteis

Não há uma ordem prescrita. Você já conhece ferramentas suficientes para escolher sozinho entre:

- filesystem e caminhos;
- processos, ambiente, stdout/stderr e exit codes;
- inspeção de bytes/encoding;
- `git status`, `git log`, `git diff`, `git show`;
- debugger e call stack;
- logs;
- `time`, `cProfile` e observação de processos.

## Critério do Stage 00

O laboratório está concluído quando você consegue contar a história causal do incidente:

> o que quebrou → como você descobriu → por que quebrou → como mediu → o que corrigiu → como provou.

Não existe mérito extra por acertar de primeira. Existe mérito em investigar com método.
