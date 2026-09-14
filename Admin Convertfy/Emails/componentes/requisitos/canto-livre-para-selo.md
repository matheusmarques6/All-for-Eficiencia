---
tipo: requisito
familia: ativo-visual
classe: diretiva_imagem
fonte_resolucao: nenhuma
default_quando_desconhecido: false
valor: canto-livre-para-selo
status: aprovada
procedencia: inventario
---

# O que é

A foto do produto tem pelo menos um canto vazio, sem elemento, onde um
selo circular pode ser sobreposto sem cobrir o produto.

# Por que é eliminatório e não preferência

O selo de percentual é sobreposto diretamente na foto, não colocado ao
lado dela em um bloco separado. Sem canto livre, o selo cai sobre o
próprio produto — não fica menos elegante, fica ilegível ou esconde
parte do que deveria vender.

Da prosa do inventário, verbatim (`produtos 5`): *"Fotos sem canto
livre — o selo cai sobre o produto."*

# Como se resolve
Não se resolve contra a loja: o pipeline **gera** a imagem com esta
propriedade. Entra em `diretivas_de_imagem` da variante e no brief da foto
(`photo_direction`); `image_format` confere por pixel o que der conferir.
**Nunca elimina variante.**