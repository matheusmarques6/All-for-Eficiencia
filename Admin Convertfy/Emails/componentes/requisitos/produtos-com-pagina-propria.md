---
tipo: requisito
familia: dado-operacional
classe: gate
fonte_resolucao: products_json
default_quando_desconhecido: false
valor: produtos-com-pagina-propria
status: aprovada
procedencia: inventario
---

# O que é

Cada produto do catálogo tem uma página própria — uma URL individual —
para onde um CTA específico pode apontar.

# Por que é eliminatório e não preferência

Variantes que dão um CTA por linha de produto pressupõem que cada item
tem destino individual navegável. O próprio inventário registra o
inverso como razão de existir de outra família de variante: quando cada
item precisa de destino próprio, a loja precisa de uma grade com CTA por
linha — o que só funciona se esse destino existir por produto.

Da prosa do inventário, verbatim (`produtos 3`): *"Quando cada item
precisa de destino próprio — use uma grade de produtos com CTA por
linha."* Sem página própria por produto, essa condição nunca se cumpre e
a variante de CTA-por-linha não tem para onde apontar cada botão.

# Como se resolve
Resolvedor (código): `products.json` → produtos publicados com `handle`
(URL própria acessível). `false` → elimina.