---
tipo: componente
slug: offer-20-codigo-relembrado-com-mecanica
variant_id: d2d50046-f27b-42dc-92c6-9c0e83dd57cc
nome_no_banco: "offer 20"
secao: offer
status: aprovada
fonte: catalogacao-2026-09-19
schema_campos: 10
product_slots: 0
objecao: [preco-valor]
aliviador: [dado_de_adequacao]
profundidade: afirmacao
registro: [bold-alto-contraste]
registro_vetado: [luxo]
paleta: [preto-e-branco]
papel_na_peca: [meio]
convivencia: []
exige: [cupom-ativo]
aprendizados: [[[cupom-repetido-precisa-de-papel]], [[incentivo-precisa-existir-em-texto]]]
---

## Descrição curta
Relembra o código e devolve o produto à frente do leitor no mesmo bloco: em cima, a mecânica (chamada, código em pílula, condição); embaixo, o painel com quatro detalhes e a foto do que ficou para trás. Obriga chamada, código, linha de condição, CTA, headline do painel, quatro detalhes e foto.

## Descrição detalhada
Dois blocos empilhados. O de cima é preto e carrega a mecânica: chamada curta (`cart_coupon_intro`), pílula branca com o código (`cart_coupon_code`), linha de condição (`cart_coupon_condition`) e CTA (`cart_cta_label`). O de baixo é o painel: headline (`cart_panel_headline`), quatro detalhes em duas colunas (`cart_detail_1_left`, `cart_detail_2_left`, `cart_detail_1_right`, `cart_detail_2_right`) e foto (`cart_photo`, gerada). O prefixo `cart_` diz o habitat: é o offer desenhado para abandono de carrinho — relembra um código que já existe e recoloca o item na frente, com a condição em texto explícito. Difere do [[offer-6-carrinho-preto-e-branco]] (mostra o carrinho, gate de cupom) por trazer painel de detalhes do produto em vez do carrinho renderizado.

## Quando usar
No toque do flow de carrinho em que o incentivo entra ou é relembrado — o desenho do flow põe o incentivo no toque 5, cuja intenção ainda não tem nota própria; até lá, o critério é a prosa do `_flow` de abandoned_cart. A condição do cupom em campo próprio serve exatamente a regra de que valor, código e condição existem em texto real. Os quatro detalhes respondem, em uma linha cada, a dúvida residual sobre o item.

## Quando não usar
Nos toques 1–4 do carrinho ([[abandoned_cart-1]] a [[abandoned_cart-4]]): todos proíbem desconto ou sinal de que virá — este bloco é literalmente o desconto entrando; usado cedo, ensina que abandonar carrinho gera cupom. E não usar em welcome: relembrar um código "do seu carrinho" para quem nunca pôs item em carrinho é mecânica sem referente.

## Convivência
Não com segundo bloco de código na peça (offer-11, offer-21): o código aparece uma vez com papel claro. O bloco dinâmico de carrinho do ESP, se presente, fica ACIMA — este painel comenta o item, não o substitui.

## Notas de cadastro
Nasceu no banco como "body 20" com `block_type` offer; renomeada para "offer 20" em 19/09. Cadastro: o `example` de `cart_coupon_condition` tinha markdown e o merge não ancorava — corrigido em 17/09; se a condição sumir na renderização, verificar o example antes de culpar a copy. Sem HTML para medir altura — `peso` omitido; ver relatório.
