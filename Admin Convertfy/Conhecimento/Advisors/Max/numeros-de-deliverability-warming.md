---
tipo: indice
modulo: deliverability
assunto: numeros-de-deliverability-warming
autor: max-sturtevant
registro: [slide, outro-narrador]
fonte: "CONTEUDO BRUTO/max.md — L8365-8646 (transcrição), L8647-8759 (slide GAMMA)"
status: aprovado
---

A rampa de aquecimento de domínio em números: volume de cada degrau, cadência,
faixa de tolerância, limiares para escalar ou recuar, batching, os parâmetros
de reparo de reputação e os dois casos reais de warming contados na fala, com
todos os volumes e taxas. Verbatim, com registro e linha; toda a fala do módulo
é `outro-narrador`. Metas e diagnóstico em
[[numeros-de-deliverability-metas-e-diagnostico]]. Índice da série:
[[mapa-dos-numeros-por-modulo]].

A faixa do módulo é L8365-8646 (transcrição) e L8647-8759 (slide GAMMA).

## Warming — rampa e cadência

| Medida | Valor verbatim | Registro | Linha | Conflito |
|---|---|---|---|---|
| Primeiro envio | `"maybe a hundred people, two hundred people, three hundred people, somewhere in that range"` | outro-narrador | L8569 | deliverability-primeiro-degrau-da-rampa |
| Cadência de rampa — degrau 1 | `"one to 200,000"` — **corrompido** | outro-narrador | L8587 | deliverability-primeiro-degrau-da-rampa |
| Cadência de rampa — degraus 2 a 8 | `"send two, going to maybe like 300 (…) send three, 500, send four, a thousand, send five, 2,000, then 4,000, then 6,000, 6,000"` | outro-narrador | L8588 | deliverability-primeiro-degrau-da-rampa |
| Passo de escalonamento (fala) | `"you scale up by about fifty to, by about fifty percent each send"` | outro-narrador | L8569 | deliverability-passo-de-escalonamento |
| " " (lendo o bullet do deck) | `"gradually increase from 25 to 50 percent percent based on performance"` | outro-narrador | L8556 | deliverability-passo-de-escalonamento |
| Limiar para continuar escalando | `"as long as you're hitting those, those 40 to 50% open rates"` | outro-narrador | L8588 | deliverability-limiar-de-open-rate |
| Frequência durante warming | `"ideally 3 to 4 times per week"` | outro-narrador | L8557 | campanhas-sweet-spot-de-frequencia |
| Racional de frequência | `"if you only send 2 times per week opposed to 4 times per week (…) twice as long"` | outro-narrador | L8561 | — |
| Teto de frequência | `"that doesn't mean send [—] emails in 7 days"` — **número perdido no ASR** | outro-narrador | L8560 | — |
| Batching — volume | `"let's say you're sending to 6,000 people"` | outro-narrador | L8585 | — |
| Batching — divisão | `"a thousand at noon, a thousand at one, two, a thousand at three, four, five, six"` | outro-narrador | L8585 | — |
| Fase de fundação | `"weeks 1 to 3"` | outro-narrador | L8578 | — |
| Segmentos a criar na fundação | `"7 day, 14, 30, 60, 90 day engage list"` | outro-narrador | L8578 | — |
| Regra de ouro | `"ideally 50 plus open rates and then you know you're good to jump to a wider segment"` | outro-narrador | L8579 | deliverability-limiar-de-open-rate |
| Faixa de tolerância | `"anywhere between 40 to 50 percent. If it starts dipping below 40, I definitely wouldn't be expanding it"` | outro-narrador | L8580 | deliverability-limiar-de-open-rate |
| Fase de expansão | `"weeks 3 to 12"` | outro-narrador | L8580 | — |
| Primeiro degrau de expansão | `"So in weeks, you know, 3 to 4, maybe you start sending to the 14 day engage list and then you want to expand it to the 30 day engage list"` | outro-narrador | L8581 | — |
| Limiar para expandir 14 → 30 | `"you're hitting, again, 45 to 50% plus"` | outro-narrador | L8582 | deliverability-limiar-de-open-rate |
| Degraus seguintes | `"Same logic from 30 to 60 (…) then maybe after a couple weeks, you expand to the 90 day"` | outro-narrador | L8583 | — |
| Segmentos-semente (email) | `"opened three times in the last thirty days"` · `"opened five times in the last sixty days"` · `"opened an email once or twice in the last week"` · `"clicked an email in the last week"` | outro-narrador | L8564-8565 | — |
| Segmento pequeno demais | `"seventy-eight people in there, which isn't really going to move the needle"` | outro-narrador | L8567 | — |
| Segmentos-semente (Shopify) | `"viewed a product in the last three days, placed an order in the last week, and started checkout in the last week"` | outro-narrador | L8574 | — |
| Onde colocar o código de desconto | `"welcome email 1, 2, 3, 4"` (nunca no form) | outro-narrador | L8548 | — |
| Correção de rota — queda | `"from your 30 day engage list to your 60 day (…) open rates go from 50% to 25%"` | outro-narrador | L8601 | — |
| Correção de rota — passo menor | `"Maybe instead of going from 30 to 60, we go from 50 from 30 to 45 day engage. And that keeps us at a 40 to 50% mark"` *(`from 50` é gagueira de ASR)* | outro-narrador | L8604 | deliverability-limiar-de-open-rate |

