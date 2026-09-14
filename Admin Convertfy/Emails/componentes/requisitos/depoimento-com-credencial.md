---
tipo: requisito
familia: prova-social
classe: reviews
fonte_resolucao: reviews_bank
default_quando_desconhecido: false
valor: depoimento-com-credencial
status: aprovada
procedencia: inventario
---

# O que é

Existe um depoimento de cliente com credencial nomeável — cargo,
título, autoridade reconhecível — não um cliente comum sem qualificação.

# Por que é eliminatório e não preferência

A estrutura inteira existe para carregar autoridade, e o slot de cargo
é onde essa autoridade se mostra. Com depoimento de cliente comum, esse
slot fica vazio — e sem ele, a variante perde o sentido de existir,
porque não há mais nada nela além dessa credencial.

Da prosa do inventário, verbatim (`review 1`): *"Sem credencial.
Depoimento de cliente comum não sustenta a variante — o slot de cargo
fica vazio e a estrutura perde o sentido."*

# Como se resolve
Depende do banco de reviews expor metadados (tamanho, foto, credencial).
Fora do escopo até lá: **não elimina**. Quando o banco expuser, o resolvedor
consulta `reviews_bank` da loja.