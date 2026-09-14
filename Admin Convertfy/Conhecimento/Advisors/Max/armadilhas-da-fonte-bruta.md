---
tipo: indice
assunto: procedencia
autor: max-sturtevant
status: aprovado
---

Sete trechos do arquivo bruto `CONTEUDO BRUTO/max.md` enganam quem lê rápido:
um título anuncia Klaviyo e a demonstração é no Omnisend, cerca de 25% da fala
é de um segundo narrador, a credencial de receita da agência tem três valores,
o Sunset Flow não tem aula, nomes próprios chegam corrompidos pelo ASR, o deck
de Optimization repete o de Flows e dois cortes de transcrição em
deliverability levaram conteúdo embora. Esta é a nota que mais evita erro de
leitura do corpus.

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

**As cinco faixas não atribuíveis a Max**, do laudo [[mapa-da-autoria]] §6 — este é o
recorte que falta no mapa de módulos acima, porque ele corta **dentro** do bloco
de transcrição de cada módulo:

| Faixa | Módulo | Classificação |
|---|---|---|
| L5617–5866 | Copywriting (ChatGPT) | **`outro-provado`** — prova nominal em L5753 |
| L4189–5154 | Campaigns (fala inteira) | `outro-provavel` |
| L5867–6248 | Copywriting (infográficos, subject lines) | `outro-provavel` |
| L8365–8646 | Deliverability (fala inteira) | `outro-provavel` |
| L8762–9109 | Optimization (fala inteira) | `outro-provavel` |

Duas ressalvas que decidem casos concretos:

- **Os slides correspondentes não estão em causa** (L5237–5599, L6501–6858,
  L8647–8759, L9110–9212): são artefato escrito de Max.
- **Dentro de cada faixa, o cabeçalho de bullets vem antes da fala** e também é
  artefato escrito. As dez fronteiras: L4189-4200 · L4422-4440 · L4676-4683 ·
  L4829-4843 · L5617-5664 · L5867-5885 · L6083-6098 · L8365-8378 · L8518-8529 ·
  L8762-8770. Só o que vem **depois** do marcador `Transcrição do Vídeo :` é fala
  não-Max.

Consequência para o método de verificação do fim de [[mapa-das-fontes]]: ao abrir
a linha
citada no `fonte:`, conferir também **contra esta tabela**. Linha dentro de faixa
não-Max sustenta a afirmação, mas não a atribuição.

**A assinatura de abertura não é critério** e nunca foi. L7603 abre com "Hello,
hello" e é comprovadamente Max — em L7817 ele digita `@max` e diz "tags me"
([[mapa-da-autoria]] §5). Nenhuma nota deve classificar autoria por saudação.

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
| L5127 | **outro-narrador** | promessa não cumprida, dentro da aula de segmentação: "We'll talk about this more in the Sunset Flow, obviously, as well." — o critério de supressão descrito ali (L5129) é o vizinho mais próximo. Quem promete não é Max |

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

**7. Dois cortes de transcrição em deliverability — a única perda de conteúdo
mensurável do corpus.** No vídeo de warming (L8531–8645), a mediana entre
marcas de tempo é 11s e o p90 é 18s. Dois saltos fogem da distribuição, e são
o primeiro e o segundo maiores do vídeo inteiro: **21:52 → 22:33 (L8641 →
L8642, 41s)** e **13:04 → 13:33 (L8593 → L8594, 29s)**.

O corte de 41s levou **o nome da ferramenta de otimização de HTML** que a aula
recomenda para quem cai na aba de promoções — a narração descreve a ferramenta, diz
que trabalha com marcas conhecidas, e nunca a nomeia. (Essa narração é
**`outro-narrador`**: L8532-8646, ver [[mapa-da-autoria]].) Irrecuperável: nunca
deduzir nem sugerir um nome. Evidência independente do corte: L8641 emenda
duas frases de assuntos diferentes sem pontuação ("questions that I can help
If your emails are landing in spam"), o que localiza a perda dentro da linha.

O corte de 29s cai no meio do raciocínio de reparo de reputação.


O mapa da fonte — o que ela é, as fronteiras de módulo e as três camadas — está
em [[mapa-das-fontes]]. O que foi descartado está em
[[descartes-contaminacao-e-falha-de-asr]] e
[[descartes-cta-comercial-e-placeholders]].
