# Git — Manual de referência profissional
Production Engineering Lab · OrderOps · DECA
Atualizado: 2026-11-27. Manual vivo, organizado por intenção. Não é necessário memorizar opções: entender o estado, escolher o comando, prever o efeito e verificar o resultado. A seção 1–6 registra os comandos apresentados no laboratório até 021 (nem todos foram executados pelo estudante); as demais incluem repertório futuro, sem atribuir domínio. Não é uma lista exaustiva de todos os subcomandos e opções existentes no Git; a referência oficial completa está ao final.

## 0. Modelo mental
- Working tree: arquivos em edição. Index/staging: snapshot preparado para o próximo commit. HEAD: referência à posição atual, normalmente por meio de uma branch. Commit: objeto imutável com snapshot, pais e metadados. Branch: referência móvel a commit.
- origin é o nome convencional de um remoto, não um nome obrigatório. origin/main é uma referência de rastreamento armazenada localmente. A branch main no servidor é uma referência diferente. Upstream é a relação configurada para rastreamento.
- Clean não significa publicado; ahead/behind usam as referências locais conhecidas. Fetch baixa objetos e atualiza refs conforme refspec, não integra o código da branch atual por padrão.
- Antes de alterar: verificar branch, HEAD, status, upstream, impacto e possibilidade de recuperação. Depois: verificar o resultado. Não expor credenciais, tokens ou dados reais.
- Sintaxe: <nome> e <hash> são placeholders; substitua pelo valor real, sem os sinais de menor/maior. Exemplos pressupõem Git Bash. --no-pager é uma opção global antes do subcomando. Se aparecer (END), pressione q. && encadeia comandos apenas em caso de sucesso. -- separa revisões/opções dos caminhos.

## 1. Diagnóstico e inventário — estudado
| Quero… | Comando | Efeito |
| --- | --- | --- |
| Saber branch e estado dos arquivos | `git status` | Consulta index, working tree e situação da operação em curso. |
| Listar branches locais | `git branch` | Consulta; * marca branch ativa. |
| Ver commits e upstreams das branches locais | `git branch -vv` | Consulta refs locais, hashes e tracking; não consulta servidor. |
| Evitar paginador | `git --no-pager branch -vv` | Mesmo diagnóstico, saída direta. |
| Ver último commit em uma linha | `git log -1 --oneline` | -1 limita a quantidade; --oneline compacta. |
| Ver grafo e referências | `git --no-pager log --oneline --graph --decorate main origin/main HEAD` | Mostra DAG e nomes das refs; pode listar todo histórico alcançável. |
| Ver commit atual e seus pais | `git log -1 --format='%h %p %s'` | Hash abreviado, hashes dos pais e assunto. |
| Resolver uma ref em hash | `git rev-parse origin/main` | Consulta o identificador local completo. |
| Encontrar melhor ancestral comum | `git merge-base HEAD origin/main` | Consulta; não integra. Em casos complexos pode haver várias melhores bases (use --all). |
| Contar commits exclusivos de cada lado | `git rev-list --left-right --count HEAD...origin/main` | Primeiro HEAD, segundo origin/main. Não conta arquivos. |

## 2. Comunicação remota — estudado
| Quero… | Comando | Efeito |
| --- | --- | --- |
| Consultar diretamente a main no servidor | `git ls-remote origin refs/heads/main` | Lê hash remoto; não atualiza origin/main nem baixa histórico. |
| Baixar atualizações do remoto | `git fetch origin` | Atualiza referências de rastreamento conforme configuração; não faz merge da branch ativa por padrão. |
| Obter só uma branch remota específica (próxima atividade) | `git fetch origin refs/heads/study/production-engineering-git-lab:refs/remotes/origin/study/production-engineering-git-lab` | Baixa objetos e atualiza a ref de rastreamento indicada; não integra arquivos. |
| Buscar e integrar na branch atual (apresentado; prática futura) | `git pull` | Fetch + integração (merge, rebase ou fast-forward, conforme opções/configuração). Não usar sem conhecer upstream e estratégia. |
| Publicar commits (apresentado; prática futura) | `git push` | Envia commits e solicita atualização da ref remota conforme configuração. Pode ser rejeitado; não force para contornar. |

