---
tipo: staging
modulo: deliverability
assunto: numeros
autor: max-sturtevant
fonte: "CONTEUDO BRUTO/max.md — L8363-8646 (transcrição), L8647-8759 (slide)"
status: rascunho
---

# Números do módulo deliverability

Todo número da faixa, verbatim. **Nada arredondado, nada convertido.** Valores
entre aspas são citação literal do corpus.

## Conceito e diagnóstico

| Medida | Valor verbatim | registro | linha | conflito |
|---|---|---|---|---|
| Destinos possíveis do email | 3 — primary tab / promotions tab / spam | transcricao + slide | L8386-8388, L8659-8661 | — |
| Open rate — exemplo de mau (fala) | "20% of people are opening your emails" | transcricao | L8390 | — |
| Open rate — exemplo de bom (fala) | "50% of the people you send it to are opening" | transcricao | L8390 | — |
| Click rate — exemplo de bom (fala) | "1% of those people are clicking" | transcricao | L8390 | — |
| Eyes of Google — exemplo (slide) | "2/10 people are opening your emails" | slide | L8665 | — |
| Analogia Instagram — escadinha de likes | "1,000 likes, 10,000 likes, 50,000 likes, 100,000 likes" | transcricao | L8394 | — |
| Erro clássico — tamanho da lista | "50,000 profiles" / "send 50,000 emails to every single profile for a week" | transcricao | L8404 | — |
| Erro clássico — volume citado no warming | "you can't just start off sending to, you know, 50,000 people" | transcricao | L8552 | — |

## Metas de métrica

| Medida | Valor verbatim | registro | linha | conflito |
|---|---|---|---|---|
| Open Rates | "Greater than 50%" | slide | L8715 | deliverability-limiar-de-open-rate |
| Open rate — piso e faixa (fala) | "above 50%. 50% to 70% is ideal. If you're above 40%, you're probably okay" | transcricao | L8436 | deliverability-limiar-de-open-rate |
| Click Rates | "Greater than 0.75%" | slide | L8716 | — |
| Click rate (fala) | "Click rates, 0.75%" | transcricao | L8438 | — |
| Bounce Rate | "Less than 1%" | slide | L8717 | — |
| Bounce rate (fala) | "under 1%" / "should be less than 1%" | transcricao | L8440, L8448 | — |
| Spam Complaint Rate | "Less than 0.01%" | slide | L8718 | — |
| Unsubscribe Rate | "Less than 0.4%" (rótulo: "doesn't affect deliverability") | slide | L8719 | deliverability-unsubscribe-afeta-ou-nao |
| Nº de métricas que decidem deliverability | 5 (open, click, bounce, unsubscribe, spam complaint) | slide | L8710 | deliverability-unsubscribe-afeta-ou-nao |
| Nº de métricas na lista falada | 5, mesma ordem ("spam, complete rate" = ASR de *spam complaint rate*) | transcricao | L8430 | — |

## Segmentação

| Medida | Valor verbatim | registro | linha | conflito |
|---|---|---|---|---|
| Janelas de engaged list disponíveis | "30, 60, 90, 120, 180, or 365 day" | transcricao + slide | L8460, L8726 | — |
| Lista base recomendada | "90 is recommended to start" | slide | L8734 | deliverability-lista-base-padrao |
| Lista para envio normal | "you might only want to send to your 60 day engage list" | transcricao | L8462 | deliverability-lista-base-padrao |
| Lista para grandes datas | "180, 365 day engage list" | transcricao | L8466 | — |
| Janela da definição do segmento base | 90 days (3 condições em OR) | slide | L8734 | — |
| Faixa de acerto da lista (fala) | "consistently receiving 50 to 60% opens" | transcricao | L8468 | deliverability-limiar-de-open-rate |
| Faixa de acerto da lista (slide) | "Whatever list gets you 50-60% opens" | slide | L8727 | deliverability-limiar-de-open-rate |
| Gatilho para alargar (slide) | "If you start to get 60%+ opens, widen your list" | slide | L8728 | deliverability-limiar-de-open-rate |
| Gatilho para apertar (slide) | "If you start to get 40% opens, tighten your list" | slide | L8729 | — |
| Gatilho para apertar (fala) | "If you start to get 40% opens or things start to drop in a significant way" | transcricao | L8470 | — |
| Exemplo de queda por alargar demais | 30 dias → "65% opens"; expandiu para 120 → "goes down to 30%" | transcricao | L8472 | — |
| Destino sugerido após a queda | "Maybe 90 is a good place to go, but probably want to go back to your 60 day" | transcricao | L8474 | — |

