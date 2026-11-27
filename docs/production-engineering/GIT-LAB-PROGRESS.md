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
| 009 | git merge-base HEAD origin/main | Escolheu C; saída 9ef37e2dbc0593127052e9d30cccae6bccb9bf02 confirma o melhor ancestral comum | validado nesta atividade |
| 010 | git diff --name-status main..HEAD | Escolheu B; 8 caminhos modificados e 1 adicionado (render-panel.cjs), 0 excluídos; total 9 caminhos, 8 commits exclusivos | validado nesta atividade |
| 011 | git diff --name-status main..origin/main; interseção de caminhos | Escolheu B; 3 modificados e 1 adicionado no remoto, 0 caminhos em comum com os 9 do lado local. Integração textual sem conflitos é previsão, não execução. | validado nesta atividade |
| 012 | git switch -c; criação de branch de integração | Escolheu B; criou integration/production-enginnering (grafia efetiva), HEAD e branch anterior apontam para ba256c7, sete branches locais; sem commit novo. | validado nesta atividade |
| 013 | git branch -m; renomeação local | Escolheu B; comando sem erro e prompt exibe integration/production-engineering. Hash pós-renomeação e working tree ainda não exibidos; confirmar no próximo passo. | validado; hash confirmado no 014 |
| 014 | Pre-merge check | Escolheu B; git log confirma HEAD ba256c7, integration/production-engineering e pe-005-frontend-and-curriculum no mesmo commit. Saída git status ausente; working tree limpa não reconfirmada. | conceito validado; gate operacional pendente |
## Notas teóricas da sessão (consolidar em theory.json preservando IDs)
- Working tree, index e HEAD são estados locais; clean não significa sincronizado.
- Branch é referência móvel a commit, que referencia snapshot; HEAD normalmente referencia a branch atual.
- Upstream é relação configurada; origin/main é referência local de rastreamento, não consulta em tempo real.
- ls-remote consulta refs do servidor sem atualizar refs locais nem baixar histórico.
- fetch baixa objetos ausentes e atualiza refs conforme refspec; no caso observado atualizou origin/main, sem integrar branch ativa. Objetos não equivalem a arquivos ou commits.
- Behind 11 indica 11 commits alcançáveis pelo upstream e não pela branch local; não equivale a 11 arquivos. --no-pager desativa o paginador nesta execução.
- O histórico Git é um DAG: commits apontam para seus pais, podendo ter mais de um em merges. Branches divergentes possuem commits exclusivos de cada lado a partir de ancestral comum. Divergência não implica conflito de arquivos. --graph representa relações; --decorate identifica refs. Limitar histórico com intervalo quando pertinente.
- Merge base é um melhor ancestral comum entre commits; pode haver mais de um em históricos complexos. git merge-base consulta o grafo sem integrar históricos ou alterar refs. Neste caso a base é a main local 9ef37e2.
- Three-way merge considera base comum e os snapshots das duas pontas; divergência sozinha não prova conflito.
- git diff --name-status A..B compara os snapshots de A e B; A (adicionado), M (modificado), D (excluído), podendo haver outros estados. Quantidade de commits não determina quantidade de caminhos com diferença líquida. Arquivos locais observados: README.md, docs/index.html, docs/production-engineering/{CODEX.md,PROGRESS.md,README.md,curriculum.json,index.html,render-panel.cjs,theory.json}.
- Comparar os dois diffs contra a mesma base permite identificar sobreposição de caminhos. Alterar o mesmo arquivo não implica conflito: depende das mudanças, e mesmo sem conflito textual pode haver inconsistência semântica. Neste caso remoto alterou docs/concursos/concursos.json, docs/connect-lab/PROGRESS.md, docs/engineering-notebook.html e adicionou docs/production-engineering/EXPANSION-2026-11-27.md; interseção observada vazia.
- git switch -c cria uma referência de branch e seleciona a nova branch; sem start-point explícito, usa o HEAD atual. Não cria commit. A branch de entrega fica preservada. A grafia efetiva da nova branch contém um erro; corrigir via git branch -m, sem forçar.
- git branch -m renomeia a referência, preservando o commit apontado; o nome de branch não integra o objeto commit. -M força renomeação e pode substituir destino existente; não necessário neste caso.
- Pre-merge check distingue precondição esperada de evidência observada. Conferir branch, HEAD, index/working tree e ausência de operação pendente antes de integrar.
## Próximo passo
Experimento 014.1: git status; confirmar working tree limpa e ausência de operação pendente na branch integration/production-engineering. HEAD ba256c7 já confirmado pelo 014. Se houver alterações ou operação pendente, parar e investigar. Não realizar merge, pull, rebase, push ou reset até confirmar o gate. Reteste 005 continua pendente.
