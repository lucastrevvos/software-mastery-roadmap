from pathlib import Path

p = Path('docs/amaris-fullstack-interview.html')
s = p.read_text(encoding='utf-8')
if 'INTERVIEW COPILOT V3' in s:
    raise SystemExit(0)

s = s.replace('Amaris Full Stack Senior — Interview Copilot V2', 'Amaris Full Stack Senior — Interview Copilot V3')
s = s.replace('⚡ Amaris — INTERVIEW COPILOT V2', '⚡ Amaris — INTERVIEW COPILOT V3')
s = s.replace('<button id="panicBtn" class="panic-btn" type="button" title="Atalho: P">🚨 Pânico</button>', '<button id="alexBtn" class="alex-btn" type="button" title="Atalho: A">🎯 Alexandre</button><button id="panicBtn" class="panic-btn" type="button" title="Atalho: P">🚨 Pânico</button>')
s = s.replace('<p><strong>Atalhos:</strong> <code>Ctrl+K</code> ou <code>/</code> busca · <code>P</code> modo pânico · <code>Esc</code> limpa · clique numa categoria para filtrar.</p>', '<p><strong>Atalhos:</strong> <code>Ctrl+K</code> ou <code>/</code> busca · <code>A</code> Alexandre Mode · <code>P</code> modo pânico · <code>Esc</code> limpa.</p>')
s = s.replace('INTERVIEW COPILOT V2 · busca por aliases PT/EN · respostas rápidas · aprofundamento · HOT ZONE da vaga · modo pânico.', 'INTERVIEW COPILOT V3 · resposta curta + resposta completa + aprofundamento · 50 perguntas encadeadas no Alexandre Mode · HOT ZONE · busca PT/EN · modo pânico.')

css = r'''
/* INTERVIEW COPILOT V3 */
.alex-btn{border:1px solid #3b5f8e;background:#12233b;color:#dbeaff;border-radius:10px;padding:9px 11px;font-weight:800;cursor:pointer;white-space:nowrap}.alex-btn.on{background:#1d5185;border-color:#79b8ff;color:#fff}.full-block{margin-top:11px;padding-top:10px;border-top:1px solid #25304c}.full-block .label{color:#c7a8ff}.full-answer{margin:0;color:#e0dded;line-height:1.58}.pressure-block .label{color:#84aaff}.alex-panel{display:none;border:1px solid #36567f;background:rgba(12,29,51,.83);border-radius:16px;padding:16px;margin-bottom:18px}.alex-mode .alex-panel{display:block}.alex-mode #grid,.alex-mode .hotzone,.alex-mode .hero{display:none}.alex-mode header h1:after{content:' · ALEXANDRE MODE';color:#86bfff}.alex-head{display:flex;align-items:flex-start;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:12px}.alex-head h2{font-size:17px;margin:0;color:#cfe5ff}.alex-head p{margin:4px 0 0;color:#9eb2ce;font-size:13px}.alex-round{margin:17px 0 8px;font-size:13px;color:#8fc4ff;text-transform:uppercase;letter-spacing:.08em}.alex-card{border:1px solid #2c4667;background:#0e1b2d;border-radius:13px;padding:14px;margin:9px 0}.alex-q{font-weight:800;font-size:15px;margin:0 0 8px;color:#f0f5ff}.alex-a{margin:0;color:#d4dfef;line-height:1.55}.alex-meta{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-top:9px}.alex-search{border:1px solid #3b638d;background:#142b47;color:#cfe7ff;border-radius:999px;padding:5px 9px;font-size:11px;cursor:pointer}.alex-next{font-size:11px;color:#8299b6}.alex-num{display:inline-block;min-width:25px;color:#73b7ff}.panic .full-block,.panic .pressure-block{display:none}.panic .alex-btn{display:none}@media(max-width:640px){.alex-btn,.panic-btn{padding:8px 9px}.full-answer{font-size:14px}}
'''
s = s.replace('</style>', css + '\n</style>', 1)

alex_html = r'''
<section id="alexPanel" class="alex-panel">
  <div class="alex-head"><div><h2>🎯 Alexandre Mode — 50 perguntas encadeadas</h2><p>Leia como uma entrevista real. Cada pergunta empurra naturalmente para a próxima. Clique em “abrir ficha” para voltar ao guia completo daquele conceito.</p></div><button id="alexExit" class="alex-search" type="button">Sair do modo</button></div>
  <div id="alexList"></div>
</section>
'''
s = s.replace('<div id="grid" class="grid"></div>', alex_html + '<div id="grid" class="grid"></div>', 1)

