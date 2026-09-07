---
tipo: principio
modulo: design
assunto: ease-of-click
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L7123-7153 (transcrição), L8145-8179 (slide)"
conflitos: [design-botao-above-the-fold-sempre]
status: aprovado
---

# O que é

Princípio nº 1 dos três. Parte de um modelo de leitor específico:

> When customers are opening emails they are in zombie mode.
> Any friction in the ability for someone to click will automatically lead to
> churn.
> We need to hand the click to them on a silver platter with the following:
> (L8147-8149, verbatim)

A fala é idêntica em conteúdo (L7123-7127). "Zombie mode" e "silver platter" são
os dois termos que ele usa para a mesma ideia: o clique tem de ser entregue, não
procurado.

# Os quatro itens

**✅ Button Above the Fold** (L8151-8156) — above the fold é "the section of the
email that is viewed without scrolling". Nem todo cliente rola, então o botão
tem de estar na hero. "Including a top button is an easy low-hanging fruit to
automatically improve your click rates" (L8156).

**✅ Large Buttons** (L8158-8161) — a régua física está só no slide:

> An iPhone screen is 2.75 inches. That's not a large space.
> Larger buttons, more surface area, easier ability to click. This has a massive
> impact on conversions. (L8160-8161, verbatim)

Cruze com a especificação de [[o-email-tem-um-trabalho-so]]: botão de 1.5-2
polegadas de largura numa tela de 2.75 polegadas — mais da metade da largura da
tela. Na fala, o teste: "I've never had a bigger button lose an A-B test in
click rates" (L7041-7043).

**✅ Clear Calls to Action** (L8163-8166) — "Your buttons should be the easiest to
view part of your email and there should be no ability for someone to click over
a button." Evitar fundo que distrai, usar cor contrastante. Na fala, o exemplo
negativo é cor genérica: "You don't want to use like a blue button here"
(L7045-7047).

**✅ Centered Main Buttons** (L8168-8171) — aqui o slide dá o mecanismo que a fala
não dá:

> Most people hold their phone in their right hand.
> If you put a button on the left side, the user has to stretch their thumb over
> to click (more friction). This actually negatively impacts conversions
> substantially. (L8170-8171, verbatim)

A fala só afirma o efeito ("Centered buttons reduce friction and boost taps",
L7067-7069) e é onde estão as exceções — imagem com o sujeito à direita, seções
de produto em zigue-zague (L7071-7081).

# O resumo dele

> Large, clear buttons above the fold that are ideally centered. (L7139)

Quatro atributos numa frase: grande, claro, acima da dobra, idealmente
centralizado. "Ideally" é dele.

# O contra-exemplo nominal

Nike. É a única marca que ele cita pelo nome como erro de design nesta seção:

> And then we have an uncentered small button right here, which is pretty much
> below the fold for Nike. It is like if you open this on your phone. It's very
> small, this small, and it's uncentered. So ideally we don't want to do that.
> (L7149-7153)

Três defeitos no mesmo botão: descentralizado, pequeno e abaixo da dobra.

# O que o corpus não diz

O slide traz quatro legendas de exemplo — ✅ Button Above The Fold, ✅ Large
Centered Button, ❌ Unclear, Small Button, Uncentered, Small Button (L8173-L8179)
— sem nenhuma imagem no bruto. São âncoras vazias: não sustentam afirmação.
Note que a quarta perdeu o ❌ (L8179), provavelmente erro do deck.

Também não há: **valor** de cor, contraste medido, raio de canto, altura de
botão, nem o que fazer quando a marca não tem cor de contraste disponível.

**Correção de escopo (varredura de falsos negativos).** A lista acima dizia
antes "não há: cor", e isso contradiz o corpo desta própria nota. A prescrição de
cor **existe** — só é qualitativa, nunca numérica. Nos dois registros: slide,
"Use **high-contrast colors** and simple backgrounds. Your buttons should be the
most obvious thing in the email" (L8141) e "Avoid distracting backgrounds and use
**contrasting colors** to get your CTAs to stand out" (L8166); fala, o único
contra-exemplo nominal de cor, "You don't want to use like a **blue** button
here" (L7045-7047). O que falta é hex, faixa de contraste medida e regra para
marca sem cor disponível.

Ver [[principio-skimmability]] e [[principio-branding]] para os outros dois.
