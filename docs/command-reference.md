# Command Reference — Caixa de Ferramentas

> Referência viva do roadmap **Como Realmente Aprender Programação**.  
> Objetivo: consultar quando surgir uma pergunta prática, sem depender de memória de comandos pouco usados.

Atualizado em: **2026-09-06**

---

## Como usar esta referência

Não comece pelo comando. Comece pela pergunta.

| Situação | Pergunta | Ferramenta principal |
|---|---|---|
| Não sei onde estou | Em qual diretório estou? | `pwd` |
| Não encontro um arquivo | O que existe aqui? | `ls -la` |
| Um comando não é encontrado | Qual executável o shell está usando? | `which`, `$PATH` |
| Programa parece travado | Qual processo está rodando? | `ps`, `jobs` |
| Programa terminou estranho | Qual foi o exit code? | `echo $?` |
| Arquivo parece igual, mas dá problema | Os bytes são realmente iguais? | `xxd`, `cmp`, `sha256sum` |
| Texto aparece corrompido | Qual encoding/bytes existem no arquivo? | `file`, `xxd`, `hexdump` |
| Código mudou | O que está diferente agora? | `git diff` |
| Não sei o estado do repositório | O que está staged, modificado ou untracked? | `git status` |
| Algo quebrou recentemente | O que mudou no histórico? | `git log`, `git show` |
| Programa lança exceção | Onde o sintoma apareceu e qual foi a cadeia de chamadas? | stack trace + `pdb` |
| Preciso observar estado em execução | Quais valores o programa realmente tem? | breakpoint + `p`, `where` |
| Bug aconteceu no passado/produção | Que evidências ficaram? | logs + `grep`/`tail` |
| Programa está lento | Onde o tempo está concentrado? | `cProfile` |
| Quero comparar antes/depois | A mudança realmente melhorou? | `time`, `cProfile` |
| Quero saber se é CPU ou espera | `real`, `user` e `sys` contam histórias diferentes? | `time` |

---

# 00.1 — Terminal e filesystem

## Orientação e navegação

| Comando | Para que serve | Quando usar |
|---|---|---|
| `pwd` | Mostra o diretório atual | Quando não sabe onde está |
| `ls` | Lista arquivos e diretórios | Inspeção rápida |
| `ls -la` | Lista detalhes e arquivos ocultos | Ver permissões, `.git`, arquivos ocultos |
| `cd <dir>` | Entra em um diretório | Navegação |
| `cd ..` | Vai para o diretório pai | Subir um nível |

## Criar e manipular arquivos

| Comando | Para que serve | Quando usar |
|---|---|---|
| `mkdir <dir>` | Cria diretório | Organizar projeto/lab |
| `touch <arquivo>` | Cria arquivo vazio ou atualiza timestamp | Criar rapidamente um arquivo |
| `cat <arquivo>` | Envia conteúdo do arquivo para stdout | Inspeção rápida de texto |
| `echo "texto" > arquivo` | Sobrescreve arquivo com stdout | Criar/substituir conteúdo simples |
| `echo "texto" >> arquivo` | Acrescenta conteúdo ao final | Append |
| `cp origem destino` | Copia arquivo | Duplicar conteúdo |
| `mv origem destino` | Move ou renomeia | Organização/rename |
| `rm <arquivo>` | Remove arquivo | Exclusão consciente |
| `rmdir <dir>` | Remove diretório vazio | Limpeza |

> Cuidado: `rm -rf` é destrutivo. Entenda exatamente o caminho antes de executar.

## Descoberta de executáveis

| Comando | Para que serve |
|---|---|
| `which <comando>` | Mostra qual executável será encontrado pelo `PATH` |
| `echo $PATH` | Mostra os diretórios onde o shell procura executáveis |

Modelo mental: **arquivo/comando sempre existe em um contexto: diretório atual, caminho e ambiente.**

---

# 00.2 — Processos, execução e I/O

## Processos

