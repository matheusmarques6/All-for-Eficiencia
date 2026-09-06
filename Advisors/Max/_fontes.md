---
tipo: indice
assunto: procedencia
autor: max-sturtevant
status: rascunho
---

# A fonte

`CONTEUDO BRUTO/max.md`. Arquivo único, **9.544 linhas, 121.344 palavras,
689.468 bytes** (medido com `wc`, não estimado).

Ressalva de contagem: `wc -l` conta quebras de linha e o arquivo não termina
com uma. Existe uma **linha 9.545**, fora do mapa de módulos abaixo — a
definição de referência `[image1]: <data:image/png;base64,…>`, 14.686
caracteres, um PNG de 624×169 embutido. É a imagem que `![][image1]` (L3402)
aponta.

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
`grep -n "^# "`: 18 marcadores, faixas contíguas de L1 a L9544, sem buraco nem
sobreposição, somando 9.544 linhas. A L9545 (definição base64 acima) não
pertence a módulo nenhum.

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
aula e o marcador de transcrição. São o índice da aula: frases curtas, sem
racional, frequentemente redundantes com a fala que vem logo abaixo.
Exemplos verificados: L5604–5611 (princípios de copy), L5619–5623
(ChatGPT), L4424–4437 (pilares de conteúdo), L8369–8377 (deliverability),
L8522–8526 (warming), L8764–8767 (A/B tests). Redundantes na maioria dos
casos — mas não sempre: L4424–4430 preserva os cinco pilares de conteúdo que
o loop de ASR destruiu na fala (ver descartes).

Ao buscar o marcador, cuidado: ele tem **oito grafias** no arquivo —
`Transcrição do Vídeo :` (29×), `Transcrição da Aula :` (5×), e uma ocorrência
cada de `Transcrição da Aula:`, `Transcrição do Audio :`, `Transcrição do
Áudio :`, `Transcrição de Audio:`, `Transcrição da Loja :` e `Transcrição dos
Texto :` — mais `Transcripts:` (6×) nos blocos vindos do YouTube.

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
transcrição.** O marcador `Transcrição do Vídeo :` em L5615 está vazio — é o
único marcador vazio do arquivo inteiro — e L5617 já é a próxima seção. Só
existem os bullets L5604–5611 e o link gamma (L5613). Qualquer nota sobre
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

Cinco linhas de fala — L4480, 4482, 4484, 4486 e 4488, intercaladas por linhas
vazias — em que o ASR travou repetindo *"If you're going to include those
testimonials"*: 7, 10, 11, 10 e 12 vezes na mesma linha, com truncamento no
fim de cada uma. O trecho fica entre L4478 (fim da explicação do pilar de
social proof) e L4490, onde a fala retoma já nos percentuais ("20%
educational, 20% social proof, 20% product, 20% community branded, one sale,
two sale emails, so 20%"). O que se perdeu é a enumeração falada dos
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
- **77 rótulos órfãos anunciando imagem que não foi exportada.** São o
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
  - Legendas de exemplo em GAMMA DESIGN — 13: `✅ **Button Above The Fold**`,
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

**3. Credenciais autorreportadas e divergentes.** Três valores diferentes para
a mesma coisa — $40M, $100M e $200M — em oito formulações. Sete são em primeira
pessoa; L3428 fala de si em terceira ("an email marketer who…"):

| Valor | Linha | Formulação verbatim |
|---|---|---|
| $40 million | L6260 | "coming from a $40 million email marketer" |
| $40 million | L6350 | "the exact process that we use at my agency which has generated $40 million for clients in the…" |
| $100 million | L6359 | "I've made $100 million making emails for e-commerce brands." |
| $100M | L5351 | "84 high-converting email campaigns handpicked by me a $100M email marketer." |
| $200 million | L5204 | "hacks that have helped me generate over $200 million for brands" |
| $200M | L3428 | "coming from an email marketer who has generated $200M for brands in their platform" |
| $100M | L3419 | "an email marketing agency that has generated over $100M in email attributed revenue for clients" |
| $100M | L9269 | idêntico a L3419, mais "in the last 12 months" |

Repare que L3419 e L9269 são a mesma frase de bio com um qualificador temporal
diferente. Nunca resolver por média nem escolher o maior; se a pergunta for de
credencial, mostrar a divergência.

**4. Sunset Flow não tem aula.** **L3398–3403**: título `# Sunset Flow`, um
link gamma (L3400) e o `![][image1]` (L3402) — que aponta para o PNG embutido
na L9545, ilegível como texto. Nada mais. O Sunset Flow também não tem seção no
deck de flows: `# GAMMA FLOWS` começa em L3404.

Mas **não é zero conteúdo**, e a recusa tem de ser calibrada. O corpus diz três
coisas sobre ele, fora da aula:

| Linha | Registro | O que diz |
|---|---|---|
| L92 | transcrição | item de lista dos flows configurados na conta de exemplo ("Browse Abandon, Cart Abandon, Checkout Abandon, Post Purchase, Side Abandon, Sunset, Welcome, Win Back") |
| L411 | slide (glossário) | definição: "**Sunset Flow** – Triggered when a contact is no longer engaging. Removes or suppresses inactive users." |
| L5127 | transcrição | promessa não cumprida, dentro da aula de segmentação: "We'll talk about this more in the Sunset Flow, obviously, as well." — o critério de supressão que ele descreve ali (L5129) é o vizinho mais próximo |

Ou seja: existe gatilho e finalidade (L411), não existe sequência, delay,
número de emails nem copy. A recusa nomeia essa fronteira — não diz que o
corpus é mudo sobre Sunset Flow.

**5. Grafias corrompidas pelo ASR.** Nomes próprios chegam deformados e a busca
literal falha. Contagens medidas no arquivo, por ocorrência (não por linha),
busca case-insensitive:

- **Klaviyo** — 136 grafias corretas contra 32 corrompidas: *Clavio* (21),
  *Claio* (5), *Clavia* (4), *Klavio* (1, L722), *Clavier* (1, L1027).
- **Milled** (milled.com, site de swipe file) — correto 11x (o link real está
  em L4432); vira *mild* em L6269, *MILD* em L6364 ("looking at MILD, which is
  just a free website, mil.com") e *Mild* em L7875.
- **Alia** (plataforma de pop-up) — correto 7x: L960, 1013, 1202, 1239, 1242,
  1243, 1302. **Cuidado:** L1242 traz `Alia` cercado de zero-width spaces e
  escapa de busca com `\b` — quem contar com `grep -o '\balia\b'` acha 6. Vira
  *Aulia* (L615), *Oly* (L617), *Olla* (L647, duas vezes), *Allie* (L966, duas
  vezes), *Olea* (L984, "I love Olea… olealearn.com"). Os domínios são
  `aliapops.com` (L1053) e `alialearn.com` (L1246). Ainda: "alias" em L2995,
  L2997 e L3904 é o *row alias* do Klaviyo, não a plataforma — falso positivo.
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
