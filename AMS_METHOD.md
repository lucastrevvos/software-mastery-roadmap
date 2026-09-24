# AMS — Adaptive Mastery Scaffolding

## 1. Objetivo

AMS é a metodologia oficial para transformar qualquer tema em aprendizagem com evidência real de domínio.

Quando o aluno disser **“use AMS”**, **“AMS”**, **“continue em AMS”** ou equivalente, o instrutor deve aplicar automaticamente este protocolo sem exigir que o aluno determine o formato pedagógico da atividade.

O aluno não precisa saber se determinado conteúdo exige quiz, terminal, arquivo, ZIP, repositório Git, projeto local, exercício interativo ou outro ambiente. Essa decisão faz parte do papel do instrutor.

## 2. Fluxo-base

**Theory → Checkpoint → Workshop → Lab → Review → Quiz → Project/Gate**

Esse fluxo pode ser adaptado quando houver justificativa pedagógica, mas não deve virar apenas teoria e quizzes quando a competência exige execução prática.

## 3. Princípio central

> **Usar o menor scaffolding que preserve prática autêntica.**

ZIP não é padrão. Quiz não substitui prática quando a habilidade é procedural, técnica, operacional ou de resolução de problemas.

## 4. Escolha automática do ambiente

Antes de criar uma atividade prática, o instrutor deve decidir:

1. A habilidade precisa ser executada ou apenas reconhecida?
2. O ambiente real acrescenta aprendizagem?
3. Criar/configurar o ambiente faz parte da competência?
4. Existe estado inicial complexo que precisa ser reproduzido fielmente?
5. Um único arquivo é suficiente?
6. O histórico Git faz parte do estado?
7. Existe algo objetivamente verificável que justifique checker ou testes?

Escolher o primeiro formato que preserve a experiência real:

**navegador → ambiente local sem starter → arquivo único → ZIP → repositório Git**

## 5. Quando usar cada formato

### Navegador / atividade interativa

Preferir para quizzes, matemática, lógica, trace, ordenação, associação, respostas curtas e exercícios autocontidos.

### Ambiente local sem starter

Usar quando criar e manipular o ambiente faz parte da própria habilidade, como terminal, filesystem, comandos básicos, pequenos programas e configuração inicial.

### Arquivo único

Usar quando a atividade depende de um artefato específico, como CSV, dataset, log, script, configuração, SQLite ou documento.

### Starter ZIP

Usar somente quando o estado inicial é necessário e recriá-lo manualmente seria ruído, não aprendizagem.

Gatilhos fortes:

- múltiplos arquivos coordenados;
- código quebrado para debugging;
- testes automatizados ou checker;
- fixtures;
- banco pré-populado;
- estrutura de diretórios importante;
- Docker/Compose;
- múltiplos serviços;
- configuração que precisa nascer em estado conhecido;
- falha específica a reproduzir;
- modificação de sistema existente.

**Nunca adicionar ZIP apenas para deixar o laboratório mais sofisticado.**

### Repositório Git

Usar em vez de ZIP quando histórico, commits ou refs fizerem parte do problema: branches, merge, rebase, tags, conflitos, bisect ou regressões.

### Projeto do zero

Não entregar starter quando construir a estrutura inicial for parte explícita da competência.

## 6. Ciclo cognitivo da prática

**Predict / Trace → Build → Execute → Observe → Debug / Repair → Explain → Transfer → Retest**

## 7. Validação

Quando a competência gerar resultado objetivamente verificável, usar validação automática quando útil: unit tests, integration tests, checker local, comparação de output, schema, SQL esperado, invariantes ou scripts de verificação.

O checker não substitui compreensão; ele serve como evidência e feedback.

## 8. Repair + Retest

Erro deve seguir preferencialmente:

**erro → evidência → hipótese → pista graduada → correção → nova tentativa → retest**

Erro conceitual recorrente deve alimentar o Error Ledger.

## 9. Retirada progressiva de ajuda

1. exemplo trabalhado;
2. prática guiada;
3. prática parcialmente guiada;
4. problema independente;
5. transferência para cenário novo;
6. reteste posterior.

## 10. Regras por domínio

### Matemática
Resolução guiada, exercícios interativos, problemas graduais, transferência e retest. Normalmente sem ZIP.

### Linux / terminal / filesystem
Preferir ambiente real. Não fornecer starter quando criar diretórios, arquivos, permissões ou comandos fizer parte da aprendizagem.

### Programação
Usar código real, testes e projetos. Starter apenas quando preparar o estado inicial manualmente não for a competência estudada.

### SQL / bancos
Usar banco ou dataset preparado quando montar os dados não for o objetivo. Se modelagem/schema forem a habilidade, começar do zero.

### Git
Usar repositório real quando histórico, branches, commits ou conflitos fizerem parte da atividade.

### Docker / infraestrutura
Usar starter ZIP ou repositório quando houver múltiplos arquivos, serviços ou configuração complexa que precise nascer em estado conhecido.

### Sistemas distribuídos
Preferir sistemas preparados quando o objetivo for investigar retries, idempotência, concorrência, filas, timeouts, consistência, falhas parciais ou observabilidade.

### Arquitetura / system design
Preferir cenários, requisitos incompletos, trade-offs, diagramas e defesa de decisões. Não forçar editor de código quando código não for o objeto da aprendizagem.

## 11. Responsabilidade do instrutor

O instrutor deve determinar automaticamente o formato pedagógico adequado.

O aluno não deve precisar pedir ZIP, teste, terminal, repositório ou projeto. Essas decisões fazem parte do AMS.

## 12. Evidência de domínio

AMS não considera conteúdo visto como domínio. O objetivo é produzir evidência de que o aluno consegue:

- explicar;
- traçar;
- construir;
- executar;
- observar;
- diagnosticar;
- corrigir;
- transferir;
- reter.

Quando aplicável, também testar, operar, defender decisões e entregar em ambiente real.

## 13. Comando de ativação

Quando o aluno disser **“Use AMS para me ensinar X”**, **“AMS”** ou equivalente, o instrutor deve carregar e aplicar todo este protocolo automaticamente, preservando o contexto atual do estudo.

## 14. Relação com os demais protocolos

AMS define **como escolher o scaffolding e o ambiente de aprendizagem**.

Ele complementa LAB_PROTOCOL.md, LEARNING_SCIENCE_PROTOCOL.md, JCI_METHOD.md, Error Ledger, Mastery Gates e Recall / Trace / Rebuild / Repair / Transfer / Retest.

AMS funciona como a regra de orquestração pedagógica que decide **qual forma de prática usar para cada competência**.