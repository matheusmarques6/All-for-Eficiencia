---
tipo: componente
slug: products-16-par-de-cards
variant_id: 417bf754-cc2c-4b1d-93bb-f429a7f9d4b6
nome_no_banco: "produto 16"
secao: products
status: aprovada
fonte: catalogacao-2026-09-19
schema_campos: 7
product_slots: 2
objecao: [escolha-variedade]
aliviador: [dado_de_adequacao]
profundidade: afirmacao
registro: [minimalista-leve]
registro_vetado: [volume-impulso]
paleta: [claro]
papel_na_peca: [meio]
itens: { min: 2, max: 2 }
peso: { altura_px: 830, classe: medio, fonte: medido }
convivencia: [grade-de-produtos-nao-convive-com-review-vitrine]
exige: [2-produtos-com-link]
aprendizados: [[[um-cta-dominante-em-email-curto]]]
---

## Descrição curta
Reduz a escolha a um par: o leitor compara dois cards empilhados — foto de um lado, nome do outro — e decide entre A e B em vez de varrer um catálogo. Obriga título em caixa alta, dois nomes, duas fotos, o label de CTA por produto e um CTA final de largura quase total.

## Descrição detalhada
Título em caixa alta (`pair_title`), dois cards de contorno fino empilhados — cada um dividido entre foto (`pair_product_N_photo`, gerada) e nome (`pair_product_N_name`), com botão por produto (`pair_product_cta_label`, label único) — e um CTA final de largura quase total (`cta_here`; o campo foge do prefixo `pair_` — erro de cadastro, ver Notas). É a ÚNICA vitrine paralela de 2 do lote; na biblioteca, as vizinhas de 2 slots são [[products-6-vitrine-de-sale]] (momento de sale) e [[products-7-dois-com-galeria-de-angulos]] (lançamento, galeria por ângulo, peça-inteira de 3298px) — esta é a versão leve e sem tema: par simples, sem preço, sem selo.

## Quando usar
Quando a curadoria honesta é binária — o best-seller e o alternativo, o para-dia e o para-noite — em toque de meio de flow: a escolha entre dois é decisão barata, e a pilha vertical dá a cada produto uma linha inteira de atenção. É a vitrine para loja de catálogo curto, onde quatro células exporiam repetição.

## Quando não usar
Quando o trabalho é mostrar amplitude ("tem mais coisa pra ver"): dois produtos comunicam exatamente o contrário — ali a grade certa é a 12/14 ou a 3×3 existente. E não no [[welcome-4]] nem nos primeiros toques de carrinho, pelas mesmas razões de qualquer vitrine: catálogo onde a intenção proíbe catálogo.

## Convivência
Não com review-vitrine ([[grade-de-produtos-nao-convive-com-review-vitrine]]). Dois botões de card + CTA final: o CTA final domina, os de card recuam.

## Notas de cadastro
Erro de cadastro no schema: o campo do CTA final chama-se `cta_here`, fora do prefixo `pair_` dos demais — qualquer automação que agrupe por prefixo vai perdê-lo; registrado no relatório. `2-produtos-com-link` sem nota em `requisitos/`. `peso` medido no HTML de produção em 19/09.
