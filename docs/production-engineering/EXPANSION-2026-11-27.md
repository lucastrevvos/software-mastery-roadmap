# Expansão curricular e direção estratégica — 27/11/2026
**Status:** decisões acordadas em conversa; consolidação no currículo local e painel pendente. Este adendo prevalece sobre a regra antiga de extração pelo Codex. Não substitui o curriculum.json, PROGRESS.md, theory.json ou os documentos locais mais recentes. Nenhum domínio atribuído.
## Baseline conhecida
A main remota foi verificada com 20 módulos/256 tópicos. Conforme relatórios do Codex (não verificados independentemente), a versão local após PE-006 tem 27 módulos/319 tópicos, 83 registros teóricos, preserva IDs anteriores e contém as expansões DDD/TDD etc.; último commit local do roadmap 3c14652 (não encontrado no GitHub). Produto local C:\dev\PROJETOS\orderops, commit efdab2e, nove módulos, três portais, 203 testes aprovados em execuções completas, 51 rotas, 19 tabelas, 11 schemas, 11 migrations, 13 diagramas, backlog de 32 riscos. PE-007 concluída localmente conforme relatório recebido; ver registro abaixo. Não marcar entrega ou aprendizagem sem evidência.
## Decisões permanentes
- Codex entrega o monólito modular e o simulador; estudante com ChatGPT assume TODAS as extrações de microsserviços, DDD, TDD, CQRS, MongoDB, Kubernetes, infraestrutura AWS, Git, CI/CD, observabilidade e evoluções. Codex auxilia sob orientação e pode injetar incidentes controlados, sem resolver antecipadamente.
- Produção didática real, isolada, com tráfego e dados sintéticos, sem staging permanente; manter testes automatizados e CI efêmero. Aprovar orçamento, escopo, limites e rollback antes de provisionar ou injetar falhas. Segurança antes de exposição; não usar credenciais, dados ou alvos de terceiros.
- DECA (Descomplicar, Experimentar, Corrigir, Avançar); Runtime Lens em todos os exemplos de código e simulações de infraestrutura; não revelar soluções em desafios. Evidências, teoria, progresso e reteste versionados.
- Estudar problemas reais antes de soluções e automação por IA; não forçar todas as extrações nem todas as tecnologias.
## Competências acordadas antes de PE-006 (reconciliar com versão local, sem duplicar)
Onboarding, technical handover, engenharia reversa, C4, SCM, Git avançado, Linux e redes, Node runtime, Docker, AWS e decisões de serviços, Terraform, CI/CD, release engineering, GitOps e Argo CD, observabilidade técnica e comercial, sustentação, RCA, incident management, SRE, SLO, error budgets, FinOps, chaos engineering, game days, performance/profiling/heap dumps/flame graphs/análise de rede, SQL/PostgreSQL, data reliability, CDC/backfill/reconciliação, resiliência, Redis/RabbitMQ, DDD estratégico e tático (event storming, context mapping, aggregates, value objects, domain events), legacy engineering, Clean/Hexagonal/Evolutionary Architecture, fitness functions, testes arquiteturais, TDD/BDD/characterization/regression/mutation/property-based/consumer-driven contract testing, API engineering (OpenAPI, AsyncAPI, gRPC, GraphQL, versionamento e compatibilidade), AppSec, Secure Coding, Secure by Design, Shift Left, Threat Modeling, SSDLC, DevSecOps (SAST, DAST, SCA, SBOM, secret scanning, container/IaC scanning), Red/Blue/Purple Team em laboratório, platform engineering/IDP/Golden Paths/DevEx, frontend em produção (CSP, CORS, XSS, CDN, caching, Core Web Vitals, erros de browser e compatibilidade), technical leadership/RFC/riscos/dívida técnica. Sistemas distribuídos: Strangler Fig, ACL, Saga, Outbox/Inbox, CQRS, Event Sourcing (opcional conforme problema), backpressure, load shedding, circuit breaker, bulkhead, Kubernetes/Helm, disaster recovery.
## Nova disciplina proposta: MCP & AI Integration Engineering
31 tópicos candidatos; atribuir IDs permanentes somente após reconciliar a versão local.
### Fundamentos (5)
1. Host, Client e Server
2. JSON-RPC 2.0 e lifecycle
3. STDIO e Streamable HTTP
4. Negociação de capacidades e versões
5. Tools, Resources e Prompts
### Desenvolvimento (7)
1. SDK TypeScript
2. Servidores MCP
3. Clientes MCP
4. JSON Schema e validação de entradas/saídas
5. MCP Inspector
6. Integração com REST e OpenAPI
7. Integração com Codex e ChatGPT; servidor de documentação oficial como exemplo
### Segurança (7)
1. OAuth, autenticação e autorização
2. Least privilege, identidade do usuário e isolamento por tenant
3. Prompt injection direta/indireta
4. Tool poisoning e confiança em ferramentas
5. Exfiltração, minimização e redação de dados
6. Aprovação humana para operações críticas, fail-closed
7. Auditoria de chamadas e proteção de credenciais
### Engenharia de produção (6)
1. Containerização e deploy
2. Observabilidade de chamadas e correlação
3. Timeout, retry e idempotência
4. Testes de contrato, integração e regressão
5. Versionamento e compatibilidade
6. Performance, rate limits e custos
### Engenharia de agentes (6)
1. Function calling vs MCP
2. Agentic workflows
3. Human in the loop
4. Evals e qualidade
5. Guardrails e políticas determinísticas
6. MCP Apps e interfaces interativas
**Lab:** estudante cria servidor MCP separado sobre a API do OrderOps, começa com ferramentas de consulta autorizada, testa discovery e invocação com cliente real. Nenhum acesso direto ao banco por padrão; nenhuma alteração da API sem necessidade demonstrada. Demonstrar autorização por usuário/tenant, auditoria, rejeição de inputs e ações indevidas, limites, rastreamento, testes e deploy controlado.
**Gate:** explicar protocolo e fronteiras; integrar uma API existente com chamadas autorizadas ponta a ponta; provar ausência de bypass de permissões; demonstrar falhas e recuperação; comparar MCP a REST/function calling sem confundir responsabilidades.
## Nova disciplina proposta: AIOps
12 tópicos candidatos; ordem revisável, após domínio da investigação manual.
1. Fundamentos, limites e diferença entre AIOps e observabilidade
2. Ingestão e normalização de logs, métricas e traces
3. Baseline, sazonalidade e detecção de anomalias
4. Correlação temporal de incidentes, deploys e mudanças
5. Agrupamento de alertas e redução de ruído
6. Recuperação de runbooks, ADRs e histórico com RAG
7. Geração de hipóteses de causa raiz com evidências e incerteza
8. Ferramentas MCP somente leitura para diagnóstico
9. Avaliação offline com incidentes conhecidos e falsos positivos
10. Aprovação humana, guardrails, limites de ação e rollback
11. Auditoria, observabilidade e custos do próprio agente
12. Game day comparando diagnóstico humano e assistido
**Lab:** agente de diagnóstico OrderOps consulta telemetria autorizada, correlaciona mudanças, propõe hipóteses e runbooks com evidências; não executa recuperação autônoma.
**Gate:** comparar resultados a baseline humana, medir erros/latência/custos, demonstrar recusa de ações não autorizadas e incerteza explícita.
## Direção estratégica da Trevvos Soluções em IA (confirmada pelo usuário)
Prioridade e provável produto/serviço principal: transformar sistemas empresariais existentes em sistemas preparados para IA, sem reconstrução desnecessária. Nome provisório **Trevvos AI Gateway**. Não é produto lançado nem arquitetura definitiva. OrderOps é primeiro cliente fictício e laboratório DECA; construir protótipo pessoalmente, não encomendar ao Codex agora.
Proposta: camada independente de integração entre agentes de IA e sistemas existentes. MCP é interface, não substitui APIs ou regras de negócio. Quando APIs existentes suportam funcionalidades, autorização, identidade, conectividade e contratos adequados, não é necessário modificar o sistema. Caso contrário adaptar integração ou complementar APIs com autorização do cliente. Para legados, avaliar SOAP, GraphQL, exportações ou acesso controlado; nunca burlar permissões.
Componentes propostos: Connector Engine (REST primeiro, SOAP/GraphQL depois), MCP Engine, Security Engine, Policy Engine, Approval Engine, Observability/Audit Engine, Workflow Engine, Management Portal. Separação de tenants, autenticação e autorização por recurso, gestão de secrets, minimização de dados, auditoria, limites e aprovação humana. Não confiar em instruções do modelo como controle de segurança.
MVP: importar OpenAPI/Swagger; gerar ferramentas candidatas semiautomaticamente; administrador seleciona e valida contratos, permissões e risco; publicar MCP somente leitura; testar integração real, falhas, isolamento, segurança e métricas. Escritas e automação crítica depois, com autorização, idempotência, aprovação, recuperação e auditoria. Reutilizar conectores sem expor endpoints indiscriminadamente.
Modelo comercial proposto: implantação, assinatura recorrente, conectores personalizados, hospedagem privada e sustentação; agentes e governança como extensões. Posicionamento: Não substituímos o software da sua empresa. Conectamos sua empresa à inteligência artificial.
## Sequência pedagógica e integração
1. PE-007 concluída conforme relatório recebido; revisar evidências locais durante handover.
2. Primeiro laboratório: onboarding e Git (inventário, commits, branches, remotos, integração segura, revisão de diffs); preservar histórico e trabalho local.
3. Consolidar este adendo na versão local de 27 módulos/319 tópicos (ou mais recente), deduplicar e preservar IDs; corrigir referências antigas à extração pelo Codex em TODOS os documentos, currículo e painel.
4. Incorporar MCP e AIOps como duas disciplinas planejadas, com laboratórios e gates acima; se todos os tópicos forem inéditos, referência preliminar 29 módulos/362 tópicos (319 + 31 + 12), recalcular de verdade após deduplicação. Não marcar tópicos dominados nem inventar notas de teoria.
5. Atualizar README, CODEX, PROGRESS, curriculum.json, theory.json conforme protocolo, index.html da trilha e contagens/links no painel e README raiz. Verificar JSON, IDs únicos e preservados, links e renderização. Commit de integração e publicação quando autorizado, sem force push.
6. Estudar produção, segurança, Git, testes, arquitetura, dados, microsserviços, Kubernetes, e só então automatizar diagnóstico via IA. O MVP comercial pode ser prototipado em etapa separada quando fundamentos de integração e segurança estiverem validados.

