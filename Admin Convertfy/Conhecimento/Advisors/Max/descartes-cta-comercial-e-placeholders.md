---
tipo: indice
assunto: procedencia
autor: max-sturtevant
status: aprovado
---

Dois tipos de conteúdo do arquivo bruto `CONTEUDO BRUTO/max.md` não viram nota:
os CTAs comerciais — links de afiliado, pitch de agência, comunidade Skool,
"book a call" — que são venda e não doutrina, e os placeholders que anunciam
conteúdo que não foi exportado, incluindo 79 rótulos órfãos de imagem dentro
dos blocos GAMMA. Esta nota lista os dois grupos linha a linha, com as exceções
que não são descarte e o que se perde de fato.

# Descartes por CTA comercial e por placeholder

O que não entra em nota nenhuma, com linha e motivo. Os descartes por ruído de
gravação e falha de ASR estão em [[descartes-contaminacao-e-falha-de-asr]].

## CTA comercial

Não entram em nota. São venda, não doutrina.

| Linhas | O que é |
|---|---|
| L358–362 | link de afiliado Klaviyo (`utm_source=001Nu0000022YR4IAM`) e Omnisend (`omnisend.com/max`, "30% OFF first 3 months with my link") |
| L1029 | pitch de agência dentro do vídeo: "we've worked with over 279 figure ecommerce brands… you can book a call below" |
| L1241, L1245–1246 | link de afiliado Klaviyo + "Say Max sent you when you book a call and you'll get a gift ;)" + alialearn.com |
| L3417–3424 | bio "I'm Max… founder of Well Copy" + Instagram, Twitter, LinkedIn, YouTube |
| L3426–3429 | "Sign Up For Klaviyo For Email Marketing" com a credencial de $200M |
| L3458–3465 | comunidade Skool (`skool.com/email-marketerz`), "30+ Module Email course", "Join Community »" |
| L4178–4186 | "That's It For This One!" + "Want More Help?" + book a free discovery consultation call ($50k/mo) |
| L4436 | link do custom GPT `wellcopy.net/gpt` dentro dos bullets de calendário |
| L5204 | "click the link in the description, first link" + credencial de $200M |
| L5212 | plug de `wellcopy.net/GPT` dentro do vídeo de text-based |
| L5473–5478 | bloco "Using AI For Calendar Creation" — pitch do Email Marketing Brain |
| L5621, L5623 | links do GPT e do Copy Template nos bullets de copy |
| L6262 | "here's my Instagram you can follow me if you want" |
| L6772–6777 | bloco "Use My AI To Help Write Copy" — repetição quase literal do pitch de L5473–5478; só mudam o título e o acréscimo de "write copy," em L6775 |
| L8044, L8063 | link de afiliado Omnisend dentro do walkthrough de upload ("30% off for the first three months") |
| L8637 | CTA de Instagram e giveaway pertencente à marca do exemplo, não ao curso |
| L9259 | "book a call with me… free Consulting call" ($50.000/mês) |
| L9267–9278 | bio + socials + três links de YouTube |
| L9280–9282, L9527–9529 | "Join My Free 3x Per Week Newsletter" (duas ocorrências) |
| L9377 | segunda ocorrência do "Join Community »" do Skool |
| L9525–9544 | bloco de encerramento: newsletter, e-mail pessoal, quatro socials, "Want More Help?" com book a call |

