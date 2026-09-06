---
tipo: procedimento
modulo: deliverability
assunto: warming-do-dominio
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L8518-8645 (transcrição); L8522-8526 (bullets do deck). O corpo do deck de warming NÃO foi exportado."
conflitos: [deliverability-limiar-de-open-rate, deliverability-passo-de-escalonamento, deliverability-primeiro-degrau-da-rampa]
validade: "procedimento — o corpus não data a gravação. Extraído em 2026-09-06."
status: rascunho
---

> **Lacuna estrutural desta nota.** O deck citado no vídeo — "Email Warming
> Deliverability Deep Dive", `https://gamma.app/docs/Email-Warming-Deliverability-Deep-Dive-ex6p9skikw53x06`
> (L8520) — **nunca foi exportado**. A seção GAMMA (L8647-8759) cobre só o deck
> de deliverability e vai direto de "Check Your Deliverability With Glockapps"
> (L8752) para `# OPTIMIZATION` (L8760). O único registro de slide sobreviveu
> como cinco bullets de resumo (L8522-8526). Todo o resto — rampa, cronograma,
> batching, casos — existe **apenas na transcrição falada**. É a única parte
> crítica do corpus sem segundo registro para conferir número.

# Quando se aplica

Bullets do deck, verbatim (L8522-8526):

