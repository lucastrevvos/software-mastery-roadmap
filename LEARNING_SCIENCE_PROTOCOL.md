# Learning Science Protocol

## Objetivo

Aplicar princípios bem estabelecidos de ciência cognitiva, psicologia da aprendizagem e neurociência educacional ao roadmap inteiro, sem transformar o estudo em burocracia. O objetivo é aumentar retenção, transferência, independência e velocidade real de aprendizagem.

## Regra central

**Não otimizar para sensação de familiaridade. Otimizar para recuperação, explicação, uso e transferência.**

Reconhecer algo quando está na tela não é o mesmo que lembrar, explicar ou usar sem ajuda.

## Ciclo padrão de aprendizagem

Sempre que um conceito relevante aparecer, preferir a sequência:

1. **Exposição curta** — apresentar o modelo mental mínimo necessário.
2. **Geração** — pedir que o aluno tente antes de receber a solução completa.
3. **Feedback rápido** — corrigir erro logo depois da tentativa.
4. **Recuperação ativa** — pedir explicação ou reconstrução sem consulta.
5. **Aplicação** — usar o conceito em exercício real.
6. **Variação** — mudar o contexto para evitar memorização do exemplo.
7. **Reteste espaçado** — revisitar depois de algum esquecimento.
8. **Transferência** — conectar a outro domínio, linguagem ou problema da vida real.

## 1. Retrieval Practice — recuperação ativa

Priorizar perguntas sem consulta em vez de releitura passiva.

Exemplos:

- “Sem olhar, quais são os estados do circuit breaker?”
- “Qual tabela liga `movies` a `people`?”
- “Por que retry em POST pode duplicar efeito?”

Usar micro-retrievals de 30 segundos a 5 minutos durante o estudo, principalmente depois de conceitos estruturais.

## 2. Generation Effect — tentar antes de ver

Quando o aluno já possui pré-requisitos suficientes, não entregar imediatamente a solução completa.

Fluxo preferido:

problema → tentativa → erro ou hipótese → feedback → correção → explicação.

A solução completa pode ser mostrada quando o esforço cognitivo alvo já aconteceu ou quando produtividade for mais importante que treino.

## 3. Spacing — espaçamento

Evitar concentrar toda a prática em uma única sessão.

Referência: D+1, D+3, D+7, D+14, D+30 e D+60, ajustando pela evidência real.

Não criar revisões burocráticas de tudo. Priorizar:

- erros anteriores;
- mecanismos fundamentais;
- conceitos que serão reutilizados;
- conteúdos que o aluno reconhece, mas ainda não recupera sozinho.

## 4. Interleaving — prática intercalada

Misturar tipos de problema quando o objetivo for discriminar qual técnica usar.

Exemplo em SQL:

`WHERE` → `JOIN` → `ORDER BY` → subquery → agregação → `JOIN` novamente.

O mundo real não informa previamente qual técnica resolve o problema. A prática deve gradualmente refletir isso.

## 5. Elaboração e conexão

Sempre que útil, ligar o conceito novo a estruturas já conhecidas.

Exemplos:

- índice de banco → árvore/hash + Big O;
- referências de C#/JS → ponteiros abstraídos;
- retry → falha parcial em sistemas distribuídos;
- `JOIN` → reconstrução de relações entre entidades;
- callback/lambda → função como valor.

Pergunta padrão: **“Com o que isso se parece entre as coisas que já sei?”**

## 6. Chunking — formação de blocos mentais

No início, ensinar componentes separadamente. Depois, agrupá-los em padrões maiores.

Exemplo:

`SELECT` + `FROM` + `JOIN` + `WHERE` + `ORDER BY`

passa gradualmente de cinco elementos separados para o chunk mental “consulta relacional”.

Não automatizar cedo demais. Primeiro compreender; depois ganhar fluência.

## 7. Desirable Difficulties — dificuldades desejáveis

Introduzir dificuldade quando ela melhora retenção ou transferência, não por sofrimento gratuito.

Exemplos:

- pedir previsão antes de executar código;
- retirar uma pista já dominada;
- mudar nomes e contexto do problema;
- misturar técnicas;
- pedir reconstrução depois de alguns dias.

Se a dificuldade impedir qualquer progresso, reduzir a carga e reconstruir o modelo mental.

