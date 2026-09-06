---
tipo: especificacao
modulo: flows
assunto: post-purchase-flow
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L3021-3220 (transcrição), L3915-3981 (slide)"
conflitos: [post-purchase-escopo-temporal]
status: rascunho
---

# O que é

O flow que dispara depois da compra. Ele o classifica como subestimado: "one of
my favorite flows, one of the more underrated ones" (L3028).

O argumento é a janela quente: "somebody bought from you. Those next seven days
is like the warmest this person ever is. It's like a honeymoon phase. They just
bought from you. They've got some dopamine. (…) This is the best time to get
cross-sells and up-sells" (L3040-3046).

# Gatilho, filtros e saída

| Campo | Valor |
|---|---|
| Gatilho | `Placed Order` — metric do Shopify (L3032, L3920) |
| Nº de emails | 2 na base ("feel free to add more", L3156, L3969) |
| Delay do 1º | imediato — "immediate post-purchase thank you" (L3064) |
| Delay do 2º | "we'll wait a couple days" (L3066) |
| Filtros | *(o corpus não informa)* |
| Saída | *(o corpus não informa)* |

**Split por número de compras.** É a única ramificação declarada: "we like to
split based on if they've purchased once, twice, three times, or four times.
Four times or more" (L3076-3078). O motivo é autenticidade, não segmentação de
oferta: "we just want to make sure that it's not the same thing every time"
(L3082). O slide reduz a pro tip: "Split by # of products purchased → adjust
message for authenticity" (L3939).

# A sequência

**Email 1 — agradecimento pessoal.** Slide, L3936-3946:

> **Purpose & Content**
> * Create a personalized customer experience right after purchase
> * Strengthen brand connection by thanking them and sharing mission
> * Encourage another purchase while they're in a high buying window
> * Pro tip: Split by # of products purchased → adjust message for authenticity
>
> **Email Template**
> * **Hero section**: Sincere thank-you from the founder (warm, personal tone)
> * **Body copy**: Reinforce brand mission + highlight their impact ("you're contributing to something bigger")
> * **Support note**: Offer help or next steps (FAQs, contact info, onboarding)
> * **CTA**: Gentle push to shop again (tailored reccs or upsell)

É text-based, do founder (L3080-3081). O PS de upsell é o único número de
performance que ele dá no flow inteiro: "just a subtle, that right there, helps
get like 2% to 3% placed order rates. It's honestly crazy how many people buy
from this" (L3116-3118). O PS, verbatim do exemplo (ASR, L3110-3113): "P.S. If
you want to add more to your order, you can do so here."

Ele abre a porta para versões agressivas — free shipping na segunda compra, ou
cross-sell condicionado ao produto comprado (L3120-3124) — mas não especifica.

**Email 2 — como aproveitar o produto.** Slide, L3954-3964:

> **Purpose & Content**
> * Improve customer experience + product enjoyment
> * Reduce returns by ensuring customers know how to use their product
> * Build trust by showing you care about their success
> * Pro tip: Split by product or category to give tailored instructions
>
> **Email Template**
> * **Hero section**: Excited headline about their order ("Your [Product] is here, let's make the most of it!")
> * **Step-by-step section**: Clear instructions on setup or usage
> * **Tips & tricks**: Extra guidance or hacks for best results
> * **CTA**: Encourage ongoing use or explore related products

Na fala ele acrescenta um recurso de execução: fechar com o bloco de
"recommended Klaviyo products", que "will automatically and dynamically show
products based on what somebody has viewed in the past or what Klaviyo would
recommend for them" (L3148).

# Os 4 emails opcionais

O slide lista quatro extensões sem template (L3974-3980): **Order On The Way**,
**Cross-Sell**, **Social Media Push**, **Founder Check-In**.

Só o primeiro ganha especificação, e ela vale registrar porque muda o flow:
"you'd also have this trigger in a separate flow, with the trigger of product
shipped or product fulfilled" (L3170). Ou seja, o "order on the way" **não
é um email deste flow** — é outro flow.

O Founder Check-In é o único com exemplo (ASR, L3196-3209): "hope you're doing
well and keeping in good health. It's been nearly three weeks since you started
your journey and I want to personally follow up with you."

# O racional dele

O flow existe porque o cliente pós-compra tem três estados ao mesmo tempo, e ele
lista os três (L3926-3928): propensão a comprar, animação com o pedido e
incerteza sobre o produto. O flow tem que atender aos três — daí um email de
reforço emocional e um de instrução.

E ele desarma o próprio conteúdo: "this is just very, very base. Feel free to
add more emails. This really is just a starting point. You know your brand"
(L3154-3160).

# Onde o corpus discorda

**Três escopos temporais, nenhum reconciliado:**

| Escopo | Verbatim | Registro | Linha |
|---|---|---|---|
| 7 dias | "those next seven days is like the warmest this person ever is" | transcrição | L3040 |
| 14 dias | "post-purchase flow as within 14 days" | transcrição | L3162 |
| 14 dias | "relevant in the first 14 days after a customer purchase" | slide | L3971 |
| ~3 semanas | "a couple of weeks after somebody bought (…) it's been nearly three weeks" | transcrição | L3194-3198 |

A linha L3162 vem logo depois de "you know your brand" (L3160) e é uma frase
truncada na transcrição — mas o slide confirma o número 14 (L3971). O exemplo de
~3 semanas está dentro da própria lista de emails opcionais que o slide diz
serem para os primeiros 14 dias.

# O que o corpus não diz

- Nenhum filtro, nenhuma condição de saída.
- O delay do email 2 nunca vira número: "a couple days" (L3066) é tudo.
- Como o split por número de compras muda a copy — ele promete exemplos
  ("we'll have examples for you", L3084) e não entrega na faixa.
- Os dois slots "**Email Example:**" do slide (L3948, L3966) vieram vazios.
