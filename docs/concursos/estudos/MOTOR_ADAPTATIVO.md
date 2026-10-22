# CME — Concurso Mastery Engine (v1)
**Status:** programa de estudo adaptativo experimental, integrado à trilha CASAN → CGU 2026. **Não promete aprovação**, não é uma IA treinada com dados de classificação e não prevê nota de corte.

## Status de fonte — 22/10/2026
A base Dataprev foi atualizada pelo **gabarito oficial preliminar** da FGV, não definitivo. Resultado recalculado: **37/70, 59,5/115**, margem de 2 pontos sobre o mínimo de 57,5 (sem zerar disciplinas). Fonte: https://conhecimento.fgv.br/sites/default/files/concursos/dataprev2026-gabaritos-para-publicacao.pdf

## Propósito
Maximizar pontos esperados por hora de estudo a partir de:
- conteúdo **presente nos editais**;
- peso e urgência das provas;
- desempenho real sob tempo (não apenas quizzes sem cronômetro);
- evidências de retenção em retestes;
- origem de cada erro: conhecimento, interpretação, tempo, esquecimento, leitura precipitada;
- cobertura de temas importantes, sem deixar assuntos inéditos por estudar;
- revisão espaçada e simulados integrais.

## Objetivos de preparação
- CASAN (AOCP, 22/11/2026): **42/50** como meta interna inicial, **não nota de corte prevista**; prova real oficial e retificações prevalecem. Treino de tempo incluindo cartão-resposta.
- CGU (Cebraspe, 13/12/2026): foco forte pós-CASAN; simular pontuação negativa dos itens e prática discursiva. Critérios do edital prevalecem.
- Pré-CASAN: aproximadamente 50% núcleo compartilhado, 40% exclusivo CASAN, 10% manutenção exclusiva CGU. Proporções iniciais, não metas imutáveis.
- Nunca bloquear acesso a um módulo porque outro está incompleto.

## Base pessoal (hipóteses iniciais até coleta)
Na Dataprev Tipo 1, a correção **extraoficial** registrou **37 acertos/70; 59,5/115**. Português **4/12**; inglês **9/12**; lógica **3/5**; atualidades **4/6**; legislação **2/5**; TI específica **15/30**. A questão 65 foi marcada B, embora o usuário tenha identificado E depois. A questão 69 foi marcada C; correção extraoficial sugeriu B. A FGV divulgou o gabarito preliminar em 13/10/2026: Q37 E, Q69 B. Q5 e Q64, antes tratadas como acertos na nossa correção, são erros conforme a FGV.
Hipóteses diagnósticas: baixa cobertura de governança, segurança, alguns tópicos de BI/ETL, lacunas de Português e dificuldade declarada de tempo. Não considerar essas hipóteses domínio medido na CASAN.

## Fundamento e limites da evidência
Pesquisa de psicologia da aprendizagem (Dunlosky et al., 2013) identifica **practice testing** e **distributed practice** como estratégias de alta utilidade. Prática intercalada e autoexplicação têm evidência promissora/moderada, dependendo de tarefa/contexto. A eficácia individual, a dose ideal e o ganho na nota **não podem ser previstos** pela literatura.
- https://doi.org/10.1177/1529100612453266
- https://pubmed.ncbi.nlm.nih.gov/23088488/
- https://eric.ed.gov/?id=EJ1036741

## Ciclo de treinamento AMS-CME
1. **Diagnóstico (sem cola):** misto por disciplina; registrar acertos, tempo e grau de confiança antes da correção.
2. **Teoria mínima (8–20 min):** só para preencher lacuna detectada ou introduzir tema realmente novo.
3. **Workshop — 10 questões comentadas:** reconhecer regra, exemplos e pegadinha da banca.
4. **Lab — 10 questões sem gabarito visível:** cronometrar e submeter antes de revelar respostas.
5. **Triagem de erros:** conhecimento, interpretação, tempo, esquecimento ou pegadinha.
6. **Repair + Retest:** refazer em formato alterado; não repetir mecanicamente a mesma alternativa.
7. **Retenção:** relembrar ativamente em dias distintos; usar revisões indicativas D+1, D+3, D+7, D+14, ajustáveis conforme acertos e prazo.
8. **Simulado semanal:** reproduzir banca, composição e tempo, incluindo cartão-resposta e estratégia de três passagens.
9. **Decisão:** adaptar dificuldade, tempo e quantidade de teoria ao erro predominante.
10. **Competência confirmada:** nunca chamar de “dominado” com base em uma sessão: requer pelo menos duas sessões independentes, em dias separados, com ≥80% e dentro do tempo-alvo; manter revisões periódicas.

