---
tipo: requisito
familia: prova-social
classe: reviews
fonte_resolucao: reviews_bank
default_quando_desconhecido: false
valor: ugc-autorizado
status: aprovada
procedencia: inventario
---

# O que é

Existe conteúdo gerado por usuário — foto de cliente real usando o
produto — com autorização de uso concedida, não foto de banco de
imagem nem modelo profissional posando.

# Por que é eliminatório e não preferência

A seção inteira depende dessa foto real, não só um bloco dela. Trocar
por foto de estúdio não deixa a peça mais genérica — derruba o
mecanismo, porque o argumento da variante é "isto é um cliente de
verdade", e uma foto de banco de imagem contradiz a própria afirmação
que a seção faz.

Da prosa do inventário, verbatim (`review 8`): *"Sem UGC autorizado. A
seção inteira depende de foto de pessoa real; substituir por foto de
estúdio derruba o mecanismo."*

# Como se resolve
Depende do banco de reviews expor metadados (tamanho, foto, credencial).
Fora do escopo até lá: **não elimina**. Quando o banco expuser, o resolvedor
consulta `reviews_bank` da loja.