| Comando | Para que serve |
|---|---|
| `ps` | Processos associados ao terminal |
| `ps aux` | Lista ampla de processos |
| `sleep 100` | Processo simples em foreground para experimentos |
| `sleep 100 &` | Executa em background |
| `jobs` | Mostra jobs do shell atual |
| `kill <PID>` | Envia sinal de término ao processo |
| `echo $$` | Mostra PID do shell atual |
| `ps -o pid,ppid,cmd` | Mostra PID, processo pai e comando |

## Exit codes

| Comando | Para que serve |
|---|---|
| `echo $?` | Mostra exit code do último comando |
| `true; echo $?` | Exemplo de sucesso (`0`) |
| `false; echo $?` | Exemplo de falha (`!= 0`) |

Convenção: **0 = sucesso; diferente de 0 = algum tipo de falha.**

## stdin, stdout, stderr e pipes

| Comando | Para que serve |
|---|---|
| `comando 2> error.txt` | Redireciona stderr para arquivo |
| `comando1 | comando2` | stdout do primeiro vira stdin do segundo |
| `python3 app.py > app.log 2>&1` | stdout e stderr vão para o mesmo arquivo |

Descritores básicos:

- `0` = stdin
- `1` = stdout
- `2` = stderr

## Ambiente e execução

| Comando | Para que serve |
|---|---|
| `env` | Lista variáveis de ambiente |
| `echo $HOME` | Home do usuário |
| `echo $USER` | Usuário atual |
| `export APP_ENV=development` | Define variável exportada para processos filhos |
| `chmod +x run.sh` | Adiciona permissão de execução |
| `./run.sh` | Executa arquivo do diretório atual |
| `bash run.sh` | Executa script explicitamente usando Bash |

Modelo mental: **programa é artefato; processo é programa em execução com PID, memória, ambiente, I/O e exit code.**

---

# 00.3 — Bytes, texto e encoding

## Inspecionar bytes

| Comando | Para que serve |
|---|---|
| `printf 'A' | xxd` | Mostra os bytes em hexadecimal |
| `printf 'ç' | xxd` | Demonstra UTF-8 multibyte |
| `printf '🙂' | xxd` | Demonstra caractere com vários bytes |
| `xxd arquivo` | Hex dump simples |
| `hexdump -C arquivo` | Offset + hexadecimal + visão textual |
| `file arquivo` | Tenta identificar tipo/encoding |

## Bytes vs caracteres

| Comando | Para que serve |
|---|---|
| `printf 'Olá 🙂' | wc -c` | Conta bytes |
| `printf 'Olá 🙂' | wc -m` | Conta caracteres |

Regra: **1 caractere não é necessariamente 1 byte.**

## Line endings

```bash
printf 'linha1\nlinha2\n' > lf.txt
printf 'linha1\r\nlinha2\r\n' > crlf.txt
xxd lf.txt
xxd crlf.txt
```

- LF = `0a`
- CRLF = `0d 0a`

## Comparar arquivos de verdade

| Comando | Para que serve |
|---|---|
| `diff a b` | Diferenças textuais |
| `cmp a b` | Comparação byte a byte |
| `sha256sum a b` | Hash dos bytes; arquivos diferentes geram hashes diferentes |

## BOM UTF-8

```bash
printf '\xEF\xBB\xBFhello\n' > bom.txt
xxd bom.txt
```

BOM UTF-8: `EF BB BF`.

Modelo mental: **arquivo guarda bytes; texto é interpretação dos bytes segundo um encoding.**

---

# 00.4 — Git como máquina do tempo

## Configuração inicial

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

## Estado e snapshots

| Comando | Para que serve | Pergunta respondida |
|---|---|---|
| `git init` | Inicializa `.git` | Quero começar um repositório |
| `git status` | Mostra working tree/staging | Em que estado está o repo? |
| `git add <arquivo>` | Prepara versão para próximo commit | O que entrará no snapshot? |
| `git commit -m "mensagem"` | Registra snapshot | Quero preservar este estado |
| `git diff` | Working Tree ↔ Staging | O que alterei e ainda não preparei? |
| `git diff --staged` | Staging ↔ último commit | O que exatamente vou commitar? |

