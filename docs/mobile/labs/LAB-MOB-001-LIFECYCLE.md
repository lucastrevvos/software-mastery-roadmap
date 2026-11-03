# LAB-MOB-001 — Android Lifecycle na prática

> **F0.01** · Kotlin / Android Studio / Logcat · **Status: aberto, aguardando execução do aluno**  
> [Voltar ao roadmap](../README.md) · [Aula de referência](../lessons/F0.01-ANDROID-FOUNDATIONS.md) · [Progresso oficial](../PROGRESS.md)

## Método

**Construir → executar → observar → provocar uma mudança → investigar → corrigir → registrar.**  
Este laboratório é **hands-on**. Não tem questionário nem prova teórica. O domínio é avaliado pelo código e pelo comportamento observado, não por assinalar alternativas.

## Missão

Criar um app Android mínimo que permita observar eventos da **Activity** no Logcat quando se abre o app, aperta Home, retorna e, em etapa posterior, gira a tela. Aprender a distinguir Activity, estado da UI e processo.

## Etapa 1 — Preparar projeto e executar

1. No Android Studio, usar **New Project → Phone and Tablet → Empty Activity** (template com Jetpack Compose).
2. Configurar: **Name:** LifecycleLab; **Package:** com.trevvos.lifecyclelab; **Language:** Kotlin; **Minimum SDK:** API 26 (apenas para este laboratório; não é recomendação universal de minimum SDK).
3. Manter Gradle Kotlin DSL, se houver essa opção. **Finish** e aguardar Gradle Sync.
4. Selecionar emulador pelo Device Manager ou celular Android com depuração USB habilitada.
5. Clicar Run e verificar que o app abre e mostra a UI criada pelo template.

**Checkpoint 1:** compila, instala e abre no dispositivo. Sem iniciar API, banco ou infraestrutura.

Guia oficial: [Criar seu primeiro app Android](https://developer.android.com/codelabs/basic-android-kotlin-compose-first-app?hl=pt-br).

## Etapa 2 — Instrumentar a Activity

Abra **app/src/main/java/com/trevvos/lifecyclelab/MainActivity.kt** (a estrutura da árvore pode apresentar o pacote em uma única linha).

- **Não substitua** o setContent do template. Preserve a UI existente.
- Adicione import `android.util.Log`.
- Dentro de `onCreate`, logo após `super.onCreate(savedInstanceState)`, adicione:

```kotlin
Log.d("LifecycleLab", "onCreate")
```

- Depois do fechamento de `onCreate`, ainda dentro da classe `MainActivity`, acrescente estes dois callbacks:

```kotlin
override fun onStart() {
    super.onStart()
    Log.d("LifecycleLab", "onStart")
}

override fun onResume() {
    super.onResume()
    Log.d("LifecycleLab", "onResume")
}
```

**Tarefa prática (sem solução pronta):** implemente callbacks equivalentes para `onPause`, `onStop`, `onRestart` e `onDestroy`. Use `override`, chame `super` e registre uma linha de log em cada callback. Preserve os métodos do template.

**Dica:** você está observando **o lifecycle da Activity**, não o lifecycle de cada rota Compose.

## Etapa 3 — Investigar com Logcat

1. Execute o app.
2. Abra **View → Tool Windows → Logcat** (atalho pode variar).
3. Escolha o dispositivo/processo corretos.
4. No campo de consulta, filtre por `tag:LifecycleLab` ou, como alternativa, `tag:LifecycleLab level:DEBUG`.
5. Observe e registre as linhas geradas pelo seu código.

**Experimentos, nesta ordem:**

- **A.** Abra o app pela primeira vez. Registre a sequência observada.
- **B.** Aperte Home. Registre os callbacks.
- **C.** Volte ao app pelos Recentes ou ícone, sem provocar encerramento do processo. Registre o resultado.
- **D.** Gire o aparelho/emulador, com rotação automática habilitada e sem orientação fixa. Registre o que mudou.

**Atenção:** o sistema pode variar a sequência por visibilidade parcial, rotação configurada, configurações do dispositivo e destruição/reativação. Não assumir que `onDestroy` é garantido na morte do processo. Não confundir **Force stop** com fechamento normal ou morte sob pressão de memória.

Guia oficial: [Logcat](https://developer.android.com/studio/debug/logcat) · [Activity lifecycle](https://developer.android.com/guide/components/activities/activity-lifecycle).

## Etapa 4 — Registrar evidência (quando tiver executado)

Crie no seu projeto local `OBSERVACOES.md` com:

```markdown
# LAB-MOB-001 — Observações

## Ambiente
- Android Studio:
- Emulador/dispositivo:
- Versão Android (API):

## Execução
- Primeiro lançamento:
- Após Home:
- Retorno ao app:
- Rotação:

## Descoberta
- Comportamento que eu esperava:
- Comportamento que observei:
- O que mudou no meu modelo mental:

## Evidência
- Link para commit:
- Logcat (sem dados pessoais):
```

Após a execução, em um terminal **na pasta do seu projeto local**:

```bash
git status
git add .
git commit -m "lab(mobile): observe Android activity lifecycle"
```

Esses comandos pressupõem que o diretório já é um repositório Git; caso não seja, inicializar com `git init` e configurar usuário Git primeiro. **Não executar push sem antes definir/configurar o remoto GitHub.** O repositório do laboratório de app ainda não foi criado automaticamente.

## Gate observável

- [ ] Projeto abre em emulador ou dispositivo.
- [ ] Logs mostram eventos de pelo menos `onCreate`, `onStart` e `onResume`.
- [ ] Os outros callbacks foram implementados e o app compila.
- [ ] Experimentos A–D foram executados e registrados.
- [ ] O aluno consegue explicar divergências entre sequência esperada e observada **a partir da evidência**.
- [ ] Commit verificável ou código + registros enviados para revisão.

**Não marcar F0.01 como comprovado antes da revisão.** Para Retention/Mastery 7 haverá revisão futura.

## Retorno no chat

Envie o `MainActivity.kt` ou trechos do Logcat e o `OBSERVACOES.md`. A revisão será sobre a execução real, as escolhas, as falhas e as correções; sem quiz.
