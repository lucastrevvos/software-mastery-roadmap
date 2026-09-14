from pathlib import Path
import json

p = Path('docs/amaris-fullstack-interview.html')
s = p.read_text(encoding='utf-8')

if 'Interview Copilot V4.6' in s or 'INTERVIEW COPILOT V4.6' in s:
    print('V4.6 already applied')
    raise SystemExit(0)

s = s.replace('Interview Copilot V4.5', 'Interview Copilot V4.6')
s = s.replace('INTERVIEW COPILOT V4.5', 'INTERVIEW COPILOT V4.6')
s = s.replace('<span class="priority">V4.5:</span>', '<span class="priority">V4.6:</span>')
s = s.replace('INTERVIEW COPILOT V4 · banco ampliado', 'INTERVIEW COPILOT V4.6 · banco ampliado')

cards = [
# EVENT-DRIVEN / MESSAGING
('Event-Driven','Quando você escolheria Event-Driven Architecture?','Quando eu preciso desacoplar produtores e consumidores, absorver picos, reagir a fatos de negócio e permitir evolução/escala independente.','Eu não escolheria EDA só porque “é moderno”. Ela compensa quando assincronia e desacoplamento resolvem um problema real; caso contrário adiciona complexidade operacional.','event driven architecture quando usar escolher desacoplamento async eventos escala'),
('Event-Driven','Quais problemas Event-Driven resolve de verdade?','Principalmente acoplamento temporal, picos de carga, fan-out e evolução independente entre componentes.','Um produtor não precisa esperar todos os consumidores nem conhecer cada destino. Isso ajuda disponibilidade e escala, mas muda o modelo de consistência.','event driven problemas resolve coupling temporal fanout spike load desacoplamento'),
('Event-Driven','Quais problemas novos Event-Driven traz?','Consistência eventual, duplicidade, mensagens fora de ordem, falhas parciais, reprocessamento e observabilidade mais difícil.','Idempotência, correlationId, schema evolution, retries/DLQ e métricas de lag deixam de ser detalhes e viram parte do design.','event driven desvantagens problemas tradeoffs eventual consistency duplicate ordering observability'),
('Event-Driven','Event-Driven significa necessariamente usar Kafka?','Não. Event-Driven é um estilo arquitetural; Kafka, RabbitMQ e Pub/Sub são tecnologias possíveis.','Também posso ter eventos internos ou outros mecanismos. A escolha do broker vem dos requisitos de entrega, ordering, replay, throughput e operação.','event driven kafka obrigatorio broker rabbit pubsub arquitetura estilo'),
('Event-Driven','Qual a diferença entre evento e comando?','Evento descreve algo que já aconteceu; comando expressa intenção de que algo seja feito.','Eventos normalmente não têm um único dono consumidor; comandos costumam apontar para uma responsabilidade específica e podem ser rejeitados.','evento comando event command diferença fato intenção'),
('Event-Driven','Choreography ou orchestration?','Choreography distribui reação entre serviços por eventos; orchestration centraliza a coordenação de etapas.','Choreography reduz coordenador central, mas pode esconder o fluxo. Orchestration deixa o processo explícito, mas cria um componente coordenador importante.','choreography orchestration saga coordenação eventos'),
('Event-Driven','Quando choreography vira problema?','Quando o fluxo fica difícil de entender, muitas reações implícitas aparecem e ninguém enxerga facilmente o estado do processo.','Nesse ponto eu consideraria uma saga orquestrada ou pelo menos melhor observabilidade e documentação do fluxo.','choreography problema spaghetti events fluxo implícito saga'),
('Event-Driven','Event-Driven e Event Sourcing são a mesma coisa?','Não. Event-Driven é comunicação/reação por eventos; Event Sourcing persiste o estado como sequência de eventos.','Posso ter EDA sem Event Sourcing e Event Sourcing sem usar broker para integração externa.','event driven event sourcing diferença'),
('Event-Driven','Event-Driven e CQRS são a mesma coisa?','Não. CQRS separa modelos de escrita e leitura; EDA trata comunicação por eventos.','Eles combinam bem em alguns cenários, mas não são dependentes um do outro.','event driven cqrs diferença read write'),
('Event-Driven','Domain Event e Integration Event: diferença?','Domain Event representa algo relevante dentro do domínio; Integration Event é o contrato publicado para outros contextos/sistemas.','Eu evito expor diretamente o modelo interno do domínio como contrato externo, porque isso aumenta acoplamento.','domain event integration event DDD bounded context'),
('Event-Driven','Como lidar com mensagens duplicadas?','Assumo que duplicatas podem acontecer e torno o consumidor idempotente usando eventId/idempotencyKey com garantia persistente.','Em banco relacional, UNIQUE constraint + transação é uma estratégia simples e forte; só um check em memória não resolve concorrência.','duplicate message idempotency eventid unique consumer'),
('Event-Driven','Como lidar com mensagens fora de ordem?','Primeiro verifico se ordering é realmente requisito; se for, uso chave/partição adequada e versão/sequence no agregado.','Mesmo com ordering do broker, retries e paralelismo podem complicar processamento. O consumidor precisa saber rejeitar/adiar evento antigo quando necessário.','out of order ordering sequence version event message'),
('Event-Driven','Como evoluir schema de eventos sem quebrar consumidores?','Prefiro mudanças compatíveis: adicionar campos opcionais, evitar renomear/remover de uma vez e versionar quando necessário.','Contrato de evento é API. Uso schema registry/validação quando faz sentido e estratégia expand-contract para consumidores independentes.','event schema evolution backward compatible versioning registry'),
('Event-Driven','O que é poison message?','É uma mensagem que falha repetidamente por problema permanente de conteúdo ou regra, não por falha transitória.','Evito retry infinito: limito tentativas, registro motivo e mando para DLQ/quarentena para investigação ou correção.','poison message dlq retry infinito'),
('Event-Driven','Retry sempre resolve falha de consumer?','Não. Retry ajuda falha transitória; em erro permanente só aumenta carga e atraso.','Uso backoff/jitter, limite de tentativas, classificação de erro e DLQ quando apropriado.','retry transient permanent consumer backoff jitter dlq'),
('Event-Driven','Como evitar retry storm?','Limito tentativas, uso exponential backoff com jitter, circuit breaker/bulkhead e controlo concorrência.','Quando uma dependência inteira cai, retry agressivo transforma falha em avalanche.','retry storm backoff jitter circuit breaker bulkhead'),
('Event-Driven','Como observar um fluxo assíncrono ponta a ponta?','Propago correlationId/traceId e acompanho métricas como lag, throughput, retries, DLQ e tempo até processamento.','Logs isolados de cada serviço não bastam. Preciso reconstruir a jornada da mensagem entre produtor, broker e consumidores.','observability async correlation trace lag event driven'),
('Event-Driven','O que é consumer lag?','É a diferença entre o que foi produzido e o que o consumidor já processou.','Lag crescente pode indicar consumidor lento, partição desbalanceada, dependência externa ou capacidade insuficiente.','consumer lag kafka backlog queue observability'),
('Event-Driven','O que é backpressure em mensageria?','É controlar a entrada/processamento quando consumidores não acompanham a taxa de produção.','Posso limitar prefetch/concurrency, autoscalar com cuidado, aplicar rate limiting ou até rejeitar/degradar trabalho para evitar colapso.','backpressure queue consumer overload prefetch concurrency'),
('Event-Driven','O que acontece se eu fizer ACK antes de persistir?','Posso perder a mensagem: o broker considera concluída e uma falha antes do efeito durável impede redelivery.','Normalmente faço efeito/commit primeiro e ACK depois, aceitando que a janela entre commit e ACK exige idempotência.','ack before commit message loss redelivery idempotency'),
('Event-Driven','O que acontece se eu persistir e cair antes do ACK?','A mensagem pode ser entregue novamente mesmo com o efeito já aplicado.','Por isso at-least-once + idempotência é um modelo mental tão importante.','commit before ack crash duplicate redelivery'),
('Event-Driven','Outbox resolve qual problema?','Resolve o dual-write entre banco e publicação de evento sem depender de uma transação distribuída com o broker.','Escrevo estado de negócio e registro da outbox na mesma transação; outro processo publica depois. Ainda preciso lidar com publicação duplicada.','outbox dual write transaction broker'),
('Event-Driven','Inbox resolve qual problema?','Registra mensagens já processadas para impedir que redelivery repita o efeito de negócio.','Costumo usar eventId UNIQUE e transação junto do efeito. Inbox e Outbox resolvem lados diferentes da confiabilidade.','inbox processed messages idempotency'),
('Event-Driven','Outbox elimina necessidade de idempotência?','Não. O publisher da outbox pode publicar de novo se cair entre publicar e marcar como enviado.','O consumidor continua precisando tolerar duplicatas. Outbox resolve atomicidade local, não exactly-once end-to-end.','outbox idempotency exactly once duplicate'),
('Event-Driven','At-least-once significa o quê na prática?','Que a mensagem não deve ser perdida, mas pode ser entregue mais de uma vez.','O preço da confiabilidade é aceitar redelivery e projetar o consumer para duplicidade.','at least once semantics duplicate'),
('Event-Driven','Exactly-once existe?','Pode existir dentro de escopos e produtos específicos, mas exatamente uma vez end-to-end é difícil e depende das fronteiras.','Em aplicação eu prefiro discutir o efeito final: at-least-once + idempotência costuma ser mais explícito e robusto.','exactly once semantics end to end'),
('Event-Driven','RabbitMQ, Kafka ou Pub/Sub: como escolher?','Eu começo pelos requisitos: filas/roteamento e ACK operacional favorecem Rabbit; replay/log/partições favorecem Kafka; integração gerenciada no GCP favorece Pub/Sub.','Não existe vencedor universal. Comparo ordering, replay, throughput, retenção, operação, custo e ecossistema.','rabbitmq kafka pubsub choose broker'),
('Event-Driven','RabbitMQ queue e exchange: diferença?','Exchange recebe mensagens e roteia; queue armazena mensagens para consumidores.','O tipo da exchange e bindings definem a estratégia de roteamento.','rabbitmq exchange queue binding'),
('Event-Driven','Direct, topic e fanout exchange?','Direct roteia por chave exata, topic por padrão de routing key e fanout envia para todas as filas ligadas.','Escolho conforme a semântica de roteamento; não uso fanout se preciso segmentar consumidores.','rabbitmq direct topic fanout exchange'),
('Event-Driven','Kafka partition serve para quê?','É a unidade de paralelismo e ordering dentro de um tópico.','Mensagens da mesma key podem ir para a mesma partição para manter ordem relativa; mais partições aumentam paralelismo mas têm custo.','kafka partition ordering key parallelism'),
('Event-Driven','O que acontece num rebalance do Kafka?','Partições são redistribuídas entre consumidores do grupo e há uma pausa/transição no processamento.','Rebalances frequentes prejudicam latência e podem revelar consumidores instáveis ou configuração inadequada.','kafka rebalance consumer group partition'),
('Event-Driven','Pub/Sub ACK deadline significa o quê?','É a janela em que o consumidor deve confirmar processamento antes de a mensagem ficar elegível para redelivery.','Processamento longo exige extensão/lease adequada; ainda assim desenho o consumer como idempotente.','pubsub ack deadline redelivery lease'),

# NODE / JS
('Node','O Event Loop executa I/O?','Não necessariamente. O Event Loop coordena a retomada do JavaScript; o I/O é feito pelo SO ou por mecanismos do runtime/libuv.','É importante separar “coordenar callbacks” de “executar fisicamente rede/disco”.','event loop io execute libuv os'),
('Node','Quais operações usam o thread pool do libuv?','Tipicamente várias operações de fs, crypto, zlib e algumas resoluções DNS.','Rede via sockets normalmente usa mecanismos assíncronos do sistema operacional, não simplesmente uma thread do pool por conexão.','libuv thread pool fs crypto zlib dns'),
('Node','Aumentar UV_THREADPOOL_SIZE resolve qualquer lentidão?','Não. Só afeta operações que realmente usam esse pool e pode aumentar contenção/CPU.','Antes eu identifico o gargalo com profiling/métricas. Ajustar thread pool sem diagnóstico pode não mudar nada.','uv_threadpool_size performance libuv'),
('Node','Promise.all é sempre melhor que await sequencial?','Não. Uso Promise.all quando operações são independentes e quero concorrência; sequencial quando uma depende da anterior ou preciso controlar carga.','Disparar centenas de Promises juntas pode sobrecarregar banco/API; às vezes preciso de concurrency limit.','promise all await sequential concurrency limit'),
('Node','Como limitar concorrência de tarefas async?','Uso pool/semaphore/concurrency limiter em vez de disparar tudo de uma vez.','O objetivo é equilibrar throughput com limites de banco, API externa, memória e sockets.','node concurrency limiter semaphore async pool'),
('Node','Microtask e macrotask: por que importa?','Promises/queueMicrotask entram na fila de microtasks, que é drenada antes de avançar para certas fases/tarefas seguintes.','Abusar de microtasks pode atrasar I/O e gerar starvation.','microtask macrotask promise event loop starvation'),
('Node','process.nextTick pode causar starvation?','Sim. Callbacks de nextTick têm prioridade alta e uma cadeia infinita pode impedir o loop de avançar.','Uso com parcimônia; normalmente Promises e APIs assíncronas comuns são preferíveis para fluxo de aplicação.','process.nexttick starvation node'),
('Node','Stream serve para quê?','Permite processar dados em partes sem carregar tudo em memória.','É útil para arquivos, HTTP e pipelines grandes; preciso respeitar backpressure.','node stream memory backpressure pipeline'),
('Node','Buffer é o quê?','É a representação de dados binários em Node.','Uso em I/O, arquivos, sockets, criptografia e transformação de bytes.','node buffer binary'),
('Node','Como detectar event-loop lag?','Meço atraso do loop junto de CPU e latência P95/P99, e uso profiling/tracing para localizar bloqueio.','Lag alto com CPU alta sugere CPU-bound; latência alta sem lag pode apontar dependência externa.','event loop lag monitor p95 p99 cpu profiling'),
('Node','Cluster e Worker Threads: diferença?','Cluster/processos têm memória isolada e escalam processos; Worker Threads compartilham o processo e são focadas em paralelismo de CPU.','Para escalar API normalmente uso múltiplos processos/containers; Worker Threads entram quando existe trabalho CPU-bound específico.','cluster worker threads process node'),
('Node','Quando Node não é uma boa escolha?','Quando o workload principal é CPU-bound intenso e o ecossistema/arquitetura exigiria muita compensação.','Ainda posso usar workers/serviços separados, mas avalio linguagem/runtime pelo perfil real do problema.','node when not use cpu bound tradeoff'),

# NEST / API
('NestJS','Controller deve ter regra de negócio?','Prefiro controller fino: valida/recebe protocolo HTTP e delega para aplicação/use case.','Regra no controller dificulta teste, reuso e manutenção; cross-cutting vai para guards/interceptors/filters conforme o caso.','nestjs thin controller business logic'),
('NestJS','Guard, middleware, interceptor, pipe e filter: como decidir?','Middleware atua antes da rota; Guard decide acesso; Pipe valida/transforma; Interceptor envolve execução; Filter trata exceções.','Eu escolho pela responsabilidade e pelo ponto do pipeline, evitando jogar tudo em middleware.','nestjs guard middleware interceptor pipe filter'),
('NestJS','DTO é entidade de domínio?','Não. DTO é contrato de entrada/saída; entidade modela regra/identidade de domínio.','Separar evita acoplar modelo interno ao transporte e facilita evolução do contrato.','nestjs dto entity domain difference'),
('NestJS','Como validar entrada no Nest?','Uso DTOs com ValidationPipe/class-validator ou solução equivalente na borda.','Validação de formato fica na borda; invariantes de negócio continuam no domínio/aplicação.','nestjs validation pipe dto class validator'),
('API','PUT e PATCH: diferença?','PUT representa substituição completa do recurso; PATCH aplica alteração parcial.','Na prática sigo o contrato documentado e preservo idempotência quando aplicável.','http put patch difference'),
('API','POST precisa ser idempotente?','Não por definição, mas operações críticas como pagamento/criação podem precisar de idempotency key.','Guardo a chave e o resultado de forma persistente para repetir a mesma resposta sem repetir o efeito.','post idempotency key api payment'),
('API','Como versionar API?','Prefiro evolução compatível quando possível; breaking change exige estratégia explícita de versão e depreciação.','Posso versionar por URL/header conforme contexto, mas o mais importante é contrato, migração e observabilidade de uso.','api versioning backward compatibility deprecation'),
('API','Como projetar paginação?','Offset é simples; cursor/keyset é melhor para grandes volumes e dados mudando frequentemente.','Cursor evita custo crescente de OFFSET e inconsistência quando registros entram/saem entre páginas.','pagination offset cursor keyset api'),
('API','Como implementar rate limiting?','Defino identidade, janela/algoritmo e comportamento em falha; Redis com operação atômica é comum em ambiente distribuído.','Token bucket/sliding window dependem do requisito. Também penso em headers, bursts e limites por tenant.','rate limiting redis token bucket sliding window'),
('API','Timeout deveria existir em chamada externa?','Sim. Sem timeout, recursos podem ficar presos indefinidamente e causar efeito cascata.','Defino timeout pelo orçamento de latência do fluxo, não por número arbitrário.','timeout external api latency budget'),
('API','Quando fazer retry em API externa?','Em falhas transitórias e operações seguras/idempotentes.','Uso limite, backoff/jitter e evito retry automático de efeito não idempotente sem proteção.','retry external api transient idempotent'),

# REACT
('React','O que realmente dispara render no React?','Mudança de state, props/context ou render do pai pode fazer componente executar novamente.','Render não significa necessariamente alteração no DOM; reconciliation decide o que realmente muda.','react what triggers render state props context parent'),
('React','React.memo resolve performance sempre?','Não. Ele compara props e também tem custo.','Uso quando há render caro e props estáveis; antes e depois verifico no Profiler.','react memo performance props profiler'),
('React','useMemo e useCallback: diferença?','useMemo memoriza um valor calculado; useCallback memoriza a referência de uma função.','Não uso por padrão. Só quando estabilidade de referência/cálculo realmente evita trabalho ou atende dependência.','usememo usecallback difference react'),
('React','Por que objeto inline pode quebrar memoização?','Cada render cria uma nova referência, então comparação rasa enxerga prop diferente.','Posso mover/estabilizar o valor, mas só faço isso se houver ganho real.','react inline object referential equality memo'),
('React','Como evitar race condition em fetch dentro de useEffect?','Cancelo/ignoro a request antiga quando parâmetros mudam e garanto que resposta velha não sobrescreva estado novo.','AbortController ou uma camada de server-state ajudam; também considero React Query/TanStack Query quando adequado.','react useeffect fetch race abortcontroller stale response'),
('React','Quando Context vira problema?','Quando valor muda muito e uma árvore grande de consumidores re-renderiza desnecessariamente.','Posso dividir contexts, manter estado local, usar selectors/store especializado ou estabilizar value.','react context performance rerender'),
('React','Server state e client state: diferença?','Server state vem de fonte remota e envolve cache, stale, refetch e sincronização; client state é estado local da UI/aplicação.','Misturar ambos em um store único pode complicar invalidação e fluxo.','react server state client state cache'),
('React','Por que key por índice pode dar problema?','Se lista reordena/remove itens, o índice muda e o React pode associar estado local ao item errado.','Prefiro uma chave estável da identidade do item.','react key index problem list'),
('React','Strict Mode chamar efeito duas vezes é bug?','Em desenvolvimento, Strict Mode pode reexecutar certos ciclos para revelar efeitos não seguros.','O código deve tolerar setup/cleanup correto; produção não deve depender do comportamento de dev.','react strict mode double effect development'),
('React','Quando usar useReducer?','Quando transições de estado são relacionadas/complexas e quero centralizar regras de atualização.','Não é automaticamente melhor que useState; escolho pela legibilidade do modelo de estado.','react usereducer usestate when'),

# OO / SOLID
('OO','Encapsulamento e abstração: diferença?','Encapsulamento protege estado/implementação; abstração expõe apenas o que importa para usar um conceito.','Eles se relacionam, mas não são sinônimos.','oop encapsulation abstraction difference'),
('OO','Polimorfismo na prática significa o quê?','Diferentes implementações respondem ao mesmo contrato/interface.','Isso permite trocar comportamento sem o chamador depender da classe concreta.','oop polymorphism interface practical'),
('OO','Composição ou herança?','Prefiro composição para reutilizar comportamento com menos acoplamento; herança faz sentido quando a relação “é um” é estável e semântica.','Herança profunda costuma criar fragilidade e violar substituição.','composition over inheritance oop'),
('OO','Interface e classe abstrata: diferença?','Interface define contrato; classe abstrata também pode compartilhar implementação/estado base.','No TypeScript interfaces desaparecem em runtime; abstract class existe como classe JavaScript.','typescript interface abstract class difference'),
('SOLID','SRP quer dizer uma função por classe?','Não. Quer dizer uma razão coerente para mudança/responsabilidade, não tamanho mínimo artificial.','Posso ter várias operações relacionadas na mesma classe sem violar SRP.','solid srp single responsibility'),
('SOLID','OCP na prática?','Projetar pontos de extensão para adicionar comportamento sem editar continuamente código estável.','Uso polimorfismo/strategy quando existe variação real; não crio abstração antecipada para tudo.','solid open closed ocp practical'),
('SOLID','LSP: me dê um exemplo de violação.','Uma subclasse que não consegue cumprir o contrato da base e começa a lançar erro para operações válidas da base viola substituição.','O problema é semântico: o cliente não deveria precisar saber qual subtipo recebeu para usá-lo corretamente.','solid liskov violation example'),
('SOLID','DIP e Dependency Injection são a mesma coisa?','Não. DIP é princípio de depender de abstrações; DI é uma técnica para fornecer dependências de fora.','Posso usar container de DI e ainda violar DIP se minhas classes dependem de detalhes concretos errados.','dip dependency inversion dependency injection difference'),
('OO','Alta coesão e baixo acoplamento significam o quê?','Coesão alta mantém coisas relacionadas juntas; acoplamento baixo reduz dependências desnecessárias entre módulos.','É um guia importante para modularidade e mudança segura.','cohesion coupling oop modularity'),

# DB / CONCURRENCY
('Banco','Índice acelera tudo?','Não. Acelera certos acessos, mas custa espaço e torna INSERT/UPDATE/DELETE mais caros.','Projeto índice pelas queries reais e confirmo com EXPLAIN ANALYZE.','database index tradeoff writes explain analyze'),
('Banco','Índice composto: ordem das colunas importa?','Sim. A ordem deve refletir filtros, ordenação e seletividade conforme o plano das consultas.','A regra exata depende do banco e da query; não escolho só pela coluna “mais seletiva” de forma automática.','composite index column order database'),
('Banco','O que é MVCC?','É um mecanismo de versões de linhas que permite concorrência entre leituras/escritas reduzindo bloqueios diretos.','PostgreSQL usa MVCC; isso também traz necessidade de VACUUM para versões mortas.','mvcc postgres concurrency'),
('Banco','Lost update é o quê?','Duas transações leem o mesmo estado e uma sobrescreve a alteração da outra.','Resolvo com locking, versionamento otimista ou operação atômica dependendo do caso.','lost update concurrency transaction'),
('Banco','Optimistic locking funciona como?','Leio com version e no UPDATE exijo a mesma version; se outra transação alterou, zero linhas atualizam e trato conflito.','É bom quando conflito é raro. Se conflito é frequente, retries podem ficar caros.','optimistic locking version concurrency'),
('Banco','Pessimistic locking quando usar?','Quando conflito é provável e preciso reservar a linha/recurso durante uma transação curta.','Locks longos reduzem throughput e aumentam risco de deadlock.','pessimistic lock for update when'),
('Banco','FOR UPDATE SKIP LOCKED resolve o quê?','Permite múltiplos workers reivindicarem linhas diferentes sem esperar as já bloqueadas.','É ótimo para work queue no banco, mas não elimina idempotência nem necessidade de recuperar jobs abandonados.','for update skip locked workers queue'),
('Banco','SKIP LOCKED garante exactly-once?','Não. Ele coordena disputa pelas linhas naquele momento; falhas depois da seleção ainda podem exigir retry/idempotência.','Concorrência e semântica de entrega são problemas diferentes.','skip locked exactly once idempotency'),
('Banco','O que causa deadlock?','Transações adquirem recursos em ordens incompatíveis e ficam esperando umas pelas outras.','Banco detecta e aborta uma; reduzo duração, padronizo ordem de locks e trato retry quando apropriado.','database deadlock cause retry lock order'),
('Banco','Connection pool por que existe?','Abrir conexão é caro; pool reutiliza conexões e limita concorrência contra o banco.','Pool grande demais em várias instâncias pode derrubar o banco; dimensiono globalmente.','database connection pool sizing'),
('Banco','Read replica serve para quê?','Escalar leituras e separar carga, aceitando possível replication lag.','Não mando leitura que exige read-your-writes para réplica atrasada sem estratégia.','read replica replication lag consistency'),
('Banco','Partitioning e sharding: diferença?','Partitioning divide dados logicamente dentro do mesmo banco/cluster; sharding distribui entre nós/bancos independentes.','Sharding aumenta muito a complexidade de queries, transações e operação.','partitioning sharding difference database'),

# DISTRIBUTED / ARCHITECTURE
('Distribuídos','O que é falha parcial?','Parte do sistema falha enquanto outras partes continuam funcionando e talvez nem saibam imediatamente.','Isso torna timeout, retry, idempotência e observabilidade fundamentais.','partial failure distributed systems'),
('Distribuídos','CAP theorem explica o quê?','Durante uma partição de rede, um sistema distribuído precisa escolher entre consistência forte e disponibilidade para aquela operação.','Não é “escolha dois o tempo todo”; a decisão relevante aparece sob partition.','cap theorem consistency availability partition'),
('Distribuídos','Consistência eventual significa dado errado?','Não necessariamente. Significa que réplicas/visões podem divergir temporariamente e convergir depois.','Preciso saber se o domínio tolera essa janela e como comunico estado pendente ao usuário.','eventual consistency meaning'),
('Distribuídos','Circuit breaker resolve o quê?','Evita continuar pressionando uma dependência que está falhando e permite recuperação gradual.','Ele não substitui timeout; normalmente trabalha junto de timeout, retry criterioso e fallback/degradação.','circuit breaker timeout retry dependency'),
('Distribuídos','Bulkhead é o quê?','Isola recursos/concorrência para uma falha não consumir toda a capacidade do sistema.','Posso separar pools, filas ou limites por dependência/tenant.','bulkhead resilience isolation'),
('Distribuídos','Load shedding é o quê?','É rejeitar ou degradar parte da carga deliberadamente para preservar o núcleo do sistema.','Sob overload, responder 429/503 controlado pode ser melhor que colapsar tudo.','load shedding overload 429 503'),
('Arquitetura','Monólito modular é atraso para microsserviços?','Não. Pode ser arquitetura final muito boa ou etapa de evolução, com limites claros sem custo distribuído.','Eu extraio serviço quando existe motivo operacional/organizacional real, não por moda.','modular monolith microservices tradeoff'),
('Arquitetura','Qual sinal indica extrair um microsserviço?','Necessidade clara de escala/deploy/ownership independente ou limite de domínio que o monólito já não atende bem.','Também considero custo: rede, observabilidade, dados distribuídos, deploy e on-call.','when extract microservice signals'),
('Arquitetura','Saga resolve o quê?','Coordena uma operação de negócio distribuída por etapas e compensações, sem transação ACID global.','Compensação não é rollback mágico; precisa ser modelada como ação de negócio.','saga distributed transaction compensation'),
('Arquitetura','2PC ou Saga?','2PC busca atomicidade coordenada mas tem forte acoplamento/limitações; Saga aceita consistência eventual e compensações.','Em microsserviços normalmente Saga é mais comum, mas depende de infraestrutura e requisito.','two phase commit 2pc saga difference'),
('Arquitetura','CQRS quando vale a pena?','Quando modelos de leitura e escrita têm necessidades muito diferentes e essa separação paga a complexidade extra.','Não uso CQRS para CRUD simples só para parecer sofisticado.','cqrs when use tradeoff'),
('Arquitetura','Cache-aside funciona como?','Leio cache; em miss vou ao banco e preencho cache.','Preciso pensar em TTL, invalidação, stampede e stale data.','cache aside redis ttl invalidation stampede'),

# K8S / GCP / DEVOPS
('Kubernetes','Pod, Deployment e Service: diferença?','Pod é unidade de execução; Deployment gerencia réplicas/rollout; Service fornece endereço estável e balanceamento para pods.','Separar essas responsabilidades ajuda a entender o modelo do Kubernetes.','kubernetes pod deployment service difference'),
('Kubernetes','Readiness e liveness: diferença?','Readiness decide se recebe tráfego; liveness decide se deve reiniciar.','Colocar banco na liveness pode criar restart loop durante uma indisponibilidade externa.','readiness liveness probe difference'),
('Kubernetes','Requests e limits: para quê?','Requests ajudam scheduling/garantia de recurso; limits impõem teto.','CPU limit pode causar throttling; memória acima do limit pode levar a OOMKilled.','kubernetes requests limits throttling oomkilled'),
('Kubernetes','HPA escala baseado em quê?','Pode usar CPU/memória e métricas customizadas conforme configuração.','Escalar pod não resolve gargalo no banco ou dependência externa; observo o sistema inteiro.','kubernetes hpa autoscaling metrics'),
('Kubernetes','StatefulSet quando usar?','Quando pods precisam identidade/armazenamento estáveis ou ordenação específica.','Não uso para qualquer serviço com banco externo; Deployment continua adequado para stateless apps.','statefulset deployment when'),
('GCP','Cloud Run ou GKE?','Cloud Run reduz operação para containers stateless/event-driven; GKE dá mais controle de Kubernetes e workloads complexos.','Eu preciso de um requisito concreto para aceitar o custo operacional extra do GKE.','cloud run vs gke choose'),
('GCP','Cloud Run concurrency significa o quê?','Quantas requisições uma instância pode processar simultaneamente.','Valor maior melhora utilização em I/O-bound, mas pode aumentar contenção de CPU/memória/conexões.','cloud run concurrency instances'),
('GCP','Pub/Sub redelivery deve ser considerado normal?','Sim. Consumo deve ser idempotente e preparado para mensagens reaparecerem.','ACK deadline, retries e falhas do subscriber tornam redelivery parte do modelo.','gcp pubsub redelivery idempotency'),
('DevOps','Blue-green e canary: diferença?','Blue-green troca entre ambientes completos; canary expõe versão nova gradualmente para parte do tráfego.','Canary dá feedback progressivo; blue-green facilita rollback rápido de ambiente.','blue green canary deployment'),
('DevOps','Como fazer migration sem quebrar rollout?','Uso expand-contract: primeiro mudanças compatíveis, depois app novo, backfill se necessário e só então removo legado.','Evito deploy que exige mudança de schema incompatível instantaneamente em todas as instâncias.','database migration expand contract zero downtime'),

# TESTES / SECURITY
('Testes','O que testar num consumer idempotente?','Processar uma vez, entregar duplicado, falhar antes/depois do commit, concorrência entre instâncias e comportamento de ACK/retry.','Um teste de integração com banco real/Testcontainers ajuda a validar UNIQUE e transação de verdade.','test idempotent consumer duplicate crash integration'),
('Testes','Mock demais é problema?','Pode ser. Teste passa mesmo que integração real esteja quebrada e fica acoplado à implementação.','Mocko fronteiras específicas; para banco/broker crítico prefiro integração real controlada quando viável.','mock too much testing integration'),
('Testes','Contract test serve para quê?','Valida que produtor/consumidor ou cliente/API continuam compatíveis no contrato.','É útil quando times/serviços evoluem independentemente.','contract testing api events consumer producer'),
('Segurança','JWT é criptografado?','Normalmente não; é assinado. O payload pode ser lido por quem possui o token.','Não coloco segredo no payload e valido assinatura, expiração, issuer/audience conforme contrato.','jwt signed encrypted security'),
('Segurança','Access token e refresh token: diferença?','Access token é curto e usado para acesso; refresh token renova sessão e precisa proteção/revogação mais cuidadosa.','Rotação e detecção de reuse aumentam segurança de refresh token.','access refresh token difference oauth'),
('Segurança','CORS protege minha API de qualquer cliente malicioso?','Não. CORS é política do navegador; clientes fora do browser podem chamar a API normalmente.','Autenticação/autorização continuam necessárias.','cors security browser not auth'),
('Segurança','CSRF quando é relevante?','Principalmente quando navegador envia credenciais automaticamente, como cookies.','SameSite, CSRF token e desenho de autenticação reduzem risco.','csrf cookie security same site'),
('Segurança','SSRF é o quê?','Quando atacante faz o servidor requisitar destinos que ele não deveria alcançar.','Valido destinos, uso allowlist quando possível e controlo acesso de rede/metadata services.','ssrf server side request forgery security'),

# SYSTEM DESIGN / SENIORITY
('System Design','Como começar uma pergunta de system design?','Começo esclarecendo requisitos, escala, invariantes e o que é mais crítico antes de desenhar componentes.','Depois passo por API, dados, fluxo síncrono/assíncrono, falhas, escala, segurança e observabilidade.','system design how start requirements invariants'),
('System Design','Como desenhar processamento assíncrono de job?','API persiste o job, publica/enfileira, worker processa idempotente e atualiza status; cliente consulta ou recebe callback.','Penso em retries, DLQ, timeout, cancelamento, dedupe e jobs presos.','async job system design queue worker status'),
('System Design','Como impedir um cliente ruim de derrubar serviço de webhook?','Isolo concorrência por endpoint/tenant, uso timeout, rate limit, circuit breaker e filas/partições adequadas.','Um destino lento não deve consumir todos os workers nem bloquear clientes saudáveis.','webhook tenant isolation bulkhead timeout circuit breaker'),
('System Design','Como desenhar audit log?','Registro append-only com ator, ação, alvo, timestamp e contexto, separado de log técnico.','Protejo integridade, retenção, acesso e dados sensíveis.','audit log system design append only'),
('System Design','Como desenhar endpoint de pagamento idempotente?','Cliente envia idempotency key; servidor persiste chave + resultado sob constraint única e devolve o mesmo resultado em retry.','A chave precisa ter escopo claro e eu considero payload incompatível usando a mesma chave.','payment idempotency key api design'),
('Senioridade','Como você responde quando não sabe?','Eu digo o limite com clareza, explico o que sei, faço perguntas e mostro como investigaria/validaria.','Inventar certeza é pior que demonstrar método.','interview dont know senior answer'),
('Senioridade','Como decide entre solução simples e sofisticada?','Escolho a menor solução que atende requisitos e deixa caminho de evolução.','Complexidade tem custo contínuo de operação, onboarding, teste e incidentes.','senior simplicity overengineering tradeoff'),
('Senioridade','Como você faria postmortem?','Linha do tempo, impacto, fatores contribuintes, por que defesas falharam e ações concretas sem caça a culpados.','Ações precisam de dono/prioridade e devem reduzir probabilidade ou impacto futuro.','postmortem incident senior blameless'),
('Senioridade','Como comunicar risco técnico para produto?','Traduzo risco em impacto, probabilidade, alternativas e custo, evitando jargão desnecessário.','Não basta dizer “tem débito técnico”; explico consequência para prazo, confiabilidade ou capacidade de mudança.','technical risk product communication senior'),
('Senioridade','Como revisar uma arquitetura que você não conhece?','Começo por requisitos, fluxos críticos, boundaries, dados e falhas antes de julgar tecnologia.','Faço perguntas e busco evidência em métricas/incidentes; evito reescrever por preferência pessoal.','architecture review senior'),
]

