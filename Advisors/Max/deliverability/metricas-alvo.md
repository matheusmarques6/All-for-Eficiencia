---
tipo: especificacao
modulo: deliverability
assunto: metricas-alvo
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L8430-8452 (transcrição), L8706-8719 (slide)"
conflitos: [deliverability-unsubscribe-afeta-ou-nao, deliverability-limiar-de-open-rate]
status: rascunho
---

# A especificação

Tabela do slide, verbatim (L8713-8719). É o registro que prevalece em
especificação:

> | Metric Name | Metric Value Goal |
> | ----- | ----- |
> | Open Rates | Greater than 50% |
> | Click Rates | Greater than 0.75% |
> | Bounce Rate | Less than 1% |
> | Spam Complaint Rate | Less than 0.01% |
> | Unsubscribe Rate (doesn't affect deliverability) | Less than 0.4% |

O enunciado que a antecede, também verbatim (L8708-8711):

> Engagement rates.
> That is all that Google, Yahoo, etc look at.
> Open rates, click rates, bounce rates, unsubscribe rates, and spam complaint
> rates.
> Send to the right people with good content → Receive positive engagement →
> Increase deliverability

A mesma lista aparece na fala, com a mesma ordem e um erro de ASR ("spam,
complete rate" por *spam complaint rate*): "all that matters, open rates, click
rates, bounce rates, spam, complete rate, and then unsubscribe rate" (L8430).

# O que a fala acrescenta

**Open rate.** A fala é a única a dar faixa e piso de tolerância (L8436):

> so open rates, you want to be above 50%. 50% to 70% is ideal. If you're above
> 40%, you're probably okay, but want those to be on the higher end, especially
> as it relates to deliverability.

Esse "above 40% you're probably okay" não existe no slide, que só dá
"Greater than 50%". E o número de open rate vira outra coisa quando o assunto é
**alargar a lista** — lá o corpus dá cinco valores diferentes. Ver
[[so-envie-para-engajados]] e [[warming-do-dominio]].

**Click rate.** A fala dá o número cru, sem "greater than": "Click rates,
0.75%" (L8438).

**Bounce rate.** O slide dá só o teto. A fala define o que é e separa dois tipos
(L8440-8448):

- *Soft bounce* — "somebody's inbox is full, so they never received it" (L8442).
  Peso menor: "That's not going to affect you as much, but it does still have an
  impact" (L8444).
- *Hard bounce* — "the inbox provider stopped your email from being delivered
  because they don't think you're a reputable sender" (L8444). Peso maior:
  "those ones are really going to bog you down" (L8446).

A instrução operacional é indiferente ao tipo: "when you see bounce rate in
Klaviyo, just know it should be less than 1%" (L8448). Ele promete aprofundar
noutro vídeo (L8446) e não aprofunda. Também menciona que "there's ways to
filter and exclude these people out" (L8450) sem dizer quais.

**Spam complaint.** "If people are marking you as spam, that is a very negative
metric for deliverability" (L8450). A ação é exclusão (L8452):

> if people mark you as spam, you want to make sure that you're excluding these
> people from your campaign sends and most likely from your flows as well.

Note o "most likely" — nos flows ele não afirma, hesita.

# Onde o corpus discorda: o unsubscribe

Conflito duro, e o slide se contradiz sozinho.

| Versão | Registro | Linha |
|---|---|---|
| "The unsubscribe is actually a neutral metric. It doesn't really affect deliverability, but it's a good thing to keep an eye on" | transcrição | L8432 |
| aparece na lista do que "Google, Yahoo, etc look at" | slide | L8708-8710 |
| tem meta numérica: "Less than 0.4%" | slide | L8719 |
| o próprio rótulo da linha da tabela diz "(doesn't affect deliverability)" | slide | L8719 |

Ou seja: o slide lista o unsubscribe entre as métricas que decidem
deliverability (L8710), dá a ele um alvo (L8719) e, no mesmo campo, nega que ele
afete deliverability (L8719). Não há como conciliar isso sem inventar.

O que ele diz que o unsubscribe **serve** para medir (L8434):

> that's a really good indicator if you're sending too many emails, honestly, or
> if your filters are messed up in your flows, because people will start
> unsubscribing in droves.

Ver `deliverability-unsubscribe-afeta-ou-nao` em [[_conflitos]].

# O que o corpus não diz

- Prazo ou janela de medição de qualquer métrica (últimos 30 dias? por campanha?
  vitalício?).
- Se as metas valem para campanhas, para flows, ou para os dois.
- Se `bounce rate < 1%` conta hard, soft ou a soma.
- Como excluir quem marcou spam — só que se deve excluir (L8452).
- O que fazer quando uma métrica fura o alvo. Não há tabela de reação; o mais
  próximo é [[reparo-de-reputacao]], que só trata do caso de spam.
