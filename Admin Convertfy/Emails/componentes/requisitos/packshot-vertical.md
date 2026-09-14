---
tipo: requisito
familia: ativo-visual
classe: diretiva_imagem
fonte_resolucao: nenhuma
default_quando_desconhecido: false
valor: packshot-vertical
status: aprovada
procedencia: inventario
---

# O que é

Existe packshot do produto em orientação vertical — mais alto que
largo, típico de garrafa, tubo, frasco — não item plano, roupa, serviço
ou assinatura.

# Por que é eliminatório e não preferência

O layout empareia o packshot vertical à esquerda com uma coluna de
texto à direita, na mesma proporção 293×155. Peça de roupa, item plano,
serviço ou assinatura não produz esse tipo de recorte — não é que o
resultado fique menos bonito, é que o formato do produto não cabe no
molde geométrico que a variante pressupõe.

Da prosa do inventário, verbatim (`review 6`): *"Produto sem packshot
vertical: peça de roupa, item plano, serviço, assinatura."*

# Como se resolve
Não se resolve contra a loja: o pipeline **gera** a imagem com esta
propriedade. Entra em `diretivas_de_imagem` da variante e no brief da foto
(`photo_direction`); `image_format` confere por pixel o que der conferir.
**Nunca elimina variante.**