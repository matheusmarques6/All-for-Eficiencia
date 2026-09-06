---
tipo: especificacao
modulo: flows
assunto: cart-checkout-abandon-flows
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L2618-3019 (transcrição), L3777-3914 (slide)"
conflitos: [cart-checkout-conteudo-igual-ou-diferente, cart-checkout-ausencia-total-de-delays, cart-checkout-bloco-dinamico]
status: rascunho
---

# O que é

**São dois flows, não um.** Essa é a tese central da aula: "most of you think
it's just one flow, but it's actually two flows. We have the cart abandoned flow
and the checkout abandoned flow" (L2629-2631).

- **Cart abandon** — a pessoa adiciona ao carrinho e não vai para o checkout.
  "It isn't the farthest intent where they go to the payment page (checkout
  abandon), but it is still very high intent" (L3783).
- **Checkout abandon** — a pessoa começa o checkout (põe email, começa a
  preencher) e não finaliza. "This is *the highest* intent flow — they were
  right there and just didn't finish" (L3789).

Demonstração com a Nike: `add to bag` dispara o cart; clicar em checkout e cair
na página de checkout dispara o outro (L2647-2659).

## A acusação contra o Klaviyo

"Most brands I audit only have a checkout abandoned flow, but it's labeled as
cart abandoned. **For whatever reason, Klaviyo, their base templates, they
labeled them wrong.** So everybody has it wrong, and they miss out on a ton of
revenue." (L2681-2685). É a única vez, na faixa inteira de flows, em que ele
aponta erro na ferramenta que recomenda.

# Gatilho, filtros e saída

| Campo | Cart abandon | Checkout abandon |
|---|---|---|
| Gatilho | `Added to Cart` (L2669, L3784) | `Started Checkout` (L3790) / "checkout started" (L2671) |
| Nº de emails | 4 (L3798-3881) | 4 (mesma sequência) |
| Delay do 1º | | |
| Delays seguintes | | |
| Filtros | | |
| Saída | | |

**As células vazias são deliberadas.** Nenhum delay, nenhum filtro e nenhuma
condição de saída é declarado para cart ou checkout abandon em nenhum dos dois
registros — nem na transcrição (L2618-3019) nem no slide (L3777-3914). Este é o
único par de flows do corpus em que ele especifica quatro emails sem dizer
quando disparam. Não preencher por analogia com browse abandon.

O nome do trigger de checkout aparece nas duas grafias: "checkout started"
(L2671) na fala, `Started Checkout` (L3790) no slide.

# A sequência

Uma sequência única, aplicada aos dois flows (L3798-3881).

**Email 1 — lembrete simples.**

> **Email Content:** Simple reminder · Dynamic Klaviyo block · Brief product Info
>
> **Subject Line Ideas:** Your order is ready to ship · One click away! · Your cart is waiting
>
> Quick Tips:
> * Include relevant shipping information (should as free shipping threshold)
> * Have the button and dynamic content at the very top of the email so the customer doesn't need to scroll

Fala: "let's not distract from anything besides, here's your product, go buy it"
(L2731). Exemplo de threshold: "free shipping on all orders over $70" (L2741).

**Email 2 — text-based.**

> **Email Content:** Text-based email · Personal reminder · Social proof
>
> **Subject Line Ideas:** Quick check-in · Holding onto your order · Have any questions with your order?
>
> Quick Tips:
> * List out just a couple social proof points
> * Avoid using too many CTAs, keep it simple

Exemplo (ASR, L2789-2813): "Hi Kelly, hope you are well and keeping in good
health. Want to check in if there's anything we can do to help you complete your
purchase" — mais social proof em números: "40 patents, 26 research studies,
United States Department of Defense, 12 dental experts on staff".

**Email 3 — desconto.**

> **Email Content:** Discount opener · Dynamic Klaviyo block · Social proof / FAQs
>
> **Subject Line Ideas:** $XX OFF Your Cart! · Limited time discount on your order · Just for you 🎁
>
> Quick Tips:
> * Feature the discount code and offer at the very top of the email
> * Keep it as simple as possible… the discount should be the main aspect of the email

Sobre o tipo de incentivo ele não decide, manda testar: "dollar off, percent
off, giving a free gift, giving free shipping. Test all these things out"
(L2829-2841).

**Email 4 — text-based last chance.**

> **Email Content:** Text-based last chance · Personal discount reminder · Offer support
>
> **Subject Line Ideas:** Last chance · Still want XX% OFF? · Your cart is expiring (and your gift)
>
> Quick Tips:
> * Add a PS section offering support
> * Bold your main points and discounts for the customer
> * Avoid too many CTAs that will cause overwhelm

# O racional dele

Todo email resolve fricção, não desejo: "these users are *one or two clicks
away* — so every email should reduce friction, provide assurance, and make
buying feel easy" (L3794). Dois dos quatro são text-based, justificados sem
dado: "we do this just because it works so well. Trust me. We've tested this."
(L2899-2905). Sobre remetente ele dá a preferência e o custo de contrariá-la:
"I always recommend coming from an actual person (…) they wanted to keep
people's names out, which is going to hurt your results most often. But you can
still do it" (L2941-2951).

# Templates

Os blocos dinâmicos dos dois flows são **diferentes** e estão em
[[conteudo-dinamico-klaviyo]]: cart usa `Split` com variável de evento único
(L3885-3895), checkout usa `Table` iterando `event.extra.line_items`
(L3901-3913).

# Onde o corpus discorda

**O conteúdo deve ser igual ou diferente?** Três posições, todas dele, na mesma
aula:

| Posição | Verbatim | Linha |
|---|---|---|
| não precisa ser diferente | "we really don't need different content for cart abandoned and checkout abandoned. You really don't." | L2689-2691 |
| a agência sempre faz diferente | "we always do for our clients. We make them different, slightly different." | L2693-2695 |
| o ideal é diferente | "ideally, if you can make the content a little bit different, that would be best, but not completely necessary" | L3015 |

O slide fica no meio: "To save time, you can use the same emails for both of
these flows. If you have time, try to make them slightly different" (L3795).

**O bloco dinâmico do cart:** a fala diz "we are using a split dynamic image on
the left" (L2971) e o slide confirma `Split` (L3885) — mas o mesmo slide
usa `Table` para browse (L3767). Ele reconhece que a diferença é histórica, não
técnica: "for Bannon checkout, it's going to be a little bit different for
whatever reason. We just have it a little bit different. This is what we've
always done" (L2987-2991).

# O que o corpus não diz

- **Nenhum delay, filtro ou condição de saída.** Ver a tabela acima.
  **Evidência da varredura:** `time delay|hour|minute|wait` na fala do módulo
  (L2618-3020) e no deck (L3777-3918) devolve zero; `kick|exclude|exclusion|
  filter|zero times|skip|exit` em toda a faixa de flows (L1307-4186) devolve
  cinco linhas e nenhuma delas é de cart ou checkout. O vizinho — e é só
  vizinho — é o teste 30min × 4h do módulo de otimização (L8952-8962), que
  reporta vencedor "at least on the site abandoned". Ver
  [[otimizacao/flow-time-delays]].
- Qual desconto usar no email 3. Os exemplos são $35 (L2871), 20% (L2923), "1x%"
  (L2911, ASR corrompido) — nenhum vira regra.
- Se o cart abandon deve excluir quem já entrou no checkout abandon, apesar de
  ele afirmar que "cart abandoned is a step before checkout abandoned" (L2661).
- Os quatro slots "**Email Example:**" do slide (L3817, L3838, L3859, L3881)
  vieram vazios.
