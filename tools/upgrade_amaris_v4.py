from pathlib import Path

p = Path('docs/amaris-fullstack-interview.html')
s = p.read_text(encoding='utf-8')
if 'INTERVIEW COPILOT V4' in s:
    raise SystemExit(0)

s = s.replace('Amaris Full Stack Senior — Interview Copilot V3', 'Amaris Full Stack Senior — Interview Copilot V4')
s = s.replace('⚡ Amaris — INTERVIEW COPILOT V3', '⚡ Amaris — INTERVIEW COPILOT V4')
s = s.replace('INTERVIEW COPILOT V3 · resposta curta + resposta completa + aprofundamento · 50 perguntas encadeadas no Alexandre Mode · HOT ZONE · busca PT/EN · modo pânico.', 'INTERVIEW COPILOT V4 · banco ampliado · resposta curta + completa + aprofundamento + próxima pergunta provável · Alexandre Mode · mapa por domínio · busca PT/EN · modo pânico.')

# Add Map button.
s = s.replace('<button id="alexBtn" class="alex-btn" type="button" title="Atalho: A">🎯 Alexandre</button>', '<button id="alexBtn" class="alex-btn" type="button" title="Atalho: A">🎯 Alexandre</button><button id="mapBtn" class="alex-btn" type="button" title="Atalho: M">🌳 Mapa</button>')
s = s.replace('<code>A</code> Alexandre Mode · <code>P</code> modo pânico', '<code>A</code> Alexandre Mode · <code>M</code> mapa · <code>P</code> modo pânico')

css = r'''
/* INTERVIEW COPILOT V4 */
.next-block{margin-top:11px;padding-top:10px;border-top:1px dashed #35415f}.next-block .label{color:#ffcf7f}.next-q{margin:0;color:#f4dfb4;line-height:1.48}.map-panel{display:none;border:1px solid #406b55;background:rgba(13,37,28,.84);border-radius:16px;padding:16px;margin-bottom:18px}.map-mode .map-panel{display:block}.map-mode #grid,.map-mode .hotzone,.map-mode .hero,.map-mode .alex-panel{display:none}.map-mode header h1:after{content:' · MAPA';color:#89ddb0}.map-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:10px}.map-card{border:1px solid #315943;background:#0e241a;border-radius:13px;padding:13px}.map-card h3{margin:0 0 8px;font-size:14px;color:#c9f2da}.map-card p{font-size:12px;color:#94b9a3;margin:0 0 9px}.map-terms{display:flex;gap:6px;flex-wrap:wrap}.map-term{border:1px solid #3d7254;background:#153322;color:#c9efd9;border-radius:999px;padding:5px 8px;font-size:11px;cursor:pointer}.map-term:hover{border-color:#7fd6a4}.panic .next-block{display:none}.statsbar{font-size:12px;color:#8da0c1;margin-top:6px}.priority{color:#ffcf7f;font-weight:700}
'''
s = s.replace('</style>', css + '\n</style>', 1)

map_html = r'''
<section id="mapPanel" class="map-panel">
  <div class="alex-head"><div><h2>🌳 Mapa de entrevista Senior</h2><p>Entre pelo assunto que você ouviu e avance pela árvore. Cada termo abre a busca correspondente.</p></div><button id="mapExit" class="alex-search" type="button">Sair do mapa</button></div>
  <div id="mapGrid" class="map-grid"></div>
</section>
'''
s = s.replace('<section id="alexPanel" class="alex-panel">', map_html + '<section id="alexPanel" class="alex-panel">', 1)