def js(v):
    return json.dumps(v, ensure_ascii=False)

existing = s
new_lines = []
for cat, q, quick, deep, tags in cards:
    if q in existing:
        continue
    new_lines.append(f"Q({js(cat)},{js(q)},{js(quick)},{js(deep)},{js(tags)})")

marker = '\nconst shortOverrides={'
idx = s.find(marker)
if idx < 0:
    raise SystemExit('shortOverrides marker not found')
arr_end = s.rfind('\n];', 0, idx)
if arr_end < 0:
    raise SystemExit('questions array end not found')

if new_lines:
    block = ',\n' + ',\n'.join(new_lines)
    s = s[:arr_end] + block + s[arr_end:]

# Richer search aliases for spoken/transcribed questions.
hot_old = "const hotTerms=['webhook','Worker Threads','concorrência','OO'"
hot_new = "const hotTerms=['event-driven','eventual consistency','webhook','Worker Threads','concorrência','OO'"
if hot_old in s:
    s = s.replace(hot_old, hot_new, 1)

# Add likely follow-up prompts to existing map without requiring a separate card relationship.
replacements = {
    "'O que é Event-Driven Architecture?':'Qual a diferença entre um evento e um comando?'": "'O que é Event-Driven Architecture?':'Quais problemas novos esse modelo traz em relação a um fluxo síncrono?'",
}
for a, b in replacements.items():
    if a in s:
        s = s.replace(a, b, 1)

