---
tipo: indice
assunto: casos-de-teste
autor: max-sturtevant
status: aprovado
---

Casos de regressão do advisor Max para afirmações que se contradizem dentro do corpus: conflito entre módulos diferentes e conflito dentro de um mesmo registro. A resposta certa mostra as duas versões com âncora, nunca a média nem a escolha silenciosa. Quatro casos (C-15 a C-18), cada um com pergunta, resposta esperada, erro típico e diagnóstico.

# Casos de conflito — C-15 a C-18


## C-15 · Conflito entre módulos — HTML contra imagem

**Pergunta:** Preciso ter seções de texto em HTML no email ou posso fazer tudo
em imagem?

**Resposta certa contém:** as duas versões, **com donos diferentes**, e a ponte.

Lado design, fala de Max (bloco L8009-8065, `max-provado`): `"There's some rumor
in the space, someone started it like 8 years ago (…) that you need to have like
HTML sections in your email. You need to have native text sections and whatnot.
But that couldn't be farther from the truth."` (L8026), com a prova oferecida em
tela — `"Look at how little HTML there is in this email (…) don't think that you
need to have native text native text sections"` (L8027-8028), sobre a Ridge.

Lado deliverability, **outro narrador** (L8381-8646, `outro-provavel`):
`"Google can't properly scan the image-based emails (…) Google read HTML.
Image-based emails have a lot less HTML."` (L8500);
`"However, if you at least have a base amount of HTML (…) that's where your alt
text comes into play."` (L8502); `"making sure you're including different bits of
HTML in your email will include deliverability"` (L8504 — `"will include"` é o
texto do bruto; a leitura óbvia é *improve*, mas a correção não está no corpus).

A reconciliação: são duas perguntas diferentes com a mesma palavra. Max nega que
seções de texto nativo sejam necessárias **para vender**; o outro narrador
afirma que algum HTML ajuda o Google a **ler** o email. A ponte é o alt text —
é HTML, é passo obrigatório do upload (L8052-8053, narrado por Max) e é o que
preenche o "base amount". O corpus **não quantifica** quanto é "a base amount".

**Resposta errada típica:** responder só um lado — quem entra pela pasta
`design/` diz "não precisa de HTML" e quem entra por `deliverability/` diz
"precisa" —, ou atribuir a Max a frase sobre deliverability.

**Se errar, quebrou:** [[mapa-dos-conflitos]] § "Conflitos entre módulos"
(`design-html-vs-imagem`), que existe exatamente porque o roteamento por pasta
do [[mapa-do-corpus-do-max]] entrega uma pasta só. Se atribuiu L8500-8504 a Max, quebrou também
a marcação de autoria.

## C-16 · Conflito entre módulos — o open rate de email dentro do SMS

**Pergunta:** O SMS tem 98% de abertura e o email só 30%. Não é melhor investir
em SMS?

**Resposta certa contém:** a correção da premissa. Os 30% aparecem **uma vez** no
corpus inteiro, num comparativo retórico do deck de SMS — `"SMS marketing
messages have an average open rate of 98% (email has an average open rate of
30%)"` (L9291) — cuja função é fazer o 98% parecer maior. Não é o benchmark de
email dele. O benchmark dele é acima de 50%: `"we need to be above 50%. This is
the only one where it's like, okay, if you're below 50%, you're fucking something
up"` (L178), `"Open Rates — 50%+"` (slide de fundamentos, L376),
`| Open Rates | Greater than 50% |` (slide de deliverability, L8715), e a
tolerância `"you ideally want to be in that 50 to 60% range, but anything over
40% is okay"` (L4236). Nota que a resposta deve dar: nenhuma das duas médias de
mercado (30% de email, 98% de SMS) tem fonte citada no corpus.

**Resposta errada típica:** aceitar os 30% como linha de base de email e
construir a comparação em cima disso.

**Se errar, quebrou:** [[mapa-dos-conflitos]] § "Conflitos entre módulos"
(`sms-open-rate-de-email`).

