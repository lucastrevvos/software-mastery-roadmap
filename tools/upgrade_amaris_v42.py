from pathlib import Path

p = Path('docs/amaris-fullstack-interview.html')
s = p.read_text(encoding='utf-8')
if 'INTERVIEW COPILOT V4.2' in s:
    raise SystemExit(0)

# Version labels
s = s.replace('Interview Copilot V4.1', 'Interview Copilot V4.2')
s = s.replace('INTERVIEW COPILOT V4.1', 'INTERVIEW COPILOT V4.2')

extras = r'''
,Q('Event-Driven','O que é Event-Driven Architecture?','É uma arquitetura em que componentes reagem a eventos que representam fatos ocorridos, em vez de depender apenas de chamadas síncronas diretas.','O ganho é desacoplamento temporal e escalabilidade; o custo é consistência eventual, observabilidade mais difícil e necessidade de idempotência.','event-driven architecture EDA events asynchronous broker pubsub')
,Q('Event-Driven','Evento vs comando: qual a diferença?','Comando expressa intenção: faça algo. Evento expressa fato: algo aconteceu.','Um comando normalmente tem um alvo esperado; evento pode ter zero, um ou muitos consumidores sem o produtor conhecê-los.','event command intent fact event-driven cqrs')
,Q('Event-Driven','Event notification vs event-carried state transfer?','Notification avisa que algo mudou e o consumidor busca detalhes; event-carried leva dados suficientes no próprio evento.','Notification reduz payload e duplicação, mas aumenta chamadas; carried state reduz acoplamento em runtime, mas duplica dados e exige governança de schema.','event notification event carried state transfer integration event')
,Q('Event-Driven','Choreography vs orchestration?','Choreography deixa serviços reagirem a eventos entre si; orchestration usa um coordenador explícito do fluxo.','Choreography reduz centralização, mas pode esconder fluxo global; orchestration deixa o processo visível, mas cria um coordenador importante.','choreography orchestration saga event-driven')
,Q('Event-Driven','Quando usar arquitetura event-driven?','Quando desacoplamento, processamento assíncrono, fan-out, integração entre domínios ou elasticidade trazem valor real.','Eu evitaria se o fluxo precisa de resposta imediata simples e o custo de eventual consistency/observabilidade não se justifica.','when use event-driven async fanout decoupling')
,Q('Event-Driven','Quando NÃO usar event-driven?','Quando uma chamada síncrona simples resolve melhor, o domínio exige resposta imediata ou a equipe não consegue operar a complexidade adicional.','Event-driven não é sinônimo de arquitetura melhor; adiciona broker, redelivery, ordering, schemas e debugging distribuído.','when not use event-driven tradeoff complexity')
,Q('Event-Driven','Event-driven significa usar Kafka?','Não. Kafka, RabbitMQ e Pub/Sub são mecanismos possíveis; event-driven é um estilo arquitetural.','Posso implementar eventos com brokers diferentes, streams ou até mecanismos internos, conforme semântica necessária.','event-driven kafka rabbitmq pubsub broker architecture')
,Q('Event-Driven','Como lidar com duplicidade de eventos?','Assumo que duplicatas podem ocorrer e torno o consumidor idempotente com identificador único e garantia persistente.','Dedup só em memória não basta após restart; o ponto do efeito precisa estar protegido.','event duplicate idempotency consumer dedup')
,Q('Event-Driven','Como lidar com ordering?','Primeiro descubro se ordem é realmente uma invariável e em qual escopo.','Quando necessária, particiono por chave/entidade, uso sequence/version e rejeito ou reordeno eventos fora de sequência conforme o domínio.','event ordering partition key sequence version')
,Q('Event-Driven','Como versionar eventos?','Trato evento como contrato: mudanças compatíveis primeiro e evolução de schema explícita.','Evito remover/renomear campos abruptamente; consumidores podem ficar versões diferentes por algum tempo.','event schema evolution versioning backward compatible contract')
,Q('Event-Driven','O que é um Domain Event?','É um fato relevante ocorrido dentro de um domínio, expresso na linguagem daquele domínio.','Nem todo domain event deve sair do bounded context; para integração posso traduzir para um integration event estável.','domain event integration event DDD bounded context')
,Q('Event-Driven','Domain Event vs Integration Event?','Domain event modela um fato interno do domínio; integration event é contrato publicado para outros contextos/sistemas.','Separar os dois evita vazar o modelo interno e permite evolução independente.','domain event integration event bounded context contract')
,Q('Event-Driven','Event-driven vs Event Sourcing?','Event-driven é comunicação/reação baseada em eventos; Event Sourcing persiste eventos como fonte de verdade do estado.','Um sistema pode ser event-driven sem Event Sourcing e vice-versa.','event-driven event sourcing difference')
,Q('Event-Driven','Event-driven exige CQRS?','Não. CQRS e event-driven podem combinar bem, mas são decisões independentes.','CQRS separa leitura e escrita; event-driven define como mudanças/fatos propagam e acionam processamento.','event-driven cqrs difference')
,Q('Event-Driven','Qual relação entre Outbox e Event-Driven?','Outbox ajuda a publicar eventos de forma confiável quando o estado de negócio e o evento precisam nascer juntos.','Persisto ambos na mesma transação local e um worker publica depois; ainda projeto para duplicidade.','outbox event-driven dual write reliable publish')
,Q('Event-Driven','Como observar um fluxo event-driven?','Uso correlation/trace IDs, logs estruturados, métricas de lag/retry/DLQ e tracing distribuído.','Sem correlação entre eventos, investigar um fluxo assíncrono vira caça ao log.','event-driven observability trace correlation lag dlq')
,Q('Event-Driven','Como lidar com poison message?','Retry limitado para falha transitória e depois DLQ/quarentena com alerta e estratégia de correção/replay.','Requeue infinito só congestiona a fila e esconde o problema.','poison message dlq retry event-driven')
,Q('Event-Driven','Como lidar com backpressure?','Meço taxa de produção versus consumo e limito concorrência, aplico batching, autoscaling ou desacelero producers quando possível.','Escalar consumer sem observar DB/API downstream pode só mover o gargalo.','backpressure event-driven consumer lag throughput')
,Q('Event-Driven','Como testar um fluxo event-driven?','Testo contrato, idempotência, duplicidade, ordering relevante, retries, DLQ e falhas antes/depois do efeito.','Testes de integração com broker real/Testcontainers capturam semânticas que mocks podem esconder.','event-driven testing contract idempotency testcontainers broker')
,Q('Event-Driven','Como evitar acoplamento escondido por eventos?','Defino ownership e contratos claros, evito eventos genéricos demais e monitoro dependências entre consumidores.','Assíncrono reduz acoplamento temporal, não elimina acoplamento semântico.','event-driven coupling semantic contract consumers')
,Q('Event-Driven','Fan-out: o que significa?','Um único evento pode ser consumido independentemente por vários consumidores.','Cada consumidor precisa ter seu próprio estado de entrega/assinatura sem competir pelo mesmo efeito quando o objetivo é broadcast.','fanout pubsub event-driven consumers')
,Q('DDD','O que é Domain-Driven Design?','É uma abordagem para modelar software a partir do domínio e da linguagem do negócio, concentrando complexidade onde ela realmente existe.','DDD não é sinônimo de criar muitas classes; inclui bounded contexts, ubiquitous language e modelos alinhados ao domínio.','DDD domain driven design domain model')
,Q('DDD','O que é Bounded Context?','É uma fronteira dentro da qual um modelo e seus termos têm significado consistente.','O mesmo termo pode significar coisas diferentes em contextos diferentes sem precisar de um modelo universal.','bounded context DDD context boundary')
,Q('DDD','O que é Ubiquitous Language?','É a linguagem compartilhada entre negócio e tecnologia usada no modelo, código e conversas.','Ela reduz tradução mental e ajuda o código a refletir conceitos do domínio.','ubiquitous language DDD domain')
,Q('DDD','O que é Aggregate e Aggregate Root?','Aggregate é um conjunto de objetos tratado como uma unidade de consistência; a root é a porta de entrada para suas invariantes.','Eu evito aggregates gigantes e mantenho a transação local dentro da fronteira quando possível.','aggregate aggregate root DDD invariant transaction')
,Q('DDD','Repository no DDD?','É uma abstração para carregar e persistir aggregates como se fossem uma coleção do domínio.','O contrato pertence ao núcleo; detalhes de ORM/SQL ficam na infraestrutura.','repository DDD aggregate persistence')
,Q('DDD','Domain Service vs Application Service?','Domain Service contém regra de domínio que não pertence naturalmente a uma entidade/value object; Application Service coordena caso de uso e infraestrutura.','Application Service orquestra; Domain Service modela regra do negócio.','domain service application service DDD')
,Q('DDD','Anti-Corruption Layer?','É uma camada de tradução que impede o modelo de um sistema externo de contaminar meu domínio.','Uso adapters/mappers para converter conceitos externos para a linguagem do meu bounded context.','anti corruption layer ACL DDD integration adapter')
,Q('Testes','O que é TDD?','É um ciclo de desenvolvimento em que escrevo um teste falhando, implemento o mínimo para passar e refatoro.','O valor está no feedback rápido e no design guiado por comportamento, não em buscar 100% de cobertura.','TDD test driven development red green refactor')
,Q('Testes','TDD vs BDD?','TDD enfatiza o ciclo de desenvolvimento guiado por testes; BDD enfatiza comportamento e linguagem compartilhada sobre cenários esperados.','Eles podem coexistir: BDD ajuda a descrever comportamento, TDD guia implementação em ciclos curtos.','TDD BDD test driven behavior driven development')
'''

