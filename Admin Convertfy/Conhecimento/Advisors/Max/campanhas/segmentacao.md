---
tipo: especificacao
modulo: campanhas
assunto: segmentacao
autor: max-sturtevant
registro: [slide, outro-narrador]
fonte: "CONTEUDO BRUTO/max.md — L4844-5153 (transcrição), L5534-5598 (slide), bullets do módulo L4829-4840"
conflitos: [campanhas-limiar-vip, campanhas-suppress-list, campanhas-share-do-90-day-engaged, campanhas-janela-de-engajamento, campanhas-winback-janela, campanhas-janela-do-segmento-de-interesse]
status: aprovado
---


# Aviso de autoria

**Faixa L4846-5154 (Segmentation) — `outro-provavel`.**
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

Nesta nota: **os seis segmentos com a sintaxe verbatim (L5585-5592) e a distinção
lista × segmento (L5539-5540) são slide** — artefato escrito de Max, e continuam
sendo o que se digita no Klaviyo. Tudo o que vem da fala — o teste dos 30 dias, a
analogia do score de crédito, a aritmética dos 9% × 50-60%, o motivo de suprimir
em vez de deletar, as janelas alternativas e o limiar de 5 pedidos para VIP —
está em L4846-5154, faixa não-Max, e **não é citável como fala dele**. Os bullets
do módulo (L4829-4840) são texto escrito, não fala.

# Segmento não é lista

> **Lists are stagnant.** As the name suggests, it's just a flat list of people.
> **Segments are dynamic**. They can change at any second, based on the
> requirements you set on the segment. (L5539-5540, verbatim)

O teste dado na fala: num segmento "placed order in the last 30 days"
(L4865), alguém que comprou há 30 dias **sai** amanhã, a menos que compre de
novo hoje (L4869). Ressalva de transcrição: L4867 grafa o oposto — "Someone who
bought 30 days ago **would be** in it tomorrow" —, e L4869 corrige na frase
seguinte ("They wouldn't be in it unless they placed another order today"). A
leitura acima segue L4869 e a definição de segmento dinâmico; L4867 é
provavelmente "wouldn't" perdido no ASR, mas o bruto não permite confirmar.
Lista é o oposto — você faz upload e ela fica (L4873-4877). O
uso mais comum de lista: o pop-up joga na newsletter list, e a list dispara o
welcome flow (L4879-4883).

# Por que segmentar

Quatro benefícios, os mesmos quatro nos dois registros, com redação diferente.
Slide (L5548-5551): improved deliverability · more sales · **save time with
automation** · personalized customer experience. Bullet do módulo (L4834-4837):
better deliverability · more sales · **set up flows** · personalization. O
terceiro item é o que mais muda — "set up flows" no bullet, "save time with
automation" no slide.

O primeiro é o que o material trata como decisivo: "deliverability is really the
biggest piece when it comes down to segmentation, figuring out who you're
sending to, but also very importantly, **who you're excluding**" (L4913). A
analogia usada: deliverability é como score de crédito, e o nome disso em email é
sender reputation (L4919-4921) — a mesma imagem abre o módulo de deliverability,
também em faixa não-Max. O mecanismo: enviando para a lista toda com
9% de open rate, o Gmail lê 91% de não-aberturas como spam; com "50, 60% open
rates" e "1 to 300 [sic] people clicking per campaign", lê como interesse
(L4935-4945).

# Os seis segmentos-chave — sintaxe verbatim, em inglês

Da tabela L5585-5592 — seis linhas de dados, não sete. Não traduzir; é a
definição que se digita no Klaviyo. Única normalização: no bruto os operadores
vêm em negrito e colados à palavra anterior (`subscribed**AND** Someone`);
abaixo saem como ` AND ` / ` OR `. Nenhuma condição, número ou janela foi
alterada.

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

