---
tipo: requisito
familia: comercial
classe: gate
fonte_resolucao: outline
default_quando_desconhecido: false
valor: desconto-automatico-sem-cupom
status: aprovada
procedencia: inventario
---

# O que é

O desconto se aplica sozinho no checkout — a pessoa não precisa digitar
nenhum código.

# Por que é eliminatório e não preferência

Estas variantes não reservam espaço algum para um código: inserir um
cupom nelas quebra a escala do layout que foi desenhado em volta do
número puro. Não é que o cupom fique feio — é que não há onde ele
caiba.

Da prosa do inventário, verbatim (`hero 7`): *"Oferta com código — a
variante não tem onde acomodar o código sem quebrar a escala."*
Reforçado em `offer 2`: *"Se o desconto é automático, dizer — é o que
remove a objeção do cupom."*

# Como se resolve
Resolvedor (código): `email_outline_templates` → oferta marcada como
automática no checkout, sem código. `false` → elimina.