from pathlib import Path

p = Path('docs/amaris-fullstack-interview.html')
s = p.read_text(encoding='utf-8')

array_pos = s.find('const alexandreRounds=[')
if array_pos == -1:
    raise SystemExit('alexandreRounds not found')

# Remove any premature render call before the data declaration.
premature = s.rfind('renderAlexandre();', 0, array_pos)
if premature != -1:
    s = s[:premature] + s[premature + len('renderAlexandre();'):]

# Insert render call after the renderAlexandre function, before hotTerms.
hot_pos = s.find("const hotTerms=", array_pos)
if hot_pos == -1:
    raise SystemExit('hotTerms marker not found')

before_hot = s[:hot_pos]
if 'renderAlexandre();' not in before_hot[array_pos:]:
    s = s[:hot_pos] + 'renderAlexandre();\n\n' + s[hot_pos:]

p.write_text(s, encoding='utf-8')
print('Alexandre Mode render order fixed')
