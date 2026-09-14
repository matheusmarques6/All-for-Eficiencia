---
tipo: requisito
familia: ativo-visual
classe: diretiva_imagem
fonte_resolucao: nenhuma
default_quando_desconhecido: false
valor: acervo-por-angulo
status: aprovada
procedencia: inventario
---

# O que é

Existe acervo de fotos do mesmo produto em ângulos diferentes de
verdade — não a mesma foto recortada reaproveitada em miniaturas.

# Por que é eliminatório e não preferência

O mecanismo da variante é mostrar profundidade do produto através de
ângulos reais. Sem acervo de ângulos, a única saída é repetir a mesma
foto recortada em três miniaturas — o que denuncia a montagem em vez de
comunicar profundidade, o oposto do efeito pretendido.

Da prosa do inventário, verbatim (`produtos 7`): *"Sem acervo de
ângulos — três miniaturas com a mesma foto recortada denunciam a
montagem."*

# Como se resolve
Não se resolve contra a loja: o pipeline **gera** a imagem com esta
propriedade. Entra em `diretivas_de_imagem` da variante e no brief da foto
(`photo_direction`); `image_format` confere por pixel o que der conferir.
**Nunca elimina variante.**