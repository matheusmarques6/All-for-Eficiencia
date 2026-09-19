---
tipo: componente
slug: products-13-vitrine-narrada-alternada
variant_id: ed0cf7b6-1f7e-4486-b97e-8430d9b49480
nome_no_banco: "produtos 13"
secao: products
status: aprovada
fonte: catalogacao-2026-09-19
schema_campos: 14
product_slots: 3
objecao: [escolha-variedade]
aliviador: [dado_de_adequacao]
profundidade: afirmacao
registro: [comercial]
registro_vetado: [luxo]
paleta: [claro]
papel_na_peca: [meio]
itens: { min: 3, max: 3 }
convivencia: [grade-de-produtos-nao-convive-com-review-vitrine]
exige: [3-produtos-com-link]
aprendizados: [[[um-cta-dominante-em-email-curto]], [[titulos-precisam-carregar-o-argumento]]]
---

## Descrição curta
Conta os produtos em vez de listá-los: o leitor desce em zigue-zague por linhas alternadas — foto de um lado, nome e uma frase de curadoria do outro — e cada item ganha o porquê que uma grade não dá. Obriga título, nome + descrição por produto, fotos, label de CTA por produto e CTA final.

## Descrição detalhada
Título centralizado (`showcase_title`) e linhas de produto empilhadas alternando foto à esquerda e à direita — cada linha com foto (`showcase_product_N_photo`), nome (`showcase_product_N_name`) e descrição de uma frase (`showcase_product_N_desc`) — mais botão por produto (`showcase_product_cta_label`, label único) e CTA final (`showcase_final_cta_label`). Incoerência de schema: há 4 pares de nome/descrição mas só 3 campos de foto, e o cadastro descreve TRÊS linhas — esta nota assume 3 itens (o que as fotos sustentam) e registra a divergência. Difere das grades (12/14/15) pela descrição por item: é a vitrine para quando a escolha precisa de uma frase de argumento, não só de nome.

## Quando usar
Curadoria comentada de três produtos — "qual é pra quê" — em toque de meio de flow: welcome do meio, cross-sell, newsletter. A descrição por item é o slot da razão de escolha; se os três textos não puderem dizer coisas de naturezas distintas, a vitrine certa é uma grade muda. O zigue-zague é a exceção clássica ao botão centralizado: o CTA de cada linha acompanha o lado do texto.

## Quando não usar
Quando há exatamente 4 produtos para mostrar: apesar dos 4 pares de nome/descrição no schema, só existem 3 fotos — o quarto item entraria sem imagem ou quebraria o layout; com 4 produtos, usar a grade 12/15. E as exclusões de qualquer vitrine: [[welcome-4]] (proíbe catálogo) e primeiros toques de carrinho.

## Convivência
Não com review-vitrine ([[grade-de-produtos-nao-convive-com-review-vitrine]]) nem com o zigue-zague de reviews (reviews-7) na mesma peça: dois zigue-zagues anulam o ritmo um do outro. CTA final domina; os de linha recuam.

## Notas de cadastro
DIVERGÊNCIA DE SCHEMA: `showcase_product_1..4_name` e `_desc` (4 slots) contra `showcase_product_1..3_photo` (3 fotos); cadastro descreve três linhas. HTML não disponível no vault para arbitrar — assumido 3 (itens, slots) pela foto e pela prosa do cadastro; o 4º par nome/descrição fica órfão até correção no admin. Registrado no relatório. `3-produtos-com-link` sem nota em `requisitos/`. `peso` omitido (sem HTML).
