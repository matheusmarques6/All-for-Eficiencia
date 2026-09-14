---
tipo: requisito
familia: prova-social
classe: reviews
fonte_resolucao: reviews_bank
default_quando_desconhecido: false
valor: tres-reviews-distintos
status: aprovada
procedencia: inventario
---

# O que é

Existem pelo menos três reviews que citam produtos diferentes entre
si — não o mesmo produto repetido nas três linhas.

# Por que é eliminatório e não preferência

O mecanismo da variante é mostrar variedade de produtos aprovados por
clientes diferentes. Repetir o mesmo produto nas três linhas não
enfraquece esse efeito — anula ele, porque a variedade É o argumento,
não um enfeite dele.

Da prosa do inventário, verbatim (`review 6`): *"Menos de três
depoimentos com produtos distintos. Repetir o mesmo produto nas três
linhas anula o mecanismo."*

# Como se resolve
Depende do banco de reviews expor metadados (tamanho, foto, credencial).
Fora do escopo até lá: **não elimina**. Quando o banco expuser, o resolvedor
consulta `reviews_bank` da loja.