from pathlib import Path
p = Path('docs/amaris-fullstack-interview.html')
s = p.read_text(encoding='utf-8')
bad = "worker threads')\nQ('JavaScript','O que é o Event Loop?'"
good = "worker threads'),\nQ('JavaScript','O que é o Event Loop?'"
if bad not in s:
    raise SystemExit('target syntax pattern not found')
s = s.replace(bad, good, 1)
p.write_text(s, encoding='utf-8')
print('V4.3 syntax repaired')
