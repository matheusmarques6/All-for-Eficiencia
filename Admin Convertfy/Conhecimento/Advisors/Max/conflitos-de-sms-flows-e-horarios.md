---
tipo: indice
modulo: sms
assunto: conflitos-sms-flows-e-horarios
autor: max-sturtevant
conflitos: [sms-mms-no-browse-abandon, sms-welcome-contagem, sms-janela-do-winback, sms-transacional-puro-ou-quase, sms-horario-de-last-chance, sms-horario-do-fim-da-tarde]
status: aprovado
---

Registro dos conflitos do módulo `sms` do corpus de Max Sturtevant sobre os flows de SMS e os horários de disparo: MMS no browse abandon, contagem do welcome, janela do winback, o que é transacional puro, horário do last chance e horário do fim da tarde. Cada entrada lista os valores divergentes por registro e fecha com um "Como responder".


Faixa: L9213-9260 (transcrição) e L9261-9544 (slide GAMMA). O bloco de fala
(L9215-9260) é `max-provado` por [[_autoria]] (L9258, L9259). `sms-benchmark-de-form`,
`sms-delay-do-popup` e `sms-exit-intent` resolvem para os slugs de list-growth;
`sms-open-rate-de-email` e `sms-frequencia-de-email-comparada` estão em
[[_conflitos#Conflitos entre módulos]].


## sms-mms-no-browse-abandon

| Valor | Registro | Linha |
|---|---|---|
| "sticking to SMS messages text only as much as you can unless it's absolutely necessary" | transcricao | L9230 |
| "**sticking to SMS text only messages** to get the highest ROI" | slide | L9386 |
| "you can A/B test including a picture of the item the person browsed" | slide | L9449 |

**Como responder:** a proibição é a regra; o browse abandon é a única exceção nomeada
— e o próprio slide da exceção repete o custo e manda medir: "Keep in mind this is
2x-3x more expensive than just using text so review results accordingly" (L9449). O
critério é o mesmo dos dois lados: a imagem precisa gerar 2-3x mais receita (L9230,
L9384). Responda com a regra e a exceção juntas, nunca só uma.


## sms-welcome-contagem

| Valor | Registro | Linha |
|---|---|---|
| "usually you want like two to three SMS messages" | transcricao | L9245 |
| Template com 2 mensagens (Welcome SMS 1 + Wait 5 days + Welcome SMS 2) | slide | L9436-9443 |

**Como responder:** o slide vence em especificação — duas mensagens, com o texto
pronto. A fala admite três, mas o corpus não fornece a terceira. Se pedirem a terceira,
diga que não existe.


## sms-janela-do-winback

| Valor | Registro | Linha |
|---|---|---|
| SMS: "Wait 120 Days from Last Purchase" | slide | L9479 |
| SMS: "anybody who purchased like months ago" | transcricao | L9245-9246 |
| Email: segmento / time delay de 90 dias | transcricao | L3314-3318 |

**Como responder:** 120 dias é do winback de SMS, 90 do de email — canais diferentes,
não é contradição direta. Mas o corpus **não justifica** a diferença em lugar nenhum.
Registre os dois números com o canal colado.


## sms-transacional-puro-ou-quase

| Valor | Registro | Linha |
|---|---|---|
| "keep things as mostly transactional" | transcricao | L9249 |
| "Purely transactional content." | slide | L9497 |
| "you can also create angles that make something seem important like a back in stock message" | transcricao | L9249 |

**Como responder:** o slide é absoluto, a fala é "quase". A fala é a que descreve o
comportamento real — ele permite enquadrar algo como importante (L9249) —, então
"mostly" é a formulação mais fiel. A lista de exclusão é idêntica nos dois registros:
nurture, prova social e conteúdo de engajamento não entram (L9249, L9496).


## sms-horario-de-last-chance

| Valor | Registro | Linha |
|---|---|---|
| "around like 6:00 to 7:00 p.m." | transcricao | L9257 |
| "such as 6:30pm-7pm" | slide | L9515 |

**Como responder:** slide vence em especificação (6:30pm-7pm); a diferença é de meia
hora no piso e ele mesmo enquadra o tema como teste ("there's no right answer besides
test it", L9255-9256). Dê a janela do slide junto do teto de 7:30pm, que os dois
registros compartilham.


## sms-horario-do-fim-da-tarde

| Valor | Registro | Linha |
|---|---|---|
| "early evenings such as like 5:00 p.m." | transcricao | L9256 |
| "or 400 p.m. works well as well" (ASR) | transcricao | L9257 |
| "evening around 5pm" | slide | L9509 |

**Como responder:** 5pm está nos dois registros. O "400 p.m." aparece uma vez só, num
trecho com ruído de ASR, e não é confirmado pelo slide — cite como possível 4pm
marcando a incerteza, ou não cite.


