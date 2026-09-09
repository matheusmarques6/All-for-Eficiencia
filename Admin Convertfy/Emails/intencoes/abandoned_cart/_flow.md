---
tipo: intencao
escopo: flow
flow_type: abandoned_cart
flow_tamanho: 8
status: rascunho
fonte: "Conhecimento/Advisors/Max/flows/cart-checkout-abandon.md — §O que é (bruto L2629-2631, L3783, L3789), §Gatilho, filtros e saída (bruto L2669, L2671, L3784, L3790), §A sequência (bruto L3798-3881), §O racional dele (bruto L3794, L2899-2905, L2941-2951), §Onde o corpus discorda (bruto L2689-2695, L3015, L3795), §O que o corpus não diz; Conhecimento/Advisors/Max/flows/conteudo-dinamico-klaviyo.md — §O que é (bruto L2512-2520), §Cart abandon (bruto L3885-3895), §Checkout abandon (bruto L3901-3913), §A diferença estrutural"
---

# A intenção do flow inteiro

A pessoa pôs um item no carrinho — ou começou o checkout — e parou. Não há
contrato nem incentivo prometido, como no welcome: há um objeto concreto,
escolhido por ela, e uma finalização que não aconteceu. No Max isso são **dois
flows**: cart abandon (`Added to Cart`, "still very high intent") e checkout
abandon (`Started Checkout`, "*the highest* intent flow") — "most of you think
it's just one flow, but it's actually two flows" (cart-checkout-abandon.md §O que
é, bruto L2629-2631, L3783, L3789). O produto tem um `flow_type` só, com oito
toques; ver "Onde a origem cala".

**O flow remove fricção; não persuade.** A regra dele: "these users are one or
two clicks away — so every email should reduce friction, provide assurance, and
make buying feel easy" (§O racional dele, bruto L3794). O primeiro toque é só o
item e o botão; ajuda e prova entram devagar; o incentivo entra tarde, quando o
lembrete e a ajuda já falharam. Cada toque assume que o anterior falhou e troca o
tipo de trabalho — a mesma regra do welcome, aplicada aqui por escolha da casa.

| Toque | O que faz | Origem |
|---|---|---|
| [[abandoned_cart-1\|1]] | lembrete simples: o item, o botão, o frete | Max, e-mail 1 |
| [[abandoned_cart-2\|2]] | check-in pessoal em texto: "posso ajudar?" + dois ou três pontos de prova | Max, e-mail 2 |
| [[abandoned_cart-3\|3]] | a dúvida que trava: uma objeção, respondida com mecanismo (FAQ tem lugar aqui, não no 1) | sem origem |
| [[abandoned_cart-4\|4]] | "e se der errado?": remoção de risco | sem origem |
| [[abandoned_cart-5\|5]] | o incentivo entra, no topo, e é o e-mail inteiro | Max, e-mail 3 |
| [[abandoned_cart-6\|6]] | last chance em texto: o incentivo vence, com hora; PS de suporte | Max, e-mail 4 |
| [[abandoned_cart-7\|7]] | o sino: mesmo dia, só a hora | sem origem |
| [[abandoned_cart-8\|8]] | epílogo humano: extensão declarada, única e final; canal aberto | sem origem |

**A ordem dos quatro do Max é preservada; a posição absoluta, não.** Ele dá
lembrete → texto pessoal → desconto → last chance em quatro posições (§A
sequência, bruto L3798-3881); aqui os mesmos quatro ocupam 1, 2, 5 e 6, e as
outras quatro posições são escolha desta intenção.

**A voz é de uma pessoa.** "I always recommend coming from an actual person (…)
they wanted to keep people's names out, which is going to hurt your results most
often. But you can still do it" (§O racional dele, bruto L2941-2951). Dois dos
quatro e-mails dele são só texto, justificados sem dado: "we do this just because
it works so well. Trust me. We've tested this." (bruto L2899-2905).

# Onde a origem cala

O que abaixo está sem lastro no Max e precisa de revisão humana com mais cuidado:

- **Toques 3, 4, 7 e 8 não existem no Max.** O 3 tem lastro na casa, não nele:
  abrir carrinho abandonado com FAQ ficou defensivo e a solução foi guardar o FAQ
  para o 3º toque ([[posicao-muda-o-efeito-do-dispositivo]], "Onde já se
  manifestou"). O 4 aplica o princípio dele — "provide assurance" (bruto
  L3794) — que ele nunca transforma em e-mail. O 7 e o 8 são a doutrina de
  fechamento do welcome ([[cadencia-decide-fechamento-ou-farsa]],
  [[extensao-declarada-quatro-condicoes]]) transposta por escolha.
- **Posições 5 e 6 para os e-mails 3 e 4 dele** — escolha desta intenção. O
  desenho alternativo (Max em 1-4, casa em 5-8) foi rejeitado: quatro toques
  depois de um "last chance" fazem do last chance uma farsa.
- **Delay, filtro e saída: pendentes de decisão humana.** O Max especifica
  quatro e-mails com subject lines e quick tips e **nenhum** delay, filtro ou
  condição de saída, nos dois registros (§Gatilho, filtros e saída; §O que o
  corpus não diz: a varredura por `time delay|hour|minute|wait` na fala e no
  deck devolve zero). Não preencher por analogia com browse abandon — é a
  instrução da própria nota de origem. O vizinho, e só vizinho, é o teste
  30min × 4h do módulo de otimização, com vencedor "at least on the site
  abandoned" (bruto L8952-8962). Isto inclui a saída óbvia — pedido feito — que
  ele também não declara.
