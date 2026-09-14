---
tipo: requisito
familia: comercial
classe: gate
fonte_resolucao: outline
default_quando_desconhecido: false
valor: cupom-ativo
status: aprovada
procedencia: inventario
---

# O que é

Existe um código de desconto válido, entregue ao contato, que a loja pode
publicar no e-mail.

# Por que é eliminatório e não preferência

As variantes que declaram este requisito são construídas em volta do
código: pílula, barra do topo, label do botão. Sem cupom os slots ficam
vazios e a peça não degrada — desmonta. Não existe versão "sem desconto"
dessas variantes.

Da prosa do inventário, verbatim (`offer 3`): *"Sem cupom. A pílula do
código é o centro da variante e não tem substituto."*

# Como se resolve
Resolvedor (código): `email_outline_templates` do flow → o toque tem
`coupon_code` preenchido e válido. `false` → elimina.