# Add direct next-question hints for high-probability V4.6 cards.
hint_marker = 'const nextHints={\n'
hints = {
'Quando você escolheria Event-Driven Architecture?':'Quais problemas novos esse modelo traz?',
'Quais problemas Event-Driven resolve de verdade?':'E quais trade-offs você aceita em troca?',
'Quais problemas novos Event-Driven traz?':'Como você lida com duplicidade e mensagens fora de ordem?',
'Choreography ou orchestration?':'Quando choreography começa a virar um fluxo difícil de operar?',
'Como evoluir schema de eventos sem quebrar consumidores?':'Como faria uma breaking change inevitável?',
'O que acontece se eu persistir e cair antes do ACK?':'Como o consumer impede repetir o efeito?',
'Outbox elimina necessidade de idempotência?':'Por que o publisher ainda pode duplicar?',
'RabbitMQ, Kafka ou Pub/Sub: como escolher?':'E se o requisito principal for replay?',
'Promise.all é sempre melhor que await sequencial?':'Como você evitaria explodir a concorrência contra o banco?',
'Controller deve ter regra de negócio?':'Onde você colocaria um caso de uso no Nest?',
'POST precisa ser idempotente?':'Como implementaria idempotency key no banco?',
'O que realmente dispara render no React?':'Render significa que o DOM mudou?',
'React.memo resolve performance sempre?':'Como você provaria que ajudou?',
'Composição ou herança?':'Me dê um caso em que herança ainda faria sentido.',
'FOR UPDATE SKIP LOCKED resolve o quê?':'Isso garante exactly-once?',
'CAP theorem explica o quê?':'O que você faria durante uma partition?',
'Monólito modular é atraso para microsserviços?':'Que sinal concreto justificaria extrair um serviço?',
'Cloud Run ou GKE?':'Qual requisito faria você aceitar o custo do GKE?',
'O que testar num consumer idempotente?':'Como simularia crash depois do commit e antes do ACK?',
'Como começar uma pergunta de system design?':'Quais invariantes você perguntaria primeiro?',
}
if hint_marker in s:
    insert = ''.join(f"{js(k)}:{js(v)},\n" for k,v in hints.items() if k not in s[s.find(hint_marker):s.find('};', s.find(hint_marker))+2])
    s = s.replace(hint_marker, hint_marker + insert, 1)

# Update visible stats text.
s = s.replace('agora inclui Fundamentos/Pleno (OO, Big-O, HTTP, SQL, backend e testes) além da cobertura avançada; use a busca por uma única pista se não lembrar a formulação exata.',
              'cobertura sistemática ampliada com perguntas-base e repreguntas de Node, Event-Driven, Nest/API, React, OO/SOLID, banco, distribuídos, mensageria, K8s/GCP, testes, segurança e System Design; busque por qualquer pista da pergunta.')

p.write_text(s, encoding='utf-8')
print(f'V4.6 applied: {len(new_lines)} new searchable cards')
