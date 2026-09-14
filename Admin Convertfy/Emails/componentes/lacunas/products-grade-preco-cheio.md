---
tipo: lacuna
secao: products
sobre: biblioteca
status: aberta
descoberta_em: 2026-09-09
fonte: batch 6249aef2
pede: { papel: apoio, itens: { min: 2, max: 3 }, preco: cheio, cupom: false }
fecha_com: variante
---

# O que o alvo pediu

Grade simples de 2–3 produtos com **preço cheio** visível — vitrine para
toque sem oferta, onde o preço é informação e não desconto.

# O que sobrou e em que passo caiu

As grades ativas de `products` ou escondem preço
([[products-6-vitrine-de-sale]], [[products-3-arco-de-novidades]]) ou
pedem selo de percentual
([[products-5-tres-com-selo-de-percentual]], exige
`desconto-percentual`). Sem oferta ativa, o passo 4 elimina as de
desconto e as restantes não mostram preço.

# Evidência

Batch `6249aef2`: posição de products sem elegível quando o toque não
tem incentivo.

# O que fecha

Variante nova (ou anatomia gerada): grade 2–3 com foto, nome e preço
cheio, sem selo de desconto, `papel_na_peca: [apoio]`, `exige: []`.
