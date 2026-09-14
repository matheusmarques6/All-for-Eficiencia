---
tipo: procedimento
modulo: deliverability
assunto: warming-do-dominio
autor: max-sturtevant
registro: [slide, outro-narrador]
fonte: "CONTEUDO BRUTO/max.md — L8556-8604 (transcrição); L8728 (slide do deck de deliverability). O corpo do deck de warming NÃO foi exportado."
conflitos: [deliverability-limiar-de-open-rate, deliverability-passo-de-escalonamento, deliverability-primeiro-degrau-da-rampa]
validade: "procedimento — o corpus não data a gravação. Extraído em 2026-09-06."
status: aprovado
---

A rampa de warming do domínio é o escalonamento de volume que aquece o domínio
de envio: primeiro envio, passo de escalonamento, cadência, batching, cronograma
por semanas e o que fazer quando a abertura despenca depois de alargar a lista.
Registra também que o limiar de open rate para alargar tem **seis valores em
conflito** no corpus. O que precede a rampa está em
[[preparacao-para-o-warming-do-dominio]].

# Aviso de autoria

**Faixa L8381-8646 (toda a fala do módulo de deliverability) — `outro-provavel`.**
Sem prova nominal. A classificação é **estilométrica**: o bloco pertence ao aglomerado
do único bloco `outro-provado` e não traz um só marcador do idioleto de Max.
`outro-provavel` não é `outro-provado` — não está provado que a voz não é dele, está
estabelecido que é muito improvável ([[mapa-da-autoria]] §7.3).

Critério: **idioleto** ([[mapa-da-autoria]] §2.1) — ausência de "I recommend", "my favorite"
e "I like to", presença de "at the end of the day" e "obviously", e o fecho coletivo
"thank you guys… see you in the next one". **A saudação de abertura não é critério e
não pode ser citada como evidência:** o laudo testou e ela caiu — o walkthrough de
Figma abre com "Hello, hello" e é comprovadamente Max, que em L7817 digita `@max` e
diz "tags me" ([[mapa-da-autoria]] §5).

Nesta nota a exposição é quase total. Os cinco bullets do deck (L8522-8526) e o
limiar de 60%+ do deck de deliverability (L8728) são **slide** — artefato de Max.
Todo o resto — fundação, segmentos-semente, rampa, passo de escalonamento,
cadência, batching, cronograma por semanas, regra de ouro e correção de rota —
está em L8532-8646, faixa não-Max, e **não é citável como fala dele**. Como o deck
de warming nunca foi exportado, este procedimento fica sem nenhum registro de Max
que o confirme: é a peça do corpus com menor lastro de autoria.

> **Lacuna estrutural desta nota.** O deck citado no vídeo — "Email Warming
> Deliverability Deep Dive", `https://gamma.app/docs/Email-Warming-Deliverability-Deep-Dive-ex6p9skikw53x06`
> (L8520) — **nunca foi exportado**. A seção GAMMA (L8647-8759) cobre só o deck
> de deliverability e vai direto de "Check Your Deliverability With Glockapps"
> (L8752) para `# OPTIMIZATION` (L8760). O único registro de slide sobreviveu
> como cinco bullets de resumo (L8522-8526). Todo o resto — rampa, cronograma,
> batching, casos — existe **apenas na transcrição falada**. É a única parte
> crítica do corpus sem segundo registro para conferir número.

# A rampa

**Primeiro envio** (L8569), na voz do material: "I always err on the side of caution, maybe a
hundred people, two hundred people, three hundred people, somewhere in that
range." É o único volume de degrau 1 que o corpus entrega íntegro — o da
cadência (L8587) está corrompido, ver abaixo.

**Passo de escalonamento** — CONFLITO, e o mais caro de errar aqui depois do
degrau 1. Em 05:30 a fala dá "gradually increase from 25 to 50 percent percent
based on performance" (L8556 — o "percent percent" é gagueira de ASR, o número
não). Em 08:08 dá "you scale up by about fifty to, by about fifty percent
each send, as long as you're still getting the metrics that you want"
(L8569-8570). **Os dois são transcrição** — o deck de warming não foi exportado,
então não há registro de slide para desempatar, e não se deve tratar L8556 como
bullet do deck só porque soa como um. Como o passo é aplicado a cada envio, a
diferença entre 25% e 50% **compõe** — as duas rampas divergem a cada degrau, não
ficam paralelas. Dar os dois números e não escolher. Ver
`deliverability-passo-de-escalonamento` em [[mapa-dos-conflitos]].

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

O objetivo final da rampa (L8556-8557, e de novo em L8600): destravar os
segmentos base — "so you have your 30, 60, 90 day engaged audiences established.
Then you have the opportunity to get more creative."

**A regra de ouro**, verbatim (L8579-8580):

> the golden rule is, you want to get ideally 50 plus open rates and then you
> know you're good to jump to a wider segment. But anywhere between 40 to 50
> percent. If it starts dipping below 40, I definitely wouldn't be expanding it.

Nunca alargar abaixo de 40%. É o único ponto que nenhuma das formulações
contradiz.

# CONFLITO: o limiar para alargar tem seis valores

Seis aqui — o conflito completo, com as dez formulações que o corpus dá para
"qual lista usar / quando alargar", está em `deliverability-limiar-de-open-rate`
([[mapa-dos-conflitos]]). Nenhuma é marcada como superior. As seis que tratam
especificamente de **alargar**, verbatim:

| Valor | Contexto | Linha |
|---|---|---|
| "above 50%. 50% to 70% is ideal (…) above 40%, you're probably okay" | métricas gerais | L8436 |
| "ideally 50 plus open rates and then you know you're good to jump to a wider segment" | regra de ouro | L8579 |
| "anywhere between 40 to 50 percent. If it starts dipping below 40, I definitely wouldn't be expanding it" | tolerância | L8580 |
| "you're hitting, again, 45 to 50% plus and then it's like, okay, that's a good indicator that we can expand" | 14 → 30 dias | L8582 |
| "as long as you're hitting those, those 40 to 50% open rates" | cadência de rampa | L8588 |
| "If you start to get 60%+ opens, widen your list" | **slide** de deliverability | L8728 |

O slide é o mais exigente (60%+), mas não desempata: ele está no deck de
deliverability — não no de warming, que não foi exportado — e discorda de si
mesmo, porque duas e três linhas antes já disse "consistent 50% open rates"
(L8725) e "Whatever list gets you 50-60% opens" (L8727). Ver
`deliverability-limiar-de-open-rate` em [[mapa-dos-conflitos]].

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
(30 → 45 em vez de 30 → 60). O material não dá critério para escolher entre as
duas.

# Continua em

A preparação que antecede a rampa — quando o método se aplica, fundação e
segmentos-semente — está em [[preparacao-para-o-warming-do-dominio]]. Os dois
casos reais, a ferramenta nunca nomeada e as lacunas declaradas estão em
[[evidencia-e-lacunas-do-warming-do-dominio]].
