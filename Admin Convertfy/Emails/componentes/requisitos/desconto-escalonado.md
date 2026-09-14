---
tipo: requisito
familia: comercial
classe: gate
fonte_resolucao: outline
default_quando_desconhecido: false
valor: desconto-escalonado
status: aprovada
procedencia: inventario
---

# O que é

O desconto varia por faixa — "até 30% conforme a quantidade ou o valor
do carrinho" — não é uma porcentagem única e fechada.

# Por que é eliminatório e não preferência

O eyebrow ("Up to", "Até", "Ganhe até") só existe para modular um valor
que varia. Com desconto fechado, esse qualificador perde a função — não
tem o que qualificar — e a escala tipográfica inteira, pensada para
acomodar essa incerteza, desmonta.

Da prosa do inventário, verbatim (`hero 7`): *"Quando o desconto é
fechado e não escalonado: sem \"up to\", o eyebrow perde a função e a
escala desmonta."*

# Como se resolve
Resolvedor (código): `email_outline_templates` → mais de um degrau de
desconto declarado (ex.: 10/15/20%). `false` → elimina.