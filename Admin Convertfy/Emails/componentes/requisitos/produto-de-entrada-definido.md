---
tipo: requisito
familia: catalogo
classe: gate
fonte_resolucao: products_json
default_quando_desconhecido: false
valor: produto-de-entrada-definido
status: aprovada
procedencia: inventario
---

# O que é

A loja tem um produto de entrada claro — kit, starter pack, bundle —
que funciona como porta de entrada da categoria para quem nunca comprou.

# Por que é eliminatório e não preferência

A variante de produto único é construída para justificar antes de
mostrar o preço: dois parágrafos de contexto, um card, um selo de
prazo. Sem um produto de entrada definido, não há o que esses dois
parágrafos estejam justificando — a variante fica sem assunto.

Da prosa do inventário, verbatim (`produtos 4`): *"Alimentos, bebidas,
suplementos, beleza, pet, assinatura — categorias com produto de entrada
definido."*

# Como se resolve
Resolvedor (código): `store_top_products[0]` existe (mais vendido
identificado). `false` → elimina.