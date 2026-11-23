# AcervoLab Academy — Registro oficial de progresso

**Atualização:** 2026-11-23  
**Status global:** FORMAÇÃO INICIADA (ACV-101/T01) / IMPLEMENTAÇÃO NÃO INICIADA  
**Repositório:** `lucastrevvos/software-mastery-roadmap`  
**Trilha:** `docs/acervolab/`

## O que foi decidido

- Projeto: **AcervoLab**, gestão de equipamentos, empréstimos, devoluções, reservas e filas de espera.
- Objetivo: usar um software de produto simples para percorrer engenharia de software, computação, .NET, POO, SOLID, GoF, dados, testes, web, segurança, cloud, arquitetura, sistemas distribuídos e Engenharia de IA.
- Grade: **6 semestres, 25 disciplinas, 312 tópicos**; ordem didática, não obrigatória, acesso livre a todo o conteúdo.
- Primeira versão: **Console em C#**, sem banco, APIs, infraestrutura ou IA. Em seguida evoluir por problemas demonstráveis.
- IA: conceitos precursores nas disciplinas de base; ML, dados e RAG no 5º semestre; agentes, LLMOps, governança e AI em .NET no 6º semestre. Módulo de IA adicional e opcional; regras críticas determinísticas.
- Método: **DECA + Recall → Trace → Rebuild → Repair → Transfer → Retest**. Um desafio/avanço pequeno por vez. Teoria sempre publicada no repositório; progresso somente com evidência.
- **Não** inferir domínio por acerto de múltipla escolha; não bloquear acesso se houver etapas pendentes.
- Cada conceito ensinado entra no `theory.json` (ou atualiza registro existente), via commit. Diário local do navegador é privado e não sincroniza.

## Histórico de conceitos já apresentados antes da nova trilha

| Conceito | Registro | Evidência | Estado |
| --- | --- | --- | --- |
| Categorias GoF | TH-001 | Conversa: Desafios 001–002 | Apresentado; sem gate |
| Interface e contrato | TH-002 | Exemplos C# didáticos | Apresentado; sem gate |
| Polimorfismo | TH-003 | Desafios 003–004, respostas B | Apresentado; sem gate |
| Strategy | TH-004 | Exemplos de pagamento e algoritmos | Apresentado; sem gate |
| Adapter | TH-005 | Desafio 002, resposta B | Apresentado; sem gate |
| OCP | TH-006 | Desafios 005–006, respostas B | Apresentado; sem gate |
| DIP | TH-007 | Desafios 006–008, respostas B | Apresentado; sem gate |
| Injeção de dependência | TH-008 | Desafio 007, resposta B | Apresentado; sem gate |
| Acoplamento | TH-009 | Desafio 008, resposta B | Apresentado; sem gate |
| Coesão | TH-010 | Desafio 009, resposta A | Apresentado; sem gate |
| SRP | TH-011 | Desafios 009–010, resposta B no 010 | Apresentado; sem gate |
| Strategy vs. SRP | TH-012 | Desafio 011 proposto, **ainda sem resposta nesta trilha** | Pendente de verificação |

**Nota pedagógica:** as respostas foram dadas sem raciocínio escrito; não são evidência suficiente de domínio independente. Os conceitos estão disponíveis na biblioteca para retest durante a formação.

## Aula em andamento e próximo passo

**ACV-101 / Engenharia de requisitos e produto / T01 — Problema e atores.**

- **2026-11-23 — Aula 001 iniciada:** problema inicial da escola com equipamentos (conflitos de reservas, atrasos, rastreabilidade); atores potenciais: professor/solicitante e responsável pelo acervo. Conceito teórico registrado como **TH-013**.
- **2026-11-23 — Desafio ACV-101-001:** resposta **B (professor)** correta; raciocínio não informado. Evidência de identificação de ator humano em uma questão de múltipla escolha, **não** suficiente para domínio ou conclusão do tópico.
- **2026-11-23 — Verificação ACV-101-002:** resposta **A (sistema externo pode ser ator)** correta; raciocínio não informado. Duas respostas corretas de múltipla escolha indicam reconhecimento de atores humanos e não humanos, **sem comprovar domínio independente**.
- **Próximo passo ACV-101-003:** aplicar o novo conceito **objetivo do ator** (TH-014) em resposta aberta, distinguindo resultado desejado de decisão de interface/tecnologia.
- **Evidência até agora:** teoria TH-013 e TH-014 versionada, duas respostas corretas; **sem justificativa própria, prática ou mastery gate validado**.
- **Depois:** definir escopo mínimo, primeira invariante e critérios de aceitação com um passo por vez.
- Ainda **não** criar projeto .NET nem infraestrutura: primeiro formular o problema.

## Gates e marcos

| Marco | Estado | Evidência |
| --- | --- | --- |
| Grade e protocolo acadêmico | Planejado/documentado | `docs/acervolab/curriculum.json`, `README.md` |
| v0.1 Console e testes | Não iniciado | — |
| v0.2 Modelagem e refatoração | Não iniciado | — |
| v1.0 API + PostgreSQL + Web | Não iniciado | — |
| v1.5 Cloud + CI/CD + observabilidade | Não iniciado | — |
| v2.0 eventos + IA experimental | Não iniciado | — |
| v3.0 IA em produção + defesa | Não iniciado | — |

## Instrução de continuidade

Ao retomar, consultar este arquivo, `README.md`, `curriculum.json` e `theory.json`; manter a ordem e os gates sem apresentar como realizado o que é apenas planejado. Atualizar este registro por commit após evidências reais. Não depender exclusivamente da memória de conversa.
