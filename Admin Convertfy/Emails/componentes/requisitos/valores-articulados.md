---
tipo: requisito
familia: catalogo
classe: gate
fonte_resolucao: pesquisa
default_quando_desconhecido: false
valor: valores-articulados
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

# Como se resolve
Resolvedor (código, com citação): pesquisa da marca → valores da marca
articulados em texto citável. Sem trecho, `false` → elimina.