## Encerramento da construção delegada — PE-007 (27/11/2026)
Fonte: relatório do Codex compartilhado pelo estudante; arquivos, commits e testes locais não inspecionados independentemente. Sete entregas reportadas concluídas; handover pelo estudante pendente, zero domínio atribuído, PE-008 não iniciada.
| Entrega | Estado reportado | Commit local |
| --- | --- | --- |
| PE-001 | Fundação | 4ea8a64 |
| PE-002 | Identidade, clientes, catálogo | 907ca65 |
| PE-003 | Estoque, pedidos | c6440e2 |
| PE-004 | Pagamentos, expedição, notificações, auditoria | a11b570 |
| PE-005 | Frontend e autorização por recurso | 42a75c7 |
| PE-006 | Baseline e handover | efdab2e |
| PE-007 | Simulador independente | 131d2ef50123822eda075e8d60c0222b1105fdc1 |

### Repositórios reportados
- OrderOps: pe-005-commercial-frontend, efdab2e, working tree limpa, sem alterações em PE-007.
- OrderOps Traffic Simulator: main, 131d2ef50123822eda075e8d60c0222b1105fdc1, local sem remoto.
- Roadmap: pe-005-frontend-and-curriculum, ba256c75f9cd08b740099fc0769a985512d0ed8f, working tree limpa, remoto configurado não usado na entrega; 27 módulos/319 tópicos.
- Nenhum push, integração de branches ou provisionamento na PE-007. Preservar históricos e IDs; não sobrescrever currículo local com o remoto antigo.
### Evidências reportadas
Simulador Node.js/TypeScript, HTTP por APIs públicas, apenas loopback, sem acesso direto ao PostgreSQL. Perfis smoke, normal, pico, sazonal e soak; seed reproduzível; limites de usuários, concorrência, RPS, duração e requisições; timeout, limite de erros, parada graciosa e imediata. Limpeza desativa contas e produtos, preservando histórico.
- Smoke real local: 109 requisições/54,536 s; throughput observado pelo cliente 1,999 req/s; p50 27,82 ms, p95 235,18 ms, p99 303,54 ms; conflito de estoque esperado, zero erros inesperados; um vencedor, saldos não negativos, reservas finais zero, pedidos em estados terminais. Não representa capacidade do servidor, SLO ou telemetria interna.
- 14 testes/6 suítes, typecheck e audit sem achados reportados. Demais perfis não exercitados contra backend. Primeira tentativa revelou parser incorreto do envelope 409; corrigido, pedido reservado cancelado pela API, recursos desativados.
- API e PostgreSQL encerrados; portas 3100/54329 livres; volume preservado.
- Limites: loopback apenas, AWS ainda não suportada; longa duração, capacidade e plataformas não Windows não verificadas; interrupção forçada pode deixar operação ambígua, recuperação manual; limpeza pode afetar estoque.
- Documentos locais: orderops-traffic-simulator/README.md, docs/PE-007.md, docs/adr/001-node-typescript-http-only.md, reports/pe007-local-smoke.json; OrderOps docs/handover/README.md e docs/PE-006.md.
### Próximo passo DECA
Onboarding e Git: estudante identifica HEAD, branches, working tree, histórico e remotos dos três repos com comandos de inspeção. Não realizar merge, rebase, pull, push, reset ou provisionamento antes de compreender o grafo e definir estratégia. Reconciliar histórico local e remoto, integrar este adendo sem perder IDs e evidências, atualizar currículo/painel e validar contagens. 29 módulos/362 tópicos são previsão, não implementação. Runtime Lens distingue grafo ilustrativo de saída real; não expor credenciais/URLs com tokens. Zero domínio atribuído.
