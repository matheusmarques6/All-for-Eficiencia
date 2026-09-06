---
tipo: indice
assunto: procedencia
autor: max-sturtevant
status: rascunho
---

# A fonte

`CONTEUDO BRUTO/max.md`. Arquivo único, **9.544 linhas, 121.344 palavras,
689.468 bytes** (medido com `wc`, não estimado).

É a transcrição e os decks de um curso de email e SMS marketing para
e-commerce atribuído a Max Sturtevant, fundador da agência Well Copy. Nove
módulos: fundamentos, list growth, flows, campanhas, copywriting, design,
deliverability, otimização, SMS. O material é misto: aulas gravadas
transcritas por ASR, vídeos de YouTube com timestamps, e o texto exportado de
apresentações GAMMA.

**Material de terceiro.** Não foi produzido aqui, não foi licenciado aqui, e
não é para republicação. O corpus em `Advisors/Max/` existe para uso interno
e por isso preserva a procedência linha a linha: toda afirmação sai de uma
linha identificável deste arquivo, e todo descarte está listado abaixo com o
motivo. Sem esse rastro o corpus vira opinião anônima e deixa de ser
auditável.

# Mapa de módulos

Cada módulo aparece duas vezes: primeiro o bloco de transcrição, depois o
bloco do slide GAMMA. As fronteiras abaixo foram confirmadas uma a uma com
`grep -n "^# "` e somam exatamente 9.544 linhas.

| Módulo | Transcrição | Slide GAMMA | Marcador de abertura |
|---|---|---|---|
| Intro / fundamentos | L1–236 | L237–522 | `# INTRO` / `# GAMMA` |
| List Growth | L523–1084 | L1085–1306 | `# LIST GROWTH` / `# GAMMA LIST` |
| Flows | L1307–3403 | L3404–4186 | `# FLOWS` / `# GAMMA FLOWS` |
| Campaigns | L4187–5236 | L5237–5599 | `# CAMPAIGNS` / `# GAMMA CAMPAIGNS` |
| Copywriting | L5600–6500 | L6501–6858 | `# COPYWRITING` / `# GAMMA COPY` |
| Design | L6859–8065 | L8066–8362 | `# DESIGN` / `# GAMMA DESIGN` |
| Deliverability | L8363–8646 | L8647–8759 | `# DELIVERABILITY` / `# GAMMA DELIVERABILITY` |
| Optimization | L8760–9109 | L9110–9212 | `# OPTIMIZATION` / `# GAMMA OPTIMIZATION` |
| SMS | L9213–9260 | L9261–9544 | `# SMS Marketing` / `# GAMMA SMS` |

A distribuição é desigual e isso importa para a cobertura. Flows tem 2.097
linhas de fala; SMS tem 48. Deliverability e Optimization têm decks de 113 e
103 linhas. Onde o bloco é curto, o corpus é raso — não é falha de extração.

# As três camadas

Dentro de cada módulo o material chega em três registros distintos, e os dois
últimos se completam e às vezes discordam.

**1. Bullets de resumo.** Ficam no bloco de transcrição, entre o título da
aula e o marcador `Transcrição do Vídeo :`. São o índice da aula: frases
curtas, sem racional, frequentemente redundantes com a fala que vem logo
abaixo. Exemplos verificados: L5604–5611 (princípios de copy), L5619–5623
(ChatGPT), L4424–4437 (pilares de conteúdo), L8369–8377 (deliverability),
L8522–8526 (warming), L8764–8767 (A/B tests). Redundantes na maioria dos
casos — mas não sempre: L4424–4430 preserva os cinco pilares de conteúdo que
o loop de ASR destruiu na fala (ver descartes).

**2. Transcrição falada.** Onde estão o julgamento, a exceção, o porquê, os
exemplos de marca e a voz. É também onde está todo o ruído: hesitação,
correção no meio da frase, grafia corrompida de nome próprio, e os blocos de
contaminação listados abaixo. Vem em dois formatos — texto corrido quebrado em
linhas curtas (aulas próprias) e linhas com timestamp `(00:00)` ou `00:00`
(vídeos de YouTube reaproveitados).

**3. Slide GAMMA.** Onde estão número de tabela, template verbatim, sintaxe
Klaviyo, checklist e listas fechadas. É o registro que fecha especificação. É
também onde estão quase todos os placeholders mortos, porque o export do GAMMA
trouxe as legendas das imagens sem as imagens.

Um caso de camada ausente: **"The Principles of Good Copy" (L5602) não tem
transcrição.** O marcador `Transcrição do Vídeo :` em L5615 está vazio e L5617
já é a próxima seção. Só existem os bullets L5604–5611. Qualquer nota sobre
S.C.E. que precise do racional falado tem de dizer que ele não está no corpus.

# Descartes

O que não entra em nota nenhuma, com linha e motivo.

## Contaminação — L860–958

