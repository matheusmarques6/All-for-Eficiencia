---
tipo: especificacao
modulo: design
assunto: secao-product
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L7446-7496 (transcrição), L8274-8290 (slide)"
conflitos: [design-cta-por-produto, design-quantidade-de-produtos, design-bridge-e-product-opcionais]
status: aprovado
---

# O que é

A parte do email que destaca um produto ou vários. Opcional (L7238; L8229 diz
"most will").

> Products can even be categories, not necessarily specific products. (L8277)

Na fala: "you could do categories. This could be a category section. So shop by
meat or shop by shop hoodies versus shop t-shirts" (L7448-7452). O primeiro
exemplo pode ser erro de transcrição; hoodies vs t-shirts é o exemplo utilizável.

# As duas regras duras

**1. CTA individual por produto**

> Every single product we showed needs to have its own button. (L7458, verbatim)

O motivo: não dá para esperar que a pessoa saiba que a imagem é clicável
(L7460). E o resultado de teste: "Every single time I test this if you let
people know shop now say hey you can shop now right here then it gets higher
clicks" (L7462). Remove atrito porque poupa o cliente de ir ao site geral e
procurar (L7464).

O slide é mais frouxo — abre uma alternativa que a fala não abre:

> Make it clear by giving individual buttons or underlines product titles.
> (L8282, verbatim)

→ `design-cta-por-produto`. Sublinhar o título do produto é a única alternativa ao
botão em todo o módulo.

**2. Sempre terminar com CTA geral**

> After you give individual products, it's important to always have a general
> CTA below. Maybe the customer is interested, but didn't like any of the
> products in the email. By leaving out a general CTA below, you lose out on all
> these customers. We've noticed 25% boosts in clicks by doing this.
> (L8286-8287, verbatim)

A fala traz o mesmo número: "We've noticed literally 25% boosts and clicks by
including this in some of our emails" (L7482). Note o "in some of our emails" —
a fala qualifica, o slide não.

O cenário que ele descreve para justificar (L7101-7115, L7474-7480): o cliente
está aberto a comprar, mas já tem algo parecido com o que você mostrou; sem botão
geral ele simplesmente sai.

# Um terceiro requisito, só na fala

> Obviously we want to have an image to our product as well. (L7472)

Imagem do produto não aparece no checklist do slide. Vem junto com nome do
produto e botão no formato mínimo que ele descreve para um produto só (L7490).

# Onde o corpus discorda: quantos produtos

Cinco respostas na mesma fala, em oito linhas:

| Versão | Verbatim | Linha |
|---|---|---|
| livre | "You can feature however many products that you want." | L7486 |
| poucos | "Ideally not that many." | L7488 |
| um | "You can have a product section be just one product as well" | L7490 |
| oito | "You can have eight products if you want." | L7492 |
| testar | "Just test it." | L7494 |

O slide não dá número nenhum. → `design-quantidade-de-produtos`. O critério final
que ele oferece é o teste, não um número — ver [[mapa-de-otimizacao]].

# A fórmula de fecho

> So always include with the general section general button and have individual
> shop now buttons for products that you feature. (L7484)

E, na versão mínima: cada produto com seu botão, e um botão geral no fim
(L7496).

# O que o corpus não diz

Layout da grade (quantos por linha), se produto tem preço, se tem desconto, como
ordenar os produtos, ou o que a "underline" do título deve parecer. O deck
promete "Optimized Product Section Example:" (L8289) e não mostra nenhum — a
linha seguinte já é `# **Footer**`. Nota de inventário: **este rótulo e o
"Great Examples That Follow Best Practices" (L8143) faltavam na contagem de
legendas vazias de GAMMA DESIGN** de [[descartes-cta-comercial-e-placeholders]] e [[lacunas-por-falha-tecnica-e-entrega-errada]], que diziam 13.
São 15. Corrigido lá.

Ver [[secao-footer]] — o footer repete a lógica do catch-all com botões de
categoria.
