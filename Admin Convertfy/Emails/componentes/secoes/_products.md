---
tipo: secao
secao: products
variantes: 9
ativas: 9
com_julgamento: 9
status: aprovada
---

# Cobertura

9 variantes, todas ativas, todas julgadas. É a seção onde a **capacidade**
— quantos produtos a peça precisa mostrar — elimina antes de qualquer
outro eixo entrar em jogo.

# Chave de decisão

`product_slots` e `itens: {min,max}` são o discriminante principal:
definem quantos produtos a loja precisa encaixar ali, e isso já corta a
lista a 1–2 candidatas antes de olhar `momento` ou `objeção`. Quando duas
variantes empatam em capacidade, `momento` e `objeção` desempatam.

| Variante | Slots | Itens (min–max) | Momento | Objeção |
|---|---|---|---|---|
| [[products-2-tres-ingredientes]] | 0 | 3–3 | consideração | composição-formulação |
| [[products-4-produto-unico-com-prazo]] | 1 | 1–1 | campanha-promocional | preço-valor |
| [[products-3-arco-de-novidades]] | 1 | 4–4 | lançamento | — |
| [[products-6-vitrine-de-sale]] | 2 | 2–2 | sale-recorrente | — |
| [[products-7-dois-com-galeria-de-angulos]] | 2 | 2–2 | lançamento | qualidade-eficácia |
| [[products-5-tres-com-selo-de-percentual]] | 3 | 3–3 | campanha-promocional | escolha-variedade |
| [[products-8a-quatro-recomendacoes]] | 4 | 4–4 | cross-sell, catálogo-mais-vendidos | escolha-variedade |
| [[products-9-grade-de-tamanho]] | 4 | 4–4 | queima-de-estoque | disponibilidade-urgência |
| [[products-8b-grade-3x3]] | 9 | 6–9 | catálogo-mais-vendidos | amplitude-de-catálogo |

**Como ler:** slots=2 empata entre products-6 e products-7 — só `momento`
(sale-recorrente vs. lançamento) e `objeção` ([] vs. qualidade-eficácia)
separam. O mesmo empate acontece em slots=4 entre products-8a e
products-9: capacidade idêntica, mas `momento` e `objeção` completamente
diferentes (cross-sell/escolha-variedade vs. queima-de-estoque/urgência).
Sem esses dois eixos, a capacidade sozinha não decide.

# Onde a seção não cobre

- Salto de capacidade: nenhuma variante com `product_slots` 5, 6, 7 ou 8 —
  o catálogo pula de 4 para 9 direto.
- **Dispositivo não coberto** (batch 6249aef2): grade de 2–3 produtos com
  **preço cheio**, sem selo de desconto, para toque sem incentivo. Ver
  [[products-grade-preco-cheio]].
- Momento: nenhuma products para `welcome-1`, `welcome-meio`,
  `welcome-tardio`, `carrinho-abandonado`, `checkout-abandonado`,
  `reengajamento`, `transacional`, `browse-abandonment`,
  `sazonal-data-comemorativa` ou `gift-card`.