> * **This if for you if:**
>   * You have sent no emails before from your Klaviyo account AND Your
>     technical setup / branded sending domain is set up
>   * OR, your deliverability is poor. This same method can be used to improve
>     it (with a few tweaks)
> * **Technical Setup: [Setting up branded sending domain >>>](https://help.klaviyo.com/hc/en-us/articles/115000357752)**
>   * If this isn't done, do this before sending ANY emails

Dois casos, portanto: conta nova **ou** deliverability ruim — "This same method
can be used to improve it (with a few tweaks)" (L8524). Os *tweaks* nunca são
enumerados como lista; o que existe é [[reparo-de-reputacao]]. O setup técnico é
pré-condição, não etapa: ver [[setup-tecnico]].

O que se está prevenindo (L8533-8534): abrir conta no Klaviyo, importar a lista
de clientes e leads e disparar para todo mundo — "nobody opens them, no one
engages, you get super low rates, and then basically everything going forward
ends up going to spam". O custo do erro (L8555, L8606): "it's much easier to
build your sender reputation and deliverability warming up than it is to fix it
when it's already in a poor position."

A imagem que ele usa (L8541): "it's like building a house. You have to establish
the infrastructure through warming before you get really creative."

# A fundação, antes de qualquer campanha

Duas coisas ligadas antes de começar a rampa.

**1. Flows de alta intenção rodando** (L8545): "Welcome Flow, Post-Purchase,
Abandoned Card [*Cart*], Abandoned Checkout, Browse, Site Abandonment, I'll list
the other ones" — ele não lista as outras. Racional (L8549-8551): são pessoas em
estágios diferentes da jornada, "these are points where we obviously want to
target people", e ficam rodando evergreen.

**2. Pop-up convertendo** (L8546): "no matter what, if it's a new account or
whenever, you want to make sure your pop-up form is converting."

E dentro do pop-up, uma regra explícita de onde **não** colocar o código
(L8548):

> it's important to not put that discount code or whatever, if there is a code.
> In the form itself, you want to strategically place that in welcome email 1,
> 2, 3, 4, so that people are prompted and conditioned from the beginning to
> expect value coming from their emails and they're forced to open and click
> that link.

O objetivo é warming, não conversão: o desconto vira o isco que garante open e
click nos primeiros quatro emails.

# De onde tirar o primeiro público

Depende do dado que existe. "It's not always going to be the same solution or
the same exact segment" (L8553).

**Com dado de email** — migração de MailChimp ou OmniSend, ou conta antiga com
deliverability ruim (L8563). "You always want to stick with your email data."
Os quatro segmentos-semente citados (L8564), verbatim:

> people who have opened three times in the last thirty days, people who have
> opened five times in the last sixty days, people that have opened an email
> once or twice in the last week, people that have clicked an email in the last
> week

Ressalva dele (L8565-8567): não existe solução única — o segmento que ele
sugerir pode estar vazio, ou ter "seventy-eight people in there, which isn't
really going to move the needle".

**Sem dado de email** — dado comportamental do Shopify, que integra com o
Klaviyo (L8571). "It's also one that you have to be a little bit careful about"
(L8572). Os três sinais citados (L8574), verbatim:

> people that have viewed a product in the last three days, placed an order in
> the last week, and started checkout in the last week

E a migração de volta assim que houver dado de email (L8576): "the best
indicator of future behavior is past performance."

# A rampa

**Primeiro envio** (L8569): "I always err on the side of caution, maybe a
hundred people, two hundred people, three hundred people, somewhere in that
range."

**Passo de escalonamento** — CONFLITO. A fala diz "you scale up by about fifty
to, by about fifty percent each send, as long as you're still getting the
metrics that you want" (L8569). O bullet do deck, lido em voz alta, diz
"gradually increase from 25 to 50 percent percent based on performance" (L8556
— o "percent percent" é gagueira de ASR, o número não). Ver
`deliverability-passo-de-escalonamento` em [[_conflitos]].

**Cadência de rampa**, verbatim (L8587-8588):

> a sample ramp up cadence would look like on the first end, you're sending to
> one to 200,000. Then on send two, going to maybe like 300, so some of the
> people in the first, and then adding on to it, and then send three, 500, send
> four, a thousand, send five, 2,000, then 4,000, then 6,000, 6,000, and you can
> continue scaling this up as long as you're hitting those, those 40 to 50% open
> rates

> **O primeiro degrau está corrompido.** "one to 200,000" é incoerente com os
> degraus seguintes (300 → 500 → 1.000 → 2.000) e com o próprio primeiro envio
> de 100-300 pessoas em L8569. O número real do degrau 1 não é recuperável do
> corpus. Nunca reproduzir "200.000" como primeiro envio.

Note que o degrau 2 não é público novo: "so some of the people in the first, and
then adding on to it" (L8588) — a amostra acumula.

**Frequência durante o warming** (L8557): "ideally 3 to 4 times per week". O
racional é volume de dado para o provedor avaliar (L8559): "They need a certain
amount of data to make those assessments. So, the more data that you're giving
them, the more that they have to work with and you will speed this process up."
E o custo de ir devagar (L8561):

> if you only send 2 times per week opposed to 4 times per week, then it's going
> to theoretically take twice as long to get the amount of data and the opens
> and the clicks and all the metrics that they're looking for

Com teto: "that doesn't mean send [—] emails in 7 days, because at a certain
point, you hit a point of diminishing returns and you actually end up hurting
yourself" (L8560). **O número desse teto se perdeu no ASR.**

**Batching intradiário** (L8584-8586): em vez de disparar tudo de uma vez,
espalhar pelo dia.

> let's say you're sending to 6,000 people. Instead of saying you want to send
> 6,000 at noon, you can send a thousand at noon, a thousand at one, two, a
> thousand at three, four, five, six, all the way through the day and batch it
> throughout the day. Cause that's something that Google or Yahoo, whoever it
> might be, won't necessarily see those spikes, but they will see it more
> actively, consistently.

# O cronograma por semanas

**Semanas 1 a 3 — fundação** (L8578-8579): criar e dimensionar os segmentos de
7, 14, 30, 60 e 90 dias; "Activate all the base forms"; enviar para uma das
listas engajadas e monitorar open rate.

**Semanas 3 a 12 — expansão progressiva** (L8580-8583): semanas 3-4 no 14 dias,
depois 30 dias; "Same logic from 30 to 60. Are we still hitting the numbers we
want? Cool. Then we can expand to the 60 day and then maybe after a couple
weeks, you expand to the 90 day."

O objetivo final da rampa (L8556, L8600): destravar os segmentos base — "so you
have your 30, 60, 90 day engaged audiences established. Then you have the
opportunity to get more creative."

**A regra de ouro**, verbatim (L8579-8580):

> the golden rule is, you want to get ideally 50 plus open rates and then you
> know you're good to jump to a wider segment. But anywhere between 40 to 50
> percent. If it starts dipping below 40, I definitely wouldn't be expanding it.

Nunca alargar abaixo de 40%. Esse é o único ponto em que os cinco valores
concordam.

# CONFLITO: o limiar para alargar tem cinco valores

Nenhum é marcado como superior. Todos, verbatim:

| Valor | Contexto | Linha |
|---|---|---|
| "above 50%. 50% to 70% is ideal (…) above 40%, you're probably okay" | métricas gerais | L8436 |
| "ideally 50 plus open rates and then you know you're good to jump to a wider segment" | regra de ouro | L8579 |
| "anywhere between 40 to 50 percent. If it starts dipping below 40, I definitely wouldn't be expanding it" | tolerância | L8580 |
| "you're hitting, again, 45 to 50% plus and then it's like, okay, that's a good indicator that we can expand" | 14 → 30 dias | L8582 |
| "as long as you're hitting those, those 40 to 50% open rates" | cadência de rampa | L8588 |
| "If you start to get 60%+ opens, widen your list" | **slide** de deliverability | L8728 |

O slide é o mais exigente (60%+) e é o único registro de slide que existe sobre
o assunto — mas ele está no deck de deliverability, não no de warming, que não
foi exportado. Ver `deliverability-limiar-de-open-rate` em [[_conflitos]].

# Correção de rota

Quando a abertura despenca depois de alargar (L8601-8604):

> if you go from your 30 day engage list to your 60 day engage list and your
> open rates go from 50% to 25%. That's a good indicator of, Hey, we got to pull
> this back (…) we clearly made too big of a jump. We need to pull this back,
> make sure we're consistent, and then we can try it again later. Or maybe we
> still expand, but we don't expand it quite as big. Maybe instead of going from
> 30 to 60, we go from 30 to 45 day engage. And that keeps us at a 40 to 50%
> mark.

Duas saídas, portanto: voltar e esperar, **ou** repetir o salto com passo menor
(30 → 45 em vez de 30 → 60). Ele não dá critério para escolher entre as duas.

# Os dois casos reais

Em [[warming-casos-reais]], com os volumes verbatim. Em uma linha cada:

- **Migração de MailChimp** (L8607-8622) — havia dado de email fora do Klaviyo,
  mas trataram como conta nova: **amostra aleatória** dentro do 30 dias
  engajados, começando com 1.000 pessoas e 46.22% de abertura. "Even if you have
  that data, it's still different platform (…) you always end up somewhat
  starting from scratch" (L8612-8613).
- **Zero dado, pré-lançamento** (L8623-8639) — só waitlist e lista de marca
  irmã. Emails de warming **todos text-based**, lotes pequenos, primeiro envio
  ~200 pessoas. Contém a autocrítica dele: "we actually weren't even including
  any CTAs, which was a bad idea on our end" (L8635).

# A ferramenta que nunca é nomeada

No fim do vídeo ele recomenda uma ferramenta de terceiros para quem cai em
promotions — e **o nome dela não está no corpus**. O trecho (L8641-8643):

> If your emails are landing in spam, don't use this, but if your emails are
> landing in promotions very heavily, this is a great tool that runs in the
> backend and optimizes all that HTML and things to make sure that you are
> landing in the primary inbox (…) they are a very, very good tool to work with
> a lot of very well-known brands as well.

Escopo declarado: serve para **promotions**, não serve para spam nem para
warming (L8643). A transcrição pula de 21:52 (L8641) para 22:33 (L8642) — cerca
de 41 segundos ausentes, exatamente onde a apresentação da ferramenta estaria. É
irrecuperável. Nunca preencher esse nome por dedução.

# O que o corpus não diz

- O corpo do deck de warming (ver o aviso no topo).
- Quantos emails por semana é "demais" — o teto de diminishing returns perdeu o
  número (L8560).
- Quais são os "few tweaks" que adaptam o método para conta com deliverability
  ruim (L8524).
- Que porcentagem de queda de open rate obriga a recuar. O exemplo é 50% → 25%
  (L8601), não é regra.
- O nome da ferramenta de otimização de HTML (L8641-8643).
- Quanto tempo o warming inteiro leva. Há "weeks 1 to 3" e "weeks 3 to 12"
  (L8578-8580) e uma "60 day window" num caso (L8611) — não são a mesma unidade.
