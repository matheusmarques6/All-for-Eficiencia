---
tipo: especificacao
modulo: flows
assunto: welcome-flow
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L1309-2324 (transcrição), L3467-3606 (slide)"
conflitos: [welcome-contagem-de-emails, welcome-cadencia, welcome-estrutura-da-sequencia, welcome-prazo-da-oferta, welcome-valor-do-desconto]
status: aprovado
---

# O que é

O flow que dispara quando alguém entra na lista. "Debatably the most important
flow" (L1316). O racional é de CAC: não dá para baixar custo de anúncio, dá para
fazer cada clique valer mais (L1320-1322) — o pop-up converte tráfego pago em
tráfego próprio, o welcome converte curiosidade em conversão (L3475). Sem isso
você perde a *trust window* e o subscriber some (L3483-3484).

Catálogo de fillers em [[welcome-fillers]]; templates em [[welcome-templates]].

# Gatilho, filtros e saída

| Campo | Valor |
|---|---|
| Gatilho | opt-in na lista |
| Metric Klaviyo | *(o corpus não nomeia)* |
| Delay do 1º email | zero — dispara imediatamente (L1420, L3492) |
| Delays seguintes | 1-2 dias (L1458, L3494) — ver conflito |
| Filtros | `placed order zero times since starting this flow` (L1542) · `bounce less than two times since starting this flow` (L1544) |
| Saída | falhar qualquer filtro: "if anybody fails to meet any of these, they'll be kicked out of the flow" (L1546) |

**O gatilho nunca é nomeado como metric — e o corpus diz por quê.** Ele descreve
("trigger after somebody opts in", L1330; "immediately after somebody signs up,
joins the email list", L1550) e não dá nome de metric, diferente de todos os
outros flows, onde dá (`Active on Site`, `Viewed Product`, `Added to Cart`,
`Started Checkout`, `Placed Order`).

Não é lacuna de extração: **o welcome não dispara por metric, dispara por
lista.** Está dito em outro módulo, na aula de segmentação (L4879-4883,
verbatim): "the most common use cases for lists is what you'll probably see in
Klaviyo already with your newsletter. So if you have a pop-up set up, someone's
in their email, phone number, and then **they go into a list. And then from that
list, they trigger a welcome flow.**" E o corpus marca a distinção explicitamente
na aula de winback: "We want to trigger this off of a **segment**. All the other
flows, we're using an actual trigger of some sort where it's some sort of
**metric**" (L3314). Ou seja, o corpus tem três formas de gatilho — metric,
lista e segmento — e o welcome é o caso de lista. Ver [[campanhas/segmentacao]] e
[[winback]]. Ressalva: L4879-4883 está na faixa `outro-provavel`; não citar como
fala de Max.

**Double opt-in desligado**, non-negotiable (L1394, L3491). O motivo: "we don't
want to give people a second chance to second guess them signing up" (L1402).
Caminho verbatim (L1412-1414) — procedimento, a tela pode ter mudado:

> go to whatever list people are joining inside of Klaviyo. Go to settings,
> list settings, consent, and then go from double opt-in to single opt-in.

# As 7 non-negotiables

Slide, verbatim (L3491-3497):

> * Turn off double opt-in
> * First email fires immediately upon sign-up
> * At least 3 emails long
> * Emails 1-2 days apart
> * Remind of welcome discount in every email
> * Include a text based email
> * Include a last chance discount email

Defesas na fala: disparo imediato porque "this is the warmest they are ever
going to be" (L1430) e porque "Give people the discount code that they signed up
for immediately" (L1426) — "The first email in the welcome flow needs to fire
automatically upon signing up" (L1420), "don't wait some bullshit 10 minutes or
wait one hour" (L1422). Lembrar o desconto em todo email porque obrigar o
cliente a procurar o código — "That's going to increase churn" (L1482). O text-based não tem gráfico e
"comes from a real person" (L1490). O last chance porque "people need urgency to
buy (…) it's just human nature, you put things off" (L1498-1504).

# A janela de 5 dias

O prazo que justifica a cadência inteira: "when somebody has a new email list,
if they don't buy within the first like five days, it's going to be very
difficult to get them to convert" (L1460).

# As sequências

O corpus dá **três** desenhos e eles não coincidem. Nenhum é marcado como
superior.

**1. "Base strategy" (fala, L1548-1586)** — 4 emails, sem conceito de filler:

| # | Conteúdo |
|---|---|
| 1 | welcome, dá o desconto, apresenta a marca, encoraja exploração (L1550) |
| 2 | lembra que o welcome offer não fica disponível para sempre (L1556) |
| 3 | "The welcome offer expires in 40 hours", lista categorias de produto, bloco de customer support (L1560-1564) |
| 4 | text-based do founder: "everything okay with order… by the way, I extended your offer" (L1572-1584) |

**2. "Template" (fala L1596-1646; slide L3511-3528)** — modular, 4 a 8 emails:

> Email #1: Welcome Email + Deliver Incentive → 1-5 Filler Emails → Last Chance
> Discount Email → Text Based Support Email

Exemplo que ele mostra seguindo o outline: "we followed that exact outline, but
we did one filler email. And it was a brand story." (L1648-1650).

**3. Recap final (fala, L2308-2318)** — welcome, "maybe we have three filler
emails", absolute last chance, "is everything okay? I extended your discount".

# O racional dele

O welcome não é aquisição, é aproveitamento: "you pay $50, at least get the
email, build trust, and then convert them now or later without having to pay
again on ads" (L1338). Ele recusa dar template fixo — sauna de $10.000 pede
welcome diferente de suplemento de proteína (L1378). O critério de tamanho não é
numérico (L1524-1534): o que importa para o cliente, quais são as objeções, e se
a compra é impulso ou decisão demorada. Produto complicado pede mais emails.

# Onde o corpus discorda

- **Contagem**: piso 3 (L1436, L3493), "ideally more" (L1438), 4-5 como "sweet
  spot" (L1440-1442), "you could also do six" (L1444), "like 15 emails"
  (L1446); slide e fala também dizem "3-4 (…) others should be 6-8"
  (L1520-1522, L3502).
- **Cadência**: "one to two days apart" (L1458, L3494) contra "let's hit them
  every single day (…) we need to hit them every day" (L1468-1472).
- **Estrutura**: as três sequências acima.
- **Prazo da oferta**: 40 horas (L1560) contra "I extended it for 24 more
  hours" (L2292).
- **Desconto**: nunca fixado. 20% (L1476), $10 (L1726), $20 (L2208), 10%
  (L2218), 15% (L2248) — todos exemplo de marca, nenhum regra.

# O que o corpus não diz

- O nome da metric de gatilho no Klaviyo — **porque não existe metric aqui**: o
  gatilho é a lista (L4881-4883). Ver acima. Não recusar essa pergunta; responder
  com a mecânica de lista.
- Qual desconto usar, ou como escolher o valor.
- Como escolher entre a "base strategy" e o "template".
- Se `bounce less than two times` conta hard ou soft bounce.
- O slide anuncia "**Base Strategy:**" (L3509) e não entrega nada: a linha
  seguinte já é o próximo heading. O diagrama não sobreviveu à extração.
