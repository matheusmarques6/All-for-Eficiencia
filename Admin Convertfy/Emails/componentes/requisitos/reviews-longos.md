---
tipo: requisito
familia: prova-social
classe: reviews
fonte_resolucao: reviews_bank
default_quando_desconhecido: false
valor: reviews-longos
status: aprovada
procedencia: inventario
---

# O que é

Existem reviews de clientes com pelo menos cerca de 80 caracteres — não
notas curtas de uma linha ("Ótimo!", "Amei").

# Por que é eliminatório e não preferência

O layout empareia uma foto alta com uma coluna de texto ao lado. Com
review curto, essa coluna fica vazia na maior parte da altura — não é
que o texto fique pobre, é que o equilíbrio visual do bloco inteiro
desmonta, porque a coluna de texto é metade da composição.

Da prosa do inventário, verbatim (`review 3`): *"Reviews curtos (menos
de ~80 caracteres). A coluna fica vazia ao lado de uma foto alta e o
bloco desmonta."*

# Como se resolve
Depende do banco de reviews expor metadados (tamanho, foto, credencial).
Fora do escopo até lá: **não elimina**. Quando o banco expuser, o resolvedor
consulta `reviews_bank` da loja.