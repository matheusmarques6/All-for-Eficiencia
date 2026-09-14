---
tipo: requisito
familia: prova-social
classe: reviews
fonte_resolucao: reviews_bank
default_quando_desconhecido: false
valor: selo-compra-verificada
status: aprovada
procedencia: inventario
---

# O que é

A loja ou a plataforma de reviews tem selo real de "compra verificada"
associado aos depoimentos — não é decoração aplicada pela IA.

# Por que é eliminatório e não preferência

O selo é o mecanismo central da variante, não um detalhe visual a mais.
Sem ele o mecanismo inteiro — a promessa de que aquele review vem de
uma compra real — fica vazio, porque não existe outro elemento na
variante que carregue essa promessa.

Da prosa do inventário, verbatim (`review 7`): *"Sem selo de compra
verificada — o mecanismo central fica vazio."*

# Como se resolve
Depende do banco de reviews expor metadados (tamanho, foto, credencial).
Fora do escopo até lá: **não elimina**. Quando o banco expuser, o resolvedor
consulta `reviews_bank` da loja.