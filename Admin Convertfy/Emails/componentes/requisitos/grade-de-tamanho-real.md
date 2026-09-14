---
tipo: requisito
familia: dado-operacional
classe: gate
fonte_resolucao: products_json
default_quando_desconhecido: false
valor: grade-de-tamanho-real
status: aprovada
procedencia: inventario
---

# O que é

O produto tem variação real de tamanho — P/M/G, numeração — com estoque
individual por tamanho, não uma categoria de tamanho único.

# Por que é eliminatório e não preferência

Duas condições eliminam essa variante e as duas vêm do mesmo lugar: sem
tamanho, a grade não tem eixo para desenhar; e se todos os tamanhos
estão disponíveis, a grade não gera urgência nenhuma — o bloco existe
para expor ruptura real, não para listar opções.

Da prosa do inventário, verbatim (`produtos 9`): *"Produto sem tamanho —
beleza, alimentos, casa; a grade não tem o que mostrar."* E: *"Todos os
tamanhos disponíveis — sem esgotados, a grade não gera urgência e o
bloco fica sem função."*

# Como se resolve
Resolvedor (código): `products.json` → alguma `option` de nome
tamanho/size com ≥3 valores. `false` → elimina.