## Histórico

| Comando | Para que serve |
|---|---|
| `git log` | Histórico detalhado |
| `git log --oneline` | Histórico compacto |
| `git log --oneline --decorate` | Mostra HEAD e ponteiros de branches |
| `git show <HASH>` | Detalhes e diff de um commit |

## Branches

| Comando | Para que serve |
|---|---|
| `git branch <nome>` | Cria branch no commit atual |
| `git switch <branch>` | Troca de branch |
| `git switch -c <branch>` | Cria e já troca para a nova branch |
| `git merge <branch>` | Integra a branch indicada na atual |

Modelo mental:

```text
Working Tree → git add → Staging/Index → git commit → History
branch = ponteiro móvel para commit
HEAD = posição/branch atual
```

## Repositório remoto

| Comando | Para que serve |
|---|---|
| `git clone <URL>` | Cria clone local de repositório remoto |
| `git pull` | Busca e integra atualizações da branch remota acompanhada |

Importante: **Git ≠ GitHub**.

---

# Git para investigar regressões

Esses comandos apareceram no primeiro laboratório integrador e devem ficar na caixa de ferramentas permanente.

| Comando | Para que serve |
|---|---|
| `git log --oneline -- app.py` | Mostra histórico somente daquele arquivo |
| `git show <HASH> -- app.py` | Mostra o que um commit alterou naquele arquivo |
| `git diff <HASH>^ <HASH> -- app.py` | Compara commit suspeito com o pai imediato |

Fluxo recomendado:

```text
sintoma recente
→ medir/reproduzir
→ git log no arquivo relevante
→ escolher commit suspeito
→ git show / git diff
→ formular hipótese
→ corrigir
→ medir novamente
```

---

# 00.5 — Debugger e stack trace (`pdb`)

Iniciar:

```bash
python3 -m pdb app.py
```

## Comandos dentro do PDB

| Comando | Significado | Uso |
|---|---|---|
| `b <função/linha>` | breakpoint | Parar antes do ponto suspeito |
| `b` | lista breakpoints | Conferir pontos de parada |
| `c` | continue | Continuar até próximo breakpoint/erro |
| `n` | next | Próxima linha sem entrar na chamada |
| `s` | step | Entra na função chamada |
| `p <expr>` | print expression | Inspecionar variável/expressão |
| `pp <expr>` | pretty print | Estruturas maiores |
| `where` | call stack | Ver cadeia de frames |
| `bt` | backtrace | Outra forma de ver stack |
| `up` | frame acima | Ir para quem chamou |
| `down` | frame abaixo | Voltar para chamado |
| `list` | código ao redor | Contextualizar linha atual |
| `q` | quit | Sair do debugger |

Fluxo mental:

```text
sintoma
→ ler stack trace
→ hipótese
→ breakpoint
→ observar estado real
→ seguir call stack
→ provar causa
→ corrigir
→ retestar/regressão
```

---

# 00.6 — Logs e observabilidade

## Capturar e consultar logs

| Comando | Para que serve |
|---|---|
| `python3 app.py > app.log 2>&1` | Captura stdout + stderr |
| `grep checkout app.log` | Filtra evento/termo específico |
| `grep ERROR app.log` | Procura erros |
| `grep checkout_failed app.log` | Procura evento específico |
| `tail app.log` | Últimas linhas |
| `tail -n 20 app.log` | Últimas 20 linhas |
| `tail -f app.log` | Acompanha novas linhas em tempo real |
| `grep ERROR app.log | wc -l` | Conta linhas de erro |

Pergunta guia: **se esta operação falhar amanhã, quais evidências eu vou desejar ter registrado?**

