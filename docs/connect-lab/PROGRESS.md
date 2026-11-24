# Connect Lab — progresso e retomada

Atualizado: 2026-11-23

Fonte de verdade do tutor: [currículo e protocolo](index.html). Referência transversal: [Caderno do Engenheiro](../engineering-notebook.html). Não presumir domínio, execução de código ou sincronização automática.

## Estado atual

- Módulo 01: iniciado (Desafios 001–004 corretos; migração para Express executada segundo relato).
- Módulos 02–12: planejados.
- Repositório de implementação: projeto local connect-lab; remoto e commits do código ainda não confirmados.
- Evidências práticas: aluno confirmou execução bem-sucedida do servidor HTTP nativo, roteamento e migração para Express nas Aulas 002–004; sem logs anexados.

## Aula 001 — Runtime versus framework

- Conceito apresentado: JavaScript/TypeScript, Node.js e Express; servidor HTTP nativo versus framework.
- Evidência 23/11/2026: resposta B, justificativa: “Teremos que usar o runtime do nodejs”. Conceito validado no nível introdutório; sem evidência prática ainda.
- Próxima ação (Aula 002): criar servidor HTTP nativo local, observar callback por requisição e testar GET /health com curl. Depois verificar entendimento antes de introduzir Express.
- Referência: [runtime versus framework no Caderno do Engenheiro](../engineering-notebook.html#connect-runtime-framework).

## Aula 002 — Servidor HTTP nativo e callback

- Evidência 23/11/2026: execução reportada como “Funcionou”; resposta B (dez requisições, dez invocações da callback).
- Conceitos validados no nível introdutório: listener de requisição, req/res, escuta na porta e resposta HTTP. Não implica thread por requisição.
- Referência: [Callback e eventos HTTP](../engineering-notebook.html#connect-http-callback).
- Próxima ação (Aula 003): implementar roteamento manual por método e caminho, GET /health com 200 e fallback 404; testar as duas respostas; desafio de compreensão. Express somente depois.

## Aula 003 — Roteamento HTTP nativo

- Evidência: execução reportada como “Funcionou”; resposta C (POST /health retorna 404 no código atual).
- Conceito validado no nível introdutório: seleção de handler por método e caminho. Explicada distinção entre fallback 404 e 405 para método não permitido; query string é uma limitação da comparação literal.
- Commit local sugerido anteriormente, ainda não confirmado pelo aluno.
- Referência: [Roteamento HTTP](../engineering-notebook.html#connect-http-routing).
- Próxima ação (Aula 004): reproduzir o mesmo contrato GET /health e fallback 404 com Express, instalar a dependência npm e comparar a abstração com o servidor nativo. Testar antes de avançar; um desafio por turno.

## Aula 004 — Express e abstração HTTP

- Evidência: execução reportada como “Funcionou”; resposta C (roteador do Express seleciona o handler).
- Conceitos validados no nível introdutório: abstração do roteamento, integração Express/Node.js; npm, manifesto e lockfile apresentados. Commit local não confirmado.
- Referência: [Framework HTTP e dependências](../engineering-notebook.html#connect-express-abstraction).
- Próxima ação (Aula 005): adicionar middleware global de logging antes das rotas; observar ordem de execução e o papel de next(); testar GET /health e GET /clientes. Um desafio por turno.

## Registro das próximas etapas

A cada avanço confirmado, registrar data, módulo/aula, conceito, evidência (resposta, teste ou commit), lacunas, reteste e próxima ação. Reaproveitar os conhecimentos de outros laboratórios sem marcar domínio automaticamente. Registrar conceitos novos no caderno transversal, evitando duplicação.
