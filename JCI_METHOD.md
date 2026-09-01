# Método Especial JCI — Japão, China e Índia

Camada transversal do **Software Mastery Roadmap** para combinar profundidade de fundamentos, treino deliberado e empregabilidade sem transformar o roadmap em uma coleção infinita de cursos.

> **Japão para compreender. China para treinar. Índia para transformar domínio em capacidade profissional.**

O JCI não substitui a ordem principal do roadmap, o Programming Mastery Lab, o Velocity Mode nem a trilha Engineering Impact. Ele define **como** estudar, praticar e validar os tópicos relevantes.

## 1. Intenção

O objetivo não é virar competitive programmer nem acumular certificados estrangeiros. É formar um engenheiro capaz de:

- entender mecanismos por baixo das abstrações;
- resolver problemas novos sem depender de tutorial;
- implementar e depurar com independência;
- reconhecer padrões sem decorar soluções;
- fazer escolhas de estrutura de dados, algoritmo e arquitetura com trade-offs;
- usar IA como amplificador sem terceirizar o modelo mental;
- converter fundamentos em sistemas reais, entrevistas, arquitetura e produção.

## 2. Os três pilares

### Japão — profundidade e mecanismo

Pergunta-guia:

> **O que está acontecendo por baixo?**

Aplicação:

- primeiros princípios;
- tracing de execução, memória, estado e fluxo;
- implementação simplificada sem abstrações quando didaticamente útil;
- reconstrução de estruturas e mecanismos;
- explicação sem consulta;
- ligação entre software, runtime, sistema operacional, rede e hardware quando relevante.

Recursos prioritários:

- **Aizu Online Judge (AOJ)** — ITP1 para fundamentos, ALDS1 para algoritmos/estruturas e ITP2 depois;
- **AtCoder** — Beginners Selection e, em marcos posteriores, contests/virtual contests para transferência.

### China — treino deliberado

Pergunta-guia:

> **Consigo reconhecer e resolver isso novamente, inclusive com pressão e variações?**

Aplicação:

- séries curtas de problemas por padrão;
- dificuldade progressiva;
- Error Ledger como registro de falhas conceituais;
- refazer problema sem solução depois de intervalo;
- alternar problema familiar e problema sem tag;
- sessões cronometradas apenas quando o fundamento já estiver compreendido.

Recursos prioritários:

- **Luogu** — listas oficiais por fundamentos, algoritmos e estruturas;
- **Nowcoder** — mais tarde, para coding interviews, Core CS, bancos de questões e preparação profissional.

### Índia — empregabilidade e aplicação

Pergunta-guia:

> **Como esse conhecimento aparece em trabalho, entrevista e engenharia de software?**

Aplicação:

- DSA conectado a entrevistas;
- Core CS conectado a system design;
- implementação conectada a projeto;
- teoria conectada a produção;
- prática em linguagens relevantes para a carreira.

Recursos prioritários:

- **CodeChef** — ginásio principal de DSA/competitive programming, com uso seletivo;
- **NPTEL / IIT / SWAYAM** — aprofundamento universitário sob demanda;
- **GeeksforGeeks** — referência complementar para revisão e interview prep, nunca fonte única de verdade.

## 3. Integração com o Programming Mastery Lab

O método existente continua sendo:

**Recall → Trace → Rebuild → Repair → Transfer → Retest**

O JCI reforça cada prova:

| Prova | JCI dominante | Evidência |
|---|---|---|
| Recall | Japão | explicar conceito e invariantes sem consulta |
| Trace | Japão | prever fluxo, memória, estado, custo e efeitos |
| Rebuild | Japão + China | implementar sem copiar |
| Repair | China | diagnosticar causa, corrigir e registrar padrão |
| Transfer | China + Índia | resolver variação/problema novo e justificar escolha |
| Retest | China | repetir depois sem solução |
| Aplicação/Defense | Índia | conectar a sistema real, entrevista ou decisão de engenharia |

A escala de Mastery 0–7 não muda. JCI melhora a qualidade das evidências usadas para subir de nível.

## 4. Política anti-inchaço

O JCI **não cria uma segunda grade curricular**.

Regras:

1. existe sempre **um curso/trilha principal** por assunto;
2. plataforma de problemas é **ginásio**, não obrigação de concluir catálogo;
3. NPTEL entra apenas quando houver ganho real de profundidade ou lacuna;
4. não repetir um curso inteiro que ensine o que CS50/Microsoft/Helsinki já cobriu bem;
5. não perseguir quantidade bruta de problemas;
6. em Velocity Mode, JCI deve consumir apenas uma fração pequena do tempo, salvo erro recorrente ou gate importante;
7. competitive programming é ferramenta de raciocínio, não objetivo profissional;
8. C++ é opcional; não será adicionada só porque domina competições;
9. problemas serão preferencialmente resolvidos em **C, C#, Python ou JavaScript**, conforme o objetivo didático;
10. qualquer recurso que vire burocracia sem ganho de domínio sai do método.

## 5. Uso das plataformas

### Aizu Online Judge

**Papel:** profundidade estruturada.

- ITP1: somente se houver lacuna de fundamentos;
- ALDS1: principal trilha externa para DSA básico;
- ITP2: depois, para técnicas e biblioteca padrão;
- bibliotecas de grafos, DP e outros tópicos entram apenas nos estágios correspondentes.

Não fazer tudo por obrigação. Selecionar problemas que comprovem o tópico recém-estudado.

### AtCoder

**Papel:** transferência e pressão controlada.

