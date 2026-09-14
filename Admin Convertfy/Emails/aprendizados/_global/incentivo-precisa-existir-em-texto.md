---
tipo: aprendizado
escopo: cross-flow
aplica_a: [welcome, abandoned_cart, browse_abandonment, post_purchase]
serve_a: [todos]
origem_estrutura: avelmore-inspecao-antecipada
autor: Convertfy
status: aprovada
tipo_regra: restricao-dura
---

# Observação

Em [[avelmore-inspecao-antecipada]], o incentivo é entregue no hero — que é uma
imagem. Com imagens bloqueadas pelo cliente de e-mail, **o código some** e o
e-mail quebra o contrato do opt-in em silêncio: a pessoa abriu para pegar o
código e não encontra nada.

A falha não aparece em teste visual. Só aparece para quem tem imagens
desativadas — e essa fatia nunca é zero.

# Regra derivada

Código de desconto, valor do incentivo e prazo existem em **texto real**, nunca
apenas dentro de imagem.

Vale para qualquer flow que entregue incentivo. Se o dispositivo escolhido põe o
código na arte, ele precisa de duplicata em texto — ou é descartado.
