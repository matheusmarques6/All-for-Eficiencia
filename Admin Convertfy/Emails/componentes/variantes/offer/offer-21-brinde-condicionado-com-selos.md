---
tipo: componente
slug: offer-21-brinde-condicionado-com-selos
variant_id: f8fd38f6-04d0-4337-a130-31e207510b59
nome_no_banco: "offer 21"
secao: offer
status: aprovada
fonte: catalogacao-2026-09-19
schema_campos: 12
product_slots: 0
objecao: [preco-valor]
aliviador: [transparencia_de_politica]
profundidade: afirmacao
registro: [bold-alto-contraste]
registro_vetado: [luxo, clinico-sobrio]
paleta: [full-dark]
papel_na_peca: [fecha]
itens: { min: 3, max: 3 }
peso: { altura_px: 634, classe: medio, fonte: medido }
convivencia: []
exige: [cupom-ativo, politica-real]
aprendizados: [[[incentivo-precisa-existir-em-texto]], [[cada-alegacao-e-uma-promessa-operacional]]]
ativa: true
dispositivo: oferta_condicionada
---

## Descrição curta
Fecha a peça com a oferta condicionada e o risco removido no mesmo andar: o leitor lê a condição com o código embutido na frase, vê o botão, a foto do brinde e três selos de compromisso. Obriga a frase com código, CTA, três ícones com rótulo e sublinha cada, e a foto.

## Descrição detalhada
Bloco preto único com quatro andares: uma frase de duas linhas com o código EMBUTIDO nela (`gift_coupon_line` — não há campo separado de código; a frase carrega mecânica, condição e código juntos), um CTA branco em pílula (`gift_cta_label`), uma foto (`gift_photo`, gerada) e uma faixa de três ícones (`gift_icon_1..3`, gerados), cada um com rótulo (`gift_icon_N_label`) e sublinha (`gift_icon_N_sub`). Nota de doutrina do dispositivo: oferta condicionada COM código vira, na prática, entrega de código — o que separa esta da entrega pura (offer-11) é que aqui a condição ("acima de X", "na primeira compra") é a manchete e o código vem dissolvido na frase, mais os três selos que a offer-11 não tem.

## Quando usar
Fechamento de peça em que a oferta tem condição real (brinde acima de valor, desconto na primeira compra) e a loja sustenta três compromissos para os selos (troca, frete, pagamento): o bloco junta gatilho e remoção de risco no ponto da decisão. Habitat: fecho de welcome com brinde condicionado, campanha de ticket médio onde a condição empurra o carrinho para cima.

## Quando não usar
Quando a mecânica não cabe numa frase de duas linhas: condição com três cláusulas dissolvida em `gift_coupon_line` vira letra miúda ilegível — mecânica complexa pede o offer-20, que tem campo próprio de condição. E não usar com selos sem lastro: cada ícone é uma promessa operacional; dois selos verdadeiros e um decorativo derrubam os três.

## Convivência
Não com body-21 de body (três selos e garantia) na mesma peça: duas faixas de selos duplicam a remoção de risco e leem como protesto. Não com outro bloco de código (offer-11, offer-20). Bloco full-dark de fecho casa com corpo claro acima.

## Notas de cadastro
Nasceu no banco como "body 21", homônima da [[body-21-tres-selos-e-garantia]]; renomeada para "offer 21" em 19/09. O código embutido em `gift_coupon_line` (sem campo próprio) é decisão de anatomia registrada aqui para a copy saber onde ele mora. `peso` medido no HTML de produção em 19/09.
