---
tipo: componente
slug: body-3-pitch-de-gift-card
secao: body
nome_no_banco: "body 3 - bridge features cards"
variant_id: 4e9726d1-40fe-40ce-aa81-c2a33b062603
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [gift-card, sazonal-data-comemorativa]
momento_vetado: [campanha-promocional]

# --- eixos de ranking, na ordem do protocolo ---
objecao: []
registro: []
registro_vetado: []
paleta: []
papel_na_peca: [apoio]

# --- requisitos duros (eliminam) ---
exige: [gift-card-digital]

# --- capacidade e composição ---
product_slots: 0
itens: null
peso: { altura_px: 816, classe: medio, fonte: medido }
convivencia: []

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: revisao-html-2026-09-09
densidade_no_banco: null
schema_campos: 7
status: aprovada
---

## Descrição curta

Pitch de gift card digital com headline anti-objeção, dois parágrafos curtos e CTA, assinado por faixa de 3 selos circulares com valores da marca.

## Descrição detalhada

Bloco de texto 100% vivo sobre fundo branco, em container fixo de 600px: título de 50px em duas linhas, dois parágrafos de 24px e CTA bulletproof de 354 × 61px (fundo preto, cantos de 8px; VML no Outlook, degrada reto). Abaixo, uma faixa de 542px com três círculos de 166px — `<td>` com fundo cinza `#8B8B8B` e `border-radius: 83px`, 22px de vão entre eles — contendo texto vivo em branco (o valor da marca). Não há `<img>` no bloco: os selos são célula + texto, não PNG; com imagens bloqueadas nada some, e no Outlook o círculo vira quadrado com o texto dentro. Sem media query: o container é `min-width: 600px` e os três selos não empilham no mobile. Os dois módulos (pitch / selos) são linhas separadas da mesma tabela — a faixa de selos pode ser reaproveitada sozinha como assinatura em outros e-mails.

## Quando usar

Campanhas de gift card — datas de presente (Natal, Dia das Mães/Pais/Namorados), corporate gifting de fim de ano, e como seção de apoio em e-mails sazonais ("não sabe o que dar? gift card"). A faixa de selos entra quando a marca tem valores articulados e quer reforço institucional — especialmente eficaz em B2B/corporate onde cultura vende.

## Quando NÃO usar

Clientes sem gift card digital (óbvio, mas o Architect precisa do dado no perfil do cliente: "tem gift card? sim/não"). Sem selos de valores produzidos, usar a variante só-pitch. E-mails promocionais de produto (o gift card compete com a oferta principal).

## Orientações de copy para a IA

Headline que mata a objeção de escolher presente (~30 caracteres): "serve pra todo gosto", "impossível errar". Parágrafo 1 funcional: o que é + benefício de conveniência (~110 caracteres); adaptar o destinatário ao contexto (B2C: "quem você ama"; B2B: "seus clientes"). Parágrafo 2 em tríade ritmada "one X, one Y, and Z" (~80 caracteres) — a musicalidade é a assinatura do bloco. CTA nomeando o produto ("DIGITAL GIFT CARD" / "CARTÃO PRESENTE"), não verbo de compra.

## Design system

_(vazio)_

## Direção fotográfica

_(vazio)_

---

HTML: [[_html/body-3-pitch-de-gift-card.html]] · Seção: [[_body]] · Protocolo: [[_protocolo-de-selecao]]