Cerca de 50 linhas inseridas no meio da AULA 4 de List Growth (walkthrough de
pop-up no Klaviyo), entre o fim da explicação de compressão de imagem (L858) e
o título da AULA 5 (L960). Não têm relação com o curso. Composição verificada:

- 17 repetições de `The quick brown fox jumps over the lazy dog.` — pangrama
  de teste de microfone (L864, 870, 886, 888, 894, 898, 902, 908, 914, 916,
  922, 928, 932, 934, 938, 952, 956).
- Testes de gravação: "Hello, is this recording working?" (L860), "Is this
  working? Okay, great." (L868), "Is this a real microphone test?" (L872),
  "Is the microphone on?" (L882), "Is it okay if I start the recording now?"
  (L924).
- Conversa doméstica: jantar (L900), compras de mercado com ovos, leite e
  ração de cachorro (L926), "Hey what's going on?" (L936).
- Uma linha em mandarim sobre ata de reunião (L912).
- Timestamp órfão `00:00:15` (L910).
- Release note de produto sem relação nenhuma com email: "The new design is a
  major upgrade… sleeker interface, improved navigation, faster loading
  speeds." (L940). **Armadilha:** lida fora de contexto parece falar de design
  de email. Não fala.
- String de UI: "Are you sure you want to delete this photo?" (L942).
- Frase religiosa solta: "The first major key to the Kingdom is prayer."
  (L944).

Motivo: material de outra gravação, colado por erro. Zero conteúdo do curso.

## Ruído de teste fora do bloco principal

Mesmo tipo de contaminação, em doses menores, nas emendas entre aulas:

| Linhas | Onde | Conteúdo |
|---|---|---|
| L150–156 | fim da AULA 4 de fundamentos | preço/`[unintelligible]` + 2 pangramas + hesitação |
| L164 | logo após `Transcrição da Aula :` da AULA 5 | 1 pangrama antes do conteúdo real começar em L166 |
| L198–210 | fim da AULA 5 | 3 pangramas + espera de trem + testing, testing |
| L231–235 | fim da AULA 6, antes de `# GAMMA` | 2 pangramas + "hoje vamos falar de coding" |
| L559–561 | fim da AULA 1 de List Growth | hesitação sobre reunião + 1 pangrama |

Motivo: TTS/teste de microfone. Nenhuma delas contém afirmação sobre email
marketing. Total de pangramas no arquivo inteiro: 26.

## Falha de ASR — L4480–4488

**Correção de mapa: o loop está em L4480–4488, não em L4293–4301.** L4293–4301
é conteúdo íntegro (revolving door de novos subscribers, graphic vs text
based).

Nove linhas em que o ASR travou repetindo *"If you're going to include those
testimonials"* — até doze vezes na mesma linha, com truncamento no fim. O
trecho fica entre L4478 (fim da explicação do pilar de social proof) e L4490
(retomada já nos percentuais: 20% educational, 20% social proof, 20% product,
20% community branded, 20% sale). O que se perdeu é a enumeração falada dos
pilares de conteúdo restantes e o critério de uso de testimonials.

Recuperação parcial: os bullets em **L4424–4430** listam os cinco pilares
(Educational, Social Proof, Community / Branded, Product or Collection
Highlights, Sales) com um exemplo cada. Use os bullets. O racional falado
sobre testimonials não existe no corpus — se a pergunta for essa, recusar.

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
| L6772–6777 | bloco "Use My AI To Help Write Copy" — repetição literal do pitch de L5473–5478 |
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
  todas as linhas de link. As aulas correspondentes (Klaviyo Walkthrough,
  YouTube Pop-Ups) não têm deck.
- **`![][image1]` quebrado: L3402.** É a **única** ocorrência de referência de
  imagem quebrada no arquivo inteiro. (Correção de mapa: não são dezenas.)
- **45 rótulos órfãos anunciando imagem que não foi exportada.** São o
  equivalente funcional das imagens perdidas — legenda sem figura. Distribuição
  verificada:
  - `**Ex. …**` — 9, todas em GAMMA COPY: L6550, 6552, 6554, 6600, 6602, 6621,
    6623, 6648, 6650.
  - `**Example \#1**` / `**Example \#2**` — 16, todas em GAMMA COPY: L6676,
    6678, 6685, 6687, 6693, 6695, 6701, 6703, 6709, 6711, 6717, 6719, 6725,
    6727, 6794, 6796.
  - `**Step 1/2/3**` — 8: L5480, 5482, 5484 (GAMMA CAMPAIGNS); L6779, 6781,
    6783 (GAMMA COPY); L9348, 9350 (GAMMA SMS).
  - Outros: `**Results**` (L5486); "Example Below: Subject line A/B test
    resulting in 3x more sales." (L6811); `**Mobile:**` / `**Desktop:**`
    (L9354–9355); as quatro legendas de pop-up em L1292, 1294, 1296, 1298;
    "Example of Text Based sale email winner:" (L4170, L9157); "Example of
    categories performing better:" (L4176, L9163).

