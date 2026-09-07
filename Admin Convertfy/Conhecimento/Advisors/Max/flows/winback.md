---
tipo: especificacao
modulo: flows
assunto: winback-flow
autor: max-sturtevant
registro: [transcricao, slide, outro-narrador]
fonte: "CONTEUDO BRUTO/max.md — L3305-3396 (transcrição), L4040-4114 (slide); definição do segmento em L5057 e L5589"
conflitos: [winback-cadencia, winback-definicao-do-segmento]
status: aprovado
---


# Aviso de autoria

**Exposição pontual: L5057, dentro de Segmentation (L4846-5154) — `outro-provavel`.**
Sem prova nominal. A classificação é **estilométrica**: o bloco pertence ao aglomerado
do único bloco `outro-provado` e não traz um só marcador do idioleto de Max.
`outro-provavel` não é `outro-provado` — não está provado que a voz não é dele, está
estabelecido que é muito improvável ([[_autoria]] §7.3).

Critério: **idioleto** ([[_autoria]] §2.1) — ausência de "I recommend", "my favorite"
e "I like to", presença de "at the end of the day" e "obviously", e o fecho coletivo
"thank you guys… see you in the next one". **A saudação de abertura não é critério e
não pode ser citada como evidência:** o laudo testou e ela caiu — o walkthrough de
Figma abre com "Hello, hello" e é comprovadamente Max, que em L7817 digita `@max` e
diz "tags me" ([[_autoria]] §5).

O flow em si (L3305-3396) é fala de Max (`max-provavel`) e o slide (L4040-4114) é
artefato dele. **A única frase não atribuível a ele nesta nota é a corroboração
falada da definição do segmento, em L5057** — a definição que vale continua sendo
a do slide, L5589, que é de Max.

# O que é

O flow para cliente que já comprou e sumiu. Slide, L4044: "an automated email
sequence sent to past customers who haven't purchased in a while."

Por que importa, verbatim (L4047-4049):

> * Re-engages lapsed customers
> * Prevents churn and boosts retention
> * Reminds them why they loved your brand

# Gatilho, filtros e saída

| Campo | Valor |
|---|---|
| Gatilho | **entrada num segmento** — não é metric (L3314, L4053) |
| Nº de emails | 3 (L3334, L4063-4065) |
| Delay do 1º | Day 0 (L3326, L4063) |
| Delay do 2º | Day 7 (L4065) — **só no slide** |
| Delay do 3º | Day 10 (L4065) — **só no slide** |
| Filtros | *(o corpus não informa)* |
| Saída | *(o corpus não informa)* |

## O único flow disparado por segmento

"We want to trigger this off of a segment. **All the other flows, we're using an
actual trigger of some sort where it's some sort of metric connected to
Shopify.** But for this one, we want to use a segment." (L3314).

O motivo é operacional, e ele o admite como impaciência (L3316-3322): se o
gatilho fosse `placed order` + delay de 90 dias, ao ligar o flow hoje ninguém
receberia nada por 90 dias. Com segmento, "I set this flow live today,
somebody's going to receive this flow tomorrow because they bought 90 days ago."
Fecha com: "that's why we like to use a segment because I'm impatient."

## A definição do segmento

O slide anuncia "**Segment Definition for 90 Day Winback Flow:**" (L4057) e
**não entrega nada** — a linha seguinte já é o próximo heading. A definição
existe, mas fora da faixa de flows, no módulo de segmentação (L5589):

> Someone can receive email marketing because person is subscribed **AND**
> Someone has placed order at least once in the past 150 days **AND** Someone
> has placed order zero times in the last 90 days

A fala do mesmo módulo confirma — mas essa fala **não é de Max**: "people who
have placed an order in the past 150 days, but they haven't made one in the last
90" (L5057). Na aula de flows
ele dá só a metade recente: "somebody has placed an order at least once, but
they've placed an order zero times in the last 90 days" (L3318) — sem o teto de
150 dias.

**Janela de lapso**: "90, 120, 180 days are the most common ones that I do"
(L3322), repetido no slide como "(90, 120, 180 days)" (L4053). O critério de
escolha é o ciclo de recompra da marca (L3324).

