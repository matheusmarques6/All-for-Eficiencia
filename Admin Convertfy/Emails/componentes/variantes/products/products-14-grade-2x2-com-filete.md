---
tipo: componente
slug: products-14-grade-2x2-com-filete
variant_id: 87bca4da-b37a-42bd-a792-c74b55bf9afb
nome_no_banco: "produto 14"
secao: products
status: aprovada
fonte: catalogacao-2026-09-19
schema_campos: 7
product_slots: 4
objecao: [escolha-variedade]
aliviador: [dado_de_adequacao]
profundidade: afirmacao
registro: [minimalista-leve]
registro_vetado: [volume-impulso]
paleta: [claro]
papel_na_peca: [meio]
itens: { min: 4, max: 4 }
peso: { altura_px: 1073, classe: medio, fonte: medido }
convivencia: [grade-de-produtos-nao-convive-com-review-vitrine]
exige: [4-produtos-com-link]
aprendizados: [[[um-cta-dominante-em-email-curto]]]
---

## Descrição curta
A grade 2×2 mais enxuta da biblioteca: o leitor vê título com filete grosso, quatro molduras com foto e nome, botão por célula e CTA final — sete campos, nada de badge, preço ou cupom. Obriga título, quatro nomes, o label de CTA por produto e o CTA final; as fotos NÃO têm campo no schema.

## Descrição detalhada
Título centralizado com um filete grosso abaixo (`grid2_title`), quatro células em grade de dois por dois — cada uma com a foto dentro de moldura e o nome (`grid2_product_N_name`) —, o botão por produto (`grid2_product_cta_label`, label único) e o CTA final (`grid2_final_cta_label`). ATENÇÃO de contrato: não há campo de foto no schema — as imagens vêm do feed de produtos ou são fixas no HTML; o HTML da variante não está no vault para confirmar qual dos dois. Difere da [[products-12-grade-2x2-com-pilula]] exatamente nisso (lá a foto é campo) e na moldura: filete sóbrio em vez de pílula dourada.

## Quando usar
Mesma posição da grade 12 — curadoria de quatro escolhas em toque de meio de flow — quando o registro pede sobriedade em vez de ornamento, ou quando a integração de feed já fornece as fotos e não se quer gerar imagem por célula. É a grade a escolher quando a peça acima é visualmente carregada: o filete não compete.

## Quando não usar
Quando a foto de cada produto precisa ser controlada pela peça (campanha com direção fotográfica própria): sem campo de foto, esta grade não aceita brief de imagem — ali a certa é a products-12. E as mesmas exclusões de catálogo: não no [[welcome-4]] (proíbe empurrar catálogo) nem nos primeiros toques de carrinho.

## Convivência
Não com review-vitrine na mesma peça ([[grade-de-produtos-nao-convive-com-review-vitrine]]). CTAs genéricos recuam diante dos quatro botões de célula.

## Notas de cadastro
Divergência de schema: cadastro descreve foto dentro de moldura em cada célula, mas o schema não tem campo de foto — origem das imagens (feed ou fixa) não confirmável sem o HTML; registrado no relatório. `4-produtos-com-link` sem nota em `requisitos/`. `peso` medido no HTML de produção em 19/09.