extras = r'''
,Q('JavaScript Avançado','Como funciona o prototype chain?','Objetos podem delegar lookup de propriedades para outro objeto via prototype. A busca sobe a cadeia até encontrar a propriedade ou chegar a null.','Isso explica herança prototípica, métodos compartilhados e por que shadowing acontece quando a propriedade existe no próprio objeto.','prototype chain prototypal inheritance Object.create __proto__ shadowing')
,Q('JavaScript Avançado','this em arrow function vs function normal?','Arrow não cria seu próprio this; ela captura lexicalmente o this externo. Function normal recebe this conforme a forma de chamada.','Por isso arrow é útil em callbacks, mas não substitui métodos normais em todos os cenários.','this arrow lexical bind call apply javascript')
,Q('JavaScript Avançado','call, apply e bind?','call e apply executam a função definindo this; bind cria outra função com this e argumentos parcialmente fixados.','A diferença call/apply é principalmente a forma de passar argumentos.','call apply bind this javascript partial application')
,Q('JavaScript Avançado','Map vs Object?','Map é uma coleção chave-valor própria para dados dinâmicos e aceita qualquer tipo de chave; Object é também a estrutura base da linguagem.','Map tem size, iteração previsível e não sofre com chaves herdadas do prototype.','map object key value javascript collection')
,Q('JavaScript Avançado','Set serve para quê?','Representa coleção de valores únicos.','É útil para deduplicação e membership checks; a escolha depende de semântica, não só performance.','set unique dedupe membership javascript')
,Q('JavaScript Avançado','Generator function: quando usar?','Generator produz valores sob demanda e pausa entre yields.','Pode representar sequências lazy, iteradores e pipelines sem materializar tudo em memória.','generator yield iterator lazy javascript')
,Q('JavaScript Avançado','Iterable e Iterator: diferença?','Iterable expõe Symbol.iterator; Iterator produz next() com value e done.','Um objeto pode ser ambos, mas os conceitos são distintos.','iterable iterator symbol.iterator next javascript')
,Q('JavaScript Avançado','EventEmitter: cuidado com quê?','Listeners precisam de ciclo de vida claro; listeners acumulados podem causar leak e comportamento duplicado.','Também observo ordem síncrona dos listeners e tratamento do evento error.','eventemitter listener memory leak node events')
,Q('JavaScript Avançado','O que é event-loop starvation?','É quando uma sequência de trabalho impede o loop de avançar e atender I/O/timers em tempo razoável.','Pode vir de CPU longa ou abuso de microtasks/nextTick.','starvation event loop microtasks nextTick cpu')
,Q('JavaScript Avançado','Como o garbage collector afeta latência?','GC recupera memória não alcançável, mas ciclos de coleta podem consumir CPU e gerar pausas.','Eu procuro alocação excessiva, heap crescendo e pressão de memória antes de culpar o GC isoladamente.','garbage collector gc heap latency v8 memory')
,Q('TypeScript Avançado','keyof serve para quê?','Produz uma union das chaves conhecidas de um tipo.','Com generics ajuda a restringir acesso a propriedades de forma segura.','keyof typescript generics keys')
,Q('TypeScript Avançado','typeof no TypeScript?','Em posição de tipo, typeof obtém o tipo de um valor declarado.','É diferente do typeof de runtime do JavaScript.','typeof typescript type query runtime')
,Q('TypeScript Avançado','Mapped types?','Transformam sistematicamente propriedades de outro tipo.','Utility types como Partial e Readonly são exemplos de mapped types.','mapped types Partial Readonly typescript')
,Q('TypeScript Avançado','Conditional types?','Escolhem um tipo com base em uma relação de tipos usando T extends U ? X : Y.','São poderosos em APIs genéricas, mas podem reduzir legibilidade se usados demais.','conditional types extends infer typescript')
,Q('TypeScript Avançado','infer serve para quê?','Permite capturar um tipo dentro de conditional types.','Exemplo clássico é extrair retorno, parâmetros ou elemento de Promise/array.','infer conditional type typescript')
,Q('TypeScript Avançado','satisfies vs as?','satisfies valida compatibilidade preservando inferência específica; as força uma asserção e pode esconder erro.','Prefiro satisfies quando quero verificar formato sem alargar o tipo.','satisfies as assertion typescript inference')
,Q('TypeScript Avançado','unknown na borda da aplicação?','Dados externos devem começar como desconhecidos até passarem por validação.','Tipagem estática não valida JSON recebido em runtime.','unknown validation runtime boundary typescript')
,Q('TypeScript Avançado','Readonly torna objeto profundamente imutável?','Não necessariamente; Readonly padrão é superficial.','Imutabilidade profunda exige modelagem/utility específica e ainda é uma garantia de tipo, não congelamento de runtime.','readonly immutable deep typescript')
,Q('Node Avançado','UV_THREADPOOL_SIZE: o que controla?','Controla o tamanho do thread pool usado pelo libuv para certas operações.','Aumentar cegamente não melhora tudo; precisa entender workload, CPU e quais APIs realmente usam o pool.','UV_THREADPOOL_SIZE libuv thread pool node')
,Q('Node Avançado','Cluster vs Worker Threads?','Cluster cria múltiplos processos; Worker Threads criam threads dentro do processo.','Cluster isola memória e escala cores para servidores; workers são melhores para CPU-bound compartilhando contexto quando necessário.','cluster worker threads process node cpu')
,Q('Node Avançado','child_process: quando usar?','Quando preciso executar outro processo/comando ou isolar uma tarefa num processo separado.','Tem custo e implicações de segurança; argumentos nunca devem ser montados com entrada não confiável.','child_process exec spawn fork node security')
,Q('Node Avançado','spawn vs exec?','spawn trabalha com streams e é melhor para saída grande; exec bufferiza saída e é conveniente para comandos pequenos.','Também considero shell injection ao escolher a API.','spawn exec child process streams buffer')
,Q('Node Avançado','Buffer em Node?','Representa dados binários fora do modelo de string comum.','Aparece em rede, arquivos, criptografia e streams; conversão de encoding precisa ser explícita.','buffer binary utf8 base64 node')
,Q('Node Avançado','Stream readable/writable/transform?','Readable produz dados, Writable consome e Transform faz ambos transformando chunks.','Pipelines ajudam propagação de backpressure e erros.','readable writable transform stream pipeline node')
,Q('Node Avançado','pipeline() por que usar?','Conecta streams com propagação adequada de erro e finalização.','É mais seguro que encadear pipe manualmente em fluxos complexos.','stream pipeline pipe error backpressure node')
,Q('Node Avançado','AbortController em Node?','Permite cancelar operações assíncronas que aceitam AbortSignal.','É útil para propagar deadlines/cancelamento e evitar trabalho inútil após timeout do cliente.','AbortController AbortSignal cancel timeout node')
,Q('Node Avançado','AsyncLocalStorage serve para quê?','Mantém contexto assíncrono por fluxo de execução, como correlation/trace IDs.','Ajuda logging contextual sem passar ID por todas as assinaturas, mas precisa uso consciente.','AsyncLocalStorage context correlation id node')
,Q('Node Avançado','Como fazer profiling em Node?','Meço CPU, heap, event-loop lag e traces antes de otimizar.','Ferramentas de CPU profile e heap snapshot ajudam a separar CPU-bound, leak e dependência lenta.','profiling cpu heap event loop node performance')
,Q('Node Avançado','O que é graceful degradation?','Quando uma parte falha, o serviço mantém funcionalidade reduzida em vez de cair inteiro.','Exemplo: retornar dados sem recomendação se um serviço secundário estiver indisponível.','graceful degradation fallback resilience node')
,Q('NestJS Avançado','Dynamic Module no NestJS?','É um módulo configurável em runtime que retorna metadata de providers/imports/exports.','É comum em módulos reutilizáveis com forRoot/forRootAsync.','nestjs dynamic module forRoot forRootAsync')
,Q('NestJS Avançado','Custom provider com useFactory/useClass/useValue?','São formas diferentes de dizer ao container como fornecer um token.','useFactory permite dependências/config dinâmica; useValue é útil para constante/mock; useClass troca implementação.','nestjs provider useFactory useClass useValue token')
,Q('NestJS Avançado','Circular dependency no Nest: o que fazer?','Primeiro revejo o desenho; circularidade costuma indicar boundary ruim.','forwardRef existe, mas é último recurso, não solução arquitetural automática.','nestjs circular dependency forwardRef architecture')
,Q('NestJS Avançado','Lifecycle hooks no Nest?','Permitem reagir a inicialização e encerramento do módulo/aplicação.','São úteis para conexões, consumers e shutdown coordenado.','nestjs lifecycle OnModuleInit OnApplicationShutdown')
,Q('NestJS Avançado','Global module: risco?','Facilita acesso, mas aumenta dependência implícita e acoplamento.','Prefiro imports explícitos para manter fronteiras visíveis.','nestjs global module coupling')
,Q('NestJS Avançado','Custom decorator: quando faz sentido?','Quando quero encapsular metadata ou composição repetida na borda.','Evito esconder regra de negócio dentro de decorator mágico.','nestjs custom decorator metadata')
,Q('NestJS Avançado','Nest microservices transport?','Nest fornece abstrações para transports de mensageria, mas a semântica real continua pertencendo ao broker.','Eu não deixaria a abstração esconder ACK, retry, ordering e idempotência.','nestjs microservices transport rabbitmq kafka')
,Q('React Avançado','O que é reconciliation?','É o processo de comparar a árvore React anterior com a próxima para decidir o que atualizar.','Keys e identidade de componentes influenciam preservação de estado.','react reconciliation keys identity fiber')
,Q('React Avançado','O que é Fiber?','É a arquitetura interna que permite quebrar trabalho de renderização e priorizar atualizações.','O ponto prático é entender que render pode ser interrompido/recomeçado e deve ser puro.','react fiber concurrent rendering')
,Q('React Avançado','Strict Mode por que chama coisas duas vezes em dev?','Ajuda detectar efeitos e renderizações com side effects não seguros.','Não é comportamento de produção, mas expõe código que depende de execução única acidental.','react strict mode double render development')
,Q('React Avançado','useRef vs useState?','State participa da renderização; ref guarda valor mutável persistente sem causar render quando muda.','Uso ref para DOM, handles ou estado imperativo que não deve dirigir UI.','useRef useState react')
,Q('React Avançado','useReducer: quando usar?','Quando transições de estado ficam complexas ou relacionadas e quero centralizar regras de atualização.','Não é automaticamente melhor que useState; depende da complexidade das transições.','useReducer state machine react')
,Q('React Avançado','React.memo resolve performance?','Só evita alguns renders quando props são consideradas iguais; não corrige arquitetura de estado ruim.','Memoização também custa comparação e complexidade.','React.memo memo performance rerender')
,Q('React Avançado','Suspense: modelo mental?','Permite coordenar UI enquanto uma parte da árvore ainda não está pronta.','O comportamento depende do framework/fonte de dados; não trato Suspense como fetch genérico sem suporte.','react suspense lazy loading')
,Q('React Avançado','Code splitting?','Divide bundle para carregar código sob demanda.','Lazy loading de rotas/componentes reduz custo inicial, mas aumenta requests e exige estratégia de loading.','code splitting lazy bundle react vite webpack')
,Q('React Avançado','Por que index como key pode ser problema?','Se a lista reordena, React pode associar estado local ao item errado.','Uso identidade estável do domínio quando possível.','react key index list state')
,Q('React Avançado','Race condition em fetch no React?','Uma resposta antiga pode chegar depois de uma nova e sobrescrever estado atual.','Uso cancelamento, identidade da requisição ou biblioteca de server state para coordenar isso.','react fetch race abortcontroller stale response')
,Q('Banco Avançado','MVCC: o que é?','Multi-Version Concurrency Control mantém versões para permitir leituras concorrentes sem bloquear toda escrita.','É base para entender snapshots e comportamento de isolamento em bancos como PostgreSQL.','mvcc postgres transaction snapshot concurrency')
,Q('Banco Avançado','WAL serve para quê?','Write-Ahead Log registra mudanças antes de aplicá-las definitivamente nas páginas de dados.','É fundamental para recuperação e replicação.','wal write ahead log postgres durability replication')
,Q('Banco Avançado','VACUUM no PostgreSQL?','Recupera/gerencia tuplas mortas geradas pelo MVCC e ajuda manter o banco saudável.','Autovacuum mal dimensionado pode levar a bloat e problemas operacionais.','vacuum autovacuum postgres bloat mvcc')
,Q('Banco Avançado','Partial index?','Indexa apenas linhas que atendem uma condição.','É útil quando queries frequentes focam um subconjunto pequeno, como registros ativos.','partial index postgres where')
,Q('Banco Avançado','Covering index / INCLUDE?','Permite que o índice carregue colunas adicionais para evitar acesso à tabela em certas queries.','Melhora algumas leituras ao custo de índice maior e escrita mais cara.','covering index include postgres index only scan')
,Q('Banco Avançado','Connection pool: por que importa?','Abrir conexão por request é caro e o banco tem limite de concorrência.','Pool controla reutilização e precisa ser dimensionado considerando número de instâncias.','connection pool postgres cloud run database')
,Q('Banco Avançado','Partitioning vs sharding?','Partitioning divide dados logicamente dentro de um sistema/banco; sharding distribui dados entre nós independentes.','Sharding aumenta complexidade de queries, rebalanceamento e consistência.','partitioning sharding database scale')
,Q('Banco Avançado','Replica de leitura: cuidado com quê?','Pode aliviar leitura, mas introduz replication lag.','Não mando leitura que precisa enxergar imediatamente a própria escrita para uma réplica eventualmente atrasada.','read replica replication lag consistency')
,Q('Banco Avançado','Phantom read?','Uma transação repete uma consulta por predicado e encontra conjunto diferente de linhas devido a outra transação.','O comportamento depende do isolation level e implementação do banco.','phantom read isolation transaction database')
,Q('Banco Avançado','Lost update?','Duas transações leem o mesmo valor e uma sobrescreve silenciosamente a atualização da outra.','Versionamento, update condicional ou isolamento adequado podem prevenir.','lost update concurrency optimistic locking')
,Q('Distribuídos Avançado','Quorum: modelo mental?','Operações exigem respostas de um subconjunto de réplicas para equilibrar consistência e disponibilidade.','A relação entre número de réplicas, leituras e escritas define sobreposição e garantias.','quorum replication distributed consistency')
,Q('Distribuídos Avançado','Leader election?','É escolher um nó responsável por coordenar determinada função.','Precisa lidar com falha, lease/termo e evitar dois líderes ativos ao mesmo tempo.','leader election distributed consensus lease')
,Q('Distribuídos Avançado','Split brain?','É quando partes do sistema acreditam simultaneamente que são autoridade/líder.','Fencing, quorum e protocolos de consenso ajudam evitar efeitos conflitantes.','split brain fencing quorum leader')
,Q('Distribuídos Avançado','Fencing token?','É um número monotônico usado para rejeitar operações de um lock/lease antigo.','Resolve o problema de um cliente pausado continuar agindo após perder o lock.','fencing token distributed lock lease')
,Q('Distribuídos Avançado','Lamport clock: para quê?','Dá uma ordem lógica parcial consistente com causalidade sem depender do relógio físico.','Não representa tempo real, mas ajuda ordenar eventos logicamente.','lamport clock logical time distributed')
,Q('Distribuídos Avançado','Vector clock: ideia principal?','Carrega informação suficiente para detectar causalidade e concorrência entre versões.','É mais informativo que Lamport, mas cresce com participantes.','vector clock causality distributed')
,Q('Distribuídos Avançado','Load shedding?','Recusar parte da carga antes que o sistema entre em colapso.','É melhor falhar rápido e controlado do que saturar todos os recursos.','load shedding overload backpressure resilience')
,Q('Distribuídos Avançado','Backpressure entre serviços?','É controlar a taxa para não produzir mais trabalho do que downstream consegue consumir.','Pode usar filas, limites de concorrência, créditos, rate limit ou feedback de lag.','backpressure distributed queue concurrency')
,Q('Distribuídos Avançado','Hedged requests?','Disparam uma segunda tentativa para reduzir tail latency de requests lentos.','Podem melhorar P99, mas aumentam carga e precisam uso seletivo.','hedged requests tail latency p99 distributed')
,Q('Distribuídos Avançado','Thundering herd?','Muitos clientes acordam/retry/recalculam ao mesmo tempo e sobrecarregam o recurso.','Jitter, single-flight e cache strategies ajudam reduzir.','thundering herd jitter retry cache')
,Q('Mensageria Avançado','Kafka retention vs compaction?','Retention remove eventos por tempo/tamanho; compaction preserva a versão mais recente por chave ao longo do log.','São mecanismos diferentes e podem coexistir.','kafka retention compaction log key')
,Q('Mensageria Avançado','Kafka ISR?','In-Sync Replicas são réplicas suficientemente atualizadas com o leader.','Configuração de acks e min.insync.replicas afeta durabilidade/disponibilidade de escrita.','kafka ISR min insync replicas acks')
,Q('Mensageria Avançado','Kafka acks=all significa exatamente uma vez?','Não. Melhora durabilidade do publish, mas exactly-once end-to-end envolve produtor, broker, consumidor e efeitos externos.','Ainda preciso idempotência ou transações no escopo adequado.','kafka acks all exactly once durability')
,Q('Mensageria Avançado','Consumer lag no Kafka?','É a diferença entre o último offset disponível e o offset consumido.','Lag crescente pode indicar consumidor lento, erro, partition skew ou downstream saturado.','kafka consumer lag monitoring')
,Q('Mensageria Avançado','Partition skew?','Algumas partitions recebem muito mais tráfego que outras por causa da distribuição de chaves.','Mesmo com muitos consumers, a hot partition vira gargalo.','kafka partition skew hot key')
,Q('Mensageria Avançado','RabbitMQ direct, topic e fanout?','Direct roteia por chave exata, topic por padrões e fanout replica para todas as filas ligadas.','Escolho exchange conforme semântica de roteamento.','rabbitmq direct topic fanout exchange')
,Q('Mensageria Avançado','RabbitMQ quorum queue?','É uma fila replicada baseada em consenso para maior segurança de dados.','Tem custos e comportamento diferentes de classic queue; escolho conforme durabilidade e throughput.','rabbitmq quorum queue replication')
,Q('Mensageria Avançado','ACK deadline no Pub/Sub?','É a janela em que a mensagem precisa ser confirmada antes de poder ser redeliver.','Processamento longo exige extensão/gestão correta e continua precisando idempotência.','pubsub ack deadline redelivery')
,Q('Mensageria Avançado','Ordering key no Pub/Sub?','Permite preservar ordem relativa para mensagens com a mesma key quando configurado.','Ordenação reduz liberdade de paralelismo e precisa ser usada só onde é requisito real.','pubsub ordering key gcp')
,Q('Kubernetes Avançado','StatefulSet vs Deployment?','StatefulSet dá identidade estável e ordenação a pods stateful; Deployment é melhor para réplicas intercambiáveis/stateless.','Não uso StatefulSet só porque existe banco; operar estado no cluster traz responsabilidade grande.','statefulset deployment kubernetes')
,Q('Kubernetes Avançado','DaemonSet?','Garante uma cópia do pod por nó elegível.','É comum para agentes de log, rede ou monitoramento.','daemonset kubernetes node agent')
,Q('Kubernetes Avançado','Job vs CronJob?','Job executa trabalho até completar; CronJob agenda Jobs periodicamente.','Preciso pensar em idempotência, concurrency policy e retries.','job cronjob kubernetes batch')
,Q('Kubernetes Avançado','Ingress vs Service?','Service fornece acesso estável aos pods; Ingress define roteamento HTTP externo via controller compatível.','Em clouds modernas também posso usar Gateway API conforme stack.','ingress service kubernetes gateway')
,Q('Kubernetes Avançado','Affinity e anti-affinity?','Controlam preferência/restrição de onde pods são agendados em relação a nós ou outros pods.','Anti-affinity pode espalhar réplicas para reduzir risco de falha correlacionada.','affinity anti affinity kubernetes scheduling')
,Q('Kubernetes Avançado','Taints e tolerations?','Taint afasta pods de um nó; toleration permite que pods específicos sejam agendados ali.','É útil para workloads dedicados, GPUs ou isolamento operacional.','taints tolerations kubernetes scheduling')
,Q('Kubernetes Avançado','PDB serve para quê?','PodDisruptionBudget limita quantos pods podem ficar indisponíveis durante disruptions voluntários.','Não protege contra todas as falhas; ajuda em manutenção/drain.','PDB pod disruption budget kubernetes')
,Q('Kubernetes Avançado','OOMKilled?','O processo ultrapassou o limite/capacidade de memória e foi terminado.','Investigo leak, working set, requests/limits e padrão de carga.','OOMKilled kubernetes memory limit')
,Q('Kubernetes Avançado','CPU throttling?','Quando o container tenta usar CPU acima do limit, pode ser limitado e aumentar latência.','Limits muito baixos podem piorar P99 mesmo sem crash.','cpu throttling kubernetes limits latency')
,Q('Kubernetes Avançado','Rolling update com migration: risco?','Versões antiga e nova podem coexistir durante rollout.','Por isso schema changes devem ser backward-compatible, usando expand-and-contract.','rolling update migration expand contract kubernetes')
,Q('GCP Avançado','Cloud Run concurrency?','Define quantas requisições simultâneas uma instância pode atender.','Ela impacta CPU, memória, pool de conexões e quantidade de instâncias.','cloud run concurrency gcp autoscaling')
,Q('GCP Avançado','Cloud Run min/max instances?','Min reduz cold start mantendo capacidade; max protege downstream/custo limitando escala.','Max também pode ser parte da proteção do banco.','cloud run min instances max instances cost')
,Q('GCP Avançado','Cold start?','É o custo de iniciar nova instância antes de atender tráfego.','Mitigo reduzindo startup, usando min instances quando justificado e escolhendo runtime/imagem adequados.','cold start cloud run functions serverless')
,Q('GCP Avançado','Pub/Sub DLQ no GCP?','Configuro dead-letter topic com política de tentativas para isolar mensagens problemáticas.','Ainda preciso observabilidade e processo de replay/correção.','gcp pubsub dead letter topic dlq')
,Q('GCP Avançado','Cloud SQL HA?','Usa arquitetura gerenciada com failover conforme configuração/região.','Mesmo gerenciado, aplicação precisa timeout/reconnect e entender RTO/RPO.','cloud sql high availability failover gcp')
,Q('GCP Avançado','VPC Connector no serverless?','Permite workloads serverless acessarem recursos privados na VPC.','Tem implicações de rota, custo e capacidade; não adiciono sem necessidade.','vpc connector cloud run gcp networking')
,Q('GCP Avançado','Service Account por workload?','Cada workload deve ter identidade própria com least privilege.','Evito compartilhar credenciais amplas ou chaves estáticas.','service account workload identity iam gcp')
,Q('GCP Avançado','Cloud Run + Pub/Sub: como integrar?','Pub/Sub pode acionar serviço HTTP via push/Eventarc conforme desenho.','Eu valido autenticação, idempotência, ack/retry e timeout do handler.','cloud run pubsub eventarc gcp')
,Q('System Design','Projete um rate limiter distribuído.','Defino identidade, janela, precisão e comportamento em falha; token bucket em Redis é uma solução comum.','Preciso de operação atômica, TTL, particionamento e decisão sobre consistência entre regiões.','system design rate limiter redis token bucket')
,Q('System Design','Projete um serviço de webhook.','Persisto eventos, entrego assíncrono com assinatura, retry/backoff e DLQ.','Consumidor precisa idempotência e eu preciso status de entrega, rotação de segredo e observabilidade.','system design webhook retry signature dlq')
,Q('System Design','Projete notificações email/push/SMS.','Recebo intenção, persisto, enfileiro por canal e workers aplicam preferência, rate limit e retry.','Separo provider adapter, template, dedupe e DLQ; entrega costuma ser eventual.','system design notifications email push sms')
,Q('System Design','Projete upload e processamento de arquivos.','Upload direto para object storage com URL assinada e processamento assíncrono por evento/fila.','Evito passar arquivo grande pelo app quando não é necessário; considero antivírus, tamanho, idempotência e status.','system design file upload object storage queue')
,Q('System Design','Projete um scheduler distribuído.','Persisto jobs com próxima execução e workers reivindicam trabalho de forma concorrente.','Preciso de idempotência, leases/locks, retries e tolerância a nó morrer durante execução.','system design scheduler distributed jobs')
,Q('System Design','Projete auditoria de ações.','Eventos de auditoria devem ser append-only, com identidade, timestamp, ação e contexto suficiente.','Protejo integridade, retenção e acesso; não confundo audit log com log técnico.','system design audit log append only')
,Q('System Design','Projete cache para catálogo muito lido.','Cache-aside com TTL é um começo; desenho invalidação, stampede e comportamento quando cache cai.','Dados muito sensíveis a stale exigem estratégia diferente.','system design cache aside redis catalog')
,Q('System Design','Projete busca de produtos.','Banco transacional continua fonte de verdade e índice de busca é uma projeção assíncrona.','Aceito eventual consistency entre escrita e pesquisa e projeto reindexação.','system design search elastic opensearch eventual consistency')
,Q('System Design','Projete chat em tempo real.','Conexão persistente via WebSocket, roteamento de sessão, persistência e fanout.','Preciso presence, ordering por conversa, reconexão, dedupe e escalabilidade do gateway.','system design chat websocket realtime')
,Q('System Design','Projete um feed.','Defino fanout-on-write vs fanout-on-read conforme número de seguidores e padrão de leitura.','Caching, ranking, pagination por cursor e hot users viram trade-offs centrais.','system design feed fanout cursor')
,Q('Senioridade','Prazo impossível: como reage?','Torno escopo, risco e capacidade explícitos e proponho alternativas: reduzir escopo, fasear ou mover data.','Evito aceitar silenciosamente e criar dívida/risco escondido.','senior prazo deadline scope negotiation')
,Q('Senioridade','Você tomou uma decisão técnica errada. O que faz?','Reconheço cedo, quantifico impacto e proponho correção incremental.','Senioridade inclui atualizar opinião quando evidência muda e documentar aprendizado.','senior wrong decision ownership')
,Q('Senioridade','Quando refatorar e quando não?','Refatoro quando reduz risco/custo de mudança relevante; não paro entrega para perseguir perfeição sem impacto.','Busco refactors pequenos próximos da mudança e justifico por benefício observável.','senior refactor technical debt')
,Q('Senioridade','Como defender uma solução simples contra overengineering?','Mostro requisitos que a solução simples atende e o custo adicional da complexidade proposta.','Também deixo pontos de evolução claros caso os requisitos mudem.','senior overengineering simplicity architecture')
,Q('Senioridade','Como conduzir postmortem?','Foco em linha do tempo, impacto, fatores contribuintes e ações concretas, sem caça a culpado.','Ações precisam owner, prioridade e acompanhamento.','senior postmortem blameless incident')
,Q('Senioridade','Como comunicar risco para produto?','Traduzo detalhe técnico em impacto: indisponibilidade, atraso, custo, segurança ou velocidade futura.','Apresento opções e trade-offs, não só o problema.','senior communication product risk')
,Q('Senioridade','Como avaliar PR grande?','Primeiro entendo objetivo/arquitetura, depois corretude, segurança, testes e operabilidade.','Se ficou grande demais, sugiro decomposição para reduzir risco de revisão.','senior code review large pr')
,Q('Senioridade','Como lidar com legado sem testes?','Crio caracterização nos fluxos críticos antes de mudanças arriscadas e refatoro por bordas.','Evito big-bang rewrite sem necessidade.','senior legacy characterization tests strangler')
,Q('Senioridade','Reescrever ou evoluir sistema existente?','Reescrita tem custo e risco altos; exijo motivo concreto que evolução incremental não resolve.','Strangler pattern pode permitir substituição gradual.','senior rewrite strangler legacy')
,Q('Senioridade','Como medir sucesso de uma arquitetura?','Pelo comportamento real: confiabilidade, latência, custo, velocidade de entrega e facilidade de operação.','Diagrama bonito não é métrica de sucesso.','senior architecture success metrics')
'''
marker = '\n];\nconst shortOverrides='
if marker not in s:
    raise SystemExit('questions-array marker not found')
