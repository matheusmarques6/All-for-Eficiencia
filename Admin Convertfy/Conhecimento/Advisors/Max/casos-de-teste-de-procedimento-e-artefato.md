---
tipo: indice
assunto: casos-de-teste
autor: max-sturtevant
status: aprovado
---

Casos de regressão do advisor Max para conteúdo que envelhece ou que não pode ser traduzido: procedimento datado de ferramenta e artefato que só vale verbatim, como subject line. Dois casos (C-13 e C-14), cada um com a pergunta como um usuário real faria, os elementos obrigatórios da resposta certa, o erro típico e a peça do corpus que a falha acusa.

# Casos de procedimento e artefato — C-13 e C-14


## C-13 · Procedimento datado — o upload que não é do Klaviyo

**Pergunta:** Como eu subo meu design do Figma para o Klaviyo?

**Resposta certa contém:** o aviso **antes** dos passos, não depois. A seção se
chama `"Uploading Designs From Figma To Klaviyo"` (L8009) e lista cinco passos
(L8011-8015), sendo o quarto `"Upload your sections as images into Klaviyo"`.
**A demonstração inteira é feita no Omnisend.** Ele anuncia a troca:
`"for this video, um, I'm going to do to use Omnisend (…) You get a 30%, uh,
discount if you use me"` (L8044), diz `"I'll say well copy because that's my
company's name"` (L8046) e fecha com o link de afiliado (L8063). Não há um único
passo executado em Klaviyo.

A resposta também carrega: (a) o carimbo de validade — o corpus não declara data
de gravação em lugar nenhum, e a âncora interna mais recente é `Nov 13, 2024` no
print da L9545; (b) o alt text como passo obrigatório, com o motivo dado ao
vivo — `"if an image doesn't load for someone, it'll show this alt text"` e
`"alt text is just good practice to have and it helps with some deliverability"`
(L8052-8053).

**Resposta errada típica:** listar os cinco passos como se fossem passos de
Klaviyo. Ou dar o aviso no fim, quando o usuário já leu a receita.

**Se errar, quebrou:** regra 4 do [[_protocolo]] (procedimento é datado e diz
qual ferramenta foi demonstrada de fato), [[_cobertura]] (§ "entregue errado") e
[[_conflitos]] (`design-klaviyo-vs-omnisend`).

## C-14 · Artefato verbatim — subject line não se traduz

**Pergunta:** Me dá umas subject lines para o cart abandon.

**Resposta certa contém:** as linhas do deck, **em inglês, sem uma palavra
mudada**. Email 1 (L3806-3810): `"Your order is ready to ship"` · `"One click
away!"` · `"Your cart is waiting"`. Email 2 (L3827-3831): `"Quick check-in"` ·
`"Holding onto your order"` · `"Have any questions with your order?"` A fala
repete as mesmas ideias — `"your order's ready to ship, one click away, your card
is waiting"` (L2737, onde o ASR escreve "card") e `"quick check-in, holding on to
your order, have any questions with the order"` (L2771). A resposta pode
acrescentar a regra dele: `"you don't need to get too cute with your subject lines
and preview text"` (L2849).

**Resposta errada típica:** entregar "Seu pedido está pronto para envio", "A um
clique de distância", "Seu carrinho está esperando". Traduzida, deixa de ser a
subject line dele. Variante igualmente errada: inventar seis subject lines novas
no mesmo espírito.

**Se errar, quebrou:** regra 3 do [[_protocolo]] e a convenção `tipo: artefato`
do [[_INDEX]] ("verbatim, em inglês, nunca traduzir").

---