Progressão:

1. practice contest;
2. AtCoder Beginners Selection;
3. problemas A/B de Beginner Contests;
4. virtual contest curto;
5. milestones de rating/contest somente se continuarem produzindo aprendizado útil.

### Luogu

**Papel:** volume deliberado e listas por padrão.

Usar listas de fundamentos/algoritmos de forma seletiva para:

- consolidar padrão;
- variar enunciado;
- aumentar dificuldade;
- retestar erro do Error Ledger.

O idioma não é barreira: tradução do navegador é aceitável porque o alvo é raciocínio algorítmico.

### Nowcoder

**Papel:** empregabilidade.

Entra principalmente quando o roadmap chegar a:

- DSA de entrevista;
- sistemas operacionais;
- redes;
- bancos de dados;
- concorrência;
- perguntas de linguagem/runtime;
- mock interviews e questões de empresas.

Não é prioridade durante a base inicial do CS50.

### CodeChef

**Papel:** ginásio DSA orientado a carreira.

Uso recomendado:

- após **Foundational C#**, aproveitar a trilha C# + Beginner DSA para praticar a linguagem principal de backend;
- após **CS50P**, usar o roadmap geral de DSA/Competitive Programming dentro do Algorithm Gym;
- selecionar séries de problemas, não concluir centenas apenas por contador.

### NPTEL / IIT / SWAYAM

**Papel:** universidade paralela sob demanda.

Prioridades:

- **Data Structures and Algorithms — IIT Delhi**: aprofundamento de estruturas/algoritmos;
- **Programming, Data Structures and Algorithms Using Python**: opcional; útil como referência, mas sobrepõe CS50P;
- **Getting Started with Competitive Programming — IIT Gandhinagar**: excelente follow-up depois da base de DSA;
- cursos de OS, redes, bancos, sistemas distribuídos, segurança e IA podem ser usados mais tarde como deep dives.

Regra: assistir aula selecionada ou módulo específico é totalmente válido. Certificado NPTEL só entra se tiver ROI; o conteúdo vale mais que o badge para este roadmap.

## 6. Integração por fase

### Fase atual — CS50x

Prioridade absoluta: exercícios oficiais do CS50.

Quando um bloco importante fechar:

- usar AOJ/ALDS1 em pequena dose para estruturas estudadas;
- aplicar Trace/Rebuild/Repair;
- abrir Error Ledger apenas para falhas conceituais reais.

**Week 5 — Data Structures:** após os exercícios oficiais, selecionar aproximadamente 3–5 problemas externos ligados a estruturas, busca, hashing/árvores quando compatíveis. Não iniciar um curso paralelo completo.

### Foundational C#

- praticar implementação das estruturas já conhecidas em C#;
- CodeChef C# + Beginner DSA passa a ser fonte de exercícios;
- comparar comportamento de arrays, collections, generics, value/reference semantics e runtime com os modelos mentais construídos em C.

### CS50P concluído — início formal do Algorithm Gym

Combinar:

- AOJ ALDS1;
- CodeChef DSA;
- AtCoder Beginners Selection;
- Luogu seletivo;
- NPTEL Competitive Programming como aprofundamento opcional.

O ginásio progride por evidência de domínio, não por quantidade de questões.

### Core CS / Backend / Arquitetura

O JCI deixa de ser predominantemente algoritmo e passa a incluir:

- implementação de mecanismos;
- labs de concorrência;
- banco e índices;
- redes e protocolos;
- cache, filas, retries, idempotência;
- profiling;
- falhas controladas;
- system design;
- Nowcoder para recuperação de Core CS e entrevistas;
- NPTEL para aprofundamento acadêmico seletivo.

### Cloud / Sistemas Distribuídos / AI Engineering

A mesma filosofia continua:

- Japão: entender mecanismo e abstração;
- China: drills de falhas, incidentes e troubleshooting;
- Índia: aplicação, entrevista, arquitetura e produção.

Aqui, resolver mais puzzles algorítmicos não substitui laboratório de sistema real.

## 7. Gate JCI de domínio

Um tópico relevante pode receber evidência JCI quando o aluno consegue, conforme aplicável:

1. **Explain** — explicar sem consulta;
2. **Trace** — prever comportamento;
3. **Build** — implementar sozinho;
4. **Debug** — encontrar causa de falha;
5. **Analyze** — justificar complexidade/custo;
6. **Transfer** — resolver variação nova;
7. **Retain** — repetir depois de intervalo;
8. **Defend** — explicar por que escolheu uma solução e por que rejeitou alternativas.

Não é necessário executar os oito itens em todo assunto. O gate é proporcional à importância e ao tipo de competência.

## 8. Métrica correta

Não medir:

- vídeos assistidos;
- horas acumuladas;
- número bruto de exercícios;
- certificados sem evidência prática.

Medir:

- redução de pistas necessárias;
- qualidade das hipóteses ao depurar;
- taxa de transferência para problemas sem tag;
- capacidade de explicar mecanismos;
- retenção;
- decisões técnicas justificadas;
- aplicação em projetos e produção.

## 9. Relação com Engineering Impact

JCI gera competência; **Engineering Impact decide quando essa competência merece virar evidência pública**.

Um exercício de árvore normalmente é Study only.

Já uma investigação de performance, runtime, arquitetura, observabilidade ou uma ferramenta reutilizável pode virar:

**Project → Article → Open source → Community contribution → Talk**

A publicação é consequência de algo tecnicamente útil, não uma meta de volume.
