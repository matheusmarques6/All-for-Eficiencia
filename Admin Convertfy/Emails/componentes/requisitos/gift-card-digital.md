---
tipo: requisito
familia: comercial
classe: gate
fonte_resolucao: products_json
default_quando_desconhecido: false
valor: gift-card-digital
status: aprovada
procedencia: inventario
---

# O que é

A loja vende gift card digital como produto — dado que precisa existir
no perfil da loja/cliente, não algo que se possa presumir.

# Por que é eliminatório e não preferência

A variante inteira é o pitch do gift card: headline, dois parágrafos e
CTA nomeando o produto. Sem a loja vender gift card digital, não há o
que a peça esteja vendendo — o requisito não é estético, é de catálogo.

Da prosa do inventário, verbatim (`body 3`): *"Clientes sem gift card
digital (óbvio, mas o Architect precisa do dado no perfil do cliente:
\"tem gift card? sim/não\")."*

# Como se resolve
Resolvedor (código): `https://<loja>/products.json` → algum produto com
`gift_card: true` ou `product_type`/`title` contendo "gift". `false` → elimina.