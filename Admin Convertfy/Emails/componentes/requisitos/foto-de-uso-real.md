---
tipo: requisito
familia: prova-social
classe: reviews
fonte_resolucao: reviews_bank
default_quando_desconhecido: false
valor: foto-de-uso-real
status: aprovada
procedencia: inventario
---

# O que é

Existe foto do produto sendo usado de verdade — vestido, aplicado, em
mão — não packshot de catálogo isolado.

# Por que é eliminatório e não preferência

Sem foto de uso real, a única alternativa disponível é o packshot — e
um packshot repetido três vezes deixa de comunicar "prova social" e
passa a comunicar "grade de produto". A peça não perde qualidade: ela
vira outra coisa, uma vitrine, o que contradiz o papel que a seção tem
na peça.

Da prosa do inventário, verbatim (`review 5`): *"Sem foto de uso real —
packshot repetido três vezes vira grade de produto."*

# Como se resolve
Depende do banco de reviews expor metadados (tamanho, foto, credencial).
Fora do escopo até lá: **não elimina**. Quando o banco expuser, o resolvedor
consulta `reviews_bank` da loja.