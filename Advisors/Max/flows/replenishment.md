---
tipo: especificacao
modulo: flows
assunto: replenishment-reminder-flow
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L3222-3303 (transcrição), L3982-4039 (slide)"
conflitos: [replenishment-janela, replenishment-desconto]
status: rascunho
---

# O que é

O flow que lembra o cliente de recomprar o que está acabando. Slide, L3986: "an
automated email sequence that reminds customers to reorder products they're
likely running low on."

É o único flow do corpus com recorte de categoria: "this can be exclusive for
CPG brands, but if you don't have a CPG brand you're welcome to include this"
(L3987). Na fala: "typically CPG brands, it's going to work the best"
(L3242-3244).

Por que importa, verbatim (L3990-3992):

> * Keeps customers stocked on their favorite products
> * Reduces churn by preventing "I forgot to buy" drop-offs
> * Drives repeat purchases without heavy discounts

# Gatilho, filtros e saída

| Campo | Valor |
|---|---|
| Gatilho | `placed order` (L3252) — **só na fala**; o slide não nomeia trigger |
| Nº de emails | 2 (L3256, L4003) |
| Delay do 1º | 21 dias (L3252), ou "whenever somebody needs to replenish typically" (L3252-3254) |
| Delay do 2º | 7 dias depois do primeiro (L3258-3260, L4003) |
| Filtros | *(o corpus não informa)* |
| Saída | não ter recomprado — implícita em "the second goes out seven days later **if they haven't reordered**" (L4003); nunca especificada como condição do Klaviyo |

**A janela oscila no ar.** Ele se autocorrige na frase: "I kind of view it as
days 30 through 60-ish, 21 through 60-ish" (L3234-3236). Depois fixa 21 dias
(L3252). E no segundo email abandona o número: "set whatever time delay you
want" (L3289-3290).

Os casos de uso que ele dá são o critério real, não o número (L3249-3251,
L3996-3998): protein powder acabando depois de 30 doses, café durando ~2
semanas, skincare durando 60 dias.

# A sequência

**Email 1 — timing e conveniência.** Slide, L4011-4022:

> **Purpose & Content**
> * Remind customers it's time to restock before they run out
> * Position restocking as staying prepared and confident (no "caught off guard" moments)
> * Encourage an easy re-purchase with a one-click CTA
> * Optionally upsell with bundles or second product suggestions
>
> **Email Template**
> * **Hero section**: Bold urgency headline ("Time for a Fresh Breath Restock!")
> * **Body copy**: Friendly reminder it's been a while since their last order, nudge to reorder now
> * **Value props section**: Highlight convenience (pocket-sized, 3-sec refresh, lasts 6+ hours, scientifically proven)
> * **Product showcase**: Flavor options + bundles to encourage variety or higher order value
> * **CTA**: Strong, clear button ("Refresh Your Breath" / "Shop Now")

**Email 2 — incentivo.** Slide, L4028-4038:

> **Purpose & Content**
> * Create urgency for customers who haven't reordered after the first reminder
> * Incentivize action with a limited-time discount code
> * Frame the message around convenience ("don't get caught without it") and lifestyle use cases
> * Position the offer as short-lived to increase FOMO
>
> **Email Template**
> * **Hero section**: Discount-focused headline ("15% Off Your Next Refill!")
> * **Body copy**: Reminder to restock + highlight pain point of running out unexpectedly
> * **Offer section**: Show discount clearly with code (e.g., COOL15)
> * **CTA**: Urgent button ("Refill Now") paired with a reminder that the deal won't last

Ele marca o email 2 como opcional: "replenish reminder, the second email is
optional if you want to do a discount" (L3269-3270). O slide não marca — trata
os dois como a estratégia (L4003).

O exemplo dele é text-based e trabalha a dor de ficar sem (ASR, L3294-3300):
"hey, it's time to restock your product. You don't want that sinking feeling
when you go for a spritz of freshness only to realize you're out. Been there. So
(…) to make your refill easier, we're also giving you 15% off."

# O racional dele

A divisão de trabalho entre os dois emails é explícita: "the first email leans
on timing and convenience while the second adds incentive for those still on the
fence" (L4004).

E ele modera o próprio flow com o argumento de sempre — campanhas fazem parte do
trabalho: "no need to get out of line here, as these users will still be
receiving campaign emails and will rebuy from those" (L4005).

Alternativa ao desconto que ele menciona de passagem: "you can use like low on
stock or something like that if you want to" (L3262-3263).

# Onde o corpus discorda

- **Janela**: "30 through 60-ish" e "21 through 60-ish" na mesma frase
  (L3234-3236); depois 21 dias fixo (L3252); depois "set whatever time delay you
  want" (L3289-3290).
- **Desconto**: o slide vende o flow como "drives repeat purchases **without
  heavy discounts**" (L3992, e a fala repete em L3248) — e o email 2 do mesmo
  slide é um headline de 15% off com código COOL15 (L4035-4037), que a fala
  também dá (L3300). A contradição está dentro do mesmo registro, nos dois.
- **Trigger**: nomeado só na fala (`placed order`, L3252). O slide inteiro
  (L3982-4039) não nomeia trigger nenhum — é o único flow do slide sem isso.

# O que o corpus não diz

- Nenhum filtro. Nenhuma condição de saída configurada.
- Como calcular o delay para um produto específico — só os três exemplos de
  duração (L3996-3998).
- Se o flow deve ser splitado por produto, apesar de a duração de consumo variar
  por SKU.
- Nada sobre quantas vezes o flow pode recorrer para o mesmo cliente.
- O slide não tem slots "**Email Example:**" neste flow.
