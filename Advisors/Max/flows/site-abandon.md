---
tipo: especificacao
modulo: flows
assunto: site-abandon-flow
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L2326-2431 (transcrição), L3607-3664 (slide)"
conflitos: [site-abandon-delay-so-na-fala]
status: rascunho
---

# O que é

O flow de quem entrou no site e não passou disso. Slide, L3611-3612: "This flow
is going to trigger when someone goes to your website, but doesn't actually
view any products or go further down the funnel. Usually it's because they
didn't find a product they like and we just need to show them what we have."

Na fala ele demonstra com a Nike: abrir `nike.com` já dispara o
`active on site`; navegar sem abrir página de produto mantém a pessoa dentro
deste flow (L2343-2355).

# Gatilho, filtros e saída

| Campo | Valor |
|---|---|
| Gatilho | `Active on Site` (L2345, L3613) |
| Nº de emails | 1 a 2 (L2363-2365, L3619) |
| Delay do 1º | 4 horas padrão; 1 hora se quiser ser agressivo (L2369-2371) — **só na fala** |
| Delays seguintes | *(o corpus não informa)* |
| Filtros | *(o corpus não informa)* |
| Saída | ver página de produto (L2347-2355) |

Sobre a saída, o que ele diz literalmente (L2347-2355): "what's going to kick me
out of this flow is if I actually view a product page (…) right when we click
onto a product page, boom, this is what would trigger a different flow, which is
the browse abandoned flow". Ele **não** mostra a condição configurada no
Klaviyo — descreve o comportamento. Fica registrado como ele disse.

Sobre o delay: "I like to wait four hours. You can test this. You're going to be
a little bit more aggressive, like a one hour time delay. Typically I find that
four hours is a pretty good time delay and usually performs the best, but test
it for your brand" (L2369-2375). O slide não menciona delay nenhum.

# A sequência

**Email 1 — encorajar browsing.** Slide, L3623-3634:

> **Email Content:**
> * Encourage browsing
> * Show product(s)
> * Offer support
>
> **Subject Line Ideas:**
> * Find what you're looking for?
> * There's more here!
> * We saw you seeing us…
> * Ready to come back?

Quick Tips, verbatim (L3638-3640):

> * Include a button above the fold so the customer doesn't need to scroll
> * Make sure to include individual buttons for each product you should
> * Include category buttons for customers to shop by category (in the footer is fine)

Na fala ele acrescenta um caso: numa marca com demografia dividida entre homens
e mulheres, ele colocou um botão para cada no topo (L2393-2395). E o critério de
tom: "we don't want this to seem like another campaign, we wanted to address the
abandonment" (L2385).

**Email 2 — lembrete pessoal.** Slide, L3646-3661:

> **Email Content:**
> * Personal reminder
> * Address brand uniqueness
> * Point in the right direction
>
> **Subject Line Ideas:**
> * Just checking in
> * Find everything okay?
> * Here to help out
>
> Quick Tips:
> * Keep it short and snappy, no one wants to read an essay
> * Update the sender name to the founders name for a more personal feel

Ele registra que este email costuma bater o primeiro: "a lot of times it
performs better than the first one" (L2409). Exemplo lido em voz alta
(ASR, L2417-2427):

> hey [name], it's Michelle, the founder of Velvet [Cowder Yard]. I noticed you
> were browsing our site and didn't find a case that you liked. We have over 200
> plus styles (…) try checking out our best sellers for a curated collection.
> (…) PS, if you got the new iphone 16, you're at a 100 plus cases for it, ready
> to ship. shop 20 off today.

A marca é **Velvet Caviar**: o mesmo email reaparece no módulo de campanhas, aí
com o nome legível — "it's Michelle, the founder of Velvet Caviar" (L5198).
"Cowder Yard" é erro de ASR.

# O racional dele

Intenção baixa pede volume baixo. "We really don't need to be doing too much
here, especially since it's lower intent than like a cart abandoned or browse
abandoned or checkout abandoned, so just one to two emails to re-engage these
people is perfect" (L2361-2365).

E o argumento de fundo — que ele repete em quase todo flow — é que o flow não
carrega sozinho: "on top of this, this person will be receiving three to four
campaigns per week from you, so we don't need to go too too crazy"
(L2365-2369).

# Onde o corpus discorda

- **Delay**: 4h padrão / 1h agressivo existe só na fala (L2369-2371). O slide
  (L3607-3664) não dá delay algum.
- **Escopo da comparação de intenção**: a fala diz que é menos intenso que cart,
  browse *e* checkout abandon (L2363); o slide diz só "lower intent than a cart
  or browse abandon flow" (L3618).

# O que o corpus não diz

- Nenhum filtro. Nenhum delay entre email 1 e email 2.
- Nada sobre bloco dinâmico neste flow — coerente, já que a pessoa não viu
  produto nenhum. Mas ele nunca declara isso.
- Nada sobre desconto neste flow, em nenhum dos dois registros.
- Os dois slots "**Email Example:**" do slide (L3642, L3663) vieram vazios.
