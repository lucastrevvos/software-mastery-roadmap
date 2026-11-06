# Módulo 1 · Semana 1 — Como o C# guarda e copia informações

**Situação:** estudando · **Início:** 06/11/2026 · **Domínio comprovado:** ainda não.

## Como será a aula

Uma ideia de cada vez:

1. Um exemplo familiar, sem palavras técnicas.
2. Explicação do código, linha a linha.
3. Uma pergunta curta sem pegadinha.
4. Depois que a ideia ficar clara, um exemplo mais difícil.
5. Só então um exercício prático com teste.

**Regra do professor:** nenhuma palavra técnica nova sem explicação simples antes. Não antecipar assuntos de semanas futuras.

## Aula 1.1 — O que significa copiar?

Imagine a ficha de uma pessoa:

- Nome: Lucas
- Idade: 35

Agora você cria **outra ficha**, quase igual, mas com nome Pedro. A ficha de Lucas não muda.

No C#, podemos fazer:

```csharp
public record Pessoa(string Nome, int Idade);

var pessoa1 = new Pessoa("Lucas", 35);

var pessoa2 = pessoa1 with { Nome = "Pedro" };

Console.WriteLine(pessoa1.Nome);
Console.WriteLine(pessoa2.Nome);
```

**Vocabulário traduzido:**

- `Pessoa`: o tipo de ficha que estamos definindo.
- `record`: uma forma do C# de definir um tipo de dados que possui recursos úteis para comparação por valores e cópia.
- `new Pessoa("Lucas", 35)`: cria uma nova ficha.
- `var`: pede ao C# que descubra o tipo da variável com base no valor atribuído.
- `with`: cria uma **nova ficha com os mesmos dados, exceto os que você troca**.
- `Console.WriteLine`: mostra uma informação na tela.

**Saídas:** `Lucas` e `Pedro`.

**Pergunta 1 (sem executar):**

```csharp
var pessoa1 = new Pessoa("Lucas", 35);
var pessoa2 = pessoa1 with { Nome = "Pedro" };

Console.WriteLine(pessoa1.Nome);
```

O que aparece? (A) Lucas (B) Pedro (C) Erro. **Aguardar resposta antes de seguir.**

## Aula 1.2 — Por que isso importa?

Depois de compreender a primeira pergunta, explicar gradualmente:

- Mudar a cópia não significa mudar a ficha original.
- Se a ficha guarda *uma lista*, duas cópias podem apontar para a **mesma lista**.
- `with` realiza cópia *superficial* no caso de um `record class`: ele cria uma instância nova, mas não duplica automaticamente todos os objetos internos.
- Só depois: distinguir tipo por valor, referência, mutabilidade e localização de memória.

**Exemplo futuro, não aplicar antes da introdução das listas:**

```csharp
public record Produto(string Nome, List<decimal> Precos);
var p1 = new Produto("A", new List<decimal> { 10m, 20m });
var p2 = p1 with { Nome = "B" };
p2.Precos.Add(30m);
```

O objetivo é perceber que uma nova ficha pode carregar **a mesma lista interna**. Não usar este exemplo como primeira avaliação.

## Aula 1.3 — Laboratório pequeno de preços (depois da base)

Sem projetos complexos ou arquitetura prematura, implementar uma função:

- Preço base: R$ 10.
- Mais R$ 2 por quilômetro.
- Para 5 km: R$ 20.
- Para 0 km: R$ 10.
- Distância negativa: rejeitar.

Depois, passo a passo, introduzir `decimal`, determinismo, validação e testes.

## Critérios de avanço na semana 1

- [ ] Explicar com as próprias palavras o que `with` faz.
- [ ] Prever a saída de dois exemplos simples.
- [ ] Explicar, depois de uma demonstração, quando compartilhar uma lista muda os dois objetos.
- [ ] Construir e testar a função simples de preço.
- [ ] Revisar a solução e justificar os limites escolhidos.

**Não marcar semana como concluída/comprovada antes de evidências.**

## Temas posteriores da mesma semana

O plano mantém os objetivos originais (CLR, stack, heap, GC, tipos e mutabilidade), mas estes serão ensinados separadamente, em camadas, com analogias e exercícios curtos. A ordem pedagógica pode ser ajustada sem reduzir o rigor.
