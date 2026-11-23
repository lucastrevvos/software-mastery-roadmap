# AcervoLab Academy — Programa de formação em Engenharia de Software e IA

> **Fonte da verdade permanente:** este diretório do repositório `lucastrevvos/software-mastery-roadmap`.
> **Painel:** https://lucastrevvos.github.io/software-mastery-roadmap/acervolab/
> **Início oficial:** 23/11/2026. **Estado:** currículo planejado, ainda sem laboratório executado.
> Trilha acadêmica autônoma e não credenciada. A organização em semestres é didática, não um compromisso de calendário.

## Objetivo

Usar **um único sistema pequeno**, o **AcervoLab** (empréstimos e reservas de equipamentos), para ensinar e praticar desde fundamentos de computação e C# até arquitetura de software, bancos, web, segurança, produção, cloud e Engenharia de IA. O objetivo não é sofisticar o produto: é criar necessidades reais que motivem conceitos e decisões de engenharia.

### Invariantes de negócio

1. Um equipamento não pode ter dois empréstimos ativos simultâneos.
2. Uma reserva obedece à política de fila/prioridade definida, verificável e auditável.
3. Não se empresta equipamento indisponível; validações pertencem ao domínio, não só à UI.
4. Um empréstimo exige usuário/equipamento válidos, prazo e identificador estável.
5. Devolução não pode ocorrer duas vezes criando efeitos duplicados.
6. Um usuário bloqueado por atraso não realiza empréstimo sem política explícita.
7. Regras evoluem sem perda de integridade ou histórico.
8. Notificações e IA não são fontes autoritativas para alterar o estado de empréstimos.

### Versão inicial (v0.1)

Aplicativo Console em memória com cadastro/listagem de equipamentos, empréstimo, devolução e proteção contra duplicidade; testes unitários das regras. **Sem banco, web, container, cloud, IA ou camadas artificiais no início.**

## Plano curricular

O arquivo [curriculum.json](curriculum.json) é a fonte estruturada que alimenta a aba. Contém **6 semestres, 25 disciplinas e 312 tópicos** e explicita objetivos, práticas, gates e marcos. Progresso não bloqueia acesso.

| Semestre | Ênfase | Marco |
| --- | --- | --- |
| 1 | Requisitos, C#, runtime, estruturas de dados, algoritmos, Git | v0.1 Console |
| 2 | POO, SOLID, Design Patterns, TDD, revisão | v0.2 Domínio testável |
| 3 | PostgreSQL, SQL, EF Core, ASP.NET Core, web, segurança | v1.0 API e frontend |
| 4 | Linux, redes, Docker, cloud, DevOps, observabilidade, concorrência, DDD | v1.5 Monólito modular publicado |
| 5 | Distribuídos e eventos; matemática, estatística, Python, ML, embeddings, LLM e RAG | v2.0 Eventos confiáveis e IA experimental |
| 6 | Agentes, ferramentas, MCP, LLMOps, avaliação, segurança, governança, IA em .NET, defesa | v3.0 IA em produção e defesa técnica |

### Engenharia de IA: integração incremental

- **Fundamento:** algoritmos, estruturas, estatística, software, HTTP, identidade, segurança, banco e experimentação.
- **ML engineering:** dados sintéticos, limpeza, treino/validação/teste, vazamento, modelos-base, métricas, pipelines, deploy e drift.
- **GenAI & LLM engineering:** tokens, contexto, embeddings, structured outputs, tool calling, seleção de modelo, busca, RAG, reranking, grounding, avaliação, desempenho e custos.
- **Agent engineering:** workflow versus autonomia, orquestração, contratos e permissões de ferramentas, MCP, memória, execução segura, human-in-the-loop, idempotência e observabilidade.
- **LLMOps & AI platform:** testes de qualidade e regressão, golden datasets, tracing, CI/CD de prompts e modelos, métricas, segurança, governança, versionamento e fallback.
- **Arquitetura .NET + IA:** módulo de IA integrado à API, providers substituíveis, orquestração assíncrona, contratos tipados, segredos, limites de custo e operação em produção.
- **Pesquisa sob demanda:** multimodalidade, vision/OCR, modelos locais, inferência, quantização, fine-tuning (LoRA), PyTorch e treinamento de deep learning podem ser aprofundados em laboratório opcional documentado, sem virar pré-requisito para publicar o sistema.

