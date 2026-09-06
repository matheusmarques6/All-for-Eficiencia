---
tipo: procedimento
modulo: deliverability
assunto: warming-casos-reais
autor: max-sturtevant
registro: [transcricao]
fonte: "CONTEUDO BRUTO/max.md — L8607-8639 (transcrição). Sem contraparte de slide."
conflitos: [deliverability-caso-mailchimp-escala-final, deliverability-salto-de-45]
status: rascunho
---

> **Registro único e números que não fecham.** Os dois casos existem só na fala
> — o deck de warming nunca foi exportado (ver [[warming-do-dominio]]). São
> narrados de memória, e vários volumes se contradizem dentro do próprio relato.
> **Usar como ilustração de método, nunca como benchmark de volume.**
> O procedimento está em [[warming-do-dominio]].

# Caso 1 — migração de MailChimp (L8607-8622)

Havia dado de email, mas fora do Klaviyo: exportaram as listas de 30, 60 e 90
dias engajados (L8608-8609). Mesmo com o dado, tratam como conta nova
(L8612-8613): "even if you have that data, it's still different platform.
Klaviyo is new, it's a new domain, that's just how it works. So you always end
up somewhat starting from scratch."

O método foi **amostra aleatória** dentro do 30 dias engajados, não a lista
inteira — a lista importada tinha ~100.000 pessoas (L8611).

| Envio | Volume | Open rate |
|---|---|---|
| 1 | "a random sample of those thousand people" | **46.22%** — "Not the greatest, but not bad either" (L8613-8614) |
| 2 | "2,000 people in a random sample" | **53%** (L8615) |
| 3 | "about 4,000 people" | **50%** (L8616) |
| 4-6 | "6,000 and then 8,000, then 12,000" — "We stayed consistent here a little bit just to make sure we were good in this range" | *(não informado)* |
| seguintes | "14,000, 20,000, 30,000, 40,000, 60,000, 80,000, all the way up to about 100,000" (L8619) | *(não informado)* |

Marcos declarados: por volta do nono envio, ~14.000 (L8610); ao fim da janela de
60 dias, "about 120,000 people per [send]" (L8611). Note que 120.000 é maior que
os ~100.000 de teto citados em L8619 — o corpus não reconcilia.

A leitura pela ótica do provedor, e a demonstração de que só o número importa
(L8621-8622):

> Cause all Google sees here is, you know, this got sent out to 40,000, 14,000
> people and 7,000 people opened it. Okay, cool. How many people clicked on it?
> 205. All right, cool. It doesn't look like it's spam.

*(O "40,000, 14,000" é gagueira de ASR: 7.000 sobre 14.000 fecha 50%.)*

# Caso 2 — zero dado, pré-lançamento (L8623-8639)

"This one we had no email data whatsoever" (L8624). O que existia: listas
antigas de fãs de uma marca irmã e uma waitlist anterior ao drop
(L8624-8625). Os emails de warming foram **todos text-based**, em lotes
pequenos, "so we can monitor what our open rates were" (L8625).

| Envio | Volume | Abertura |
|---|---|---|
| 1 | "about 200 people or so" | "a hundred people open it" (L8626) |
| 2 | *(não informado)* | "175 people open it" (L8627) |
| 3 | "in like the 600 total [sends] mark" | *(não informado)* (L8627) |
| 4-5 | "right around 1,300, 1,400, and then boom to like 1,600" | *(não informado)* (L8628) |
| seguintes | "probably like 10,000, and then 12,000, 15,000" (L8630) | *(não informado)* |
| — | 30 dias engajados + outra lista de amostra → "about 26,000" (L8630-8631) | *(não informado)* |
| — | "all the active people, which was about 45" — **unidade ausente no corpus** | "our open rates clearly dropped a bit here" (L8631-8632) |

O salto para "all the active people" é explicitamente chamado de erro assumido:
"that was a steep jump (…) alright, shit, we gotta reel this one in" (L8631-8632).
E é justificado pelo contexto: "This is when they were doing the launch, so
sometimes you're gonna have to take these sorts of risks" (L8634).

**A autocrítica**, verbatim (L8635):

> in the beginning, we were just saying, like, heads up, you know, like, a
> launch is coming, we actually weren't even including any CTAs, which was a bad
> idea on our end.

A correção foi apontar todo mundo para um CTA único e gamificado (L8636-8638):
conteúdo de bastidor no Instagram ("Give us a follow there"), e um giveaway —
"One person who guesses what the first flavor is going to be, we attach it to a
form. Click here, vote, and then the winner is going to get a free $3 gift
card." *(A linha seguinte repete a frase corrompida; o valor de $3 aparece uma
vez só.)*

O fecho (L8639): "they want people to open it, they want them to click it, and
that's where the quality of the content becomes very important as well."