marker = '\nconst shortOverrides={'
idx = s.find(marker)
if idx < 0:
    raise SystemExit('shortOverrides marker not found')
arr_end = s.rfind('\n];', 0, idx)
if arr_end < 0:
    raise SystemExit('questions array end not found')
s = s[:arr_end] + extras + s[arr_end:]

# Add Event-Driven to HOT ZONE.
s = s.replace("const hotTerms=['event loop'", "const hotTerms=['event loop','Event-Driven','DDD'")

# Add map cards before existing interview map items.
map_marker = "const interviewMap=[\n"
map_add = "['Event-Driven','evento → command vs event → sync/async → idempotência → ordering → schema → saga → observabilidade',['Event-Driven','event command','choreography orchestration','idempotência','event ordering','schema evolution','saga','event-driven observability']],\n['DDD','ubiquitous language → bounded context → aggregate → domain events → repositories → integração',['DDD','bounded context','aggregate root','domain event','repository DDD','anti corruption layer']],\n"
if map_marker in s:
    s = s.replace(map_marker, map_marker + map_add, 1)

# Add likely follow-up hints.
hints_marker = "const nextHints={\n"
hints = "'O que é Event-Driven Architecture?':'Qual a diferença entre um evento e um comando?',\n'Evento vs comando: qual a diferença?':'E choreography versus orchestration, quando escolheria cada uma?',\n'Choreography vs orchestration?':'Como você garante consistência se cada serviço tem seu próprio banco?',\n'Event-driven vs Event Sourcing?':'E CQRS, ele é obrigatório nesse desenho?',\n'O que é Domain-Driven Design?':'Então me explique bounded context e aggregate root.',\n"
if hints_marker in s:
    s = s.replace(hints_marker, hints_marker + hints, 1)

# Upgrade visible labels.
s = s.replace('<!-- INTERVIEW COPILOT V4 -->', '<!-- INTERVIEW COPILOT V4.2 -->')
p.write_text(s, encoding='utf-8')
print('V4.2 applied')
