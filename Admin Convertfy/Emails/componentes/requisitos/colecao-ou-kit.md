---
tipo: requisito
familia: catalogo
valor: colecao-ou-kit
verificavel_hoje: false
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

# Como o agente verifica

**Não verifica automaticamente hoje.** Nenhum campo de `client_stores`
responde a esta pergunta. Ver [[_parametros-da-loja]].