s = s.replace(marker, extras + marker, 1)

# Next-question hints for common/high-probability topics.
next_js = r'''
const nextHints={
'O que é o Event Loop?':'E o que acontece se eu colocar processamento pesado de CPU nessa thread?',
'Node.js é single-threaded?':'Então quando você usaria Worker Threads e quando preferiria uma fila?',
'Worker Threads: quando usar?':'Como você mede se o problema realmente é CPU-bound?',
'Como você organiza uma aplicação NestJS?':'E como evita que o domínio fique acoplado ao framework?',
'Provider e Dependency Injection?':'Quando DI vira abstração desnecessária?',
'REST: o que caracteriza uma boa API?':'Como você trataria idempotência em um POST de pagamento?',
'POST é idempotente?':'Como persistiria a Idempotency-Key de forma concorrente?',
'O que é idempotência?':'E se o processo cair depois do commit mas antes do ACK?',
'O que é Transactional Outbox?':'Como vários workers processariam a mesma outbox sem pegar a mesma linha?',
'FOR UPDATE SKIP LOCKED: para quê?':'Isso elimina a necessidade de idempotência?',
'RabbitMQ vs Kafka?':'Como você decide quando replay é requisito?',
'Kafka: o que é partition?':'O que acontece com ordering e paralelismo quando uso a mesma key?',
'Kafka consumer group?':'O que acontece durante um rebalance?',
'RabbitMQ ACK/NACK?':'Como evita requeue infinito de poison message?',
'GCP Pub/Sub: modelo mental?':'Como lida com redelivery e ACK deadline?',
'Monólito modular ou microsserviços?':'Que sinal concreto faria você extrair um serviço?',
'Quando extrair um microsserviço?':'Como evitar transação distribuída depois da extração?',
'useEffect: para que serve?':'E se o effect disparar duas requests ou capturar estado antigo?',
'Context API: quando usar?':'Quando Context começa a causar renders demais?',
'Como evitar renders desnecessários?':'Como você provaria que memoização realmente ajudou?',
'Índice: o que é e qual o custo?':'Como valida se o índice foi usado e melhorou a query?',
'Transação e ACID?':'Qual anomaly ainda pode ocorrer no isolation level escolhido?',
'Optimistic vs pessimistic locking?':'O que faria se o conflito otimista virar frequente?',
'Liveness vs readiness?':'Você colocaria dependência do banco na liveness?',
'Requests e limits?':'O que acontece com CPU throttling e OOMKilled?',
'Cloud Run vs GKE?':'Qual requisito faria você aceitar a complexidade operacional do GKE?',
'Unitário vs integração vs E2E?':'Qual parte você testaria com Testcontainers?',
'Coverage alto significa bons testes?':'Como você testa falha e concorrência, não só caminho feliz?',
'JWT: o que é e o que não é?':'Como você revoga acesso ou lida com refresh token?',
'Como você toma decisões arquiteturais?':'Como registra a decisão e sabe depois se ela funcionou?'
};
function nextFor(x){return nextHints[x.q]||''}
'''
anchor = 'function card(x,i){'
if anchor not in s:
    raise SystemExit('card function marker not found')
