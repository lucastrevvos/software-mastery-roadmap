from pathlib import Path

p = Path('docs/amaris-fullstack-interview.html')
s = p.read_text(encoding='utf-8')
if 'FUNDAMENTOS PLENO V4.1' in s:
    raise SystemExit(0)

extras = r'''
,Q('Fundamentos OO','Quais são os pilares da orientação a objetos?','Encapsulamento, abstração, herança e polimorfismo são os quatro pilares clássicos.','Na prática eu destacaria que composição e boas fronteiras costumam ser mais importantes do que usar herança em todo lugar.','oop oo orientação objetos pilares encapsulamento abstração herança polimorfismo')
,Q('Fundamentos OO','Classe vs objeto?','Classe define estrutura e comportamento; objeto é uma instância concreta criada a partir desse modelo.','Em JavaScript classes são uma sintaxe sobre o modelo prototípico, então o conceito de OO continua válido, mas a implementação interna é diferente de linguagens class-based tradicionais.','classe objeto instance class oop javascript typescript')
,Q('Fundamentos OO','O que é encapsulamento?','É esconder detalhes internos e expor uma interface controlada para preservar invariantes.','Encapsulamento não é só colocar private; é impedir que qualquer parte do sistema manipule estado interno de forma inválida.','encapsulation encapsulamento private invariants oop')
,Q('Fundamentos OO','O que é abstração?','É representar apenas os aspectos relevantes de algo e esconder detalhes desnecessários para quem usa.','Uma boa abstração reduz carga mental e acoplamento; uma abstração ruim só adiciona camadas sem simplificar o problema.','abstraction abstração interface oop design')
,Q('Fundamentos OO','O que é herança?','É uma relação em que um tipo deriva comportamento/estrutura de outro.','Uso com cautela porque cria acoplamento forte entre hierarquias. Quando a relação é mais “tem um” do que “é um”, composição costuma ser melhor.','inheritance herança is-a oop')
,Q('Fundamentos OO','O que é polimorfismo?','É tratar diferentes implementações por uma interface/contrato comum.','Exemplo: PaymentGateway pode ter StripeGateway e MercadoPagoGateway; o caso de uso depende do contrato e não da implementação concreta.','polymorphism polimorfismo interface strategy adapter oop')
,Q('Fundamentos OO','Overload vs override?','Overload oferece assinaturas diferentes para uma operação; override redefine comportamento herdado.','TypeScript tem overloads no sistema de tipos, mas uma única implementação em runtime; override depende da herança/prototype chain.','overload override sobrecarga sobrescrita typescript oop')
,Q('Fundamentos OO','Interface vs classe abstrata?','Interface define contrato; classe abstrata pode definir contrato e compartilhar implementação/estado.','Prefiro interface/port quando quero desacoplar implementações; classe abstrata faz sentido quando existe comportamento base realmente compartilhado.','interface abstract class classe abstrata oop typescript')
,Q('Fundamentos OO','Composição vs herança?','Composição monta comportamento usando objetos menores; herança cria hierarquia entre tipos.','Composição costuma dar mais flexibilidade e menos acoplamento. Eu uso herança quando a relação “é um” é estável e realmente faz sentido.','composition inheritance composição herança favor composition')
,Q('Fundamentos OO','Associação, agregação e composição?','São formas de relacionamento entre objetos com diferentes níveis de dependência de ciclo de vida.','Composição é a relação mais forte: a parte pertence ao todo; agregação é mais fraca e a parte pode existir separadamente.','association aggregation composition oop uml')
,Q('Fundamentos OO','O que é alta coesão?','É quando uma classe/módulo concentra responsabilidades relacionadas entre si.','Alta coesão facilita entendimento, teste e mudança porque o componente tem um propósito claro.','coesão cohesion module class design oop')
,Q('Fundamentos OO','O que é baixo acoplamento?','É reduzir dependências desnecessárias entre componentes.','Baixo acoplamento não significa zero dependência; significa dependências explícitas, estáveis e orientadas a contratos adequados.','coupling acoplamento dependency design oop')
,Q('Fundamentos OO','O que significa “favor composition over inheritance”?','Prefira montar comportamento com componentes colaborando em vez de criar hierarquias profundas.','Isso normalmente reduz fragilidade de subclasses e facilita trocar comportamento em runtime/testes.','composition over inheritance oop design')
,Q('Fundamentos OO','O que é Liskov na prática?','Uma implementação derivada deve poder substituir o contrato base sem quebrar as expectativas do cliente.','Se uma subclasse precisa lançar erro para uma operação válida no tipo base, provavelmente a hierarquia está errada.','LSP liskov substitution solid oop')
,Q('Fundamentos OO','Interface Segregation na prática?','Clientes não deveriam depender de métodos que não usam.','Prefiro contratos menores e coesos a uma interface gigante implementada parcialmente.','ISP interface segregation solid oop')
,Q('Fundamentos OO','Dependency Inversion vs Dependency Injection?','DIP é princípio arquitetural: depender de abstrações. DI é uma técnica para fornecer dependências externamente.','Posso fazer DI sem seguir DIP e posso seguir DIP sem usar um container de DI.','DIP dependency inversion dependency injection DI SOLID')
,Q('Fundamentos OO','O que é imutabilidade?','É evitar alterar um valor depois de criado; mudanças produzem novos valores/estados.','Ajuda a reduzir efeitos colaterais e facilitar raciocínio, mas copiar estruturas grandes também tem custo.','immutability immutable oop functional state')
,Q('Fundamentos OO','Entidade vs Value Object?','Entidade é definida por identidade ao longo do tempo; Value Object é definido pelos seus valores.','Money(10, BRL) é um exemplo clássico de Value Object; um Customer geralmente é entidade.','entity value object ddd oop')
,Q('Fundamentos OO','O que é Law of Demeter?','Um objeto deve conhecer o mínimo necessário sobre a estrutura interna de outros objetos.','Evita cadeias do tipo a.getB().getC().doX() que espalham conhecimento estrutural e aumentam acoplamento.','law demeter least knowledge coupling oop')
,Q('Fundamentos OO','private no TypeScript é segurança de runtime?','Nem sempre. Modificadores tradicionais são principalmente verificação de compilação; #private tem semântica privada nativa do JavaScript.','TypeScript não deve ser tratado como boundary de segurança.','typescript private #private runtime oop')
,Q('Fundamentos CS','Stack vs heap?','Stack normalmente guarda frames de execução; heap armazena objetos/dados com ciclo de vida dinâmico.','No JavaScript esses detalhes são gerenciados pelo runtime, mas o modelo ajuda a entender call stack, closures, heap e GC.','stack heap memory call stack gc fundamentals')
,Q('Fundamentos CS','JavaScript passa objeto por referência?','JavaScript passa argumentos por valor; para objetos, o valor é uma referência ao objeto.','Por isso reatribuir o parâmetro não troca a variável externa, mas mutar o objeto referenciado pode ser observado fora.','pass by value reference javascript object fundamentals')
,Q('Fundamentos CS','O que é Big O?','É uma forma de descrever como custo de tempo ou memória cresce com o tamanho da entrada.','Exemplo: acesso por índice em array é tipicamente O(1), busca linear O(n), busca binária O(log n) em dados ordenados.','big o complexity complexidade O1 On Ologn algorithms')
,Q('Fundamentos CS','Array vs lista encadeada?','Array favorece acesso por índice e localidade; lista ligada favorece inserções/remoções quando já tenho o nó.','Na prática em JavaScript arrays são muito mais comuns; linked list aparece mais em fundamentos/estruturas específicas.','array linked list lista encadeada data structure')
,Q('Fundamentos CS','Stack vs Queue?','Stack é LIFO; Queue é FIFO.','Call stack é exemplo de stack; processamento de trabalhos em ordem de chegada é um exemplo conceitual de queue.','stack queue lifo fifo data structure')
,Q('Fundamentos CS','Hash map: modelo mental?','Mapeia uma chave para uma posição/bucket usando hash para acesso médio muito rápido.','Colisões precisam ser tratadas; complexidade média costuma ser O(1), mas depende da implementação/distribuição.','hash map hashmap dictionary map complexity')
,Q('Fundamentos CS','Set vs Map?','Set guarda valores únicos; Map guarda pares chave-valor.','Escolho pela semântica: membership/deduplicação → Set; associação chave→valor → Map.','set map data structures javascript')
,Q('Fundamentos CS','Busca linear vs binária?','Linear percorre elementos O(n); binária reduz espaço de busca pela metade O(log n), mas exige ordenação/acesso adequado.','Não uso binary search se o custo de manter dados ordenados não fizer sentido.','linear search binary search big o')
,Q('Fundamentos CS','BFS vs DFS?','BFS explora por níveis usando fila; DFS aprofunda caminhos usando stack/recursão.','BFS é útil para menor número de arestas em grafo não ponderado; DFS é ótimo para exploração/topologia/detecção de ciclos conforme o problema.','bfs dfs graph tree queue stack algorithms')
,Q('Fundamentos Web','GET vs POST?','GET lê/representa recurso e deve ser safe; POST envia uma nova ação/representação e não é idempotente por definição.','Ainda posso projetar um POST idempotente com chave de idempotência quando o negócio exige.','GET POST HTTP safe idempotent REST')
,Q('Fundamentos Web','PUT vs PATCH?','PUT normalmente substitui a representação do recurso; PATCH aplica alteração parcial.','A semântica precisa ser consistente com o contrato e validação da API.','PUT PATCH HTTP REST update')
,Q('Fundamentos Web','Métodos safe e idempotent?','Safe não deveria alterar estado observável do servidor; idempotent pode ser repetido sem mudar o efeito após a primeira aplicação.','GET é safe/idempotent; PUT/DELETE são idempotentes por semântica; POST não necessariamente.','safe idempotent HTTP methods REST')
,Q('Fundamentos Web','Principais status HTTP que você espera saber?','200 sucesso, 201 criação, 204 sem corpo, 400 entrada inválida, 401 autenticação, 403 autorização, 404 não encontrado, 409 conflito, 422 semântica inválida, 429 limite, 5xx servidor.','Mais importante que decorar todos é preservar uma semântica previsível no contrato.','http status codes 200 201 204 400 401 403 404 409 422 429 500')
,Q('Fundamentos Web','Header vs body?','Headers carregam metadados/protocolo; body carrega a representação/payload principal.','Auth, content type, cache e tracing normalmente aparecem em headers; dados de domínio geralmente no body.','http header body content type authorization')
,Q('Fundamentos Web','Cookie vs localStorage?','Cookie pode ser enviado automaticamente ao servidor e ter HttpOnly/SameSite/Secure; localStorage é acessível pelo JavaScript e não acompanha requests automaticamente.','Tokens sensíveis em localStorage ficam expostos a XSS; a escolha depende do modelo de autenticação/ameaças.','cookie localStorage session storage security web')
,Q('Fundamentos Web','O que HTTPS adiciona?','HTTP sobre TLS fornece confidencialidade, integridade e autenticação do servidor via certificado.','HTTPS não torna aplicação segura contra XSS, SQL injection ou falhas de autorização.','https tls ssl certificate encryption web')
,Q('Fundamentos Web','O que acontece ao digitar uma URL?','Em alto nível: resolve DNS, abre conexão, negocia TLS se HTTPS, envia HTTP, recebe resposta e o browser processa recursos/renderização.','Em HTTP/2/3 alguns detalhes de transporte mudam, mas esse modelo é suficiente para explicar o fluxo.','url dns tcp tls http browser fundamentals')
,Q('Fundamentos SQL','INNER JOIN vs LEFT JOIN?','INNER retorna só linhas com correspondência; LEFT mantém todas da esquerda e preenche ausência da direita com NULL.','Escolho pelo significado dos dados, não pelo hábito.','sql inner join left join database')
,Q('Fundamentos SQL','WHERE vs HAVING?','WHERE filtra linhas antes da agregação; HAVING filtra grupos depois do GROUP BY.','Se o filtro não depende da agregação, normalmente deve estar no WHERE.','sql where having group by aggregate')
,Q('Fundamentos SQL','GROUP BY para quê?','Agrupa linhas para aplicar agregações como COUNT, SUM e AVG por chave.','As colunas selecionadas precisam ser agregadas ou compatíveis com a regra de agrupamento do banco.','sql group by count sum avg aggregate')
,Q('Fundamentos SQL','Primary Key vs Unique?','Primary Key identifica a linha e implica unicidade/não-null; UNIQUE impõe unicidade adicional.','Uma tabela tem uma PK, mas pode ter várias constraints UNIQUE de negócio.','primary key unique constraint sql database')
,Q('Fundamentos SQL','Foreign Key serve para quê?','Garante integridade referencial entre tabelas.','Também preciso decidir políticas de delete/update e entender custo/locking em operações grandes.','foreign key referential integrity sql database')
,Q('Fundamentos SQL','NULL é igual a NULL?','Em SQL comum, comparação com NULL usa lógica de três valores; NULL = NULL não é TRUE.','Uso IS NULL/IS NOT NULL e tomo cuidado com NOT IN quando há NULL.','sql null three valued logic is null')
,Q('Fundamentos SQL','Normalização: por quê?','Reduz redundância e anomalias de atualização separando dados conforme dependências.','Desnormalização pode ser consciente para leitura/performance, mas precisa justificar consistência e custo de atualização.','normalization denormalization sql database 3nf')
,Q('Fundamentos SQL','DELETE vs TRUNCATE vs DROP?','DELETE remove linhas, TRUNCATE esvazia tabela com semântica própria do banco, DROP remove o objeto.','Locks, logging, triggers e rollback variam por banco; eu confirmo a semântica específica antes de operação crítica.','delete truncate drop sql ddl dml')
,Q('Fundamentos Backend','Síncrono vs assíncrono?','Síncrono mantém o chamador esperando o resultado; assíncrono permite desacoplar tempo de processamento/entrega.','Assíncrono melhora desacoplamento e resiliência em alguns fluxos, mas adiciona eventual consistency e complexidade operacional.','sync async backend messaging api')
,Q('Fundamentos Backend','Stateless vs stateful?','Stateless não depende de estado local da instância entre requisições; stateful mantém estado de sessão/processo.','Stateless facilita escala horizontal; estado durável costuma ir para banco/cache/serviço apropriado.','stateless stateful backend scale')
,Q('Fundamentos Backend','Escala vertical vs horizontal?','Vertical aumenta recursos de uma máquina; horizontal aumenta número de instâncias.','Horizontal exige pensar em estado compartilhado, coordenação, balanceamento e limites downstream.','vertical horizontal scaling scale backend')
,Q('Fundamentos Backend','Cache: quando usar?','Quando leitura repetida/cara e tolerância a dados possivelmente stale justificam reduzir trabalho.','Antes de adicionar cache eu defino chave, TTL, invalidação e comportamento em miss/falha.','cache ttl invalidation backend redis')
,Q('Fundamentos Backend','Connection pool: por quê?','Reutiliza conexões caras com banco em vez de abrir uma por request.','Pool precisa de limite compatível com capacidade do banco e número de instâncias.','connection pool database backend')
,Q('Fundamentos Backend','O que é N+1?','Uma consulta carrega N itens e depois dispara mais uma consulta por item, causando N+1 round trips.','Resolvo com join, batch/eager loading ou DataLoader conforme ORM/arquitetura.','n+1 query orm database performance')
,Q('Fundamentos Backend','O que é race condition?','É quando resultado depende da ordem/interleaving de operações concorrentes.','Resolvo protegendo a invariável no ponto certo: operação atômica, constraint, transação, lock ou versionamento.','race condition concurrency backend')
,Q('Fundamentos Backend','Processo vs thread?','Processos têm espaço de memória isolado; threads compartilham memória dentro do processo.','Threads têm comunicação mais barata, mas exigem sincronização; processos aumentam isolamento e custo.','process thread concurrency operating system fundamentals')
,Q('Fundamentos Testes','Mock vs Stub vs Fake?','Stub devolve respostas controladas; mock também verifica interações; fake é uma implementação simplificada funcional.','Os termos variam entre ferramentas, mas eu escolho test double pelo risco que quero isolar.','mock stub fake test double testing')
,Q('Fundamentos Testes','AAA em testes?','Arrange prepara, Act executa, Assert verifica.','É uma estrutura simples para deixar intenção do teste evidente.','arrange act assert AAA testing unit')
,Q('Fundamentos Testes','O que torna um teste bom?','Determinístico, legível, rápido no nível adequado e focado em comportamento relevante.','Evito testar detalhe interno sem necessidade porque isso cria testes frágeis a refactor.','good test deterministic brittle testing')
,Q('Fundamentos Git','git fetch vs pull?','fetch baixa referências sem integrar; pull normalmente faz fetch + merge/rebase conforme configuração.','Prefiro entender o que será integrado antes de puxar mudanças em branches importantes.','git fetch pull merge rebase fundamentals')
,Q('Fundamentos Git','Reset vs revert?','reset move ponteiros/histórico local; revert cria um novo commit que desfaz mudanças.','Em histórico compartilhado, revert costuma ser mais seguro porque não reescreve commits publicados.','git reset revert history fundamentals')
'''

