# Programming Mastery Lab — Protocol

## 1. Objetivo

Transformar cada avanço de curso em habilidade demonstrável, reduzindo reconhecimento passivo e dependência de solução pronta.

## 2. Gatilho

Quando um novo avanço for informado no chat:

1. atualizar `docs/data/progress.json`;
2. identificar conceitos novos e competências impactadas;
3. atualizar `docs/data/mastery.json` apenas com evidência real;
4. decidir se é necessário Recall, Lab, Review ou Mastery Gate;
5. adicionar revisão futura quando houver conteúdo que precise ser retido.

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

## 4. Mastery Scale

- 0 — desconhecido/não avaliado
- 1 — reconhece
- 2 — explica
- 3 — executa com ajuda
- 4 — executa sozinho
- 5 — depura
- 6 — transfere para problema novo
- 7 — retido após revisões espaçadas

Um nível pode ser marcado como `provisional` quando houver evidência de curso/projeto, mas ainda faltar um gate independente.

## 5. Error Ledger

Entradas em `docs/data/error-ledger.json` devem registrar:

- competência;
- erro observado;
- contexto/lab;
- causa provável ou modelo mental incorreto;
- correção esperada;
- status `open`, `corrected` ou `retained`;
- evidência de correção/retenção.

Erro isolado de digitação não precisa virar entrada. Padrões conceituais, bugs de lógica e decisões de engenharia recorrentes precisam.

## 6. Revisões espaçadas

Protocolo inicial: D+1, D+3, D+7, D+14, D+30 e D+60 após um gate aprovado. O espaçamento pode mudar conforme desempenho real.

## 7. Learning Mode

Antes da primeira tentativa do aluno, a IA não deve entregar a solução completa.

Permitido:

- esclarecer requisito;
- fazer perguntas;
- fornecer pistas graduais;
- criar casos de teste;
- indicar categoria de erro;
- revisar raciocínio e código;
- mostrar solução completa depois que o esforço cognitivo alvo já ocorreu.

## 8. Production Mode

Em projetos de produção, produtividade tem prioridade: IA, Codex, documentação, autocomplete, bibliotecas e ferramentas externas podem ser usados livremente, salvo restrições específicas do projeto.

## 9. Ciclo Git

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

## 10. Regra de ouro

**Memória para fundamentos. Modelos mentais para mecanismos. Prática para padrões. Documentação para detalhes.**
