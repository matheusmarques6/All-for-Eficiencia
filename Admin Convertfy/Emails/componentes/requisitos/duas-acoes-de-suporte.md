---
tipo: requisito
familia: catalogo
classe: gate
fonte_resolucao: pesquisa
default_quando_desconhecido: false
valor: duas-acoes-de-suporte
status: aprovada
procedencia: inventario
---

# O que é

Existem duas ações reais de suporte, com pesos diferentes, que a loja pode
oferecer no mesmo e-mail (conta e central de ajuda, chat e FAQ, consultoria e
catálogo).

# Por que é eliminatório e não preferência

A variante é construída em volta de dois CTAs hierárquicos — um primário
sólido, um secundário de contorno. Sem uma segunda alternativa real, o botão
de contorno não tem para onde apontar: não existe versão de um CTA só.

Da prosa do inventário, verbatim (`hero 9`, "welcome - hero section 9"):
*"Uma ação só — sem a segunda alternativa, o botão de contorno fica vazio de
função."* A mesma variante define o que conta como as duas ações: *"Quando
existem duas ações reais de suporte com pesos diferentes (conta e central de
ajuda, chat e FAQ, consultoria e catálogo)."*

# Como se resolve
Resolvedor (código, com citação): pesquisa da marca → duas ações de
suporte reais (troca fácil, atendimento X) com trecho. Senão `false` → elimina.