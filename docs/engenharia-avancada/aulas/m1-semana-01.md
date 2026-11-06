# Módulo 1 · Semana 1 — Runtime, semântica de tipos e código determinístico

> **Situação:** em estudo · **Início:** 2026-11-06 · **Evidência de domínio:** pendente. Esta aula é orientada por mentoria: a conclusão depende da explicação, execução dos testes e defesa técnica.

## Objetivos verificáveis

1. Diferenciar *value semantics* de *reference semantics* sem confundir tipo por valor com endereço físico de memória.
2. Explicar *stack frames*, *managed heap*, CLR, JIT e GC nos limites apropriados.
3. Identificar mutabilidade compartilhada em objetos e cópias superficiais.
4. Implementar uma função de precificação determinística, usando decimal e arredondamento explícito.
5. Validar entradas, invariantes e fronteiras com testes automatizados.

## Aula 1.1 — Execução e aliasing

- A *stack* organiza frames e estados de execução de métodos. O *managed heap* armazena objetos gerenciados tipicamente de referência. Localizações físicas podem variar segundo otimizações, captura por closure, composição e runtime.
- Em C#, *value type* possui semântica de cópia do valor; *reference type* possui semântica de cópia da referência, que pode apontar para objeto compartilhado.
- Uma propriedade com `init` ou um `record` não torna, por si só, todos os objetos internos imutáveis. Cópia com `with` é rasa para campos/propriedades de referência.
- Uma API deve estabelecer propriedade de dados e comportamento de mutabilidade, principalmente ao receber e devolver coleções.

### Diagnóstico (sem executar antes de responder)

```csharp
public record Produto(string Nome, List<decimal> Precos);

var p1 = new Produto("Produto A", new List<decimal> { 10m, 20m });
var p2 = p1 with { Nome = "Produto B" };

p2.Precos.Add(30m);

Console.WriteLine(p1.Precos.Count);
Console.WriteLine(p2.Precos.Count);
Console.WriteLine(ReferenceEquals(p1, p2));
Console.WriteLine(ReferenceEquals(p1.Precos, p2.Precos));
```

Responder:
1. Quatro saídas exatas, na ordem.
2. Por que a operação `with` não isolou a lista.
3. Diferença entre imutabilidade superficial e profunda.
4. Como projetar a coleção para não permitir mutação externa (avaliar também aliasing de referências recebidas no construtor).

## Aula 1.2 — Laboratório de precificação (após diagnóstico)

Implementar `PriceCalculator.Calculate(PriceInput input)` como função pura. Sem HTTP, bancos, ORM ou estado global.

**Modelo de entrada:** distância não negativa (`decimal` em km), duração não negativa (`int` em minutos), `bool HighDemand`, `decimal DiscountPercent` entre 0 e 100.

**Política:**
- Tarifa fixa R$ 12,00.
- Distância: R$ 2,40 por km.
- Duração: R$ 0,65 por minuto.
- Demanda alta multiplica subtotal por 1,25; normal por 1,00.
- Desconto aplicado após multiplicador: `DiscountPercent / 100`.
- Arredondamento **somente no final**, 2 casas decimais, `MidpointRounding.AwayFromZero`.
- Entradas fora dos limites lançam `ArgumentOutOfRangeException`; entrada nula, `ArgumentNullException`.
- Escolher comportamento explícito em caso de overflow.

**Casos mínimos esperados:**
- 10 km, 20 min, demanda normal, desconto 0%: R$ 49,00.
- 10 km, 20 min, demanda alta, desconto 10%: R$ 55,13.
- 0 km, 0 min, demanda normal, desconto 0%: R$ 12,00.
- Distância negativa e desconto >100%: rejeição por validação.

**Perguntas de engenharia:** por que `decimal` e não `double` para preços? Por que aplicar arredondamento só ao final? A função é determinística? Há efeitos colaterais? Como impedir mutação externa?

## Checkpoint da semana 1 (ainda não validado)

- [ ] Diagnóstico de referências e imutabilidade explicado sem consultar execução.
- [ ] Implementação compilável de motor de preço puro.
- [ ] Testes com casos normais, limites e inválidos.
- [ ] Evidência associada a commit, diff ou testes revisados.
- [ ] Explicação fundamentada de cópia de valor, cópia de referência e aliasing.

**Regra:** não marcar esta semana como `Comprovado` enquanto os itens não forem verificados. A avaliação do Módulo 1 permanece no gate A da semana 2.

## Caminho de continuidade

Após diagnóstico, executar o laboratório, revisar a implementação, introduzir testes de propriedades e seguir para complexidade assintótica na semana 2.
