---
tipo: requisito
familia: comercial
classe: gate
fonte_resolucao: outline
default_quando_desconhecido: false
valor: prazo-real
status: aprovada
procedencia: inventario
---

# O que é

Existe uma data de expiração real e verificável para a oferta — não uma
urgência genérica de "por tempo limitado" sem prazo por trás.

# Por que é eliminatório e não preferência

O selo de prazo é o mecanismo central da variante, não um enfeite. Um
prazo inventado corrói exatamente a confiança que o selo existe para
construir; e sem prazo nenhum, o selo simplesmente fica vazio — não há
versão da variante sem ele.

Da prosa do inventário, verbatim (`produtos 4`): *"Sem prazo real — o
selo é o mecanismo central e prazo falso corrói confiança."*

# Como se resolve
Resolvedor (código): `email_outline_templates` + cadência do flow → existe
prazo com data/hora real (não "por tempo limitado" vago). `false` → elimina.