# A sequência

Slide, verbatim (L4063-4065):

> **Email 1 (Day 0):** A warm "We miss you" message to reconnect and spark familiarity. The goal here is emotional—remind them of the positive experience they had with your brand.
> **Email 2 (Day 7):** If they don't respond, introduce a discount (X% off). This adds a tangible reason to return and lowers the barrier to purchase.
> **Email 3 (Day 10):** A final "Last Chance" discount to drive urgency. This is the last push before considering them inactive, so the tone should be direct and urgent.

**Email 1 — we miss you.** Templates (L4079-4082): hero sobre reabastecer
("Time to Restock Your Bar"), body lembrando que podem estar acabando, content
add-ons (receitas, social proof, engajamento de comunidade), CTA convidativo
("Get Back Into It"). Na fala ele explica a hipótese por trás dos add-ons: talvez
a pessoa não tenha voltado porque não sabe o que fazer com o produto — daí as
receitas de coquetel (L3348-3352). E a regra de hero: "I always like to have the
hero section address that it's been a while, so it's not just like a regular
campaign" (L3340-3342).

**Email 2 — o desconto.** Templates (L4094-4097): headline clara de desconto
("Take 10% Off Your Next Order"), body com o código, vitrine de reposição, CTA
de urgência. O enquadramento é de apreço, não de venda: "make the message about
appreciation" (L4089), "take 10% off just because we miss you" (L3360). O
tipo de incentivo fica em aberto: "X percent off or dollar off or gifting,
whatever it is. This is also really good to test" (L3330).

**Email 3 — last chance.** Templates (L4110-4113): headline urgente ("Last
Chance for 10% Off"), body reforçando FOMO, código com expiração, botão direto.
Text-based (L3368). Exemplo (ASR, L3374-3380): "hey Max, your cocktail game
deserves a comeback (…) don't let the fun stop. Restock right here. Use this
discount code. Ends tonight."

# O racional dele

A progressão é o produto: "this flow works because it moves from emotional
connection → financial incentive → urgency, giving you three chances to bring a
lapsed customer back before they churn completely" (L4066).

E ele coloca o flow em segundo plano deliberadamente: "keep in mind, again,
people are receiving campaigns and **most of your retention and repeat purchases
are going to come from those campaigns**, since people are receiving them three
times per week" (L3384-3386). A defesa que sobra é de contingência: "just in
case you forget to send campaigns for like two weeks" (L3392).

# Onde o corpus discorda

- **Cadência**: o slide dá Day 0 / Day 7 / Day 10 (L4063-4065). A fala dá só
  "email one, day zero" (L3326) e nenhum intervalo depois. Não é contradição, é
  omissão de um lado — mas o intervalo Day 7 → Day 10 (3 dias) é mais curto que
  Day 0 → Day 7 (7 dias), e nenhum registro explica por quê.
- **Definição do segmento**: a versão da aula de flows (L3318) tem só a
  condição de 90 dias; a do módulo de segmentação (L5589) tem também o teto de
  150 dias e a exigência de consentimento. O slide de flows promete a definição
  (L4057) e não entrega.
- **Frequência de campanha citada**: "three times per week" aqui (L3386) contra
  "three to four campaigns per week" em site abandon (L2367).

# O que o corpus não diz

- Nenhum filtro, nenhuma condição de saída **dentro do flow** — o critério de
  entrada existe e é o segmento (L3318, L5589). **Evidência da varredura:**
  `kick|exclude|exclusion|filter|zero times|skip|exit` em L1307-4186 devolve
  cinco linhas, e a única do winback é L3318, que define o segmento de entrada,
  não filtro nem saída.
- O que acontece com quem sai do segmento no meio do flow.
- O que é o "longer term win back" que ele menciona duas vezes (L3332, L3334) —
  nomeia e não especifica.
- Qual desconto usar. 10% aparece três vezes como exemplo (L3360, L4094, L4110)
  e nunca como regra.
- O slide não tem slots "**Email Example:**" neste flow.
