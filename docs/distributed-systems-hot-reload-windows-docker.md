# Checkpoint — Hot reload com Docker Desktop + Git Bash no Windows

## Contexto
No `distributed-workshop`, o `payments-service` estava rodando com `npm run start:dev` (`nest start --watch`), mas alterações feitas no host não estavam provocando reload automático do Nest.

## Hipótese inicial
O problema poderia estar em uma destas camadas:

1. o bind mount do host para o container não estava ativo;
2. o arquivo mudava no host, mas não dentro do container;
3. o arquivo mudava dentro do container, mas o watcher do Nest/TypeScript não percebia a mudança.

## Diagnóstico executado

### 1. Verificação dos mounts

```bash
docker inspect "$(docker compose ps -q payments)" \
  --format '{{range .Mounts}}{{println .Source "->" .Destination}}{{end}}'
```

Saída observada:

```text
C:\dev\ESTUDOS\distributed-workshop\payments-service -> /app
/var/lib/docker/volumes/.../_data -> /app/node_modules
```

Conclusão: o bind mount `./payments-service:/app` estava correto e `/app/node_modules` estava preservado em volume separado.

### 2. Pegadinha do Git Bash / MSYS path conversion

O comando abaixo falhou:

```bash
docker compose exec payments \
  grep -n "HOT_RELOAD_TEST_123" /app/src/payment.service.ts
```

Erro observado:

```text
grep: C:/Program Files/Git/app/src/payment.service.ts: No such file or directory
```

Causa: o Git Bash converteu automaticamente o path Linux `/app/...` para um path Windows antes de chamar o Docker.

Soluções úteis:

```bash
docker compose exec payments \
  sh -lc 'grep -n "HOT_RELOAD_TEST_123" /app/src/payment.service.ts'
```

ou:

```bash
MSYS_NO_PATHCONV=1 docker compose exec payments \
  grep -n "HOT_RELOAD_TEST_123" /app/src/payment.service.ts
```

No laboratório, preferimos `sh -lc` quando o comando usa caminhos Linux dentro do container.

### 3. Prova de que o arquivo alterado no host chega ao container

Após adicionar no host:

```ts
// HOT_RELOAD_TEST_123
```

foi executado:

```bash
docker compose exec payments \
  sh -lc 'grep -n "HOT_RELOAD_TEST_123" /app/src/payment.service.ts'
```

Saída observada:

```text
75:// HOT_RELOAD_TEST_123
```

Conclusão: o bind mount está sincronizando corretamente o arquivo host -> container.

### 4. Prova de que o serviço realmente está em watch mode

```bash
docker compose exec payments \
  sh -lc 'grep -n "start:dev" /app/package.json'
```

Saída observada:

```text
14:    "start:dev": "nest start --watch",
```

Conclusão: o processo está configurado para watch mode.

## Diagnóstico final até este ponto

```text
arquivo muda no Windows               ✅
        ↓
bind mount atualiza /app no container ✅
        ↓
Nest roda com `nest start --watch`     ✅
        ↓
watcher reage à mudança               ❌
```

Logo, o problema restante está na detecção de eventos de filesystem do watcher do TypeScript/Nest através do bind mount Windows -> Linux, e não no volume Docker.

## Próximo experimento
Forçar polling no watcher do TypeScript via variáveis de ambiente no `payments`:

```yaml
environment:
  TSC_WATCHFILE: DynamicPriorityPolling
  TSC_WATCHDIRECTORY: DynamicPriorityPolling
```

Depois recriar o container e testar alteração em `.ts` sem rebuild.

## Modelo mental
`start:dev` sozinho não garante hot reload entre host e container. São necessárias duas coisas independentes:

```text
1. código do host realmente disponível dentro do container
2. watcher capaz de detectar a mudança nesse filesystem montado
```

Neste experimento, (1) foi comprovado e (2) é a camada ainda problemática.
