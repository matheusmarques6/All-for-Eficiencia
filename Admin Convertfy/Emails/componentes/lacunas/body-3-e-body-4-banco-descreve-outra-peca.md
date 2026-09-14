---
tipo: lacuna
sobre: cadastro
secao: body
descoberta_em: 2026-09-09
status: aberta
---

As linhas do banco de [[body-3-pitch-de-gift-card]] e de
[[body-4-comparativo-em-duas-colunas]] carregam nome, tags e schema de
output de peças que não são o HTML que o pipeline monta — as duas notas
do vault já descrevem o HTML (revistas linha a linha em 09/09), mas o que
o vault não alcança continua descrevendo outra coisa e só se corrige com
acesso ao banco.

# O que falta

- **body-3** (`4e9726d1-…`, "body 3 - bridge features cards"). O HTML
  (`_html/body-3-pitch-de-gift-card.html`) é título, dois parágrafos, CTA
  "Digital Gift Card" e três círculos de texto vivo (`<td>` com
  `border-radius`, sem nenhum `<img>`). O nome e as tags gravadas
  (`feature_cards`, `three_features`, `icon_panel_left`, `card_border`,
  `no_cta`, `not_mobile_stacked` — inventário de 31/08) descrevem três
  cards de feature com ícone à esquerda e sem CTA. O schema (7 campos)
  declara `value_seal_1/2/3_image` como imagem gerada — o HTML não tem
  onde recebê-las, e o texto dos três selos, que é o que ele renderiza,
  não tem campo.
- **body-4** (`63736c6c-…`, "body 4 - bridge fundo cards"). O HTML é o
  comparativo em duas colunas (o arquivo foi renomeado de
  `body-4-tutorial-de-uso.html` em 02/09 sem mudança de conteúdo). O nome
  e as tags (`tag_cards`, `pill_tags`, `zigzag_layout`, `overlap_card`,
  `background_image`, `no_cta`) descrevem um zigue-zague de cards com
  pílulas sobre imagem de fundo, sem CTA. O schema (9 campos:
  `section_headline`, `howto_1_title/image/steps`, `howto_2_*`,
  `section_cta_label/url`) é o do tutorial — o exemplo de nenhum dos 9
  campos aparece no HTML. A nota declara `schema_campos: 18` (contagem
  dos slots do HTML), não os 9 do banco.
- A nota de body-4 foi renomeada em 02/09 (`body-4-tutorial-de-uso` →
  `body-4-comparativo-em-duas-colunas`); quatro tabelas do banco guardam
  o caminho da nota. Se alguma ainda aponta para o caminho antigo, o sync
  e a geração leem a peça por um nome que não existe mais.

# Por que importa

O Curador decide pela prosa do vault e o Montador preenche o HTML pelo
schema da linha do banco. Em body-4 o schema não tem placeholder nenhum
no HTML: a copy gerada não tem onde entrar. Em body-3 o schema pede três
imagens que o HTML não usa. Enquanto isso durar, a nota certa não basta —
provavelmente é o que a telemetria segue marcando como
`catalogo_divergente` depois de as notas terem sido corrigidas (a nota de
body-3 já descrevia a peça certa quando foi marcada).

# O que se perde hoje

Duas das três variantes de body ativas e julgadas (ver [[_body]]) têm
contrato de preenchimento que não corresponde à peça montada. body-4 é a
única cobertura ativa de `qualidade-eficacia` e `preco-valor`; se o
Montador não consegue preencher o comparativo, a seção body perde as duas
objeções que tinha.

# Fora do escopo desta entrega

Corrigir nome, tags e schema das duas linhas e conferir o caminho gravado
para body-4 — dado vivo de produção. Mesmo padrão já registrado em
[[tags-do-banco-contradizem-a-prosa]] (hero-8): tag e nome são cadastro,
não julgamento; a prosa do vault é a que vale, e é ela que foi alinhada
ao HTML.