## 3. Inspecionar alterações — estudado
| Quero… | Comando | Efeito |
| --- | --- | --- |
| Ver edições ainda não staged | `git diff` | Index × working tree; não inclui arquivos untracked. |
| Ver alterações staged | `git diff --cached` | HEAD × index; --staged é sinônimo. |
| Ver alterações rastreadas em relação ao HEAD | `git diff HEAD` | HEAD × working tree; não inclui untracked. |
| Ver caminhos e tipos de alteração local | `git diff --name-status main..HEAD` | Compara snapshots das duas pontas. A = adicionado, M = modificado, D = excluído; R = renomeado, entre outros. |
| Ver caminhos alterados no remoto conhecido | `git diff --name-status main..origin/main` | Compara snapshots; neste caso main é a base comum confirmada. |
| Resumo quantitativo staged | `git --no-pager diff --cached --stat` | Inserções/exclusões por arquivo; não valida semântica. |
| Revisar um arquivo staged | `git --no-pager diff --cached -- docs/engineering-notebook.html` | Patch completo restrito ao caminho. |
| Revisar por palavras, sem linhas de contexto extras | `git --no-pager diff --cached --word-diff=plain --unified=0 -- docs/engineering-notebook.html` | [-remoção-] e {+adição+}; linhas longas ainda podem gerar saída extensa. |
| Detectar whitespace problemático e marcadores de conflito introduzidos | `git diff --cached --check` | Inspeção; saída não zero se detectar problema. Não substitui testes. |
| Verificar identidade do index com referência em certos caminhos | `git diff --cached --exit-code origin/main -- docs/concursos/concursos.json` | 0 quando não há diferenças; 1 quando há diferenças. Repita para outros caminhos relevantes. |
Diferença importante: em git log/rev-list A..B seleciona commits alcançáveis por B e não por A; em git diff A..B compara snapshots A e B. git diff A...B compara a merge base com B (assimétrico). Em rev-list A...B é a diferença simétrica. Não confundir as semânticas.
Patch: --- e +++ identificam versões; @@ delimita hunk; - remove, + adiciona, espaço indica contexto. Uma substituição de linha geralmente é uma remoção e uma inserção.

## 4. Branches e commits — estudado/apresentado
| Quero… | Comando | Efeito |
| --- | --- | --- |
| Criar e selecionar branch a partir do HEAD | `git switch -c integration/production-engineering` | Cria ref e troca HEAD; não cria commit. |
| Renomear a branch atual | `git branch -m integration/production-engineering` | Mantém o commit; falha se destino existir. |
| Renomear forçando (apenas explicado) | `git branch -M <nome>` | Pode substituir ref existente; evitar por padrão. |
| Preparar arquivo (simulado) | `git add <arquivo>` | Atualiza o index com o conteúdo selecionado. |
| Criar commit | `git commit -m "mensagem clara"` | Cria commit a partir do index, move branch atual. Não publica. |
| Revisar e consolidar integração | `git commit -m "merge: integrate roadmap and production engineering updates"` | Conclui merge pendente quando index está resolvido; dois pais no caso do lab. |

## 5. Merge controlado e recuperação — estudado/apresentado
| Quero… | Comando | Efeito |
| --- | --- | --- |
| Preparar merge sem commit automático | `git merge --no-commit --no-ff origin/main` | Integra na branch atual e pausa antes do commit quando bem-sucedido; --no-ff impede fast-forward. Pode produzir conflitos. |
| Verificar estado da integração | `git status` | Mostra MERGING e mudanças staged/unmerged. All conflicts fixed não implica que houve conflitos. |
| Abortar integração pendente (apresentado) | `git merge --abort` | Tenta restaurar o estado anterior; melhor quando working tree estava limpa antes do merge. Não desfaz merge já commitado. |
| Confirmar integração após commit | `git log -1 --format='%h %p %s'` | Mostra pais; em nosso merge ba256c7 e 37ea052. |
| Conferir ancestralidade e divergência | `git rev-list --left-right --count HEAD...origin/main` | 9 0 no lab após 91f8e50. |
Divergência não é conflito. Merge textual bem-sucedido não garante correção semântica. Revisar arquivos, testar, validar dados e renderização antes de publicar.

