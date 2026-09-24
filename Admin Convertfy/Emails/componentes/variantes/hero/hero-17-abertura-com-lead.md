---
tipo: componente
slug: hero-17-abertura-com-lead
variant_id: 7f3a72a6-e24c-4aa6-b4ca-14df7f3d80b5
nome_no_banco: "hero section 17"
secao: hero
status: aprovada
fonte: catalogacao-2026-09-19
schema_campos: 5
product_slots: 0
objecao: [pertencimento]
aliviador: [dado_de_adequacao]
profundidade: afirmacao
registro: [premium-editorial]
registro_vetado: [volume-impulso]
paleta: [claro]
papel_na_peca: [abre]
peso: { altura_px: 556, classe: leve, fonte: medido }
convivencia: []
exige: []
aprendizados: []
ativa: true
dispositivo: abertura_editorial
---

## Descrição curta
Abre o e-mail em meia tela e passa a palavra rápido: o leitor lê título, um lead que fisga e um corpo curto — a abertura editorial mais compacta das três, feita para quem quer o argumento no bloco seguinte. Obriga título, lead, corpo, CTA e foto de fundo. O logo é célula fixa do layout.

## Descrição detalhada
Bloco único de 598 × 556 apoiado numa foto de fundo (`hero_background_image`, gerada), com o logo fixo centralizado no topo (célula do layout, sem campo) e, na metade inferior, o conjunto de texto: título (`hero_title`), lead (`hero_body_lead`), corpo (`hero_body`) e CTA (`hero_cta_label`). Sem oferta, sem código, sem prazo. É a mais curta das três aberturas editoriais do lote — e a única com slot de LEAD entre título e corpo, a frase-ponte que as outras não têm: a [[hero-16-arco-editorial]] aposta na moldura do arco (966px) e a [[hero-18-abertura-alta-centrada]] na altura (977px).

## Quando usar
Abertura editorial quando o e-mail abaixo é denso: por ser a mais leve das três, deixa orçamento de peso para um corpo longo (comparação, mecanismo, vitrine). O lead é o slot para a tese em uma frase — o toque de tese ([[welcome-1]] com entrega de código em outra posição, ou nutrição/reengajamento editorial) é o habitat. Quando o topo precisa entregar decisão e o meio precisa de espaço, esta é a editorial a escolher.

## Quando não usar
Como peça de impacto único: com 556px e sem oferta, ela não sustenta um e-mail curto sozinha — num toque de fechamento (welcome-6/7) a abertura editorial calma é o registro errado: ali o topo pertence ao prazo, não à atmosfera. E não usar quando o toque exige entrega de incentivo e não há bloco de código abaixo.

## Convivência
Feita para conviver com blocos pesados abaixo — é o par natural de um body de 1200px+. Não empilhar com segunda abertura editorial (16 ou 18): duas capas em sequência, nenhuma abre.

## Notas de cadastro
Descrição do banco bate com a anatomia. Divergência de `peso` resolvida por medição em 19/09: a ficha declarava `medio` a 554px; o HTML de produção mede 556px, que pelos limiares da spec (leve <600) é `leve` — é a única das três aberturas editoriais na classe leve, e é o que a torna a escolha quando o corpo do e-mail precisa de orçamento.

**Conserto de 19/09 (admin, auditor de âncoras)**: saiu `hero_logo_image` (sem slot). 6 → 5 campos.