## Warming — rampa e cadência

| Medida | Valor verbatim | registro | linha | conflito |
|---|---|---|---|---|
| Primeiro envio | "maybe a hundred people, two hundred people, three hundred people, somewhere in that range" | transcricao | L8569 | deliverability-primeiro-degrau-da-rampa |
| Passo de escalonamento (fala) | "you scale up by about fifty to, by about fifty percent each send" | transcricao | L8569 | deliverability-passo-de-escalonamento |
| Passo de escalonamento (bullet do deck, lido) | "gradually increase from 25 to 50 percent percent based on performance" | transcricao (lendo slide) | L8556 | deliverability-passo-de-escalonamento |
| Cadência de rampa — degrau 1 | "one to 200,000" — **corrompido, incoerente com os degraus seguintes** | transcricao | L8587 | deliverability-primeiro-degrau-da-rampa |
| Cadência de rampa — degraus 2 a 8 | "send two, going to maybe like 300 (…) send three, 500, send four, a thousand, send five, 2,000, then 4,000, then 6,000, 6,000" | transcricao | L8588 | deliverability-primeiro-degrau-da-rampa |
| Limiar para continuar escalando | "as long as you're hitting those, those 40 to 50% open rates" | transcricao | L8588 | deliverability-limiar-de-open-rate |
| Frequência durante warming | "ideally 3 to 4 times per week" | transcricao | L8557 | — |
| Racional de frequência | "if you only send 2 times per week opposed to 4 times per week (…) twice as long" | transcricao | L8561 | — |
| Teto de frequência | "that doesn't mean send [—] emails in 7 days" — **número perdido no ASR** | transcricao | L8560 | — |
| Batching — exemplo de volume | "let's say you're sending to 6,000 people" | transcricao | L8585 | — |
| Batching — divisão | "a thousand at noon, a thousand at one, two, a thousand at three, four, five, six" | transcricao | L8585 | — |

## Warming — cronograma e segmentos-semente

| Medida | Valor verbatim | registro | linha | conflito |
|---|---|---|---|---|
| Fase de fundação | "weeks 1 to 3" | transcricao | L8578 | — |
| Segmentos a criar na fundação | "7 day, 14, 30, 60, 90 day engage list" | transcricao | L8578 | — |
| Regra de ouro | "ideally 50 plus open rates and then you know you're good to jump to a wider segment" | transcricao | L8579 | deliverability-limiar-de-open-rate |
| Faixa de tolerância | "anywhere between 40 to 50 percent. If it starts dipping below 40, I definitely wouldn't be expanding it" | transcricao | L8580 | deliverability-limiar-de-open-rate |
| Fase de expansão | "weeks 3 to 12" | transcricao | L8580 | — |
| Primeiro degrau de expansão | "in weeks 3 to 4, maybe you start sending to the 14 day engage list and then expand it to the 30 day" | transcricao | L8581 | — |
| Limiar para expandir 14 → 30 | "you're hitting, again, 45 to 50% plus" | transcricao | L8582 | deliverability-limiar-de-open-rate |
| Degraus seguintes | "Same logic from 30 to 60 (…) then maybe after a couple weeks, you expand to the 90 day" | transcricao | L8583 | — |
| Segmentos-semente com dado de email | "opened three times in the last thirty days"; "opened five times in the last sixty days"; "opened an email once or twice in the last week"; "clicked an email in the last week" | transcricao | L8564 | — |
| Segmento pequeno demais — exemplo | "seventy-eight people in there, which isn't really going to move the needle" | transcricao | L8567 | — |
| Segmentos-semente comportamentais (Shopify) | "viewed a product in the last three days, placed an order in the last week, and started checkout in the last week" | transcricao | L8574 | — |
| Onde colocar o código de desconto | "welcome email 1, 2, 3, 4" (nunca no form) | transcricao | L8548 | — |
| Correção de rota — exemplo de queda | "from your 30 day engage list to your 60 day (…) open rates go from 50% to 25%" | transcricao | L8601 | — |
| Correção de rota — passo menor | "instead of going from 30 to 60, we go from 30 to 45 day engage. And that keeps us at a 40 to 50% mark" | transcricao | L8604 | deliverability-limiar-de-open-rate |

## Reparo de reputação

