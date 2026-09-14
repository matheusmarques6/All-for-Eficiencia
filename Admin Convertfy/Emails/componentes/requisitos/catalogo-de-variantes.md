---
tipo: requisito
familia: catalogo
classe: gate
fonte_resolucao: products_json
default_quando_desconhecido: false
valor: catalogo-de-variantes
status: aprovada
procedencia: inventario
---

# O que é

O catálogo tem variantes reais do mesmo produto — cor, aroma, formulação —
que podem ser citadas separadamente, uma por linha, sem repetir o
mesmo item.

# Por que é eliminatório e não preferência

Mecânicas que exigem "um produto por depoimento, todos diferentes"
dependem de haver variantes distintas do catálogo para preencher cada
linha. Sem catálogo de variantes, a única forma de cumprir a regra seria
repetir o mesmo item, o que a própria orientação de copy da variante
proíbe.

Da prosa do inventário, verbatim (`review 6`, texto de "Quando NÃO
usar"): *"Menos de três depoimentos com produtos distintos. Repetir o
mesmo produto nas três linhas anula o mecanismo."*

# Como se resolve
Resolvedor (código): `products.json` → produtos com mais de uma `variant`
com opções distintas (cor, sabor, tamanho). `false` → elimina.