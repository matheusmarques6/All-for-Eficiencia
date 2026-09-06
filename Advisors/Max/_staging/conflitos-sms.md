---
tipo: staging
modulo: sms
fonte: "CONTEUDO BRUTO/max.md — L9213-9260 (transcrição), L9261-9544 (slide GAMMA)"
status: rascunho
---

# Contradições do módulo SMS

Dezesseis entradas. Três delas (`sms-benchmark-de-form`, `sms-delay-do-popup`,
`sms-exit-intent`) **complementam** conflitos já abertos pelo módulo de list
growth: é a mesma disputa, com uma versão a mais vinda daqui.

## sms-frequencia

| Valor | registro | linha |
|---|---|---|
| "not more than one maybe two SMS messages per week" | transcricao | L9227 |
| "**I wouldn't recommend sending more than 1-2 sms messages per week**" | slide | L9367 |
| "for sms we see the best results sending only 1-2 times per week" | slide | L9491 |
| "try not to send more than once per week every now and again you can do twice" | transcricao | L9228 |
| "with SMS we only want to send once per weekish" | transcricao | L9248 |
| Calendário-exemplo: 6 mensagens + 1 teaser opcional em 31 dias, com 30 e 31 em dias consecutivos, declarado "perfect" | transcricao | L9250-9255 |

