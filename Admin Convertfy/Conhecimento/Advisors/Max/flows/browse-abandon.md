---
tipo: especificacao
modulo: flows
assunto: browse-abandon-flow
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L2433-2616 (transcrição), L3665-3776 (slide)"
conflitos: [browse-abandon-janela-de-delays, browse-abandon-definicao-do-gatilho]
status: aprovado
---

# O que é

O flow de quem abriu uma página de produto e parou aí. "They showed interest in
that product, enough so to view the product page, but they didn't take action.
So our job is to remind them of what caught their high and guide them closer to a
purchase" (L2448-2452) — "high" é ASR de *eye*, como o slide confirma (L3670).

Demonstração com a Nike: navegar o site não entra; clicar no produto dispara
(L2454-2460).

# Gatilho, filtros e saída

| Campo | Valor |
|---|---|
| Gatilho | `Viewed Product` (L2452, L3671) |
| Nº de emails | 4 (L2472, L3678) |
| Delay do 1º | 1 hora (L2476) |
| Delays seguintes | 1 dia entre os demais (L2476-2478) |
| Filtros | *(o corpus não informa)* |
| Saída | *(o corpus não informa)* |

O slide dá a janela agregada em vez dos delays: "**4 emails works well here**,
spaced out over 3-4 days" (L3678). A fala dá os intervalos: "we like to wait one
hour and then one day between the rest of these emails" (L2476-2478).

Justificativa do aperto: "we don't want to wait too long because at this point,
if somebody viewed a product, then we don't email them again for like two weeks
or a week, then they have lost interest" (L2478-2482).

# A sequência

**Email 1 — dinâmico + social proof + outros produtos.** Slide, L3682-3698:

> **Email Content:** Dynamic Klaviyo block · Give social proof · Show other products
>
> **Subject Line Ideas:**
> * Something catch your eye?
> * Watcha got there?
> * Saved for you
>
> Quick Tips:
> * Make your buttons nice and big
> * Feature multiple products that may better fit the customer
> * Put the dynamic content block as high up in the email as possible

**Email 2 — lembrete + FAQs.** Slide, L3704-3719:

> **Email Content:** Dynamic Klaviyo block · Simple reminder · Answer FAQs
>
> **Subject Line Ideas:**
> * Take another look!
> * Quick reminder
> * Don't wait on this one
>
> Quick Tips:
> * Answer only 3 FAQs to avoid overwhelm
> * Try to sneak in some social proof (one testimonial is good)

**Email 3 — o desconto.** Slide, L3725-3740:

> **Email Content:** Discount opener · Dynamic Klaviyo block · Show other products
>
> **Subject Line Ideas:**
> * Still thinking?
> * A gift for you 🎁
> * 10% OFF your viewed item!
>
> Quick Tips:
> * Mention the discount in the preview text or subject line
> * Put the discount high up in the email for easy access

Este email é opcional na fala: "we're going to enter a discount at the end of
this flow, which you can make this optional if you want (…) you could send this
to just people who haven't bought from you before" (L2488-2490), via split no
Klaviyo (L2550).

**Email 4 — text-based last chance.** Slide, L3746-3761:

> **Email Content:** Text-based last chance · Personal discount reminder · Educate on brand info
>
> **Subject Line Ideas:**
> * Checking in on your gift
> * Hey, It's Ashley!
> * Saved this discount for you…
>
> Quick Tips:
> * Bold your main points, especially the discount
> * Make it seem personal, like the founder reaching out

Exemplo lido em voz alta (ASR, L2572-2580): "hey there, it's Ashley, the rebel
mastermind behind Rebel Bro. We started this brand with one goal in mind: to
create cool clothes for boys with exceptional quality made to last. (…) That's
why we saved your discount for you. This is your last chance."

# O racional dele

Intenção maior que site abandon, então persuasão maior: "this is higher intent
than site abandon, so we want to be a bit more persuasive. Highlight benefits,
provide social proof, and answer questions they might have" (L3676).

E a regra de layout que ele generaliza para todos os abandonos: o bloco dinâmico
vai o mais alto possível. O motivo (L2516-2520): "if somebody opens an email and
we show them right in their face the product that they were just looking at like
20 minutes ago or an hour ago, that's going to catch their eye and make them
keep reading". Em emails comuns basta botão above the fold; em abandono o que
tem que estar above the fold é o conteúdo dinâmico (L2512-2514).

Um detalhe de estratégia que só a fala tem: mostrar **outros** produtos, porque
"the item that they browsed, they didn't add it to cart — it might not be the
product that they want" (L2470-2472).

# Templates

O bloco dinâmico deste flow está em [[conteudo-dinamico-klaviyo]] (fórmula do
slide, L3767-3775). Ele avisa que pode não funcionar direto: "sometimes it
depends on how your store is set up and you might need to hit up Klaviyo
support" (L2590-2592), e recomenda abrir o template nativo de browse abandon do
Klaviyo para conferir (L2594-2596).

# Onde o corpus discorda

- **Delays**: fala dá 1h + 1 dia entre os demais (L2476-2478), o que produz
  ~3 dias e 1h de janela; slide dá "spaced out over 3-4 days" (L3678) sem
  intervalos. As duas versões são compatíveis em ordem de grandeza, mas só uma
  é acionável.
- **Definição do gatilho**: a fala diz que a pessoa "didn't go any further"
  (L2446); o slide diz "views a product on your site but doesn't add anything to
  their cart" (L3669). São condições diferentes de saída implícita.
- **Tipo de bloco**: a fala começa dizendo "you create a split" e emenda "create
  a table block in Klaviyo" (L2598-2600); o slide diz `Table` (L3767).

# O que o corpus não diz

- Nenhum filtro, nenhuma condição de saída configurada. **Evidência da
  varredura:** `kick|exclude|exclusion|filter|zero times|skip|exit` em toda a
  faixa de flows (L1307-4186) devolve só L1540-1546 (welcome), L2349 (site
  abandon) e L3318 (segmento do winback). Nada na faixa do browse abandon —
  nem na fala (L2440-2618) nem no deck (L3665-3776).
- Qual desconto usar no email 3 (o exemplo é 10%, L2554, mas nunca vira
  regra).
- Se o split para excluir compradores anteriores é recomendado ou apenas
  possível.
- Os quatro slots "**Email Example:**" do slide (L3700, L3721, L3742, L3763)
  vieram vazios.
