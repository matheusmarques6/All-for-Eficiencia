---
tipo: especificacao
modulo: otimizacao
assunto: time-delay-de-flow
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L8946-8970 (transcrição), L9176-9180 (slide)"
conflitos: [otimizacao-onde-testar, otimizacao-metricas-do-print, otimizacao-deck-duplicado]
status: rascunho
---

# O que compara

Tempo. Duas coisas, segundo o slide (L9178-9180), verbatim:

> This is the biggest lever I'd say.
> Testing the amount of time from the action of the customer and the first email
> they receive.
> Then also, the time delay between your flow messages.

Na fala: "This is one of the biggest lever and it's very, very simple,
especially in your abandonment flows" (L8946-8948). É o teste de maior alavanca
declarada do módulo — ver [[_index]].

O mesmo bloco de slide aparece uma segunda vez no corpus, idêntico, dentro do
deck de flows (L4141-4145).

# Onde aplicar

Nos flows de abandono: "think site abandoned, cart abandoned, browse abandoned,
checkout abandoned, cart abandoned, um, the time delays in the flow"
(L8948-8950) — ele repete cart abandoned duas vezes, provável tropeço de fala.
A formulação do teste: "after someone abandons their cart, do we send the first
email to them after 30 minutes or do we send it four hours later?" (L8952-8954).

# O caso real

30 minutos contra 4 horas. Antes do resultado, o aviso de que não há vencedor
universal: "we've seen different results on, um, on both just depending on the
brand and the, and the audience that we're sending to" (L8954-8956).

| Métrica | Resultado | Linha |
|---|---|---|
| vencedor | 4 horas, "at least on the site abandoned" | L8956-8958 |
| placed order rate | "a 10 to 15% higher placed order rate" | L8958 |
| receita | "about a thousand dollars in extra revenue" | L8960 |
| click rate | "slightly higher on, on the 30 minutes, but, uh, marginal at best" | L8962 |

A hesitação dele está no meio da leitura — "I don't know the exact math off the
top of my head" (L8958-8960) — e o print, como em todos os casos deste módulo,
não está no corpus.

# A ressalva dura

Nem todo flow entra no teste (L8966-8970), verbatim:

> I wouldn't, you can test it out in like the welcome flow as well, or post
> purchase, but at least for those email ones, you're want to going to want to
> deliver those instantly if it's, uh, if it's post purchase or if it's welcome
> flow for sure.

Ou seja: welcome e post-purchase saem instantaneamente, e o delay do primeiro
email deles não é campo de teste. Isso bate com a non-negotiable do welcome
("First email fires immediately upon sign-up") — ver [[flows/_index]]. O campo
livre é o abandono: "site abandoned tons of room to try different things out,
see how different people respond as well" (L8970-8972).

# Onde o corpus discorda

O deck de flows guarda este mesmo slide, mas a estratégia declarada logo acima
dele é não testar em flow: "Rather than have a ton of active tests in flows (…)
We mostly use campaigns as our testing ground (…) Rather than waiting for
results like you have to do in flows, you can get near instant data with
campaigns" (L4128-4131). A maior alavanca do módulo está, portanto, no lugar que
o outro registro desaconselha como campo de teste:
`otimizacao-onde-testar`.

# O que o corpus não diz

Nenhum outro par de delay é citado — só 30 minutos e 4 horas, e só em site
abandon. Não há nada sobre o delay entre o email 2 e o 3 apesar de o slide
mandar testar isso (L9180), nem sobre quanto tempo esperar para ler o resultado
de um teste dentro de flow, onde o volume chega devagar.
