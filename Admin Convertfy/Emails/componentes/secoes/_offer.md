---
tipo: secao
secao: offer
variantes: 6
ativas: 6
com_julgamento: 6
status: aprovada
---

# Cobertura

6 variantes, todas ativas, todas julgadas.

# Chave de decisão

`momento` já separa as seis sem ambiguidade — não há duas variantes no
mesmo momento. `exige` (presença de cupom ativo) e `objeção` refinam a
leitura dentro de momentos próximos (welcome-1 vs. welcome-meio) e
explicam por que duas variantes que parecem "a mesma coisa" (offer
sazonal vs. offer de carrinho) não competem entre si.

| Variante | Momento | Exige cupom | Objeção | Registro |
|---|---|---|---|---|
| [[offer-1-condicao-sem-imagem]] | campanha-promocional | não | — | — |
| [[offer-2-duas-ofertas-sazonais]] | sazonal-data-comemorativa | não (usa prazo real, não cupom) | — | — |
| [[offer-3-lembrete-de-cupom]] | browse-abandonment, carrinho-abandonado | sim | — | — |
| [[offer-4-manifesto-antes-do-cupom]] | welcome-1 | sim | pertencimento | premium-editorial |
| [[offer-5-tres-diferenciais-e-cupom]] | welcome-meio | sim | preço-valor | premium-editorial |
| [[offer-6-carrinho-preto-e-branco]] | carrinho-abandonado, checkout-abandonado | sim | — | bold-alto-contraste |

**Como ler:** offer-4 e offer-5 têm o mesmo registro (`premium-editorial`)
e as duas exigem cupom — é só o `momento` (welcome-1 vs. welcome-meio) e a
`objeção` (pertencimento vs. preço-valor) que decidem qual entra em qual
e-mail da régua. offer-3 e offer-6 disputam momentos de abandono
próximos: offer-6 é `peça-inteira` com bloco dinâmico de carrinho
(exige-o explicitamente); offer-3 é mais leve e serve também
browse-abandonment, onde não há carrinho para renderizar.

# Onde a seção não cobre

- Nenhum offer para `consideração`, `reengajamento`, `lançamento`,
  `cross-sell`, `catálogo-mais-vendidos`, `queima-de-estoque` ou
  `pós-compra`.
- Nenhum offer ataca `qualidade-eficácia`, `amplitude-de-catálogo`,
  `escolha-variedade`, `confiança-no-canal` ou `suporte-dúvida` — só
  `pertencimento` (offer-4) e `preço-valor` (offer-5) têm oferta com
  objeção declarada; as outras quatro não declaram objeção nenhuma.
