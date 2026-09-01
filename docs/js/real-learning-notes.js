const esc=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[c]));
const list=(items=[])=>items.length?`<ul>${items.map(x=>`<li>${esc(x)}</li>`).join('')}</ul>`:'<p class="empty">Ainda não registrado.</p>';
async function init(){
  const response=await fetch('data/real-learning-lessons.json',{cache:'no-store'});
  if(!response.ok) throw new Error('Falha ao carregar aulas');
  const data=await response.json();
  const lessons=data.stages.flatMap(s=>s.lessons||[]);
  document.querySelector('#lesson-count').textContent=lessons.length;
  document.querySelector('#completed-count').textContent=lessons.filter(x=>x.status==='completed').length;
  document.querySelector('#next-lesson').textContent=lessons.find(x=>x.status==='next')?.id||'—';
  document.querySelector('#lesson-root').innerHTML=data.stages.map(stage=>`
    <section class="lesson-stage">
      <header class="lesson-stage-head"><span>${esc(stage.id.toUpperCase())}</span><h2>${esc(stage.title)}</h2></header>
      <div class="lesson-list">
        ${(stage.lessons||[]).map(lesson=>`
          <details class="lesson" ${lesson.status==='next'?'':'open'}>
            <summary>
              <div class="lesson-title"><span class="lesson-id">${esc(lesson.id)}</span><strong>${esc(lesson.title)}</strong></div>
              <span class="lesson-status lesson-status-${esc(lesson.status)}">${lesson.status==='completed'?'concluída':'próxima'}</span>
            </summary>
            <div class="lesson-content">
              <p class="lesson-summary">${esc(lesson.summary)}</p>
              ${lesson.mentalModel?`<div class="mental-model"><strong>Modelo mental</strong><code>${esc(lesson.mentalModel)}</code></div>`:''}
              <div class="lesson-columns">
                <section class="lesson-box"><h3>Conceitos</h3>${list(lesson.concepts)}</section>
                <section class="lesson-box"><h3>Mini-lab</h3>${list(lesson.lab)}</section>
                <section class="lesson-box"><h3>Armadilhas</h3>${list(lesson.traps)}</section>
                <section class="lesson-box"><h3>Retenção</h3>${lesson.takeaway?`<p class="empty">${esc(lesson.takeaway)}</p>`:'<p class="empty">Será preenchido ao concluir.</p>'}</section>
              </div>
              ${lesson.commands?.length?`<section class="commands"><h3>Comandos da aula</h3><div class="command-list">${lesson.commands.map(c=>`<div class="command-row"><code>${esc(c.cmd)}</code><span>${esc(c.meaning)}</span></div>`).join('')}</div></section>`:''}
              ${lesson.takeaway?`<div class="takeaway"><strong>Levar desta aula:</strong> ${esc(lesson.takeaway)}</div>`:''}
            </div>
          </details>
        `).join('')}
      </div>
    </section>
  `).join('');
}
document.addEventListener('DOMContentLoaded',()=>init().catch(err=>{document.querySelector('#lesson-root').innerHTML=`<p class="section-note">${esc(err.message)}</p>`;}));