| Medida | Valor verbatim | registro | linha | conflito |
|---|---|---|---|---|
| Listas em uso quando a conta cai em spam | "you're sending to, you know, 90, 120 day engage list" | transcricao | L8589 | — |
| Janela de reparo | "anywhere between 2 to 3 weeks to start" | transcricao | L8591 | — |
| Segmentos de reparo | "7 day engage, 14 day engage, 30 day engage" | transcricao | L8591 | — |
| Parâmetro extra de reparo | "people that have opened 2 times, 3 times in the last 14 days" | transcricao | L8591 | — |
| Alvo de abertura no reparo | "once you hit those 60% open rates, 60, 70, 80" | transcricao | L8592 | — |

## Caso real 1 — migração de MailChimp (L8607-8622)

| Medida | Valor verbatim | registro | linha | conflito |
|---|---|---|---|---|
| Listas exportadas | "60 day engage, 90 day engage. 30 day engage list" | transcricao | L8608-8609 | — |
| Tamanho da lista importada | "it was, you know, a hundred thousand people" | transcricao | L8611 | — |
| Primeiro envio | "we ended up starting sending out to a thousand people" | transcricao | L8610 | — |
| Marco do nono envio | "by nine [sends], we were sending to roughly 14,000" | transcricao | L8610 | — |
| Fim da janela de 60 dias | "we were sending to about 120,000 people per [send]" | transcricao | L8611 | deliverability-caso-mailchimp-escala-final |
| Amostra 1 | "a random sample of those thousand people (…) get a 46.22% open rate" | transcricao | L8613-8614 | — |
| Amostra 2 | "2,000 people in a random sample (…) 53%" | transcricao | L8615 | — |
| Amostra 3 | "about 4,000 people, 50%" | transcricao | L8616 | — |
| Degraus 4 a 6 | "6,000 and then 8,000, then 12,000" | transcricao | L8617 | — |
| Degrau corrompido | "And then we go up to 4,000. 14,000." | transcricao | L8618 | deliverability-caso-mailchimp-escala-final |
| Escala final | "14,000, 20,000, 30,000, 40,000, 60,000, 80,000, all the way up to about 100,000" | transcricao | L8619 | deliverability-caso-mailchimp-escala-final |
| Leitura do Google — enviados | "this got sent out to 40,000, 14,000 people" — dois números para o mesmo envio | transcricao | L8621 | deliverability-caso-mailchimp-escala-final |
| Leitura do Google — abertos | "7,000 people opened it" | transcricao | L8621 | — |
| Leitura do Google — cliques | "How many people clicked on it? 205" | transcricao | L8622 | — |

## Caso real 2 — zero dado, pré-lançamento (L8623-8639)

| Medida | Valor verbatim | registro | linha | conflito |
|---|---|---|---|---|
| Envio 1 — volume | "about 200 people or so" | transcricao | L8626 | — |
| Envio 1 — aberturas | "we had a hundred people open it" | transcricao | L8626 | — |
| Envio 2 — aberturas | "we had 175 people open it" | transcricao | L8627 | — |
| Marco acumulado | "we're in like the 600 total [sends] mark" | transcricao | L8627 | — |
| Degraus seguintes | "right around 1,300, 1,400, and then boom to like 1,600" | transcricao | L8628 | — |
| Degraus seguintes | "probably like 10,000, and then 12,000, 15,000" | transcricao | L8630 | — |
| 30 dias engajados + amostra | "which took us to about 26,000" | transcricao | L8630-8631 | — |
| Salto final | "we sent to all the active people, which was about 45" — **unidade ausente** | transcricao | L8631 | deliverability-salto-de-45 |
| Prêmio do giveaway | "a free $3 gift card" | transcricao | L8638 | — |

## Ferramentas e procedimentos

| Medida | Valor verbatim | registro | linha | conflito |
|---|---|---|---|---|
| Registros DNS na prosa do slide | 4 — "MX, SPF, DMARC, DKIM" | slide | L8671 | deliverability-registros-dns |
| Registros DNS na lista de requisitos | 3 — SPF, DMARC, DKIM | slide | L8687-8689 | deliverability-registros-dns |
| Passos de upload | 5 | slide | L8744-8748 | — |
| Glockapps — tamanho da lista de teste | "a list of 100+ email addresses" | slide | L8756 | — |
| Glockapps — cadência sugerida | "consider using one of their tests once per month" | slide | L8757 | — |
| Flows de alta intenção citados | 5 nomeados + "I'll list the other ones" (nunca lista) | transcricao | L8545 | — |
| Gap de transcrição — reparo | 13:04 → 13:33, ~29 segundos ausentes | transcricao | L8593-8594 | — |
| Gap de transcrição — nome da ferramenta | 21:52 → 22:33, ~41 segundos ausentes | transcricao | L8641-8642 | — |
