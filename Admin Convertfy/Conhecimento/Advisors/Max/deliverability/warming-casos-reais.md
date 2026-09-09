---
tipo: procedimento
modulo: deliverability
assunto: warming-casos-reais
autor: max-sturtevant
registro: [outro-narrador]
fonte: "CONTEUDO BRUTO/max.md — L8607-8639 (transcrição). Sem contraparte de slide."
conflitos: [deliverability-caso-mailchimp-escala-final, deliverability-salto-de-45]
validade: "procedimento — o corpus não data a gravação. Extraído em 2026-09-06. Os volumes são narrados de memória e não fecham entre si: ilustração de método, nunca benchmark."
status: aprovado
---

Dois casos narrados de aquecimento de domínio — uma migração do MailChimp com dado antigo e um pré-lançamento sem dado nenhum: volumes por envio, aberturas obtidas e os erros assumidos. Ilustração de método, não benchmark de volume.


# Aviso de autoria

**Faixa L8381-8646 (toda a fala do módulo de deliverability) — `outro-provavel`.**
Sem prova nominal. A classificação é **estilométrica**: o bloco pertence ao aglomerado
do único bloco `outro-provado` e não traz um só marcador do idioleto de Max.
`outro-provavel` não é `outro-provado` — não está provado que a voz não é dele, está
estabelecido que é muito improvável ([[mapa-da-autoria]] §7.3).

Critério: **idioleto** ([[mapa-da-autoria]] §2.1) — ausência de "I recommend", "my favorite"
e "I like to", presença de "at the end of the day" e "obviously", e o fecho coletivo
"thank you guys… see you in the next one". **A saudação de abertura não é critério e
não pode ser citada como evidência:** o laudo testou e ela caiu — o walkthrough de
Figma abre com "Hello, hello" e é comprovadamente Max, que em L7817 digita `@max` e
diz "tags me" ([[mapa-da-autoria]] §5).

Nesta nota **não sobra nada de Max**: os dois casos são fala (L8607-8639), dentro
da faixa não-Max, sem contraparte de slide. Os volumes, as aberturas e a
autocrítica sobre os CTAs são **da agência narrada no material**, não relatos
pessoais citáveis como dele. Já valia a regra de não usar como benchmark; agora
também não se usa como experiência dele.

> **Registro único e números que não fecham.** Os dois casos existem só na fala
> — o deck de warming nunca foi exportado (ver [[evidencia-e-lacunas-do-warming-do-dominio]]). São
> narrados de memória, e vários volumes se contradizem dentro do próprio relato.
> **Usar como ilustração de método, nunca como benchmark de volume.**
> O procedimento está em [[preparacao-para-o-warming-do-dominio]] e [[rampa-de-warming-do-dominio]].

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
60 dias, "about 120,000 people per [send]" (L8611). Esse 120.000 não fecha por
**dois** lados, ambos na mesma linha ou logo adiante: é maior que a lista
importada inteira — "it was, you know, a hundred thousand people" (L8611) — e
maior que o topo declarado na mesma narração para a escala, "all the way up to
about 100,000" (L8619). Enviar 120.000 por campanha a partir de uma lista de 100.000 é
impossível. O corpus não reconcilia.

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
card." *(A própria L8638 repete a frase logo em seguida, corrompida — "Click
here, vote, and winner is going get a free $3 engagement". O valor **$3 aparece
duas vezes na linha**, nas duas versões; é o único número do trecho com
repetição própria, o que o torna menos suspeito de erro de ASR do que parece.)*

O fecho (L8639): "they want people to open it, they want them to click it, and
that's where the quality of the content becomes very important as well."

