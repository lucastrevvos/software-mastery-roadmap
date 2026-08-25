const $=selector=>document.querySelector(selector);

async function loadJson(path){
  const response=await fetch(path,{cache:'no-store'});
  if(!response.ok) throw new Error(`Falha ao carregar ${path}: ${response.status}`);
  return response.json();
}

function statusLabel(status){
  return ({'in-progress':'em andamento','not-started':'não iniciado','completed':'concluído','mastered':'dominado'}[status]||status);
}

function statusClass(status){return `status status-${status}`;}

function renderCurrent(progress){
  const courses=Object.entries(progress.courses).filter(([,c])=>c.status==='in-progress');
  $('#current-courses').innerHTML=courses.map(([id,c])=>`
    <article class="course-card">
      <span class="${statusClass(c.status)}">${statusLabel(c.status)}</span>
      <h3>${id==='cs50x'?'CS50x':id==='fcc-js-v10'?'freeCodeCamp JavaScript':id}</h3>
      <p class="muted">Atual: ${c.current||'a definir'}</p>
      ${c.completed?.length?`<small>${c.completed.length} marco(s) registrado(s)</small>`:''}
    </article>`).join('');
}

function renderMastery(mastery){
  const list=mastery.competencies;
  const assessed=list.filter(x=>x.level>0);
  const avg=assessed.length?assessed.reduce((sum,x)=>sum+x.level,0)/assessed.length:0;
  $('#mastery-average').textContent=`${avg.toFixed(1)}/7`;
  $('#mastery-list').innerHTML=list.map(item=>`
    <div class="mastery-row">
      <div>
        <strong>${item.title}</strong>
        ${item.provisional?'<div class="provisional">provisório — aguardando gate/reteste</div>':''}
      </div>
      <div class="mastery-track" title="${item.level}/7"><div class="mastery-fill" style="width:${(item.level/7)*100}%"></div></div>
      <div class="mastery-score">${item.level}/7</div>
    </div>`).join('');
}

function renderReviews(reviews){
  const pending=reviews.queue.filter(r=>r.status!=='completed');
  $('#reviews-due').textContent=pending.length;
  $('#review-list').innerHTML=pending.length?pending.map(r=>`
    <article class="review-card">
      <div><strong>${r.id}</strong><span class="muted">${r.source}</span></div>
      <div><span class="status status-in-progress">${r.type}</span><div class="muted">Prazo: ${r.dueDate}</div></div>
    </article>`).join(''):'<p class="muted">Nenhuma revisão pendente.</p>';
}

function renderErrors(ledger){
  const open=ledger.errors.filter(e=>e.status==='open').length;
  $('#errors-open').textContent=open;
}

function paidPrice(item){
  const price=item.examPrice||item.programPrice;
  if(!price) return '';
  const base=item.priceAsOf?` · base ${item.priceAsOf}`:'';
  return `<small class="roadmap-price"><strong>Preço:</strong> ${price}${base}</small>`;
}

function isFreeCredential(item){
  if(item.priority==='free-credential') return true;
  if(item.cost!=='free') return false;
  const credential=(item.credential||'').toLowerCase();
  const externalCredential=/(certificate|certification|digital credential|micro-credential|university certificate|ects|badge)/.test(credential);
  const internalOnly=/(no external certificate|mastery|portfolio|applied project|documentation)/.test(credential);
  return externalCredential&&!internalOnly;
}

function freeCredentialBadge(item){
  return isFreeCredential(item)?'<span class="free-credential-badge">CERTIFICAÇÃO GRÁTIS</span>':'';
}

