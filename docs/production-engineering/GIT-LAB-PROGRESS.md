# Production Engineering Lab — diário DECA de Git
Data: 2026-11-27. Evidências: saídas e respostas fornecidas pelo estudante, não execução independente. Nenhum módulo marcado como dominado. Registro em branch separada para não alterar a main usada no experimento de integração.
| Experimento | Conceito | Evidência / resposta | Estado |
| --- | --- | --- | --- |
| 001 | git status, working tree e index | Respondeu que Git consegue determinar alterações sem internet; branch pe-005-frontend-and-curriculum, working tree clean | validado nesta atividade |
| 002 | git log -1 --oneline, HEAD | Deduziu último commit em uma linha; ba256c7 | validado; refinado significado dos argumentos |
| 003 | git branch, referências | Não duplica arquivos; identificou referência ao snapshot; seis branches locais | validado; branch aponta a commit |
| 004 | git branch -vv, upstream | Nomes iguais não garantem hashes iguais; main 9ef37e2 [origin/main]; cinco branches sem upstream exibido | validado |
| 005 | git ls-remote | Executou corretamente; não soube prever efeito local; refs/heads/main = 37ea05237c10c87a17b22f3f7fd093e7a7dc6c11 | reteste pendente |
| 006 | git fetch origin | Escolheu B (origin/main); saída 9ef37e2..37ea052 main -> origin/main; 51 objetos, 34 deltas | validado nesta atividade |
| 007 | git --no-pager branch -vv, behind | Escolheu B; main 9ef37e2 [origin/main: behind 11], branch ativa ba256c7; seis branches locais mantiveram os hashes anteriores | validado nesta atividade |
| 008 | git log --oneline --graph --decorate, divergência | Escolheu B; grafo mostra base comum 9ef37e2, 11 commits exclusivos de origin/main (37ea052) e 8 exclusivos de HEAD (ba256c7) | validado nesta atividade |
## Notas teóricas da sessão (consolidar em theory.json preservando IDs)
- Working tree, index e HEAD são estados locais; clean não significa sincronizado.
- Branch é referência móvel a commit, que referencia snapshot; HEAD normalmente referencia a branch atual.
- Upstream é relação configurada; origin/main é referência local de rastreamento, não consulta em tempo real.
- ls-remote consulta refs do servidor sem atualizar refs locais nem baixar histórico.
- fetch baixa objetos ausentes e atualiza refs conforme refspec; no caso observado atualizou origin/main, sem integrar branch ativa. Objetos não equivalem a arquivos ou commits.
- Behind 11 indica 11 commits alcançáveis pelo upstream e não pela branch local; não equivale a 11 arquivos. --no-pager desativa o paginador nesta execução.
- O histórico Git é um DAG: commits apontam para seus pais, podendo ter mais de um em merges. Branches divergentes possuem commits exclusivos de cada lado a partir de ancestral comum. Divergência não implica conflito de arquivos. --graph representa relações; --decorate identifica refs. Limitar histórico com intervalo quando pertinente.
## Próximo passo
Experimento 009: git merge-base HEAD origin/main; prever o hash do melhor ancestral comum neste grafo e verificar. Apenas inspeção; não executar merge, pull, rebase, push ou reset. Reteste 005 continua pendente. Preservar os históricos, integrar diário e currículo posteriormente.
