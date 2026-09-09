---
tipo: intencao
flow_type: abandoned_cart
email_number: 4
status: rascunho
fonte: "sem origem — escrito da operação (princípio do Max sem e-mail correspondente: 'provide assurance', cart-checkout-abandon.md §O racional dele, bruto L3794)"
modo: quebra_de_objecao
n_objecoes: [1, 1]
fonte_das_objecoes: medos_de_categoria
riscos_elegiveis: [financeiro, seguranca]
profundidade_minima: garantia
aliviadores_admissiveis: [garantia_de_devolucao, transparencia_de_politica, seguranca_de_pagamento, reputacao_da_loja]
trabalhos_fixos: [remocao_de_risco]
permite_reataque: false
dimensao_alvo: integridade
proibicoes:
  - alegar garantia, prazo de troca ou selo que a operação não sustenta
  - desconto, ou sinal de que virá um
  - reapresentar o argumento do toque 3
  - superlativo — só compromissos verificáveis
---

# Abandoned cart 4 — E se der errado?

*(sem origem no Max — escolha desta intenção)*

## O que este email deve fazer

Depois de três toques, quem sobra não duvida do item; duvida da transação: "se
não servir, se não chegar, se der problema no pagamento, o prejuízo é meu?". É a
objeção que o eixo [[checkout-abandonado]] nomeia — erro de pagamento, frete
revelado tarde, indecisão de última hora — e que o Max resume num princípio sem
e-mail: "reduce friction, provide assurance, and make buying feel easy"
(cart-checkout-abandon.md §O racional dele, bruto L3794). Este toque é a casa
transformando "provide assurance" em um e-mail.

O trabalho é remover o risco no ponto da decisão, visível — não no rodapé
([[remocao-de-risco-escala-com-o-ticket]]): a política de troca ou devolução
como ela é, a segurança do pagamento, o histórico da loja. Compromissos, não
promessas vagas — cada medo riscado é uma promessa operacional
([[cada-alegacao-e-uma-promessa-operacional]]). Quanto maior o ticket, mais alto
a garantia sobe na peça. O item e o botão continuam no topo.

Quando ela termina de ler: sabe exatamente o que acontece se der errado, e que
isso não custa nada a ela; o item continua a um clique; ainda não houve
desconto nem pressão.

## O que este email NÃO deve fazer

- Não alegar o que a operação não sustenta — garantia inventada é problema de
  confiança e, em vários mercados, jurídico.
- Não oferecer desconto nem sinalizar que virá.
- Não reapresentar a resposta do toque 3 — este toque é sobre a transação, não
  sobre o produto.
- Não usar superlativo ("compra 100% segura") sem o compromisso concreto por
  trás.

---

Flow: [[_flow]] · Princípio: [[remocao-de-risco-escala-com-o-ticket]] · Momento: [[checkout-abandonado]]
