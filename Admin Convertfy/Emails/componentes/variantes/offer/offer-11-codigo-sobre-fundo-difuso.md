---
tipo: componente
slug: offer-11-codigo-sobre-fundo-difuso
variant_id: 3ce59e7b-0b26-4ec7-9de7-5b8ddc9ca4bc
nome_no_banco: "body 11"
secao: offer
status: aprovada
fonte: catalogacao-2026-09-19
schema_campos: 8
product_slots: 0
objecao: [preco-valor]
aliviador: [dado_de_adequacao]
profundidade: afirmacao
registro: [minimalista-leve]
registro_vetado: [festivo]
paleta: [cinza-neutro]
papel_na_peca: [fecha]
convivencia: []
exige: [cupom-ativo]
aprendizados: [[[cupom-repetido-precisa-de-papel]], [[incentivo-precisa-existir-em-texto]]]
---

## Descrição curta
Entrega o código num respiro visual: o leitor sai do argumento e cai numa tela calma — fundo difuso, pilha de texto branco centralizada, o código e o botão. Obriga título, subtítulo, dois parágrafos, rótulo e código do cupom, CTA e o fundo desfocado.

## Descrição detalhada
Fundo cinza uniforme com formas desfocadas (`gift_background_image`, gerada) e, sobre ele, uma pilha centralizada de texto branco: título (`gift_title`), subtítulo em negrito (`gift_subtitle`), dois parágrafos (`gift_body_1`, `gift_body_2`), rótulo e código do cupom (`gift_coupon_label`, `gift_coupon_code`) em texto real e CTA (`gift_cta_label`). Os dois parágrafos são o que a distingue dos offers de código existentes: [[offer-3-lembrete-de-cupom]] relembra sem argumentar; esta entrega o código COM contexto — dois slots de prosa para dizer o que o código significa antes de dá-lo.

## Quando usar
Fechamento de peça cujo argumento veio antes: a hero abriu a tese, o body sustentou, e este bloco entrega (ou re-entrega com papel novo) o código como conclusão — os dois parágrafos amarram argumento e resgate. Serve o welcome quando a hero escolhida não tem slot de cupom (hero 14, 16, 17, 18): esta posição vira a entrega do incentivo obrigatório, em texto real, como [[incentivo-precisa-existir-em-texto]] exige.

## Quando não usar
Na mesma peça que uma hero que já entrega o mesmo código (hero 11, 13, 15) sem papel novo para esta aparição: repetição sem mudança de papel é ruído — se a hero entregou, este bloco só entra se fechar um argumento que a hero não fez ([[cupom-repetido-precisa-de-papel]]). E não em toque sem cupom ativo: o bloco inteiro é o resgate; sem código, os oito campos não têm assunto.

## Convivência
Não com outro bloco de código na mesma peça (offer-20, offer-21) — um resgate por peça. Como fecho calmo, casa depois de blocos densos; entre duas seções escuras, o cinza difuso faz a transição.

## Notas de cadastro
`nome_no_banco` é "body 11", mas o `block_type` no banco é offer — o arquivo vive em `variantes/offer/` (o caminho é o tipo). Nome a corrigir no admin. Descrição do banco bate com a anatomia. Sem HTML para medir altura — `peso` omitido; ver relatório.
