---
tipo: indice
modulo: sms
assunto: conflitos-sms-frequencia-e-captacao
autor: max-sturtevant
conflitos: [sms-frequencia, sms-quinze-por-cento, sms-instrucoes-de-optin-sao-de-email, sms-vias-de-crescimento, sms-auto-check-e-a-lei]
status: aprovado
---

Registro dos conflitos do módulo `sms` do corpus de Max Sturtevant sobre frequência de envio e captação de número: frequência de SMS, os 15% de participação na receita, instruções de opt-in que são de email, vias de crescimento da lista e o auto check diante da lei. Cada entrada lista os valores divergentes por registro e fecha com um "Como responder".


Faixa: L9213-9260 (transcrição) e L9261-9544 (slide GAMMA). O bloco de fala
(L9215-9260) é `max-provado` por [[_autoria]] (L9258, L9259). `sms-benchmark-de-form`,
`sms-delay-do-popup` e `sms-exit-intent` resolvem para os slugs de list-growth;
`sms-open-rate-de-email` e `sms-frequencia-de-email-comparada` estão em
[[_conflitos#Conflitos entre módulos]].


## sms-frequencia

| Valor | Registro | Linha |
|---|---|---|
| "I wouldn't recommend sending more than one maybe two SMS messages per week" | transcricao | L9227 |
| "**I wouldn't recommend sending more than 1-2 sms messages per week**" (com o mecanismo: "we notice results plateau and unsubscribe rates increase past this") | slide | L9367 |
| "for sms we see the best results sending only 1-2 times per week" | slide | L9491 |
| "try not to send more than once per week every now and again you can do twice" | transcricao | L9228 |
| "with SMS we only want to send once per weekish" | transcricao | L9248 |
| "ideally you're going to be sending one SMS campaign to your list every week" | transcricao | L9247 |
| "If you are sending more you need to make sure you're really segmenting your list to only send to extremely engaged segments" | slide | L9368 |
| Calendário-exemplo de outubro: 4, (8 ou 9, opcional), 10, 15, 23, 30, 31 — "this calendar is perfect" | transcricao | L9250-9255 |

**Como responder:** o **teto é 1-2 por semana** — é a única formulação que aparece nos
dois registros, três vezes, e a única que traz mecanismo declarado ("results plateau
and unsubscribe rates increase past this", L9367). "Once per weekish" (L9248), "one
SMS campaign every week" (L9247) e "once per week, twice de vez em quando" (L9228) são
a mesma regra com o teto puxado para o piso: ele trata **2 como exceção, não como
cadência**.

O calendário-exemplo é o ponto de atrito, e **não se resolve por média.** Ele declara
esse calendário "perfect" (L9255), e as datas que ele nomeia são 4, 8 ou 9 (teaser,
declarado opcional), 10, 15, 23, 30 e 31. Lendo as datas: o trecho de 4 a 10 de
outubro carrega três mensagens quando o teaser é usado, o que está acima do teto que
ele acabou de enunciar. Isso é **leitura das datas que ele deu**, não posição dele — o
corpus nunca faz essa conta e nunca reconhece o atrito. Não converta o calendário em
taxa semanal, nem em mensagens por mês: dividir 7 por 31 dias produz um número que não
está em lugar nenhum do corpus e apaga exatamente o que interessa.

**Os critérios que ele dá, e que substituem a aritmética:**

1. **Evento, não calendário.** Mensagem só quando há motivo — "only sending on like big
   events or important messages" (L9228). Os dois eventos do mês-exemplo (lançamento
   dia 10, flash sale 30-31) puxam 5 das 7 mensagens.
2. **Lacuna nunca maior que uma semana.** É por isso que ele insere as mensagens dos
   dias 4 e 23: "for the rest of the month we have some gaps of over a week without an
   SMS so I just want to insert like two to three extra campaigns in there" (L9253).
   Esse é o único piso de frequência que o corpus enuncia.
3. **Dias consecutivos são liberados para evento grande.** "for big events like that
   it's fine to send on back-to-back days" (L9253) — é a exceção que ele nomeia para o
   par 30/31.
4. **Acima do teto, segmente.** O deck dá a condição de escape: "If you are sending
   more you need to make sure you're really segmenting your list to only send to
   extremely engaged segments" (L9368). É o mesmo mecanismo que reconcilia a cadência
   alta de email em `campanhas-cadencia-alta-vs-tier-1m`.

Ou seja: a resposta certa dá o teto (1-2/semana), a exceção (evento), o piso implícito
(lacuna < 1 semana) e a condição de escape (segmentação), e diz que o calendário que
ele chama de perfeito passa do teto na semana do lançamento sem que o corpus comente.


## sms-quinze-por-cento

**Armadilha de leitura, não conflito.**

| Valor | Mede o quê | Registro | Linha |
|---|---|---|---|
| "automations (…) the on average 15% click rates" | click rate de automação | transcricao | L9224 |
| "contributing to 15% of total store revenue" | share da receita da loja | slide | L9412 |
| "that contributes to 20% of the Brand's total revenue" | share da receita da loja, marca não nomeada | transcricao | L9224 |

**Como responder:** o mesmo "15%" mede duas coisas — click rate de automação (L9224) e
share da receita total da loja (L9412) — e ainda há um terceiro número, 20% de share
(L9224), para uma marca não nomeada. O print a que L9412 se refere não sobreviveu à
extração, então não dá para saber se é a mesma marca. **Nunca some, nunca escolha:
diga qual 15% é qual.**


## sms-instrucoes-de-optin-sao-de-email

| Valor | Registro | Linha |
|---|---|---|
| Título "Instructions for **Post Purchase Opt-Ins**", dentro de "How To Grow Your **SMS** List" | slide | L9318, L9328 |
| Prosa: o checkbox "will sign up someone's **number** for receiving marketing" | slide | L9322 |
| Passo 2: "in the **Marketing options** section, check **Email**" | slide | L9331 |
| Passo 3: "the **email** marketing sign-up check box (…) **email** subscription list" (3x) | slide | L9332 |
| Mesmos passos no módulo de email, onde estão corretos | slide | L1118-1121 |

**Como responder:** o passo a passo é de opt-in de **email**, reaproveitado sem
adaptação numa seção de SMS. **Ele não ativa coleta de telefone.** Se perguntarem como
capturar telefone no checkout do Shopify, a resposta é que **o corpus não tem esse
procedimento** — tem o de email, com título de SMS. O defeito interno do passo 3
(pré-marcado para quem está e para quem não está na lista, L9332) é o mesmo já
registrado em `list-growth-checkbox-preselecionado` (L1120): descreva-o lá, não aqui.
São dois achados distintos sobre a mesma linha copiada — canal errado (aqui) e texto
que se anula (lá).


## sms-vias-de-crescimento

| Valor | Registro | Linha |
|---|---|---|
| "similar to email marketing there are **two** main ways to grow your SMS list" | transcricao | L9237 |
| "four types, four methods of list growth" / "The 4 Methods of List Growth" | transcricao, slide | L531, L1093 |

**Como responder:** para SMS ele nomeia duas vias (checkbox de checkout e pop-up);
para email, quatro (as duas anteriores mais sign-up page e embed). O corpus não diz se
sign-up page e embed captam telefone. Trate como recorte de canal, mas não afirme que
só existem duas vias sem dizer que a frase é dele sobre SMS.


## sms-auto-check-e-a-lei

| Valor | Registro | Linha |
|---|---|---|
| "We want it to be auto-checked so someone will be added to the list" | slide | L9324 |
| "it's actually illegal to do in the US lol… so we're only limited to one message" (cart abandon) | slide | L9461 |
| "sneaky little trick" (sobre o checkbox pré-marcado, no módulo de email) | transcricao | L541 |

**Como responder:** não é contradição textual, é uma tensão que o corpus não resolve.
Ele exige consentimento pré-marcado para telefone (L9324) e, duas seções adiante,
invoca a lei americana para limitar o próprio envio (L9461). O corpus não diz uma
palavra sobre TCPA, consentimento expresso escrito ou texto de opt-in. **Se a pergunta
for de compliance, recuse: está fora do corpus.**

---