A IA terá usos **opcionais e verificáveis** no AcervoLab: busca semântica de equipamentos, perguntas sobre política de empréstimo com fontes, análise exploratória de demanda com dados sintéticos, classificação de descrição de avarias, assistente que **propõe** reservas sem executá-las sem autorização. Não usar dados pessoais reais nos testes. Regras de negócio e autorização continuam determinísticas.

## Protocolo de aula — obrigatório para continuar o curso

Em cada interação:

1. **Consultar** este README, [PROGRESS.md](PROGRESS.md), [curriculum.json](curriculum.json) e [theory.json](theory.json). Não assumir conclusões que não estejam documentadas.
2. **Identificar** o próximo conceito na disciplina em estudo e as dúvidas anteriores; manter o Método DECA, um desafio por vez, sem pular fundamentos. A apresentação da teoria pode ser anterior ou posterior ao desafio conforme a didática, sempre explicitando o que foi demonstrado.
3. **Explicar** o mecanismo em linguagem simples, exemplos curtos de C#/.NET ou Python apenas quando apropriados, mostrando o problema que justifica o recurso e uma alternativa.
4. **Implementar** com pequenos incrementos testáveis: Git, testes automatizados, depuração, decisões, eventual ADR; sem criar arquitetura inteira antecipadamente.
5. **Documentar teoria no GitHub**: todo conceito NOVO apresentado deve receber ou atualizar nota em `docs/acervolab/theory.json` (id estável, topicId, categoria, definição, problema, exemplo, armadilha, relações, data e origem). Se já existe, ampliar nota existente e evitar duplicatas. A versão publicada na aba é essa fonte da verdade.
6. **Registrar progresso comprovado**: atualizar `PROGRESS.md` somente mediante evidência verificável: teste, commit, explicação técnica própria, diagnóstico, retest. Respostas corretas em múltipla escolha sem justificativa servem como indício, NÃO como domínio.
7. **Encerrar com um próximo passo** pequeno, considerando o estado e não uma aula inteira automática. O usuário pode selecionar outras disciplinas sem bloqueios.

**Limitação operacional importante:** a página estática **não grava diretamente no GitHub**. A teoria pública só muda quando o assistente efetivamente executar um commit via GitHub em uma conversa futura; jamais afirmar sincronização automática. Evidências e diário digitados no painel ficam somente no navegador (`localStorage`) e podem ser exportados/importados como JSON. Não publicar segredos, dados reais nem o backup privado.

## Mapa de arquivos

- `index.html`: painel público.
- `styles.css`: layout responsivo e acessibilidade.
- `app.js`: leitura da grade/notas e progresso em `localStorage`.
- `curriculum.json`: disciplinas, tópicos, objetivos, milestones e gates.
- `theory.json`: **biblioteca permanente de teoria**, editada via commits; inclui notas anteriores do estudo de SOLID/Strategy.
- `PROGRESS.md`: **estado oficial resumido**, lacunas, marcos e evidências comprovadas.
- `README.md`: contrato didático e decisões de longo prazo.

## Escala de domínio

`Não iniciado → Estudando → Praticado → Validado com evidência`.

**Validado não equivale a domínio irreversível**. Retest após intervalo, mudança de cenário e aplicação autônoma podem confirmar ou revogar domínio. Indicadores do painel representam anotações do navegador, não certificações acadêmicas.

## Política de decisões arquiteturais

Começar com um projeto C# Console e testes. Evoluir para PostgreSQL, API, UI, cloud e AI **somente** diante de objetivos de aprendizagem e problemas documentados. Para decisões relevantes, registrar Contexto → Opções → Consequências → Decisão → Revisão. Nem microservices nem agentes são objetivos obrigatórios; são hipóteses a testar.

## Como retomar em outro chat

Instrução compacta para o assistente: **"Continue a AcervoLab Academy no repositório lucastrevvos/software-mastery-roadmap. Leia docs/acervolab/README.md, PROGRESS.md, curriculum.json e theory.json, mantenha o Método DECA, ensine um conceito por vez, atualize a teoria oficial via commit no GitHub quando aprender algo novo e só marque domínio mediante evidência."**

O trabalho anterior de perguntas de múltipla escolha sobre Design Patterns, polimorfismo e SOLID foi usado para inicializar a biblioteca em `theory.json`. Isso **não** significa que a trilha acadêmica ou o AcervoLab v0.1 já começaram a ser implementados.
