---
tipo: especificacao
modulo: campanhas
assunto: segmentacao
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L4844-5153 (transcrição), L5534-5598 (slide), bullets do módulo L4829-4840"
conflitos: [campanhas-limiar-vip, campanhas-suppress-list, campanhas-share-do-90-day-engaged, campanhas-janela-de-engajamento, campanhas-winback-janela, campanhas-janela-do-segmento-de-interesse]
status: rascunho
---

# Segmento não é lista

> **Lists are stagnant.** As the name suggests, it's just a flat list of people.
> **Segments are dynamic**. They can change at any second, based on the
> requirements you set on the segment. (L5539-5540, verbatim)

O teste que ele dá na fala: num segmento "placed order in the last 30 days",
alguém que comprou há 30 dias **sai** amanhã, a menos que compre de novo hoje
(L4863-4869). Lista é o oposto — você faz upload e ela fica (L4873-4877). O
uso mais comum de lista: o pop-up joga na newsletter list, e a list dispara o
welcome flow (L4879-4883).

# Por que segmentar

Quatro benefícios, iguais nos dois registros (L4833-4837, L5548-5551):
improved deliverability · more sales · save time with automation ·
personalized customer experience.

O primeiro é o que ele trata como decisivo: "deliverability is really the
biggest piece when it comes down to segmentation, figuring out who you're
sending to, but also very importantly, **who you're excluding**" (L4913). A
analogia dele: deliverability é como score de crédito, e o nome disso em email
é sender reputation (L4919-4921). O mecanismo: enviando para a lista toda com
9% de open rate, o Gmail lê 91% de não-aberturas como spam; com "50, 60% open
rates" e "1 to 300 [sic] people clicking per campaign", lê como interesse
(L4935-4945).

# Os seis segmentos-chave — sintaxe verbatim, em inglês

Da tabela L5585-5592. Não traduzir; é a definição que se digita no Klaviyo.

> **90 Day Engaged List** *(You can use any time frame, 90 is recommended to start)*
> `Someone can receive email marketing because person is subscribed AND Someone
> has Opened Email at least once in the last 90 days OR Someone has been Active
> on Site at least once in the last 90 days OR Someone has Placed An Order at
> least once in the last 90 days`
> → base de envio de todas as campanhas.

> **High-Potential Purchasers**
> `Someone can receive email marketing because person is subscribed AND Someone
> has placed order 0 times in the past 30 days AND Someone has been active on
> site at least once in the past 30 days`
> → 1x-2x emails extras por mês, além dos envios para a engaged list. Na fala:
> "window shoppers" (L5045-5049).

> **Winback Potential Customers** *(Time frames will vary based on your store)*
> `Someone can receive email marketing because person is subscribed AND Someone
> has placed order at least once in the past 150 days AND Someone has placed
> order zero times in the last 90 days`
> → 1x email extra por mês, e/ou entrada num winback flow.

> **VIP Customers** *(use your gut on what counts as a VIP customer)*
> `Someone can receive email marketing because person is subscribed AND Someone
> has placed order at least 4 times over all time`
> → 1x email extra por mês e/ou flow. Ele prefere contagem de pedidos a LTV,
> "because you can predict it a little better and send emails to people every
> purchase letting them know how many purchases they are away from the VIP
> list" (L5590). Sugere também um VIP email por trimestre (L5590).

> **Interested in X Product / Category**
> `Someone can receive email marketing because person is subscribed AND Someone
> has viewed item where category is [category] at least once over all time. OR
> Someone has added item to cart where category is [category] at least once
> over all time. OR Someone has started checkout with item where collection is
> [collection] at least once over all time. OR Someone has placed order with
> item where collection is [collection] at least once over all time.`
> → campanhas, anúncios e lançamentos daquele item.

> **Suppress List**
> `Someone can receive email marketing because person is subscribed AND Someone
> has received email at least 5 times over all time AND Someone has opened
> email zero times in the last 365 days OR Someone has bounced email at least 3
> times over all time OR Someone has marked email as spam at least once over
> all time`
> → não enviar NADA. Revisar uma vez por mês e suprimir (L5592).

# Suprimir não é deletar

> instead of deleting them from the whole list, you can suppress them, which
> means you can't send to them, but you can get them back if you want. So
> they're not gone forever. (L4979-4981, verbatim)

O motivo declarado de preferir suprimir a deletar é reversibilidade: dá para
dessuprimir em períodos de venda grande — "Think pretty much BFCM is the main
one" (L4983-4985). O segundo motivo é custo: "keep our Klaviyo bill
manageable", já que o Klaviyo cobra por perfil (L5133, L5592).

# Onde o corpus discorda

- **VIP.** Slide: `at least 4 times over all time` (L5590). Fala: "if someone's
  placed five orders on the site, give them an additional discount" (L5103).
  Ver `campanhas-limiar-vip`.
- **Suppress list.** A fala é impressionista — "received at least five to ten
  emails over all time, opened zero times in the last year, bounced email, you
  know, multiple times, or marked as spam" (L5129). O slide é exato: 5 emails,
  365 dias, 3 bounces, 1 spam complaint (L5592). E o bullet do módulo cita só
  "Bounced 3+ times" (L4840). Ver `campanhas-suppress-list`.
- **Peso do 90 day engaged.** Quatro valores diferentes, medindo coisas
  diferentes (L4838, L4652, L5139, L5597). Ver
  `campanhas-share-do-90-day-engaged`.
- **Janela de engajamento.** "30, 60, 90 days, depending on how wide you want to
  get" (L4949) e "depending on how old the Klaviyo account is" (L5151), contra
  90 fixo como base (L5025-5033, L5596). Ver `campanhas-janela-de-engajamento`.
- **Winback.** 150/90 na fala e no slide (L5057, L5589); ele mesmo oferece
  100/180 como alternativa para ciclo de compra longo (L5071-5075). Ver
  `campanhas-winback-janela`.
- **Segmento de interesse.** "in the last 30 days" (L4965) contra "over all
  time" (L5119-5121, L5591). Ver `campanhas-janela-do-segmento-de-interesse`.

# O que o corpus não diz

Não há segmento de exclusão declarado além do suppress list — o bullet do
módulo diz "Exclusion segments should include (but not be limited to): Bounced
3+ times" (L4839-4840) e nunca completa a lista. O Sunset Flow, que ele promete
em L5127 ("We'll talk about this more in the Sunset Flow"), não é desenvolvido
em lugar nenhum do corpus. Não há regra de quando dessuprimir além de "BFCM e
talvez outros eventos" (L4985).

# Ligações

[[nao-hipersegmentar]] · [[montar-o-calendario]] · [[frequencia-de-envio]]
