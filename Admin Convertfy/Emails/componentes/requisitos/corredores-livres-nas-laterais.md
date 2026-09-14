---
tipo: requisito
familia: ativo-visual
classe: diretiva_imagem
fonte_resolucao: nenhuma
default_quando_desconhecido: false
valor: corredores-livres-nas-laterais
status: aprovada
procedencia: inventario
---

# O que é

A foto do produto tem espaço vazio — corredor — nas laterais, sem
elemento nem textura ocupando essa área.

# Por que é eliminatório e não preferência

A variante sobrepõe rótulos de texto exatamente nesses corredores. Sem
eles, os rótulos caem sobre o produto em vez de ao lado dele, e como o
produto tem textura e detalhe, o texto sobreposto fica ilegível — não é
um problema de acabamento, é o slot de texto não ter onde existir.

Da prosa do inventário, verbatim (`produtos 2`): *"Foto sem corredores
livres nas laterais — os rótulos caem sobre o produto e nada fica
legível."*

# Como se resolve
Não se resolve contra a loja: o pipeline **gera** a imagem com esta
propriedade. Entra em `diretivas_de_imagem` da variante e no brief da foto
(`photo_direction`); `image_format` confere por pixel o que der conferir.
**Nunca elimina variante.**