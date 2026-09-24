---
tipo: componente
slug: hero-12-contador-com-oferta
variant_id: 9bc6a6c7-2fb8-4b66-bffa-0d64b6d28063
nome_no_banco: "hero 12"
secao: hero
status: aprovada
fonte: catalogacao-2026-09-19
schema_campos: 8
product_slots: 0
objecao: [disponibilidade-urgencia]
aliviador: [dado_de_adequacao]
profundidade: afirmacao
registro: [comercial, volume-impulso]
registro_vetado: [luxo, clinico-sobrio]
paleta: [claro]
papel_na_peca: [abre]
peso: { altura_px: 937, classe: medio, fonte: medido }
convivencia: []
exige: [prazo-real]
aprendizados: [[[deadline-falso-queima-o-proximo]], [[cadencia-decide-fechamento-ou-farsa]]]
ativa: true
dispositivo: prazo_declarado
---

## Descrição curta
Abre o e-mail com o relógio correndo: o leitor vê o contador antes de qualquer argumento e entende que a janela fecha — a oferta vem logo abaixo, em três partes, já com o botão. Obriga faixa de contador com linha de benefício, sobrescrito, oferta em verbo+valor e sufixo (o % é célula fixa), sublinha, corpo, CTA e fundo. O logo é célula fixa do layout.

## Descrição detalhada
Faixa cinza no topo com três caixas de contador e uma linha de benefício (`countdown_benefit_line`), seguida de painel claro que cobre quase toda a peça: sobrescrito (`countdown_eyebrow`), oferta em duas partes de texto real (`countdown_offer_main`, ex. "GET 10", e `countdown_offer_suffix`; o % é célula fixa do layout), sublinha (`countdown_subline`), corpo (`countdown_body`), CTA (`countdown_cta_label`), sobre `countdown_background_image`; o logo é célula fixa (`LOGO HERE`), sem campo. Não há campo de cupom: a oferta é declarada, não entregue — quem entrega código é outra posição ou o desconto é automático. É a única hero do lote cujo argumento é o tempo, não o valor nem a campanha.

## Quando usar
No fechamento do ciclo da oferta: [[welcome-6]] (o prazo com hora como moldura, primeira coisa lida) e [[welcome-7]] (o sino — só a hora tem valor marginal). Exige prazo real configurado na plataforma: o contador é a forma mais explícita de prazo que existe, e prazo declarado tem que ser prazo cumprido — a credibilidade se decide no e-mail seguinte ([[deadline-falso-queima-o-proximo]]). Se dois toques repetem a mesma hora, o intervalo entre eles se mede em horas, nunca em dias.

## Quando não usar
No [[welcome-2]]: a intenção proíbe prazo com hora fechada — hora fechada pertence ao fechamento do ciclo (regra transversal 3 do flow), e um contador no toque 2 fixa uma hora que o toque 3 não vai honrar, queimando os dois prazos do flow de uma vez. Também não em loja de registro luxo: contagem regressiva contraria a escassez percebida que esse registro constrói.

## Convivência
Não empilhar com outro bloco de prazo ou segunda menção de hora diferente: um prazo por peça — duas horas distintas na mesma peça provam que nenhuma é real. Depois dela, blocos curtos: quem abre com relógio não pode pedir leitura longa.

## Notas de cadastro
Descrição do banco bate com a anatomia. Não há campo de código — divergiria de qualquer leitura que a trate como entrega de cupom. `peso` medido no HTML de produção em 19/09.

**Conserto de 19/09 (admin, auditor de âncoras)**: saíram `countdown_offer_symbol` (o % é célula fixa) e `countdown_logo_image` (sem slot); example de `countdown_offer_main` = "GET 10". 10 → 8 campos.
