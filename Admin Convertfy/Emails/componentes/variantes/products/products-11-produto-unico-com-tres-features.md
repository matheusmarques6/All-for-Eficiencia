---
tipo: componente
slug: products-11-produto-unico-com-tres-features
variant_id: 57f25213-768b-4102-9617-3394fac595ce
nome_no_banco: "produtos 11"
secao: products
status: aprovada
fonte: catalogacao-2026-09-19
schema_campos: 6
product_slots: 1
objecao: [qualidade-eficacia]
aliviador: [dado_de_adequacao]
profundidade: afirmacao
registro: [premium-editorial]
registro_vetado: [volume-impulso]
paleta: [claro]
papel_na_peca: [meio]
itens: { min: 1, max: 1 }
peso: { altura_px: 941, classe: medio, fonte: medido }
convivencia: []
exige: [1-produto-com-link]
aprendizados: [[[titulos-precisam-carregar-o-argumento]]]
---

## Descrição curta
Dá a um único produto o e-mail inteiro de atenção: o leitor lê um parágrafo de abertura, vê a foto vertical grande e três atributos nomeados dentro de uma moldura que amarra tudo ao CTA. Obriga a introdução, três features de uma linha, o CTA e a foto.

## Descrição detalhada
Parágrafo de abertura em quatro linhas centralizadas (`prod_intro`), uma foto vertical grande (`prod_photo`, gerada) e uma moldura de contorno que envolve os três atributos (`prod_feature_1..3`) até o CTA (`prod_cta_label`). Decisão de profundidade pela anatomia: cada feature é UM campo de texto curto, sem par título+texto — os atributos NOMEIAM, não explicam; portanto `afirmacao`, não `mecanismo`. Quem explica o como é a body 15 (callouts com título+texto apontados na foto); esta apresenta. Difere da [[products-4-produto-unico-com-prazo]] existente por não ter prazo nem oferta, e da [[products-10-winback-com-relato]] por não ter voz de terceiro: é o produto único em voz de marca, limpo.

## Quando usar
Quando o toque pede foco em um herói sem pressão: apresentação do best-seller no welcome do meio, produto de entrada em nutrição, o item específico em browse abandonment. Os três atributos são as três palavras que a varredura lê — cada um de natureza distinta (material, uso, resultado), nunca três sinônimos de qualidade.

## Quando não usar
No toque do cético ([[welcome-3]], [[abandoned_cart-3]]): a profundidade mínima ali é `mecanismo`, e esta anatomia só afirma — três linhas nomeando atributos não respondem "como isso se sustenta"; ali entra a body 15 ou a body 13. Também não quando a loja não define um produto herói: aplicá-la a um produto qualquer desperdiça o foco que é a razão dela.

## Convivência
Não empilhar com outro bloco de produto único (products-4, products-10): dois heróis disputam a peça. Casa bem depois de uma abertura editorial leve (hero 17) — a peça fica tese em cima, produto embaixo.

## Notas de cadastro
Descrição do banco bate com a anatomia. `1-produto-com-link` sem nota em `requisitos/`; relatório. `peso` medido no HTML de produção em 19/09.
