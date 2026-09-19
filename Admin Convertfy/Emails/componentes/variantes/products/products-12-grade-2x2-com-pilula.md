---
tipo: componente
slug: products-12-grade-2x2-com-pilula
variant_id: c772b4f0-f453-4f08-9862-34e8c1acc66a
nome_no_banco: "produto 12"
secao: products
status: aprovada
fonte: catalogacao-2026-09-19
schema_campos: 11
product_slots: 4
objecao: [escolha-variedade]
aliviador: [dado_de_adequacao]
profundidade: afirmacao
registro: [comercial]
registro_vetado: [luxo]
paleta: [claro]
papel_na_peca: [meio]
itens: { min: 4, max: 4 }
peso: { altura_px: 1373, classe: pesado, fonte: medido }
convivencia: [grade-de-produtos-nao-convive-com-review-vitrine]
exige: [4-produtos-com-link]
aprendizados: [[[um-cta-dominante-em-email-curto]]]
---

## Descrição curta
Reduz o catálogo a quatro escolhas nomeadas: o leitor varre uma grade 2×2 — foto, nome, botão por célula — sob uma pílula dourada que nomeia o recorte, e sai por um CTA final. Obriga o badge, quatro nomes, quatro fotos, o label de CTA por produto e o CTA final. Sem preço.

## Descrição detalhada
Uma pílula dourada com o nome da seção no topo (`grid_badge`), quatro células iguais em grade de dois por dois — cada uma com foto (`grid_product_N_photo`, gerada ou de feed), nome (`grid_product_N_name`) e o botão por produto (um label único, `grid_product_cta_label`, repetido nas células) — e um CTA final (`grid_final_cta_label`). Sem campo de preço. Das vitrines paralelas do lote: a [[products-14-grade-2x2-com-filete]] é a mesma grade SEM campo de foto no schema; a [[products-15-grade-com-cupom]] adiciona headline dupla e linha de cupom; a [[products-16-par-de-cards]] desce para 2 produtos.

## Quando usar
Quando o toque pede curadoria de escolha — "qual dessas é a certa pra mim" — com quatro produtos linkáveis: cross-sell, mais-vendidos, welcome do meio quando a vitrine volta. O badge é o slot da curadoria ("best-sellers", "para presente"): é ele que transforma a grade de catálogo em recorte. Sem preço por desenho, serve toque sem oferta sem expor a ausência de desconto.

## Quando não usar
No [[welcome-4]]: a intenção proíbe empurrar catálogo — quem chegou ali já viu o que há para ver; falta confiança, não opção. Idem nos primeiros toques de carrinho ([[abandoned_cart-1]]: nada além do item). E não usar com menos de quatro produtos com página própria: célula vazia ou produto repetido expõe a costura.

## Convivência
Não com review-vitrine na mesma peça ([[grade-de-produtos-nao-convive-com-review-vitrine]]). Com quatro botões de célula mais o CTA final, os CTAs genéricos da peça precisam recuar — um dominante ([[um-cta-dominante-em-email-curto]]).

## Notas de cadastro
Descrição do banco bate com a anatomia. O CTA por produto é um label único repetido (não um por célula) — a copy escreve um texto que sirva aos quatro. `4-produtos-com-link` não existe em `requisitos/`; relatório. `peso` medido no HTML de produção em 19/09.
