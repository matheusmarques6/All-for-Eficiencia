---
tipo: requisito
familia: ativo-visual
valor: duas-ou-tres-cores-de-identidade
verificavel_hoje: false
status: aprovada
procedencia: inventario
---

# O que é

A marca tem pelo menos duas ou três cores definidas na identidade — não
uma cor única aplicada em tudo.

# Por que é eliminatório e não preferência

As barras de assinatura visual da variante existem para expressar a
paleta da marca através de blocos de cor distintos. Com marca de uma
cor só, essas barras não têm o que diferenciar entre si — ficam sem
função e, em vez de assinatura, viram ruído visual repetitivo.

Da prosa do inventário, verbatim (`hero 7`): *"Marca de uma cor só — as
barras ficam sem função e viram ruído."*

# Como o agente verifica

**Não verifica automaticamente hoje**, mas o campo existe:
`client_stores.cores` (jsonb `[{name,hex,use}]`,
`20260520_client_stores_marca_fields.sql:13`) — contar as entradas do
array responde diretamente se a marca tem duas, três ou mais cores
definidas. O que falta não é o dado, é o Curador cruzar `exige` contra
ele: hoje `exige` nem entra no prompt do Curador (ver
[[o-que-o-curador-ainda-nao-tem]]). Ver [[_parametros-da-loja]].