## 6. Runbook de integração do OrderOps / roadmap — caso real
Base comum 9ef37e2; branch original ba256c7 (8 commits exclusivos), origin/main 37ea052 (11 exclusivos). Diffs contra base: 9 caminhos locais e 4 remotos, interseção zero. Branch de integração criada e renomeada. Merge 91f8e50 com dois pais, working tree limpa; 9/0 contra origin/main conhecido. Reteste 005 aprovado no 021. Revisão qualitativa de HTML não demonstrada independentemente. Não repetir a receita de merge agora: já foi executada.
Ordem de trabalho para futuros casos:
1. git status; git log -1 --oneline; git branch -vv.
2. git ls-remote origin refs/heads/main; git fetch origin.
3. git merge-base HEAD origin/main; git rev-list --left-right --count HEAD...origin/main.
4. git log --oneline --graph --decorate HEAD origin/main; revisar diffs contra a base comum.
5. Criar branch de integração com nome único, preservar baseline. Confirmar status limpo.
6. git merge --no-commit --no-ff origin/main; git status; se conflito, diagnosticar antes de resolver.
7. git diff --cached --stat; revisar patch; git diff --cached --check; conferir arquivos e testar.
8. git commit -m "merge: ..."; git log -1 --format='%h %p %s'; git status.
9. Verificar referências remotas atualizadas e política do repo; publicar branch de integração e revisar PR quando autorizado. Não force push.
10. Verificar publicação, testes CI e atualização da branch de trabalho conforme política.

## 7. Repertório profissional futuro — fundamentos, configuração e inspeção
| Intenção | Comando | Efeito / cuidado |
| --- | --- | --- |
| Ver versão do Git | `git --version` | Consulta. |
| Ajuda do comando | `git help <comando>` / `git <comando> -h` | Manual completo ou ajuda rápida. |
| Criar repo | `git init` | Inicializa metadados locais; verificar diretório. |
| Clonar | `git clone <url>` | Cria cópia local, geralmente configura origin. |
| Identidade de commits | `git config --local user.name "Nome"` / `git config --local user.email "email"` | Configura apenas repo atual; --global afeta usuário. |
| Listar configuração e origem | `git config --list --show-origin` | Consulta; pode conter dados sensíveis. |
| Ver raiz do repo | `git rev-parse --show-toplevel` | Consulta. |
| Estado compacto | `git status -sb` | Resumo de branch e mudanças. |
| Ver branches remotas conhecidas / todas | `git branch -r` / `git branch -a` | Consulta local. |
| Ver remotos e URLs | `git remote -v` | Consulta; sanitizar URLs com tokens. |
| Ver conteúdo de commit | `git show <hash>` | Consulta patch/metadados. |
| Ver arquivo em outra versão | `git show <hash>:<caminho>` | Consulta sem checkout. |
| Histórico limitado | `git log -10 --oneline` | Últimos dez commits segundo travessia. |
| Histórico de arquivo | `git log --follow -- <arquivo>` | Tenta acompanhar renomeações de um arquivo. |
| Buscar commit por texto | `git log --grep="termo"` | Busca mensagens. |
| Buscar mudança de string | `git log -S "texto" -- <arquivo>` | Pickaxe; mudanças na contagem da string. |
| Buscar alterações por regex | `git log -G "regex" -- <arquivo>` | Busca linhas do diff que correspondem. |
| Investigar autoria por linha | `git blame -- <arquivo>` | Mostra commits associados às linhas; não atribui culpa. |
| Buscar conteúdo rastreado | `git grep -n "termo"` | Pesquisa arquivos rastreados. |
| Entender ignore | `git check-ignore -v <arquivo>` | Exibe regra aplicável; .gitignore não deixa de rastrear arquivo já rastreado. |
| Inspecionar objetos | `git cat-file -t <hash>` / `git cat-file -p <hash>` | Tipo/conteúdo do objeto. |
| Listar árvore | `git ls-tree -r HEAD` | Consulta snapshot. |
| Listar index | `git ls-files --stage` | Consulta entradas staged e estágios de conflito. |