s = s.replace(anchor, next_js + '\n' + anchor, 1)

old = '''function card(x,i){const short=shortOverrides[x.q]||x.quick,full=fullAnswer(x);return `<article class="card" data-i="${i}" data-cat="${esc(x.category)}" data-search="${esc((x.category+' '+x.q+' '+short+' '+full+' '+x.deep+' '+x.tags+' '+x.safe).toLowerCase())}"><div class="catline"><span class="catbadge">${esc(x.category)}</span><span class="score"></span></div><h2>${esc(x.q)}</h2><div class="meta">${x.tags.split(' ').slice(0,7).map(t=>`<span class="tag">${esc(t)}</span>`).join('')}</div><div class="quick-block"><div class="label">⚡ Resposta curta · 5–10s</div><p class="answer">${esc(short)}</p></div><div class="full-block"><div class="label">🎯 Resposta completa · 20–40s</div><p class="full-answer">${esc(full)}</p></div><div class="pressure-block"><div class="label">🧠 Se ele aprofundar</div><p class="deep">${esc(x.deep)}</p></div>${x.safe?`<div class="safe-block"><div class="label">💼 Como puxar para prática</div><p class="safe">${esc(x.safe)}</p></div>`:''}</article>`}'''
new = '''function card(x,i){const short=shortOverrides[x.q]||x.quick,full=fullAnswer(x),next=nextFor(x);return `<article class="card" data-i="${i}" data-cat="${esc(x.category)}" data-search="${esc((x.category+' '+x.q+' '+short+' '+full+' '+x.deep+' '+x.tags+' '+x.safe+' '+next).toLowerCase())}"><div class="catline"><span class="catbadge">${esc(x.category)}</span><span class="score"></span></div><h2>${esc(x.q)}</h2><div class="meta">${x.tags.split(' ').slice(0,7).map(t=>`<span class="tag">${esc(t)}</span>`).join('')}</div><div class="quick-block"><div class="label">⚡ Resposta curta · 5–10s</div><p class="answer">${esc(short)}</p></div><div class="full-block"><div class="label">🎯 Resposta completa · 20–40s</div><p class="full-answer">${esc(full)}</p></div><div class="pressure-block"><div class="label">🧠 Se ele aprofundar</div><p class="deep">${esc(x.deep)}</p></div>${next?`<div class="next-block"><div class="label">🔥 Próxima pergunta provável</div><p class="next-q">${esc(next)}</p></div>`:''}${x.safe?`<div class="safe-block"><div class="label">💼 Como puxar para prática</div><p class="safe">${esc(x.safe)}</p></div>`:''}</article>`}'''
if old not in s:
    raise SystemExit('exact card function not found')
