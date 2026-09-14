---
tipo: requisito
familia: ativo-visual
classe: diretiva_imagem
fonte_resolucao: nenhuma
default_quando_desconhecido: false
valor: terco-superior-liso
status: aprovada
procedencia: inventario
---

# O que é

A foto disponível tem uma faixa lisa e uniforme no terço superior — sem
objeto, sombra dura ou variação de cor forte ali.

# Por que é eliminatório e não preferência

Essa faixa recebe todo o overlay de texto — wordmark, lockup, tagline,
cupom, CTA. Sem uma superfície lisa ali, não existe onde o texto pousar
sem cair em cima de detalhe da foto e ficar ilegível; a variante inteira
depende dessa zona limpa existir fisicamente na imagem.

Da prosa do inventário, verbatim (`hero 9`): *"Quando a foto disponível
não tem fundo de estúdio liso no terço superior."*

# Como se resolve
Não se resolve contra a loja: o pipeline **gera** a imagem com esta
propriedade. Entra em `diretivas_de_imagem` da variante e no brief da foto
(`photo_direction`); `image_format` confere por pixel o que der conferir.
**Nunca elimina variante.**