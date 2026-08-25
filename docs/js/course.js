const $=selector=>document.querySelector(selector);

async function loadJson(path){
  const response=await fetch(path,{cache:'no-store'});
  if(!response.ok) throw new Error(`Falha ao carregar ${path}: ${response.status}`);
  return response.json();
}

function escapeHtml(value){
  return String(value??'').replace(/[&<>"']/g,char=>({
    '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'
  })[char]);
}

function statusLabel(status){
  return ({'in-progress':'em andamento','not-started':'não iniciado','completed':'concluído','mastered':'dominado'}[status]||status);
}

function statusClass(status){return `status status-${status}`;}

function isFreeCredential(item){
  if(item.priority==='free-credential') return true;
  if(item.cost!=='free') return false;
  const credential=(item.credential||'').toLowerCase();
  const externalCredential=/(certificate|certification|digital credential|micro-credential|university certificate|ects|badge)/.test(credential);
  const internalOnly=/(no external certificate|mastery|portfolio|applied project|documentation)/.test(credential);
  return externalCredential&&!internalOnly;
}

function metaCard(label,value,extraClass=''){
  if(!value) return '';
  return `<article class="course-meta-card ${extraClass}"><span>${escapeHtml(label)}</span><strong>${escapeHtml(value)}</strong></article>`;
}

function renderLinks(item){
  const candidates=[
    ['Fonte oficial',item.source],
    ['Objetivos',item.objectives],
    ['Material de estudo',item.learningMaterial],
    ['Prática / tutorial',item.practice],
    ['Preço / registro',item.priceSource]
  ].filter(([,url])=>url);

  $('#course-links').innerHTML=candidates.length
    ? candidates.map(([label,url])=>`<a href="${escapeHtml(url)}" target="_blank" rel="noreferrer">${escapeHtml(label)} ↗</a>`).join('')
    : '<span class="muted">Links oficiais serão adicionados conforme a trilha for sendo detalhada.</span>';
}

function renderProgress(courseProgress,item){
  const target=$('#course-progress');
  if(!courseProgress){
    target.innerHTML=`<p class="muted">Este item ainda não possui progresso detalhado registrado.</p>`;
    return;
  }

  const completed=courseProgress.completed||[];
  target.innerHTML=`
    <div class="progress-current">
      <span>Atual</span>
      <strong>${escapeHtml(courseProgress.current||'a definir')}</strong>
    </div>
    ${completed.length?`
      <div class="completed-block">
        <h3>Marcos concluídos</h3>
        <div class="completed-list">${completed.map(step=>`<span>✓ ${escapeHtml(step)}</span>`).join('')}</div>
      </div>`:'<p class="muted">Nenhum marco concluído registrado ainda.</p>'}
  `;
}

function renderFocus(item){
  const target=$('#course-focus');
  const focus=item.focus||[];
  const extras=[];
  if(item.assessment) extras.push(`<div class="course-callout"><strong>Avaliação</strong><p>${escapeHtml(item.assessment)}</p></div>`);
  if(item.estimatedHours) extras.push(`<div class="course-callout"><strong>Tempo estimado</strong><p>${escapeHtml(item.estimatedHours)}</p></div>`);
  if(item.note) extras.push(`<div class="course-callout"><strong>Estratégia no roadmap</strong><p>${escapeHtml(item.note)}</p></div>`);

  if(!focus.length&&!extras.length){
    target.innerHTML='<p class="muted">O conteúdo detalhado será registrado conforme este item se aproximar na trilha.</p>';
    return;
  }

  target.innerHTML=`
    ${focus.length?`<div class="focus-tags">${focus.map(topic=>`<span>${escapeHtml(topic)}</span>`).join('')}</div>`:''}
    ${extras.join('')}
  `;
}

function renderNotes(notes=[]){
  $('#notes-count').textContent=notes.length?`${notes.length} nota(s) registrada(s)`:'nenhuma nota ainda';
  const target=$('#course-notes-page');
  if(!notes.length){
    target.innerHTML='<div class="empty-notes"><strong>Nenhuma anotação ainda.</strong><p>Quando uma explicação, conexão ou resumo valer a pena guardar, ela aparecerá aqui.</p></div>';
    return;
  }

  target.innerHTML=notes.map(note=>`
    <article class="knowledge-note" id="${escapeHtml(note.id||'')}">
      <div class="knowledge-note-head">
        <div>
          <span class="course-note-type">${escapeHtml(note.type||'nota')}</span>
          <h3>${escapeHtml(note.title)}</h3>
        </div>
        <time>${escapeHtml(note.date||'')}</time>
      </div>
      ${note.summary?`<p class="knowledge-summary">${escapeHtml(note.summary)}</p>`:''}
      ${note.points?.length?`<ul>${note.points.map(point=>`<li>${escapeHtml(point)}</li>`).join('')}</ul>`:''}
      ${note.mentalModel?`<div class="note-mental-model page-model"><strong>Modelo mental</strong><code>${escapeHtml(note.mentalModel)}</code></div>`:''}
      ${note.relatedTopics?.length?`<div class="note-tags">${note.relatedTopics.map(tag=>`<span>${escapeHtml(tag)}</span>`).join('')}</div>`:''}
    </article>
  `).join('');
}

async function init(){
  try{
    const courseId=new URLSearchParams(window.location.search).get('id');
    if(!courseId) throw new Error('Curso não informado.');

    const [roadmap,descriptions,progress,notesData]=await Promise.all([
      loadJson('data/roadmap.json'),
      loadJson('data/course-descriptions.json'),
      loadJson('data/progress.json'),
      loadJson('data/course-notes.json')
    ]);

    let item=null;
    let phase=null;
    for(const candidatePhase of roadmap.phases){
      const candidate=candidatePhase.items.find(x=>x.id===courseId);
      if(candidate){item=candidate;phase=candidatePhase;break;}
    }
    if(!item) throw new Error(`Item '${courseId}' não encontrado no roadmap.`);

    document.title=`${item.title} · Software Mastery Roadmap`;
    $('#course-phase').textContent=`${phase.title} · etapa ${item.order}`;
    $('#course-title').textContent=item.title;
    $('#course-description').textContent=item.description||descriptions[item.id]||item.note||'';

    const status=$('#course-status');
    status.className=statusClass(item.status);
    status.textContent=statusLabel(item.status);

    const price=item.examPrice||item.programPrice;
    $('#course-meta').innerHTML=[
      metaCard('Provedor',item.provider),
      metaCard('Credencial',item.credential,isFreeCredential(item)?'meta-free':''),
      isFreeCredential(item)?metaCard('Custo da credencial','GRÁTIS','meta-free'):metaCard('Preço',price),
      metaCard('Prioridade',item.priority),
      metaCard('Custo / modelo',item.cost),
      metaCard('Preço verificado em',item.priceAsOf)
    ].join('');

    renderLinks(item);
    renderProgress(progress.courses?.[item.id],item);
    renderFocus(item);
    renderNotes(notesData.courses?.[item.id]||[]);
  }catch(error){
    console.error(error);
    document.body.innerHTML=`<main class="shell course-error"><a class="back-link" href="index.html">← Voltar ao roadmap</a><h1>Não foi possível abrir este curso</h1><p>${escapeHtml(error.message)}</p></main>`;
  }
}

document.addEventListener('DOMContentLoaded',init);
