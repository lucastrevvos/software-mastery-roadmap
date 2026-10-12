"use strict";
const STORAGE_KEY="software-mastery-concursos-cme-v1";
const LINKED_KEY="software-mastery-concursos-casan-cgu-2026-v1";
const $=id=>document.getElementById(id);
let model=null;
let state=loadStore();
const gaps={por:.72,lei:.90,delphi:.90,mat:.62,gov:.75,sec:.70,java:.44,sql:.30,arq:.38,eng:.50,atual:.50,aud:.92,dados:.78,disc:.92};
function initial(){return {schemaVersion:1,minutes:240,sessions:[],updatedAt:null}}

function loadStore(){try{const x=JSON.parse(localStorage.getItem(STORAGE_KEY));return x?.schemaVersion===1&&Array.isArray(x.sessions)?{...initial(),...x}:initial()}catch{return initial()}}

function saveStore(){state.updatedAt=new Date().toISOString();localStorage.setItem(STORAGE_KEY,JSON.stringify(state));render()}

function esc(x){return String(x??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]))}

function localDate(x){const d=new Date(x);return new Date(d.getFullYear(),d.getMonth(),d.getDate(),12)}

function dateKey(x){const d=localDate(x);return [d.getFullYear(),String(d.getMonth()+1).padStart(2,"0"),String(d.getDate()).padStart(2,"0")].join("-")}

function daysUntil(date){return Math.round((localDate(date+"T12:00:00")-localDate(new Date()))/86400000)}

function phase(){return daysUntil("2026-11-22")>=0?"casan":daysUntil("2026-12-13")>=0?"cgu":"after"}

function linkedSessions(){
 try{
  const old=JSON.parse(localStorage.getItem(LINKED_KEY));
  if(!Array.isArray(old?.labHistory))return [];
  return old.labHistory.filter(x=>Number.isFinite(+x.correct)&&x.completedAt).map((x,i)=>{
   const blank=Array.isArray(x.answers)?x.answers.filter(y=>y===null).length:0;
   const total=Number(x.total||10),correct=Number(x.correct);
   return {id:"linked-"+i+"-"+x.completedAt,topic:"por",exam:"casan",mode:"lab",total,correct,wrong:Math.max(0,total-correct-blank),blank,minutes:Number(x.minutes||25),confidence:"",reason:"none",at:x.completedAt,linked:true};
  });
 }catch{return []}
}

function sessionsAll(){return [...state.sessions,...linkedSessions()].filter(x=>+x.total>0&&+x.correct>=0).sort((a,b)=>new Date(a.at)-new Date(b.at))}

function observed(t,all){
 const matches=all.filter(s=>s.topic===t.id).slice(-5);let wc=0,wt=0,time=0,missing=0;
 matches.forEach((s,i)=>{const n=i+1;wc+=s.correct*n;wt+=s.total*n;if(s.reason==="time")time++;if(s.reason==="knowledge"||s.reason==="forgetting")missing++});
 const accuracy=wt?wc/wt:null,gap=accuracy===null?(gaps[t.id]??.6):Math.max(.04,1-accuracy);
 let streak=0;for(let i=matches.length-1;i>=0;i--){if(matches[i].correct/matches[i].total>=.8)streak++;else break}
 const interval=streak>=3?14:streak===2?7:streak===1?3:1;
 const last=matches.at(-1);let next=null,due=false;
 if(last){const date=localDate(last.at);date.setDate(date.getDate()+interval);next=dateKey(date);due=localDate(new Date())>=date}
 return {accuracy,gap,count:matches.length,last,streak,interval,next,due,time,missing};
}

function weight(t,s,p){
 const relevance=p==="casan"?(t.track==="casan"?1.55:t.track==="shared"?1.32:.31):p==="cgu"?(t.track==="cgu"?1.7:t.track==="shared"?1.28:.1):1;
 let v=(4-t.priority)*relevance*(1+1.7*s.gap);
 if(!s.count)v*=1.13;if(s.due)v*=1.27;
 if(s.time)v*=1+Math.min(.25,s.time*.11);
 if(s.missing)v*=1+Math.min(.18,s.missing*.07);
 if(s.count>=2&&s.accuracy>=.85&&!s.due)v*=.65;
 return +v.toFixed(2);
}