**Como responder:** 1-2 por semana é a posição sustentada — está nos dois
registros e é a única que traz o mecanismo ("results plateau and unsubscribe
rates increase past this", L9367). "Once per weekish" (L9248) e "once per week,
twice de vez em quando" (L9228) são a mesma regra com o teto puxado para o piso:
ele trata 2 como exceção, não como cadência. O calendário-exemplo não viola o
teto semanal — 7 mensagens em 31 dias dá média abaixo de 2/semana — mas viola o
espaçamento uniforme: concentra 4 mensagens em torno dos dois eventos e admite
dias consecutivos "for big events like that" (L9253). O critério dele não é a
média, é o evento: mensagem só quando há motivo, e lacuna nunca maior que uma
semana (L9253).

## sms-frequencia-de-email-comparada

| Valor | registro | linha |
|---|---|---|
| Email: "four to five messages a week" sem backlash | transcricao | L9226 |
| Email: "4-5 email campaigns per week" | slide | L9364 |
| Email: "like four times a week" | transcricao | L9248 |
| Email: "best results and engagement sending 4x per week (every other day)" | slide | L9490 |
| Email: tabela por faturamento, 2x a 5-6x/semana | slide (campanhas) | L5295-5298 |
| Email: "two to four times per week is really hitting the sweet spot" | transcricao (campanhas) | L4242 |

**Como responder:** os números de email citados *dentro do módulo de SMS* são
comparativos de argumento, não a especificação de email. A especificação está no
módulo de campanhas, que decide por tier de faturamento ou tráfego (L5295-5298)
e cujo sweet spot declarado é 2-4x (L4242) ou 3x (L5255). Nunca responda "4-5 por
semana" citando L9226/L9364: aquilo existe para dizer que SMS é menos.

## sms-mms-no-browse-abandon

| Valor | registro | linha |
|---|---|---|
| "stick to SMS messages text only as much as you can unless it's absolutely necessary" | transcricao | L9230 |
| "**sticking to SMS text only messages** to get the highest ROI" | slide | L9386 |
| "you can A/B test including a picture of the item the person browsed" | slide | L9449 |

**Como responder:** a proibição é a regra; o browse abandon é a única exceção
nomeada — e o próprio slide da exceção repete o custo e manda medir: "Keep in
mind this is 2x-3x more expensive than just using text so review results
accordingly" (L9449). O critério é o mesmo dos dois lados: a imagem precisa gerar
2-3x mais receita (L9230, L9384). Responda com a regra e a exceção juntas, nunca
só uma.

## sms-open-rate-de-email

| Valor | registro | linha |
|---|---|---|
| "(email has an average open rate of 30%)" | slide | L9291 |
| "we need to be above 50%" | transcricao | L178 |
| "Open Rates — 50%+" (tabela de métricas) | slide | L376, L8715 |
| "Target: 45%+ for engaged segments" | slide | L430 |
| "ideally 50 to 60% range, but anything over 40% is okay" | transcricao | L4236 |

**Como responder:** são coisas diferentes usadas como se fossem a mesma. Os 30%
são média de mercado, citados para fazer o 98% do SMS parecer maior; os 50%+ são
a meta dele para as contas que gere, e ele a trata como linha de corte ("if
you're below 50%, you're fucking something up", L178). Nunca cite 30% como
benchmark de email do Max.

## sms-quinze-por-cento

| Valor | registro | linha |
|---|---|---|
| "automations (…) the on average 15% click rates" | transcricao | L9224 |
| "contributing to 15% of total store revenue" | slide | L9412 |
| "that contributes to 20% of the Brand's total revenue" | transcricao | L9224 |

**Como responder:** o mesmo "15%" mede duas coisas — click rate de automação
(L9224) e share da receita total da loja (L9412) — e ainda há um terceiro número,
20% de share (L9224), para uma marca não nomeada. O print a que L9412 se refere
não sobreviveu à extração, então não dá para saber se é a mesma marca. Nunca
some, nunca escolha: diga qual 15% é qual.

## sms-instrucoes-de-optin-sao-de-email

| Valor | registro | linha |
|---|---|---|
| Título "Instructions for **Post Purchase Opt-Ins**", dentro de "How To Grow Your **SMS** List" | slide | L9318, L9328 |
| Prosa: o checkbox "will sign up someone's **number** for receiving marketing" | slide | L9322 |
| Passo 2: "in the **Marketing options** section, check **Email**" | slide | L9331 |
| Passo 3: "the **email** marketing sign-up check box (…) **email** subscription list" (3x) | slide | L9332 |
| Mesmos passos no módulo de email, onde estão corretos | slide | L1118-1121 |

**Como responder:** o passo a passo é de opt-in de **email**, reaproveitado sem
adaptação numa seção de SMS. Ele não ativa coleta de telefone. Se perguntarem
como capturar telefone no checkout do Shopify, a resposta é que **o corpus não
tem esse procedimento** — tem o de email, com título de SMS. O defeito interno do
passo 3 (pré-marcado para quem está e para quem não está na lista, L9332) é o
mesmo já registrado em `list-growth-checkbox-preselecionado` (L1120).

## sms-benchmark-de-form

*Complementa `list-growth-benchmark-de-form`.*

| Valor | registro | linha |
|---|---|---|
| "around 2 to 3% of website visitors" (o que ele audita) → "8% to 10%" (alcançável) | transcricao | L9238-9239 |
| "6 to 12% (…) minimum 6%, ideally 10% plus (…) some brands 20 to 30%" | transcricao | L194 |
| "10%+ opt in rates (…) should continue to be tested to try to reach 20%+" | slide | L1186-1187 |
| Case: 2.5% → 8.75% | slide | L1175-1181 |

**Como responder:** o número muda conforme o papel da frase. Como diagnóstico do
mercado ele usa 2-3% (L9238); como meta mínima, 6%; como meta boa, 10%+; como
teto perseguido, 20%+. Cite a faixa e o papel, nunca um número solto.

## sms-delay-do-popup

*Complementa `list-growth-time-delay`.*

| Valor | registro | linha |
|---|---|---|
| "6 to 10 seconds after page load", e ele usa 6 | transcricao (SMS) | L9239-9240 |
| "4 to 12 seconds" | transcricao + slide | L655, L820, L1251, L1274 |
| "4 to 8 seconds (…) typically (…) a 6second delay" | transcricao | L1033 |
| "four to six second time delay trigger" | transcricao | L194 |
| "it's based after 5 seconds" (demonstração) | transcricao | L982 |

**Como responder:** as cinco faixas concordam em uma coisa só — o valor que ele
efetivamente usa é 6 segundos (L9240, L1033). Dê 6s como default e a faixa mais
larga (4-12s) como espaço de teste.

## sms-exit-intent

*Complementa `list-growth-exit-intent`.*

| Valor | registro | linha |
|---|---|---|
| "I wouldn't recommend doing like scrolling or anything like that or exit intent because sometimes it can misfire" | transcricao (SMS) | L9240 |
| "when a visitor is exiting, which I don't recommend. Exit intent isn't very good (…) sometimes it'll misfire" | transcricao | L818-820 |
| "Exit intent pop-ups work good on desktop, but for mobile, they misfire a lot" | transcricao | L1035 |

**Como responder:** a rejeição é geral em dois trechos e condicionada a
dispositivo num terceiro. A versão mais específica (L1035) explica as outras: o
problema é mobile. No módulo de SMS ele descarta sem qualificar (L9240).

## sms-vias-de-crescimento

| Valor | registro | linha |
|---|---|---|
| "similar to email marketing there are **two** main ways to grow your SMS list" | transcricao | L9237 |
| "four types, four methods of list growth" / "The 4 Methods of List Growth" | transcricao, slide | L531, L1093 |

**Como responder:** para SMS ele nomeia duas vias (checkbox de checkout e
pop-up); para email, quatro (as duas anteriores mais sign-up page e embed). O
corpus não diz se sign-up page e embed captam telefone. Trate como recorte de
canal, mas não afirme que só existem duas vias sem dizer que a frase é dele sobre
SMS.

## sms-welcome-contagem

| Valor | registro | linha |
|---|---|---|
| "usually you want like two to three SMS messages" | transcricao | L9245 |
| Template com 2 mensagens (Welcome SMS 1 + Wait 5 days + Welcome SMS 2) | slide | L9436-9443 |

**Como responder:** o slide vence em especificação — duas mensagens, com o texto
pronto. A fala admite três, mas o corpus não fornece a terceira. Se pedirem a
terceira, diga que não existe.

## sms-janela-do-winback

| Valor | registro | linha |
|---|---|---|
| SMS: "Wait 120 Days from Last Purchase" | slide | L9479 |
| SMS: "anybody who purchased like months ago" | transcricao | L9245 |
| Email: segmento / time delay de 90 dias | transcricao | L3314-3318 |

**Como responder:** 120 dias é do winback de SMS, 90 do de email — canais
diferentes, não é contradição direta. Mas o corpus **não justifica** a diferença
em lugar nenhum. Registre os dois números com o canal colado.

## sms-transacional-puro-ou-quase

| Valor | registro | linha |
|---|---|---|
| "keep things as mostly transactional" | transcricao | L9249 |
| "Purely transactional content." | slide | L9497 |
| "you can also create angles that make something seem important like a back in stock message" | transcricao | L9249 |

**Como responder:** o slide é absoluto, a fala é "quase". A fala é a que descreve
o comportamento real — ele permite enquadrar algo como importante (L9249) —, então
"mostly" é a formulação mais fiel. A lista de exclusão é idêntica nos dois
registros: nurture, prova social e conteúdo de engajamento não entram (L9249,
L9496).

## sms-horario-de-last-chance

| Valor | registro | linha |
|---|---|---|
| "around like 6:00 to 7:00 p.m." | transcricao | L9257 |
| "such as 6:30pm-7pm" | slide | L9515 |

**Como responder:** slide vence em especificação (6:30pm-7pm); a diferença é de
meia hora no piso e ele mesmo enquadra o tema como teste ("there's no right
answer besides test it", L9255-9256). Dê a janela do slide junto do teto de
7:30pm, que os dois registros compartilham.

## sms-horario-do-fim-da-tarde

| Valor | registro | linha |
|---|---|---|
| "early evenings such as like 5:00 p.m." | transcricao | L9256 |
| "or 400 p.m. works well as well" (ASR) | transcricao | L9257 |
| "evening around 5pm" | slide | L9509 |

**Como responder:** 5pm está nos dois registros. O "400 p.m." aparece uma vez só,
num trecho com ruído de ASR, e não é confirmado pelo slide — cite como possível
4pm marcando a incerteza, ou não cite.

## sms-auto-check-e-a-lei

| Valor | registro | linha |
|---|---|---|
| "We want it to be auto-checked so someone will be added to the list" | slide | L9324 |
| "it's actually illegal to do in the US lol… so we're only limited to one message" (cart abandon) | slide | L9461 |
| "sneaky little trick" (sobre o checkbox pré-marcado, no módulo de email) | transcricao | L541 |

**Como responder:** não é contradição textual, é uma tensão que o corpus não
resolve. Ele exige consentimento pré-marcado para telefone (L9324) e, duas seções
adiante, invoca a lei americana para limitar o próprio envio (L9461). O corpus
não diz uma palavra sobre TCPA, consentimento expresso escrito ou texto de
opt-in. Se a pergunta for de compliance, recuse: está fora do corpus.
