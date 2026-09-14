---
tipo: requisito
familia: ativo-visual
classe: diretiva_imagem
fonte_resolucao: nenhuma
default_quando_desconhecido: false
valor: foto-de-campanha-propria
status: aprovada
procedencia: inventario
---

# O que é

Existe uma foto de campanha produzida pela própria marca — não banco de
imagem genérico.

# Por que é eliminatório e não preferência

Nestas variantes uma única foto cobre o e-mail inteiro; ela é a base de
tudo o que vem sobreposto (wordmark, cupom, CTA). Banco de imagem em
proporção incomum denuncia a marca de forma visível, e não há segundo
ativo na peça para disfarçar isso — a foto própria não é acabamento, é
a estrutura inteira.

Da prosa do inventário, verbatim (`hero 4`): *"Sem foto de campanha.
Banco de imagem em 598 × 1150 denuncia a marca."*

# Como se resolve
Não se resolve contra a loja: o pipeline **gera** a imagem com esta
propriedade. Entra em `diretivas_de_imagem` da variante e no brief da foto
(`photo_direction`); `image_format` confere por pixel o que der conferir.
**Nunca elimina variante.**