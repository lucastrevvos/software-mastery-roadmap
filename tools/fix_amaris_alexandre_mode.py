from pathlib import Path

# Triggered patch: render Alexandre data only after alexandreRounds is initialized.
p = Path('docs/amaris-fullstack-interview.html')
s = p.read_text(encoding='utf-8')

old = "document.getElementById('alexList').addEventListener('click',e=>{const b=e.target.closest('[data-term]');if(!b)return;setAlex(false);active='Todos';renderChips();searchEl.value=b.dataset.term;filter();searchEl.focus()});renderAlexandre();\n\nconst alexandreRounds=["
new = "document.getElementById('alexList').addEventListener('click',e=>{const b=e.target.closest('[data-term]');if(!b)return;setAlex(false);active='Todos';renderChips();searchEl.value=b.dataset.term;filter();searchEl.focus()});\n\nconst alexandreRounds=["

if old not in s:
    raise SystemExit('Expected pre-fix marker not found')

s = s.replace(old, new, 1)

anchor = "function renderAlexandre(){const root=document.getElementById('alexList');let n=0;root.innerHTML=alexandreRounds.map(r=>`<div class=\"alex-round\">${esc(r.title)}</div>${r.items.map((it,j)=>{n++;return `<div class=\"alex-card\"><p class=\"alex-q\"><span class=\"alex-num\">${n}.</span>${esc(it[0])}</p><p class=\"alex-a\">${esc(it[1])}</p><div class=\"alex-meta\"><button class=\"alex-search\" data-term=\"${esc(it[2])}\">abrir ficha: ${esc(it[2])}</button><span class=\"alex-next\">${j<r.items.length-1?'↳ próxima pergunta aprofunda este tema':'✓ fim do round'}</span></div></div>`}).join('')}`).join('')}"

if anchor not in s:
    raise SystemExit('renderAlexandre function marker not found')

s = s.replace(anchor, anchor + "\nrenderAlexandre();", 1)
p.write_text(s, encoding='utf-8')
print('Alexandre Mode render order fixed')
