# Mobile Engineering Roadmap

**Android nativo primeiro · Flutter depois · arquitetura, qualidade e produto completo.**

> [Abrir painel interativo](https://lucastrevvos.github.io/software-mastery-roadmap/mobile/) · [Currículo em JSON](data.json) · [Progresso oficial](PROGRESS.md) · [Certificações](CERTIFICACOES.md) · [Portfólio e LinkedIn](CARREIRA_PORTFOLIO.md)

## Missão e ponto de partida

Formar um Mobile Software Engineer capaz de **projetar, desenvolver, testar, publicar, operar e evoluir** aplicativos Android e multiplataforma. Começamos **do zero, sem diagnóstico inicial**. Todos os tópicos da nova trilha começam como não iniciados, mesmo existindo experiência profissional anterior.

A experiência em backend .NET, o aplicativo **Carga Cheia em Flutter** e o **KM One em Android nativo** serão aproveitados como diferenciais e casos práticos. Experiência prévia não significa domínio já validado neste currículo.

**Stack principal:** Kotlin, Android SDK, Jetpack Compose, Coroutines/Flow, Room, Hilt, WorkManager.  
**Secundária:** Dart e Flutter, plugins e integrações nativas.  
**Transversal:** HTTP/REST, Git, Gradle, testes, CI/CD, OWASP MASVS, observabilidade, performance, APIs e backend .NET.

## Cronograma orientativo

| Fase | Duração | Competências centrais | Entrega e gate |
|---|---:|---|---|
| F0 — Fundamentos e ambiente | 2 semanas | Android/iOS, ferramentas, Git, lógica, HTTP/JSON | Hello Mobile compilável, versionado e explicado |
| F1 — Kotlin do básico ao assíncrono | 6 semanas | Sintaxe, null safety, OOP, generics, collections, JUnit, coroutines, Flow | Kotlin Core Lab; certificado JetBrains como meta |
| F2 — Android moderno | 8 semanas | SDK, lifecycle, Compose, state, ViewModel, navegação, rede, Room | Android Engineering Lab v1 |
| F3 — Arquitetura e resiliência | 8 semanas | UDF, MVVM/MVI, DI, offline-first, WorkManager, sincronização, idempotência | Lab v2 com testes de rede e duplicação |
| F4 — Qualidade e produção | 6 semanas | Testes, Actions, release, segurança MASVS, profiling, Android vitals | Pipeline, relatório de performance e checklist de release |
| F5 — Flutter / Dart | 8 semanas | Dart, widgets, state management, plugins, testes, iOS/Android | Flutter Production Lab |
| F6 — Engenharia avançada e carreira | 8 semanas | System design, KMP inicial, IA, ADRs, portfólio, entrevistas | Três cases documentados, artigo e defesa técnica |

**Total:** 46 semanas de referência (~9–12 meses), ajustáveis por disponibilidade e Mastery Gates. Planejamento de 8–10 horas/semana, não promessa de senioridade.

## Método: aprender, comprovar, reter

- **25% teoria:** documentação oficial, fundamentos, mecanismos e notas curtas.
- **55% prática:** código próprio, testes, depuração e projetos.
- **20% validação:** explicações sem consulta, erro induzido, exercício de transferência e reteste.
- **Learning Mode:** primeiro tentar sozinho; IA pode fazer perguntas, dar pistas, revisar e sugerir testes, sem resolver antes da tentativa.
- **Production Mode:** IA e ferramentas podem acelerar a entrega, mas toda alteração exige validação técnica.

**Escala de domínio 0–7:** 0 não iniciado; 1 reconhece; 2 explica; 3 executa com ajuda; 4 executa sozinho; 5 depura; 6 transfere para problema novo; 7 retém após revisões. Fazer revisões espaçadas (inicialmente 1, 7 e 30 dias).

No painel: **Não iniciado → Estudado → Comprovado**. O status Comprovado exige implementação, explicação, debug, aplicação e evidência; **marcar checkbox não transforma alguém em especialista**. Guardar URL de commit, testes ou ADR sempre que possível.

### Mastery Gate de cada fase

**F0:** executar um pequeno programa Kotlin, gerar commits e explicar como compilar e depurar sem copiar tutorial.

**F1:** biblioteca Kotlin com testes e coroutines; resolver variação nova e depurar problema real; ser capaz de explicar null safety e concorrência.

**F2:** app Android com quatro telas, estado de UI, API, persistência Room, acessibilidade e testes; reproduzir build.

**F3:** registrar operação sem rede e sincronizar depois sem duplicar; demonstrar retries, erros, conflitos e testes.

**F4:** build/testes automatizados, revisão básica MASVS, profiling antes/depois e estratégia de publicação/rollback.

**F5:** app Flutter com estado, persistência, testes e integração nativa; comparar escolhas Flutter versus Android nativo.

**F6:** três projetos/cases tecnicamente defendíveis, documentação em inglês, artigo com evidências e simulação de entrevista de arquitetura mobile.

## Fontes oficiais por fase

**F0:** [Android Developers — Get Started](https://developer.android.com/get-started/overview) · [Kotlin Getting Started](https://kotlinlang.org/docs/getting-started.html) · [GitHub Skills](https://skills.github.com/).

**F1:** [Kotlin Docs](https://kotlinlang.org/docs/home.html) · [Kotlin Koans](https://play.kotlinlang.org/koans/overview) · [JetBrains Kotlin Certificate](https://blog.jetbrains.com/kotlin/2026/04/kotlin-professional-certificate-by-jetbrains-now-on-linkedin-learning/).

**F2:** [Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course) · [Compose](https://developer.android.com/develop/ui/compose/documentation) · [Now in Android](https://github.com/android/nowinandroid).

**F3:** [Android Architecture](https://developer.android.com/topic/architecture) · [Offline-first](https://developer.android.com/topic/architecture/data-layer/offline-first) · [WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager).

**F4:** [GitHub Actions](https://docs.github.com/en/actions) · [OWASP MASVS](https://mas.owasp.org/MASVS/) · [Android Vitals](https://developer.android.com/topic/performance/vitals).

**F5:** [Flutter Learn](https://docs.flutter.dev/learn) · [Dart Docs](https://dart.dev/language) · [Flutter Testing](https://docs.flutter.dev/testing/overview).

**F6:** [Android Quality](https://developer.android.com/docs/quality-guidelines) · [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform.html).

## Certificações reais, sem inflar credenciais

| Ordem | Credencial | Natureza e aplicabilidade |
|---|---|---|
| P1 | [Kotlin Professional Certificate by JetBrains](https://www.linkedin.com/learning/paths/kotlin-professional-certificate-by-jetbrains) | Quatro cursos e exame final via LinkedIn Learning; comprova formação Kotlin, não é exame Android SDK |
| P2 | [GitHub Actions Certification (GH-200)](https://learn.microsoft.com/en-us/credentials/certifications/github-actions/) | Exame profissional de CI/CD, útil após construir pipeline mobile |
| Complementar | [Google Play Store Listing Certificate](https://playacademy.withgoogle.com/intl/pt-BR/certificate/) | Distribuição, ficha e aquisição; **não é certificação de programação Android** |
| Opcional | [AWS Certified Developer – Associate](https://aws.amazon.com/certification/certified-developer-associate/) | Cloud/backend; preparar versão DVA-C03 quando fizer sentido, a partir de dezembro/2026 |

**Não incluir** a antiga Google Associate Android Developer (descontinuada), nem apresentar certificados privados como oficiais. Mais informações e condições: [CERTIFICACOES.md](CERTIFICACOES.md).

## Portfólio obrigatório

1. **Kotlin Core Lab:** biblioteca e testes próprios com README em inglês.
2. **Android Engineering Lab:** Compose, API, Room, offline-first, WorkManager, testes, CI/CD e documentação.
3. **KM One Engineering Case Study:** desafios reais Android (serviços, permissões, resiliência, performance) sem expor dados privados, segredos ou inventar métricas.
4. **Flutter Production Lab:** app multiplataforma com plugin/integração nativa, testes e comparação técnica.

Cada projeto deve permitir a reprodução do cenário, justificar arquitetura, apresentar erros/limitações e evidenciar resultados verdadeiros. Nada de segredos, dados pessoais ou números imaginados.

## Mercado e posicionamento

Headline de trabalho: **Software Engineer | Android Native & Flutter | Mobile Architecture | Kotlin & .NET**. O histórico sênior geral não equivale automaticamente à senioridade Android; evoluir o título conforme evidências e a atuação real. Ver [guia de carreira](CARREIRA_PORTFOLIO.md).

## Aula 01 publicada — F0.01

- [**F0.01 — Como funcionam os aplicativos, Android e lifecycle**](lessons/F0.01-ANDROID-FOUNDATIONS.md) — explicações, exemplos, código ilustrativo, sete exercícios e avaliação de 16 pontos.
- **Estado:** conteúdo disponibilizado; ainda não comprovado. Responder exercícios para correção e posterior laboratório.

## Primeira sessão — começar sem diagnóstico

1. Abrir [a Fase 0 do painel](https://lucastrevvos.github.io/software-mastery-roadmap/mobile/).
2. Estudar **F0.01 — Como funcionam aplicativos móveis, SO e ciclo de vida**.
3. Instalar/validar Android Studio, SDK, emulador/JDK e executar um projeto Kotlin simples.
4. Criar Hello Mobile, versionar e documentar o que foi feito, mantendo o status de domínio honesto.
5. Exportar o backup JSON do painel periodicamente. Atualizar o [PROGRESS.md](PROGRESS.md) com evidências após commits.

## Persistência

O painel web usa **localStorage do navegador**, com exportação/importação JSON. Isso **não grava no GitHub automaticamente**. O currículo versionado é [data.json](data.json) e o histórico oficial é [PROGRESS.md](PROGRESS.md), atualizado por commits. O foco é acompanhar progresso real, não simular aprovação de provas.

Planejado em 30/10/2026. Revisar validade e elegibilidade de exames nas fontes oficiais antes de pagar ou agendar.
