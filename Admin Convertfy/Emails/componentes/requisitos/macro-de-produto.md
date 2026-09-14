---
tipo: requisito
familia: ativo-visual
classe: diretiva_imagem
fonte_resolucao: nenhuma
default_quando_desconhecido: false
valor: macro-de-produto
status: aprovada
procedencia: inventario
---

# O que é

Existe uma foto em macro/close-up do produto, capaz de provar em detalhe um
diferencial de material, acabamento ou processo — não um packshot inteiro
centralizado.

# Por que é eliminatório e não preferência

O mecanismo da variante é mostrar o diferencial em close extremo, cortado nas
laterais e no topo. Sem esse ativo não há substituto: um packshot centralizado
muda o registro da peça para "catálogo", e sem diferencial visível em close a
headline promete o que a foto não entrega.

Da prosa do inventário, verbatim (`hero 2`, "welcome - hero section 2"):
*"Sem macro de produto disponível. Packshot inteiro centralizado transforma a
peça em catálogo."* Reforço na mesma variante: *"Produto sem diferencial
visível. Se a qualidade não aparece em close, a headline promete o que a foto
não entrega."*

# Como se resolve
Não se resolve contra a loja: o pipeline **gera** a imagem com esta
propriedade. Entra em `diretivas_de_imagem` da variante e no brief da foto
(`photo_direction`); `image_format` confere por pixel o que der conferir.
**Nunca elimina variante.**