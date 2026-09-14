---
tipo: eixo
eixo: momento
valor: queima-de-estoque
procedencia: inferida
status: aprovada
---

> Derivado por código de `flow_type` + `email_number` (`momentoDoEmail` em curador-vault.ts). Filtro do passo 5, não eixo de ranking; não é lido pelo LLM. Mudou o vocabulário, muda o mapa no mesmo commit.

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

# Procedência

Esta distinção foi inferida, não extraída de doutrina existente do vault.
Utilizável, mas ainda não validada por quem opera as lojas.
