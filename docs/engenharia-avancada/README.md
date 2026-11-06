# Engenharia de Software Avançada

**5 módulos · 40 semanas · 12–16 h/semana · 480–640 horas planejadas**

[Abrir painel interativo no GitHub Pages](https://lucastrevvos.github.io/software-mastery-roadmap/engenharia-avancada/) · [Voltar ao roadmap principal](../index.html) · [Currículo completo em JSON](data.json)

## Objetivo

Formar competência verificável de engenharia e arquitetura de software de alto nível: entender mecanismos, construir código correto, projetar fronteiras e operar software em falhas reais. Esta trilha é independente das trilhas Mobile/Physical AI e demais cursos existentes.

## Mapa do curso

| Módulo | Semanas | Competência | Projeto |
|---|---:|---|---|
| 1. Fundação de Código, Algoritmos e Testes | 1–8 | Correção, custo computacional, design e testes | Motor de preço e matching em memória |
| 2. Engenharia de Dados, Concorrência e Internos de SGBDs | 9–16 | MVCC, transações, locks, isolamento, query planning | Reservas concorrentes PostgreSQL/Oracle |
| 3. Design de Software, Clean Architecture e DDD | 17–24 | Bounded contexts, aggregates, modularidade, ADRs | ServiceOps Modular Monolith |
| 4. Sistemas Distribuídos, Microsserviços e EDA | 25–32 | Mensageria, falha parcial, Outbox/Inbox, Saga | Billing Service e orquestração distribuída |
| 5. Infraestrutura, Observabilidade e Cloud | 33–40 | CI/CD, containers, Kubernetes, cloud e SRE | Ambiente operável com recuperação de incidentes |

## Como usar a aba

1. Selecione o módulo e abra uma semana para consultar teoria, laboratório e evidências exigidas.
2. Marque **Estudando** ao iniciar. Somente selecione **Comprovado** quando houver código/testes/experimentos verificáveis; a interface requer campo de evidência preenchido.
3. Ao terminar cada checkpoint, registre evidências dos critérios de aceite e marque **Validado**.
4. Consulte a seção **Avaliação e comprovação** para a escala 0–4. Nível 3 exige autonomia; nível 4 exige transferência para problemas novos.
5. Use **Exportar progresso JSON** para backup e **Importar progresso JSON** para transferir entre navegadores. Estes controles não modificam o repositório GitHub.
6. As sessões conduzidas pela mentoria podem atualizar o arquivo versionado `coaching-progress.json`. O painel lê esses avanços ao carregar e preserva status locais mais avançados. **Iniciar uma aula não significa comprovar domínio.** A sincronização GitHub → navegador não envia modificações do navegador de volta ao repositório.

As oito semanas de cada módulo são uma estimativa. **Checkpoints são bloqueantes**: não avance por calendário ignorando falhas críticas. As percentagens da tela refletem *semanas marcadas como comprovadas com evidência*; não são uma certificação automática.

## Projeto integrador — ServiceOps

Plataforma fictícia para operações de serviços: pedidos, profissionais, preços, disponibilidade, alocação, reservas, faturamento simulado e notificações. O produto evolui por necessidades justificadas, não pela quantidade de frameworks.

Princípios:

- Começar com algoritmos em memória e testes de invariantes antes de persistência.
- Garantir consistência transacional com constraints e experimentos concorrentes.
- Preferir monólito modular inicialmente; extrair Billing quando o módulo 4 exigir falhas independentes.
- Mensagens são potencialmente duplicadas; garantir idempotência e reconciliação.
- Demonstrar deploy, observabilidade e restauração, não apenas produzir diagramas.

## Estrutura dos arquivos

- `index.html`: interface da nova aba, vinculada ao roadmap principal.
- `data.json`: **fonte da verdade** do currículo (objetivos, 40 semanas, termos, requisitos dos projetos, critérios de aceite, checkpoints e leituras).
- `coaching-progress.json`: estado versionado da mentoria, com semanas em andamento e evidências validadas.
- `aulas/`: materiais e desafios de cada encontro, publicados conforme o avanço.
- `app.js`: navegação, acompanhamento, validação de evidência e exportação/importação local.
- `styles.css`: apresentação responsiva em padrão visual compatível com o repositório.
- `README.md`: este manual.

Para editar o programa, modifique `data.json`, não o HTML. Mantenha `schemaVersion` e IDs estáveis para preservar compatibilidade do progresso exportado.

## Segurança, privacidade e limites

O progresso pessoal é armazenado em `localStorage` sob a chave `advanced-engineering-roadmap-progress-v1`; nada é enviado ao servidor. **Não coloque dados pessoais, senhas, tokens ou URLs privadas de sistemas** no campo de evidências, principalmente ao compartilhar um backup JSON.

A conclusão da trilha não substitui vivência de produção nem promete cargo ou certificação de mercado. Ela fornece evidências concretas e auditáveis de competência.

## Metas do desafio final

Quatro cenários não anunciados, cobrindo mudança de regra de negócio, conflito de concorrência, falha distribuída e degradação operacional. A avaliação deve incluir diagnóstico, patch, testes de regressão, explicação causal e riscos remanescentes.

*Bons sistemas são julgados pelo comportamento sob carga, concorrência e falhas, não pela quantidade de padrões arquiteturais presentes.*
