---
tipo: requisito
familia: ativo-visual
classe: diretiva_imagem
fonte_resolucao: nenhuma
default_quando_desconhecido: false
valor: ativo-composto-faixa-inteira
status: aprovada
procedencia: inventario
---

# O que é

Existe um ativo de imagem já montado como faixa inteira — composição
horizontal única — não fotos recortadas soltas que precisariam ser
compostas no HTML.

# Por que é eliminatório e não preferência

A variante exige esse ativo composto porque o zigue-zague de texto e
imagem é desenhado sobre ele como uma peça só. Com fotos recortadas em
coluna, a variante simplesmente não tem o ativo que a estrutura
pressupõe — a saída não é adaptar, é usar outra variante (uma seção de
cards).

Da prosa do inventário, verbatim (`review 7`): *"Fotos recortadas em
coluna — a variante exige o ativo composto de faixa inteira. Se o
acervo só tem recortes verticais, use uma seção de cards."*

# Como se resolve
Não se resolve contra a loja: o pipeline **gera** a imagem com esta
propriedade. Entra em `diretivas_de_imagem` da variante e no brief da foto
(`photo_direction`); `image_format` confere por pixel o que der conferir.
**Nunca elimina variante.**