anchor = 'const shortOverrides={'
pos = s.find(anchor)
if pos < 0:
    raise SystemExit('shortOverrides marker not found')
prefix = s[:pos]
close = prefix.rfind('];')
if close < 0:
    raise SystemExit('questions close not found')
s = s[:close] + extras + '\n' + s[close:]

# Put fundamentals at the top of the map.
map_anchor = 'const interviewMap=[\n'
if map_anchor in s:
    entry = "['Fundamentos / Pleno','OO → estruturas/Big-O → HTTP → SQL → backend → testes/Git',['Fundamentos OO','Big O','HTTP status','SQL join','race condition','mock stub fake']],\n"
    s = s.replace(map_anchor, map_anchor + entry, 1)

# Add fast hot-zone entry.
s = s.replace("const hotTerms=['event loop'", "const hotTerms=['OO','HTTP','SQL','Big O','event loop'", 1)

# Add follow-up hints.
nh = 'const nextHints={\n'
if nh in s:
    hints = "'Quais são os pilares da orientação a objetos?':'Qual a diferença entre abstração e encapsulamento?',\n'Composição vs herança?':'Me dê um exemplo em que herança criaria acoplamento ruim.',\n'Interface vs classe abstrata?':'Quando você escolheria uma em vez da outra?',\n'O que é Big O?':'Qual a complexidade de buscar num array, hash map e árvore balanceada?',\n'INNER JOIN vs LEFT JOIN?':'E o que muda se não houver correspondência na tabela da direita?',\n'GET vs POST?':'Quais métodos HTTP são safe e quais são idempotentes?',\n"
    s = s.replace(nh, nh + hints, 1)

# Visual marker/version text.
s = s.replace('Amaris Full Stack Senior — Interview Copilot V4</title>', 'Amaris Full Stack Senior — Interview Copilot V4.1</title>', 1)
s = s.replace('⚡ Amaris — INTERVIEW COPILOT V4</h1>', '⚡ Amaris — INTERVIEW COPILOT V4.1</h1>', 1)
s = s.replace('<span class="priority">V4:</span> cobertura ampliada para perguntas avançadas e derivadas;', '<span class="priority">V4.1:</span> agora inclui Fundamentos/Pleno (OO, Big-O, HTTP, SQL, backend e testes) além da cobertura avançada;', 1)
s = s.replace('<!-- INTERVIEW COPILOT V4 -->', '<!-- INTERVIEW COPILOT V4 -->\n<!-- FUNDAMENTOS PLENO V4.1 -->', 1)

p.write_text(s, encoding='utf-8')
print('Fundamentos/Pleno added')