Consequência prática: os oito tipos de infográfico (L6664–6728) têm o nome e
uma frase de racional cada, e **nenhum exemplo visual**. Perguntas do tipo
"como é um comparison chart dele" não têm resposta no corpus.

# Armadilhas da fonte

Coisas que enganam quem lê rápido. Cada uma foi aberta e conferida.

**1. O título mente sobre a ferramenta.** A seção **L8009 — "Uploading Designs
From Figma To Klaviyo"** tem uma lista de 5 passos (L8011–8015) cujo passo 4
diz "Upload your sections as images into **Klaviyo**". A demonstração inteira,
L8044–8063, é feita no **Omnisend** — o narrador anuncia a troca em L8044 ("for
this video I'm going to use Omnisend… you get a 30% discount if you use me") e
fecha em L8063 com o link de afiliado. Não há um único passo executado em
Klaviyo. Toda nota derivada daqui é `tipo: procedimento`, datada, e tem de
dizer qual plataforma foi realmente demonstrada.

**2. Pelo menos dois narradores.** **L5753** diz *"So we have a email marketing
brain, something that **Max had put together himself**"* — terceira pessoa,
dentro do módulo de copywriting. O mesmo artefato aparece em primeira pessoa em
**L6387** (*"I actually made this with over 500 docs of email marketing
trainings"*) e em **L6774** (*"Lucky for you, I've created the Email Marketing
Brain"*). O bloco em torno de L5753 não é citável como fala do Max. Marcar
`registro: outro-narrador`.

**3. Credenciais autorreportadas e divergentes.** Quatro números diferentes
para a mesma coisa, todos ditos em primeira pessoa:

| Valor | Linha | Formulação verbatim |
|---|---|---|
| $40 million | L6350 | "the exact process that we use at my agency which has generated $40 million for clients in the…" |
| $100 million | L6359 | "I've made $100 million making emails for e-commerce brands." |
| $200 million | L5204 | "hacks that have helped me generate over $200 million for brands" |
| $200M | L3428 | "coming from an email marketer who has generated $200M for brands in their platform" |
| $100M | L3419 | "an email marketing agency that has generated over **$100M in email attributed revenue** for clients" |
| $100M | L9269 | idêntico a L3419, mais "**in the last 12 months**" |

Repare que L3419 e L9269 são a mesma frase de bio com um qualificador temporal
diferente. Nunca resolver por média nem escolher o maior; se a pergunta for de
credencial, mostrar a divergência.

**4. Sunset Flow não existe.** **L3398–3403**: título `# Sunset Flow`, um link
gamma (L3400) e um `![][image1]` quebrado (L3402). Nada mais. O Sunset Flow
também não tem seção no deck — `# GAMMA FLOWS` começa em L3404. Aparece só como
item de lista em L92. Zero conteúdo. Caso de recusa obrigatória.

**5. Grafias corrompidas pelo ASR.** Nomes próprios chegam deformados e a busca
literal falha. Contagens medidas no arquivo:

- **Klaviyo** — 135 grafias corretas contra 32 corrompidas: *Clavio* (21),
  *Claio* (5), *Clavia* (4), *Klavio* (1, L722), *Clavier* (1, L1027).
- **Milled** (milled.com, site de swipe file) — correto 10x (o link real está
  em L4432); vira *mild* em L6269, *MILD* em L6364 ("looking at MILD, which is
  just a free website, mil.com") e *Mild* em L7875.
- **Alia** (plataforma de pop-up) — correto 6x; vira *Aulia* (L615), *Oly*
  (L617), *Olla* (L647, duas vezes), *Allie* (L966, duas vezes), *Olea* (L984,
  "I love Olea… olealearn.com"). O domínio real é `alialearn.com` (L1246).
- **cart abandon** → *card abandon* em L2363 e L2442.
- **site abandon** → *side abandon* em L92, L2401 e L2466.

Ao buscar qualquer um desses termos no bruto, buscar todas as variantes.

**6. O deck de Optimization repete o deck de Flows.** Três seções aparecem duas
vezes, quase verbatim: *Flow Time Delays* (L4141–4145 = L9176–9180), *SLs and
PTs* (L4153–4162 = L9165–9174) e *Graphic vs Text Based* + *Promoting
Categories vs Products* (L4164–4176 = L9151–9163). A única diferença material
é um typo: L4160 traz "Ilusing" onde L9172 traz "Using". Não são duas fontes
independentes — não contar como confirmação cruzada.

# Como usar este mapa

Ao verificar uma afirmação de qualquer nota: pegue a linha citada no
`fonte:` do frontmatter e abra-a no bruto — `sed -n 'X,Yp' "CONTEUDO
BRUTO/max.md"`. Se a linha sustenta a afirmação, a nota está certa. Se a linha
não sustenta, **o erro é da nota**, não do corpus, e a nota se corrige contra a
linha.

Se a linha citada cair dentro de uma faixa de descarte listada acima, a nota
não deveria existir: apague-a.

Se a afirmação não tiver linha nenhuma, ela foi inventada. Mesmo destino.
