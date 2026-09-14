---
tipo: requisito
familia: catalogo
classe: gate
fonte_resolucao: products_json
default_quando_desconhecido: false
valor: colecao-ou-kit
status: aprovada
procedencia: inventario
---

# O que é

Os produtos mostrados na mesma peça pertencem à mesma coleção ou kit —
têm um destino de navegação final coerente em comum.

# Por que é eliminatório e não preferência

Algumas variantes fecham dois produtos com um único CTA final. Esse CTA
só faz sentido se os dois produtos pertencerem à mesma coleção — se não
pertencerem, não existe um destino que sirva igualmente bem para os
dois, e o CTA fica sem para onde apontar de verdade.

Da prosa do inventário, verbatim (`produtos 7`): *"Produtos que não
compartilham coleção — o CTA final fica sem destino coerente."*

# Como se resolve
Resolvedor (código): `products.json` → `product_type`/`tags` indicando
kit/combo, ou `collections.json` com coleção temática. `false` → elimina.