const roadmapDescriptions={
  'cs50x':'Introdução rigorosa à ciência da computação: pensamento computacional, C, algoritmos, memória, estruturas de dados, Python, SQL e fundamentos web.',
  'foundational-csharp':'Fundamentos de C# e .NET com tipos, variáveis, controle de fluxo, métodos, arrays, tratamento de dados e construção de programas de console.',
  'fcc-js-v10':'Trilha prática de JavaScript moderno para consolidar sintaxe, funções, arrays, objetos, algoritmos, lógica e resolução de problemas por projetos.',
  'cs50-sql':'Bancos relacionais do modelo aos detalhes de implementação: consultas, joins, modelagem, normalização, índices, transações e desempenho.',
  'cs50p':'Programação em Python com funções, exceções, bibliotecas, testes, arquivos, expressões regulares, orientação a objetos e boas práticas.',
  'linux-essentials':'Fundamentos práticos de Linux: terminal, sistema de arquivos, permissões, processos, usuários, pacotes, redes básicas, segurança e shell scripting.',
  'cisco-networking-basics':'Base oficial de redes com Ethernet, IPv4/IPv6, switching, roteamento, TCP/UDP, protocolos de aplicação, wireless, segurança e troubleshooting.',
  'cisco-ccst-networking':'Certificação de entrada que valida suporte e fundamentos de redes, endereçamento IP, conectividade, switching/routing, troubleshooting e segurança básica.',
  'full-stack-open-core':'Engenharia web full stack moderna com React, Node.js/Express, APIs REST, testes, gerenciamento de estado e integração frontend-backend.',
  'full-stack-open-extensions':'Aprofundamentos selecionados do Full Stack Open, como TypeScript, GraphQL, CI/CD, containers, bancos relacionais e outros tópicos de produção.',
  'angular-official-essentials':'Entrada oficial no Angular moderno: modelo mental do framework, componentes, templates, signals, CLI e construção da primeira aplicação.',
  'angular-official-core':'Domínio do núcleo do Angular com standalone components, composição, bindings, control flow, Signals e Dependency Injection.',
  'angular-official-app-engineering':'Construção de aplicações Angular completas com Router, HTTP, interceptors, forms, carregamento sob demanda e fluxo de dados.',
  'angular-official-testing-debugging':'Testes e diagnóstico de aplicações Angular com TestBed, testes de componentes, HTTP, Router, async e Angular DevTools.',
  'angular-official-performance-ssr':'Angular para produção com performance, lazy loading, @defer, SSR/SSG, hydration, Core Web Vitals e arquitetura zoneless.',
  'angular-mastery-project':'Projeto aplicado para provar que os conceitos de Angular podem ser explicados, construídos, depurados e transferidos sem depender de tutorial.',
  'hackerrank-angular-basic':'Avaliação prática de fundamentos Angular, incluindo componentes, templates, TypeScript, data binding e validação de formulários.',
  'hackerrank-angular-intermediate':'Avaliação intermediária de Angular com Routing, módulos, Observables, Dependency Injection, integração com APIs e estrutura de aplicações.',
  'dotnet-backend':'Engenharia backend com .NET/C#: ASP.NET Core, APIs, persistência, async, testes, segurança, observabilidade e práticas de arquitetura.',
  'cs50-web':'Desenvolvimento web avançado com Python, JavaScript, Django, SQL, APIs, interfaces, testes, segurança, escalabilidade e projetos completos.',
  'ibm-ai-foundations-understanding':'Base conceitual de IA, machine learning, redes neurais, deep learning, aplicações, ética e princípios de IA responsável.',
  'ibm-artificial-intelligence-fundamentals':'Fundamentos aplicados de IA cobrindo ML, deep learning, NLP, visão computacional, chatbots, redes neurais e execução de modelos.',
  'alteryx-ml-fundamentals':'Microcredencial sobre o ciclo básico de machine learning: preparação de dados, escolha, avaliação e interpretação de modelos.',
  'cs50-ai':'Fundamentos clássicos de IA com busca, representação de conhecimento, incerteza, otimização, aprendizado de máquina, redes neurais e linguagem.',
  'cs50-cyber':'Introdução prática à segurança digital: contas, sistemas, software, privacidade, ameaças, autenticação, defesa e decisões de risco.',
  'python-ai-engineering':'Python voltado à engenharia de IA em produção: organização de código, dados, integração de modelos, APIs, testes, observabilidade e automação.',
  'azure-foundations':'Fundamentos da nuvem Microsoft Azure: conceitos cloud, principais serviços, segurança, governança, custos e modelo operacional.',
  'azure-developer':'Desenvolvimento de aplicações cloud no Azure com serviços de IA, containers, dados, mensageria, segurança, integração e observabilidade.',
  'azure-administrator':'Administração operacional do Azure: identidades, governança, storage, compute, redes virtuais, monitoramento e manutenção de recursos.',
  'azure-solutions-architect':'Arquitetura de soluções Azure com identidade, governança, dados, continuidade de negócio, infraestrutura, integração e trade-offs de design.',
  'aws-foundations':'Fundamentos AWS e preparação para Cloud Practitioner: serviços principais, segurança, arquitetura, custos, suporte e conceitos de nuvem.',
  'aws-solutions-architect-associate':'Certificação de arquitetura AWS que valida desenho de soluções seguras, resilientes, performáticas e otimizadas em custo.',
  'oci-foundations':'Fundamentos da Oracle Cloud Infrastructure, incluindo compute, storage, networking, bancos, segurança, governança e serviços essenciais.',
  'isaqb-cpsa-f-curriculum':'Currículo vendor-neutral de arquitetura de software cobrindo fundamentos, design, atributos de qualidade, documentação, comunicação e decisões arquiteturais.',
  'architecture-foundations':'Prática dos fundamentos arquiteturais: drivers, restrições, qualidade, acoplamento, coesão, estilos, trade-offs e tomada de decisão.',
  'architecture-documentation':'Comunicação de arquitetura com C4, ADRs, cenários de qualidade, views/viewpoints e registro explícito do raciocínio por trás das decisões.',
  'ddd-clean-hexagonal':'Modelagem e modularidade com DDD, bounded contexts, Clean Architecture, Ports & Adapters, direção de dependências e testabilidade.',
  'distributed-systems':'Fundamentos de sistemas distribuídos com mensageria, consistência, idempotência, retries, timeouts, circuit breakers e arquitetura orientada a eventos.',
  'observability-platform':'Operação de software moderno com logs, métricas, traces, CI/CD, containers, plataformas internas, automação e práticas de confiabilidade.',
  'architecture-mastery-defense':'Gate prático em que uma arquitetura é criada a partir de requisitos, documentada, criticada e defendida com trade-offs explícitos.',
  'isaqb-cpsa-f-exam':'Certificação vendor-neutral que valida conhecimento fundamental de arquitetura de software segundo o currículo oficial do iSAQB.',
  'sei-software-architecture-professional':'Programa profissional avançado do SEI/Carnegie Mellon sobre princípios, documentação, design e análise sistemática de arquiteturas de software.',
  'llm-apps':'Engenharia de aplicações com LLMs: integração de modelos, prompts, structured outputs, ferramentas, contexto, custo, latência e confiabilidade.',
  'rag-agents':'Construção de RAG e agentes com recuperação, embeddings, busca, tool use, memória, workflows e limites entre decisões probabilísticas e determinísticas.',
  'llmops':'Operação de sistemas de IA com avaliações, observabilidade, segurança, guardrails, versionamento, custo, latência e melhoria contínua.',
  'capstone-system':'Sistema final que integra frontend, backend, cloud, dados, segurança, observabilidade e IA em uma solução de portfólio próxima de produção.',
  'architecture-defense':'Defesa final escrita e oral das decisões do capstone, demonstrando domínio de requisitos, trade-offs, evolução, riscos e comunicação arquitetural.'
};

