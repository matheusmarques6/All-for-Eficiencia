---
tipo: requisito
familia: comercial
valor: desconto-automatico-sem-cupom
verificavel_hoje: false
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

# Como o agente verifica

**Não verifica automaticamente hoje.** Nenhum campo de `client_stores`
responde a esta pergunta. Ver [[_parametros-da-loja]].
