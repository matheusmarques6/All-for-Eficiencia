---
tipo: requisito
familia: ativo-visual
classe: diretiva_imagem
fonte_resolucao: nenhuma
default_quando_desconhecido: false
valor: foto-de-cena-ambiente
status: aprovada
procedencia: inventario
---

# O que é

Existe foto de cena/ambiente do produto em contexto — mesa posta, uso
real, cenário — não produto isolado em estúdio.

# Por que é eliminatório e não preferência

Toda a variante flutua sobre uma única foto de cena que se estende do
topo ao fim da seção — não há bloco de cor separado nem segundo ativo.
Um produto que precisa ser mostrado isolado ou em detalhe não serve como
base: a foto que a variante exige é ambiente, não packshot, e as duas
coisas não são intercambiáveis.

Da prosa do inventário, verbatim (`offer 2`): *"Produto que precisa ser
mostrado isolado ou em detalhe. A foto aqui é ambiente, não packshot."*

# Como se resolve
Não se resolve contra a loja: o pipeline **gera** a imagem com esta
propriedade. Entra em `diretivas_de_imagem` da variante e no brief da foto
(`photo_direction`); `image_format` confere por pixel o que der conferir.
**Nunca elimina variante.**