## Reparo de reputação

| Medida | Valor verbatim | Registro | Linha | Conflito |
|---|---|---|---|---|
| Listas em uso quando a conta cai em spam | `"you're sending to, you know, 90, 120 day engage list"` | outro-narrador | L8589 | — |
| Janela de reparo | `"anywhere between 2 to 3 weeks to start"` | outro-narrador | L8591 | — |
| Segmentos de reparo | `"7 day engage, 14 day engage, 30 day engage"` | outro-narrador | L8591 | — |
| Parâmetro extra | `"people that have opened 2 times, 3 times in the last 14 days"` | outro-narrador | L8591-8592 | — |
| Alvo de abertura no reparo | `"once you hit those 60% open rates, 60, 70, 80"` | outro-narrador | L8592 | — |

## Casos reais de warming

**Caso 1 — migração de MailChimp (L8607-8622).** Listas exportadas `"60 day
engage, 90 day engage. 30 day engage list"` · lista importada `"a hundred
thousand people"` · primeiro envio `"a thousand people"` · nono envio `"roughly
14,000"` · fim da janela de 60 dias `"about 120,000 people per [send]"` ·
amostras `"a random sample of those thousand people (…) get a 46.22% open
rate"`, `"2,000 people in a random sample (…) 53%"`, `"about 4,000 people, 50%"`
· degraus `"6,000 and then 8,000, then 12,000"` · degrau corrompido `"And then
we go up to 4,000. 14,000."` · escala final `"14,000, 20,000, 30,000, 40,000,
60,000, 80,000, all the way up to about 100,000"` · leitura do Google `"this got
sent out to 40,000, 14,000 people"` (dois números para o mesmo envio),
`"7,000 people opened it"`, `"How many people clicked on it? 205"`.
Registro: `outro-narrador`. Conflito: `deliverability-caso-mailchimp-escala-final`.

**Caso 2 — zero dado, pré-lançamento (L8623-8639).** Envio 1 `"about 200 people
or so"` com `"a hundred people open it"` · envio 2 `"175 people open it"` ·
marco `"the 600 total [sends] mark"` · degraus `"right around 1,300, 1,400, and
then boom to like 1,600"`, depois `"probably like 10,000, and then 12,000,
15,000"` · 30 dias engajados + amostra `"which took us to about 26,000"` · salto
final `"we sent to all the active people, which was about 45"` — **unidade
ausente** (`deliverability-salto-de-45`) · prêmio do giveaway `"a free $3 gift
card"`. Registro: `outro-narrador`.

