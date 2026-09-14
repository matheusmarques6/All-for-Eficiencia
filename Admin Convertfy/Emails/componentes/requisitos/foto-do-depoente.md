---
tipo: requisito
familia: prova-social
classe: reviews
fonte_resolucao: reviews_bank
default_quando_desconhecido: false
valor: foto-do-depoente
status: aprovada
procedencia: inventario
---

# O que é

Existe uma foto real da pessoa que deu o depoimento — não placeholder,
não avatar genérico, não ícone.

# Por que é eliminatório e não preferência

A credibilidade que o bloco existe para construir depende dessa foto
ser real. Um placeholder ou avatar genérico não enfraquece o efeito —
derruba ele, porque o mecanismo é "esta pessoa existe, veja o rosto
dela", e sem a foto essa afirmação não se sustenta.

Da prosa do inventário, verbatim (`review 1`): *"Sem foto do depoente.
Placeholder ou avatar genérico derruba a credibilidade que o bloco
existe para construir."*

# Como se resolve
Depende do banco de reviews expor metadados (tamanho, foto, credencial).
Fora do escopo até lá: **não elimina**. Quando o banco expuser, o resolvedor
consulta `reviews_bank` da loja.