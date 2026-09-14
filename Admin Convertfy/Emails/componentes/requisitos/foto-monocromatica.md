---
tipo: requisito
familia: ativo-visual
classe: diretiva_imagem
fonte_resolucao: nenhuma
default_quando_desconhecido: false
valor: foto-monocromatica
status: aprovada
procedencia: inventario
---

# O que é

Existe foto de produto ou campanha tratada em monocromia — não fundo
variado nem alto contraste.

# Por que é eliminatório e não preferência

O texto é sobreposto diretamente sobre o sujeito da foto, sem caixa de
proteção. A legibilidade desse texto depende do tratamento monocromático
reduzir o contraste local da imagem; sem monocromia, o texto sobre o
sujeito simplesmente some — não fica difícil de ler, fica ilegível.

Da prosa do inventário, verbatim (`hero 6`): *"Foto com fundo variado ou
contraste alto — sem monocromia, o texto sobre o sujeito some."*

# Como se resolve
Não se resolve contra a loja: o pipeline **gera** a imagem com esta
propriedade. Entra em `diretivas_de_imagem` da variante e no brief da foto
(`photo_direction`); `image_format` confere por pixel o que der conferir.
**Nunca elimina variante.**