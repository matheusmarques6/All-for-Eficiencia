---
tipo: eixo
eixo: momento
valor: queima-de-estoque
status: aprovada
---

# Queima de estoque

Liquidação de item que precisa sair do estoque — a motivação é operacional
(fim de coleção, excesso de compra, descontinuação), não sazonal nem
editorial. O desconto tende a ser mais agressivo que em `campanha-promocional`
comum, e a disponibilidade é genuinamente limitada, não simulada.

# Como usar na seleção

Uma variante com `momento: [queima-de-estoque]` pode declarar quantidade
finita real com honestidade — este é um dos poucos momentos em que "últimas
unidades" tende a ser verdade, não recurso retórico. Ainda assim, todo número
citado precisa de lastro: ver
[[numeros-de-escassez-precisam-de-backing]]. A objeção dominante costuma ser
`disponibilidade-urgencia` combinada com `preco-valor`.
