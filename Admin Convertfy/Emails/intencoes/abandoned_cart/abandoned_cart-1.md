---
tipo: intencao
flow_type: abandoned_cart
email_number: 1
status: rascunho
fonte: "Conhecimento/Advisors/Max/flows/cart-checkout-abandon.md — §A sequência, Email 1 (bruto L3798-3881, L2731, L2741); §O racional dele (bruto L3794); Conhecimento/Advisors/Max/flows/conteudo-dinamico-klaviyo.md — §O que é (bruto L2512-2520)"
modo: quebra_de_objecao
n_objecoes: [0, 1]
fonte_das_objecoes: nao_atacadas
riscos_elegiveis: [financeiro, tempo]
profundidade_minima: afirmacao
aliviadores_admissiveis: [transparencia_de_politica]
trabalhos_fixos: []
permite_reataque: false
proibicoes:
  - qualquer coisa além do item, do botão e da informação de frete
  - desconto, ou sinal de que virá um
  - FAQ, garantia ou bloco defensivo — cedo, cria a dúvida
  - bloco dinâmico ou botão abaixo da dobra
---

# Abandoned cart 1 — O item, o botão, o frete

## O que este email deve fazer

A pessoa deixou um item no carrinho — ou começou o checkout — há pouco. A
intenção é alta e recente; o trabalho é pôr o item de volta na frente dela e
tornar terminar fácil. Nas palavras do Max: "let's not distract from anything
besides, here's your product, go buy it" (cart-checkout-abandon.md §A sequência,
bruto L2731).

Conteúdo, verbatim do slide: "Simple reminder · Dynamic Klaviyo block · Brief
product Info" (bruto L3798-3881). O bloco dinâmico com o item e o botão ficam no
topo, "so the customer doesn't need to scroll" (quick tip, mesma faixa) — ver o
produto na cara ao abrir é o mecanismo (conteudo-dinamico-klaviyo.md §O que é,
bruto L2512-2520). A única objeção que este toque pode tocar é o frete, e como
informação, não como argumento: "Include relevant shipping information (such as
free shipping threshold)" — exemplo dele, "free shipping on all orders over $70"
(bruto L2741). Subject lines dele: "Your order is ready to ship · One click
away! · Your cart is waiting".

Quando a pessoa termina de ler: viu o item de novo; sabe que o botão a devolve
ao carrinho ou ao checkout com o item preservado; sabe o que o frete custa (ou a
partir de quanto é grátis). Nada mais.

## O que este email NÃO deve fazer

- Não oferecer desconto nem sugerir que virá — o incentivo é do e-mail 3 dele,
  toque 5 aqui.
- Não abrir com FAQ, garantia ou qualquer bloco defensivo: neste flow isso foi
  observado, ficou defensivo e foi movido para o 3º toque
  ([[posicao-muda-o-efeito-do-dispositivo]]; [[carrinho-abandonado]]).
- Não contar história, empurrar catálogo ou pedir outra coisa — "let's not
  distract".
- Não deixar o bloco dinâmico abaixo da dobra.

---

Flow: [[_flow]] · Origem: cart-checkout-abandon.md, e-mail 1 · Momento: [[carrinho-abandonado]], [[checkout-abandonado]]
