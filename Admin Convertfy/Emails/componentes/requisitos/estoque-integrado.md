---
tipo: requisito
familia: dado-operacional
valor: estoque-integrado
verificavel_hoje: false
status: aprovada
procedencia: inventario
---

# O que é

A loja expõe, via API, o estoque real por SKU ou variante — não apenas
o catálogo de produtos, o número de unidades disponíveis.

# Por que é eliminatório e não preferência

A grade de estoque existe para mostrar ruptura real e gerar urgência
genuína. Sem esse dado, ela vira decoração — o e-mail estaria prometendo
uma escassez que ninguém verificou, o que é o oposto do que a variante
existe para fazer.

Da prosa do inventário, verbatim (`produtos 9`): *"Sem dado de estoque
real — a grade vira decoração e o e-mail promete o que não pode
cumprir."*

# Como o agente verifica

**Não verifica automaticamente hoje.** Nenhum campo de `client_stores`
responde a esta pergunta. Ver [[_parametros-da-loja]].