## Motor de seleção v1 (heurística explícita, não modelo científico)
Cada tema possui prioridade editorial P1–P3 e rótulo CASAN / compartilhado / CGU; estimativa inicial de lacuna proveniente da Dataprev e do caráter inédito do conteúdo; cada treino registrado fornece observações mais confiáveis.

**Prioridade ajustada** combina:
- pertinência à prova mais próxima (CASAN até 22/11; CGU depois);
- peso/urgência/risco de conteúdo novo;
- lacuna de domínio **observada**, quando existem tentativas; caso contrário, **estimada**;
- revisão vencida;
- incidência de erros por falta de tempo, interpretação ou conhecimento;
- mitigação para tópicos nunca treinados.
Os parâmetros são heurísticos, transparentes no código e podem ser ajustados ao desempenho. **Não são probabilidades de acerto nem previsões de classificação.**

## Registro de sessão
Cada treino contém: data, concurso/banca, disciplina, tipo (workshop, lab, simulado, revisão, discursiva), total, acertos, erros, brancos, tempo em minutos, confiança autorreferida e causa de erro. O tempo e o resultado podem ser usados para sugerir o treino seguinte. O sistema não verifica a honestidade de uma resposta informada manualmente.

## Administração de tempo
- **CASAN:** três passagens: fáceis/rápidas, trabalhosas, conferência final. Reservar tempo para preencher cartão. O usuário relatou que seu gargalo na Dataprev foi tempo.
- **CGU:** cálculo da penalização (acerto +1 ou +2; erro -1 ou -2; branco 0, conforme provas específicas e edital), além de planejamento separado para discursiva.
- Laboratório de 10 questões: 25 minutos é **meta de treino inicial**, não limite da AOCP.
- Se precisão sem limite de tempo for alta, mas com tempo cair, priorizar treino de velocidade e leitura.
- Se precisão persistir baixa mesmo sem tempo, priorizar teoria focada, workshop e questões graduadas.

## Rotina mínima
- Início: 10–15 min de recuperação sem consulta de assuntos em revisão.
- Principal: um a três blocos curtos sobre os tópicos de maior prioridade.
- Encerramento: questões inéditas/intercaladas, cronômetro e Error Ledger.
- Uma vez por semana: simulado completo e 30–60 min de auditoria de erros.
- Dia de menor energia: revisão de 15 min ou até descanso planejado; **regularidade sustentável** supera contagem de horas inviável.

## Gates objetivos
- **CASAN (treino):** alcançar pelo menos 42/50 em **dois** simulados completos recentes, com cartão simulado, analisando a distribuição por matéria.
- **CGU (treino):** aplicar pontuação negativa por prova, acompanhar mínimos objetivos e resposta discursiva com rubrica de fidelidade aos critérios. Nenhum score estimado garante habilitação, classificação ou nota de corte.
- **Retenção:** manter 80%+ nos retestes sobre temas estudados, inclusive após intervalo.
- Se não houver dados suficientes, mostrar **“diagnóstico preliminar”**, sem inventar índice de domínio.

## Armazenamento e privacidade
- Código versionado no GitHub Pages em `docs/concursos/estudos/motor.html`, `motor.js`.
- Progresso inserido na página é salvo **somente em localStorage do navegador**. O GitHub não recebe automaticamente notas, alternativas nem histórico; use Exportar/Importar JSON e, se quiser persistência no repo, envie o export nesta conversa para atualização.
- Planejamento, fontes, banco de questões e análise extraoficial são versionados no GitHub.
- Para evitar coleta de informação identificadora desnecessária, não registrar dados de inscrição, documento, remuneração ou saúde no painel.

## Fontes do conteúdo
- CASAN: https://www.institutoaocp.org.br/concursos/711
- CGU: https://www.cebraspe.org.br/concursos/cgu_26_affc
- Matriz: [plano-2026.json](./plano-2026.json)
- Treino inicial: [questoes-portugues.json](./questoes-portugues.json)
- Diagnóstico: [dataprev-2026-extraoficial.md](./dataprev-2026-extraoficial.md)

**Governança do método:** revisar algoritmo após duas semanas, conforme as métricas, evitando ajustar parâmetros a cada resultado aleatório de 10 itens.
