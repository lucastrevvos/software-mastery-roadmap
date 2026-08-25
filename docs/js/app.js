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
            <div>
              <div class="roadmap-title-line"><h4>${item.order}. ${item.title}</h4>${freeCredentialBadge(item)}</div>
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