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
## Notas teóricas da sessão (consolidar em theory.json preservando IDs)
- Working tree, index e HEAD são estados locais; clean não significa sincronizado.
- Branch é referência móvel a commit, que referencia snapshot; HEAD normalmente referencia a branch atual.
- Upstream é relação configurada; origin/main é referência local de rastreamento, não consulta em tempo real.
- ls-remote consulta refs do servidor sem atualizar refs locais nem baixar histórico.
- fetch baixa objetos ausentes e atualiza refs conforme refspec; no caso observado atualizou origin/main, sem integrar branch ativa. Objetos não equivalem a arquivos ou commits.
## Próximo passo
Experimento 007: git --no-pager branch -vv; prever e conferir main local, origin/main e branch atual. Não executar merge, pull, rebase, push ou reset. Retestar diferença ls-remote/fetch posteriormente. Integrar este diário com a versão local do currículo após revisão, sem sobrescrever evidências.
