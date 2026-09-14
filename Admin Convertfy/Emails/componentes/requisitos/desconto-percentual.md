---
tipo: requisito
familia: comercial
classe: gate
fonte_resolucao: outline
default_quando_desconhecido: false
valor: desconto-percentual
status: aprovada
procedencia: inventario
---

# O que é

A loja está rodando um desconto percentual — não fixo em R$, não frete
grátis — que pode ser exibido como número puro ("35% OFF").

# Por que é eliminatório e não preferência

Em algumas variantes o percentual é o maior elemento tipográfico da peça
inteira, maior que o próprio wordmark da marca — a hierarquia é invertida
de propósito para a oferta dominar. Sem desconto percentual, esse slot
central não tem o que exibir e a peça perde o elemento que a organiza.

Da prosa do inventário, verbatim (`hero 6`): *"Marca premium que não
desconta — o percentual em 60px define a peça."*

# Como se resolve
Resolvedor (código): `email_outline_templates` → a oferta do toque é
percentual (não frete, não brinde). `false` → elimina.