## 8. Repertório futuro — edição, branches, sincronização e colaboração
| Intenção | Comando | Efeito / cuidado |
| --- | --- | --- |
| Preparar tudo | `git add -A` | Inclui alterações e exclusões; revisar arquivos e segredos antes. |
| Preparar hunks interativamente | `git add -p` | Seleção granular. |
| Retirar do index sem perder edição | `git restore --staged -- <arquivo>` | Mantém working tree; verificar status. |
| Descartar edição não staged | `git restore -- <arquivo>` | **Perde alterações não commitadas** no caminho; revisar diff antes. |
| Corrigir último commit local | `git commit --amend` | Cria novo hash; não reescrever commit compartilhado sem coordenação. |
| Trocar branch | `git switch <branch>` | Atualiza HEAD e arquivos conforme destino; pode bloquear mudanças conflitantes. |
| Criar branch a partir de ref | `git switch -c <nova> <ref>` | Cria e seleciona. |
| Criar branch sem trocar | `git branch <nova> <ref>` | Cria referência somente. |
| Excluir branch já integrada | `git branch -d <branch>` | Proteção contra não integrada conforme upstream/HEAD. |
| Excluir branch à força | `git branch -D <branch>` | **Risco de perder referência a commits**; não usar rotineiramente. |
| Adicionar remoto | `git remote add origin <url>` | Configura endpoint. |
| Alterar URL | `git remote set-url origin <url>` | Verificar repositório de destino. |
| Limpar refs remotas obsoletas | `git fetch --prune origin` | Remove refs de rastreamento que não existem mais no remoto conforme refspec. |
| Configurar upstream | `git branch --set-upstream-to=origin/<branch>` | Configura rastreamento da branch atual; não integra. |
| Publicar branch com upstream | `git push -u origin <branch>` | Cria/atualiza remoto e tracking em sucesso. Preferir branch de trabalho + PR. |
| Simular push | `git push --dry-run origin <branch>` | Simulação sem atualizar refs remotas; não garante sucesso futuro. |
| Atualizar só por fast-forward | `git pull --ff-only` | Rejeita integração divergente. |
| Fast-forward de uma branch | `git merge --ff-only <ref>` | Move referência apenas se possível sem merge commit; falha em divergência. |
| Merge convencional | `git merge <ref>` | Integra na branch atual; pode criar commit, fazer fast-forward ou conflitar. |
| Integrar via rebase | `git rebase <ref>` | Reaplica commits, geralmente novos hashes; não usar em histórico compartilhado sem coordenação. |
| Rebase interativo | `git rebase -i HEAD~3` | Reordena/edita/combina commits locais; reescreve histórico. |
| Prosseguir / abortar rebase | `git rebase --continue` / `git rebase --abort` | Após resolver e preparar arquivos; abortar tenta restaurar estado original. |
| Trazer um commit específico | `git cherry-pick <hash>` | Reaplica mudanças criando commit novo; pode conflitar. |
| Prosseguir / abortar cherry-pick | `git cherry-pick --continue` / `git cherry-pick --abort` | Controla operação em andamento. |
| Ver conflitos pendentes | `git diff --name-only --diff-filter=U` | Lista arquivos unmerged. |
| Concluir merge resolvido | `git add <arquivo>` e `git merge --continue` | Revisar resolução; continue conclui com commit. |
| Simular merge sem tocar index/working tree (Git recente) | `git merge-tree --write-tree HEAD origin/main` | Calcula resultado e conflitos sem integrar branch; pode gravar objetos locais. |
| Publicar histórico reescrito com proteção | `git push --force-with-lease` | **Alto risco**: ainda reescreve remoto; autorização explícita e expectativa de ref verificada. Nunca usar para contornar proteção. |
| Remover branch remota | `git push origin --delete <branch>` | **Altera servidor**, somente após revisão e autorização. |
Pull request é recurso do provedor (GitHub etc.), não um comando Git nativo. Use revisão, branch protection, CI e evidências antes de integrar à main.