s = s.replace(old, new, 1)

# Knowledge map and mode wiring.
map_js = r'''
const interviewMap=[
['JavaScript / Node','event loop → libuv → microtasks → CPU-bound → workers → streams → memória → profiling',['event loop','libuv','microtask','worker threads','streams','memory leak','profiling']],
['TypeScript','tipagem → narrowing → generics → structural typing → mapped/conditional types → runtime validation',['TypeScript','narrowing','generics','structural typing','conditional types','unknown']],
['NestJS / API','modules → DI → controller/service → guards/pipes/interceptors → REST → auth → idempotência',['NestJS','dependency injection','guard interceptor pipe','API REST','JWT','idempotência']],
['React','render → reconciliation → state → effect → closures → context → server state → performance',['React render','reconciliation','useState','useEffect','stale closure','Context API','server state','React performance']],
['Distribuídos','falha parcial → timeout → retry → idempotência → outbox/inbox → consistency → locks → clocks',['distributed','timeout','retry','idempotência','outbox','inbox','eventual consistency','distributed lock','clock skew']],
['Mensageria','delivery → ACK → retry/DLQ → Rabbit/Kafka/PubSub → ordering → partitions → lag/rebalance',['at least once','ACK','DLQ','rabbitmq','kafka','Pub/Sub','ordering','consumer lag','rebalance']],
['Banco','ACID → isolation → MVCC → locks → índices → planner → pool → replication → partition/shard',['ACID','isolation','MVCC','deadlock','index','EXPLAIN ANALYZE','connection pool','replica','sharding']],
['Arquitetura','SOLID → ports/adapters → modular monolith → microservices → saga/CQRS → ADR → cache',['SOLID','hexagonal','monolith modular','microservices','saga','CQRS','ADR','cache']],
['Docker / K8s','image → pod → deployment/service → probes → resources → autoscale → stateful/scheduling → rollout',['docker image container','pod deployment service','liveness readiness','requests limits','HPA','StatefulSet','affinity','rolling update']],
['GCP','Cloud Run → Functions → Pub/Sub → Cloud SQL → IAM/VPC → GKE → observabilidade/custo',['Cloud Run','Cloud Functions','Pub/Sub','Cloud SQL','IAM','VPC Connector','GKE']],
['Testes / DevOps','unit/integration/e2e → Testcontainers → failure tests → CI/CD → rollout → SLO/observability',['unit integration e2e','Testcontainers','idempotency test','CI CD','canary','SLI SLO SLA','golden signals']],
['System Design / Senior','requirements → invariants → API/data → async → failure → scale → security → operability → trade-offs',['system design','rate limiter','webhook','notifications','scheduler','chat','architecture tradeoff','postmortem']]
];
function renderMap(){document.getElementById('mapGrid').innerHTML=interviewMap.map(m=>`<div class="map-card"><h3>${esc(m[0])}</h3><p>${esc(m[1])}</p><div class="map-terms">${m[2].map(t=>`<button class="map-term" data-mapterm="${esc(t)}">${esc(t)}</button>`).join('')}</div></div>`).join('')}
'''
anchor2 = "const hotTerms=["
if anchor2 not in s:
    raise SystemExit('hotTerms marker not found')
