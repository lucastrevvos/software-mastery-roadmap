from pathlib import Path

p = Path('docs/amaris-fullstack-interview.html')
s = p.read_text(encoding='utf-8')
if 'INTERVIEW COPILOT V4.3' in s:
    raise SystemExit(0)

s = s.replace('Interview Copilot V4.2', 'Interview Copilot V4.3')
s = s.replace('INTERVIEW COPILOT V4.2', 'INTERVIEW COPILOT V4.3')
s = s.replace('<span class="priority">V4.1:</span>', '<span class="priority">V4.3:</span>')

q = "Q('Node','Como o Node consegue atender várias requisições simultaneamente se o JavaScript normalmente executa em uma única thread?','O JavaScript normalmente roda na main thread, mas o Node não fica esperando I/O terminar. O runtime delega rede, disco e outras operações ao sistema operacional/libuv e continua processando outras requisições; quando o I/O termina, a continuação volta ao Event Loop.','O ponto central é concorrência assíncrona, não executar todo o trabalho em paralelo na mesma thread. Isso funciona muito bem para workloads I/O-bound. Se eu colocar CPU pesada na main thread, bloqueio o Event Loop e aumento a latência de todas as requisições; nesse caso avalio Worker Threads, fila ou outro serviço.','node várias requisições simultâneas milhares conexões single-thread single threaded concurrency concorrência event loop libuv io nonblocking non-blocking worker threads')\n"
marker = "Q('JavaScript','O que é o Event Loop?'"
idx = s.find(marker)
if idx < 0:
    raise SystemExit('Event Loop question marker not found')
if "Q('Node','Como o Node consegue atender várias requisições simultaneamente" not in s[:idx]:
    s = s[:idx] + q + s[idx:]

# Add direct synonym expansion for how interviewers tend to phrase this question.
s = s.replace("const synonymMap={fila:", "const synonymMap={simultaneamente:'node event loop single thread concurrency io libuv',conexoes:'node event loop io nonblocking concurrency',requisicoes:'node api event loop concurrency',fila:")

# Add likely follow-up.
hints_marker = "const nextHints={\n"
hint = "'Como o Node consegue atender várias requisições simultaneamente se o JavaScript normalmente executa em uma única thread?':'E o que acontece se uma dessas requisições fizer processamento pesado de CPU?',\n"
if hints_marker in s and hint not in s:
    s = s.replace(hints_marker, hints_marker + hint, 1)

s = s.replace('<!-- INTERVIEW COPILOT V4.2 -->', '<!-- INTERVIEW COPILOT V4.3 -->')
p.write_text(s, encoding='utf-8')
print('V4.3 applied')
