---
tipo: staging
modulo: deliverability
assunto: conflitos
autor: max-sturtevant
fonte: "CONTEUDO BRUTO/max.md — L8363-8646 (transcrição), L8647-8759 (slide)"
status: rascunho
---

# Conflitos do módulo deliverability

Sete entradas, mais uma adjacente. Nenhuma resolvida por média.

---

## deliverability-limiar-de-open-rate

O conflito mais grave da pasta: o número que decide qual lista usar e quando
alargá-la aparece com **dez formulações diferentes**, sete na fala e três no
slide.

| Valor | Contexto | Registro | Linha |
|---|---|---|---|
| "above 50%. 50% to 70% is ideal. If you're above 40%, you're probably okay" | meta geral de métrica | transcricao | L8436 |
| "consistently receiving 50 to 60% opens" | saber se a lista está certa | transcricao | L8468 |
| "ideally 50 plus open rates and then you know you're good to jump to a wider segment" | **a "golden rule"** do warming | transcricao | L8579 |
| "anywhere between 40 to 50 percent. If it starts dipping below 40, I definitely wouldn't be expanding it" | tolerância, linha seguinte à golden rule | transcricao | L8580 |
| "you're hitting, again, 45 to 50% plus (…) that's a good indicator that we can expand" | expandir de 14 para 30 dias | transcricao | L8582 |
| "as long as you're hitting those, those 40 to 50% open rates" | cadência de rampa | transcricao | L8588 |
| "And that keeps us at a 40 to 50% mark" | alvo após recuar de 30→60 para 30→45 | transcricao | L8604 |
| "This is how we can get consistent 50% open rates" | o que enviar só para engajados entrega | **slide** | L8725 |
| "Whatever list gets you 50-60% opens" | escolha da lista, **duas linhas depois** | **slide** | L8727 |
| "If you start to get 60%+ opens, widen your list to a larger timeframe" | **alargar** | **slide** | L8728 |

Duas adjacências agravam o conflito, e são a prova de que ele não é artefato de
recorte:

- **L8579 e L8580 são linhas consecutivas** e já discordam entre si: "50 plus"
  vira "40 a 50" na frase imediatamente seguinte, dentro da mesma respiração.
- **L8725, L8727 e L8728 estão no mesmo slide**, a uma e duas linhas de
  distância: o slide promete "consistent 50%", manda escolher a lista por
  "50-60%" e depois exige "60%+" para alargar. O registro que vence em
  especificação pelo protocolo tem três números em quatro linhas.

**Como responder:** dar os valores todos, na ordem em que aparecem, e nomear os
dois pontos em que **nenhuma das dez formulações contradiz as outras** —
(a) **abaixo de 40% nunca se alarga** (L8580, e L8729/L8470 mandam apertar em
40%); (b) o alvo de operação é `Greater than 50%` (L8715). O slide é o mais
exigente na hora de alargar — **60%+** (L8728) — mas não é um bloco coerente:
duas e três linhas antes ele já disse "consistent 50%" (L8725) e "50-60%"
(L8727). Ou seja, a precedência do protocolo (slide vence em especificação) não
resolve este conflito, porque o slide discorda de si mesmo. A fala é mais
permissiva e oscila entre 40 e 50. Se a pergunta for "posso alargar com 45%?",
a resposta honesta é: pelo gatilho do slide não (60%+), pela fala talvez (L8582
diz 45-50+), e ele nunca reconcilia. O critério de segurança que ele próprio dá não é numérico —
"I always err on the side of caution" (L8569) e "it's much easier to build your
sender reputation (…) than it is to fix it when it's already in a poor
position" (L8555). Na dúvida, o número mais alto.

---

## deliverability-passo-de-escalonamento

Quanto se aumenta o volume a cada envio durante o warming.

| Valor | Contexto | Registro | Linha |
|---|---|---|---|
| "gradually increase from 25 to 50 percent percent based on performance" (*"percent percent" = gagueira de ASR*) | "the formula", 05:30 | transcricao | L8556 |
| "you scale up by about fifty to, by about fifty percent each send, as long as you're still getting the metrics that you want" | primeiro envio de 100-300, 08:08 | transcricao | L8569 |

**Como responder:** dar os dois, sem escolher. **Os dois são transcrição** — o
deck de warming nunca foi exportado (ver a lacuna abaixo), então nenhum dos dois
tem o peso de slide e a regra de precedência do protocolo não se aplica aqui. Em
L8554 ele diz "the formula, and it's pretty self-explanatory", o que *sugere*
que L8556 esteja sendo lido de um slide — mas o corpus não diz isso e a hipótese
não pode virar registro.

Não dizer que "50% é o teto e 25% é o padrão": o corpus não hierarquiza. L8556
dá uma faixa condicionada a desempenho ("based on performance"); L8569 dá um
passo único (~50%) igualmente condicionado ("as long as you're still getting the
metrics that you want"). A diferença operacional é real e grande — escalar 25%
ou 50% por envio muda a agressividade da rampa em 2×. O critério que ele próprio
oferece não é numérico: "I always err on the side of caution" (L8569) e "it's
much easier to build your sender reputation (…) than it is to fix it when it's
already in a poor position" (L8555).

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