s = s.replace(anchor2, map_js + '\n' + anchor2, 1)

# Replace control declaration to include map elements.
s = s.replace("const searchEl=document.getElementById('search'),panicBtn=document.getElementById('panicBtn'),alexBtn=document.getElementById('alexBtn'),alexExit=document.getElementById('alexExit');let panic=false,alexMode=false;", "const searchEl=document.getElementById('search'),panicBtn=document.getElementById('panicBtn'),alexBtn=document.getElementById('alexBtn'),alexExit=document.getElementById('alexExit'),mapBtn=document.getElementById('mapBtn'),mapExit=document.getElementById('mapExit');let panic=false,alexMode=false,mapMode=false;")

wire_anchor = "alexBtn.addEventListener('click',()=>setAlex(!alexMode));alexExit.addEventListener('click',()=>setAlex(false));"
wire_new = wire_anchor + "function setMap(v){mapMode=v;document.body.classList.toggle('map-mode',mapMode);mapBtn.classList.toggle('on',mapMode);mapBtn.textContent=mapMode?'✅ Guia normal':'🌳 Mapa';if(mapMode){setAlex(false);panic=false;document.body.classList.remove('panic');panicBtn.classList.remove('on');panicBtn.textContent='🚨 Pânico';window.scrollTo({top:0,behavior:'smooth'})}}mapBtn.addEventListener('click',()=>setMap(!mapMode));mapExit.addEventListener('click',()=>setMap(false));document.getElementById('mapGrid').addEventListener('click',e=>{const b=e.target.closest('[data-mapterm]');if(!b)return;setMap(false);active='Todos';renderChips();searchEl.value=b.dataset.mapterm;filter();searchEl.focus()});"
if wire_anchor not in s:
    raise SystemExit('alex wiring marker not found')
