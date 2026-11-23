"use strict";
(() => {
  const KEY = "acervolab-academy-progress-v1";
  const STATUS = { "nao-iniciado": "Não iniciado", estudando: "Estudando", praticado: "Praticado", validado: "Validado com evidência" };
  const $ = (s, root = document) => root.querySelector(s);
  const $$ = (s, root = document) => Array.from(root.querySelectorAll(s));
  const esc = value => String(value ?? "").replace(/[&<>"']/g, c => ({ "&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;", "'":"&#39;" }[c]));
  const safeUrl = value => { try { const u = new URL(String(value), location.href); return ["https:","http:"].includes(u.protocol) ? u.href : null; } catch { return null; } };
  let curriculum = null, notebook = null, currentSemester = 0;
  let state = { schemaVersion: 1, topics: {}, diary: [] };
  function readLocal() {
    try {
      const raw = localStorage.getItem(KEY);
      if (!raw) return;
      const data = JSON.parse(raw);
      if (data && data.schemaVersion === 1) {
        state = { schemaVersion:1, topics: data.topics && typeof data.topics === "object" && !Array.isArray(data.topics) ? data.topics : {}, diary: Array.isArray(data.diary) ? data.diary.slice(0,2000) : [] };
      }
    } catch (error) { console.warn("Não foi possível ler o progresso local.", error); }
  }
  function saveLocal() {
    try { localStorage.setItem(KEY, JSON.stringify(state)); }
    catch (error) { alert("Falha ao salvar no navegador. Exporte um backup JSON."); console.error(error); }
  }
  function subjects() { return curriculum.semesters.flatMap(s => s.subjects); }
  function topics() { return subjects().flatMap(s => s.topics); }
  function active(topicId) { const x = state.topics[topicId]; return x && STATUS[x.status] ? x : { status:"nao-iniciado",evidence:"" }; }
  function validated(topicList) { return topicList.filter(x => active(x.id).status === "validado").length; }
  function stats() {
    const t = topics();
    const valid = validated(t);
    const studying = t.filter(x => ["estudando","praticado"].includes(active(x.id).status)).length;
    $("#stat-progress").textContent = t.length ? Math.round(valid/t.length*100)+"%" : "0%";
    $("#stat-progress-detail").textContent = valid+" de "+t.length+" tópicos com evidência";
    $("#stat-study").textContent = String(studying);
    $("#stat-theory").textContent = String(notebook.notes.length);
    $("#hero-topics").textContent = t.length+" tópicos";
  }
  function selectView(name) {
    $$(".view-tab").forEach(b => { const on = b.dataset.view === name; b.classList.toggle("active",on); b.setAttribute("aria-selected",String(on)); });
    $$(".view").forEach(section => { const on = section.id === "view-"+name; section.hidden = !on; section.classList.toggle("active",on); });
    if (name === "teoria") renderTheory();
    if (name === "diario") renderDiary();
  }
  function renderSidebar() {
    $("#semester-nav").innerHTML = curriculum.semesters.map((s,i) => {
      const t = s.subjects.flatMap(x => x.topics);
      return '<button type="button" class="semester-btn '+(i===currentSemester?'active':'')+'" data-semester="'+i+'" aria-pressed="'+(i===currentSemester)+'"><strong>'+esc((i+1)+"º semestre")+'</strong><small>'+t.filter(x=>active(x.id).status==="validado").length+'/'+t.length+' tópicos comprovados</small></button>';
    }).join("");
  }
  function renderSemester() {
    const s = curriculum.semesters[currentSemester];
    const noteIds = new Set(notebook.notes.map(n => n.topicId));
    const header = '<div class="semester-head"><p class="eyebrow">SEMESTRE '+(currentSemester+1)+'</p><h3>'+esc(s.name)+'</h3><p>'+esc(s.objective)+'</p><span class="milestone">'+esc(s.milestone)+'</span></div>';
    const body = s.subjects.map((sub,i) => {
      const valid = validated(sub.topics);
      const percent = sub.topics.length ? Math.round(valid/sub.topics.length*100) : 0;
      const cards = sub.topics.map(t => {
        const p = active(t.id);
        const link = noteIds.has(t.id) ? ' <button class="text-button theory-anchor" data-note-topic="'+esc(t.id)+'" type="button">Ler teoria</button>' : '';
        const options = Object.entries(STATUS).map(([v,label]) => '<option value="'+v+'" '+(v===p.status?'selected':'')+'>'+label+'</option>').join("");
        return '<div class="topic" data-status="'+esc(p.status)+'"><div class="topic-title"><span class="topic-id">'+esc(t.id)+'</span><span>'+esc(t.title)+'</span>'+link+'</div><div class="topic-actions"><label class="sr-only" for="sel-'+esc(t.id)+'">Status de '+esc(t.title)+'</label><select id="sel-'+esc(t.id)+'" data-topic="'+esc(t.id)+'">'+options+'</select></div><div class="topic-extra"><label for="ev-'+esc(t.id)+'">Evidência (commit, PR, teste ou explicação verificável)</label><input id="ev-'+esc(t.id)+'" data-evidence="'+esc(t.id)+'" maxlength="500" value="'+esc(p.evidence||"")+'" placeholder="Ex.: https://github.com/…/commit/…"></div></div>';
      }).join("");
      return '<details class="discipline" '+(i===0?'open':'')+'><summary class="discipline-head"><span><small>'+esc(sub.id)+'</small><strong>'+esc(sub.title)+'</strong></span><span class="discipline-meta"><span>'+valid+' / '+sub.topics.length+' validados</span><span class="discipline-meter"><i style="width:'+percent+'%"></i></span></span></summary><div class="discipline-body"><p>'+esc(sub.why)+'</p><div class="labblock"><div><strong>Laboratório:</strong> '+esc(sub.lab)+'</div><div><strong>Gate:</strong> '+esc(sub.gate)+'</div></div><div class="topic-list">'+cards+'</div></div></details>';
    }).join("");
    $("#semester-detail").innerHTML = header+body;
  }
  function renderTheory() {
    const value = ($("#theory-search").value || "").trim().toLocaleLowerCase("pt-BR");
    const found = notebook.notes.filter(n => [n.name,n.definition,n.problem,n.kind,n.related,n.example,n.topicId].join(" ").toLocaleLowerCase("pt-BR").includes(value));
    $("#theory-results").innerHTML = found.length ? found.map(n =>
      '<article class="theory-card"><div class="theory-meta"><span class="chip">'+esc(n.kind)+'</span><span>'+esc(n.topicId)+'</span><span>· '+esc(n.state)+'</span></div><h3>'+esc(n.name)+'</h3><dl>'+
      '<dt>Definição</dt><dd>'+esc(n.definition)+'</dd>'+
      '<dt>Problema que resolve</dt><dd>'+esc(n.problem)+'</dd>'+
      '<dt>Exemplo</dt><dd><code>'+esc(n.example)+'</code></dd>'+
      '<dt>Armadilha comum</dt><dd>'+esc(n.pitfall)+'</dd>'+
      '<dt>Relações</dt><dd>'+esc(n.related)+'</dd>'+
      '</dl><p class="subtle">Registro: '+esc(n.learnedAt)+' · '+esc(n.source)+'</p></article>'
    ).join("") : '<p class="empty">Nenhum conceito encontrado. As novas notas de aula serão adicionadas aqui por commit no repositório.</p>';
  }
  function renderDiary() {
    $("#diary-count").textContent = state.diary.length+" registros";
    $("#diary-list").innerHTML = state.diary.length ? state.diary.map(d => {
      const evidence = safeUrl(d.evidence);
      return '<article class="diary-entry"><button class="delete-entry" type="button" data-delete="'+esc(d.id)+'" aria-label="Excluir registro">Excluir</button><h4>'+esc(d.subject)+'</h4><small>'+esc(d.date)+'</small><p>'+esc(d.note)+'</p>'+(evidence?'<a href="'+esc(evidence)+'" target="_blank" rel="noopener noreferrer">Ver evidência</a>':(d.evidence?'<small>Referência: '+esc(d.evidence)+'</small>':''))+'</article>';
    }).join("") : '<p class="empty">Nenhum registro local ainda. Use o formulário para registrar experimentos e dúvidas.</p>';
  }
  function renderMilestones() {
    $("#milestone-list").innerHTML = curriculum.milestones.map(m =>
      '<div class="milestone-item"><span class="milestone-version">'+esc(m.id)+'</span><div><strong>'+esc(m.text)+'</strong><p>'+esc(m.architecture)+'</p></div></div>'
    ).join("");
  }
  function onTopicChange(select) {
    const id=select.dataset.topic;
    const existing=active(id);
    const next=select.value;
    if (!(next in STATUS)) { select.value=existing.status;return; }
    if(next==="validado" && !String(existing.evidence||"").trim()) {
      alert("Para marcar como validado, registre antes uma evidência verificável. Primeiro escolha Praticado, preencha a evidência e depois valide.");
      select.value=existing.status;return;
    }
    state.topics[id]={status:next,evidence:String(existing.evidence||"")};
    select.closest(".topic").dataset.status=next;
    saveLocal();stats();renderSidebar();
    const details=select.closest(".discipline");
    const all=$$("[data-topic]",details);
    const valid=all.filter(x=>active(x.dataset.topic).status==="validado").length;
    const text=$(".discipline-meta span",details);
    if(text) text.textContent=valid+" / "+all.length+" validados";
    const meter=$(".discipline-meter i",details);
    if(meter)meter.style.width=Math.round(valid/all.length*100)+"%";
  }
  function onEvidenceChange(input) {
    const id=input.dataset.evidence;
    const p=active(id);
    state.topics[id]={status:p.status,evidence:input.value.trim().slice(0,500)};
    if(p.status==="validado" && !state.topics[id].evidence) {
      state.topics[id].status="praticado";
      const sel=$('[data-topic="'+id+'"]');
      if(sel)sel.value="praticado";
      input.closest(".topic").dataset.status="praticado";
      stats();renderSidebar();
    }
    saveLocal();
  }
  function exportJSON(){
    const blob=new Blob([JSON.stringify({schemaVersion:1,exportedAt:new Date().toISOString(),topics:state.topics,diary:state.diary},null,2)],{type:"application/json"});
    const url=URL.createObjectURL(blob),a=document.createElement("a");
    a.href=url;a.download="acervolab-academy-progresso.json";document.body.appendChild(a);a.click();a.remove();
    setTimeout(()=>URL.revokeObjectURL(url),1000);
  }
  function importJSON(file) {
    if(!file || file.size>2e6){alert("Arquivo ausente ou maior que 2 MB.");return;}
    const reader=new FileReader();
    reader.onload=()=>{
      try {
        const value=JSON.parse(String(reader.result));
        if(value.schemaVersion!==1 || !value.topics || !Array.isArray(value.diary)) throw Error("Estrutura JSON inválida");
        const allowed=new Set(topics().map(t=>t.id)),clean=Object.create(null);
        for(const [id,entry] of Object.entries(value.topics)) {
          if(!allowed.has(id)||!entry||!STATUS[entry.status]) continue;
          const evidence=String(entry.evidence||"").slice(0,500);
          clean[id]={status:entry.status==="validado"&&!evidence?"praticado":entry.status,evidence};
        }
        const entries=value.diary.slice(0,2000).filter(d=>d&&typeof d==="object").map((d,i)=>({
          id:String(d.id||i).slice(0,80),date:String(d.date||"").slice(0,40),subject:String(d.subject||"").slice(0,120),note:String(d.note||"").slice(0,6000),evidence:String(d.evidence||"").slice(0,500)
        }));
        if(!confirm("Substituir o progresso local pelo conteúdo do arquivo importado?"))return;
        state={schemaVersion:1,topics:clean,diary:entries};saveLocal();stats();renderSidebar();renderSemester();renderDiary();
        alert("Backup importado com sucesso.");
      } catch(error){alert("Não foi possível importar: "+error.message);}
    };
    reader.readAsText(file);
  }
  function events(){
    $$(".view-tab").forEach(b=>b.addEventListener("click",()=>selectView(b.dataset.view)));
    $("#semester-nav").addEventListener("click",e=>{
      const b=e.target.closest("[data-semester]");if(!b)return;
      currentSemester=Number(b.dataset.semester);renderSidebar();renderSemester();
    });
    $("#semester-detail").addEventListener("change",e=>{if(e.target.matches("[data-topic]"))onTopicChange(e.target);});
    $("#semester-detail").addEventListener("input",e=>{if(e.target.matches("[data-evidence]"))onEvidenceChange(e.target);});
    $("#semester-detail").addEventListener("click",e=>{
      const b=e.target.closest("[data-note-topic]");if(!b)return;
      const n=notebook.notes.find(n=>n.topicId===b.dataset.noteTopic);
      if(!n)return;$("#theory-search").value=n.name;selectView("teoria");window.scrollTo({top:$("#view-teoria").offsetTop-10,behavior:"smooth"});
    });
    $("#theory-search").addEventListener("input",renderTheory);
    $("#diary-form").addEventListener("submit",e=>{
      e.preventDefault();
      const subject=$("#diary-subject").value.trim(),note=$("#diary-note").value.trim(),evidence=$("#diary-evidence").value.trim();
      if(!subject||!note)return;
      state.diary.unshift({id:String(Date.now())+"-"+String(Math.random()).slice(2,8),date:new Date().toLocaleString("pt-BR"),subject,note,evidence});
      saveLocal();e.target.reset();renderDiary();
    });
    $("#diary-list").addEventListener("click",e=>{
      const b=e.target.closest("[data-delete]");if(!b)return;
      if(!confirm("Excluir esta anotação local?"))return;
      state.diary=state.diary.filter(d=>d.id!==b.dataset.delete);saveLocal();renderDiary();
    });
    $("#export-progress").addEventListener("click",exportJSON);
    $("#import-progress").addEventListener("click",()=>$("#import-file").click());
    $("#import-file").addEventListener("change",e=>{importJSON(e.target.files?.[0]);e.target.value="";});
  }
  async function init(){
    readLocal();
    try {
      const [c,n]=await Promise.all([fetch("curriculum.json",{cache:"no-store"}),fetch("theory.json",{cache:"no-store"})]);
      if(!c.ok||!n.ok) throw Error("Dados não disponíveis: curriculum.json / theory.json");
      curriculum=await c.json();notebook=await n.json();
      if(!Array.isArray(curriculum.semesters)||!Array.isArray(notebook.notes))throw Error("Formato inesperado");
      renderSidebar();renderSemester();renderTheory();renderMilestones();renderDiary();stats();events();
      const hash=location.hash.replace("#","");
      if(["grade","teoria","diario","metodo"].includes(hash))selectView(hash);
    }catch(error){
      $("#semester-detail").innerHTML='<p class="empty">Não foi possível carregar a grade curricular. Acesse o endereço publicado no GitHub Pages e tente atualizar. '+esc(error.message)+'</p>';
      console.error(error);
    }
  }
  init();
})();
