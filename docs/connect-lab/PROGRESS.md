# Connect Lab — progresso e retomada

Atualizado: 2026-11-26

Fonte de verdade do tutor: [currículo e protocolo](index.html). Referência transversal: [Caderno do Engenheiro](../engineering-notebook.html). Não presumir domínio, execução de código ou sincronização automática.

## Estado atual

- Módulo 01: iniciado (41 desafios validados em nível introdutório; 39/41 acertos na primeira tentativa; Retestes 037.1 e 039.1 corretos; gate completo de runtime ainda pendente).
- Módulos 02 e 09: tópicos antecipados em nível introdutório (HTTP/arquitetura/domínio e testes/qualidade); gates e entregas completas pendentes.
- Módulos 03–08 e 10–12: entregas principais planejadas; transferência conceitual e preparação para entrevista já realizadas pontualmente.
- Currículo original consultado em 25/11/2026: M01 ainda exige aprofundamento de event loop, V8/libuv, memória, async/await, microtasks, I/O, concorrência/paralelismo, workers, streams/buffers, ESM e TypeScript; gate CPU-bound pendente. Não há calendário com datas nem total fixo de aulas; acertos não representam percentual de conclusão. Incremento de transição imutável concluído segundo relato; retomada dos fundamentos de execução na Aula 028 antes de avançar a persistência.
- Repositório de implementação: projeto local connect-lab; remoto e commits do código ainda não confirmados.
- Evidências práticas: aluno confirmou execução bem-sucedida do servidor HTTP nativo, roteamento, Express e middleware de logging e proteção simulada de conversas e agrupamento e extração do Router e do middleware de autenticação e do Conversation Service, além do primeiro teste unitário e ciclo TDD completo, testes negativos, experimento manual de mutação, testes de caracterização, seam temporal, Stub, Fake, Spy, Mock, Dummy, FSM, tabela de transições, integração ao Service, factory, imutabilidade superficial, transição imutável, experimento de Event Loop, bloqueio HTTP CPU-bound, espera assíncrona simulada, leitura assíncrona real, stack trace, referências de objetos, Garbage Collection, retenção de memória/cache limitado, ciclo de vida de Promise, encadeamento de Promises, adoção de resultado, async/await e experimentos de ordem de microtasks, FIFO, Next Tick Queue e setImmediate em contexto de I/O, nas Aulas 002–041; sem logs anexados.

## Aula 001 — Runtime versus framework

