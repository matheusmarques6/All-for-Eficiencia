---
tipo: requisito
familia: ativo-visual
classe: diretiva_imagem
fonte_resolucao: nenhuma
default_quando_desconhecido: false
valor: foto-estudio-fundo-claro
status: aprovada
procedencia: inventario
---

# O que é

Existe foto de produto feita em estúdio, com fundo claro e uniforme —
não fundo colorido, escuro ou de ambiente.

# Por que é eliminatório e não preferência

A variante monta o bloco de cor e a foto como uma superfície contínua,
sem costura visível entre os dois. Com fundo colorido, escuro ou de
ambiente, essa continuidade quebra e a emenda entre foto e bloco de cor
aparece — o problema não é estético isolado, é que o efeito que a
variante existe para produzir (peça sem costura) deixa de acontecer.

Da prosa do inventário, verbatim (`hero 10`): *"Foto com fundo colorido,
escuro ou de ambiente — aparece a emenda."* A condição positiva
correspondente também está registrada: *"Quando a marca tem fotografia
de estúdio em fundo claro e embalagem colorida."*

# Como se resolve
Não se resolve contra a loja: o pipeline **gera** a imagem com esta
propriedade. Entra em `diretivas_de_imagem` da variante e no brief da foto
(`photo_direction`); `image_format` confere por pixel o que der conferir.
**Nunca elimina variante.**