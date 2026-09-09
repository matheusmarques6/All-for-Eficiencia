---
tipo: especificacao
modulo: deliverability
assunto: metricas-alvo
autor: max-sturtevant
registro: [slide, outro-narrador]
fonte: "CONTEUDO BRUTO/max.md — L8430-8452 (transcrição), L8706-8719 (slide)"
conflitos: [deliverability-unsubscribe-afeta-ou-nao, deliverability-limiar-de-open-rate]
status: aprovado
---

Os alvos numéricos de engajamento que sustentam a entregabilidade — abertura, clique, bounce, spam complaint e unsubscribe: qual é a meta de cada um, o que a aula acrescenta sobre bounce e spam, e onde o corpus se contradiz sobre o unsubscribe.


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

Nesta nota: a tabela de metas (L8713-8719) é **slide**, artefato de Max, e continua
valendo como especificação. Tudo que vem da fala — faixa e piso de open rate
(L8436), soft vs hard bounce (L8440-8448), a leitura do unsubscribe como métrica
neutra (L8432-8434) — está na faixa não-Max e **não é citável como fala dele**.

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

A mesma lista de cinco aparece na fala, com um erro de ASR ("spam, complete
rate" por *spam complaint rate*): "all that matters, open rates, click rates,
bounce rates, spam, complete rate, and then unsubscribe rate" (L8430). **A ordem
não é a mesma**: as três primeiras coincidem, mas as duas últimas estão
trocadas — no slide vem `unsubscribe rates, and spam complaint rates` (L8710) e
na fala vem `spam, complete rate, and then unsubscribe rate` (L8430). Nenhum dos
dois registros declara que a ordem signifique peso, então a inversão não é
citável como hierarquia; é só divergência de listagem.

# O que a fala acrescenta

**Open rate.** A fala é a única a dar faixa e piso de tolerância (L8436):

> so open rates, you want to be above 50%. 50% to 70% is ideal. If you're above
> 40%, you're probably okay, but want those to be on the higher end, especially
> as it relates to deliverability.

Esse "above 40% you're probably okay" não existe no slide, que só dá
"Greater than 50%". E o número de open rate vira outra coisa quando o assunto é
**escolher ou alargar a lista** — lá o corpus dá **dez formulações diferentes**,
catalogadas em `deliverability-limiar-de-open-rate` ([[mapa-dos-conflitos]]). Ver
[[so-envie-para-engajados]] e [[rampa-de-warming-do-dominio]].

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
Klaviyo, just know it should be less than 1%" (L8448). O material promete aprofundar
noutro vídeo (L8446) e não aprofunda. Também menciona que "there's ways to
filter and exclude these people out" (L8450) sem dizer quais.

**Spam complaint.** "If people are marking you as spam, that is a very negative
metric for deliverability" (L8450). A ação é exclusão (L8452):

> if people mark you as spam, you want to make sure that you're excluding these
> people from your campaign sends and most likely from your flows as well.

Note o "most likely" — nos flows o material não afirma, hesita.

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

O que a fala diz que o unsubscribe **serve** para medir (L8434):

> that's a really good indicator if you're sending too many emails, honestly, or
> if your filters are messed up in your flows, because people will start
> unsubscribing in droves.

Ver `deliverability-unsubscribe-afeta-ou-nao` em [[mapa-dos-conflitos]].

# O que o corpus não diz

- Prazo ou janela de medição **destes alvos** (últimos 30 dias? por campanha?
  vitalício?). Correção de escopo (varredura de falsos negativos): o corpus tem
  duas janelas declaradas, e elas medem outra coisa — atribuição de receita, 3 a
  5 dias após o clique (L54), e leitura do painel, 30 dias contra os 30
  anteriores (L64). Ver [[fundamentos/dashboard-do-klaviyo]]. Oferecer as duas e
  marcar que **nenhuma é a janela do alvo**; nunca transpor uma para a outra.
- Se as metas valem para campanhas, para flows, ou para os dois.
- Se `bounce rate < 1%` conta hard, soft ou a soma.
- Como excluir quem marcou spam — só que se deve excluir (L8452).
- O que fazer quando uma métrica fura o alvo. Não há tabela de reação; o mais
  próximo é [[reparo-de-reputacao]], que só trata do caso de spam.
