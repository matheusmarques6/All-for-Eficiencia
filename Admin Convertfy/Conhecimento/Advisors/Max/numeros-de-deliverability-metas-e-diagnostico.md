---
tipo: indice
modulo: deliverability
assunto: numeros-de-deliverability-metas-e-diagnostico
autor: max-sturtevant
registro: [slide, outro-narrador]
fonte: "CONTEUDO BRUTO/max.md — L8365-8646 (transcrição), L8647-8759 (slide GAMMA)"
status: aprovado
---

As cinco metas de métrica de deliverability (open, click, bounce, unsubscribe,
spam complaint), o diagnóstico por janela de engajamento — quando apertar e
quando alargar a lista —, e as ferramentas citadas com suas lacunas. Verbatim,
com registro e linha; toda a fala do módulo é `outro-narrador`. A rampa de
warming está em [[numeros-de-deliverability-warming]]. Índice da série:
[[mapa-dos-numeros-por-modulo]].

Faixa: L8365-8646 (transcrição), L8647-8759 (slide GAMMA). **Toda a fala do
módulo é `outro-narrador`.** O que resta de Max é o deck (L8647-8759), que é
curto e também diz "our team" (L8692).

## Metas de métrica (deliverability)

| Medida | Valor verbatim | Registro | Linha | Conflito |
|---|---|---|---|---|
| Open Rates | `"Greater than 50%"` | slide | L8715 | deliverability-limiar-de-open-rate |
| " " (fala) | `"above 50%. 50% to 70% is ideal. If you're above 40%, you're probably okay"` | outro-narrador | L8436 | deliverability-limiar-de-open-rate |
| Click Rates | `"Greater than 0.75%"` | slide | L8716 | — |
| " " (fala) | `"Click rates, 0.75%"` | outro-narrador | L8438 | — |
| Bounce Rate | `"Less than 1%"` | slide | L8717 | — |
| " " (fala) | `"under 1%"` / `"should be less than 1%"` | outro-narrador | L8440, L8448 | — |
| Spam Complaint Rate | `"Less than 0.01%"` | slide | L8718 | fundamentos-spam-glossario |
| Unsubscribe Rate | `"Less than 0.4%"` (rótulo: `"doesn't affect deliverability"`) | slide | L8719 | deliverability-unsubscribe-afeta-ou-nao |
| Ordem das 5 métricas na prosa do deck | open, click, bounce, **unsubscribe, spam complaint** | slide | L8710 | deliverability-unsubscribe-afeta-ou-nao |
| Ordem das 5 métricas na tabela do deck | open, click, bounce, **spam complaint, unsubscribe** | slide | L8715-8719 | deliverability-unsubscribe-afeta-ou-nao |
| Ordem das 5 métricas na fala | open, click, bounce, **spam complaint, unsubscribe** (`"spam, complete rate"` = ASR) | outro-narrador | L8430 | — |

O unsubscribe aqui é `<0.4%`; em fundamentos é `<0.3%` (L378) e no glossário
`<0.2%` (L436). Três valores para a mesma métrica.

## Diagnóstico e segmentação

| Medida | Valor verbatim | Registro | Linha | Conflito |
|---|---|---|---|---|
| Destinos possíveis do email | 3 — primary tab / promotions tab / spam | outro-narrador + slide | L8386-8388, L8659-8661 | — |
| Open rate — exemplo de mau | `"20% of people are opening your emails"` | outro-narrador | L8390 | — |
| " " (slide) | `"2/10 people are opening your emails"` | slide | L8665 | — |
| Open rate — exemplo de bom | `"50% of the people you send it to are opening"` | outro-narrador | L8390 | — |
| Click rate — exemplo de bom | `"1% of those people are clicking"` | outro-narrador | L8390 | — |
| Analogia Instagram | `"1,000 likes, 10,000 likes, 50,000 likes, 100,000 likes"` | outro-narrador | L8394 | — |
| Erro clássico — tamanho da lista | `"50,000 profiles"` / `"send 50,000 emails to every single profile for a week"` | outro-narrador | L8404 | — |
| Janelas de engaged list disponíveis | `"30, 60, 90, 120, 180, or 365 day"` | outro-narrador + slide | L8460, L8726 | — |
| Lista base recomendada | `"90 is recommended to start"` | slide | L8734 | deliverability-lista-base-padrao |
| " " (fala) | `"you might only want to send to your 60 day engage list"` | outro-narrador | L8462 | deliverability-lista-base-padrao |
| Lista para grandes datas | `"180, 365 day engage list"` | outro-narrador | L8466 | — |
| Definição do segmento base | 90 days, 3 condições em OR (opened / active on site / placed order) | slide | L8734 | — |
| Resultado prometido de enviar só a engajados | `"This is how we can get consistent 50% open rates"` | slide | L8725 | deliverability-limiar-de-open-rate |
| Faixa de acerto da lista | `"Whatever list gets you 50-60% opens"` | slide | L8727 | deliverability-limiar-de-open-rate |
| " " (fala) | `"consistently receiving 50 to 60% opens"` | outro-narrador | L8468 | deliverability-limiar-de-open-rate |
| Gatilho para alargar | `"If you start to get 60%+ opens, widen your list"` | slide | L8728 | deliverability-limiar-de-open-rate |
| Gatilho para apertar | `"If you start to get 40% opens, tighten your list"` | slide | L8729 | — |
| " " (fala) | `"If you start to get 40% opens or things start to drop in a significant way"` | outro-narrador | L8470 | — |
| Exemplo de queda por alargar demais | 30 dias → `"65% opens"`; expandiu para 120 → `"goes down to 30%"` | outro-narrador | L8472 | — |
| Destino sugerido após a queda | `"Maybe 90 is a good place to go, but probably want to go back to your 60 day"` | outro-narrador | L8474 | — |

Os três limiares do deck — `50%` (L8725), `50-60%` (L8727) e `60%+` (L8728) —
estão na mesma tela, em quatro linhas. Não há desempate possível: a resposta
entrega os três com as linhas (ver [[_protocolo]]).

## Ferramentas e lacunas

| Medida | Valor verbatim | Registro | Linha | Conflito |
|---|---|---|---|---|
| Registros DNS na prosa do slide | 4 — `"MX, SPF, DMARC, DKIM"` | slide | L8671 | deliverability-registros-dns |
| Registros DNS na lista de requisitos | 3 — SPF, DMARC, DKIM | slide | L8687-8689 | deliverability-registros-dns |
| Passos de upload | 5 | slide | L8744-8748 | design-passos-do-upload |
| Glockapps — tamanho da lista de teste | `"a list of 100+ email addresses"` | slide | L8756 | — |
| Glockapps — cadência sugerida | `"consider using one of their tests once per month"` | slide | L8757 | — |
| Flows de alta intenção citados | 6 nomeados (Welcome, Post-Purchase, Abandoned Card [*Cart*], Abandoned Checkout, Browse, Site Abandonment) + `"I'll list the other ones"` (nunca lista) | outro-narrador | L8545 | — |
| Gap de transcrição — reparo | 13:04 → 13:33, ~29 segundos ausentes | outro-narrador | L8593-8594 | — |
| Gap de transcrição — nome da ferramenta | 21:52 → 22:33, ~41 segundos ausentes | outro-narrador | L8641-8642 | — |

