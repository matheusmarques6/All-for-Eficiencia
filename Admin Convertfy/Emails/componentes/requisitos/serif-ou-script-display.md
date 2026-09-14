---
tipo: requisito
familia: ativo-visual
classe: gate
fonte_resolucao: brand_identity
default_quando_desconhecido: false
valor: serif-ou-script-display
status: aprovada
procedencia: inventario
---

# O que é

A marca tem uma fonte display serifada ou script definida na
identidade — não apenas a fonte de texto corrido usada no restante do
e-mail.

# Por que é eliminatório e não preferência

O lockup tipográfico é montado com script sobreposto a serif de alto
contraste; é a combinação das duas que sustenta a leitura. Sem essa
dupla, o lockup não se sustenta como composição — a recomendação do
próprio inventário, nesse caso, é trocar de variante inteira.

Da prosa do inventário, verbatim (`hero 4`): *"Sem identidade
tipográfica própria. Sem script + serif display, o lockup não se
sustenta — use o welcome de fundo fotográfico simples."*

# Como se resolve
Resolvedor (código): `store_brand_identity` → fonte display serif ou
script cadastrada. `false` → elimina.