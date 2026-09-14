---
tipo: requisito
familia: ativo-visual
classe: gate
fonte_resolucao: brand_identity
default_quando_desconhecido: false
valor: cor-de-acento-definida
status: aprovada
procedencia: inventario
---

# O que é

A marca tem uma cor de acento definida na identidade — não apenas
preto, branco e cinza neutro.

# Por que é eliminatório e não preferência

A headline usa um trecho destacado em cor de acento para carregar o
diferencial — é esse destaque que a variante existe para produzir. Sem
cor de acento definida, o destaque não tem onde se apoiar: a variante
não perde intensidade, perde a peça central do próprio efeito
tipográfico.

Da prosa do inventário, verbatim (`hero 2`): *"Marca sem cor de acento
definida — o destaque da headline fica sem onde apoiar."*

# Como se resolve
Resolvedor (código): `store_brand_identity` → existe cor com papel de
destaque/acento (não é `client_stores.cores`). `false` → elimina.