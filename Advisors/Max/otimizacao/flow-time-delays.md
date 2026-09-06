---
tipo: especificacao
modulo: otimizacao
assunto: time-delay-de-flow
autor: max-sturtevant
registro: [slide, outro-narrador]
fonte: "CONTEUDO BRUTO/max.md — L8946-8970 (transcrição), L9176-9180 (slide)"
conflitos: [otimizacao-onde-testar, otimizacao-metricas-do-print, otimizacao-deck-duplicado]
status: rascunho
---


# Aviso de autoria

**Faixa L8773-9109 (toda a fala do módulo de otimização) — `outro-provavel`.**
Sem prova nominal. A classificação é **estilométrica**: o bloco pertence ao aglomerado
do único bloco `outro-provado` e não traz um só marcador do idioleto de Max.
`outro-provavel` não é `outro-provado` — não está provado que a voz não é dele, está
estabelecido que é muito improvável ([[_autoria]] §7.3).

Critério: **idioleto** ([[_autoria]] §2.1) — ausência de "I recommend", "my favorite"
e "I like to", presença de "at the end of the day" e "obviously", e o fecho coletivo
"thank you guys… see you in the next one". **A saudação de abertura não é critério e
não pode ser citada como evidência:** o laudo testou e ela caiu — o walkthrough de
Figma abre com "Hello, hello" e é comprovadamente Max, que em L7817 digita `@max` e
diz "tags me" ([[_autoria]] §5).

Nesta nota: o bloco de slide (L9178-9180, repetido verbatim no deck de flows em
L4141-4145) é artefato de Max — inclusive a frase "This is the biggest lever I'd
say". O caso real 30min × 4h, os números lidos do print ausente e a ressalva sobre
welcome e post-purchase (L8946-8970) vêm da faixa não-Max e **não são citáveis
como fala dele**.

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
(L8948-8950) — cart abandoned aparece duas vezes, provável tropeço de fala.
A formulação do teste: "after someone abandons their cart, do we send the first
email to them after 30 minutes or do we send it four hours later?" (L8952-8954).

# O caso real

30 minutos contra 4 horas. Antes do resultado, o aviso, na aula, de que não há vencedor
universal: "we've seen different results on, um, on both just depending on the
brand and the, and the audience that we're sending to" (L8954-8956).

| Métrica | Resultado | Linha |
|---|---|---|
| vencedor | 4 horas, "at least on the site abandoned" | L8956-8958 |
| placed order rate | "a 10 to 15% higher placed order rate" | L8958 |
| receita | "about a thousand dollars in extra revenue" | L8960 |
| click rate | "slightly higher on, on the 30 minutes, but, uh, marginal at best" | L8962 |

A hesitação está no meio da leitura — "I don't know the exact math off the top of
my head" (L8958-8960) — e o print, como em todos os casos deste módulo, não está
no corpus. A hesitação é do narrador da aula, não de Max.

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
