---
tipo: requisito
familia: ativo-visual
classe: gate
fonte_resolucao: brand_identity
default_quando_desconhecido: false
valor: duas-ou-tres-cores-de-identidade
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

# Como se resolve
Resolvedor (código): `store_brand_identity` → 2–3 cores com papéis
definidos (fundo, texto, destaque). `false` → elimina.