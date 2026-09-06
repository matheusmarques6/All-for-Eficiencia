---
tipo: indice
assunto: autoria
autor: max-sturtevant
status: rascunho
---

# 1. O problema e por que importa

O corpus inteiro existe para clonar o julgamento de **uma** pessoa. O material
bruto, porém, é uma compilação de curso: 41 blocos de fala de origens diferentes
— aulas gravadas, vídeos de YouTube reaproveitados, walkthroughs de tela — mais
nove decks GAMMA. Nada no arquivo declara quem fala em cada bloco.

Uma linha prova que não é sempre a mesma pessoa. **L5753** diz:

> "So we have a email marketing brain, something that **Max had put together
> himself**. And it's awesome."

Terceira pessoa. Se essa faixa entrar no corpus como fala do Max, o advisor
passa a devolver, na voz dele e com a autoridade dele, o julgamento de outra
pessoa — e não há como um leitor da nota perceber. É o único tipo de erro deste
corpus que é **invisível na saída**: um número errado alguém confere, uma voz
errada ninguém confere.

Este laudo determina, bloco a bloco, quem fala.

---

# 2. O padrão de prova

Cinco níveis. Cada classificação exige evidência **nomeada por linha**.

| Nível | O que exige |
|---|---|
| `max-provado` | O narrador se identifica: é chamado de "Max" na própria fala, ou reivindica em primeira pessoa um ativo que só Max possui — o link de afiliado `omnisend.com/max`, a agência Well Copy, a comunidade Skool, o custom GPT, os designers da agência, o canal de YouTube. |
| `outro-provado` | O narrador fala de Max em terceira pessoa. |
| `max-provavel` | Sem auto-identificação nominal, mas com o **idioleto** de Max (ver §2.1) e/ou continuidade anunciada em primeira pessoa a partir de um bloco `max-provado`. |
| `outro-provavel` | Pertence ao aglomerado estilométrico do único bloco `outro-provado`, com **ausência total** dos marcadores de idioleto de Max e presença dos marcadores complementares. |
| `indeterminado` | Não há fala, ou não há sinal. |

**Assinatura de abertura não é prova de nada.** Isto foi testado e falhou — ver
§5. Um bloco classificado só pela abertura não recebe classificação nenhuma.

## 2.1 O critério que sobreviveu: idioleto, não assinatura

Cinco marcadores, medidos por ocorrência sobre o total de palavras faladas. As
duas colunas são o aglomerado A (75.381 palavras) e o aglomerado B (25.141
palavras), definidos ao fim desta medição, não antes dela.

| Marcador | A (/1.000 pal.) | B (/1.000 pal.) | Razão |
|---|---|---|---|
| "I recommend" / "I'd recommend" / "I highly recommend" | 0,42 (32×) | **0,00 (0×)** | ∞ |
| "my favorite" | 0,19 (14×) | **0,00 (0×)** | ∞ |
| "I like to" | 0,62 (47×) | 0,04 (1×) | 16× |
| "at the end of the day" | 0,027 (2×) | **1,03 (26×)** | 39× |
| "obviously" | 0,19 (14×) | **1,75 (44×)** | 9,4× |

Os três primeiros são **enunciados de preferência pessoal** — a marca de quem
tem autoridade própria sobre o assunto. Os dois últimos são **muletas de
discurso**. Se o aglomerado B fosse a mesma pessoa, a taxa de "I recommend" do
aglomerado A projetaria 10,6 ocorrências esperadas em B; observaram-se **zero**
(Poisson, λ=10,6 → p ≈ 2,5·10⁻⁵). Na direção inversa, a taxa de "at the end of
the day" de B projetaria 78 ocorrências em A; observaram-se **duas**.

Reforço independente, o **fecho de vídeo**. Os dez blocos do aglomerado B fecham
com pedido coletivo — "hit us up" (L4420, L9108), "reach out to us" (L4674),
"shoot us over emails, ask us questions. We're here for you" (L4827), "thank you
guys ... see you in the next one" (L5153, L5865, L6081, L6247, L8516, L8645).
Essa fórmula **não ocorre nenhuma vez** fora do aglomerado B. Os blocos
`max-provado` fecham no singular: "let me know if you have any questions" (L677,
L8064), "message me or the group" (L2616), "book a call with me" (L9259).

