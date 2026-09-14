---
tipo: requisito
familia: dado-operacional
classe: plataforma
fonte_resolucao: nenhuma
default_quando_desconhecido: false
valor: estoque-integrado
status: superada
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

# Como se resolve
Superado: isto é configuração de ESP/loja fora da geração, não uma
pergunta sobre a loja. A nota fica no repo como histórico
(`status: superada`, fora do sync).