# Insert answer overrides/data immediately before categories declaration.
marker = "const categories=['Todos',...new Set(questions.map(x=>x.category))];"
idx = s.index(marker)
answer_data = r'''
const shortOverrides={
'O que é o Event Loop?':'É o mecanismo que permite ao Node coordenar muitas operações assíncronas sem bloquear a thread que executa JavaScript. O ponto principal é: I/O pode continuar fora da call stack e o callback volta quando estiver pronto.',
'Node.js é single-threaded?':'O JavaScript normalmente roda em uma thread principal, mas o Node não é “inteiro single-thread”. O runtime usa o sistema operacional, libuv, thread pool e pode usar Worker Threads.',
'Como funciona async/await?':'async/await é uma forma legível de trabalhar com Promises. O await pausa aquela função assíncrona, não a thread inteira nem o servidor.',
'Como você organiza uma aplicação NestJS?':'Eu organizo por domínio/feature, mantendo controller fino, regra em services/use cases e infraestrutura atrás de adapters/repositories. Assim o framework não domina a regra de negócio.',
'O que é idempotência?':'É garantir que repetir a mesma operação não gere um segundo efeito de negócio. Em eventos, normalmente uso um identificador único e uma garantia no banco para reconhecer duplicatas.',
'O que é Transactional Outbox?':'É salvar a mudança de negócio e o evento de saída na mesma transação do banco. Um worker publica depois, evitando o dual-write banco + broker.',
'FOR UPDATE SKIP LOCKED: para quê?':'Permite vários workers pegarem lotes diferentes da mesma tabela sem esperar por linhas já travadas. É ótimo para filas/outbox no PostgreSQL, mas não substitui idempotência.',
'RabbitMQ vs Kafka?':'RabbitMQ é muito forte em filas e roteamento de trabalho; Kafka é um log de eventos com retenção e replay. Eu escolheria pela semântica do problema, não por qual parece mais “enterprise”.',
'Cloud Run vs GKE?':'Cloud Run prioriza simplicidade e operação gerenciada; GKE entrega controle e flexibilidade de Kubernetes. Eu começaria pelo requisito operacional e de workload.',
'Monólito modular ou microsserviços?':'Eu não começo escolhendo microsserviços. Se deploy independente, escala ou ownership ainda não justificam a distribuição, prefiro um monólito modular bem separado.',
'useEffect: para que serve?':'Uso effect para sincronizar React com algo externo ao render, como subscription, timer ou API imperativa. Não uso como lugar genérico para qualquer lógica.',
'Context API: quando usar?':'Context é bom para compartilhar dados relativamente estáveis pela árvore. Para estado de alta frequência ou server state, eu avalio soluções mais específicas.',
'Índice: o que é e qual o custo?':'Índice acelera certos acessos ao banco, mas ocupa espaço e torna escritas mais caras. Eu crio índice a partir das queries reais e valido com plano de execução.',
'Unitário vs integração vs E2E?':'Unitário valida lógica pequena e rápida; integração valida componentes reais juntos; E2E valida o fluxo pelo sistema. Eu uso cada nível para um tipo diferente de risco.',
'Liveness vs readiness?':'Liveness diz se o container deve ser reiniciado; readiness diz se ele pode receber tráfego agora. Misturar as duas pode gerar restart loop durante falha temporária de dependência.',
'401 vs 403?':'401 é problema de autenticação; 403 é usuário autenticado sem autorização para aquela ação. São erros diferentes e eu preservo essa semântica no contrato.',
'At-least-once, at-most-once e exactly-once?':'At-least-once aceita duplicação, at-most-once aceita perda e exactly-once depende muito do escopo. Em aplicações distribuídas eu geralmente projeto para at-least-once + idempotência.'
};
const longAnswers={
'O que é o Event Loop?':`Eu explicaria o Event Loop como o coordenador da execução assíncrona do Node. O JavaScript executa na call stack da thread principal; quando fazemos I/O, o runtime delega o trabalho ao sistema operacional ou a mecanismos do libuv e continua atendendo outras tarefas. Quando aquela operação termina, a continuação é colocada nas filas apropriadas e volta a ser executada quando a stack está livre. Na prática, isso torna Node excelente para workload I/O-bound. O cuidado é CPU-bound: se eu fizer um loop pesado, compressão grande ou cálculo intenso na main thread, eu bloqueio o loop e aumento a latência de todas as requisições.`,
'Node.js é single-threaded?':`Eu evitaria responder simplesmente “sim”. O código JavaScript normalmente executa numa thread principal, mas o runtime Node usa muito mais do que uma thread: há I/O tratado pelo sistema operacional, thread pool do libuv para certas operações e Worker Threads quando precisamos paralelizar CPU. Então o modelo mental correto é: a execução comum do JavaScript é single-threaded, mas o processo e o runtime não são. Isso explica por que milhares de conexões I/O podem coexistir e também por que uma tarefa pesada de CPU pode prejudicar todo o serviço.`,
'Como funciona async/await?':`async/await é uma camada de sintaxe sobre Promises. Quando uma função chega a um await, ela devolve o controle ao runtime e sua continuação é retomada quando a Promise resolve; isso não bloqueia a thread como um sleep síncrono faria. Eu também tomo cuidado para não serializar operações independentes por acidente: se três chamadas podem rodar juntas, posso iniciar as Promises e usar Promise.all. Em entrevista eu destacaria esse trade-off entre legibilidade, concorrência e tratamento de erro.`,
'Como você organiza uma aplicação NestJS?':`Eu prefiro organizar NestJS por domínio ou feature. O controller fica fino, responsável pelo protocolo HTTP: entrada, status, headers e delegação. A regra de aplicação fica em services/use cases; acesso a banco, broker ou APIs externas fica atrás de adapters/repositories ou providers específicos. Uso DTOs e validação na borda, guards para autorização, filters para erros e interceptors para cross-cutting concerns. A ideia é aproveitar DI e módulos do Nest sem transformar a regra de negócio em código dependente do framework.`,
'Provider e Dependency Injection?':`No Nest, providers são objetos gerenciados pelo container de injeção. Eu uso DI para que uma classe declare o que precisa sem instanciar diretamente os detalhes. Por exemplo, um caso de uso pode depender de uma interface/token de repositório e receber a implementação PostgreSQL em produção e uma fake em teste. Isso reduz acoplamento, melhora testabilidade e é uma aplicação prática de Dependency Inversion. Eu evito criar abstrações só por estética; uso quando existe uma fronteira ou variação real.`,
'REST: o que caracteriza uma boa API?':`Para mim uma boa API começa pelo contrato. Recursos e operações precisam ser claros, os métodos e status HTTP devem ter semântica previsível e as entradas precisam ser validadas na borda. Depois penso em autenticação/autorização, erros padronizados, paginação, idempotência onde existe risco de repetição, versionamento e documentação OpenAPI. Em produção acrescento observabilidade, rate limit, timeout e compatibilidade com consumidores. O objetivo não é só “funcionar”, é ser previsível e evoluir sem quebrar quem depende dela.`,
'O que é idempotência?':`Idempotência é garantir que a repetição da mesma intenção não produza efeitos adicionais. Isso é essencial porque em sistemas distribuídos timeout não significa necessariamente que a operação falhou e brokers podem redeliver mensagens. Um padrão comum é cada comando/evento ter um identificador único e o consumidor persistir esse ID, ou usar uma constraint UNIQUE ligada ao efeito de negócio. Assim, se a mensagem chegar novamente, reconhecemos o processamento anterior e não cobramos duas vezes, por exemplo. Eu trato idempotência como regra de negócio e persistência, não apenas como configuração do broker.`,
'O que é Transactional Outbox?':`Transactional Outbox resolve o problema de dual-write. Se eu salvar o pedido no banco e depois publicar no broker em duas operações independentes, posso confirmar uma e perder a outra. Com outbox eu salvo, na mesma transação local, tanto a mudança do domínio quanto um registro do evento a publicar. Depois um worker lê a outbox e envia ao broker. Ainda pode haver publicação duplicada se houver crash entre publish e marcação, então produtor e consumidor precisam ser idempotentes. O ganho é mover a atomicidade para um único recurso transacional: o banco.`,
'FOR UPDATE SKIP LOCKED: para quê?':`Eu uso FOR UPDATE para travar as linhas escolhidas dentro da transação. O SKIP LOCKED faz outro worker ignorar aquelas linhas em vez de esperar pelo lock. Isso permite que várias instâncias consumam uma tabela de trabalho/outbox em paralelo, cada uma pegando um lote diferente. É muito útil no PostgreSQL para implementar concorrência de workers sem um coordenador central. Mas eu sempre ressalto que o lock só protege a disputa enquanto a transação existe; se o processo publicar e cair antes de registrar sucesso, pode haver replay, então idempotência continua necessária.`,
'RabbitMQ vs Kafka?':`Eu começaria pela semântica. RabbitMQ encaixa muito bem quando penso em work queue, roteamento, ACK/NACK, prioridades e distribuição de tarefas entre consumidores. Kafka é um log distribuído: os eventos permanecem retidos, podem ser reprocessados e partitions dão paralelismo e ordenação local. Então, para jobs e comandos assíncronos, RabbitMQ costuma ser natural; para streaming, integração por eventos e replay, Kafka pode ser melhor. Depois eu compararia throughput, ordering, retenção, operação, custo e conhecimento do time.`,
'GCP Pub/Sub: modelo mental?':`No Pub/Sub eu penso em publishers escrevendo num topic e subscriptions representando fluxos independentes de consumo. É interessante porque o GCP gerencia escala e infraestrutura, então reduz bastante a operação de broker. Mas isso não remove os problemas da aplicação: ainda preciso pensar em ACK, redelivery, retry, DLQ, ordering quando necessário e consumidor idempotente. Eu usaria especialmente quando a arquitetura já está no GCP e quero integração assíncrona gerenciada sem administrar Kafka ou RabbitMQ.`,
'Monólito modular ou microsserviços?':`Eu começaria pelo monólito modular se não houver uma razão objetiva para distribuir. Microsserviços dão deploy e escala independentes, ownership e isolamento de falha, mas também introduzem rede, observabilidade distribuída, consistência eventual, contratos, retry, mensageria e operação. Então eu olho limites de domínio, tamanho e autonomia das equipes, padrões de escala e necessidade de deploy independente. Se essas pressões não existem, um monólito modular bem desenhado costuma ser mais barato e confiável.`,
'Cloud Run vs GKE?':`Cloud Run é minha escolha natural quando tenho containers HTTP ou event-driven e quero autoscaling e pouca operação. GKE faz sentido quando preciso realmente do modelo Kubernetes: topologias mais complexas, controle de scheduling, sidecars, políticas avançadas, múltiplos workloads e ecossistema K8s. Eu não escolheria GKE só porque é “mais poderoso”; esse poder tem custo operacional. Começo pelo serviço mais simples que atende os requisitos e só aceito a complexidade adicional quando existe benefício claro.`,
'Pod, Deployment e Service?':`Eu penso em Pod como a menor unidade executável do Kubernetes, normalmente contendo um container principal e eventualmente sidecars. Deployment expressa o estado desejado para uma aplicação stateless: número de réplicas, estratégia de rollout e template dos pods. Service dá uma identidade de rede estável sobre pods que são efêmeros e podem mudar de IP. Em operação eu ainda conecto isso a readiness/liveness, requests/limits, autoscaling e observabilidade.`,
'useEffect: para que serve?':`Eu uso useEffect quando preciso sincronizar o componente com algo externo ao processo puro de renderização: subscription, timer, event listener, API imperativa ou algum efeito similar. Não uso effect para derivar dados que podem ser calculados diretamente durante o render. Também trato dependências como parte da semântica, não como algo para “enganar o lint”: se uma dependência causa loop, procuro a causa — referência instável, estado mal modelado ou lógica no lugar errado. E sempre penso em cleanup quando existe recurso externo.`,
'Context API: quando usar?':`Context é um mecanismo de propagação de valores pela árvore, não uma solução universal de state management. Eu gosto para autenticação, tema, configuração e alguns estados compartilhados relativamente estáveis. Se o valor muda o tempo todo, muitos consumidores podem renderizar novamente; aí separo contexts ou uso uma store adequada. Também separo client state de server state: dados remotos têm cache, invalidation, retry e stale data, problemas diferentes do estado da UI.`,
'Índice: o que é e qual o custo?':`Índice é uma estrutura adicional que permite localizar dados mais eficientemente sem varrer a tabela inteira em muitos casos. O custo é espaço, manutenção e escrita mais cara, porque INSERT/UPDATE/DELETE também precisam atualizar os índices. Eu não crio índice “em toda coluna”: parto das queries reais, filtros, joins, ordenação e seletividade e valido com EXPLAIN/EXPLAIN ANALYZE. Em índice composto, a ordem das colunas precisa refletir o padrão de acesso.`,
'Unitário vs integração vs E2E?':`Eu escolho o nível do teste pelo risco que quero detectar. Teste unitário é rápido e ótimo para regras de negócio isoladas; integração valida banco, broker, adapters ou framework trabalhando de verdade; E2E atravessa a aplicação como um consumidor e valida contratos e fluxos críticos. Não tento resolver tudo com E2E porque fica caro e frágil, e também não mocko tudo porque posso esconder problemas reais. Em backend distribuído eu gosto especialmente de integração com dependências reais descartáveis, por exemplo via Testcontainers.`,
'Liveness vs readiness?':`Readiness responde se o pod pode receber tráfego agora; liveness responde se o processo está tão comprometido que deve ser reiniciado. Essa diferença é importante: se eu colocar a saúde de um banco externo na liveness, uma indisponibilidade temporária do banco pode fazer todos os pods reiniciarem e piorar o incidente. Readiness pode tirar a instância do tráfego enquanto ela não está pronta. Eu também considero startup probe para aplicações que precisam de mais tempo para inicializar.`,
'CI CD pipeline GitLab build deploy':`Eu espero que um pipeline faça build reproduzível, lint/typecheck, testes, análise de segurança/qualidade, gere um artefato imutável e promova esse mesmo artefato entre ambientes. Deploy deve ser observável e reversível, com estratégia de rollback ou roll-forward e migrations compatíveis com versões coexistindo. Eu também separo deploy de release quando feature flags fazem sentido.`,
'Como começar qualquer System Design?':`Eu começo fechando requisitos antes de desenhar caixas: volume, padrões de leitura/escrita, latência aceitável, disponibilidade, consistência e principais invariantes. Em seguida desenho o caminho mais simples de ponta a ponta — cliente, API, domínio, banco e integrações. Só depois adiciono cache, mensageria, particionamento, replicas, autoscaling e mecanismos de resiliência conforme os gargalos. Durante toda a discussão eu explico falhas possíveis, observabilidade, segurança e trade-offs. A entrevista de system design é menos sobre achar “a arquitetura certa” e mais sobre mostrar raciocínio e decisões conscientes.`,
'Desenhe pedidos + pagamentos + notificações resilientes.':`Eu começaria com uma API de pedidos que valida a requisição e persiste Order no banco. Na mesma transação, gravaria um evento na outbox. Um publisher envia esse evento ao broker e o serviço de pagamento consome de forma idempotente. Depois do pagamento, outro evento atualiza o pedido e alimenta notificações. Cada integração externa teria timeout, retry limitado, circuit breaker quando fizer sentido e DLQ para mensagens persistentes. Eu propagaria trace/correlation ID e monitoraria latência, erros e backlog. Na discussão eu destacaria especificamente as janelas de falha: commit sem publish, processamento sem ACK e duplicação por retry.`
};
const categoryBridge={
'JavaScript':'Eu conectaria isso ao impacto no event loop, concorrência e comportamento em runtime.',
'TypeScript':'Eu também lembraria que a tipagem é compile-time e entradas externas continuam exigindo validação em runtime.',
'Node.js':'Na prática eu observaria event-loop lag, uso de CPU/memória e comportamento sob concorrência.',
'NestJS':'Eu manteria controller fino e usaria DI para separar regra de negócio de infraestrutura.',
'API':'Eu fecharia com contrato, validação, segurança, idempotência e observabilidade.',
'React':'Eu separaria correção de performance e só otimizaria depois de medir renders e latência.',
'Distribuídos':'Eu parto do princípio de que rede falha e operações podem atrasar, duplicar ou ficar parcialmente concluídas.',
'Mensageria':'Eu sempre fecho semântica de entrega, ACK, retry, DLQ, ordering e idempotência.',
'Banco':'Eu validaria a decisão com o plano de execução, garantias transacionais e padrão real de acesso.',
'Arquitetura':'Eu explicaria também quando não usaria o padrão e qual complexidade ele adiciona.',
'Testes':'Eu escolheria o nível do teste pelo tipo de risco que quero detectar.',
'Kubernetes':'Eu conectaria a resposta a rollout, probes, recursos, autoscaling e observabilidade.',
'GCP':'Eu escolheria o serviço pelo requisito e pelo custo operacional, não pelo número de recursos.',
'DevOps':'Eu priorizaria automação reproduzível, artefato imutável, observabilidade e reversibilidade.',
'Observabilidade':'Eu tentaria transformar a discussão em sinais mensuráveis e alertas acionáveis.',
'Segurança':'Eu aplicaria least privilege e assumiria que toda entrada externa é não confiável.'
};
function fullAnswer(x){return longAnswers[x.q] || `${x.quick} ${x.deep}${categoryBridge[x.category]?' '+categoryBridge[x.category]:''}${x.safe?' Na prática, eu conectaria com: '+x.safe:''}`}
'''
s = s[:idx] + answer_data + '\n' + s[idx:]

