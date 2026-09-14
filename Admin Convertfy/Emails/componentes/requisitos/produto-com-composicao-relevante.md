---
tipo: requisito
familia: catalogo
classe: gate
fonte_resolucao: products_json
default_quando_desconhecido: false
valor: produto-com-composicao-relevante
status: aprovada
procedencia: inventario
---

# O que é

O produto tem composição, ingredientes ou materiais que valem a pena
listar — categorias como beleza, alimento, suplemento — não moda,
acessório ou eletrônico de consumo.

# Por que é eliminatório e não preferência

O infográfico "quantidade → o que tem → o que não tem" é sobre
composição. Em categorias sem composição relevante não existe conteúdo
nenhum para preencher esse formato — não é que a composição fique fraca,
é que ela não existe como argumento naquela categoria.

Da prosa do inventário, verbatim (`produtos 2`): *"Produto sem
composição relevante — moda, acessório, eletrônico de consumo."*

# Como se resolve
Resolvedor (código): `products.json` → `body_html` cita
composição/ingredientes/materiais de forma substantiva. `false` → elimina.