s = s.replace(wire_anchor, wire_new, 1)

# Add M shortcut and map render call.
s = s.replace("else if(e.key.toLowerCase()==='a'&&!typing){setAlex(!alexMode)}else if(e.key.toLowerCase()==='p'&&!typing)", "else if(e.key.toLowerCase()==='a'&&!typing){setAlex(!alexMode)}else if(e.key.toLowerCase()==='m'&&!typing){setMap(!mapMode)}else if(e.key.toLowerCase()==='p'&&!typing)")
s = s.replace("else if(e.key==='Escape'){if(alexMode)setAlex(false);", "else if(e.key==='Escape'){if(alexMode)setAlex(false);if(mapMode)setMap(false);")
s = s.replace('renderChips();filter();\n</script>', "renderMap();renderChips();filter();\n</script>")

# Add visible count hint in hero.
s = s.replace('<p class="small">INTERVIEW COPILOT V4', '<p class="statsbar"><span class="priority">V4:</span> cobertura ampliada para perguntas avançadas e derivadas; use a busca por uma única pista se não lembrar a formulação exata.</p><p class="small">INTERVIEW COPILOT V4', 1)

s = s.replace('<!-- INTERVIEW COPILOT V3 -->', '<!-- INTERVIEW COPILOT V4 -->')
p.write_text(s, encoding='utf-8')
print('Amaris Interview Copilot upgraded to V4')
