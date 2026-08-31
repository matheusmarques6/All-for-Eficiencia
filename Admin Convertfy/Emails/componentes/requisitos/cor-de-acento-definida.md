---
tipo: requisito
familia: ativo-visual
valor: cor-de-acento-definida
verificavel_hoje: false
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

# Como o agente verifica

**Não verifica automaticamente hoje**, mas o campo existe:
`client_stores.cores` (jsonb `[{name,hex,use}]`,
`20260520_client_stores_marca_fields.sql:13`) registra as cores da
identidade com um rótulo de uso (`use`) por entrada — dá para checar se
alguma entrada tem `use` de acento fora de preto/branco/cinza. O que
falta não é o dado, é o Curador cruzar `exige` contra ele: hoje `exige`
nem entra no prompt do Curador (ver
[[o-que-o-curador-ainda-nao-tem]]). Ver [[_parametros-da-loja]].
