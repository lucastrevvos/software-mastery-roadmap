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

- **CS50x:** em andamento — Weeks 0–4 concluídas, incluindo Problem Sets 0–4; etapa atual: Week 5 — Data Structures.
- **freeCodeCamp JavaScript Certification:** em andamento, em paralelo.
- **Programming Mastery Lab:** ativo em modo de checkpoints cumulativos.
- **Engineering Impact:** trilha transversal ativa para transformar maturidade técnica em projetos, documentação, open source e contribuição pública quando fizer sentido.
- **Método Especial JCI:** camada transversal ativa; Japão = profundidade, China = treino deliberado, Índia = aplicação/empregabilidade. Ver [JCI_METHOD.md](JCI_METHOD.md).

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