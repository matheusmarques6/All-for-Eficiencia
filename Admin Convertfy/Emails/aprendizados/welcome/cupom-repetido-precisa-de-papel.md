---
tipo: aprendizado
flow_type: welcome
serve_a: [welcome-1, welcome-2, welcome-3, welcome-4, welcome-5, welcome-6]
origem_estrutura: avelmore-deadline-objecao
autor: Convertfy
tipo_regra: preferencia
aplica_a: [welcome, hero, offer, products]
status: aprovada
---

# Observação

Em [[avelmore-deadline-objecao]] o cupom aparece quatro vezes: hero,
offer e mais duas menções no bloco de produtos — a mesma coisa quatro vezes.

Em [[avelmore-inspecao-antecipada]] o cupom aparece duas vezes e funciona, porque
cada aparição tem papel distinto: entrega no hero, fechamento no body.

# Regra derivada

Repetir a oferta só se cada aparição tiver papel próprio no argumento. Repetição
sem mudança de papel é ruído, não reforço.

# Refinamento — o número certo

A versão canônica de [[avelmore-deadline-objecao]] fecha a conta: **duas
ocorrências bastam** — hero e bloco de prazo.

E confirma o contraste com [[avelmore-inspecao-antecipada]]: lá as duas
repetições têm papéis distintos (entrega da promessa vs. fechamento do
argumento); aqui as quatro têm a mesma função.