# Replace card renderer with three answer levels.
a = s.index('function card(x,i){return `')
b = s.index('\nconst grid=', a)
new_card = r'''function card(x,i){const short=shortOverrides[x.q]||x.quick,full=fullAnswer(x);return `<article class="card" data-i="${i}" data-cat="${esc(x.category)}" data-search="${esc((x.category+' '+x.q+' '+short+' '+full+' '+x.deep+' '+x.tags+' '+x.safe).toLowerCase())}"><div class="catline"><span class="catbadge">${esc(x.category)}</span><span class="score"></span></div><h2>${esc(x.q)}</h2><div class="meta">${x.tags.split(' ').slice(0,7).map(t=>`<span class="tag">${esc(t)}</span>`).join('')}</div><div class="quick-block"><div class="label">⚡ Resposta curta · 5–10s</div><p class="answer">${esc(short)}</p></div><div class="full-block"><div class="label">🎯 Resposta completa · 20–40s</div><p class="full-answer">${esc(full)}</p></div><div class="pressure-block"><div class="label">🧠 Se ele aprofundar</div><p class="deep">${esc(x.deep)}</p></div>${x.safe?`<div class="safe-block"><div class="label">💼 Como puxar para prática</div><p class="safe">${esc(x.safe)}</p></div>`:''}</article>`}'''
s = s[:a] + new_card + s[b:]

