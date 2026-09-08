---
tipo: indice
title: Peças — mapa
modulo: padrao-convertfy
assunto: mapa-das-pecas
autor: convertfy
status: aprovado
---

# O que tem aqui

Peças reais da Convertfy, uma por nota, com o HTML como foi para o ar e
o porquê de cada decisão ao lado dele. É o que a ConvertIA lê quando
precisa MONTAR alguma coisa — a doutrina do Max diz o que perseguir,
estas notas mostram como fica.

# A anatomia de uma nota de peça

Quatro partes, nesta ordem:

1. **O que é** — uma frase: que peça, para que tipo de loja, em que
   situação. É o resumo que aparece na busca.
2. **A peça** — o HTML num bloco de código. Completo o bastante para
   rodar, enxuto o bastante para caber: o modelo lê até 12.000
   caracteres da nota, e o que passa disso é cortado sem aviso.
3. **As decisões, uma a uma** — a parte que faz a nota valer. Cada
   escolha com o motivo: por que 440px, por que um campo só, por que
   16px no input. Sem isto a nota é um snippet, e snippet o modelo já
   sabe escrever — mal.
4. **Quando não usar** — o limite. Peça sem limite declarado vira
   resposta padrão para situação que não é a dela.

# O que NÃO entra

Peça que não foi para o ar, ou que foi e não performou. A base é o
padrão da casa, não o arquivo de tentativas — nota ruim aqui sai como
recomendação com a autoridade da base inteira.

# Nesta pasta

- [[popup-captura-duas-etapas]] — captura de e-mail com cupom, a
  referência de estrutura.
