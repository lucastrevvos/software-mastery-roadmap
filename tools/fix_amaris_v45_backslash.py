from pathlib import Path

p = Path('docs/amaris-fullstack-interview.html')
s = p.read_text(encoding='utf-8')

before = s
s = s.replace('const longAnswers={\n\\\n', 'const longAnswers={\n')
s = s.replace('const nextHints={\n\\\n', 'const nextHints={\n')

if s == before:
    print('No repair needed')
else:
    p.write_text(s, encoding='utf-8')
    print('V4.5 stray backslashes repaired')

# Guard against the exact generation regression.
assert 'const longAnswers={\n\\\n' not in s
assert 'const nextHints={\n\\\n' not in s