- **A hora no toque 6 é da casa.** O Max diz "last chance" e "your cart is
  expiring (and your gift)" (bruto L3798-3881), sem hora. A hora fechada é a
  regra 3 do welcome, e é o que torna o toque 7 legítimo. Se o produto não
  consegue disparar o 7 no mesmo dia do 6, o 7 não deve existir.
- **Um `flow_type`, dois gatilhos.** Qual gatilho o produto usa — cart, checkout
  ou os dois — é decisão humana. Sobre o conteúdo ser igual ou diferente, ele
  diz três coisas na mesma aula (bruto L2689-2691, L2693-2695, L3015) e o slide
  concilia: "To save time, you can use the same emails for both of these flows.
  If you have time, try to make them slightly different" (bruto L3795). Esta
  intenção escreve um conteúdo, seguindo o slide, como a nota de conflitos da
  origem recomenda (`conflitos-de-flows-abandono-de-navegacao-e-carrinho.md`,
  §cart-checkout-conteudo-igual-ou-diferente). O que muda de fato é o bloco
  dinâmico e o link de volta. Se o cart deve excluir quem já entrou no checkout,
  ele não diz (§O que o corpus não diz).
- **Valor e tipo do incentivo: da loja.** Ele manda testar — "dollar off,
  percent off, giving a free gift, giving free shipping. Test all these things
  out" (bruto L2829-2841); os exemplos ($35, 20%, "1x%") nunca viram regra
  (bruto L2871, L2923, L2911). Se a loja não tem incentivo para este flow, os
  toques 5-8 ficam sem objeto — esta intenção não escreve a variante sem
  incentivo; o flow terminaria no 4. Decisão humana.
- **A tradução para o contrato é desta intenção.** `modo`, `riscos_*`,
  `aliviadores_*`, `trabalhos_fixos` e `dimensao_alvo` são vocabulário da casa;
  o Max não fala nele. O que tem lastro é a descrição de cada e-mail, citada por
  linha nos toques.
- **Autoria:** as duas notas de origem têm `registro: [transcricao, slide]`, sem
  `outro-narrador`.

# Gatilho e cadência (o que o Max dá)

| Campo | Cart | Checkout | Origem |
|---|---|---|---|
| Gatilho | `Added to Cart` | `Started Checkout` / "checkout started" | bruto L2669, L3784; L3790, L2671 |
| Nº de e-mails | 4 | 4, mesma sequência | bruto L3798-3881 |
| Delay do 1º | pendente de decisão humana | pendente | o Max não dá |
| Delays seguintes | pendente | pendente | o Max não dá |
| Filtros | pendente | pendente | o Max não dá |
| Saída | pendente | pendente | o Max não dá |

O item volta em cima do e-mail: "for abandonments, we really want to make sure
that we have the dynamic content above the fold" (conteudo-dinamico-klaviyo.md
§O que é, bruto L2512-2514) — o motivo é ver o produto na cara ao abrir (bruto
L2516-2520). Cart e checkout usam blocos diferentes: `Split` com variável de
evento único (§Cart abandon, bruto L3885-3895) contra `Table` iterando
`event.extra.line_items` (§Checkout abandon, bruto L3901-3913). O link de volta é
a página de carrinho no cart e `checkout_url` no checkout (§A diferença
estrutural).

# Regras transversais

1. Onde há bloco dinâmico, o item e o botão ficam no topo, acima da dobra — o
   Max para os e-mails 1 e 3 dele (bruto L3798-3881); estendido aos toques 3 e 4
   por escolha desta intenção.
2. A objeção dominante do primeiro toque é operacional (frete, prazo); bloco
   defensivo — FAQ, garantia — cedo demais cria a dúvida que queria curar
   ([[carrinho-abandonado]]; [[posicao-muda-o-efeito-do-dispositivo]]).
3. O incentivo entra uma vez (toque 5), em texto real
   ([[incentivo-precisa-existir-em-texto]]), e nunca aumenta depois. Hora
   fechada existe uma vez (toque 6); o 7 só a repete no mesmo dia; o 8 honra a
   expiração e estende uma vez, declarando. O flow termina. *(Doutrina da casa,
   regras 2-6 do welcome; sem origem no Max para este flow.)*
4. Quem já iniciou o checkout ouve menos argumento e mais fricção removida
   ([[checkout-abandonado]] — procedência inferida, não validada).
5. Cada alegação — frete, garantia, prazo de troca, segurança de pagamento — é
   uma promessa operacional ([[cada-alegacao-e-uma-promessa-operacional]]).

# O que é da loja (e portanto NÃO está nestas notas)

Qual item, qual limiar de frete grátis, quais pontos de prova, qual dúvida trava
a categoria, qual garantia existe de verdade, qual incentivo e de que tipo, quem
assina.

# Camada observada

Não há `_progressao` para este flow: nenhuma estrutura catalogada em
`estruturas/abandoned_cart/`. A única observação registrada é a do FAQ movido do
1º para o 3º toque ([[posicao-muda-o-efeito-do-dispositivo]]).

---

Colisão de nome: sete `_flow.md` no vault — [[wikilink-flow-ambiguo-com-seis-flows]], decisão de código.
