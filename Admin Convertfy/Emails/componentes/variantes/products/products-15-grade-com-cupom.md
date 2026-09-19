---
tipo: componente
slug: products-15-grade-com-cupom
variant_id: ddad9b06-55f3-423e-8dc6-6f9f2629d104
nome_no_banco: "produto 15"
secao: products
status: aprovada
fonte: catalogacao-2026-09-19
schema_campos: 13
product_slots: 4
objecao: [preco-valor, escolha-variedade]
aliviador: [dado_de_adequacao]
profundidade: afirmacao
registro: [comercial]
registro_vetado: [luxo]
paleta: [claro]
papel_na_peca: [meio]
itens: { min: 4, max: 4 }
peso: { altura_px: 1191, classe: medio, fonte: medido }
convivencia: [grade-de-produtos-nao-convive-com-review-vitrine]
exige: [4-produtos-com-link, cupom-ativo]
aprendizados: [[[cupom-repetido-precisa-de-papel]], [[incentivo-precisa-existir-em-texto]]]
---

## Descrição curta
Junta a escolha e o gatilho no mesmo bloco: o leitor varre quatro produtos numa moldura arredondada e, antes do CTA final, lê a linha de cupom que dá o motivo para escolher agora. Obriga headline em duas escalas, quatro títulos, quatro fotos, label de CTA por produto, a linha de cupom e o CTA final.

## Descrição detalhada
Headline em duas escalas no topo (`offergrid_headline_1`, `offergrid_headline_2`), moldura de contorno fino com cantos arredondados envolvendo a grade de quatro produtos — título (`offergrid_product_N_title`) e foto (`offergrid_product_N_photo`, gerada) por célula, botão por produto (`offergrid_product_cta_label`, label único) —, linha de cupom em texto real (`offergrid_coupon_line`) e CTA final (`offergrid_final_cta_label`, example "SHOP THE SALE" — distinto do label por produto "SHOP NOW", senão os dois campos disputam a mesma âncora). É a única vitrine do lote com slot de incentivo: difere da [[products-12-grade-2x2-com-pilula]] (badge, sem cupom) e da [[products-14-grade-2x2-com-filete]] (sem foto no schema, sem cupom) pela linha de cupom e pela headline dupla.

## Quando usar
Toque COM incentivo em que a vitrine fecha o argumento: welcome do meio com cupom vivo ([[welcome-2]], [[welcome-3]] — o lembrete de incentivo vivo é trabalho fixo desses toques, e a linha de cupom é onde ele mora), campanha com desconto e quatro produtos linkáveis. A aparição do cupom aqui tem papel próprio — fechamento junto à escolha — desde que a entrega tenha acontecido em outra posição.

## Quando não usar
Toque sem incentivo: a linha de cupom ficaria com o texto de exemplo ou vazia — o slot obriga um código que precisa existir e estar ativo; sem ele, o passo 4 elimina. Também não nos toques 1–4 do carrinho (proíbem desconto ou sinal de que virá) nem como terceira aparição do mesmo código na peça.

## Convivência
Não com review-vitrine ([[grade-de-produtos-nao-convive-com-review-vitrine]]) nem com segundo bloco de cupom colado (offer de código imediatamente antes ou depois duplica a mecânica). Cantos arredondados: cuidado ao colar em blocos de canto vivo.

## Notas de cadastro
Descrição do banco bate com a anatomia. `4-produtos-com-link` sem nota em `requisitos/` (cupom-ativo existe). Sem HTML para medir altura — `peso` omitido; ver relatório.

**Conserto de 19/09 (admin, auditor de âncoras)**: example de `offergrid_final_cta_label` = "SHOP THE SALE" (HTML ajustado nos dois ramos, normal e Outlook).