function rankings(){
 const p=phase(),all=sessionsAll();
 return model.topics.map(t=>({...t,measure:observed(t,all)})).map(t=>({...t,rank:weight(t,t.measure,p)})).sort((a,b)=>b.rank-a.rank);
}

function advice(t){
 const s=t.measure.last;
 if(!s)return "Sem medição neste tema: fazer 10 questões diagnósticas sem consulta.";
 if(s.reason==="time")return "10 itens cronometrados; pular os demorados e voltar na segunda passagem.";
 if(s.reason==="interpretation")return "Comparar as alternativas e explicar por que cada distrator está errado.";
 if(s.reason==="knowledge")return "15 min de teoria focal, 10 questões comentadas e 10 independentes.";
 if(s.reason==="forgetting")return "Lembrar sem consulta e retestar com questão diferente.";
 if(s.correct/s.total>=.8)return "Revisão espaçada com questões inéditas; sem repetir apenas as respostas.";
 return "Classificar os erros, revisar exemplos e retestar.";
}

function topicName(id){return model.topics.find(t=>t.id===id)?.name||id}

function reasonName(id){return {knowledge:"Conteúdo",interpretation:"Interpretação",time:"Tempo",forgetting:"Esquecimento",none:"Não indicado"}[id]||id}

function renderPriorities(list){
 $("priorityList").innerHTML=list.slice(0,6).map((t,i)=>{
  const s=t.measure;
  return `<article class="topic"><div><p class="eyebrow">#${i+1} · ${esc(t.track==="shared"?"CASAN + CGU":t.track.toUpperCase())} · P${t.priority}</p><h3>${esc(t.name)}</h3><p>${s.count?Math.round(s.accuracy*100)+"% em "+s.count+" treino(s) recente(s)":"Hipótese inicial: ainda sem medição"}${s.due?" · revisão vencida":""}</p><p>${esc(advice(t))}</p></div><div><strong class="score">${t.rank.toFixed(1)}</strong><div class="meta">Índice<br>relativo</div></div></article>`
 }).join("");
}

function pick(list,track,used){return list.find(t=>t.track===track&&!used.has(t.id))||list.find(t=>!used.has(t.id))||list[0]}

function allocations(total,shares){let rest=total;return shares.map((v,i)=>{const n=i===shares.length-1?rest:Math.round(total*v);rest-=n;return n})}

function renderSchedule(list){
 const p=phase(),tracks=p==="casan"?["review","casan","shared","shared","cgu","ledger"]:p==="cgu"?["review","cgu","shared","cgu","shared","ledger"]:["review","shared","cgu","casan","shared","ledger"];
 const shares=p==="casan"?[.10,.32,.28,.14,.10,.06]:p==="cgu"?[.10,.32,.24,.19,.09,.06]:[.12,.28,.24,.20,.10,.06];
 const times=allocations(state.minutes,shares),used=new Set();
 const due=list.filter(t=>t.measure.due).sort((a,b)=>a.measure.next.localeCompare(b.measure.next));
 const blocks=tracks.map((type,i)=>{
  if(type==="review")return ["Revisão ativa",due.length?"Reteste vencido: "+due[0].name:"Recordar cinco regras sem consulta.",times[i]];
  if(type==="ledger")return ["Error Ledger","Anotar erros, causa, correção e próxima tentativa.",times[i]];
  const t=pick(list,type,used);used.add(t.id);return [t.name,advice(t),times[i]];
 });
 $("dailyPlan").innerHTML=blocks.map(([name,tip,min],i)=>`<div class="block"><div class="split"><h3>${i+1}. ${esc(name)}</h3><strong class="good-text">${min} min</strong></div><p>${esc(tip)}</p></div>`).join("")+`<div class="split"><strong>Total</strong><strong class="good-text">${state.minutes} minutos</strong></div>`;
}

