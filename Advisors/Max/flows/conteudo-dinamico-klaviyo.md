---
tipo: artefato
modulo: flows
assunto: conteudo-dinamico-klaviyo
autor: max-sturtevant
registro: [slide, transcricao]
fonte: "CONTEUDO BRUTO/max.md — L3765-3776, L3883-3896, L3897-3914 (slide); L2589-2616, L2956-3012 (transcrição)"
conflitos: [cart-checkout-bloco-dinamico]
status: rascunho
---

# O que é

As três fórmulas de bloco dinâmico do Klaviyo que o corpus entrega: uma para
[[browse-abandon]], uma para cart abandon e uma para checkout abandon (as duas
últimas em [[cart-checkout-abandon]]). Código verbatim em inglês, do slide.

Regra de layout que vale para as três: o bloco dinâmico vai o mais alto possível
no email. "For abandonments, we really want to make sure that we have the
dynamic content above the fold" (L2512-2514) — e o motivo é ver o produto na
cara ao abrir (L2516-2520).

> **Nota de transcrição.** No arquivo bruto os underscores aparecem escapados
> por markdown (`line\_items`, `currency\_format`, `missing\_product\_image`).
> O código abaixo está sem os escapes, que é como ele funciona no Klaviyo.

# Browse abandon

Slide, L3767-3775:

> * Create a "Table" block in Klaviyo
> * Add an image on the left side
> * Use a "Dynamic Image"
> * Insert the dynamic variable "{{ event.ImageURL }}"
> * Add text on the right side
> * For the item name use "{{ event.Name }}"
> * For the price use the variable "{{ event.Price|default:'' }}"
> * Add the correct link to the photo, text, and buttons
> * Use the dynamic link "{{ event.URL }}" which will take the customer top the product page they viewed

# Cart abandon

Slide, L3885-3895:

> * Create a "Split" block in Klaviyo
> * Add an image on the left side
> * Use a "Dynamic Image"
> * Insert the dynamic variable "{{ event.ImageURL }}"
> * Add text on the right side
> * For the item name use "{{ event.Name }}"
> * For the price use the variable "{{ event.Price|default:'' }}"
> * Add the correct checkout link to the photo, text, and buttons
> * If you have a cart page on your site, use that link.
> * Will most likely be "storename.com/cart"
> * If you don't, use the dynamic link "{{ event.URL }}"

# Checkout abandon

Slide, L3901-3913:

> * Create a "Table" block in Klaviyo
> * Under table settings select "Dynamic"
> * Under "Row collection" enter "event.extra.line_items"
> * Under "Row alias" enter "item"
> * Add an image on the left side
> * Use a "Dynamic Image"
> * Insert the dynamic variable "{% if item.product.variant.images.0.src %}{{item.product.variant.images.0.src}}{%else%}{{item.product.images.0.src|missing_product_image}}{%endif%}"
> * Add text on the right side
> * For the item name use "{{ item.product.title }}"
> * For the price use the variable "{% currency_format item.line_price|floatformat:2 %}"
> * For the quantity use the variable "{{ item.quantity|floatformat:0 }}"
> * Add the correct checkout link to the photo, text, and buttons
> * Use the dynamic variable "{{ event.extra.checkout_url|default:'' }}"

# A diferença estrutural

Browse e cart usam **variável de evento único**. O evento que dispara o flow
carrega um produto só — o que foi visto, ou o que foi adicionado — e as
variáveis apontam direto para ele: `event.ImageURL`, `event.Name`,
`event.Price`. O bloco renderiza um item. Por isso ambos usam blocos estáticos
(`Table` no browse, `Split` no cart) com variáveis dentro.

Checkout **itera uma coleção**. O evento `Started Checkout` carrega o carrinho
inteiro, então o bloco precisa de repetição: a tabela é marcada como `Dynamic`,
a coleção a percorrer é `event.extra.line_items`, e cada volta do laço recebe o
apelido `item`. Todas as variáveis passam a ser relativas a esse apelido —
`item.product.title`, `item.line_price`, `item.quantity` — em vez de relativas
ao evento. É o que permite mostrar três produtos quando o carrinho tem três.

Três consequências práticas dessa diferença, todas visíveis no código:

1. **Quantidade só existe no checkout.** `{{ item.quantity|floatformat:0 }}` não
   tem equivalente em browse ou cart, porque não há linha de pedido para contar.
2. **O preço muda de natureza.** Browse e cart lêem um preço bruto com fallback
   vazio (`|default:''`). Checkout usa `{% currency_format ... %}` sobre
   `item.line_price`, ou seja, formata moeda sobre o preço da linha — total do
   item, não preço unitário.
3. **A imagem precisa de fallback.** Só o checkout traz um `{% if %}`: tenta a
   imagem da variante (`item.product.variant.images.0.src`) e, se não houver, cai
   na imagem do produto passada por `|missing_product_image`. Browse e cart usam
   `{{ event.ImageURL }}` cru, sem rede de proteção — o evento já traz a imagem
   resolvida.

O destino do link também segue essa lógica: browse manda de volta para a página
do produto (`event.URL`), cart manda para a página de carrinho da loja
(`storename.com/cart`, ou `event.URL` como alternativa), e checkout manda para a
URL de retomada do checkout (`event.extra.checkout_url`).

# O racional dele

Ele não garante que funcione. Duas vezes manda validar contra o template nativo:
"go into Klaviyo and just look up when you're creating flows (…) click their
template and then go and check if it works for you" (L2594-2596) e "test their
dynamic content that they give inside the template" (L2961-2969). E manda usar o
preview: "if you click preview and test right here, once you have it in here,
you're actually going to see what it looks like for your customers" (L2981).

Sobre por que a fórmula do checkout é mais pesada, a explicação é histórica, não
técnica: "for [abandoned] checkout, it's going to be a little bit different for
whatever reason. We just have it a little bit different. This is what we've
always done" (L2987-2991).

# Onde o corpus discorda

O tipo de bloco do browse: a fala hesita — "so you create a split, it's
step-by-step right here, create a table block in Klaviyo" (L2598-2600) — e o
slide diz `Table` (L3767). Vale o slide.

Capitalização das variáveis: a fala diz `event.name` e `event.url`
(L2608-2610); o slide diz `{{ event.Name }}` e `{{ event.URL }}` (L3772,
L3775). Vale o slide — é artefato.

# O que o corpus não diz

- Nada sobre bloco dinâmico em site abandon, post-purchase, replenishment ou
  winback. As três fórmulas cobrem só os flows de produto abandonado.
- Nenhuma fórmula de fallback para quando o evento não traz produto.
- Nenhuma versão para SMS.
- A alternativa que ele cita para post-purchase, "recommended Klaviyo products"
  (L3148), não tem código nem instrução — é bloco nativo.
