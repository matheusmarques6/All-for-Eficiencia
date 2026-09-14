---
tipo: requisito
familia: catalogo
classe: gate
fonte_resolucao: pesquisa
default_quando_desconhecido: false
valor: motivo-sazonal
status: aprovada
procedencia: inventario
---

# O que é

Existe um motivo sazonal real — data comemorativa, evento do calendário —
para ancorar a campanha, não uma oferta genérica vestida de sazonal
sem nenhum evento por trás.

# Por que é eliminatório e não preferência

A faixa de topo e o CTA são construídos em torno desse motivo — o nome
do evento aparece no sobrescrito, na headline, no botão. Sem um motivo
sazonal real, a seção inteira perde o que a amarra: não é uma versão
mais neutra, é uma seção sem eixo.

Da prosa do inventário, verbatim (`offer 2`): *"Marca sem motivo
sazonal para usar na faixa e no CTA — sem ele a seção perde o que a
amarra."*

# Como se resolve
Resolvedor (código, com citação): pesquisa/calendário → motivo sazonal
real e datado para esta loja. Sem ele, `false` → elimina.