## 2.2 O teste que decidiu

Em **25.141 palavras** do aglomerado B não existe **um único possessivo de
primeira pessoa sobre ativo de negócio**. Varredura exaustiva de `my \w+`
naquelas faixas devolve, ao todo: `my inbox`, `my dad`, `my head` (2×), `my
camera`, `my list` (hipotético), `my brand` (hipotético). Nada mais.

Nas faixas `max-provado` o mesmo padrão devolve: `my link` (L34), `my checklist`
(L617), `my resources` (L686), `my agency` (L6350), `my community my school`
(L6279), `my designers` (L6458), `my channel` (L6499), `my company's name`
(L8046), `my clients` (L9237), `my newsletter` (L6350), além de `my favorite`
14×.

É essa assimetria — não a saudação — que sustenta o laudo.

---

# 3. A tabela mestra

41 blocos. Faixas contíguas, conferidas contra `grep -n "^# "`, os 21 marcadores
`\# File-…` e os 45 marcadores de transcrição.

| # | Vídeo | Faixa | Módulo | Classificação | Evidência nomeada |
|---|---|---|---|---|---|
| 1 | AULA 1 — Profitable Ecommerce Funnel | L3–14 | Intro | `max-provavel` | idioleto A; "at the end of the day" 1× (L9) é a única fuga do aglomerado A |
| 2 | AULA 2 — 3.5 Pillars | L15–23 | Intro | `max-provavel` | idioleto A; nenhum marcador B |
| 3 | AULA 3 — Setting Up Your ESP | L24–39 | Intro | **`max-provado`** | **L34: "if you use my link below right here, which is uh omnisend.com/max"** — o narrador é dono do link `omnisend.com/max` (idem deck L358) |
| 4 | AULA 4 — Klaviyo Walkthrough | L40–157 | Intro | `max-provavel` | continuidade anunciada em 1ª pessoa por bloco `max-provado` (#3): L36 "I'm going to walk through a Klaviyo tutorial"; L82 "that's how I recommend creating your emails" |
| 5 | AULA 5 — Core Metrics | L158–211 | Intro | `max-provavel` | idioleto A; zero marcadores B em 1.045 palavras |
| 6 | AULA 6 — Glossary | L212–236 | Intro | `max-provavel` | "yada yada" (L227); zero marcadores B |
| 7 | AULA 1 — Types of List Growth | L525–562 | List Growth | `max-provavel` | zero marcadores B |
| 8 | AULA 2 — Importance of Pop-Ups | L563–604 | List Growth | `max-provavel` | zero marcadores B |
| 9 | AULA 3 — Effective Pop-Up Forms | L605–678 | List Growth | **`max-provado`** | **L631: "If you ask me, Hey Max, do you want 10% off? ... if you went up to me and said, Hey Max, $20 off"** — o falante se põe como o interlocutor chamado Max. Reforço: L617 "run your form through my checklist" ≡ deck L1206/L1208; L615 "I've tested this across multiple different brands" |
| 10 | AULA 4 — Klaviyo Pop-Up Walkthrough | L679–959 | List Growth | **`max-provado`** | anunciado como próprio pelo bloco `max-provado` #9: **L677 "physically step-by-step how I'm creating these inside of Klaviyo"**; L686 "the rest of my resources on um forms" e "my favorite form" (mesma linha) |
| 11 | AULA 5 — Alia Walkthrough | L960–985 | List Growth | `max-provavel` | mesmo anúncio L677 ("all the pop-up form creation I'm going to be providing"); L984 "I love Olea" |
| 12 | AULA 6 — YouTube Pop-Ups | L986–1084 | List Growth | **`max-provado`** | **L1014: "Just say that Max sent you a 30-day free trial"** ≡ deck L1245 "Say Max sent you when you book a call"; L1029 pitch da agência em 1ª pessoa do plural com CTA próprio |
| 13 | Welcome Flow | L1309–2325 | Flows | `max-provavel` | idioleto A denso: "I like to" 4× (L1440, L1520+), "boom" 13×, "yada" 8×; zero marcadores B em 4.394 palavras |
| 14 | Site Abandon Flow | L2326–2432 | Flows | `max-provavel` | "boom" 5×; zero marcadores B |
| 15 | Browse Abandon Flow | L2433–2617 | Flows | `max-provavel` | **L2616: "feel free to message me or the group as well"** — o narrador se distingue do grupo/comunidade; L2536 "I like to do FAQs"; L2594 "what i recommend is go into klaviyo" |
| 16 | Cart / Checkout Abandon | L2618–3020 | Flows | `max-provavel` | L2831 "I recommend testing discounts"; L2943 "I always recommend coming from an actual person"; zero marcadores B em 1.872 palavras |
| 17 | Post Purchase Flow | L3021–3221 | Flows | `max-provavel` | L3028 "One of my favorite flows" |
| 18 | Replenishment Reminder | L3222–3304 | Flows | `max-provavel` | zero marcadores B |
| 19 | Winback Flow | L3305–3397 | Flows | `max-provavel` | zero marcadores B |
| 20 | Sunset Flow | L3398–3403 | Flows | `indeterminado` | não há fala nenhuma (título + link + `![][image1]`) |
| 21 | Campaign Strategy | L4189–4421 | Campaigns | `outro-provavel` | "at the end of the day" 5× (L4208, L4240, L4242, L4336, L4386), "obviously" 7×, "I recommend"/"my favorite"/"I like to" **0×** em 2.875 palavras; fecho L4420 "feel free to hit us up" |
| 22 | Campaign Calendar Creation | L4422–4675 | Campaigns | `outro-provavel` | "at the end of the day" 2× (L4448, L4658), "obviously" 6×, zero idioleto A; fecho L4674 "feel free to reach out to us" |
| 23 | Creating Great Campaigns | L4676–4828 | Campaigns | `outro-provavel` | "at the end of the day" (L4747), "obviously" 2×, zero idioleto A; fecho L4827 "shoot us over emails, ask us questions. We're here for you"; L4823 "results for our clients" |
| 24 | Segmentation | L4829–5154 | Campaigns | `outro-provavel` | "at the end of the day" (L4919), "obviously" 3×, zero idioleto A em 2.745 palavras; fecho L5153 "thank you guys very much for watching, and we'll see you in the next one" |
| 25 | Text Based Email Masterclass (YT) | L5155–5236 | Campaigns | **`max-provado`** | **L5212: "you can get access to my custom GPT right here called the email marketing brain"** — 1ª pessoa sobre o mesmo artefato que L5753 atribui a terceiro; L5204 credencial "$200 million" em 1ª pessoa |
| 26 | The Principles of Good Copy | L5602–5616 | Copywriting | `indeterminado` | marcador de transcrição vazio (L5615) — o único do arquivo; só bullets e link |
| 27 | ChatGPT Copywriting | L5617–5866 | Copywriting | **`outro-provado`** | **L5753: "something that Max had put together himself"** — ver §4.1 |
| 28 | Utilizing Infographics | L5867–6082 | Copywriting | `outro-provavel` | "obviously" 7× em 2.039 palavras (a maior taxa do arquivo), "at the end of the day" (L6033), zero idioleto A; fecho L6081 "thank you guys very much ... we'll see you in the next video" |
| 29 | Subject Lines & Preview Texts | L6083–6248 | Copywriting | `outro-provavel` | "at the end of the day" 5× (L6109, L6167, L6223, L6225, L6233) em 1.468 palavras, zero idioleto A; fecho L6247 "thank you guys again for watching. See you in the next one" |
| 30 | Gymshark's Emails in 47 min (YT) | L6253–6352 | Copywriting | **`max-provado`** | **L6350: "the exact process that we use at my agency which has generated $40 million"** + "subscribe to my newsletter" (mesma linha); **L6279: "Community we have over 450 people ... shout out to you Dominic"** |
| 31 | MrBeast's Emails in 42 min (YT) | L6353–6500 | Copywriting | **`max-provado`** | **L6359: "I've made $100 million making emails for e-commerce brands"**; **L6387: "I actually made this with over 500 docs"** (o Email Marketing Brain, em 1ª pessoa); **L6458: "one of my designers on hand ... Shout out Diana"**; L6499 "my channel" |
| 32 | Importance Of Email Design | L6861–6999 | Design | `max-provavel` | zero marcadores B em 1.193 palavras |
| 33 | The Principles of Good Design | L7000–7220 | Design | `max-provavel` | L7029 "I'd recommend majority of them"; "at the end of the day" 1× (L7013) é a segunda e última fuga do aglomerado A |
| 34 | Mastering The Different Email Sections | L7221–7589 | Design | `max-provavel` | L7384 "which is my favorite"; L7580 "my favorite is to add transitions behind photos"; zero marcadores B em 2.014 palavras |
| 35 | Figma Email Design Walkthrough | L7590–7840 | Design | **`max-provado`** | **L7817–7818: "You could be, 'Hey, at max, this is terrible.' Let me just make sure it actually tags me"** — ver §5, é a contraprova do laudo |
| 36 | Designing Walkthroughs | L7841–8008 | Design | `max-provavel` | **L7871: "these are my websites for finding emails to steal from"** ≡ deck L8311/L8317 "My Best Tip For Design: STEAL! / Use These Websites For Finding Emails to Steal From" — alinhamento em 1ª pessoa com o slide; L7875, L7883, L7905, L7957 "my favorite" 4× |
| 37 | Uploading Designs (YT) | L8009–8065 | Design | **`max-provado`** | **L8044: "You get a 30%, uh, discount if you use me"** (= `omnisend.com/max`, L34/L358); **L8046: "I'll say well copy because that's my company's name"** |
| 38 | What is Deliverability? | L8365–8517 | Deliverability | `outro-provavel` | "at the end of the day" 4× (L8386, L8392, L8468, L8490), "essentially" 8×, zero "I recommend"/"my favorite"; L8416 "feel free to message our team as well"; fecho L8516 "let us know if you guys have any questions" |
| 39 | Warming Your Domain | L8518–8646 | Deliverability | `outro-provavel` | "at the end of the day" (L8542), "obviously" 4×, zero idioleto A em 4.204 palavras; fecho L8645 "please let us know if you have any questions" |
| 40 | High Leverage A/B Tests | L8762–9109 | Optimization | `outro-provavel` | "obviously" **9×** em 3.121 palavras, "at the end of the day" 3× (L8928, L8932, L8936), zero idioleto A; L8798 "the tests that our team runs"; fecho L9108 "feel free to hit us up" |
| 41 | SMS Marketing Masterclass (YT) | L9215–9260 | SMS | **`max-provado`** | **L9258: "in the doc I have a swipe file of 30 SMS messages which I handpicked"** ≡ deck L9522 "I went through Attentive's SMS database and picked 30 of my favorite SMS messages"; **L9259 "you can book a call with me"**; L9237 "I like to always have that for all of my clients" |

**Contagem:** 9 `max-provado` · 20 `max-provavel` · 1 `outro-provado` ·
9 `outro-provavel` · 2 `indeterminado`.

## 3.1 Os decks GAMMA

Os nove blocos GAMMA (L237–522, L1085–1306, L3404–4186, L5237–5599, L6501–6858,
L8066–8362, L8647–8759, L9110–9212, L9261–9544) são **artefato escrito de Max**,
não fala. Carregam a bio assinada (L3419, L9269: "I'm Max. I'm the founder of
Well Copy") e reivindicações em 1ª pessoa: L5475/L6774 "I've created the Email
Marketing Brain", L1208 "Use my checklist", L8311 "My Best Tip For Design",
L9522 "30 of my favorite SMS messages", L358 "with my link below".

**Ressalva importante:** os decks também dizem "our copywriters" (L6790) e
"message our team" (L8692). Isso é decisivo para o §5.

---

# 4. As evidências fortes

## 4.1 A prova de terceira pessoa — L5753, e por que ela é mais forte do que parece

O narrador de **ChatGPT Copywriting (L5617–5866)** está percorrendo o deck de
copywriting ao vivo. Ele diz, em L5761:

> "I could have just followed the prompts on it, but I just copy and pasted
> **from the presentation** into here."

Isto é, ele lê a apresentação. Quando chega ao slide **L6772–6777**, cujo título
é `## Use My AI To Help Write Copy` e cujo corpo é `Lucky for you, I've created
the Email Marketing Brain…`, ele o traduz em voz alta como:

> **L5753** — "So we have a email marketing brain, something that **Max had put
> together himself**."

Não é uma menção solta a um terceiro. É a **conversão de um "eu" escrito num
"Max… himself" falado**, no momento exato em que o narrador lê o texto do autor.
Quem escreveu "I've created" e quem disse "Max had put together himself" não são
a mesma pessoa.

A triangulação sobre o **mesmo artefato** fecha o caso:

| Linha | Bloco | Formulação | Pessoa |
|---|---|---|---|
| L5475 | slide GAMMA CAMPAIGNS | "Lucky for you, **I've created** the Email Marketing Brain" | 1ª |
| L6774 | slide GAMMA COPY | idem, verbatim | 1ª |
| L5212 | Text Based Masterclass (YT) | "you can get access to **my custom GPT** right here called the email marketing brain" | 1ª |
| L6387 | MrBeast (YT) | "**I actually made this** with over 500 docs of email marketing trainings" | 1ª |
| **L5753** | **ChatGPT Copywriting** | **"something that Max had put together himself"** | **3ª** |

Quatro reivindicações em primeira pessoa contra uma atribuição em terceira. A
exceção é o bloco L5617–5866.

**Ressalva honesta:** L5753 é ASR. Não se pode excluir por completo uma alucinação
de nome próprio. Mas a frase é gramatical, o pronome reflexivo concorda com o
nome ("Max … himself"), e o bloco é independentemente o que mais se afasta do
idioleto de Max em todo o arquivo. A ressalva não muda a classificação; muda o
tom da nota que dela derivar.

## 4.2 A prova de primeira pessoa mais limpa — L631

Em **AULA 3 de List Growth (L605–678)**, discutindo desconto percentual versus
desconto em valor:

> **L631** — "What do you think sounds better? 10% off or $20 off? **If you ask
> me, Hey Max, do you want 10% off?** I'd be like, maybe. But if you went up to
> me and said, **Hey Max, $20 off, here's a $20 bill.** I'd be like, fuck yeah."

O falante encena um diálogo em que ele é o interlocutor, e o interlocutor é
chamado de Max. Duas vezes, com "me" ligando as duas metades. É a
auto-identificação nominal mais direta do arquivo.

O mesmo bloco fecha (L677) anunciando os dois seguintes como próprios —
"physically step-by-step **how I'm creating these** inside of Klaviyo, and then
all the pop-up form creation **I'm going to be providing** that for you as well
in a separate video" —, o que carrega os blocos #10 e #11.

## 4.3 O link de afiliado como assinatura — L34, L8044, L8046

O deck declara o link em L358: `omnisend.com/max` — "30% OFF first 3 months
**with my link** below". Dois blocos falados reivindicam esse mesmo link em
primeira pessoa:

- **L34** (AULA 3 de fundamentos): "you get 30% off your first 3 months **if you
  use my link** below right here, which is uh **omnisend.com/max**."
- **L8044** (Uploading Designs, YT): "You get a 30%, uh, discount **if you use
  me**." Seguido, em **L8046**, de: "I'll say **well copy** because that's **my
  company's name**."

Well Copy é a agência de que Max é fundador (L3419). Quem chama Well Copy de "my
company" e o link `/max` de "my link" é Max.

## 4.4 A comunidade, os designers e o canal — L6279, L6458, L6499

Nos dois vídeos longos de YouTube do módulo de copy, o narrador exerce papéis
que só o dono exerce:

- **L6279** — "**Community we have over 450 people**, he sent this in of an
  email he did himself and I absolutely love this, **shout out to you Dominic**."
  (A comunidade é `skool.com/email-marketerz`, L3465.)
- **L6458** — "I'd be lying if I said I didn't consult with **one of my
  designers** on hand to put this together… **Shout out Diana**."
- **L6350** — "the exact process that we use at **my agency** which has generated
  $40 million for clients."
- **L6499** — "Make sure to check out this video on **my channel**."

Os dois terceiros nomeados do arquivo — **Dominic** (membro da comunidade) e
**Diana** (designer da agência) — aparecem exatamente aqui, e ambos como
subordinados/membros, nunca como autoridade. Nenhum bloco do arquivo trata Max
como subordinado a alguém.

## 4.5 O separador de si e do grupo — L2616

**Browse Abandon Flow** fecha com:

> "you're going to have to hit up klaviyo support, feel free to **message me or
> the group** as well and we'll get you a fix."

O narrador se põe ao lado do grupo, não dentro dele. É `max-provavel`, não
`provado` — um funcionário sênior poderia dizer o mesmo —, mas alinha com todo o
resto do módulo de flows.

---

# 5. Evidência contrária encontrada — a hipótese da assinatura **caiu**

Isto era o que se pediu para procurar. Foi encontrado, e derruba dois critérios.

## 5.1 A assinatura de abertura é inútil — L7603 + L7817

**Figma Email Design Walkthrough (L7590–7840)** abre em **L7603** com:

> "**Hello, hello.** So in this video, I just wanted to give you just a brief
> look around as to Figma…"

Ou seja: a saudação atribuída ao "outro narrador". E em **L7817–7818**, o mesmo
narrador demonstra o recurso de comentários do Figma digitando uma menção a si
mesmo:

> "You could be, '**Hey, at max, this is terrible.**' **Let me just make sure it
> actually tags me** so I know that this is terrible."

Ele escreve `@max` e diz "**tags me**". O narrador é Max. **Um vídeo que abre com
"Hello, hello" é comprovadamente Max.**

Consequência: `"Hello, hello"`, `"Yo, yo"`, `"What up, what up"` e `"Alrighty"`
**não são critério de autoria**. Qualquer nota que classifique um trecho pela
saudação está classificando por nada. Confirmação secundária: L7590–7840 tem
"boom" 8× — bordão do aglomerado A — e zero "at the end of the day", zero
"obviously", zero "you guys".

Repare no que isso significa metodologicamente: DE-Figma é **neutro em todos os
cinco marcadores de idioleto** (zero em ambas as direções). Só a evidência
nomeada o resolveu. Onde não há nome, não há certeza — é por isso que 20 blocos
ficam em `provavel` e não sobem.

## 5.2 O pronome coletivo é inútil — L6790, L8692, L6285+L6350

A hipótese dizia que "our copywriters", "our team" e "hit us up" marcariam o
outro narrador. Três achados derrubam isso:

1. **L6790**, dentro do deck GAMMA COPY — o mesmo deck que em L6774 diz "**I've
   created** the Email Marketing Brain" — afirma: "Instead, **our copywriters**
   act as 'Email Architects'." O artefato escrito de Max usa o pronome coletivo.
2. **L8692**, no deck GAMMA DELIVERABILITY: "Feel free to **message our team**
   as well if you have issues with this."
3. **L6285 e L6350 estão no mesmo vídeo.** Em Gymshark (YT), o narrador diz "the
   winning layout that we do for a lot of our emails **for our clients**" (L6285)
   e, 65 linhas depois, "**my agency** which has generated $40 million" (L6350).
   O mesmo falante alterna entre "our clients" e "my agency" em 46 minutos.

Um dono de agência dizendo "our team" não é evidência de coisa nenhuma — a
suspeita levantada na tarefa estava correta e se confirma. Os pronomes coletivos
saem do conjunto de critérios.

## 5.3 O que restou de pé

A hipótese **de que há dois narradores** continua de pé: L5753 a prova. O que
caiu foram os **critérios propostos para separá-los**. O critério que os separa é
a ausência de enunciados de preferência pessoal ("I recommend", "my favorite",
"I like to") combinada com a presença de "at the end of the day" e "obviously" —
e, como corroboração, o fecho coletivo "thank you guys … see you in the next
one", que não ocorre uma única vez fora do aglomerado B.

Registre-se ainda: o aglomerado B coincide exatamente com quatro módulos inteiros
(Campaigns, Copywriting exceto os dois YouTube, Deliverability, Optimization) e
não é fatiado por gênero de vídeo — o walkthrough de tela DE-Figma e o walkthrough
de tela LG-A4 são ambos do aglomerado A. Não é efeito de formato. É pessoa.

---

# 6. Consequência prática por pasta

Faixas não-Max, para a correção posterior:

- **`outro-provado`** — L5617–5866
- **`outro-provavel`** — L4189–5154, L5867–6248, L8365–8646, L8762–9109

Total: **2.462 linhas de fala**, ~25.141 palavras — cerca de 26% de toda a fala do
corpus. As faixas de slide correspondentes (L5237–5599, L6501–6858, L8647–8759,
L9110–9212) **não** estão em causa: são artefato escrito de Max.

## 6.1 Notas afetadas, por pasta

**`deliverability/` — 9 de 9 notas. A pasta inteira.**
`auditoria-glockapps` (L8508) · `metricas-alvo` (L8430) · `o-que-e` (L8382) ·
`reparo-de-reputacao` (L8589) · `setup-tecnico` (L8396) ·
`so-envie-para-engajados` (L8456) · `upload-para-deliverability` (L8492) ·
`warming-casos-reais` (L8607) · `warming-do-dominio` (L8518, L8522).
Toda a fala do módulo (L8365–8646) é `outro-provavel`. O que sobra de Max é o
deck L8647–8759 — que é curto (113 linhas) e que também diz "our team" (L8692).

**`otimizacao/` — 7 de 7 notas. A pasta inteira.**
`categorias-vs-produtos` (L8890) · `flow-time-delays` (L8946) ·
`grafico-vs-texto` (L8862) · `outros-testes` (L8972) · `quando-vale-testar`
(L8774, L9096) · `send-time` (L8828) · `testar-subject-line-por-receita` (L8918).
Agravante já registrado em `_fontes`: o deck de Optimization (L9110–9212) é cópia
quase verbatim do deck de Flows. Ou seja, a pasta é fala não-Max mais um deck
duplicado.

**`campanhas/` — 8 de 9 notas.**
`cem-ideias-de-email` (L4516) · `frequencia-de-envio` (L4220, L4238, L4404,
L4191) · `mix-grafico-e-texto` (L4298) · `montar-o-calendario` (L4441, L4424) ·
`nao-hipersegmentar` (L4993, L5135) · `ocupar-espaco-mental` (L4244, L4194) ·
`os-cinco-pilares-de-conteudo` (L4372, L4426, L4472, L4538) · `segmentacao`
(L4844, L4829). Escapa apenas `email-de-texto-puro`, que vem de L5155–5235
(`max-provado`).

**`copy/` — 6 de 9 notas.**
`email-architect` (L5725, L5803) · `infograficos` (L5886, L5867) ·
`preview-texts` (L6171, L6090) · `principio-skimmable` (L5889) · `prompt-de-copy`
(L5627, L5667) · `subject-lines` (L6099, L6083). Escapam `o-que-evitar`,
`principio-clear-e-conciso` e `principio-engaging`, que saem do deck.
Caso particular: **`email-architect`** deriva de L5803, que é o narrador de
L5617–5866 lendo o slide L6790 — o conceito é de Max (está no deck), a
formulação falada não é dele.

**`doutrina/` — 8 de 13 notas.**
`a-ia-e-um-copywriter-junior` (L5667) · `desconto-constante-barateia-a-marca`
(L4372, L4191) · `disruptor-vence-no-inbox` (L6191, L6103) ·
`o-basico-entrega-90-por-cento` (L8778, L9098, L8764) ·
`o-numero-decide-nao-a-opiniao` (L6227, L8792) ·
`otimize-para-a-varredura-nao-para-a-leitura` (L4703) ·
`sce-o-framework-que-atravessa-tudo` (L4703, L4819) ·
`texto-puro-funciona-porque-e-raro` (L4326).
Esta é a pasta mais sensível: doutrina é exatamente o registro que o advisor
parafraseia na voz dele. `a-ia-e-um-copywriter-junior` sai de L5667 — o bloco
`outro-provado`.

**`flows/` — 1 de 12 notas.** Só `winback` (L5057, dentro de Segmentation).
O resto do módulo é `max-provavel` sem contraevidência.

**`design/`, `fundamentos/`, `list-growth/`, `sms/` — 0 notas afetadas.**
As quatro pastas estão inteiramente em faixa Max, e cada uma tem ao menos um
bloco `max-provado` como âncora (L7817/L8044 · L34 · L631/L1014 · L9258).

## 6.2 O número que muda de dono

Consequência concreta e imediata para `_numeros` e `_conflitos`: **a frequência
de campanhas**. As formulações faladas estão quase todas em faixa não-Max:

| Linha | Bloco | Classificação | Verbatim |
|---|---|---|---|
| L4220 | Campaign Strategy | `outro-provavel` | "two to four campaigns per week is generally going to be the sweet spot" |
| L4268 | Campaign Strategy | `outro-provavel` | "three to four emails a week" |
| L8557 | Warming Your Domain | `outro-provavel` | "ideally 3 to 4 times per week" |
| L8788 | High Leverage A/B Tests | `outro-provavel` | "three to four campaigns a week" |
| L2367 | Site Abandon Flow | `max-provavel` | "three to four campaigns per week from you" |
| **L5255** | **slide GAMMA CAMPAIGNS** | **Max (escrito)** | **"3x per week is typically the sweet spot"** |

A regra sobrevive — o slide de Max diz 3×/semana e L2367 corrobora —, mas o
"two to four … sweet spot" de L4220 deixa de ser citável como fala dele. Vale a
regra do `_protocolo`: quando os registros discordam sobre especificação, vale o
slide.

Não afetados, para tranquilidade: o piso de emails do welcome flow (L1440
"four to five", L1520 "three to four") está em `max-provavel`, e o alvo de 40%
de atribuição de receita (L170) também.

---

# 7. O que continua indeterminado

1. **Quem é o segundo narrador.** O laudo prova que L5617–5866 não é Max. Não
   prova quem é. O arquivo nunca o nomeia; ele nunca se apresenta; nenhum bloco
   diz "meu nome é X". Provavelmente alguém da Well Copy — L4224 mostra que tem
   acesso à conta Klaviyo da agência ("This is just a dummy account for WellCopy.
   Do some things in here for our team"), e L5801/L6019/L8798 falam de "our
   copywriters"/"our team" de dentro. Mas é inferência, não prova.

2. **Se o aglomerado B é uma pessoa ou mais de uma.** Os dez blocos são
   estilometricamente homogêneos e os quatro módulos são contíguos, mas nada
   exclui dois colaboradores com hábitos parecidos. Nenhum teste feito aqui
   separa B em sub-grupos.

3. **Os nove blocos `outro-provavel` não estão provados.** A base é
   estilométrica, não nominal. A probabilidade de acaso é baixíssima (§2.1), mas
   o padrão de prova deste laudo reserva `provado` para auto-identificação, e
   nenhum deles a tem — nem a favor, nem contra. Se aparecer, num desses nove,
   uma linha do tipo de L7817, o bloco sobe para `max-provado` e o aglomerado
   inteiro precisa ser reavaliado. Foi exatamente isso que aconteceu com
   DE-Figma.

4. **Os vinte blocos `max-provavel`.** Mesma ressalva na direção oposta. Onze
   deles não têm nenhum marcador em nenhuma direção porque são curtos demais
   (INTRO-A2, A5, A6, LG-A1, LG-A2, FL-Replenishment, FL-Winback,
   DE-Importance). Em bloco curto, ausência de marcador não é sinal.

5. **Se o narrador B escreveu algum slide.** Os decks trazem a bio de Max e
   reivindicações em 1ª pessoa dele, mas também "our copywriters" (L6790) e "our
   team" (L8692). Não há como distinguir "Max escreveu usando 'nós'" de "a
   equipe escreveu e Max assinou". Para efeito prático não muda nada — o deck é
   artefato oficial dele em qualquer dos dois casos —, mas convém não citar um
   slide como "ele disse".

6. **L5753 e o ASR.** Ver a ressalva em §4.1. É a única linha do arquivo que
   sustenta uma classificação `outro-provado`, e ela vem de transcrição
   automática. Se alguém recuperar o áudio original e a frase for outra, este
   laudo inteiro precisa ser refeito — porque sem L5753 não sobra prova nominal
   de segundo narrador, só estilometria.

---

## Como aplicar

Toda nota cujo `fonte:` caia em L4189–5154, L5617–6248, L8365–8646 ou
L8762–9109 recebe `registro: outro-narrador` na parte derivada da transcrição, e
a afirmação deixa de ser citável como fala de Max — conforme a regra 6 do
[[_protocolo]]. As partes derivadas de slide, na mesma nota, permanecem.

Nenhuma outra nota foi alterada por esta unidade. Este arquivo é o laudo; a
aplicação é trabalho separado.
