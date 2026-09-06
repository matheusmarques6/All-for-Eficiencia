---
tipo: staging
modulo: deliverability
assunto: conflitos
autor: max-sturtevant
fonte: "CONTEUDO BRUTO/max.md — L8363-8646 (transcrição), L8647-8759 (slide)"
status: rascunho
---

# Conflitos do módulo deliverability

Sete entradas. Nenhuma resolvida por média.

---

## deliverability-limiar-de-open-rate

O conflito mais grave da pasta: o número que autoriza alargar a lista aparece
com **seis formulações diferentes**, cinco na fala e uma no slide.

| Valor | Contexto | Registro | Linha |
|---|---|---|---|
| "above 50%. 50% to 70% is ideal. If you're above 40%, you're probably okay" | meta geral de métrica | transcricao | L8436 |
| "consistently receiving 50 to 60% opens" | saber se a lista está certa | transcricao | L8468 |
| "ideally 50 plus open rates and then you know you're good to jump to a wider segment" | **a "golden rule"** do warming | transcricao | L8579 |
| "anywhere between 40 to 50 percent. If it starts dipping below 40, I definitely wouldn't be expanding it" | tolerância, linha seguinte à golden rule | transcricao | L8580 |
| "you're hitting, again, 45 to 50% plus (…) that's a good indicator that we can expand" | expandir de 14 para 30 dias | transcricao | L8582 |
| "as long as you're hitting those, those 40 to 50% open rates" | cadência de rampa | transcricao | L8588 |
| "Whatever list gets you 50-60% opens" | escolha da lista | **slide** | L8727 |
| "If you start to get 60%+ opens, widen your list to a larger timeframe" | **alargar** | **slide** | L8728 |

Note que L8579 e L8580 são **linhas consecutivas** e já discordam entre si: "50
plus" vira "40 a 50" na frase seguinte.

**Como responder:** dar os valores todos, na ordem em que aparecem, e nomear os
dois pontos em que o corpus é unânime — (a) **abaixo de 40% nunca se alarga**
(L8580, e L8729/L8470 mandam apertar em 40%); (b) o alvo de operação é
`Greater than 50%` (L8715). O slide, que vence em especificação pelo protocolo,
é o mais conservador: exige **60%+** para alargar (L8728). A fala é mais
permissiva e oscila entre 40 e 50. Se a pergunta for "posso alargar com 45%?",
a resposta honesta é: pelo slide não, pela fala talvez (L8582 diz 45-50+), e ele
nunca reconcilia. O critério de segurança que ele próprio dá não é numérico —
"I always err on the side of caution" (L8569) e "it's much easier to build your
sender reputation (…) than it is to fix it when it's already in a poor
position" (L8555). Na dúvida, o número mais alto.

---

## deliverability-passo-de-escalonamento

Quanto se aumenta o volume a cada envio durante o warming.

| Valor | Registro | Linha |
|---|---|---|
| "you scale up by about fifty to, by about fifty percent each send, as long as you're still getting the metrics that you want" | transcricao | L8569 |
| "gradually increase from 25 to 50 percent percent based on performance" (*"percent percent" = gagueira de ASR*) | transcricao, lendo o bullet do deck de warming | L8556 |

**Como responder:** a faixa **25 a 50%** é a formulação do deck (lida em voz
alta em L8556) e contém a da fala; os **~50%** de L8569 são o topo dessa faixa,
não um valor concorrente. Dar as duas e dizer que 50% é o teto, não o padrão —
consistente com o "err on the side of caution" da mesma linha L8569. Ressalva
obrigatória: o deck de warming **não foi exportado** (ver a lacuna abaixo), então
L8556 é a fala citando o slide, não o slide. Não há registro independente para
conferir.

---

## deliverability-primeiro-degrau-da-rampa

O primeiro volume da cadência de rampa está corrompido na transcrição.

| Valor | Contexto | Registro | Linha |
|---|---|---|---|
| "on the first end, you're sending to one to 200,000" | cadência de rampa | transcricao | L8587 |
| "maybe a hundred people, two hundred people, three hundred people, somewhere in that range" | primeiro envio | transcricao | L8569 |
| degraus seguintes: 300 → 500 → 1.000 → 2.000 → 4.000 → 6.000 → 6.000 | mesma cadência | transcricao | L8588 |

**Como responder:** o "200,000" de L8587 é **erro de transcrição, não dado**.
É incoerente com o degrau imediatamente seguinte (300) e com o primeiro envio
declarado em L8569 (100-300 pessoas). O número real do degrau 1 não é
recuperável. Responder com **100-300 pessoas** (L8569) e declarar que a linha da
cadência está corrompida. Nunca reproduzir "200.000" como primeiro envio — é o
erro que quebra a conta.

---

## deliverability-unsubscribe-afeta-ou-nao

O slide se contradiz sozinho, e a fala contradiz o slide.

