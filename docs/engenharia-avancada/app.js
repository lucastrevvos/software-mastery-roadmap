(() => {
  "use strict";
  const STORE_KEY = "advanced-engineering-roadmap-progress-v1";
  const VALID_STATUSES = ["not-started", "studying", "proven"];
  let curriculum = null;
  let state = loadState();
  const $ = id => document.getElementById(id);
  const safe = value => String(value ?? "").replace(/[&<>"']/g, c => ({
    "&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;", "'":"&#39;"
  }[c]));
  const fmt = s => safe(s).replace(/\n/g, "<br>");
  const safeUrl = value => {
    try {const u = new URL(value); return u.protocol === "https:" ? u.href : "#"; }
    catch {return "#";}
  };
  function loadState() {
    try {
      const parsed = JSON.parse(localStorage.getItem(STORE_KEY) || "{}");
      return {
        version: 1,
        weeks: parsed && typeof parsed.weeks === "object" && !Array.isArray(parsed.weeks) ? parsed.weeks : {},
        gates: parsed && typeof parsed.gates === "object" && !Array.isArray(parsed.gates) ? parsed.gates : {}
      };
    } catch {return {version:1,weeks:{},gates:{}};}
  }
  function save() {try {localStorage.setItem(STORE_KEY, JSON.stringify(state));} catch(e) { console.warn("Persistência local indisponível",e); }}
  const weekKey = (m, w) => m.id + "-w" + w;
  const gateKey = (m, g) => m.id + "-" + g.label;
  const weekInfo = key => state.weeks[key] || {status:"not-started",evidence:""};
  const gateInfo = key => state.gates[key] || {validated:false,evidence:""};
  const progressOf = m => {
    const done = m.weeks.filter((w,i) => weekInfo(weekKey(m,m.start+i)).status === "proven").length;
    return {done,total:m.weeks.length,percent:Math.round(done/m.weeks.length*100)};
  };
  function updateStats() {
    if (!curriculum) return;
    const weeksDone = curriculum.modules.reduce((n,m)=>n+progressOf(m).done,0);
    const gatesDone = curriculum.modules.reduce((n,m)=>n+m.checkpoints.filter(g=>gateInfo(gateKey(m,g)).validated).length,0);
    $("stat-weeks").textContent = weeksDone + "/40";
    $("stat-gates").textContent = gatesDone + "/15";
    $("stat-percent").textContent = Math.round(weeksDone/40*100) + "%";
    $("global-meter").style.width = Math.round(weeksDone/40*100) + "%";
  }
  function activeId() {
    const hash = location.hash.slice(1);
    return curriculum.modules.some(m=>m.id===hash) ? hash : curriculum.modules[0].id;
  }
  function renderSidebar() {
    const active = activeId();
    $("module-nav").innerHTML = curriculum.modules.map(m=>{
      const p=progressOf(m);
      return '<button type="button" class="module-pill' + (m.id===active?' active':'') +
       '" data-module="' + safe(m.id) + '" aria-current="' + (m.id===active?'true':'false') + '">' +
       '<b>' + m.number + '. ' + safe(m.title) + '</b><small>Semanas ' + m.start + '–' + m.end +
       ' · ' + p.done + '/' + p.total + ' comprovadas</small>' +
       '<div class="track"><span style="width:' + p.percent + '%"></span></div></button>';
    }).join("");
  }
  const li = items => items.map(x=>'<li>'+safe(x)+'</li>').join("");
  function renderWeek(m, week, i) {
    const n=m.start+i, k=weekKey(m,n), w=weekInfo(k);
    const status=VALID_STATUSES.includes(w.status)?w.status:"not-started";
    const statusLabel={ "not-started":"Não iniciado", "studying":"Estudando", "proven":"Comprovado" }[status];
    return '<article class="week" id="week-'+n+'">' +
      '<div class="week-header"><div class="week-heading"><small>SEMANA '+n+'</small><strong>'+safe(week[0])+'</strong></div>' +
      '<span class="status-label'+(status==="proven"?' done':'')+'">'+statusLabel+'</span></div>' +
      '<details><summary>Teoria profunda, laboratório e evidência</summary><div class="week-body">' +
      '<h4>Teoria e mecanismos</h4><p>'+safe(week[1])+'</p>' +
      '<h4>Laboratório</h4><p class="lab">'+safe(week[2])+'</p>' +
      '<div class="week-controls"><label>Status<select data-week-status="'+safe(k)+'">' +
      [['not-started','Não iniciado'],['studying','Estudando'],['proven','Comprovado']].map(a=>'<option value="'+a[0]+'"'+(status===a[0]?' selected':'')+'>'+a[1]+'</option>').join('') +
      '</select></label><label>Evidência: link para commit, teste, relatório ou descrição<textarea rows="2" data-week-evidence="'+safe(k)+'" placeholder="Ex.: commit SHA, relatório dos testes, hipótese + resultado...">'+safe(w.evidence||"")+'</textarea></label></div>' +
      '<p class="note">Marque Comprovado apenas após executar, explicar, depurar e transferir o conhecimento. Evidência obrigatória.</p>' +
      '</div></details></article>';
  }
  function renderGate(m,g) {
    const k=gateKey(m,g), s=gateInfo(k);
    return '<article class="gate"><div class="gate-top"><strong>Checkpoint '+safe(g.label)+' · Semana '+g.week+' — '+safe(g.title)+'</strong>'+
    '<small>'+ (s.validated?'VALIDADO COM EVIDÊNCIA':'PENDENTE') +'</small></div><ul class="gate-list">'+li(g.items)+'</ul>'+
    '<div class="gate-controls"><label>Resultado<select data-gate-status="'+safe(k)+'">'+
    '<option value="pending"'+(!s.validated?' selected':'')+'>Pendente</option>'+
    '<option value="validated"'+(s.validated?' selected':'')+'>Validado</option></select></label>'+
    '<label>Evidência da validação<input class="gate-proof" type="text" data-gate-evidence="'+safe(k)+'" value="'+safe(s.evidence||"")+'" placeholder="Commits, artefatos, resultados, ADRs..."></label></div></article>';
  }
  function renderModule() {
    const m=curriculum.modules.find(x=>x.id===activeId()) || curriculum.modules[0], p=progressOf(m);
    const project=m.project;
    $("module-content").innerHTML =
      '<p class="micro">MÓDULO '+m.number+' · SEMANAS '+m.start+'–'+m.end+'</p>' +
      '<h2 class="module-title">'+safe(m.title)+'</h2><p class="lead">'+safe(m.summary)+'</p>'+
      '<div class="module-flags"><span class="flag">'+safe(m.focus)+'</span><span class="flag">'+p.done+'/'+p.total+' semanas comprovadas</span></div>'+
      (m.caveat?'<div class="notice"><strong>Atenção conceitual:</strong> '+safe(m.caveat)+'</div>':'')+
      '<div class="block"><h3>1. Objetivos de aprendizado</h3><p class="muted">Ao final deste módulo você deverá conseguir demonstrar:</p>'+
      '<ol class="objective-list">'+li(m.objectives)+'</ol></div>'+
      '<div class="block"><h3>2. Grade curricular · semana a semana</h3><p class="muted">Abra cada semana, execute o laboratório e registre a evidência antes de comprovar.</p>'+
      '<div class="weeks">'+m.weeks.map((w,i)=>renderWeek(m,w,i)).join('')+'</div></div>'+
      '<div class="block"><h3>3. Conceitos-chave e termos de busca</h3><div class="keyword-table"><table><thead><tr><th>Área</th><th>Português e inglês para aprofundamento</th></tr></thead><tbody>'+
      m.keywords.map(x=>'<tr><td>'+safe(x[0])+'</td><td>'+safe(x[1])+'</td></tr>').join('')+'</tbody></table></div></div>'+
      '<div class="block"><h3>4. Projeto prático de consolidação</h3><div class="project-card"><h4>'+safe(project.name)+'</h4>'+
      '<p class="stack">'+safe(project.stack)+'</p><p class="scenario">'+safe(project.scenario)+'</p>'+
      '<h4>Requisitos e desafios de engenharia</h4><ul class="requirements-list">'+li(project.requirements)+'</ul></div>'+
      (m.failureMatrix?'<h4>Matriz de falhas obrigatórias</h4><div class="scroll"><table><thead><tr><th>Falha</th><th>Comportamento exigido</th></tr></thead><tbody>'+m.failureMatrix.map(x=>'<tr><td>'+safe(x[0])+'</td><td>'+safe(x[1])+'</td></tr>').join('')+'</tbody></table></div>':'')+
      (m.targets?'<h4>Metas iniciais do laboratório (não são SLAs universais)</h4><div class="scroll"><table><tbody>'+m.targets.map(x=>'<tr><td>'+safe(x[0])+'</td><td>'+safe(x[1])+'</td></tr>').join('')+'</tbody></table></div>':'')+'</div>'+
      '<div class="block"><h3>5. Critérios de aceite e checkpoints</h3><p class="muted">Cada gate exige evidência concreta. Assinalar “validado” sem evidência não é permitido.</p>'+
      '<div class="gates">'+m.checkpoints.map(g=>renderGate(m,g)).join('')+'</div></div>'+
      '<div class="block"><h3>Referências e documentação</h3><ul class="readings">'+li(m.readings)+'</ul><div class="links-list">'+
      m.links.map(x=>'<a href="'+safe(safeUrl(x.url))+'" target="_blank" rel="noopener noreferrer">'+safe(x.label)+' ↗</a>').join('')+'</div></div>';
    renderSidebar();
    updateStats();
  }
  function renderStatic() {
    $("project-overview").textContent = curriculum.integratedProject.summary;
    $("project-progression").innerHTML = curriculum.integratedProject.progression.map((s,i)=>
      '<div class="progress-step"><b>MÓDULO '+(i+1)+'</b>'+safe(s)+'</div>').join('');
    $("mastery-scale").innerHTML = curriculum.masteryScale.map(x=>
      '<div class="scale-item"><b>NÍVEL '+x.value+'</b><strong>'+safe(x.label)+'</strong><p>'+safe(x.description)+'</p></div>').join('');
    $("approval-rules").innerHTML=li(curriculum.approval);
    $("evidence-table").innerHTML=curriculum.evidenceMatrix.map(x=>
      '<tr><td>'+safe(x[0])+'</td><td>'+safe(x[1])+'</td></tr>').join('');
    $("final-challenges").innerHTML=curriculum.finalChallenge.map(x=>
      '<div class="info-card"><strong>'+safe(x[0])+'</strong><p>'+safe(x[1])+'</p></div>').join('');
    $("competencies").innerHTML=curriculum.competencies.map(x=>
      '<div class="info-card"><strong>'+safe(x[0])+'</strong><p>'+safe(x[1])+'</p></div>').join('');
    $("disclaimer").textContent=curriculum.disclaimer;
  }
  function updateEvidence(type,key,value) {
    const target=type==="week"?state.weeks:state.gates;
    if(!target[key]) target[key]=type==="week"?{status:"not-started",evidence:""}:{validated:false,evidence:""};
    target[key].evidence=value;
    if(!value.trim()){
      if(type==="week"&&target[key].status==="proven")target[key].status="studying";
      if(type==="gate"&&target[key].validated)target[key].validated=false;
    }
    save(); updateStats(); renderSidebar();
  }
  function onChange(e){
    const t=e.target, k=t.dataset.weekStatus;
    if(k){
      const v=t.value;
      if(!VALID_STATUSES.includes(v))return;
      const o=state.weeks[k]||{status:"not-started",evidence:""};
      if(v==="proven"&&!(o.evidence||"").trim()){
        alert("Registre uma evidência concreta (commit, teste, resultado ou relatório) antes de marcar Comprovado.");
        t.value=o.status||"not-started";return;
      }
      o.status=v;state.weeks[k]=o;save();renderModule();const activeWeek=document.getElementById("week-"+k.split("-w")[1]);if(activeWeek){const details=activeWeek.querySelector("details");if(details)details.open=true;}return;
    }
    const g=t.dataset.gateStatus;
    if(g){
      const o=state.gates[g]||{validated:false,evidence:""};
      if(t.value==="validated"&&!(o.evidence||"").trim()){
        alert("Preencha a evidência do checkpoint antes de marcar Validado.");t.value=o.validated?"validated":"pending";return;
      }
      o.validated=t.value==="validated";state.gates[g]=o;save();renderModule();return;
    }
    if(t.dataset.weekEvidence)updateEvidence("week",t.dataset.weekEvidence,t.value);
    if(t.dataset.gateEvidence)updateEvidence("gate",t.dataset.gateEvidence,t.value);
  }
  function exportProgress() {
    const body={schemaVersion:1,roadmap:"engenharia-avancada",exportedAt:new Date().toISOString(),progress:state};
    const blob=new Blob([JSON.stringify(body,null,2)],{type:"application/json"});
    const url=URL.createObjectURL(blob);
    const a=document.createElement("a");a.href=url;a.download="engenharia-avancada-progresso.json";
    document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);
  }
  async function importProgress(file) {
    if(!file)return;
    try {
      const payload=JSON.parse(await file.text());
      if(payload.roadmap!=="engenharia-avancada"||payload.schemaVersion!==1)throw new Error("Arquivo não corresponde a este roadmap.");
      const p=payload.progress;
      if(!p||!p.weeks||!p.gates||typeof p.weeks!=="object"||typeof p.gates!=="object")throw new Error("Estrutura de progresso inválida.");
      const validWeeks={},validGates={};
      for(const [k,v] of Object.entries(p.weeks)){
        if(!/^m[1-5]-w([1-9]|[1-3][0-9]|40)$/.test(k))continue;
        if(!v||!VALID_STATUSES.includes(v.status))continue;
        const evidence=String(v.evidence||"").slice(0,4000);
        validWeeks[k]={status:v.status==="proven"&&!evidence.trim()?"studying":v.status,evidence};
      }
      for(const [k,v] of Object.entries(p.gates)){
        if(!/^m[1-5]-[ABC]$/.test(k)||!v)continue;
        const evidence=String(v.evidence||"").slice(0,4000);
        validGates[k]={validated:!!v.validated&&!!evidence.trim(),evidence};
      }
      if(!confirm("Substituir o progresso local pelo arquivo importado?"))return;
      state={version:1,weeks:validWeeks,gates:validGates};save();renderModule();
      alert("Progresso importado.");
    }catch(err){alert("Não foi possível importar: "+err.message);}
    finally{$("file-import").value="";}
  }
  async function init() {
    try {
      const r=await fetch("data.json",{cache:"no-cache"});if(!r.ok)throw new Error("HTTP "+r.status);
      curriculum=await r.json();
      if(!Array.isArray(curriculum.modules)||curriculum.modules.length!==5||curriculum.modules.some(m=>m.weeks.length!==8))throw new Error("Estrutura curricular inesperada.");
      renderStatic();renderModule();
      window.addEventListener("hashchange",()=>{renderModule();});
      $("module-nav").addEventListener("click",e=>{
        const b=e.target.closest("[data-module]");if(!b)return;
        location.hash=b.dataset.module;
        renderModule();
        $("module-content").scrollIntoView({behavior:"smooth",block:"start"});
      });
      $("module-content").addEventListener("change",onChange);
      $("module-content").addEventListener("input",e=>{
        const t=e.target;
        if(t.dataset.weekEvidence)updateEvidence("week",t.dataset.weekEvidence,t.value);
        if(t.dataset.gateEvidence)updateEvidence("gate",t.dataset.gateEvidence,t.value);
      });
      $("btn-export").addEventListener("click",exportProgress);
      $("btn-import").addEventListener("click",()=> $("file-import").click());
      $("file-import").addEventListener("change",e=>importProgress(e.target.files[0]));
      $("btn-clear").addEventListener("click",()=>{
        if(confirm("Apagar o progresso local desta trilha? Esta ação não altera o GitHub.")){
          state={version:1,weeks:{},gates:{}};save();renderModule();
        }
      });
    }catch(err){
      $("module-content").innerHTML='<h2>Falha ao carregar o currículo</h2><p>Verifique a publicação de <code>data.json</code> e abra a página via GitHub Pages.</p><pre>'+safe(err.message)+'</pre>';
      console.error(err);
    }
  }
  document.addEventListener("DOMContentLoaded",init);
})();