Nunca registrar em logs: senha, token, API key, cookie de sessão, dados bancários ou outros segredos/dados sensíveis.

---

# 00.7 — Profiling básico

## Medição rápida

| Comando | Para que serve |
|---|---|
| `time python3 app.py` | Mede tempo total e CPU de uma execução |
| `time bash run.sh` | Mede o runner completo |

Leitura:

- `real` = tempo de relógio percebido
- `user` = CPU em user space
- `sys` = CPU gasta pelo kernel em favor do processo

`real` alto com `user/sys` baixos sugere **espera/I/O**, não CPU intensa.

## Python `cProfile`

| Comando | Para que serve |
|---|---|
| `python3 -m cProfile app.py` | Perfil geral de funções |
| `python3 -m cProfile -s cumulative app.py` | Ordena por tempo acumulado; excelente para achar hotspot |
| `python3 -m cProfile -s calls app.py` | Ordena por número de chamadas |

Colunas importantes:

- `ncalls` = número de chamadas
- `tottime` = tempo dentro da própria função
- `cumtime` = função + chamadas feitas por ela

## CPU e memória no sistema

| Comando | Para que serve |
|---|---|
| `/usr/bin/time -v python3 app.py` | Tempo + métricas extras, incluindo pico de memória residente |
| `top` | Processos e consumo de CPU/memória em tempo real |
| `htop` | Alternativa amigável, quando instalada |

Pergunta guia: **qual evidência mostra onde o custo está concentrado?**

Fluxo:

```text
baseline
→ profiler
→ hotspot
→ hipótese
→ uma alteração
→ mesma medição
→ comparar antes/depois
```

---

# 00.8 — Laboratório integrador: comandos de operação

```bash
# atualizar clone
git pull

# entrar no laboratório
cd real-learning-labs/stage-00-integrator

# criar branch de trabalho
git switch -c stage-00-fix

# executar
bash run.sh

# verificar exit code
echo $?

# baseline de performance
time bash run.sh

# localizar hotspot
python3 -m cProfile -s cumulative app.py

# investigar histórico do arquivo
git log --oneline -- app.py

# investigar um commit
git show <HASH> -- app.py

# comparar commit com seu pai
git diff <HASH>^ <HASH> -- app.py
```

## Investigação que estamos praticando

```text
OBSERVAÇÃO
↓
EVIDÊNCIA
↓
HIPÓTESE
↓
EXPERIMENTO
↓
RESULTADO
↓
CAUSA PROVADA
↓
CORREÇÃO
↓
RETESTE
↓
MEDIÇÃO ANTES × DEPOIS
```

---

# Receitas rápidas

## “Não é um repositório Git”

```bash
pwd
ls -la
```

Procure `.git`. Se o projeto ainda não foi clonado:

```bash
git clone <URL>
cd <repositorio>
git status
```

## “O programa falhou”

```text
1. Leia a mensagem e stack trace inteiro.
2. Não edite imediatamente.
3. Formule hipótese.
4. Use debugger se puder reproduzir.
5. Use logs se precisar reconstruir uma execução passada.
6. Corrija a causa, não apenas a linha onde explodiu.
7. Reteste o caminho corrigido e caminhos antigos.
```

## “O programa está lento”

```bash
time python3 app.py
python3 -m cProfile -s cumulative app.py
```

Depois investigue **o hotspot**, não o código que “parece feio”.

## “Ficou lento depois de uma mudança”

```bash
git log --oneline -- app.py
git show <HASH> -- app.py
git diff <HASH>^ <HASH> -- app.py
```

Cruze o histórico com o profiler.

---

# Regra final

A caixa de ferramentas não existe para decorar comandos.

Ela existe para transformar:

```text
Tenho um sintoma
→ sei qual pergunta fazer
→ sei qual ferramenta fornece evidência
→ testo hipótese
→ provo a causa
```

Novos comandos importantes das próximas fases devem ser adicionados aqui conforme surgirem.