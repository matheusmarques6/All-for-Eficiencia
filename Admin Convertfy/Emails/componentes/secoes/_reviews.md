---
tipo: secao
secao: reviews
variantes: 7
ativas: 7
com_julgamento: 7
status: aprovada
---

# Cobertura

7 variantes no inventário, todas ativas e julgadas — mas
[[reviews-3a-depoimento-longo-monoespacado]] e
[[reviews-3b-depoimento-longo-monoespacado]] são a mesma peça gravada duas
vezes (prosa, eixos, requisitos e `peso` idênticos byte a byte; só
`variant_id` e `slug` divergem). Ver [[reviews-3-duplicado]]. Contam como
7 no inventário, 6 perfis de decisão distintos.

# Chave de decisão

Três das sete declaram a mesma objeção — `qualidade-eficácia`
(reviews-1, reviews-3a/3b, reviews-7) — atacando a mesma dúvida com
**tipos de prova diferentes**. Ali, quem separa não é `objeção` (que
empata), é o tipo de evidência que cada uma pede
(`requisitos_de_reviews` — não elimina até o banco de reviews expor
metadados; hoje é critério de desempate, não gate).

| Variante | Objeção | Tipo de prova | Momento |
|---|---|---|---|
| [[reviews-1-depoimento-com-credencial]] | qualidade-eficácia | depoimento com credencial + foto do depoente | consideração, welcome-meio, reengajamento |
| [[reviews-3a-depoimento-longo-monoespacado]] | qualidade-eficácia | foto de uso real + reviews longos | checkout-abandonado, carrinho-abandonado |
| [[reviews-7-zigue-zague-com-cupom]] | qualidade-eficácia | selo de compra verificada + reviews curtos (e gate de cupom ativo no passo 4) | consideração |
| [[reviews-5-prova-por-volume]] | adesão-social | foto de uso real + reviews curtos | consideração, reengajamento |
| [[reviews-6-review-por-variante]] | escolha-variedade | catálogo de variantes + packshot vertical + 3 reviews distintos | welcome-meio, reengajamento, cross-sell |
| [[reviews-8-ugc-de-comunidade]] | pertencimento | UGC autorizado | (qualquer — sem filtro de momento) |

**Como ler:** três provas diferentes para a mesma dúvida —
**credencial** (reviews-1: quem disse, com título), **foto de uso real**
(reviews-3a/3b: mostra o produto em uso), **selo verificado + cupom**
(reviews-7: prova de compra real, empurra para conversão). A escolha entre
elas depende do que a loja tem disponível — depoimento com nome e cargo,
foto de cliente, ou selo de plataforma de review — não da objeção, que é
igual nas três.

# Onde a seção não cobre

- Nenhuma reviews ataca `preço-valor`, `amplitude-de-catálogo`,
  `composição-formulação`, `disponibilidade-urgência`, `suporte-dúvida`
  ou `confiança-no-canal` — essa última é servida só por
  [[body-5-comparacao-nos-vs-eles]] em toda a biblioteca, e está inativa
  (ver [[welcome-5-sem-variante-ativa]]).
- Nenhuma reviews para `welcome-1`, `campanha-promocional`, `sazonal`,
  `lançamento`, `queima-de-estoque` ou `gift-card`.
- Duplicata reduz a cobertura real de `qualidade-eficácia` por
  "foto de uso real" a um único ativo de fato, não dois.
