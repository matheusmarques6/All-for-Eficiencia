---
tipo: artefato
modulo: sms
assunto: flows-de-sms
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L9244-9247 (transcrição), L9414-9482 (slide)"
conflitos: [sms-mms-no-browse-abandon, sms-welcome-contagem, sms-janela-do-winback]
status: aprovado
---

# O que são e quantos são

"SMS flows are the automated messages that will fire when a customer completes a
specified action" (L9418). São **cinco**: "there are five main SMS flows that I
like to start out with you really don't need too much with your flows because
again we don't want to overload our customers with messages" (L9244).

O princípio que rege todos: "Rather than create long flows of 8-10 messages like
we usually do for email, our sms flows have to be minimal. / We don't want to
barge the customer with a ton of texts and risk getting unsubscribes"
(L9424-9425). Os flows são o piso automatizado, não o canal principal: "these
automations are just for quick High converting and high Roi messages" (L9247).

# A especificação

| Flow | Gatilho | Delay | Nº de SMS |
|---|---|---|---|
| Welcome | opt-in na lista de SMS (L9429) | 1º: *não declarado* · 2º: `Wait 5 days` (L9440) | 2 no template (L9436-9443) · "two to three" na fala (L9245) |
| Browse Abandon | vê um item, não adiciona ao carrinho nem compra (L9447) | `Wait 60 minutes from Browse Event` (L9453) | 1 |
| Cart Abandon | "people who add to cart" (L9245) — evento próprio (L9460) | `Wait 30 minutes from Event` (L9466) | 1 — limite legal (L9461) |
| Checkout Abandon | "or go to checkout" (L9245) — evento próprio (L9460) | `Wait 30 minutes from Event` (L9466) | 1 |
| Winback | última compra (L9245) | `Wait 120 Days from Last Purchase` (L9479) | 1 · opcional (L9473) |

Cart e checkout são **dois flows separados**: "You want to setup two different
flows for cart and checkout abandon (different events)" (L9460), mas dividem o
mesmo template e o mesmo delay (L9466-9469).

# Os templates, verbatim

O corpus os anuncia como testados: "I've tested these over and over again (…)
I've literally tested this over millions of data points" (L9246). No arquivo
bruto os underscores vêm com escape de markdown (`\_\_\_`); abaixo estão sem o
escape.

**Welcome** (L9436-9443):

> **Welcome SMS 1**
> Welcome to ___! [Quick branded remark]. Use code ___ for __ OFF your first order!
> Shop Now: [link]
> **Wait 5 days**
> **Welcome SMS 2**
> Hey there, we noticed you signed up, but haven't shopped __ OFF yet. Don't miss out, this offer is about to expire!
> Shop Now: [link]

**Browse Abandon** (L9453-9456):

> **Wait 60 minutes from Browse Event**
> **Browse Abandon SMS**
> Have your eye on something? You have good taste ;)
> Keep Shopping: [Link]

**Cart / Checkout Abandon** (L9466-9469):

> **Wait 30 minutes from Event**
> **Cart / Checkout Abandon SMS**
> It looks like you forgot something in your cart!
> Finish Your Order: [link]

**Winback** (L9479-9482):

> **Wait 120 Days from Last Purchase**
> In the market for a NEW [product]?
> We miss you, take 10% OFF with code: [code]
> Shop 10% OFF:

# O racional flow a flow

**Welcome.** Entrega o desconto e nada mais. "This person will also be receiving
the email welcome flow, so don't try to do anything fancy with education or
anything like that. I like to simply do welcome message with the discount then a
closer saying the discount is expiring" (L9431-9432). É a regra de divisão de
trabalho entre canais: educação é do email — ver [[o-que-enviar-por-sms]].

**Browse abandon.** "This is one that not everybody has but is extremely
profitable for getting customers re-engaged" (L9448).

**Cart / checkout abandon.** A restrição é legal, não editorial: "In an ideal
world I would love to send multiple cart abandon sms messages, but it's actually
illegal to do in the US lol… so we're only limited to one message" (L9461). Com
uma mensagem só, a instrução é ir direto: "Don't waste any time in this message,
I found that just addressing the abandonment gets the best results" (L9462).

**Winback.** "This is optional to include… the customer will be receiving your
important messages via sms campaigns and many will convert from that" (L9473).
O desconto é opcional dentro do opcional: "You could alternatively exclude the
discount and keep it general" (L9475).

# Onde o corpus discorda

- **MMS.** A doutrina é text-only salvo necessidade absoluta (L9230, L9386), mas
  o browse abandon manda testar imagem: "you can A/B test including a picture of
  the item the person browsed to help them remember what they looked at. Keep in
  mind this is 2x-3x more expensive than just using text so review results
  accordingly" (L9449). Ver `sms-mms-no-browse-abandon`.
- **Tamanho do welcome.** Fala: "usually you want like two to three SMS
  messages" (L9245). Template do slide: duas (L9436-9443). Ver
  `sms-welcome-contagem`.
- **Janela do winback.** 120 dias no SMS (L9479) contra os 90 dias do winback de
  email (L3314-3318); a fala só diz "purchased like months ago" (L9245). Ver
  `sms-janela-do-winback`.

# O que o corpus não diz

- Nenhum nome de metric ou trigger de plataforma para nenhum dos cinco flows —
  diferente dos flows de email, onde ele nomeia `Viewed Product` (L3671),
  `Added to Cart` (L3784) e `Started Checkout` (L3790).
- Nenhum filtro, exclusão ou condição de saída: nem `placed order zero times`,
  nem supressão de quem já comprou.
- Nenhum delay para o primeiro SMS do welcome — só que dispara depois do sign-up
  (L9429).
- Nada sobre post-purchase, cross-sell ou sunset **como flow de SMS** — os cinco
  flows são welcome, browse, cart, checkout e winback, e a lista fecha ali.
  **Correção de escopo (varredura de falsos negativos):** a versão anterior
  incluía "back-in-stock" nessa lista, e isso é falso. Back-in-stock existe em
  SMS — só que como **conteúdo de campanha**, não como flow. Fala: "you can also
  create angles that make something seem important like a **back in stock**
  message" (L9249). Slide: "Sales, flash discounts, new product drops,
  **restocks**, etc" (L9498) e, no calendário de exemplo, "Notice the use of
  reminders and filling in an empty space with a product restock. **Restocks are
  a great way to get traction when you aren't sure what to send**" (L9504-9505).
  Já estava em [[o-que-enviar-por-sms]] e [[calendario-e-horarios]]. Quem perguntar por
  back-in-stock em SMS recebe a resposta de campanha e a lacuna de flow.
- O template do winback não tem rótulo de mensagem nem placeholder de link: a
  última linha é "Shop 10% OFF:" e termina ali (L9482).
- A restrição legal é afirmada sem fonte, e sem dizer se vale também para
  checkout abandon (L9461).
