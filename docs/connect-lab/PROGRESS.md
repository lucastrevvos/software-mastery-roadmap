# Connect Lab — progresso e retomada

Atualizado: 2026-11-24

Fonte de verdade do tutor: [currículo e protocolo](index.html). Referência transversal: [Caderno do Engenheiro](../engineering-notebook.html). Não presumir domínio, execução de código ou sincronização automática.

## Estado atual

- Módulo 01: iniciado (Desafios 001–018 corretos; testes com Fake executados segundo relato).
- Módulos 02–12: planejados.
- Repositório de implementação: projeto local connect-lab; remoto e commits do código ainda não confirmados.
- Evidências práticas: aluno confirmou execução bem-sucedida do servidor HTTP nativo, roteamento, Express e middleware de logging e proteção simulada de conversas e agrupamento e extração do Router e do middleware de autenticação e do Conversation Service, além do primeiro teste unitário e ciclo TDD completo, testes negativos, experimento manual de mutação, testes de caracterização, seam temporal, Stub e Fake, nas Aulas 002–018; sem logs anexados.

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

## Registro das próximas etapas

A cada avanço confirmado, registrar data, módulo/aula, conceito, evidência (resposta, teste ou commit), lacunas, reteste e próxima ação. Reaproveitar os conhecimentos de outros laboratórios sem marcar domínio automaticamente. Registrar conceitos novos no caderno transversal, evitando duplicação.