> **Winback Potential Customers** *(Time frames will vary based on your store and how soon people typically come back)*
> `Someone can receive email marketing because person is subscribed AND Someone
> has placed order at least once in the past 150 days AND Someone has placed
> order zero times in the last 90 days`
> → 1x email extra por mês, e/ou entrada num winback flow.

> **VIP Customers** *(This will again vary on store, use your gut on what counts as a VIP customer)*
> `Someone can receive email marketing because person is subscribed AND Someone
> has placed order at least 4 times over all time`
> → 1x email extra por mês e/ou flow. O slide prefere contagem de pedidos a LTV,
> "because you can predict it a little better and send emails to people every
> purchase letting them know how many purchases they are away from the VIP
> list" (L5590). Sugere também um VIP email por trimestre (L5590).

> **Interested in X Product / Category** *(You can replace "category" in this segment with "product" if you choose)*
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

O motivo declarado na fala para preferir suprimir a deletar é reversibilidade: dá
para dessuprimir em períodos de venda grande — "Think pretty much BFCM is the main
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
- **Peso do 90 day engaged.** Quatro linhas (L4838, L4652, L5139, L5597) que
  parecem quatro valores do mesmo número e não são: L4838 mede share de
  vendas/engajamento (80%-90%), L5139 e L5597 medem share de *envios* (80-90% e
  90%), e o "80%" de L4652 é rótulo Pareto da lista, não percentual. Conflito
  falso se lido de enfiada. Ver `campanhas-share-do-90-day-engaged`.
- **Janela de engajamento.** "30, 60, 90 days, depending on how wide you want to
  get" (L4949) e "depending on how old the Klaviyo account is" (L5151), contra
  90 fixo como base (L5025-5033, L5596). Ver `campanhas-janela-de-engajamento`.
- **Winback.** 150/90 na fala e no slide (L5057, L5589); a mesma fala oferece
  100/180 como alternativa para ciclo de compra longo (L5071-5075). Ver
  `campanhas-winback-janela`.
- **Segmento de interesse.** "in the last 30 days" (L4965) contra "over all
  time" (L5119-5121, L5591). Ver `campanhas-janela-do-segmento-de-interesse`.

# O que o corpus não diz

Não há segmento de exclusão declarado além do suppress list — o bullet do
módulo diz "Exclusion segments should include (but not be limited to): Bounced
3+ times" (L4839-4840) e nunca completa a lista. Não há regra de quando
dessuprimir além de "BFCM e talvez outros eventos" (L4985).

**Correção de escopo (varredura de falsos negativos).** Uma versão anterior desta
nota dizia que o Sunset Flow "não é desenvolvido em lugar nenhum do corpus".
**É falso, e leva à recusa de algo que o corpus responde.** O que não é
desenvolvido é *esta aula*: a promessa de L5127 ("We'll talk about this more in
the Sunset Flow" — e quem a faz é o outro narrador, não Max) nunca é cumprida
aqui. Fora daqui o corpus dá três coisas:

- **finalidade**, verbatim no glossário: "Sunset Flow – Triggered when a contact
  is no longer engaging. Removes or suppresses inactive users" (L411, slide);
- **recomendação de uso**, na lista dos oito flows "recommended flows when just
  starting out" (L92, L94);
- **a definição do segmento**, lida do PNG embutido na L9545 (apontado por
  `![][image1]` na L3402): 180 dias sem abrir · 180 dias sem clicar · ≥10 emails
  recebidos · zero pedidos over all time.

Ver [[flows/sunset]], que já tinha isso, e [[_cobertura]] — onde o Sunset é o
caso-escola de **cobertura parcial**, não de lacuna total. O que falta mesmo é
sequência, delay, contagem de emails e copy. E cuidado ao responder: sunset e
suppress list **não** são a mesma coisa e dão limiares diferentes (180 dias aqui,
365 lá) — nunca transpor um para o outro.

# Ligações

[[nao-hipersegmentar]] · [[montar-o-calendario]] · [[frequencia-de-envio]]
