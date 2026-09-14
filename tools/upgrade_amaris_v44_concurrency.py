from pathlib import Path

p = Path('docs/amaris-fullstack-interview.html')
s = p.read_text(encoding='utf-8')

if 'INTERVIEW COPILOT V4.4' in s:
    raise SystemExit(0)

s = s.replace('Interview Copilot V4.3', 'Interview Copilot V4.4')
s = s.replace('INTERVIEW COPILOT V4.3', 'INTERVIEW COPILOT V4.4')
s = s.replace('<span class="priority">V4.3:</span>', '<span class="priority">V4.4:</span>')

marker = "Q('JavaScript','O que é o Event Loop?'"
idx = s.find(marker)
if idx < 0:
    raise SystemExit('Event Loop marker not found')

extras = """Q('Node','Qual é a diferença entre concorrência e paralelismo no Node?','Concorrência é lidar com várias tarefas em andamento, alternando o progresso sem precisar executá-las exatamente ao mesmo tempo. Paralelismo é executar trabalho realmente ao mesmo tempo em múltiplas threads ou núcleos. No Node, o Event Loop entrega concorrência assíncrona; paralelismo pode aparecer com Worker Threads, processos ou trabalho externo.','Para I/O-bound, o Node ganha muito com concorrência porque não bloqueia esperando rede ou disco. Para CPU-bound, a main thread pode virar gargalo; se eu precisar usar mais de um core para computação, considero Worker Threads, múltiplos processos, fila distribuída ou um serviço separado conforme isolamento, retry e escala necessários.','concorrência paralelismo concurrency parallelism node event loop worker threads cpu bound io bound threads cores'),\nQ('Node','I/O-bound vs CPU-bound: qual a diferença?','I/O-bound passa boa parte do tempo esperando rede, disco, banco ou outro serviço; CPU-bound gasta tempo efetivamente calculando. Node é especialmente eficiente em I/O-bound por causa do modelo assíncrono.','Em CPU-bound, uma função pesada na main thread bloqueia o Event Loop e piora a latência das outras requisições. A saída pode ser dividir o trabalho, usar Worker Threads, fila assíncrona ou serviço especializado.','io bound cpu bound node performance event loop blocking worker threads'),\nQ('Node','O que acontece se uma requisição fizer processamento pesado de CPU na main thread?','Ela bloqueia o Event Loop enquanto o JavaScript estiver executando, então outras requisições ficam esperando e a latência sobe.','Async/await não resolve CPU-bound por si só. Se o cálculo é pesado, eu meço primeiro e então avalio Worker Threads, processo separado, fila ou serviço dedicado; também observo event-loop lag, CPU e P95/P99.','cpu pesada cpu-bound blocking event loop main thread latency worker threads async await'),\nQ('Node','Quando usar Worker Threads e quando usar uma fila?','Worker Threads servem para paralelismo de CPU dentro do processo; fila desacopla o trabalho, permite processamento posterior, retry e distribuição entre múltiplas instâncias.','Se preciso resposta ainda no ciclo da requisição e o cálculo pode ser paralelizado localmente, Worker Thread pode fazer sentido. Se o trabalho pode ser assíncrono, longo, precisa retry, durabilidade ou escala independente, fila costuma ser melhor.','worker threads fila queue cpu bound parallelism retry distributed jobs'),\n"""

s = s[:idx] + extras + s[idx:]

# Improve discoverability in hot terms when the array is present.
s = s.replace("'event loop','Event-Driven','DDD'", "'event loop','concorrência','CPU-bound','Event-Driven','DDD'", 1)

p.write_text(s, encoding='utf-8')
print('V4.4 concurrency cards applied')
