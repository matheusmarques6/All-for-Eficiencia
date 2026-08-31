---
tipo: requisito
familia: ativo-visual
valor: serif-ou-script-display
verificavel_hoje: false
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

# Como o agente verifica

**Não verifica automaticamente hoje**, e o campo que existe só responde
em parte: `client_stores.fontes` (jsonb `{titulo,corpo}`,
`20260520_client_stores_marca_fields.sql:14`) guarda o NOME da fonte de
título, o que já reduz a busca, mas não diz se essa família é serifada
ou script — isso exige olhar a fonte (ou seu nome) e classificar, algo
que o campo por si não resolve. Resposta parcial. Ver
[[_parametros-da-loja]].
