---
tipo: eixo
eixo: momento
valor: checkout-abandonado
procedencia: inferida
status: aprovada
---

> Derivado por código de `flow_type` + `email_number` (`momentoDoEmail` em curador-vault.ts). Filtro do passo 5, não eixo de ranking; não é lido pelo LLM. Mudou o vocabulário, muda o mapa no mesmo commit.

# Checkout abandonado

Mais fundo no funil que `carrinho-abandonado`: a pessoa já iniciou o
checkout — em muitos casos já preencheu endereço ou pagamento — e saiu antes
de confirmar. A intenção de compra é mais forte e mais recente; a objeção
provável já não é "isso vale a pena", é fricção pontual: erro de pagamento,
custo de frete revelado tarde, indecisão de última hora.

# Como usar na seleção

Uma variante com `momento: [checkout-abandonado]` deve ser mais direta e
menos argumentativa que a de `carrinho-abandonado` — a pessoa já decidiu
comprar, só não terminou. Priorizar remoção de fricção (link direto de volta
ao checkout com o carrinho preservado, reasseguramento sobre pagamento e
segurança) sobre reapresentação de tese ou prova social.

# Procedência

Esta distinção foi inferida, não extraída de doutrina existente do vault.
Utilizável, mas ainda não validada por quem opera as lojas.
