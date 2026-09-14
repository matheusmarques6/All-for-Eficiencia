---
tipo: requisito
familia: ativo-visual
classe: diretiva_imagem
fonte_resolucao: nenhuma
default_quando_desconhecido: false
valor: foto-com-pessoas
status: aprovada
procedencia: inventario
---

# O que é

Existe foto de pessoa real usando ou perto do produto — não packshot
isolado sobre fundo neutro.

# Por que é eliminatório e não preferência

A colagem é feita para alternar cenas com pessoas; um packshot no lugar
de uma dessas cenas não completa a colagem — esvazia ela, porque o que
sustenta o formato é justamente o contraste entre cenas humanas que
conversam entre si.

Da prosa do inventário, verbatim (`body 2`): *"Sem fotografia de
pessoas — packshot na colagem esvazia o bloco."*

# Como se resolve
Não se resolve contra a loja: o pipeline **gera** a imagem com esta
propriedade. Entra em `diretivas_de_imagem` da variante e no brief da foto
(`photo_direction`); `image_format` confere por pixel o que der conferir.
**Nunca elimina variante.**