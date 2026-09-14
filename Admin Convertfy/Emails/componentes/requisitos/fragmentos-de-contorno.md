---
tipo: requisito
familia: ativo-visual
classe: diretiva_imagem
fonte_resolucao: nenhuma
default_quando_desconhecido: false
valor: fragmentos-de-contorno
status: aprovada
procedencia: inventario
---

# O que é

Existem ativos de imagem com fragmentos de contorno — molduras
parciais, elementos gráficos que emolduram o recorte do produto.

# Por que é eliminatório e não preferência

A variante depende desses fragmentos para fechar visualmente a
composição em volta do produto. Colar uma foto comum, sem esses
fragmentos preparados, deixa a moldura visivelmente aberta — o produto
fica solto no layout em vez de emoldurado por ele.

Da prosa do inventário, verbatim (`produto 8 - 4 produtos`): *"Sem
ativos com fragmentos de contorno — colar uma foto comum deixa a
moldura aberta."*

# Como se resolve
Não se resolve contra a loja: o pipeline **gera** a imagem com esta
propriedade. Entra em `diretivas_de_imagem` da variante e no brief da foto
(`photo_direction`); `image_format` confere por pixel o que der conferir.
**Nunca elimina variante.**