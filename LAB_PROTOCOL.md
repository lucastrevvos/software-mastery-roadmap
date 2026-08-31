# Programming Mastery Lab — Protocol

## 1. Objetivo

Transformar cada avanço de curso em habilidade demonstrável, reduzindo reconhecimento passivo e dependência de solução pronta, sem transformar o sistema de mastery em uma segunda grade curricular que atrase desnecessariamente certificações e trilhas oficiais.

## 2. Gatilho

Quando um novo avanço for informado no chat:

1. atualizar `docs/data/progress.json`;
2. identificar conceitos novos e competências impactadas;
3. atualizar `docs/data/mastery.json` apenas com evidência real;
4. decidir se é necessário Recall, Lab, Review ou Mastery Gate;
5. adicionar revisão futura apenas quando houver conteúdo conceitual relevante, erro observado ou fundamento transferível que precise ser retido.

## 3. Tipos de atividade

### Recall
Perguntas sem consulta para recuperar conhecimento anterior.

### Trace
Prever fluxo, estado, saída e comportamento antes de executar.

### Rebuild
Reconstruir uma solução sem copiar o exemplo original.

### Repair
Diagnosticar e corrigir código quebrado a partir de hipóteses.

### Transfer
Aplicar o mesmo princípio em um problema diferente.

### Retest
Reavaliar depois de um intervalo para medir retenção.

## 4. Velocity Mode — certificações e cursos longos

Quando a prioridade operacional for concluir uma certificação ou curso oficial sem sacrificar aprendizado real, usar **Velocity Mode**.

Regras:

- os exercícios oficiais do curso são a prática principal;
- não criar automaticamente um lab completo após cada aula, semana ou problem set;
- registrar erros conceituais reais observados durante os exercícios oficiais;
- fazer micro-retrievals curtos e seletivos quando necessário, preferindo 5–15 minutos;
- consolidar várias semanas em checkpoints cumulativos em vez de duplicar cada bloco do curso;
- preservar labs completos já preparados para um checkpoint maior ou para o sprint de mastery pós-curso;
- priorizar fundamentos transferíveis entre linguagens e sistemas, e não memorização de sintaxe específica sem utilidade provável;
- se um erro reaparecer, ele volta para a fila de Repair/Retest mesmo em Velocity Mode.

Para CS50, a lógica, os modelos mentais, algoritmos, memória, estruturas de dados, debugging e representação computacional têm prioridade de retenção. Sintaxe específica de C deve ser retida apenas no nível necessário para compreender esses mecanismos e resolver os problemas do curso.

## 5. Mastery Scale

- 0 — desconhecido/não avaliado
- 1 — reconhece
- 2 — explica
- 3 — executa com ajuda
- 4 — executa sozinho
- 5 — depura
- 6 — transfere para problema novo
- 7 — retido após revisões espaçadas

Um nível pode ser marcado como `provisional` quando houver evidência de curso/projeto, mas ainda faltar um gate independente.

## 6. Error Ledger

Entradas em `docs/data/error-ledger.json` devem registrar:

- competência;
- erro observado;
- contexto/lab;
- causa provável ou modelo mental incorreto;
- correção esperada;
- status `open`, `corrected` ou `retained`;
- evidência de correção/retenção.

Erro isolado de digitação não precisa virar entrada. Padrões conceituais, bugs de lógica e decisões de engenharia recorrentes precisam.

Em Velocity Mode, o Error Ledger é o principal mecanismo para decidir o que merece treino extra. Não retestar conteúdo que já foi demonstrado de forma sólida apenas para cumprir calendário.

## 7. Revisões espaçadas

Protocolo completo de referência: D+1, D+3, D+7, D+14, D+30 e D+60 após um gate aprovado.

Em Velocity Mode, esses intervalos não precisam gerar uma atividade separada para cada lab. Revisões podem ser agrupadas em checkpoints cumulativos e devem priorizar erros prévios e fundamentos transferíveis. O espaçamento é guiado por desempenho real, não por burocracia de calendário.

## 8. Learning Mode

Antes da primeira tentativa do aluno, a IA não deve entregar a solução completa.

Permitido:

- esclarecer requisito;
- fazer perguntas;
- fornecer pistas graduais;
- criar casos de teste;
- indicar categoria de erro;
- revisar raciocínio e código;
- mostrar solução completa depois que o esforço cognitivo alvo já ocorreu.

## 9. Production Mode

Em projetos de produção, produtividade tem prioridade: IA, Codex, documentação, autocomplete, bibliotecas e ferramentas externas podem ser usados livremente, salvo restrições específicas do projeto.

## 10. Ciclo Git

Para labs completos e checkpoints formais:

1. `git pull`
2. executar o laboratório localmente
3. testar
4. `git add .`
5. commit descritivo
6. `git push`
7. informar no chat o ID do laboratório
8. revisão no GitHub
9. corrigir e repetir se necessário
10. atualizar mastery, reviews e error ledger após a avaliação

Micro-retrievals feitos durante Velocity Mode podem ocorrer diretamente no chat e só precisam virar artefato Git quando gerarem nova evidência relevante, erro recorrente ou decisão de mastery.

## 11. Regra de ouro

**Memória para fundamentos. Modelos mentais para mecanismos. Prática para padrões. Documentação para detalhes.**


## 12. Algorithm Gym — prática progressiva de resolução de problemas

Depois do CS50P, iniciar um bloco explícito de prática algorítmica progressiva. O objetivo não é memorizar soluções nem depender de enunciados que indiquem a técnica, mas desenvolver capacidade de decompor problemas novos, reconhecer padrões, escolher estruturas de dados, implementar, analisar custo e adaptar a solução quando as regras mudarem.

### Progressão por níveis

1. loops, condições, contadores, min/max e strings;
2. arrays/lists, frequência, two pointers e sliding window;
3. hash tables, sets, stacks e queues;
4. sorting, binary search e recursion;
5. linked lists, trees e BSTs;
6. graphs, BFS e DFS;
7. greedy, backtracking e divide and conquer;
8. dynamic programming;
9. problemas mistos sem indicar previamente a técnica;
10. problemas de engenharia com dados grandes, memória, concorrência, banco, latência, caching, filas e distribuição.

### Ciclo de cada problema

problema → decomposição → reconhecimento de padrão → pseudocódigo → implementação → análise de Big O → variação de requisito → adaptação/transferência.

### Regras de progressão

- não subir de nível por quantidade bruta de exercícios;
- exigir evidência de Explain, Trace, Build, Debug e Transfer;
- alternar linguagens quando isso ajudar a separar algoritmo de sintaxe, especialmente Python, C# e JavaScript;
- problemas avançados devem deixar de indicar a técnica esperada;
- usar gates cumulativos para provar independência de solução pronta;
- o objetivo final é resolver problemas novos com método, não fazer qualquer algoritmo de memória.

O bloco deve ser formalizado no roadmap principal quando o CS50P for concluído, preservando a prioridade atual de concluir a base do CS50 sem inflar a carga paralela.