| Versão | Registro | Linha |
|---|---|---|
| "The unsubscribe is actually a neutral metric. It doesn't really affect deliverability, but it's a good thing to keep an eye on" | transcricao | L8432 |
| listado entre "Open rates, click rates, bounce rates, unsubscribe rates, and spam complaint rates" sob o título "All That Matters For Deliverability" e a frase "That is all that Google, Yahoo, etc look at" | slide | L8706-8710 |
| tem meta numérica na tabela: "Less than 0.4%" | slide | L8719 |
| o rótulo da própria linha da tabela diz "(doesn't affect deliverability)" | slide | L8719 |

**Como responder:** mostrar as quatro versões. A posição mais sustentada é a de
que **não afeta deliverability**, porque aparece nos dois registros (fala L8432 e
o rótulo do slide L8719) — mas o mesmo slide o lista entre as métricas que o
Google olha (L8710) e lhe dá alvo (L8719). A leitura que concilia sem inventar:
**é métrica de monitoramento com alvo, não de deliverability**. O uso que ele dá
é diagnóstico (L8434): "a really good indicator if you're sending too many
emails, honestly, or if your filters are messed up in your flows, because people
will start unsubscribing in droves." Se o usuário perguntar "unsubscribe alto me
manda para spam?", a resposta é: ele diz que não, mas ainda assim exige
`< 0.4%` e o coloca na lista do que os provedores olham.

---

## deliverability-lista-base-padrao

Qual janela usar como lista base do dia a dia.

| Valor | Registro | Linha |
|---|---|---|
| "90 Day Engaged List (You can use any time frame, 90 is recommended to start)" — "This is your base segment for sending all your email campaigns to" | slide | L8734 |
| "for a normal send or normal sends, you might only want to send to your 60 day engage list" | transcricao | L8462 |

**Como responder:** slide vence em especificação — **90 dias para começar**
(L8734), com a ressalva explícita de que a janela é parametrizável ("You can use
any time frame"). A fala usa 60 como envio normal (L8462) e, no exemplo de
correção de rota, também aponta 60 como o lugar seguro para onde voltar (L8474).
O critério real não é o número e sim o resultado: a lista certa é a que entrega
50-60% de abertura (L8727, L8468) — ou seja, os dois valores são pontos de
partida, não regras.

---

## deliverability-registros-dns

O slide lista quatro registros na prosa e três na lista de requisitos.

| Valor | Contexto | Registro | Linha |
|---|---|---|---|
| "MX, SPF, DMARC, DKIM" | prosa de "What Affects Deliverability" | slide | L8671 |
| SPF, DMARC, DKIM | lista "Records you need on your domain for inbox placement" | slide | L8687-8689 |

**Como responder:** três são requisito declarado (**SPF, DMARC, DKIM**, L8687-8689);
o **MX** é citado uma vez, na prosa (L8671), e não entra na lista de requisitos.
Não afirmar que o MX é dispensável nem que é obrigatório — o corpus não decide.
A fala não menciona nenhum dos quatro por nome: ela delega inteiramente ao artigo
do Klaviyo (L8410-8412) e à verificação no `glockapps.com/domain-checker` (L8691).

---

## deliverability-caso-mailchimp-escala-final

Os números do caso real 1 não fecham entre si.

| Valor | Contexto | Registro | Linha |
|---|---|---|---|
| "a hundred thousand people" | tamanho da lista importada | transcricao | L8611 |
| "about 120,000 people per [send]" | volume ao fim da janela de 60 dias | transcricao | L8611 |
| "all the way up to about 100,000" | topo da escala final | transcricao | L8619 |
| "And then we go up to 4,000. 14,000." | degrau após 12.000 | transcricao | L8618 |
| "this got sent out to 40,000, 14,000 people and 7,000 people opened it" | leitura do Google | transcricao | L8621 |

**Como responder:** citar os números verbatim e dizer que o caso é **narrado de
memória, com números que não fecham**. 120.000 por envio (L8611) é maior que a
lista importada de 100.000 (L8611) e que o topo declarado de 100.000 (L8619).
O "4,000. 14,000" de L8618 é regressão impossível (o degrau anterior já era
12.000) — é gagueira de ASR corrigindo-se para 14.000. Em L8621, o par "40,000,
14,000" é a mesma gagueira: 7.000 aberturas sobre 14.000 fecham os 50% que ele
está demonstrando. **Usar o caso como ilustração de método, nunca como
benchmark de volume.** O único número limpo e verificável do caso é o open rate
do primeiro envio: **46.22%** (L8614).

---

# Conflito adjacente, registrado mas não numérico

## deliverability-salto-de-45

Em L8631, "we sent to all the active people, which was about 45" — a **unidade
está ausente**. O contexto (degrau anterior de ~26.000, e o resultado descrito
como "a steep jump" que derrubou as aberturas) sugere 45.000, mas o corpus não
diz. **Não completar.** Responder: "about 45", unidade não informada.