function renderReviews(list){
 const practiced=list.filter(t=>t.measure.last).sort((a,b)=>a.measure.next.localeCompare(b.measure.next));
 $("reviews").innerHTML=practiced.length?practiced.slice(0,8).map(t=>`<article class="block"><div class="split"><strong>${esc(t.name)}</strong><span class="pill ${t.measure.due?"good":""}">${t.measure.due?"VENCIDA":"REVER "+t.measure.next.split("-").reverse().join("/")}</span></div><p>Último treino: ${Math.round(t.measure.last.correct/t.measure.last.total*100)}% · intervalo D+${t.measure.interval}</p></article>`).join(""):'<p class="empty">Sem sessões registradas. O primeiro Lab gera uma data de reteste.</p>';
}

function renderGates(all){
 const casan=all.filter(s=>s.exam==="casan"&&s.mode==="simulado"&&s.total===50&&s.minutes<=240&&s.correct>=42);
 const dates=new Set(casan.map(s=>dateKey(s.at)));
 const ids=["cgu-p1","cgu-p2","cgu-p3"],len=[40,40,90],mins=[8,12,54];
 const p=ids.map((id,i)=>{const s=all.filter(x=>x.exam===id&&x.mode==="simulado"&&x.total===len[i]).at(-1);return s?{points:(s.correct-s.wrong)*(i===2?2:1)}:null});
 const ready=p.every(Boolean),sum=ready?p.reduce((v,x)=>v+x.points,0):null;
 $("gates").innerHTML=`<div class="block"><div class="split"><h3>CASAN · 42/50 em duas datas</h3><span class="pill ${dates.size>=2?"good":""}">${dates.size>=2?"Meta de treino atingida":"Em progresso"}</span></div><p>${dates.size}/2 simulados completos em dias distintos, ≤240 min.</p></div><div class="block"><div class="split"><h3>CGU · mínimos objetivos</h3><span class="pill ${ready&&p.every((s,i)=>s.points>=mins[i])&&sum>=78?"good":""}">${ready?sum+" pontos (P1+P2+P3)":"Sem simulado integral"}</span></div><p>${ready?p.map((s,i)=>"P"+(i+1)+": "+s.points).join(" · "):"P1: 40 itens; P2: 40; P3: 90. C/E com erros penalizados."} Discursiva avaliada separadamente.</p></div><p class="muted" style="font-size:12px">Os critérios aqui são metas do treinamento, não classificação ou habilitação oficial.</p>`;
}

function renderHistory(all){
 $("history").innerHTML=all.length?all.slice().reverse().slice(0,25).map(s=>{
  const d=new Date(s.at).toLocaleDateString("pt-BR"),score=s.exam==="cgu-p3"?2:s.exam.startsWith("cgu-")?1:0;
  return `<article class="history-item"><div><strong>${esc(topicName(s.topic))} · ${Math.round(100*s.correct/s.total)}%</strong><p>${esc(d)} · ${esc(s.mode)} · ${s.correct} acertos, ${s.wrong} erros, ${s.blank} brancos · ${s.minutes} min${score?" · C/E: "+(s.correct-s.wrong)*score+" pontos":""}</p><p>Causa: ${esc(reasonName(s.reason))}</p></div>${s.linked?'<span class="pill">Vinculado</span>':`<button type="button" class="btn danger small" data-delete="${esc(s.id)}">Excluir</button>`}</article>`;
 }).join(""):'<p class="empty">Nenhum resultado registrado. Comece pelo workshop ou informe uma bateria de questões.</p>';
 document.querySelectorAll("[data-delete]").forEach(el=>el.addEventListener("click",()=>{if(!confirm("Excluir esta sessão?"))return;state.sessions=state.sessions.filter(s=>s.id!==el.dataset.delete);saveStore()}));
}

