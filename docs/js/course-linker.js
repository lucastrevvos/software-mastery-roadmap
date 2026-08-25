async function loadRoadmapForLinks(){
  const response=await fetch('data/roadmap.json',{cache:'no-store'});
  if(!response.ok) return null;
  return response.json();
}

function decorateRoadmapCards(roadmap){
  const items=roadmap.phases.flatMap(phase=>phase.items);
  const byOrder=new Map(items.map(item=>[String(item.order),item]));

  document.querySelectorAll('.roadmap-item').forEach(card=>{
    if(card.dataset.courseLinked==='true') return;
    const heading=card.querySelector('h4');
    const content=card.querySelector('.roadmap-item-content');
    if(!heading||!content) return;
    const match=heading.textContent.trim().match(/^(\d+)\./);
    if(!match) return;
    const item=byOrder.get(match[1]);
    if(!item) return;

    card.querySelector('.course-notes')?.remove();
    const link=document.createElement('a');
    link.className='course-page-link';
    link.href=`course.html?id=${encodeURIComponent(item.id)}`;
    link.textContent='Abrir curso →';
    content.appendChild(link);
    card.dataset.courseLinked='true';
  });
}

function decorateCurrentCards(roadmap){
  const titleToId={
    'CS50x':'cs50x',
    'freeCodeCamp JavaScript':'fcc-js-v10'
  };
  document.querySelectorAll('.course-card').forEach(card=>{
    if(card.dataset.courseLinked==='true') return;
    const title=card.querySelector('h3')?.textContent.trim();
    const id=titleToId[title];
    if(!id) return;
    const link=document.createElement('a');
    link.className='course-page-link';
    link.href=`course.html?id=${encodeURIComponent(id)}`;
    link.textContent='Abrir curso →';
    card.appendChild(link);
    card.dataset.courseLinked='true';
  });
}

document.addEventListener('DOMContentLoaded',async()=>{
  const roadmap=await loadRoadmapForLinks();
  if(!roadmap) return;
  const apply=()=>{
    decorateRoadmapCards(roadmap);
    decorateCurrentCards(roadmap);
  };
  apply();
  const observer=new MutationObserver(apply);
  const roadmapRoot=document.querySelector('#roadmap');
  const currentRoot=document.querySelector('#current-courses');
  if(roadmapRoot) observer.observe(roadmapRoot,{childList:true,subtree:true});
  if(currentRoot) observer.observe(currentRoot,{childList:true,subtree:true});
  window.setTimeout(()=>observer.disconnect(),5000);
});