- Conceito apresentado: JavaScript/TypeScript, Node.js e Express; servidor HTTP nativo versus framework.
- Evidência 23/11/2026: resposta B, justificativa: “Teremos que usar o runtime do nodejs”. Conceito validado no nível introdutório; sem evidência prática ainda.
- Próxima ação (Aula 002): criar servidor HTTP nativo local, observar callback por requisição e testar GET /health com curl. Depois verificar entendimento antes de introduzir Express.
- Referência: [runtime versus framework no Caderno do Engenheiro](../engineering-notebook.html#connect-runtime-framework).

## Aula 002 — Servidor HTTP nativo e callback

- Evidência 23/11/2026: execução reportada como “Funcionou”; resposta B (dez requisições, dez invocações da callback).
- Conceitos validados no nível introdutório: listener de requisição, req/res, escuta na porta e resposta HTTP. Não implica thread por requisição.
- Referência: [Callback e eventos HTTP](../engineering-notebook.html#connect-http-callback).
- Próxima ação (Aula 003): implementar roteamento manual por método e caminho, GET /health com 200 e fallback 404; testar as duas respostas; desafio de compreensão. Express somente depois.

## Aula 003 — Roteamento HTTP nativo

- Evidência: execução reportada como “Funcionou”; resposta C (POST /health retorna 404 no código atual).
- Conceito validado no nível introdutório: seleção de handler por método e caminho. Explicada distinção entre fallback 404 e 405 para método não permitido; query string é uma limitação da comparação literal.
- Commit local sugerido anteriormente, ainda não confirmado pelo aluno.
- Referência: [Roteamento HTTP](../engineering-notebook.html#connect-http-routing).
- Próxima ação (Aula 004): reproduzir o mesmo contrato GET /health e fallback 404 com Express, instalar a dependência npm e comparar a abstração com o servidor nativo. Testar antes de avançar; um desafio por turno.

## Aula 004 — Express e abstração HTTP

- Evidência: execução reportada como “Funcionou”; resposta C (roteador do Express seleciona o handler).
- Conceitos validados no nível introdutório: abstração do roteamento, integração Express/Node.js; npm, manifesto e lockfile apresentados. Commit local não confirmado.
- Referência: [Framework HTTP e dependências](../engineering-notebook.html#connect-express-abstraction).
- Próxima ação (Aula 005): adicionar middleware global de logging antes das rotas; observar ordem de execução e o papel de next(); testar GET /health e GET /clientes. Um desafio por turno.

## Aula 005 — Middleware pipeline

- Evidência: execução reportada como “Funcionou”; resposta B (middleware que envia 401 sem next não executa o handler).
- Conceitos validados no nível introdutório: next(), responsabilidades transversais e short-circuiting. Logging testado segundo relato; autenticação 401 analisada teoricamente. Commit local não confirmado.
- Referência: [Middleware pipeline](../engineering-notebook.html#connect-middleware-pipeline).
- Próxima ação (Aula 006): experimentar ordem de registro e interrupção antecipada em rota protegida GET /conversations, usando cabeçalho fictício x-lab-token exclusivamente para demonstração local; manter /health público, testar 401 e 200 e verificar posicionamento do middleware. Não tratar token fixo como segurança real.

## Aula 006 — Ordem dos middlewares e acesso protegido

- Evidência: execução reportada como “Funcionou”; resposta C (handler anterior ao middleware de autenticação permite acesso sem a verificação).
- Conceitos validados no nível introdutório: ordem de registro, rota pública, rota protegida e risco de controle de acesso. Token fictício exclusivamente local; JWT ainda não implementado. Commit local não confirmado.
- Referência: [Ordem do pipeline](../engineering-notebook.html#connect-middleware-order).
- Próxima ação (Aula 007): extrair requireAuth como função e registrá-la explicitamente em GET /conversations antes do handler, remover autenticação global; verificar 200 público, 401 protegido sem token, 200 com token e 404 para rota inexistente sem token. Um desafio por turno.

## Aula 007 — Escopo de middleware e composição

- Evidência 24/11/2026: execução reportada como “Funcionou”; resposta B (GET /customers sem associação a requireAuth não está protegido).
- Conceitos validados no nível introdutório: middleware de rota, composição e reutilização. Commit local e resultados individuais dos quatro testes não confirmados.
- Referência: [Escopo de middleware](../engineering-notebook.html#connect-middleware-scope).
- Próxima ação (Aula 008): usar express.Router(), registrar requireAuth no início do grupo privado, montar em /api e incluir GET /conversations e GET /customers no grupo. Manter GET /health público e fallback 404 externo. Testar acesso com e sem token fictício; não expor dados reais. Um desafio por turno.

## Aula 008 — Router e agrupamento de rotas

- Evidência 24/11/2026: execução reportada como “Funcionou”; resposta C (rota /api/messages registrada depois de requireAuth no Router retorna 401 sem token).
- Conceitos validados no nível introdutório: agrupamento, prefixo de montagem e proteção por padrão no grupo. Token simulado; commit local e resultados individuais dos testes não confirmados.
- Referência: [Agrupamento de rotas](../engineering-notebook.html#connect-router-groups).
- Próxima ação (Aula 009): extrair o Router privado, incluindo sua proteção simulada e handlers existentes, para api-router.js; exportar com module.exports e importar em server.js via require. Preservar o contrato HTTP e testar regressão; introduzir Separation of Concerns, módulos CommonJS e refatoração sem criar camadas adicionais. Um desafio por turno.

## Aula 009 — Separation of Concerns e CommonJS

- Evidência 24/11/2026: execução reportada como “Funcionou”; resposta A (refatoração preserva comportamento observável).
- Conceitos apresentados e validados em nível introdutório: SoC, refatoração e módulos CommonJS. Router extraído para api-router.js segundo relato; commit local e resultados individuais dos testes não confirmados.
- Referência: [SoC e refatoração](../engineering-notebook.html#connect-separation-of-concerns).
- Próxima ação (Aula 010): extrair requireAuth para middleware/require-auth.js, manter Router e handlers atuais, explicar SRP como razão de mudança associada a uma responsabilidade/ator e distinguir de SoC; preservar endpoints e testar 401/200. Um desafio por turno.

## Aula 010 — Single Responsibility Principle

- Evidência 24/11/2026: execução reportada como “Funcionou”; resposta C (responsabilidades independentes e razões diferentes para mudar).
- Conceito validado em nível introdutório: SRP, distinção de SoC e extração de requireAuth para middleware/require-auth.js. Token fictício apenas local; commit local e resultados individuais dos testes não confirmados.
- Referência: [SRP](../engineering-notebook.html#connect-srp).
- Próxima ação (Aula 011): introduzir coesão e acoplamento por meio da extração de dados e lógica de consulta de conversas para conversations/conversation-service.js; exportar listConversations(), sem dependência de Express, manter handler responsável pela resposta HTTP e dados atuais. Testar função diretamente e endpoint com token; explicar que dependências explícitas ainda existem e não são necessariamente ruins. Um desafio por turno.

## Aula 011 — Coesão e acoplamento

- Evidência 24/11/2026: execução reportada como “Funcionou”; resposta D (Service não depende diretamente dos componentes HTTP do Express).
- Conceitos validados em nível introdutório: coesão, acoplamento e separação da lógica de consulta do transporte HTTP. listConversations() extraída segundo relato; commit local e saídas individuais não confirmados.
- Referência: [Coesão e acoplamento](../engineering-notebook.html#connect-cohesion-coupling).
- Próxima ação (Aula 012): criar teste unitário com node:test e node:assert/strict para listConversations(), usando Arrange–Act–Assert e node --test; observar uma falha deliberada e restaurar o teste. Não instalar dependências adicionais. Um desafio por turno.

## Aula 012 — Testes unitários e AAA

- Evidência 24/11/2026: execução reportada como “Funcionou”; resposta C (acoplamento aos objetos HTTP aumenta preparação/simulação necessária para teste isolado).
- Conceitos validados em nível introdutório: teste unitário isolado, AAA, assertions e relação com desacoplamento; node:test e node:assert/strict apresentados. Resultado individual do experimento de falha/restauração e commit local não confirmados.
- Referência: [Testes unitários e AAA](../engineering-notebook.html#connect-unit-testing-aaa).
- Próxima ação (Aula 013): primeiro ciclo TDD Red–Green–Refactor, adicionando teste para canCloseConversation(status) que permite encerrar apenas conversa OPEN. Ver falha pela ausência da função; implementar o mínimo, executar toda a suíte e avaliar necessidade de refatorar. Sem alterar endpoints ou persistir estado ainda. Um desafio por turno.

## Aula 013 — TDD: Red–Green–Refactor

- Evidência 24/11/2026: execução reportada como “Funcionou”; resposta B. Aluno confirmou explicitamente: escreveu o teste primeiro, observou a falha, implementou a função, observou aprovação da suíte e avaliou a necessidade de refatoração.
- Conceito validado em nível introdutório: TDD como processo de desenvolvimento; regra canCloseConversation(status) permite OPEN. Primeiro teste cobre apenas OPEN; casos negativos ainda pendentes. Logs e commit local não apresentados.
- Referência: [TDD](../engineering-notebook.html#connect-tdd).
- Próxima ação (Aula 014): acrescentar dois testes negativos WAITING e CLOSED, executar suíte, experimentar temporariamente implementação defeituosa return true e observar que os novos testes detectam a falha, restaurar regra e executar novamente. Explicar que é ampliação de cobertura e experimento manual de mutação, não novo ciclo TDD estrito. Um desafio por turno.

## Aula 014 — Testes positivos, negativos e mutação

- Evidência 24/11/2026: execução reportada como “Funcionou”; resposta C. Aluno confirmou adição dos testes negativos, quatro testes aprovados, introdução de defeito com falhas e restauração da regra correta.
- Conceito validado em nível introdutório: testes cobrem cenários/assertions, e uma suíte verde não garante ausência de bugs; mutação manual ajuda a avaliar capacidade de detecção. Logs e commit local não apresentados.
- Observação do aluno: testar código legado também é um desafio. Incorporar testes de caracterização, identificação de dependências e introdução de seams à trilha de qualidade, sem assumir que o produto da Plug Social é legado.
- Referência: [Testes negativos e mutação](../engineering-notebook.html#connect-negative-testing).
- Próxima ação (Aula 015, inserida antes de máquinas de estados): criar exemplo isolado de classificação legada de conversas, observar comportamento existente, registrar testes de caracterização incluindo comportamento surpreendente, distinguir comportamento observado de requisito correto e não alterar a regra sem decisão de negócio. Preservar código atual do produto. Um desafio por turno.

## Aula 015 — Testes de caracterização de código legado

- Evidência 24/11/2026: execução reportada como “Funcionou”; resposta D (caracterizar comportamento existente, investigar requisitos e decidir alteração conscientemente).
- Conceitos validados em nível introdutório: characterization testing, distinção de comportamento observado e desejado, valores-limite (30/31 minutos). Contagem individual de testes, mudança deliberada da fronteira e commit local não confirmados.
- Referência: [Testes de caracterização](../engineering-notebook.html#connect-characterization).
- Próxima ação (Aula 016): introduzir um seam em função legada de cálculo de prioridade dependente de Date.now(), preservando chamadas existentes com parâmetro now padrão; usar relógio controlado em teste determinístico sem sleep ou mock global. Explicar injeção de dependência por parâmetro e diferenciar seam de test double; não alterar regras anteriores nem avançar para máquinas de estados ainda. Um desafio por turno.

## Aula 016 — Test Seams e injeção de dependência

- Evidência 24/11/2026: execução reportada como “Funcionou”; resposta B (introduzir ponto de substituição para fornecer dependência controlada).
- Conceitos validados em nível introdutório: seam, fornecimento de timestamp por parâmetro e teste determinístico; distinção entre ponto de substituição e substituto. Contagem individual dos testes, logs e commit local não apresentados.
- Referência: [Test Seams](../engineering-notebook.html#connect-test-seams).
- Próxima ação (Aula 017): introduzir Test Doubles focando somente Stub; criar legacy/customer-priority.js com getPriorityForCustomer(customerId, waitingMinutes, getCustomerType), reutilizando calculatePriority da Aula 015. Testar com função síncrona injetada que devolve VIP ou REGULAR; não chamar API/banco real, não introduzir framework de mocks. Distinguir retorno predefinido de verificação de interações. Manter demais tipos de double para aulas posteriores. Um desafio por turno.

## Aula 017 — Test Doubles: Stub

- Evidência 24/11/2026: execução reportada como “Funcionou”; resposta C (função que fornece saldo predefinido é um Stub).
- Conceitos validados em nível introdutório: test double, Stub e resposta controlada por função injetada; distinção de verificação de interações. Consulta CRM simulada e síncrona. Contagem individual dos testes, logs e commit local não apresentados.
- Referência: [Stub](../engineering-notebook.html#connect-stub).
- Próxima ação (Aula 018): introduzir Fake com repositório de clientes em memória (Map, save e getCustomerType), usado exclusivamente em teste de getPriorityForCustomer. Verificar a mudança de REGULAR para VIP no mesmo cliente e manter a suíte anterior. Não adicionar banco real, frameworks nem outros tipos de double; explicitar que Fake não reproduz garantias reais de persistência. Um desafio por turno.

## Aula 018 — Test Doubles: Fake

- Evidência 24/11/2026: execução reportada como “Funcionou”; resposta D (repositório funcional em memória é um Fake).
- Conceitos validados em nível introdutório: Fake, estado em memória, Map chave-valor, diferença de Stub e limites de simulação de banco. Contagem individual dos testes, logs e commit local não apresentados.
- Referência: [Fake](../engineering-notebook.html#connect-fake).
- Próxima ação (Aula 019): introduzir Spy manual com array de chamadas; criar função closeConversation(conversation, notifyCustomer) em conversations/conversation-service.js que retorna nova conversa CLOSED para OPEN e solicita notificação com ID; para status não permitido retorna a conversa original sem notificar. Reutilizar canCloseConversation; adicionar dois testes de interação para quantidade, argumento e ausência de chamada; não integrar ao HTTP nem enviar notificações reais. Um desafio por turno.

## Aula 019 — Test Doubles: Spy

- Evidência 24/11/2026: execução reportada como “Funcionou”; resposta A (função que registra chamadas e argumentos é Spy).
- Conceitos validados em nível introdutório: Spy, verificação de estado e de interações, notificação simulada no fechamento da conversa. Contagem individual dos testes, logs e commit local não apresentados.
- Observação espontânea: aluno perguntou como o ID chega ao callback sem ser passado na chamada externa. Explicadas funções de primeira classe, higher-order function, callback síncrono, closure sobre calls e equivalência conceitual com delegate Action<int> do C#. O ID é passado explicitamente na invocação interna, não capturado por closure. Sem exercício adicional sobre isso, conforme solicitado.
- Referência: [Spy e callbacks](../engineering-notebook.html#connect-spy).
- Próxima ação (Aula 020): diferenciar Mock de Spy por expectativas de interação pré-definidas; adicionar apenas um teste com mock manual que exige exatamente uma notificação com ID 123, rejeita chamadas inesperadas e verifica ausência de chamada no final. Reutilizar closeConversation sem alterar produção; explicar que nomenclatura varia entre ferramentas. Um desafio por turno.

## Aula 020 — Test Doubles: Mock

- Evidência 24/11/2026: execução reportada como “Funcionou”; resposta C (expectativas predefinidas sobre interação caracterizam Mock na classificação clássica).
- Conceitos validados em nível introdutório: Mock, expectativas de argumento e quantidade de chamadas, distinção conceitual de Spy e variação de nomenclatura entre ferramentas. Logs, contagem individual e commit local não apresentados.
- Referência: [Mock](../engineering-notebook.html#connect-mock).
- Próxima ação (Aula 021): finalizar os cinco tipos clássicos com Dummy; acrescentar um teste de closeConversation para status CLOSED fornecendo uma função vazia como argumento não utilizado, sem modificar produção. Verificar estado e identidade do objeto retornado, explicar que Dummy não verifica interações e que Spy seria necessário para comprovar ausência de chamada. Um desafio por turno; depois retomar regras de negócio e máquinas de estados.

## Aula 021 — Test Doubles: Dummy

- Evidência 24/11/2026: execução reportada como “Funcionou”; resposta A (substituto fornecido apenas para preencher parâmetro sem uso no cenário é Dummy).
- Conceitos validados em nível introdutório: Dummy, retorno antecipado, identidade de objetos com assert/strict e diferença entre preencher parâmetro e verificar ausência de interação. Cinco tipos clássicos de Test Doubles concluídos no nível introdutório. Logs, contagem individual e commit local não apresentados.
- Referência: [Dummy](../engineering-notebook.html#connect-dummy).
- Próxima ação (Aula 022): introduzir máquina de estados finita para conversas, com WAITING --ASSIGN--> OPEN e OPEN --CLOSE--> CLOSED; transições não previstas preservam estado no exercício. Criar conversations/conversation-state.js com transitionConversation(status, event) e três testes (atribuir, encerrar, atribuição inválida após encerramento). Não modificar serviço existente ou HTTP nesta etapa; regra de atribuição é decisão didática, não requisito confirmado da Plug Social. Um desafio por turno.

## Aula 022 — Finite State Machine

- Evidência 24/11/2026: execução reportada como “Funcionou”; resposta C (WAITING + CLOSE preserva WAITING; ASSIGN leva a OPEN; CLOSE leva a CLOSED).
- Conceitos validados em nível introdutório: estado, evento, transição permitida, transição inválida preservando estado. Logs, contagem individual e commit local não apresentados.
- Direção do produto reafirmada pelo aluno: construir plataforma omnichannel própria inspirada nas funcionalidades públicas da Plug Social, com evolução real de backend, interface Angular, canais, mensagens em tempo real, filas, persistência, automação e IA. Preservar os 12 módulos e o Método DECA (conceito primeiro, implementação depois, transferência por último; um pequeno passo por turno). Não alegar conhecimento da arquitetura proprietária; integrações reais dependem de acesso e credenciais.
- Referência: [FSM](../engineering-notebook.html#connect-fsm).
- Próxima ação (Aula 023): refatorar transitionConversation em tabela de transições com Map aninhado e fallback via optional chaining e nullish coalescing; preservar contrato e estados, executar testes existentes, acrescentar caso WAITING + CLOSE caso ausente. Não alterar Service ou HTTP. Um desafio por turno.

## Aula 023 — Transition Table

- Evidência 25/11/2026: execução reportada como “Funcionou”; resposta C (OPEN + ASSIGN não está na tabela e preserva OPEN).
- Conceitos validados em nível introdutório: tabela de transições, Map aninhado, optional chaining e nullish coalescing no fallback. Logs, contagem individual e commit local não apresentados.
- Dúvida espontânea sobre persistência: explicada diferença entre definição de transições e estado/histórico de cada conversa. Direção arquitetural proposta: regras fundamentais estáticas no código em memória, estado e histórico no banco (MongoDB previsto) e configuração de automações por cliente persistida futuramente com validação/versionamento. Não afirmar que essa arquitetura pertence à Plug Social nem que persistência já foi implementada.
- Referência: [Transition Table](../engineering-notebook.html#connect-transition-table).
- Próxima ação (Aula 024): integrar FSM ao Conversation Service como fonte única das regras de transição. Importar transitionConversation; canCloseConversation deriva permissão de mudança de estado pelo evento CLOSE; closeConversation usa próximo estado calculado pela FSM, retorna conversa original sem notificar se não houver mudança e mantém notificação simulada em transição válida. Preservar contrato existente e executar suíte; acrescentar teste Spy verificando ausência de notificação para CLOSED. Explicar limitação da comparação de estados caso futuramente haja self-transitions. Não alterar HTTP nem persistência nesta etapa. Um desafio por turno.

## Aula 024 — Single Source of Truth

- Evidência 25/11/2026: execução reportada como “Funcionou”; resposta B (centralizar a definição da regra evita divergências entre componentes).
- Conceitos validados em nível introdutório: SSOT, centralização das regras de transição na FSM, preservação de comportamento por regressão e verificação de interação via Spy. Limitação de comparação de estados sem self-transitions explicada. Logs, resultados individuais e commit local não apresentados.
- Referência: [SSOT](../engineering-notebook.html#connect-ssot).
- Próxima ação (Aula 025): introduzir invariantes de domínio na criação de conversa por uma factory createConversation(id, customer) em conversations/conversation.js: ID inteiro positivo, nome não vazio após trim, estado inicial WAITING definido internamente. Acrescentar três testes (criação válida, ID inválido, cliente em branco), sem alterar listagem, FSM, Service ou HTTP. Explicar que factory protege apenas objetos criados por ela, não mutações posteriores, unicidade ou existência de cliente no banco. Regras didáticas do Connect Lab. Um desafio por turno.

## Aula 025 — Domain Invariants

- Evidência 25/11/2026: execução reportada como “Funcionou”; resposta C (saldo não negativo em conta sem cheque especial é invariante de domínio).
- Conceitos validados em nível introdutório: invariantes, factory function e validação na criação; assert.deepEqual e assert.throws apresentados. Estado WAITING é condição inicial, não invariante permanente. Logs, resultados individuais e commit local não apresentados.
- Referência: [Domain Invariants](../engineering-notebook.html#connect-domain-invariants).
- Próxima ação (Aula 026): primeiro passo de encapsulamento por proteção de snapshots imutáveis: usar Object.freeze no objeto retornado por createConversation, mantendo formato e contrato; adicionar teste em modo estrito verificando TypeError ao alterar status e preservação de WAITING. Explicar freeze superficial, diferença entre encapsulamento e imutabilidade, limitação de objetos criados por outros caminhos e que Service/FSM ainda não foram integrados à factory. Não adicionar classes, banco ou HTTP nesta etapa. Um desafio por turno.

## Aula 026 — Encapsulation e Immutability

- Evidência 25/11/2026: execução reportada como “Funcionou”; resposta B (Object.freeze é superficial, objeto address aninhado continua mutável).
- Conceitos validados em nível introdutório: imutabilidade superficial, strict mode, distinção de encapsulamento, limites da proteção. Logs, resultados individuais e commit local não apresentados.
- Aluno pediu localização no cronograma: conferido currículo original de 12 módulos, sem datas fixas; M01 aberto, conteúdo de M02/M09 antecipado, gates não concluídos. Retomar runtime/event loop após a próxima pequena integração, sem eliminar tópicos pendentes.
- Referência: [Imutabilidade](../engineering-notebook.html#connect-immutability).
- Próxima ação (Aula 027): proteger snapshot retornado por closeConversation com Object.freeze sobre novo objeto spread, preservando comportamento e identidade no caminho inválido; acrescentar um teste com objeto criado pela factory em WAITING, transição ASSIGN preparada explicitamente como snapshot congelado, e closeConversation com notificação simulada, verificando original OPEN, novo CLOSED, identidade distinta e Object.isFrozen. Não integrar HTTP nem banco; próxima aula após validação: retomar event loop. Um desafio por turno.

## Aula 027 — Immutable State Transition

- Evidência 25/11/2026: execução reportada como “Funcionou”; resposta D (spread cria novo objeto mutável, preservando original congelado e seu estado).
- Conceitos validados em nível introdutório: cópia superficial, identidade de referência versus ID, novo snapshot protegido por Object.freeze. Serviço mantém identidade no caminho sem transição. Logs, resultados individuais e commit local não apresentados.
- Referência: [Immutable State Transition](../engineering-notebook.html#connect-immutable-transition).
- Próxima ação (Aula 028): retomar módulo 01 original, introduzir Event Loop e bloqueio da thread de JavaScript em experimento isolado experiments/event-loop.js: agendar setTimeout de 0 ms, executar laço síncrono limitado por aproximadamente 2 s usando performance.now(), observar ordenação e atraso do callback, comparar sem o laço. Não modificar a API; próximo passo demonstrar efeito em requisições HTTP concorrentes e aprofundar runtime. Um desafio por turno.

## Aula 028 — Event Loop

- Evidência 25/11/2026: execução reportada como “Funcionou”; resposta B (console.log síncrono executa antes do callback de setTimeout com atraso zero).
- Conceitos validados em nível introdutório: agendamento de timer, execução síncrona, bloqueio da thread JavaScript e distinção entre assincronia e paralelismo. Logs, tempos medidos e commit local não apresentados.
- Referência: [Event Loop](../engineering-notebook.html#connect-event-loop).
- Próxima ação (Aula 029): demonstrar impacto de processamento CPU-bound em servidor HTTP isolado experiments/blocking-server.js, escutando somente 127.0.0.1:3001, com /heavy executando laço síncrono limitado a aproximadamente 3 s e /health imediato. Cliente experiments/blocking-client.js em processo separado, Node 18+, mede /health sozinho e depois durante /heavy, iniciando /health 200 ms após disparo de /heavy; ordem depende do agendamento, verificar logs e repetir se necessário. Não modificar API principal nem publicar rota de bloqueio. Um desafio por turno; próxima etapa contrastar espera assíncrona I/O-bound simulada por timer, sem alegar que timer torna cálculo paralelo.

## Aula 029 — Event Loop Blocking em HTTP

- Evidência 25/11/2026: execução reportada como “Funcionou”; resposta C (processamento CPU-bound síncrono atrasa outros callbacks da mesma thread JavaScript).
- Conceitos validados em nível introdutório: CPU-bound versus I/O-bound, latência compartilhada por requisições concorrentes, experimento isolado HTTP local. Logs, tempos medidos e commit local não apresentados; gate completo de runtime ainda pendente.
- Dúvida espontânea: por que await request('/health') na medição isolada e ausência de await imediato nas chamadas concorrentes? Explicados sequenciamento, início da operação com Promise retornada, espera posterior com Promise.all, suspensão da função assíncrona sem bloquear toda a thread e analogia com Task.WhenAll em C#. Não inferir domínio de Promises por essa explicação.
- Referência: [CPU-bound e concorrência](../engineering-notebook.html#connect-http-blocking).
- Próxima ação (Aula 030): adicionar /waiting ao servidor experimental com setTimeout de 3000 ms que responde no callback, preservando /heavy e /health. Parametrizar caminho da primeira requisição no cliente por argumento CLI (default /heavy). Comparar as duas execuções e observar /health respondendo enquanto /waiting aguarda. Timer simula espera, não é I/O real nem paraleliza trabalho CPU-bound; não modificar API principal. Um desafio por turno. Próximo passo: aprofundar I/O real e papel de libuv/SO.

## Aula 030 — Non-blocking I/O

- Evidência 25/11/2026: execução reportada como “Funcionou”; resposta C (outras requisições podem ser processadas durante espera HTTP assíncrona). Timer simula espera e não é I/O real. Tempos finais e commit local não apresentados.
- Erro observado: Git Bash converteu /heavy para C:/Program Files/Git/heavy, causando ERR_INVALID_URL. Orientadas duas soluções: MSYS_NO_PATHCONV=1 e argumentos CLI heavy/waiting sem barra, construindo a rota no código. Não confirmado qual solução foi aplicada.
- Preferência permanente confirmada pelo aluno: laboratórios animados interativos no Método DECA, quando úteis, com foco em Call Stack, Heap, Event Loop, Promises, libuv, Worker Threads, RabbitMQ e WebSockets. Diretriz incorporada ao protocolo oficial em index.html; simulações não substituem experimentos reais nem um desafio por turno.
- Referência: [Non-blocking I/O](../engineering-notebook.html#connect-nonblocking-io).
- Próxima ação (Aula 031): apresentar libuv com animação de delegação e retorno de I/O, distinguindo pool de threads para filesystem e mecanismos de I/O de rede do SO. Criar experiments/libuv.js com fs.readFile(__filename, 'utf8', callback) e logs antes/depois da chamada, observando callback posterior ao código síncrono. Não adicionar rotas nem afirmar que todo I/O usa thread pool. Um desafio por turno; depois aprofundar Call Stack e Heap.

## Aula 031 — libuv

- Evidência 25/11/2026: execução reportada como “Funcionou”; resposta D (leitura de arquivo utiliza pool da libuv, callback JavaScript executa na thread JavaScript).
- Conceitos validados em nível introdutório: distinção entre V8, APIs Node.js, libuv, pool de threads e I/O de rede do SO. Leitura assíncrona real via fs.readFile; ordem de logs esperada, sem logs ou commit local apresentados. A animação didática não demonstra rastreamento real de threads.
- Referência: [libuv](../engineering-notebook.html#connect-libuv).
- Próxima ação (Aula 032): Call Stack e LIFO; animar entrada/saída de funções receiveMessage → handleMessage → normalizeMessage, com reprodução, pausa e avanço por etapa. Criar experiments/call-stack.js com chamadas síncronas aninhadas, console.trace em normalizeMessage e retorno do texto normalizado por trim. Observar frames em ordem do mais recente ao chamador; distinguir stack trace de instrumentação ao vivo. Não alterar produto ou aprofundar heap ainda. Um desafio por turno; próxima etapa Heap e referências.

## Aula 032 — Call Stack

- Evidência 25/11/2026: execução reportada como “Funcionou”; resposta B, com justificativa de que C foi a última chamada, precedida de B e A, portanto sai primeiro pelo princípio LIFO.
- Conceitos validados: ordem LIFO de chamadas síncronas, push/pop, leitura introdutória de stack trace; terminologia corrigida para Last In, First Out. Logs e commit local não apresentados. Animação omite frames internos.
- Referência: [Call Stack](../engineering-notebook.html#connect-call-stack).
- Próxima ação (Aula 033): Memory Heap e referências. Animação com variáveis conversation e alias apontando ao mesmo objeto, mutação observável em ambas e cópia superficial com spread criando outro objeto; controles de reprodução/pausa/reinício e passo. Criar experiments/heap.js e observar igualdade por referência e estados antes/depois. Usar modelo didático de referências, sem afirmar localização física fixa de variáveis ou endereços reais no V8. Não modificar produto nem aprofundar GC nesta etapa. Um desafio por turno; próxima etapa Garbage Collection e alcançabilidade.

## Aula 033 — Memory Heap

- Evidência 25/11/2026: execução reportada como “Funcionou”; resposta C e justificativa de que a alteração por b afeta o objeto acessado por a. Refinada a terminologia: b e a referenciam o mesmo objeto, não uma variável à outra.
- Conceitos validados em nível introdutório: heap, aliasing, igualdade referencial, cópia superficial via spread e distinção de const versus imutabilidade. Modelo visual não representa endereços físicos ou alocação exata do V8. Logs e commit local não apresentados.
- Referência: [Memory Heap](../engineering-notebook.html#connect-heap).
- Próxima ação (Aula 034): Garbage Collector e alcançabilidade. Animar duas referências fortes ao mesmo objeto e remoção de cada uma; objeto torna-se elegível para coleta somente quando inalcançável a partir das raízes, sem garantir momento da coleta. Criar experiments/garbage-collector.js com array moderado de objetos, alias, remoção das referências, process.memoryUsage().heapUsed e global.gc opcional via node --expose-gc; explicar que métricas são variáveis e coleta não equivale à liberação imediata de RAM ao SO. Não introduzir algoritmos de GC avançados nem alterar produto. Um desafio por turno; próximo passo retenção de memória e memory leak.

## Aula 034 — Garbage Collector

- Evidência 25/11/2026: execução reportada como “Funcionou”; resposta B (array cache mantém referência forte ao objeto mesmo após conversation = null).
- Conceitos validados em nível introdutório: alcançabilidade, raízes, elegibilidade para coleta, diferença entre remoção de referência e recuperação de memória. Experimento com heapUsed e solicitação explícita de GC. Logs, valores reais e commit local não apresentados.
- Referência: [Garbage Collector](../engineering-notebook.html#connect-garbage-collector).
- Próxima ação (Aula 035): memory leak por retenção em cache sem limite, com animação comparativa de crescimento e cache limitado. Criar experiments/memory-leak.js, usando Map de longa duração, cinco lotes de 10000 objetos e modo bounded com limite de 10000 entradas por remoção das mais antigas; medir size e heapUsed após solicitação opcional de GC. Executar modos leak e bounded em processos separados com node --expose-gc; argumentos CLI sem barra. Diferenciar cache intencional de retenção indefinida de dados desnecessários; tamanho limitado não garante ausência de outros vazamentos. Não alterar API principal. Um desafio por turno; próxima etapa retomar Promises.

## Aula 035 — Memory Leak

- Evidência 25/11/2026: execução reportada como “Funcionou”; resposta D (remover sessões desnecessárias do Map permite coleta dos objetos que se tornam inalcançáveis). Não duplicar registro da Aula 034, reenviada antes da resposta atual.
- Conceitos validados em nível introdutório: retenção indevida, cache limitado, remoção FIFO, distinção entre tratar causa e aumentar memória/forçar GC. Valores reais de heapUsed, logs e commit local não apresentados.
- Referência: [Memory Leak](../engineering-notebook.html#connect-memory-leak).
- Próxima ação (Aula 036): Promise como representação de resultado futuro, estados pending, fulfilled e rejected, transição única a estado settled. Animação interativa de sucesso e falha, com reprodução/pausa/reinício. Criar experiments/promises.js com simulação de envio de mensagem via new Promise, executor síncrono, setTimeout de 1 s e resolve/reject conforme argumento CLI success/failure; consumir com then e catch, logs antes/depois da criação. Explicar que Promise não é thread, não torna CPU-bound não bloqueante e que resolve com valor simples difere de adoção de outra Promise (adiar detalhes). Não modificar API principal. Um desafio por turno; próxima etapa encadeamento de Promises.

## Aula 036 — Promises

- Evidência 25/11/2026: execução reportada como “Funcionou”; resposta B (resolve com valor simples determina fulfilled; reject posterior não altera resultado).
- Conceitos validados em nível introdutório: pending, fulfilled, rejected, settled, executor síncrono e consumo assíncrono via then/catch. Não inferir domínio de microtasks, adoção de thenables ou encadeamento. Logs e commit local não apresentados.
- Referência: [Promise lifecycle](../engineering-notebook.html#connect-promise-lifecycle).
- Próxima ação (Aula 037): Promise chaining com propagação de valores e rejeições. Criar experiments/promise-chaining.js com receiveMessage retornando Promise resolvida, saveMessage(message) simulando persistência via timer e sucesso/falha por argumento CLI success/failure, notifyOperator(savedMessage) retornando confirmação. Encadear receiveMessage().then(saveMessage).then(notifyOperator).then(console.log).catch(handler), demonstrar que retorno de Promise é aguardado pela próxima etapa e que rejeição pula handlers de sucesso subsequentes. Animação comparativa sucesso/falha com pausa e reinício; persistência e notificação simuladas, sem alterar API principal. Um desafio por turno; próximo passo reescrever cadeia com async/await e try/catch.

## Aula 037 — Promise Chaining

- Evidência 25/11/2026: execução reportada como “Funcionou”; resposta D (objeto Promise), incorreta. Resultado correto C (25). Sem justificativa apresentada; causa cognitiva específica não confirmada. Logs e commit local não apresentados.
- Lacuna a verificar: distinguir objeto Promise retornado pelo callback do valor de cumprimento recebido pelo próximo then; cada then retorna nova Promise que adota o resultado do callback, inclusive outra Promise. Não marcar domínio de encadeamento ainda. 36 acertos em 37 primeiras tentativas.
- Próxima ação (Reteste 037.1): explicar com três Promises nomeadas e animação de adoção de resultado; executar experimento curto isolado que compara Promise com valor recebido no callback, com timer para demonstrar espera. Aplicar um único desafio de transferência com valores diferentes e justificativa opcional. Não avançar para async/await até validar o conceito. Registrar no Caderno do Engenheiro quando consolidado, preservando erro inicial e reteste.

## Reteste 037.1 — Promise Adoption

- Evidência 25/11/2026: execução reportada como “Funcionou”; resposta D correta (number 15). Reteste com valores diferentes do desafio inicial. Lacuna de distinção entre objeto Promise e valor recebido no then recuperada em nível introdutório; explicação autônoma ainda não apresentada e deverá ser verificada em recall futuro. Logs e commit local não apresentados.
- Métricas: 37 desafios validados, 36/37 acertos na primeira tentativa (97,3%); 1 reteste correto. Preservar erro inicial, sem recontá-lo como acerto de primeira.
- Referência: [Promise Chaining](../engineering-notebook.html#connect-promise-chaining).
- Próxima ação (Aula 038): reescrever apenas a cadeia da Aula 037 em uma função async processMessage com await receiveMessage(), await saveMessage(message), notifyOperator(savedMessage) síncrona e try/catch; preservar o arquivo anterior copiando para experiments/async-await.js. Chamar processMessage() e observar código externo prosseguir enquanto a função aguarda. Animação da suspensão/retomada da função e fluxo sucesso/falha; async retorna Promise, await suspende a continuação, não bloqueia a thread, e rejeição é lançada no ponto do await. Um desafio por turno. Próxima etapa microtasks e ordem de execução.

## Aula 038 — Async/Await

- Evidência 26/11/2026: execução reportada como “Funcionou”; resposta C correta (a instanceof Promise é true; typeof b é number). Logs e commit local não apresentados.
- Métricas: 38 desafios validados em nível introdutório, 37/38 acertos na primeira tentativa (97,4%), 1 reteste correto. Gate completo de runtime pendente.
- Aprofundamentos espontâneos: diagramas da microtask queue gerenciada pelo V8, integração Node/V8/libuv, fases do Event Loop e checkpoints entre callbacks; comparação com CLR, Task e Thread Pool do ASP.NET Core (continuação pode mudar de thread, Task concluída pode prosseguir sincronamente); trade-offs CPU-bound/I/O-bound sem alegar superioridade universal; concorrência sem paralelismo, race condition check-then-act em monólito, atualização condicional no banco e desafios de arquitetura orientada a eventos. Não contabilizar como desafios adicionais nem inferir domínio. Revisitar controle de concorrência na etapa de persistência/sistemas distribuídos.
- Referências: [Async/Await](../engineering-notebook.html#connect-async-await), [Race Condition](../engineering-notebook.html#connect-async-race).
- Próxima ação (Aula 039): microtasks e ordem FIFO no checkpoint. Criar experiments/microtasks.js com logs síncronos, setTimeout, Promise.resolve().then e queueMicrotask; uma microtask adiciona outra ao final da fila. Visualizar fila e saída, sem nextTick ou setImmediate nesta etapa. Explicar que a fila drena incluindo novas microtasks antes de prosseguir ao timer elegível; não confundir prioridade com preempção de JS síncrono. Um desafio de ordenação diferente do experimento; depois estudar process.nextTick e setImmediate separadamente.

## Aula 039 — Microtasks e FIFO

- Evidência 26/11/2026: execução reportada como “Funcionou”; resposta B (1, 6, 2, 3, 4, 5) incorreta; resultado correto D (1, 6, 2, 4, 3, 5). Sem justificativa; não inferir causa cognitiva específica. Logs e commit local não apresentados.
- Lacuna a verificar: uma microtask agendada durante a execução de outra entra no final da fila; não passa à frente dos trabalhos que já estavam enfileirados. Resposta escolhida preserva a ordem síncrona e o timer no final, mas inverte 3 e 4. Não marcar domínio de microtasks ainda.
- Métricas: 38 desafios validados de 39 respondidos, 37/39 acertos de primeira tentativa; Reteste 037.1 correto, Reteste 039.1 pendente.
- Próxima ação (Reteste 039.1): visualizar fila FIFO passo a passo, com microtask pai agendando duas novas microtasks enquanto outra já aguarda; experimento curto isolado, seguido de um único desafio de transferência com uma cadeia de then e queueMicrotask. Explicar diferença entre registrar uma reação em Promise pendente e enfileirar trabalho elegível. Se reteste correto, registrar conceito no Caderno do Engenheiro preservando erro inicial e avançar a process.nextTick em CommonJS. Não contabilizar reteste como novo desafio numerado.

## Reteste 039.1 — Microtask FIFO

- Evidência 26/11/2026: execução reportada como “Funcionou”; resposta C correta (A, B, C, D), em novo exemplo que combina Promise Chaining e queueMicrotask. Recuperada em nível introdutório a lacuna de inserção ao final da fila; explicação autônoma ainda não apresentada, revisar em recall futuro. Logs e commit local não apresentados.
- Métricas: 39 desafios validados; 37/39 acertos na primeira tentativa (94,9%); dois retestes corretos. Preservar erros iniciais.
- Referência: [Microtask Queue](../engineering-notebook.html#connect-microtask-queue).
- Próxima ação (Aula 040): Next Tick Queue gerenciada pelo Node.js, distinta da fila do V8. Criar experiments/next-tick.cjs explicitamente CommonJS, com logs síncronos, Promise.resolve().then, queueMicrotask, process.nextTick e setTimeout. Visualizar execução síncrona seguida de nextTick, microtasks e timer neste cenário; não apresentar como regra universal (top-level ESM e nextTick agendado dentro de microtask podem ter ordem diferente). API nextTick classificada Legacy, preferir queueMicrotask em novos usos comuns, conforme documentação oficial https://nodejs.org/api/process.html#when-to-use-queuemicrotask-vs-processnexttick. Um desafio por turno; próxima etapa setImmediate em contexto I/O.

## Aula 040 — process.nextTick

- Evidência 26/11/2026: execução reportada como “Funcionou”; resposta B correta (1, 6, 3, 5, 2, 4) em CommonJS. Validação introdutória da ordem de duas filas independentes; não inferir domínio dos casos ESM ou agendamento aninhado. Logs e commit local não apresentados.
- Métricas: 40 desafios validados; 38/40 acertos na primeira tentativa (95%); dois retestes corretos.
- Referência: [Next Tick Queue](../engineering-notebook.html#connect-next-tick).
- Próxima ação (Aula 041): setImmediate e setTimeout dentro de callback de fs.readFile. Criar experiments/immediate.cjs com leitura real do próprio arquivo, tratamento de erro, log síncrono dentro do callback, agendar timer de 0 ms antes de immediate e observar immediate primeiro no contexto I/O. Animação Poll → checkpoint → Check → timer elegível; evitar afirmar ordem garantida entre timer e immediate no topo do módulo ou que timer executa exatamente em 0 ms. Um desafio de transferência com nextTick e microtask dentro do callback de I/O; próxima etapa integração das fases e starvation ou concorrência conforme evidência.

## Aula 041 — setImmediate

- Evidência 26/11/2026: execução reportada como “Funcionou”; resposta C correta (1, 6, 5, 4, 3, 2), combinando código síncrono, nextTick, microtasks, immediate e timer dentro de callback de I/O. Validação introdutória; logs e commit local não apresentados.
- Métricas: 41 desafios validados; 39/41 acertos de primeira tentativa (95,1%); dois retestes corretos.
- Referência: [setImmediate](../engineering-notebook.html#connect-set-immediate).
- Próxima ação (Aula 042): Event Loop Starvation por microtasks que se reabastecem. Criar experiments/starvation.cjs com modo microtask versus immediate, trabalho finito de 100000 passos, timer de 0 ms e contagem dos passos completados no timer; mesmo trabalho nas duas versões, uma função por passo, sem loop infinito. No modo microtask o timer só executa após todos os passos; no immediate pode executar antes do fim, contagem variável. Animação comparativa de fila que se reabastece e cessão cooperativa de controle. Não confundir yielding com paralelismo nem prometer latência exata. Um desafio por turno; próxima etapa concorrência versus paralelismo e posteriormente Worker Threads.

## Registro das próximas etapas

A cada avanço confirmado, registrar data, módulo/aula, conceito, evidência (resposta, teste ou commit), lacunas, reteste e próxima ação. Reaproveitar os conhecimentos de outros laboratórios sem marcar domínio automaticamente. Registrar conceitos novos no caderno transversal, evitando duplicação.
