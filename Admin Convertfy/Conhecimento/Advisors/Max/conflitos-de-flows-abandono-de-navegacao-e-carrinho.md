---
tipo: indice
modulo: flows
assunto: conflitos-flows-abandono-de-navegacao-e-carrinho
autor: max-sturtevant
conflitos: [site-abandon-delay-so-na-fala, browse-abandon-janela-de-delays, browse-abandon-definicao-do-gatilho, cart-checkout-conteudo-igual-ou-diferente, cart-checkout-ausencia-total-de-delays, cart-checkout-bloco-dinamico]
status: aprovado
---

Registro dos conflitos do módulo `flows` do corpus de Max Sturtevant sobre os flows de abandono: site abandon, browse abandon (janela de delays e definição do gatilho) e cart/checkout abandon (conteúdo igual ou diferente, ausência total de delays e bloco dinâmico). Cada entrada lista os valores divergentes por registro e fecha com um "Como responder".


Faixa: L1307-3403 (transcrição) e L3404-4186 (slide GAMMA). `flows-onde-testar`
está em [[conflitos-entre-modulos-onde-testar-frequencia-e-pontas-soltas]].


## site-abandon-delay-so-na-fala

| Valor | Registro | Linha |
|---|---|---|
| "I like to wait four hours (…) usually performs the best, but test it for your brand" | transcricao | L2369-2375 |
| "a one hour time delay" (variante agressiva) | transcricao | L2371 |
| nenhum delay | slide | L3607-3664 |

**Como responder:** 4 horas como padrão, 1 hora como variante agressiva, e diga que
o número vem só da fala — o slide não especifica delay para este flow. Ele mesmo
enquadra como testável, não como regra. Não há delay declarado entre o email 1 e o
email 2 em nenhum dos dois registros.


## browse-abandon-janela-de-delays

| Valor | Registro | Linha |
|---|---|---|
| "wait one hour and then one day between the rest of these emails" | transcricao | L2476-2478 |
| "**4 emails works well here**, spaced out over 3-4 days" | slide | L3678 |

**Como responder:** os dois são a mesma janela vista de ângulos diferentes. Não é
contradição de valor, é diferença de granularidade. Use a fala, que é a única
acionável, e cite o slide como confirmação da ordem de grandeza. Registre que os
intervalos entre os emails 2, 3 e 4 nunca são especificados separadamente.


## browse-abandon-definicao-do-gatilho

| Valor | Registro | Linha |
|---|---|---|
| "they click onto a product page, but they didn't go any further" | transcricao | L2446 |
| "views a product on your site but doesn't add anything to their cart" | slide | L3669 |

**Como responder:** o trigger é o mesmo nos dois (`Viewed Product`); o que muda é a
condição implícita de permanência. "Didn't go any further" é mais amplo que "doesn't
add anything to cart" — pela versão do slide, quem adiciona ao carrinho sai do browse
abandon; pela versão da fala, sai qualquer um que avance de qualquer forma. Nenhum
dos dois registros declara essa condição de saída como configuração. Diga que o
corpus não especifica.


## cart-checkout-conteudo-igual-ou-diferente

| Posição | Verbatim | Registro | Linha |
|---|---|---|---|
| não precisa ser diferente | "we really don't need different content for cart abandoned and checkout abandoned. You really don't." | transcricao | L2689-2691 |
| a agência sempre faz diferente | "we always do for our clients. We make them different, slightly different." | transcricao | L2693-2695 |
| o ideal é diferente, mas não é necessário | "ideally, if you can make the content a little bit different, that would be best, but not completely necessary" | transcricao | L3015 |
| meio-termo | "To save time, you can use the same emails for both of these flows. If you have time, try to make them slightly different." | slide | L3795 |

**Como responder:** a posição de referência é a do slide, porque é a única que
concilia as três falas: mesmo conteúdo é aceitável, conteúdo diferente é melhor, e o
que decide é tempo disponível. Mas mostre que na fala ele diz as três coisas em
minutos — inclusive que a própria agência dele sempre faz diferente, o que contradiz
na prática o conselho que ele acabou de dar. O que **não** muda entre os dois flows é
o bloco dinâmico (L3885-3913). Ver `cart-checkout-bloco-dinamico`.


## cart-checkout-ausencia-total-de-delays

| Campo | Cart | Checkout | Registro | Linha |
|---|---|---|---|---|
| Delay do 1º | ausente | ausente | transcricao e slide | L2618-3019, L3777-3914 |
| Delays seguintes | ausente | ausente | transcricao e slide | idem |
| Filtros | ausente | ausente | transcricao e slide | idem |
| Condição de saída | ausente | ausente | transcricao e slide | idem |

**Como responder:** não é conflito, é **lacuna** — e é a lacuna mais cara do módulo,
porque estes são os dois flows de maior intenção e o corpus especifica quatro emails
com subject lines e quick tips para eles sem dizer quando disparam. **Nunca preencher
por analogia com browse abandon.** Se perguntarem o delay do cart abandon, a resposta
é que o corpus não informa, e o vizinho mais próximo é o princípio geral de que time
delay é "the biggest lever" (L4143) e deve ser testado.


## cart-checkout-bloco-dinamico

| Flow | Bloco | Fonte da imagem | Registro | Linha |
|---|---|---|---|---|
| Browse | `Table` | `{{ event.ImageURL }}` | slide | L3767-3770 |
| Browse | "you create a split (…) create a table block" | — | transcricao | L2598-2600 |
| Cart | `Split` | `{{ event.ImageURL }}` | slide | L3885-3888 |
| Cart | "we are using a split dynamic image on the left" | — | transcricao | L2971 |
| Checkout | `Table` + `Dynamic` + `Row collection` | `{% if item.product.variant.images.0.src %}…` | slide | L3901-3907 |

**Como responder:** vale o slide, é artefato. A hesitação da fala em L2598-2600
("split… table block") é ruído. A diferença real entre browse/cart e checkout é
estrutural: os dois primeiros lêem variável de evento único, o terceiro itera
`event.extra.line_items`. Já a diferença `Table` (browse) vs `Split` (cart) para o
mesmo tipo de dado não tem explicação técnica no corpus — ele mesmo diz "it's going
to be a little bit different for whatever reason (…) this is what we've always done"
(L2987-2991).