function roadmapDescription(item){
  return item.description||roadmapDescriptions[item.id]||item.note||'';
}

function renderRoadmap(roadmap){
  const items=roadmap.phases.flatMap(p=>p.items);
  const completed=items.filter(i=>['completed','mastered'].includes(i.status)).length;
  const active=items.filter(i=>i.status==='in-progress').length;
  const weighted=completed+(active*.5);
  const percent=items.length?Math.round((weighted/items.length)*100):0;
  $('#roadmap-percent').textContent=`${percent}%`;
  $('#roadmap-count').textContent=`${completed} concluído(s) · ${active} em andamento · ${items.length} total`;
  $('#roadmap').innerHTML=roadmap.phases.map((phase,index)=>`
    <section class="phase">
      <div class="phase-title"><span>${String(index+1).padStart(2,'0')}</span><h3>${phase.title}</h3></div>
      <p>${phase.goal}</p>
      <div class="phase-items">
        ${phase.items.map(item=>`
          <article class="roadmap-item ${isFreeCredential(item)?'roadmap-item-free-credential':''}">
            <div class="roadmap-item-content">
              <div class="roadmap-title-line"><h4>${item.order}. ${item.title}</h4>${freeCredentialBadge(item)}</div>
              ${roadmapDescription(item)?`<p class="roadmap-description">${roadmapDescription(item)}</p>`:''}
              <small>${item.provider} · ${item.credential}</small>
              ${paidPrice(item)}
            </div>
            <span class="${statusClass(item.status)}">${statusLabel(item.status)}</span>
          </article>`).join('')}
      </div>
    </section>`).join('');
}

async function init(){
  try{
    const [roadmap,progress,mastery,reviews,ledger]=await Promise.all([
      loadJson('data/roadmap.json'),
      loadJson('data/progress.json'),
      loadJson('data/mastery.json'),
      loadJson('data/reviews.json'),
      loadJson('data/error-ledger.json')
    ]);
    renderCurrent(progress);
    renderMastery(mastery);
    renderReviews(reviews);
    renderErrors(ledger);
    renderRoadmap(roadmap);
    $('#last-updated').textContent=`Atualizado ${progress.updatedAt.replace('T',' ').replace('-03:00',' BRT')}`;
  }catch(error){
    console.error(error);
    document.body.insertAdjacentHTML('afterbegin',`<div style="padding:12px;background:#5b1e25;color:white;text-align:center">Não foi possível carregar os dados do dashboard. ${error.message}</div>`);
  }
}

document.addEventListener('DOMContentLoaded',init);