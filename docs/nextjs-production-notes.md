# Next.js + Arquitetura Web Moderna — Production Notes

> Objetivo: transformar os experimentos locais do `distributed-workshop/next-payments-dashboard` em decisões e critérios de produção. Regra: **lab local serve para observar o comportamento; a conclusão precisa responder como isso escala, falha, é protegido e operado em produção.**

## 1. Server Components e Client Components

- `page.tsx` no App Router é Server Component por padrão.
- `useState`, `useEffect`, event handlers e browser APIs exigem Client Component.
- Preferência de produção: empurrar `'use client'` para a menor boundary necessária, em vez de transformar páginas inteiras em client-side sem necessidade.
- Motivos: menos JavaScript no browser, menor superfície de bundle, segredos e acesso a serviços permanecem no servidor.

### Experimento executado

`useState` foi colocado em `page.tsx` e o build falhou. A solução final extraiu apenas o `Counter` como Client Component.

## 2. CSR, CORS e server-side fetch

### Experimento executado

Um Client Component chamou diretamente:

```text
Browser :3002 -> Payments :3001
```

O browser bloqueou a resposta por CORS. A mesma leitura foi movida para o servidor do Next:

```text
Browser -> Next :3002 -> Payments :3001
```

O request para `:3001` desapareceu do Network do browser e o dado continuou sendo renderizado.

### Produção

Não tratar BFF/server-side fetch apenas como "forma de evitar CORS". Em produção, a decisão envolve:

- esconder topologia interna dos serviços;
- manter tokens/segredos server-side;
- padronizar autenticação/autorização;
- agregar respostas para a experiência web;
- aplicar timeout, retry seletivo, circuit breaker quando fizer sentido;
- tracing e correlation IDs;
- evitar que o browser precise conhecer dezenas de serviços internos.

CORS continua sendo necessário quando o browser realmente deve chamar uma origem diferente.

## 3. SSR, TTFB, Suspense e streaming

### Experimento executado

Foi adicionado `delayMs=5000` ao Payments.

Antes de Suspense:

```text
TTFB: 5.093562s
TOTAL: 5.093915s
```

A página inteira esperava o Payments.

Depois, o fetch lento foi movido para `PaymentsServer` dentro de uma `Suspense` boundary. O shell/fallback passou a ser enviado antes de a dependência terminar.

### Produção

Streaming não torna a dependência mais rápida. Ele **isola latência**.

Em produção, definir boundaries conforme UX e domínio:

```text
Dashboard
├── Account summary      crítico
├── Orders               importante
├── Payments             pode carregar isoladamente
└── Recommendations      opcional
```

Uma falha/lentidão opcional não deveria necessariamente derrubar ou bloquear a página inteira.

Também considerar:

- timeout por dependência;
- fallback útil, não spinner infinito;
- error boundaries;
- telemetria de TTFB e latência upstream;
- budgets de performance;
- cancelamento/abort de requests quando aplicável.

## 4. Hydration

### Experimento executado

`Math.random()` foi renderizado diretamente em um Client Component e produziu hydration mismatch. A correção manteve o primeiro render determinístico e gerou o valor apenas depois do mount via `useEffect`.

### Produção

Evitar durante o primeiro render valores dependentes de:

- `Math.random()`;
- relógio local (`Date.now`, `new Date`) sem estratégia;
- browser-only APIs;
- locale/timezone diferente entre server e client;
- dados que mudam entre prerender e hydration.

Hydration mismatch não deve ser "silenciado" sem entender a divergência.

## 5. Next 16 — Cache Components

O lab usa o modelo moderno com:

```text
cacheComponents: true
'use cache'
cacheLife(...)
cacheTag(...)
```

Foi observado que `export const dynamic = 'force-dynamic'` é incompatível com `cacheComponents`, e que valores não determinísticos como `new Date()` durante prerender precisam ser tratados conscientemente.

## 6. Cache stale — comprovado

### Experimento executado

Estado inicial:

```text
Payments API = 8
Next Dashboard = 8
```