Duas exceções que **não** são descarte: a comparação Klaviyo vs Omnisend em
L34 e L357–358 contém julgamento de ferramenta ("Klaviyo is just the best…
Omnisend is a solid budget option"), e o critério de $50k/mo aparece repetido
o bastante para ser um dado sobre o público que ele atende. Registrar o
julgamento, descartar o link.

## Placeholders sem conteúdo

- **L1304 — `\[need\]`.** Marcador de produção deixado no deck de List Growth,
  sob o título "Alia Pop-Up Form Creation" (L1302). O tutorial de Alia no deck
  não existe. O título "Klaviyo Pop-Up Form Creation" (L1300) também está
  vazio.
- **Campos de link GAMMA vazios: L42 (`link do gamma app :`) e L988
  (`Link do gamma :`).** Os únicos dois do arquivo — checado com regex sobre
  todas as linhas de link. A aula de YouTube Pop-Ups não tem seção nenhuma no
  deck. Klaviyo Walkthrough tem seção (L364), mas ela é só a frase
  `Watch the video below for a Klaviyo walkthrough.` (L366).
- **`![][image1]`: L3402.** É a única referência de imagem do arquivo inteiro
  (correção de mapa: não são dezenas) e **não está quebrada**: a definição
  `[image1]: <data:image/png;base64,…>` está na L9545 e carrega um PNG de
  624×169. Não é legível como texto, mas a imagem existe no arquivo.
- **79 rótulos órfãos anunciando imagem que não foi exportada.** *(Era 77;
  a varredura de falsos negativos achou dois a mais em GAMMA DESIGN — ver
  abaixo.)* São o
  equivalente funcional das imagens perdidas — legenda sem figura, nada abaixo
  dela até o próximo título. Todos dentro de blocos GAMMA. Distribuição
  verificada:
  - `**Ex. …**` — 9, todas em GAMMA COPY: L6550, 6552, 6554, 6600, 6602, 6621,
    6623, 6648, 6650.
  - `**Example \#1**` / `**Example \#2**` — 16, todas em GAMMA COPY: L6676,
    6678, 6685, 6687, 6693, 6695, 6701, 6703, 6709, 6711, 6717, 6719, 6725,
    6727, 6794, 6796.
  - `**Step 1/2/3**` — 8: L5480, 5482, 5484 (GAMMA CAMPAIGNS); L6779, 6781,
    6783 (GAMMA COPY); L9348, 9350 (GAMMA SMS). Fecham a sequência
    `**Results**` (L5486) e `**Output**` (L6785).
  - `**Email Example:**` — 12, todas em GAMMA FLOWS: L3642, 3663 (Site
    Abandon); L3700, 3721, 3742, 3763 (Browse Abandon); L3817, 3838, 3859,
    3881 (Cart / Checkout Abandon); L3948, 3966 (Post-Purchase). É o exemplo
    visual de **cada email de cada flow de abandono** que não existe.
  - Legendas de exemplo em GAMMA DESIGN — **15**: `#### **Great Examples That
    Follow Best Practices**` (L8143, fecha a lista "Email Design That Drives
    Clicks" e a linha seguinte já é o Princípio #1) e
    `#### **Optimized Product Section Example:**` (L8289, a linha seguinte já é
    `# **Footer**`) — **os dois faltavam nesta contagem**; mais
    `✅ **Button Above The Fold**`,
    `✅ **Large Centered Button**`, `❌ **Unclear, Small Button**`,
    `**Uncentered, Small Button**` (L8173, 8175, 8177, 8179);
    `✅ **Simple \+ Use Of Infographic**`, `✅ **Simple \+ Highlighted Main
    Points**`, `❌ **Too Complex**` (L8207, 8209, 8211); "Here's an example:"
    (L8230); `✅ **Optimized Hero Section**` duas vezes (L8253, 8255); "Here
    are some other simple examples:" (L8272); `**Good Example \#1/\#2**`
    (L8298, 8300).
  - Outros: "Example Below: Subject line A/B test resulting in 3x more sales."
    (L6811); `**Mobile:**` / `**Desktop:**` (L9354–9355); as quatro legendas de
    pop-up em L1292, 1294, 1296, 1298; "Example of Text Based sale email
    winner:" (L4170, L9157); "Example of categories performing better:"
    (L4176, L9163); `**Graphic Based Email**` / `**Text-Based Email**` (L5309,
    5311); `**1 SMS Long**` / `**3 SMS Long (triple the cost)**` (L9397, 9399);
    `**Base Strategy:**` (L3509); `**Segment Definition for 90 Day Winback
    Flow:**` (L4057).

Dois desses doem mais que os outros. **L4057** anuncia a definição de segmento
do Winback de 90 dias e não entrega nada — a especificação do segmento não
existe em lugar nenhum do corpus. E **L8307** ("Here are a few methods to do
this:") fecha a seção `# **Email Transitions**` (L8302) sem listar método
nenhum: o deck de design não diz como fazer transição.

Consequência prática: os nove tipos de infográfico (L6664–6727 — Checklists,
Icon Graphics, Feature Diagrams, Timelines, Numbered Lists, Comparison Chart,
Tables, Flow Charts, Graphs) têm o nome e uma frase de racional cada, e
**nenhum exemplo visual**. Perguntas do tipo "como é um comparison chart dele"
não têm resposta no corpus.