# Insert Alexandre 50-question dataset before existing hotTerms.
hot_idx = s.index("const hotTerms=")
alex_js = r'''
const alexandreRounds=[
{title:'Round 1 — JavaScript / Node',items:[
['Node consegue atender milhares de conexões sendo single-thread?','O JavaScript executa na main thread, mas I/O é coordenado de forma assíncrona pelo runtime e SO. O segredo é não bloquear o event loop.','event loop'],
['Então me explique o Event Loop.','A call stack executa JS; operações assíncronas terminam fora dela e suas continuações retornam pelas filas quando a stack está disponível.','event loop'],
['O que acontece se você fizer CPU pesada nessa thread?','Eu bloqueio o loop e aumento a latência de todas as requisições. Para CPU-bound avalio Worker Threads, fila ou serviço separado.','worker threads'],
['Worker Threads ou fila: como escolhe?','Worker é paralelismo dentro do processo; fila desacopla execução, dá retry e distribuição entre processos. Escolho pelo ciclo de vida e resiliência do trabalho.','worker threads'],
['Como você detectaria que o event loop está sofrendo?','Métricas de event-loop lag, CPU, P95/P99, profiling e traces ajudam a separar bloqueio local de dependência externa lenta.','performance'] ]},
{title:'Round 2 — NestJS / API',items:[
['Como você estruturaria uma API NestJS?','Módulos por domínio, controller fino, service/use case para comportamento e adapters para infraestrutura; DTO e validação na borda.','NestJS'],
['Por que usar Dependency Injection?','Para reduzir acoplamento e permitir trocar detalhes como repositórios/providers sem a regra criar essas dependências diretamente.','dependency injection'],
['Guard, Pipe, Interceptor e Filter: diferença?','Guard decide acesso; Pipe valida/transforma entrada; Interceptor envolve execução; Filter traduz exceções.','guard interceptor pipe filter'],
['Como você desenha uma boa API REST?','Começo por recursos e contrato, depois semântica HTTP, validação, auth, erros, idempotência, paginação, versionamento e observabilidade.','API REST'],
['POST pode ser idempotente?','Não por definição, mas posso construir idempotência com Idempotency-Key e persistência do resultado/efeito ligado à chave.','POST idempotency'] ]},
{title:'Round 3 — Sistemas distribuídos',items:[
['O que muda quando seu sistema vira distribuído?','Eu deixo de poder assumir rede confiável ou execução única. Timeout, falha parcial, duplicata, concorrência e observabilidade entram no desenho.','distributed'],
['At-least-once é ruim?','Não. É uma garantia útil desde que o consumidor tolere redelivery. Eu normalmente combino at-least-once com idempotência.','at least once'],
['Como implementa idempotência?','Identificador único + garantia persistente no ponto do efeito, como constraint UNIQUE ou registro inbox/processado.','idempotência'],
['Timeout aconteceu. Você faz retry?','Só se a falha puder ser transitória e a operação for segura/idempotente. Uso limite, backoff, jitter e respeito o deadline total.','retry'],
['Circuit breaker resolve tudo?','Não; ele evita gastar recurso numa dependência claramente ruim. Ainda preciso timeout, bulkhead, retry criterioso e fallback quando possível.','circuit breaker'] ]},
{title:'Round 4 — Mensageria',items:[
['RabbitMQ, Kafka ou Pub/Sub?','Rabbit para work queue/roteamento; Kafka para log, retenção e replay; Pub/Sub quando quero mensageria gerenciada integrada ao GCP.','rabbitmq kafka pubsub'],
['O consumidor processou e caiu antes do ACK. O que acontece?','A mensagem pode voltar. Por isso o efeito precisa ser idempotente.','ack duplicate'],
['E se for uma mensagem que nunca consegue processar?','Retry limitado e depois DLQ, com métrica, alerta, investigação e estratégia de replay.','DLQ'],
['Como manter ordem no Kafka?','A garantia é dentro da partition. Eventos que exigem ordem devem compartilhar uma chave que os leve à mesma partition.','kafka ordering'],
['O que é rebalance?','Redistribuição de partitions entre consumers do mesmo group; pode interromper/reorganizar consumo e precisa ser considerado em processamento longo.','kafka rebalance'] ]},
{title:'Round 5 — Banco / Concorrência',items:[
['Duas requisições compram o último item ao mesmo tempo.','A invariável precisa estar protegida no banco com update condicional, transação, lock ou versão; SELECT e UPDATE soltos criam race.','race condition'],
['Optimistic ou pessimistic locking?','Optimistic detecta conflito e funciona bem quando colisão é rara; pessimistic serializa acesso quando conflito é esperado.','optimistic pessimistic'],
['FOR UPDATE SKIP LOCKED serve para quê?','Permite múltiplos workers pegarem linhas diferentes sem esperar pelas já travadas; excelente para work queue/outbox em Postgres.','FOR UPDATE SKIP LOCKED'],
['Como você decide criar um índice?','Parto da query real e do plano: filtros, joins, sort, seletividade e cardinalidade. Índice também custa escrita e espaço.','index'],
['EXPLAIN ANALYZE te mostra o quê?','O plano realmente executado com tempos e linhas reais, permitindo comparar estimativas e achar scans/joins caros.','EXPLAIN ANALYZE'] ]},
{title:'Round 6 — React',items:[
['Quando um componente React renderiza?','A função do componente produz a próxima descrição da UI; React reconcilia e só depois aplica no DOM o que realmente mudou.','React render'],
['Para que serve useEffect?','Sincronização com sistema externo ao render, não um depósito genérico de lógica.','useEffect'],
['O array de dependências dá loop. Você remove a dependência?','Não como gambiarra. Eu procuro referência instável, estado derivado ou responsabilidade mal colocada e corrijo a causa.','useEffect dependencies'],
['Context API substitui Redux/Zustand?','Não. Context propaga valor; frequência de updates, tamanho do estado e tooling podem justificar uma store.','Context API'],
['Como investiga performance no React?','Primeiro meço com profiler e rede. Depois reduzo estado compartilhado, renders e trabalho caro; memoização vem depois da evidência.','React performance'] ]},
{title:'Round 7 — Arquitetura',items:[
['SOLID serve para quê na prática?','Para aumentar coesão e reduzir acoplamento/custo de mudança. Não uso como desculpa para criar abstrações em todo lugar.','SOLID'],
['Clean ou Hexagonal: o que realmente importa?','Manter regra de negócio independente dos detalhes e dependências apontando para contratos do núcleo.','clean hexagonal'],
['Quando você escolheria microsserviços?','Quando fronteiras, deploy independente, ownership, escala ou isolamento justificam o custo distribuído.','microservices'],
['O que é Transactional Outbox?','Persistir estado + evento na mesma transação local e publicar depois, evitando dual-write inconsistente.','outbox'],
['Saga ou 2PC?','Saga aceita transações locais e compensações; 2PC coordena atomicidade e pode reduzir disponibilidade/acoplar participantes.','saga 2pc'] ]},
{title:'Round 8 — Docker / Kubernetes / GCP',items:[
['Imagem e container?','Imagem é o artefato/template imutável; container é uma instância em execução daquela imagem.','docker image container'],
['Readiness e liveness?','Readiness controla tráfego; liveness decide reinício. Misturar dependência externa na liveness pode criar restart storm.','readiness liveness'],
['Requests e limits?','Requests ajudam scheduling/capacidade; limits impõem teto e podem causar throttling/OOM se mal definidos.','requests limits'],
['Cloud Run ou GKE?','Cloud Run para simplicidade e workload containerizado gerenciado; GKE quando realmente preciso do modelo e controle Kubernetes.','Cloud Run GKE'],
['Escalar pods sempre resolve?','Não. Posso apenas deslocar o gargalo para DB, broker ou API externa. Autoscaling precisa observar capacidade downstream.','HPA autoscaling'] ]},
{title:'Round 9 — Testes / DevOps / Segurança',items:[
['O que você testaria num consumer de fila?','Sucesso, duplicata, redelivery, poison message, idempotência e falhas antes/depois do efeito.','consumer test'],
['Coverage 100% significa bons testes?','Não. Coverage mede execução de linha, não qualidade da assertion nem cenários relevantes.','coverage'],
['Como faria CI/CD?','Build reproduzível, lint/typecheck, testes, scans, artefato imutável e promoção observável/reversível.','CI CD'],
['JWT é criptografado?','Não necessariamente; assinatura garante integridade/autenticidade, e claims normalmente podem ser lidas.','JWT'],
['OAuth2 e OIDC?','OAuth2 é autorização; OIDC adiciona identidade/autenticação sobre OAuth2.','OAuth2 OIDC'] ]},
{title:'Round 10 — System Design / Senioridade',items:[
['Desenhe pedidos, pagamentos e notificações.','API + banco + outbox + broker + consumers idempotentes; depois resiliência, tracing, DLQ e escala.','orders payments system design'],
['Banco confirmou e publish falhou.','Outbox evita essa janela porque estado e evento são gravados atomicamente no mesmo banco.','outbox'],
['Publish ocorreu e worker caiu antes de marcar sucesso.','Posso republicar; por isso o consumidor precisa tolerar duplicata.','idempotência'],
['Como decide arquitetura sob pressão?','Começo por invariantes, requisitos e riscos; comparo alternativas e explicito trade-offs antes de escolher tecnologia.','architecture tradeoff'],
['E se eu te perguntar algo que você não sabe?','Eu separo o que sei da incerteza, raciocino por fundamentos e explico como validaria. Prefiro isso a inventar experiência.','não sei'] ]}
];
function renderAlexandre(){const root=document.getElementById('alexList');let n=0;root.innerHTML=alexandreRounds.map(r=>`<div class="alex-round">${esc(r.title)}</div>${r.items.map((it,j)=>{n++;return `<div class="alex-card"><p class="alex-q"><span class="alex-num">${n}.</span>${esc(it[0])}</p><p class="alex-a">${esc(it[1])}</p><div class="alex-meta"><button class="alex-search" data-term="${esc(it[2])}">abrir ficha: ${esc(it[2])}</button><span class="alex-next">${j<r.items.length-1?'↳ próxima pergunta aprofunda este tema':'✓ fim do round'}</span></div></div>`}).join('')}`).join('')}
'''
s = s[:hot_idx] + alex_js + '\n' + s[hot_idx:]