## 9. Repertório futuro — recuperação, investigação e releases
| Intenção | Comando | Efeito / cuidado |
| --- | --- | --- |
| Guardar edição temporária | `git stash push -u -m "contexto"` | Guarda mudanças rastreadas e untracked; não inclui ignored por padrão. |
| Listar / examinar stashes | `git stash list` / `git stash show -p stash@{0}` | Consulta; proteger dados sensíveis. |
| Recuperar sem remover stash | `git stash apply stash@{0}` | Reaplica; pode conflitar. |
| Recuperar e remover em sucesso | `git stash pop` | Reaplica e remove entrada em sucesso. |
| Desfazer commit publicado | `git revert <hash>` | Cria commit inverso; preserva histórico; pode conflitar. |
| Reverter merge | `git revert -m 1 <merge-hash>` | Seleção do pai principal tem consequências em merges futuros; revisar e testar. |
| Recuperar referências locais | `git reflog` | Histórico local de movimentações; não é backup permanente nem compartilhado. |
| Criar branch de recuperação | `git branch rescue/<nome> <hash>` | Preserva acesso ao commit encontrado; verificar hash. |
| Mover HEAD mantendo index/arquivos | `git reset --soft <hash>` | Reescreve posição da branch; mudanças permanecem staged conforme estado. |
| Mover HEAD e redefinir index | `git reset --mixed <hash>` | Mantém working tree; altera histórico local e staging. |
| Reset completo | `git reset --hard <hash>` | **Destrutivo**: descarta alterações rastreadas e pode apagar untracked que impeçam checkout. Só com backup/escopo e autorização. |
| Prévia de limpeza | `git clean -nd` | Lista untracked que seriam removidos. |
| Limpar untracked | `git clean -fd` | **Destrutivo**, arquivos podem não ser recuperáveis pelo Git. Não usar sem prévia e backup. |
| Investigar regressão | `git bisect start` / `git bisect bad` / `git bisect good <hash>` | Busca binária; testar cada estado e marcar good/bad; requer teste confiável. |
| Automatizar bisect | `git bisect run <script>` | Executa teste em commits; verificar script, ambiente e efeitos. |
| Finalizar bisect | `git bisect reset` | Retorna à referência inicial. |
| Listar tags | `git tag --list` | Consulta. |
| Criar tag anotada | `git tag -a v1.0.0 -m "Release 1.0.0"` | Identifica versão local; não publica. |
| Publicar tag específica | `git push origin v1.0.0` | Pode disparar pipeline/release; revisar política e autorização. |
| Verificar tag/commit assinado | `git tag -v v1.0.0` / `git verify-commit <hash>` | Verifica assinatura quando existente e chaves configuradas. |
| Trabalhar em outra branch sem trocar a atual | `git worktree add ../review <branch>` | Cria working tree adicional; respeitar restrições de branches já selecionadas. |
| Listar / remover worktrees | `git worktree list` / `git worktree remove ../review` | Verificar alterações antes de remover. |
| Verificar integridade dos objetos | `git fsck` | Diagnóstico de integridade; pode reportar objetos dangling normais. |
| Fazer backup portátil de refs e objetos alcançáveis | `git bundle create backup.bundle --all` | Não inclui alterações não commitadas, hooks ou config; proteger arquivo. |
| Verificar bundle | `git bundle verify backup.bundle` | Verifica formato e pré-requisitos. |
| Inicializar submódulos | `git submodule update --init --recursive` | Baixa dependências nas revisões registradas; revisar fontes confiáveis. |
| Inspecionar espaço de objetos | `git count-objects -vH` | Consulta. |
| Manutenção local | `git gc` | Compactação/limpeza conforme política; não usar agressivamente como recuperação. |

## 10. Escolha pela situação
- Quero apenas entender: status, log, branch, diff, show, rev-parse.
- Quero saber se o servidor mudou: ls-remote. Quero baixar: fetch. Quero integrar: merge/rebase conforme política.
- Quero desfazer uma alteração publicada: revert normalmente é preferível a reescrever histórico.
- Quero recuperar commit perdido: reflog + branch de recuperação, antes de reset.
- Quero diagnosticar regressão: log, blame, bisect, testes.
- Quero publicar: revisar staged/commits, testes, fetch, comparar refs, push branch específica, PR, CI.
- Qualquer comando destrutivo, publicação em main, alteração de credenciais ou release: confirmar escopo, backup, impacto, autorização, plano de recuperação. Nunca executar comandos destrutivos só para silenciar um erro.
- Git não substitui backup de arquivos não rastreados, banco de dados, segredos ou infraestrutura.

## Referências oficiais
- [Todos os comandos e opções do Git](https://git-scm.com/docs)
- [Pro Git — livro gratuito](https://git-scm.com/book/en/v2)
- [Git glossary](https://git-scm.com/docs/gitglossary)
- [GitHub Docs — pull requests](https://docs.github.com/en/pull-requests)
- [Diário DECA Git Lab](GIT-LAB-PROGRESS.md)

Manutenção: adicionar cada comando novo da formação, seu objetivo, efeito, risco, como verificar e evidência prática. Separar comandos apresentados, executados e dominados; não repetir módulos somente para decorar sintaxe. Integrar link no painel de Production Engineering quando o currículo local for reconciliado; manter este arquivo como referência canônica.