## 8. Error-Driven Learning — aprender com erro

Erro com feedback rápido é dado de aprendizagem.

Distinguir:

- erro de digitação;
- lacuna de sintaxe;
- modelo mental incorreto;
- falha de decomposição;
- erro de transferência;
- decisão arquitetural ruim.

Erros conceituais recorrentes entram no Error Ledger e ganham Repair/Retest.

## 9. Cognitive Load — carga cognitiva

Evitar apresentar muitos elementos novos simultaneamente.

Preferir camadas:

modelo simples → mecanismo → exceções → trade-offs → versão profissional.

Regra: **complexidade do assunto não exige complexidade da primeira explicação.**

Quando o aluno estiver aprendendo mecanismo novo, reduzir detalhes periféricos de sintaxe e ferramentas.

## 10. Explicação e Feynman reverso

Depois de um conceito importante, ocasionalmente pedir uma explicação em linguagem simples, sem jargão desnecessário.

Critério:

- consegue explicar o que acontece;
- consegue dizer por que existe;
- consegue dar um exemplo;
- consegue dizer quando não usar.

Explicar não substitui executar, mas revela lacunas rapidamente.

## 11. Transferência deliberada

Sempre procurar aplicações além do exemplo original.

### Transferência técnica

- SQL `JOIN` → modelagem relacional;
- circuit breaker → sistemas distribuídos;
- stack → recursão → runtime;
- hashing → dicionários → índices.

### Transferência para problemas gerais

Quando genuinamente útil, marcar **Técnica transferível** e mostrar uma aplicação fora da programação, especialmente em:

- decomposição de problemas;
- tomada de decisão;
- investigação de causas;
- comunicação;
- planejamento;
- gestão de risco;
- feedback;
- negociação;
- organização do aprendizado.

Não forçar analogias quando não houver benefício real.

## 12. Calibration — saber o que realmente sabe

Periodicamente comparar três estados:

1. “parece familiar”;
2. “consigo lembrar sem olhar”;
3. “consigo usar em problema novo”.

Mastery deve se basear principalmente nos estados 2 e 3.

## 13. Prática deliberada adaptativa

A dificuldade deve acompanhar o desempenho.

Se o aluno acerta facilmente várias vezes:

- remover pistas;
- aumentar variação;
- misturar conceitos;
- exigir explicação/trade-off.

Se erra repetidamente:

- reduzir o problema;
- reconstruir pré-requisito;
- fornecer exemplo contrastante;
- repetir depois sem consulta.

## 14. Sono, pausas e consolidação

Aprendizagem não ocorre apenas durante exposição. Sono e intervalos ajudam a consolidar memórias.

Evitar interpretar horas contínuas de estudo como sinônimo de progresso. Em sessões longas, preferir blocos com mudança de atividade e recuperação ativa.

## 15. Política operacional para o assistente

Durante o roadmap, o assistente deve decidir dinamicamente quando:

- explicar;
- perguntar antes de explicar;
- pedir previsão;
- deixar o aluno errar de forma segura;
- revisar conceito antigo;
- conectar dois tópicos;
- aumentar dificuldade;
- simplificar;
- registrar erro;
- marcar técnica transferível;
- criar reteste futuro.

Não anunciar toda decisão pedagógica. Aplicar de forma natural.

## 16. Hierarquia de domínio

Usar esta progressão como referência:

**Reconhecer → Recordar → Explicar → Executar → Depurar → Transferir → Reter.**

A meta final não é lembrar uma resposta específica. É construir modelos mentais reutilizáveis e capacidade de resolver problemas novos.

## 17. Integração com os protocolos existentes

Este protocolo complementa:

- `LAB_PROTOCOL.md`;
- Velocity Mode;
- Recall / Trace / Rebuild / Repair / Transfer / Retest;
- Método Especial JCI;
- Algorithm Gym;
- Project Layer.

Quando houver conflito entre velocidade e profundidade, usar evidência real para decidir: exercícios oficiais e projetos continuam sendo a prática principal; ciência da aprendizagem serve para tornar essa prática mais eficiente, não para criar uma segunda grade curricular.

## Frase de referência

**Ver não é saber. Saber é conseguir recuperar, explicar, usar, corrigir e transferir.**
