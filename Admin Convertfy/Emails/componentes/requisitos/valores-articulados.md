---
tipo: requisito
familia: catalogo
valor: valores-articulados
verificavel_hoje: false
status: aprovada
procedencia: inventario
---

# O que é

A marca tem valores institucionais já articulados — não inventados na
hora — que podem virar selos de reforço ("sustentável", "cruelty-free",
"feito à mão").

# Por que é eliminatório e não preferência

A faixa de selos é um módulo separável da variante que existe
especificamente para reforço institucional, e entra só quando a marca
tem esses valores articulados. Sem selos de valores produzidos, a
variante completa (pitch + faixa) perde metade da estrutura — não
degrada graciosamente, cai para a variante só-pitch, que é outra nota.

Da prosa do inventário, verbatim (`body 3`): *"a marca tem valores
articulados e quer reforço institucional"* (quando usar) e *"Sem selos
de valores produzidos, usar a variante só-pitch"* (quando não usar).

# Como o agente verifica

**Não verifica automaticamente hoje.** Nenhum campo de `client_stores`
responde a esta pergunta. Existe um campo próximo — `brand_pillars`
(jsonb, 3 tiles `{label,text}`, `20260516000000_pesquisa_diagnostico.sql:9`)
— mas não é equivalente: são pilares de mensagem/posicionamento livres
produzidos pela Pesquisa & Diagnóstico, sem garantia de serem valores
institucionais nomeáveis prontos para virar selo (o pedido aqui é
especificamente "sustentável", "cruelty-free", "feito à mão" — categoria
de afirmação, não qualquer pilar de marca). Tratado como não-resposta.
Ver [[_parametros-da-loja]].