function render(){
 if(!model)return;
 const p=phase(),date=p==="casan"?"2026-11-22":p==="cgu"?"2026-12-13":null,all=sessionsAll(),r=rankings();
 $("countdown").textContent=date?daysUntil(date)+" dias":"Encerradas";
 $("examName").textContent=p==="casan"?"CASAN primeiro":p==="cgu"?"CGU em foco":"Novo ciclo a planejar";
 $("phaseLabel").textContent=p==="casan"?"CASAN primeiro":p==="cgu"?"CGU prioritária":"Histórico";
 $("sessionsCount").textContent=all.length;$("questionCount").textContent=all.reduce((s,x)=>s+x.total,0);
 $("dueCount").textContent=r.filter(x=>x.measure.due).length;
 $("minutes").value=String(state.minutes);
 renderPriorities(r);renderSchedule(r);renderReviews(r);renderGates(all);renderHistory(all);
}

function addSession(e){
 e.preventDefault();const f=new FormData(e.currentTarget);
 const total=Number(f.get("total")),correct=Number(f.get("correct")),wrong=Number(f.get("wrong")),blank=Number(f.get("blank")),minutes=Number(f.get("minutes"));
 if(![total,correct,wrong,blank,minutes].every(Number.isInteger)||total<1||total>200||correct<0||wrong<0||blank<0||correct+wrong+blank!==total||minutes<1||minutes>600){$("saveStatus").textContent="Confira os valores: acertos + erros + brancos deve ser igual ao total.";return}
 const topic=String(f.get("topic")),exam=String(f.get("exam")),mode=String(f.get("mode"));
 if(!model.topics.some(x=>x.id===topic)||!["casan","cgu-p1","cgu-p2","cgu-p3","other"].includes(exam)||!["lab","simulado","review"].includes(mode)){$("saveStatus").textContent="Assunto ou prova inválidos.";return}
 state.sessions.push({id:new Date().toISOString()+"-"+state.sessions.length,topic,exam,mode,total,correct,wrong,blank,minutes,confidence:String(f.get("confidence")||""),reason:String(f.get("reason")),at:new Date().toISOString()});
 saveStore();$("saveStatus").textContent="Treino registrado. Prioridades e retestes recalculados.";e.currentTarget.reset();
}

function exportState(){
 const content=JSON.stringify({...state,exportedAt:new Date().toISOString(),source:"Concurso Mastery Engine"},null,2)+"\n";
 const url=URL.createObjectURL(new Blob([content],{type:"application/json"}));const a=document.createElement("a");a.href=url;a.download="cme-progresso-"+dateKey(new Date())+".json";a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
}

async function importState(e){
 const file=e.target.files?.[0];if(!file)return;
 try{
  const obj=JSON.parse(await file.text());
  if(obj.schemaVersion!==1||!Array.isArray(obj.sessions)||!obj.sessions.every(s=>typeof s.topic==="string"&&s.id&&Number.isInteger(s.total)&&s.correct+s.wrong+s.blank===s.total))throw Error("Histórico incompatível ou inválido.");
  if(!confirm("Substituir o histórico atual pelos dados importados?"))return;
  state={...initial(),...obj};saveStore();$("importStatus").textContent="Importação concluída.";
 }catch(err){$("importStatus").textContent="Falha: "+err.message}finally{e.target.value=""}
}

async function init(){
 try{
  const r=await fetch("./plano-2026.json",{cache:"no-store"});if(!r.ok)throw Error("Plano de estudos inacessível");
  model=await r.json();if(!Array.isArray(model.topics))throw Error("Formato inválido do plano.");
  $("topic").innerHTML=model.topics.map(t=>`<option value="${esc(t.id)}">${esc(t.name)}</option>`).join("");
  $("minutes").addEventListener("change",e=>{state.minutes=Number(e.target.value);saveStore()});
  $("sessionForm").addEventListener("submit",addSession);
  $("export").addEventListener("click",exportState);
  $("import").addEventListener("change",importState);
  render();
 }catch(err){$("priorityList").innerHTML=`<p class="note" role="alert">${esc(err.message)}</p>`}
}

document.addEventListener('DOMContentLoaded', init);
