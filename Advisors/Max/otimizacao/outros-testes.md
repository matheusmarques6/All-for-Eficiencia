---
tipo: especificacao
modulo: otimizacao
assunto: catalogo-de-testes-restantes
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L8972-9094 (transcrição), L9182-9209 (slide)"
conflitos: [otimizacao-lista-redundante, otimizacao-grafico-numero-de-variantes, otimizacao-from-name-testar-ou-prescrever, otimizacao-deck-duplicado]
status: rascunho
---

# O que é

A lista de fechamento, "Other High-Impact A/B Tests to Run" (L9182). Ele
atravessa tudo depressa — "I will run through all of these pretty quickly"
(L8972-8974) — e nenhum item aqui vem com caso, número ou vencedor. São 13
itens (contagem dos bullets; o corpus não numera).

# Os 13

| Teste (verbatim do slide) | O que compara | Alavanca declarada |
|---|---|---|
| Show Product Prices vs. Hide Them (L9184) | preço visível no email vs escondido | "Showing the price sets expectations early. Hiding it may drive curiosity and clicks. Measure both CTR and conversion rate." (L9185) |
| Graphic vs. Plain Text vs. Branded Plain Text (L9186) | as três vias de formato | "The email format impacts how trustworthy and engaging it feels." (L9187) |
| Clear Discount vs. Mystery Discount (L9188) | "10, 20% off" vs "mystery discount" (L8996) | "Clarity removes friction, but mystery can tap into curiosity and boost urgency." (L9189) |
| Lifestyle Imagery vs. Product Imagery (L9190) | pessoa usando o produto vs produto isolado | "Lifestyle photos may create a stronger desire to purchase, but sometimes simple visuals outperform." (L9191) |
| Long-Form vs. Short-Form Emails (L9192) | quantidade de seções do email | "Different products and audiences respond to different formats. Find the ideal balance of info and brevity." (L9193) |
| Send Time and Day of Week (L9194) | horário e dia da semana | "Use data to uncover hidden timing windows that improve open and click rates." (L9195) |
| CTA Link Placement (L9196) | quantidade e posição dos botões | "Different subscribers scroll and consume content differently." (L9197) |
| Subject Line Framing: Curiosity vs. Clarity (L9198) | curiosidade vs clareza na SL | "Curiosity may boost opens. Clarity may increase conversions." (L9199) |
| From Name and Sender Identity (L9200) | nome do remetente | "Sender identity impacts trust and open rates. The right sender name might boost both engagement and deliverability." (L9201) |
| CTA Text (L9202) | copy dentro do botão | "Some CTAs push urgency, others are more inviting. Small changes can mean big results." (L9203) |
| Visual Format: GIF vs. Static Image (L9204) | GIF vs imagem estática | "GIFs can attract attention but may also slow load times." (L9205) |
| Personalization Depth (L9206) | profundidade da personalização | "sometimes they're ignored or seem gimmicky. Test if it truly improves engagement." (L9207) |
| Email Length: Short vs. Long-Form (L9208) | comprimento do email | "Short emails may drive faster clicks. Longer emails may convert better after building more context." (L9209) |

# O que a fala acrescenta

**Preço.** Nasce com autocorreção: "showing products or figuring out whether you
want to hide them or not. Um, uh, showing the prices, sorry, not the products"
(L8974-8976). Mede-se CTR e conversão (L8978-8980).

**Branded plain text** é a terceira via, e só a fala diz o que é:
"it's still a Klaviyo template where it's not just a straight text base, but you
also include like the brand name up there, maybe the footers, but it's still
text-based as well. Put together using the Klaviyo blocks." (L8984-8988) Ver
[[grafico-vs-texto]].

**Mystery discount** vem do pop-up: "This is something we tried on the pop-ups a
lot" (L8994) — ver [[list-growth/_index]].

**Long vs short form** se testa mexendo em seções (L9010-9016): o padrão é "hero
section, bridge section, then product section"; as variantes são tirar o bridge
("just a hero section going straight to the products") ou ficar só com o hero,
sem produtos. O só-hero tem uso declarado — "really good for, for last chance
reminders on a sale (…) Hey, this sales ending in 12 hours, get yours"
(L9016-9020). O deck de flows dá a este mesmo teste um racional que não existe
nesta faixa: "especially in flows like abandonments when people have objections.
Sometimes it makes sense to be quick and get an impulse purchase, other times it
makes sense to spend time working through objections" (L4149-4151).

**Dia da semana** se resolve por exportação, não por A/B: "you can always export
all the data from Klaviyo (…) placed order, average placed order and break
things down by day" (L9034-9036).

**CTA.** O piso é fixo — "you should always have one in the hero" (L9040-9042) —
e o que se testa é a seção de produto: quatro produtos com um CTA no fim contra
quatro produtos com um "shop now" sob cada (L9042-9046).

**GIF.** Uso citado, apparel: frente, costas e alguém vestindo num só GIF; "It
saves space and makes it a bit more dynamic (…) and interactive as well"
(L9064-9068). O custo de load time só aparece no slide.

**Personalização** é first name na SL, no preview text ou na primeira linha:
"Hey, Michael, Hey, Max, Hey, Alex, um, we noticed that you" (L9072-9074).

**Comprimento**, por analogia com conteúdo (L9086-9092): short form para
"getting that, that initial dopamine, getting people kind of hooked"; long form
para quando "you're explaining something a bit more in depth".

# Onde o corpus discorda

- Long-Form vs. Short-Form (L9192) e Email Length: Short vs. Long-Form (L9208)
  são o mesmo par, listados duas vezes com racionais diferentes; Send Time
  aparece como teste de topo (L9143) e de novo aqui (L9194):
  `otimizacao-lista-redundante`.
- Gráfico vs texto é de duas vias no topo (L9151) e de três aqui (L9186):
  `otimizacao-grafico-numero-de-variantes`.
- **From Name and Sender Identity existe só no slide** — a fala pula de
  curiosity/clarity direto para CTA text (L9052-9054). E em outros módulos o
  sender name não é campo de teste, é prescrição: "update the sender name to be
  an actual human's name" (L2413), "Update the sender name to the founders name"
  (L3661), "people should open your emails based off your sender name, NOT your
  Subject line" (L6093). `otimizacao-from-name-testar-ou-prescrever`.

# O que o corpus não diz

Nenhum destes 13 tem número, vencedor ou caso. Ele encerra citando material que
não está no corpus: "there's another document we have that outlines some of the
higher leverage AB tests with a little bit more info on it as well"
(L9094-9096).