## C-17 · Conflito dentro do mesmo registro — a tabela contra o glossário

**Pergunta:** Qual é o teto de spam complaint rate que eu tenho que respeitar?

**Resposta certa contém:** **0,01%** como posição sustentada, e o 0,1% do
glossário como registro divergente — nunca como faixa. Sustentam o 0,01%: a fala
(`"we want it to be less than 0.01%"`, L192), a tabela de metas de fundamentos
(`| Spam Complaint Rates | <0.01% |`, L379) e a tabela do deck de deliverability
(`| Spam Complaint Rate | Less than 0.01% |`, L8718). Diverge: o glossário, no
**mesmo deck** de fundamentos — `"Spam Complaint Rate – (…) Target: <0.1%."`
(L438). Dez vezes mais permissivo.

O desempate, e a resposta tem que dizer por que ele existe: em L217 ele declara
que vai pular o glossário — `"So I am going to gloss over this glossary (…) You
can use these if you want"` — enquanto defendeu a tabela linha por linha na fala
(L168-194). Tabela é material que ele sustentou; glossário é material que ele
entregou. Diagnóstico associado, verbatim: `"then you have a content problem,
potentially a segmentation problem"` (L192) — a hesitação no segundo termo é
dele e fica.

**Resposta errada típica:** "entre 0,01% e 0,1%". É a média inventada mais
perigosa do corpus: é a diferença entre uma conta saudável e uma conta em risco
de bloqueio.

**Se errar, quebrou:** [[mapa-dos-conflitos]] § "Conflitos dentro do mesmo registro"
(`fundamentos-spam-glossario`) e regra 2 do [[_protocolo]]. Se a resposta
aplicou a precedência slide-vence-fala e ficou com o glossário, quebrou o
entendimento de que a precedência só vale **entre** registros.

## C-18 · Conflito dentro do mesmo registro — três números em quatro linhas

**Pergunta:** Estou com 45% de abertura. Já posso alargar minha lista de
engajados?

**Resposta certa contém:** que o corpus não reconcilia, e os dois caminhos.

Pelo slide (deck de deliverability, três números em quatro linhas):
`"This is how we can get consistent 50% open rates."` (L8725) ·
`"Whatever list gets you 50-60% opens."` (L8727) ·
`"If you start to get 60%+ opens, widen your list to a larger timeframe"`
(L8728) · `"If you start to get 40% opens, tighten your list to a smaller
timeframe."` (L8729). Pelo gatilho do slide, 45% **não** alarga.

Pela fala, a golden rule e a contradição imediata:
`"the golden rule is, you want to get ideally 50 plus open rates and then you know
you're good to jump to a wider segment"` (L8579) e, na **linha seguinte**,
`"But anywhere between 40 to 50 percent. If it starts dipping below 40, I
definitely wouldn't be expanding it."` (L8580); depois `"you're hitting, again,
45 to 50% plus and then it's like, okay, that's a good indicator that we can
expand"` (L8582). Pela fala, 45% talvez alargue.

O que **nenhuma** formulação contradiz: abaixo de 40% nunca se alarga. E o
critério que ele dá não é numérico — `"I always err on the side of caution"`
(L8569). Aqui não existe desempate: é a mesma tela dando três números, e não há
material sustentado contra material entregue. Toda a fala é `outro-provavel`.

**Resposta errada típica:** "sim, 45% já dá" ou "não, precisa de 50%", em
qualquer dos dois casos sem mostrar que o corpus diz as duas coisas. Pior
variante: "o alvo é uns 55%", que é a média dos três números do slide.

**Se errar, quebrou:** [[mapa-dos-conflitos]] § "Conflitos dentro do mesmo registro"
(`deliverability-limiar-de-open-rate`) e a seção "Quando o conflito é dentro do
mesmo registro" do [[_protocolo]], que usa este caso como exemplo-limite.

---

