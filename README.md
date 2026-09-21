# Software Mastery Roadmap

Repositório oficial da formação **Full Stack Software Architect & Cloud Engineer** e do **Programming Mastery Lab**.

Este repositório é a fonte da verdade para quatro coisas diferentes:

1. **Roadmap** — o que estudar e em qual ordem.
2. **Progress** — o que foi iniciado/concluído nos cursos.
3. **Mastery** — o que realmente consegue ser explicado, construído, depurado e transferido sem ajuda.
4. **Retention** — o que continua disponível na memória depois de dias/semanas.
5. **Método Especial JCI** — como combinar profundidade japonesa, treino deliberado chinês e pragmatismo indiano em cada etapa relevante.

> Curso concluído não significa domínio. Certificado é evidência externa; Mastery Gate é evidência interna.

## Estado atual

- **CS50x:** concluído em 17/09/2026 — certificado oficial: https://certificates.cs50.io/45c5bcfe-b8cc-4aac-ad26-96b3f4824997.pdf?size=letter. Final Project: **LifeBoard** — https://github.com/lucastrevvos/lifeboard · demo: https://youtu.be/9Tg2Lx1C2bk.
- **freeCodeCamp JavaScript Certification:** em andamento e agora é a **trilha principal ativa**. Posição registrada: Variables and Strings; próximo exercício: Build a Sentence Maker.
- **CS50's Introduction to Databases with SQL:** em andamento em paralelo desde 18/09/2026; etapa atual: Week 0 — Querying — https://cs50.harvard.edu/sql/weeks/0/.
- **Foundational C# with Microsoft:** não iniciado e intencionalmente adiado para a segunda grande janela de backend, depois da consolidação Node/Nest + Full Stack Open + profundidade de backend.
- **Programming Mastery Lab:** ativo em modo de checkpoints cumulativos. A conclusão do CS50x registra progresso externo, mas não promove automaticamente competências para Mastery 7.
- **Engineering Impact:** trilha transversal ativa para transformar maturidade técnica em projetos, documentação, open source e contribuição pública quando fizer sentido.
- **Método Especial JCI:** camada transversal ativa; Japão = profundidade, China = treino deliberado, Índia = aplicação/empregabilidade. Ver [JCI_METHOD.md](JCI_METHOD.md).


## Estratégia de execução — Employment First

O roadmap é executado em **janelas de imersão**, não como uma lista de tecnologias estudadas em paralelo.

Regra operacional:

- no máximo **2 cursos ativos** ao mesmo tempo;
- **1 principal** (~70–80% do esforço);
- **1 complementar** (~20–30%);
- uma nova stack só abre quando a janela anterior atingiu um ponto claro de uso profissional.

Ordem estratégica atual:

1. **JavaScript + SQL** — fechar os fundamentos ativos.
2. **Node.js + NestJS** — atingir empregabilidade real como backend TypeScript.
3. **Full Stack Open + React** — ampliar candidaturas para full stack sem abandonar a identidade backend.
4. **Backend Senior Depth** — Linux, networking, Nest avançado, DDD, arquitetura, sistemas distribuídos, observabilidade e AWS.
5. **AI-Enabled Backend** — Python just-in-time, LLM apps, RAG, agentes e LLMOps.
6. **C#/.NET + Azure** — segunda grande janela de backend, reaplicando conceitos já dominados.
7. **Frontend Specialization** — Next.js e Angular com profundidade.
8. **AI/Data/Security avançados + Capstone** — especialização e credenciais de longo prazo.

> Empregabilidade Gate #1: **KM One** será o projeto backend real em Node.js + TypeScript + NestJS, com PostgreSQL/Neon e deploy na Azure. Ao concluir um backend profissional e defensável tecnicamente, iniciar candidaturas para vagas Node.js/TypeScript/NestJS sem esperar cloud ou arquitetura avançadas. Decisão detalhada em [projects/KM_ONE_NODE_NEST_GATE.md](projects/KM_ONE_NODE_NEST_GATE.md).

> Empregabilidade Gate #2: após o Full Stack Open, ampliar candidaturas para posições Node/React/TypeScript Full Stack.


## Método do laboratório

Todo conhecimento importante pode passar por seis provas:

**Recall → Reason/Trace → Rebuild → Repair → Remix/Transfer → Retest**

A escala de domínio é:

- `0` desconhecido
- `1` reconhece
- `2` explica
- `3` executa com ajuda
- `4` executa sozinho
- `5` depura
- `6` transfere para problema novo
- `7` retido após revisões espaçadas

### Learning Mode

Durante laboratórios de aprendizagem, IA não entrega a solução completa antes da tentativa do aluno. Ela pode dar pistas, criar testes, revisar raciocínio, apontar classes de erro e elevar/reduzir dificuldade.

### Production Mode

Em trabalho real, vale usar ChatGPT, Codex, autocomplete, documentação e demais ferramentas para produtividade máxima.

## Método Especial JCI

O Mastery Lab é reforçado pelo **JCI — Japão, China e Índia**:

- **Japão:** primeiros princípios, mecanismos por baixo das abstrações, implementação e explicação;
- **China:** repetição progressiva, Error Ledger, variações, reteste e sessões cronometradas quando apropriado;
- **Índia:** DSA, Core CS, entrevistas, system design e aplicação prática.

Plataformas prioritárias: **Aizu Online Judge, AtCoder, Luogu, Nowcoder e CodeChef**. **NPTEL/IIT/SWAYAM** entra como aprofundamento universitário sob demanda, não como segunda grade curricular. Detalhes e política anti-inchaço em [JCI_METHOD.md](JCI_METHOD.md).

## Ciclo de trabalho

1. Lucas informa no chat um avanço real de curso.
2. O progresso é atualizado em `docs/data/progress.json`.
3. O conteúdo estudado é convertido em competências em `docs/data/mastery.json`.
4. Quando necessário, nasce um laboratório em `labs/` ou um Mastery Gate em `mastery-gates/`.
5. O [Método Especial JCI](JCI_METHOD.md) decide se o tópico merece profundidade extra, treino externo, reteste cronometrado ou aplicação profissional — sem duplicar cursos por burocracia.
6. Tópicos maduros são avaliados pela trilha [Engineering Impact](ENGINEERING_IMPACT.md): estudo apenas, projeto, artigo, open source, contribuição comunitária ou palestra.
7. Lucas executa localmente, faz commit e push.
8. O código é revisado no GitHub.
9. Erros conceituais recorrentes entram em `docs/data/error-ledger.json`.
10. Revisões futuras entram em `docs/data/reviews.json`.
11. Só após retenção e transferência o tópico chega a Mastery 7.

## Estrutura

```text
software-mastery-roadmap/
├── README.md
├── docs/                  # GitHub Pages / dashboard
│   ├── index.html
│   ├── css/app.css
│   ├── js/app.js
│   └── data/
├── labs/                  # exercícios implementados localmente
├── mastery-gates/         # provas de domínio
├── reviews/               # revisões espaçadas
└── projects/              # projetos integradores
```

## Regra de ouro

**Memória para fundamentos. Modelos mentais para mecanismos. Prática para padrões. Documentação para detalhes.**

---

Atualizado continuamente conforme o avanço real nos cursos e nos laboratórios.