Uma nova order percorreu:

```text
Orders -> RabbitMQ -> Payments -> PostgreSQL
```

Depois:

```text
Payments API = 9
Next Dashboard = 8
```

O cache estava funcionando corretamente; a visão do Next estava stale.

### Produção

Pergunta central de arquitetura:

> **Quanto tempo este dado pode ficar incorreto/desatualizado?**

A política depende do domínio.

Exemplos:

```text
Página institucional       minutos/horas podem ser aceitáveis
Catálogo                  segundos/minutos, depende do negócio
Estoque                   tolerância baixa
Saldo financeiro          tolerância muito baixa
Status de pagamento       geralmente baixa
```

Não usar cache apenas porque "fica mais rápido".

## 7. Revalidação temporal

Foi testado `cacheLife` com janela curta de revalidation.

Modelo:

```text
cache antigo
   ↓
janela de revalidate passou
   ↓
request pode receber stale
   ↓
refresh em background
   ↓
requests seguintes recebem fresh
```

Isso é apropriado quando baixa latência vale mais do que consistência imediata.

## 8. Invalidação explícita

Foi criada uma tag:

```text
payments
```

E um Route Handler de laboratório chamou:

```text
revalidateTag('payments', { expire: 0 })
```

Resultado executado:

```text
API = N+1
Dashboard = N

invalidate 'payments'

próximo acesso -> fetch fresh -> Dashboard = N+1
```

### Conceito

Revalidação temporal:

```text
"talvez esteja velho; verifique depois de X tempo"
```

Invalidação:

```text
"eu sei que ficou velho agora"
```

O endpoint criado é apenas o mecanismo de laboratório/webhook. Um sistema externo precisa de **algum canal de integração** para sinalizar a invalidação: HTTP/webhook autenticado, mensageria, pub/sub, ou infraestrutura compartilhada.

## 9. Cache local não é cache distribuído

No lab, o cache runtime do Next é local ao processo/instância.

Em uma implantação com réplicas:

```text
Load Balancer
   ├── Next A -> cache A
   ├── Next B -> cache B
   └── Next C -> cache C
```

Pode ocorrer:

```text
A = payment 11
B = payment 10
C = payment 10
```

Invalidar somente A não garante invalidação de B/C.

### Produção

Para múltiplas réplicas, avaliar:

- cache remoto/compartilhado;
- Redis/KV/DynamoDB ou handler equivalente;
- propagação de invalidações;
- comportamento em restart/deploy;
- TTLs e eviction;
- cache stampede/thundering herd;
- observabilidade de hit/miss/stale;
- fallback se o cache remoto cair.

Cache não é fonte da verdade. Banco/serviço de domínio continua sendo a source of truth.

## 10. Invalidação orientada a eventos

Evitar acoplamento desnecessário:

```text
Payments Service -> POST direto no frontend
```

quando o domínio pode publicar apenas o fato:

```text
PaymentSucceeded
```

Consumidores interessados podem reagir:

```text
PaymentSucceeded
├── Notifications
├── Analytics
├── Cache Invalidator
└── outros consumidores
```

O produtor não precisa conhecer a existência do Next.

## 11. Critério permanente para os próximos labs

Para cada conceito, responder sempre:

1. O que observamos localmente?
2. Qual problema real isso resolve?
3. O que quebra com múltiplas instâncias?
4. Onde fica o estado?
5. O que acontece no restart/deploy?
6. Como autenticar/proteger a integração?
7. Qual timeout e comportamento de falha?
8. Como observar/logar/traçar?
9. Qual impacto de custo e escala?
10. Qual trade-off eu defenderia em uma entrevista de arquitetura?

## Próximos passos

- Route Handler como BFF.
- BFF com timeout e tratamento de falha parcial.
- Comparar BFF vs API Gateway.
- Duas réplicas do Next com cache local divergente.
- Cache compartilhado/propagação de invalidação.
- Microfrontends e independent deployment.
- Module Federation/runtime composition.