# Upgrade event initialization to include Alexandre mode.
old = "const searchEl=document.getElementById('search'),panicBtn=document.getElementById('panicBtn');let panic=false;"
new = "const searchEl=document.getElementById('search'),panicBtn=document.getElementById('panicBtn'),alexBtn=document.getElementById('alexBtn'),alexExit=document.getElementById('alexExit');let panic=false,alexMode=false;"
s = s.replace(old, new, 1)
old_line = "searchEl.addEventListener('input',filter);panicBtn.addEventListener('click',()=>{panic=!panic;document.body.classList.toggle('panic',panic);panicBtn.classList.toggle('on',panic);panicBtn.textContent=panic?'✅ Normal':'🚨 Pânico';searchEl.focus()});"
new_line = "searchEl.addEventListener('input',filter);panicBtn.addEventListener('click',()=>{panic=!panic;document.body.classList.toggle('panic',panic);panicBtn.classList.toggle('on',panic);panicBtn.textContent=panic?'✅ Normal':'🚨 Pânico';searchEl.focus()});function setAlex(v){alexMode=v;document.body.classList.toggle('alex-mode',alexMode);alexBtn.classList.toggle('on',alexMode);alexBtn.textContent=alexMode?'✅ Guia normal':'🎯 Alexandre';if(alexMode){panic=false;document.body.classList.remove('panic');panicBtn.classList.remove('on');panicBtn.textContent='🚨 Pânico';window.scrollTo({top:0,behavior:'smooth'})}}alexBtn.addEventListener('click',()=>setAlex(!alexMode));alexExit.addEventListener('click',()=>setAlex(false));document.getElementById('alexList').addEventListener('click',e=>{const b=e.target.closest('[data-term]');if(!b)return;setAlex(false);active='Todos';renderChips();searchEl.value=b.dataset.term;filter();searchEl.focus()});renderAlexandre();"
s = s.replace(old_line, new_line, 1)
# add A shortcut before P branch
s = s.replace("}else if(e.key.toLowerCase()==='p'&&!typing){", "}else if(e.key.toLowerCase()==='a'&&!typing){setAlex(!alexMode)}else if(e.key.toLowerCase()==='p'&&!typing){", 1)
# Escape exits Alexandre mode first.
s = s.replace("}else if(e.key==='Escape'){searchEl.value='';searchEl.blur();active='Todos';renderChips();filter()}});", "}else if(e.key==='Escape'){if(alexMode)setAlex(false);searchEl.value='';searchEl.blur();active='Todos';renderChips();filter()}});", 1)

# Marker for idempotent upgrade.
s = s.replace('</body></html>', '<!-- INTERVIEW COPILOT V3 -->\n</body></html>', 1)
p.write_text(s, encoding='utf-8')
print('Amaris Interview Copilot V3 generated')
