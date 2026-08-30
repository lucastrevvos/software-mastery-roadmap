# Software Mastery Roadmap

Repositório oficial da formação **Full Stack Software Architect & Cloud Engineer** e do **Programming Mastery Lab**.

Este repositório é a fonte da verdade para quatro coisas diferentes:

1. **Roadmap** — o que estudar e em qual ordem.
2. **Progress** — o que foi iniciado/concluído nos cursos.
3. **Mastery** — o que realmente consegue ser explicado, construído, depurado e transferido sem ajuda.
4. **Retention** — o que continua disponível na memória depois de dias/semanas.

> Curso concluído não significa domínio. Certificado é evidência externa; Mastery Gate é evidência interna.

## Estado atual

- **CS50x:** em andamento — Weeks 0–4 concluídas, incluindo Problem Sets 0–4; etapa atual: Week 5 — Data Structures.
- **freeCodeCamp JavaScript Certification:** em andamento, em paralelo.
- **Programming Mastery Lab:** ativo em modo de checkpoints cumulativos.
- **Engineering Impact:** trilha transversal ativa para transformar maturidade técnica em projetos, documentação, open source e contribuição pública quando fizer sentido.

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

## Ciclo de trabalho

1. Lucas informa no chat um avanço real de curso.
2. O progresso é atualizado em `docs/data/progress.json`.
3. O conteúdo estudado é convertido em competências em `docs/data/mastery.json`.
4. Quando necessário, nasce um laboratório em `labs/` ou um Mastery Gate em `mastery-gates/`.
5. Tópicos maduros são avaliados pela trilha [Engineering Impact](ENGINEERING_IMPACT.md): estudo apenas, projeto, artigo, open source, contribuição comunitária ou palestra.
6. Lucas executa localmente, faz commit e push.
7. O código é revisado no GitHub.
8. Erros conceituais recorrentes entram em `docs/data/error-ledger.json`.
9. Revisões futuras entram em `docs/data/reviews.json`.
10. Só após retenção e transferência o tópico chega a Mastery 7.

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