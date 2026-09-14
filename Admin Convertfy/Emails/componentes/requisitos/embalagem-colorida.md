---
tipo: requisito
familia: ativo-visual
classe: diretiva_imagem
fonte_resolucao: nenhuma
default_quando_desconhecido: false
valor: embalagem-colorida
status: aprovada
procedencia: inferida
---

# O que é

O produto tem embalagem colorida — a cor da embalagem funciona como
elemento visual da peça — não embalagem transparente ou neutra que se
funde ao fundo.

# Por que é eliminatório e não preferência

A variante junta fundo de estúdio claro com embalagem colorida de
propósito: é o contraste entre os dois que dá cor à composição inteira,
já que o fundo em si é neutro. Sem embalagem colorida, falta a peça
que carrega cor para dentro do quadro — a foto fica sem o elemento
cromático que o layout pressupõe.

Da prosa do inventário, verbatim (`hero 10`, condição de uso — pareada
com [[foto-estudio-fundo-claro]]): *"Quando a marca tem fotografia de
estúdio em fundo claro e embalagem colorida."*

# Como se resolve
Não se resolve contra a loja: o pipeline **gera** a imagem com esta
propriedade. Entra em `diretivas_de_imagem` da variante e no brief da foto
(`photo_direction`); `image_format` confere por pixel o que der conferir.
**Nunca elimina variante.**

# Procedência

Este requisito foi inferido, não extraído de citação do inventário nem de
doutrina do vault. O inventário só registra a condição positiva ("Quando
a marca tem fotografia de estúdio em fundo claro e embalagem
colorida...") — não há cláusula de "Quando NÃO usar" declarando
embalagem transparente ou neutra como motivo de exclusão. Utilizável,
mas ainda não validado por quem opera as lojas.
