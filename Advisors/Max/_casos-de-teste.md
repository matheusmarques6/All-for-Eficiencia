---
tipo: indice
assunto: casos-de-teste
autor: max-sturtevant
status: rascunho
---

# O que este arquivo é

O eval do corpus. Não é uma lista de perguntas bonitas: é o conjunto de
perguntas que, **se o advisor errar, provam que alguma peça específica
quebrou** — e cada caso diz qual.

Vinte e cinco casos. Cada um tem quatro campos: a pergunta como um usuário real
faria, os elementos obrigatórios da resposta certa com âncora de linha, o erro
concreto que o caso pega, e a peça do corpus que a falha acusa.

**Toda âncora foi conferida abrindo a linha em `CONTEUDO BRUTO/max.md`.** Onde
o caso pede verbatim, o verbatim está aqui em inglês, como no bruto — inclusive
o ruído de ASR. Prosa em português, artefato em inglês: a mesma regra do
[[_protocolo]].

**Como ler o campo "Se errar, quebrou".** As peças possíveis são: roteamento
([[_INDEX]] + [[_protocolo]] passos 1-2), [[_numeros]] (passo 3),
[[_conflitos]] (passo 4), [[_cobertura]] (passo 6), [[persona]] (passo 7),
marcação de autoria ([[_autoria]]) e verbatim (regra 3 do [[_protocolo]]).
Erro de mais de uma peça é comum e está registrado quando acontece.

---

# Os casos

## Roteamento

### C-01 · Roteamento simples — resolve em 3 notas, não em 12

**Pergunta:** Quando o primeiro email do welcome flow tem que disparar?

**Resposta certa contém:** disparo imediato, sem delay. Slide: `"First email
fires immediately upon sign-up"` (L3492). Fala, categórica: `"The first email in
the welcome flow needs to fire automatically upon signing up."` (L1420) e
`"Don't wait some bullshit 10 minutes or wait one hour. No."` (L1422-1424). O
motivo dado por ele: `"Give people the discount code that they signed up for
immediately."` (L1426). Caminho de leitura esperado: [[_INDEX]] →
[[_numeros]] (linha "Qual o delay entre os emails do welcome?") →
[[flows/welcome]]. Três notas, no máximo quatro com [[_conflitos]] — o conflito
`welcome-cadencia` é sobre o intervalo **entre** os emails, não sobre o
primeiro.

**Resposta errada típica:** "espere uns 10 a 15 minutos para não parecer
automático demais" — boa prática genérica de mercado, que o corpus nega com
todas as letras. Ou uma resposta correta obtida depois de varrer as doze notas
de `flows/`.

**Se errar, quebrou:** roteamento (passos 1-2 do [[_protocolo]]) se a resposta
saiu de leitura ampla; [[_numeros]] (passo 3) se o delay não veio da tabela;
guardrail se veio de conhecimento geral.

---

## Número

### C-02 · Número com conflito — as duas versões, nunca a média

**Pergunta:** Quantos emails eu coloco no meu welcome flow?

**Resposta certa contém:** o piso e a dispersão, separados. Piso, nos dois
registros: `"We need to have at least three emails in our welcome flow."`
(transcrição, L1436) e `"At least 3 emails long"` (slide, L3493). Preferência
declarada: `"I like to do like four to five emails."` (L1440). Faixas do slide:
`"Some welcome flows can we 3-4 emails others should be 6-8 emails."` (L3502).
Extremo: `"I have some welcome flows that are like 15 emails, but at least three
emails long."` (L1446). E o critério, que não é numérico — o corpus registra que
ele se recusa a dar template fixo porque `"a brand that's selling $10,000 saunas
is going to be different than a brand selling protein supplements"` (L1378).

**Resposta errada típica:** "cerca de 5 emails" ou "entre 4 e 6". Média
inventada a partir de 3, 4-5, 6-8 e 15 — indistinguível de conhecimento real e
impossível de auditar depois.

**Se errar, quebrou:** [[_numeros]] regra 3 e [[_conflitos]]
(`welcome-contagem-de-emails`). Se a resposta deu só um dos valores, o passo 4
do [[_protocolo]] não rodou.

### C-03 · Número sem conflito — o valor verbatim com a linha

**Pergunta:** Qual é o limite de caracteres de um SMS, e o que acontece se eu
passar?

**Resposta certa contém:** os valores verbatim do slide de SMS.
`"In each SMS you only have 160 characters, which is NOT a lot…"` (L9390);
`"You can go over, but it's more expensive."` (L9391); `"If you go over by even 1
character to 161, the price of your message doubles."` (L9392). Em seguida, o
custo do MMS, que é a pergunta imediata: `"MMS messages are usually 2-3x MORE
expensive than sending an sms."` (L9383) e a exigência que ele deriva disso —
`"you'd have to make 2x-3x more revenue with your mms messages to outperform sms
message ROI"` (L9384), com a recomendação `"sticking to SMS text only messages"`
(L9386). E o emoji: `"the equivalent of 35-50 characters in your message"`
(L9405). Registro: tudo slide. Não existe entrada em [[_conflitos]] para
nenhum destes valores.

**Resposta errada típica:** arredondar ("uns 160, mais ou menos"), converter
("mais ou menos 2 a 3 linhas de texto") ou responder em português traduzindo os
verbatins.

**Se errar, quebrou:** [[_numeros]] regra 1 (verbatim). Se a resposta inventou
um conflito que não existe, quebrou o passo 4 — [[_conflitos]] não tem entrada
para tamanho de mensagem.

### C-04 · Armadilha de referente — os três "75%" do design

**Pergunta:** Vi em algum lugar que 75% do email tem que ficar acima da dobra.
É isso mesmo?

**Resposta certa contém:** a correção do referente antes de qualquer número. O
corpus tem **três** "75%" no módulo de design e eles medem coisas diferentes:

- esforço de produção alocado na hero section — `"Most people will only read the
  top section so 75% of your efforts should go to this."` (slide, L8235; a mesma
  frase na fala, L7258);
- proporção de emails que precisam de botão acima da dobra — `"Button above the
  fold for 75% of your email."` (transcrição, L7027);
- marcas auditadas sem botão por produto — `"75% of the brands I audit don't have
  individual shop now [buttons]"` (transcrição, L7089).

E existe um quarto, em outro módulo: `"Form covers at least 75% of screen"`
(slide, L1253; fala L657), que é cobertura de tela do pop-up. Nenhum deles diz
que 75% do email fica acima da dobra.

**Resposta errada típica:** "sim, 75% do conteúdo tem que estar acima da dobra"
— cita o número sem o referente e funde os três numa regra que o corpus não tem.

**Se errar, quebrou:** [[_numeros]] (seção Armadilhas de número) e
[[_conflitos]] (`design-tres-usos-de-75-por-cento`, marcado `armadilha`, não
`conflito`).

### C-05 · Número corrompido e irrecuperável — a rampa de warming

**Pergunta:** Quantos contatos eu mando no primeiro envio da rampa de warming?

**Resposta certa contém:** o degrau limpo, e a recusa explícita do degrau
corrompido. Citável: `"maybe a hundred people, two hundred people, three hundred
people, somewhere in that range, and then you scale up by about fifty to, by
about fifty percent each send"` (L8569) — o `"by about fifty to, by about fifty
percent"` é gagueira de ASR e fica como está. **Não citável:** L8587,
`"a sample ramp up cadence would look like on the first end, you're sending to
one to 200,000."`, incoerente com os degraus da frase seguinte —
`"send two, going to maybe like 300 (…) send three, 500, send four, a thousand"`
(L8588). A resposta diz que essa linha está corrompida e que o corpus não
autoriza deduzir "100 to 200". Marcação de autoria obrigatória: toda a fala de
warming (L8518-8646) é `outro-provavel` — é material do curso, não fala do Max.

**Resposta errada típica:** "de 100 a 200.000 no primeiro envio", ou a correção
silenciosa para "100 a 200" — que parece razoável e é invenção.

**Se errar, quebrou:** [[_numeros]] (armadilha L8587) e [[_conflitos]]
(`deliverability-primeiro-degrau-da-rampa`). Se a resposta atribuiu a fala a
Max, quebrou também a marcação de autoria.

### C-06 · Número corrompido sem versão limpa — a contagem de clientes

**Pergunta:** Com quantas marcas a agência dele já trabalhou?

**Resposta certa contém:** a recusa do número, com o motivo. A única linha do
arquivo que declara contagem de clientes é `"We've worked with over 279 figure
e-commerce brands"` (L1029) — corrompida, e sem versão limpa em nenhum outro
lugar. O corpus não autoriza escolher entre "279 marcas", "27 marcas de 9
dígitos" ou qualquer outra segmentação. A linha é CTA comercial. O vizinho que
existe é a credencial de receita, e ela também não fecha:
`"the exact process that we use at my agency which has generated $40 million for
clients in the past few years"` (L6350); `"I've made $100 million making emails
for e-commerce brands"` (L6359, e `over $100M` no deck L3419);
`"hacks that have helped me generate over $200 million for brands"` (L5204, e
`$200M` no deck L3428). Se a pergunta for de credencial, entregar os três com as
linhas, nunca um como *o* número.

**Resposta errada típica:** "mais de 279 marcas de e-commerce", ou a
reconstrução "27 marcas de nove dígitos" apresentada como leitura óbvia.

**Se errar, quebrou:** [[_numeros]] (armadilha L1029) e [[persona]] §1
(ressalva obrigatória sobre os números de credencial).

### C-07 · Corrompido **mas** citável — o caso do pop-up

**Pergunta:** Naquele case do pop-up, quanto a receita subiu de fato?

**Resposta certa contém:** os dois pares de valores, da versão limpa. Conversão
do form: `"We increased our pop-up conversion rate from 2.5% to 8.75%"`
(transcrição, L585) e a tabela do slide, `| Form Conversion Rate | 2.5% | 8.75%
|` (L1179). Receita do welcome flow: `"their monthly email welcome flow revenue
went from $7,000 a month, automatically, to $25,000 a month"` (transcrição,
L587) e `| Welcome Flow Revenue | $7,000 | $25,000 |` (slide, L1181). E o
contexto que ele faz questão de dar: `"We literally did not touch any of their
emails."` (L585).

A resposta **não** cita L595, que traz as mesmas medidas corrompidas —
`"8.57 8.75%"` e `"147,000 to 25,000"`. Esse é o ponto do caso: diferente de
L8587 e L1029, aqui a corrupção não bloqueia a resposta, porque a medida existe
íntegra em outro lugar. O corpus não diz se `"8.57 8.75%"` é autocorreção falada
ou artefato de ASR — não afirmar nenhuma das duas.

**Resposta errada típica:** duas, opostas. Ou cita "147.000" como se fosse o
valor de partida, ou recusa a pergunta inteira dizendo que os números do case
estão corrompidos.

**Se errar, quebrou:** [[_numeros]] (armadilha L595). A recusa indevida é a
falha mais reveladora aqui: mostra que a regra de "número corrompido" virou
reflexo em vez de verificação.

### C-08 · Rótulo que não é percentual — a "80% list"

**Pergunta:** O que é essa "80% list" que ele fala? É 80% da minha base?

**Resposta certa contém:** que não é percentual nenhum — é rótulo de Pareto para
a lista de 90 dias engajados. Verbatim: `"ideally send pretty much all of these
to your 90 day engage list. That's your 80% list. That's where you're going to
get the majority of your sales"` (L4650-4654). A metáfora é explicitada em
outra linha: `"It's like the 80-20 rule."` (L5017), `"That 80% is going to be
that 30, 60, 90-day engage list."` (L5019), `"That 20% (…) that's the extra 20 as
you want to optimize things as you grow."` (L5021).

Os percentuais que **existem** para o mesmo assunto são outros e medem coisas
diferentes entre si: `"accounting for 80%-90% of your sales & engagement"`
(slide, L4838 — share de vendas) e `"We achieve these results just sending to our
engaged list for 90% of sends."` (slide, L5597 — share de envios). Marcação de
autoria: L4650-4654 e L5017-5021 estão em L4189-5154, `outro-provavel`.

**Resposta errada típica:** "é a lista que representa 80% da sua base" ou "80%
das suas vendas vêm dela" — as duas leem o rótulo como medida.

**Se errar, quebrou:** [[_numeros]] (armadilha L4652) e [[_conflitos]]
(`campanhas-share-do-90-day-engaged`, marcado `armadilha`).

---

## Cobertura e recusa

### C-09 · Recusa total — nomear a lacuna e oferecer o vizinho

**Pergunta:** Quanto custa o Klaviyo por mês para uma lista de 30 mil?

**Resposta certa contém:** a recusa nomeada. O corpus não tem preço de
ferramenta nenhuma: `pricing` tem **uma** ocorrência no arquivo inteiro (L6001)
e é sobre tiers de produto do cliente, não sobre custo de plataforma. O vizinho,
oferecido como vizinho: `"Klaviyo is just the best (…) It's worth it, but if you
are going to say that, then Omnisend is a solid budget option as well"` (L34) —
e "budget option" nunca é definido; Alia, `"the ROI is worth it every time"`
(L1243), afirmação sem número; Attentive e Postscript, `"they're relatively the
same price"` (L9236). Corolário que a resposta deve dizer: não existe limiar de
tamanho de lista nem de faturamento para escolher entre plataformas.

**Resposta errada típica:** citar tiers reais de preço do Klaviyo. É a falha
mais grave da lista porque é indetectável para quem não conhece o corpus — a
resposta está certa no mundo e errada como resposta *dele*.

**Se errar, quebrou:** guardrail (regra 5 do [[_protocolo]]) e [[_cobertura]]
(§ "Preço de qualquer ferramenta"). Diagnóstico do [[_arquitetura]] §5: "opina
sobre coisa fora do corpus".

### C-10 · Recusa parcial — o Sunset Flow

**Pergunta:** Como eu monto o Sunset Flow?

**Resposta certa contém:** a metade que existe, entregue, e a metade que falta,
nomeada. Existe:

- finalidade, verbatim do glossário — `"Sunset Flow – Triggered when a contact is
  no longer engaging. Removes or suppresses inactive users."` (L411);
- a recomendação de uso — o Sunset está na lista dos oito flows que ele chama de
  `"the recommended flows when just starting out"` (L92-94);
- a **definição do segmento**, lida do PNG embutido na L9545: 180 dias sem abrir,
  180 dias sem clicar, ao menos 10 emails recebidos, zero pedidos over all time;
- o vizinho mais próximo, o critério de suppression list que ele descreve na
  mesma frase em que promete o sunset — `"Someone who's received at least five to
  ten emails over all time, opened zero times in the last year, bounced email,
  you know, multiple times, or marked as spam."` (L5129), logo depois de
  `"We'll talk about this more in the Sunset Flow, obviously, as well."` (L5127),
  promessa que nunca é cumprida.

Falta, e a resposta diz: sequência, contagem de emails, delay, subject line,
template, copy, filtro e condição de saída. Não há aula (L3398-3403 é título,
link e imagem) nem seção no deck. E o glossário diz `"Removes or suppresses"` e
nunca escolhe entre os dois.

**Resposta errada típica:** recusar por inteiro — "o corpus não desenvolve o
Sunset Flow em lugar nenhum". Era o que a nota de cobertura dizia antes da
varredura de falsos negativos, e é falso: a especificação do segmento estava num
PNG em base64, invisível a busca textual.

**Se errar, quebrou:** [[_cobertura]] (§ cobertura parcial) e a regra de recusa
parcial do [[_protocolo]]. Se a resposta inventou a sequência, quebrou o
guardrail.

### C-11 · Célula vazia que não se preenche — delay do cart abandon

**Pergunta:** Qual o delay do primeiro email do cart abandon?

**Resposta certa contém:** que o corpus não informa, com a evidência da
ausência. O deck especifica quatro emails de cart/checkout abandon (L3777-3918)
com conteúdo, subject lines e quick tips — e **zero delay e zero filtro**. A
fala do módulo (L2618-3020) não tem uma única ocorrência de time delay, hora ou
minuto. A ausência é informação, não erro de extração.

O vizinho — e a resposta tem que dizer que é só vizinho — está no módulo de
otimização, e é o resultado de um teste em **outro** flow: `"do we send the first
email to them after 30 minutes or do we send it four hours later?"`, com
`"the four hours actually ended up winning at least on the site abandoned, uh, a
10 to 15% higher placed order rate"` e `"about a thousand dollars in extra
revenue"` (L8952-8962). Faixa `outro-provavel`.

**Resposta errada típica:** "4 horas, igual ao site abandon" — empresta o delay
de outro flow por analogia. É o item explícito da lista "o que nunca fazer" do
[[_protocolo]].

**Se errar, quebrou:** [[_protocolo]] ("preencher célula vazia por analogia com
outro flow") e [[_cobertura]] (§ lacuna total). Se citou as 4h sem dizer que são
de outro flow e de faixa não-Max, quebrou também a marcação de autoria.

### C-12 · Atribuição — a frequência de campanha

**Pergunta:** O Max recomenda mandar quantas campanhas por semana?

**Resposta certa contém:** a separação entre o que é fala dele e o que é
material do curso. A formulação mais citada — `"two to four campaigns per week is
generally going to be the sweet spot"` (L4220) — está em L4189-5154, faixa
`outro-provavel` por [[_autoria]]. Sai como **"o material do curso diz"**, nunca
como "o Max diz". O que é dele, escrito: `"3x per week is typically the sweet
spot for retaining your list while also getting good consistent revenue."`
(slide L5255) e o piso `"I wouldn't recommend going lower than 2x per week no
matter your ecom store size."` (slide L5256), mais a tabela por faturamento —
`$0-50k/mo → 2x per week`, `$50k-250k/mo → 3x per week`, `$250k-1M/mo → 4x per
week`, `$1M/mo+ → 5-6x per week` (L5295-5298). Corroboração em faixa Max:
`"this person will be receiving three to four campaigns per week from you"`
(L2367, `max-provavel`).

**Resposta errada típica:** "o Max diz que 2 a 4 campanhas por semana é o sweet
spot" — atribui a ele uma linha de outro narrador. O erro é invisível se a
resposta não for auditada contra [[_autoria]].

**Se errar, quebrou:** marcação de autoria (regra 6 do [[_protocolo]],
[[_autoria]] §6.2 — esta medida está lá nomeada como "o número que muda de
dono"). Se a resposta deu um número só, quebrou também [[_conflitos]]
(`campanhas-sweet-spot-de-frequencia`).

---

## Procedimento e artefato

### C-13 · Procedimento datado — o upload que não é do Klaviyo

**Pergunta:** Como eu subo meu design do Figma para o Klaviyo?

**Resposta certa contém:** o aviso **antes** dos passos, não depois. A seção se
chama `"Uploading Designs From Figma To Klaviyo"` (L8009) e lista cinco passos
(L8011-8015), sendo o quarto `"Upload your sections as images into Klaviyo"`.
**A demonstração inteira é feita no Omnisend.** Ele anuncia a troca:
`"for this video, um, I'm going to do to use Omnisend (…) You get a 30%, uh,
discount if you use me"` (L8044), diz `"I'll say well copy because that's my
company's name"` (L8046) e fecha com o link de afiliado (L8063). Não há um único
passo executado em Klaviyo.

A resposta também carrega: (a) o carimbo de validade — o corpus não declara data
de gravação em lugar nenhum, e a âncora interna mais recente é `Nov 13, 2024` no
print da L9545; (b) o alt text como passo obrigatório, com o motivo dado ao
vivo — `"if an image doesn't load for someone, it'll show this alt text"` e
`"alt text is just good practice to have and it helps with some deliverability"`
(L8052-8053).

**Resposta errada típica:** listar os cinco passos como se fossem passos de
Klaviyo. Ou dar o aviso no fim, quando o usuário já leu a receita.

**Se errar, quebrou:** regra 4 do [[_protocolo]] (procedimento é datado e diz
qual ferramenta foi demonstrada de fato), [[_cobertura]] (§ "entregue errado") e
[[_conflitos]] (`design-klaviyo-vs-omnisend`).

### C-14 · Artefato verbatim — subject line não se traduz

**Pergunta:** Me dá umas subject lines para o cart abandon.

**Resposta certa contém:** as linhas do deck, **em inglês, sem uma palavra
mudada**. Email 1 (L3806-3810): `"Your order is ready to ship"` · `"One click
away!"` · `"Your cart is waiting"`. Email 2 (L3827-3831): `"Quick check-in"` ·
`"Holding onto your order"` · `"Have any questions with your order?"` A fala
repete as mesmas ideias — `"your order's ready to ship, one click away, your card
is waiting"` (L2737, onde o ASR escreve "card") e `"quick check-in, holding on to
your order, have any questions with the order"` (L2771). A resposta pode
acrescentar a regra dele: `"you don't need to get too cute with your subject lines
and preview text"` (L2849).

**Resposta errada típica:** entregar "Seu pedido está pronto para envio", "A um
clique de distância", "Seu carrinho está esperando". Traduzida, deixa de ser a
subject line dele. Variante igualmente errada: inventar seis subject lines novas
no mesmo espírito.

**Se errar, quebrou:** regra 3 do [[_protocolo]] e a convenção `tipo: artefato`
do [[_INDEX]] ("verbatim, em inglês, nunca traduzir").

---

## Conflito

### C-15 · Conflito entre módulos — HTML contra imagem

**Pergunta:** Preciso ter seções de texto em HTML no email ou posso fazer tudo
em imagem?

**Resposta certa contém:** as duas versões, **com donos diferentes**, e a ponte.

Lado design, fala de Max (bloco L8009-8065, `max-provado`): `"There's some rumor
in the space, someone started it like 8 years ago (…) that you need to have like
HTML sections in your email. You need to have native text sections and whatnot.
But that couldn't be farther from the truth."` (L8026), com a prova oferecida em
tela — `"Look at how little HTML there is in this email (…) don't think that you
need to have native text native text sections"` (L8027-8028), sobre a Ridge.

Lado deliverability, **outro narrador** (L8381-8646, `outro-provavel`):
`"Google can't properly scan the image-based emails (…) Google read HTML.
Image-based emails have a lot less HTML."` (L8500);
`"However, if you at least have a base amount of HTML (…) that's where your alt
text comes into play."` (L8502); `"making sure you're including different bits of
HTML in your email will include deliverability"` (L8504 — `"will include"` é o
texto do bruto; a leitura óbvia é *improve*, mas a correção não está no corpus).

A reconciliação: são duas perguntas diferentes com a mesma palavra. Max nega que
seções de texto nativo sejam necessárias **para vender**; o outro narrador
afirma que algum HTML ajuda o Google a **ler** o email. A ponte é o alt text —
é HTML, é passo obrigatório do upload (L8052-8053, narrado por Max) e é o que
preenche o "base amount". O corpus **não quantifica** quanto é "a base amount".

**Resposta errada típica:** responder só um lado — quem entra pela pasta
`design/` diz "não precisa de HTML" e quem entra por `deliverability/` diz
"precisa" —, ou atribuir a Max a frase sobre deliverability.

**Se errar, quebrou:** [[_conflitos]] § "Conflitos entre módulos"
(`design-html-vs-imagem`), que existe exatamente porque o roteamento por pasta
do [[_INDEX]] entrega uma pasta só. Se atribuiu L8500-8504 a Max, quebrou também
a marcação de autoria.

### C-16 · Conflito entre módulos — o open rate de email dentro do SMS

**Pergunta:** O SMS tem 98% de abertura e o email só 30%. Não é melhor investir
em SMS?

**Resposta certa contém:** a correção da premissa. Os 30% aparecem **uma vez** no
corpus inteiro, num comparativo retórico do deck de SMS — `"SMS marketing
messages have an average open rate of 98% (email has an average open rate of
30%)"` (L9291) — cuja função é fazer o 98% parecer maior. Não é o benchmark de
email dele. O benchmark dele é acima de 50%: `"we need to be above 50%. This is
the only one where it's like, okay, if you're below 50%, you're fucking something
up"` (L178), `"Open Rates — 50%+"` (slide de fundamentos, L376),
`| Open Rates | Greater than 50% |` (slide de deliverability, L8715), e a
tolerância `"you ideally want to be in that 50 to 60% range, but anything over
40% is okay"` (L4236). Nota que a resposta deve dar: nenhuma das duas médias de
mercado (30% de email, 98% de SMS) tem fonte citada no corpus.

**Resposta errada típica:** aceitar os 30% como linha de base de email e
construir a comparação em cima disso.

**Se errar, quebrou:** [[_conflitos]] § "Conflitos entre módulos"
(`sms-open-rate-de-email`).

### C-17 · Conflito dentro do mesmo registro — a tabela contra o glossário

**Pergunta:** Qual é o teto de spam complaint rate que eu tenho que respeitar?

**Resposta certa contém:** **0,01%** como posição sustentada, e o 0,1% do
glossário como registro divergente — nunca como faixa. Sustentam o 0,01%: a fala
(`"we want it to be less than 0.01%"`, L192), a tabela de metas de fundamentos
(`| Spam Complaint Rates | <0.01% |`, L379) e a tabela do deck de deliverability
(`| Spam Complaint Rate | Less than 0.01% |`, L8718). Diverge: o glossário, no
**mesmo deck** de fundamentos — `"Spam Complaint Rate – (…) Target: <0.1%."`
(L438). Dez vezes mais permissivo.

O desempate, e a resposta tem que dizer por que ele existe: em L217 ele declara
que vai pular o glossário — `"So I am going to gloss over this glossary (…) You
can use these if you want"` — enquanto defendeu a tabela linha por linha na fala
(L168-194). Tabela é material que ele sustentou; glossário é material que ele
entregou. Diagnóstico associado, verbatim: `"then you have a content problem,
potentially a segmentation problem"` (L192) — a hesitação no segundo termo é
dele e fica.

**Resposta errada típica:** "entre 0,01% e 0,1%". É a média inventada mais
perigosa do corpus: é a diferença entre uma conta saudável e uma conta em risco
de bloqueio.

**Se errar, quebrou:** [[_conflitos]] § "Conflitos dentro do mesmo registro"
(`fundamentos-spam-glossario`) e regra 2 do [[_protocolo]]. Se a resposta
aplicou a precedência slide-vence-fala e ficou com o glossário, quebrou o
entendimento de que a precedência só vale **entre** registros.

### C-18 · Conflito dentro do mesmo registro — três números em quatro linhas

**Pergunta:** Estou com 45% de abertura. Já posso alargar minha lista de
engajados?

**Resposta certa contém:** que o corpus não reconcilia, e os dois caminhos.

Pelo slide (deck de deliverability, três números em quatro linhas):
`"This is how we can get consistent 50% open rates."` (L8725) ·
`"Whatever list gets you 50-60% opens."` (L8727) ·
`"If you start to get 60%+ opens, widen your list to a larger timeframe"`
(L8728) · `"If you start to get 40% opens, tighten your list to a smaller
timeframe."` (L8729). Pelo gatilho do slide, 45% **não** alarga.

Pela fala, a golden rule e a contradição imediata:
`"the golden rule is, you want to get ideally 50 plus open rates and then you know
you're good to jump to a wider segment"` (L8579) e, na **linha seguinte**,
`"But anywhere between 40 to 50 percent. If it starts dipping below 40, I
definitely wouldn't be expanding it."` (L8580); depois `"you're hitting, again,
45 to 50% plus and then it's like, okay, that's a good indicator that we can
expand"` (L8582). Pela fala, 45% talvez alargue.

O que **nenhuma** formulação contradiz: abaixo de 40% nunca se alarga. E o
critério que ele dá não é numérico — `"I always err on the side of caution"`
(L8569). Aqui não existe desempate: é a mesma tela dando três números, e não há
material sustentado contra material entregue. Toda a fala é `outro-provavel`.

**Resposta errada típica:** "sim, 45% já dá" ou "não, precisa de 50%", em
qualquer dos dois casos sem mostrar que o corpus diz as duas coisas. Pior
variante: "o alvo é uns 55%", que é a média dos três números do slide.

**Se errar, quebrou:** [[_conflitos]] § "Conflitos dentro do mesmo registro"
(`deliverability-limiar-de-open-rate`) e a seção "Quando o conflito é dentro do
mesmo registro" do [[_protocolo]], que usa este caso como exemplo-limite.

---

## Voz e doutrina

### C-19 · Voz — regra dura não leva "teste isso" junto

**Pergunta:** Meu sócio acha que double opt-in é mais seguro. Deixo ligado?

**Resposta certa contém:** a regra fechada, sem hedge. `"Turn off double
opt-in."` (L1394) e o motivo dele: `"We don't want to give people a second chance
to second guess them signing up to the email list."` (L1402). E o limite
declarado: **não vale para SMS** — `"double opt in, if you're using Postscript or
Tentative [Attentive], you [have] to do that. You can also do single opt in"`
(L978).

Critérios de voz verificáveis, não impressionistas:

1. **usa o critério de decisão dele** — a fricção no opt-in é o que custa
   assinante; a decisão é de conversão, não de higiene de lista;
2. **não anexa "teste isso para sua marca"** — este é um item eliminatório, e
   ele fecha eliminatório sem mandar testar ([[persona]] §2 e §7.12). Anexar
   teste a regra dura erra tanto quanto omiti-lo numa preferência;
3. **não usa "at the end of the day"** — marcador do outro narrador (26× nas
   faixas dele contra 2× nas faixas do Max);
4. **não generaliza a regra de email sobre SMS.**

**Resposta errada típica:** "depende do seu objetivo, vale testar os dois" — soa
consultivo e é exatamente o registro que ele reserva para preferência, não para
eliminatório. Segunda variante: aplicar a regra também ao SMS.

**Se errar, quebrou:** [[persona]] (§2 separar eliminatório de preferência, §7.4
e §7.12). Diagnóstico do [[_arquitetura]] §5: "acerta o fato mas soa genérico".

### C-20 · Doutrina qualificada — desconto não é uma posição só

**Pergunta:** Ele é contra desconto, certo? Posso tirar o desconto do meu
pop-up?

**Resposta certa contém:** a separação dos três contextos, porque a posição dele
muda entre eles e o corpus nunca a generaliza.

- **Campanha:** contra. `"I don't really like to send discounts because we want to
  save on our margins you really don't have to if you execute email marketing
  properly"` (L6261).
- **Opt-in:** desconto é a moeda, e ele é agressivo nisso. `"Hey, want emails
  you'll actually read? No, nobody fucking cares about emails (…) All people care
  about is this discount. It's all people care about."` (L547).
- **Abandono:** a favor de testar. `"I recommend testing discounts."` (L2831).

Ou seja: tirar o desconto do pop-up é exatamente o contrário do que ele
recomenda. A resposta que interpreta a posição de campanha como doutrina geral
inverte a prescrição no lugar em que ele é mais categórico.

**Resposta errada típica:** "sim, ele é contra desconto — tire" — generaliza uma
posição qualificada.

**Se errar, quebrou:** [[persona]] §7.11 (item explicitamente marcado como
"qualificado, não absoluto"). Se a resposta apresentou a posição como consenso de
mercado, quebrou também a última linha do "o que nunca fazer" do [[_protocolo]].

---

## Falso negativo

### C-21 · Falso negativo — o limiar de teste que já foi declarado lacuna

**Pergunta:** Quantas vezes eu preciso rodar um A/B test para o resultado valer?

**Resposta certa contém:** a régua, que existe. L8800-8816, verbatim nas partes
que importam: lista de 1.000 dividida 500/500 — `"I wouldn't say that is enough
data to make a sound conclusion"`; lista de `"100,000, 200,000, 500,000"` —
`"you can probably get away with sending one, maybe two at different times and get
pretty conclusive results"`; lista de `"5,000 to 10,000"` — `"you might want to
test that three or four times"`; e a regra explícita: `"Base it off the number of
recipients that are receiving."` (L8816). Cadência de teste de form, em outro
módulo: `"at least for like bi-weekly. Once every two weeks, run some sort of
test"` (L663).

E o que de fato falta, que a resposta nomeia: **nenhum nível de significância,
nenhum intervalo de confiança, nenhuma duração em dias e nenhum teto de testes
simultâneos.** A conclusividade é medida por volume, nunca por estatística.
Faixa `outro-provavel` (L8762-9109).

**Resposta errada típica:** "o corpus não define limiar estatístico de teste" —
recusa por lacuna que não existe. Este item já foi declarado lacuna inexistente
e sobreviveu em duas notas depois de corrigido no índice.

**Se errar, quebrou:** recuperação ([[_arquitetura]] §5, "erra um fato → conserto
o caminho de leitura") e [[_cobertura]] (§ "Cinco coisas que já foram declaradas
lacuna total e não são"). Diagnóstico agravado: se a resposta recusou, o corpus
está produzindo recusa onde tem conteúdo — a falha mais cara de todas, porque é
silenciosa.

### C-22 · Falso negativo — o deck promete e a fala entrega

**Pergunta:** Que métodos ele dá para fazer transição entre as seções do email?

**Resposta certa contém:** os quatro, todos da fala (L7550-7588):

1. **gradiente** — `"You can do things like a gradient. Take this hero section and
   use a gradient into the next section so it kind of flows together."`
   (L7552-7556);
2. **formas ou quebras de linha** — `"You can use shapes or line breaks. So it's
   not like a super clear flat line."` (L7560-7562);
3. **fundo consistente com elementos em primeiro plano** — `"You could have
   consistent background with foreground elements."` (L7570);
4. **transição atrás de foto**, o favorito dele — `"And my favorite is to add
   transitions behind photos (…) Because a customer will like go through, look at
   the photo, and scroll through the photo without even realizing it."`
   (L7580-7584).

A resposta deve dizer que o **deck** é que não lista nenhum: a seção "Email
Transitions" termina em `"Here are a few methods to do this:"` (L8307) e a linha
seguinte já é outro heading. É lacuna do slide, não do corpus.

**Resposta errada típica:** "o deck promete os métodos e não entrega; o corpus
não tem" — o escopo errado. O certo quase nunca é "o corpus não diz"; é "**este
deck** não diz".

**Se errar, quebrou:** [[_cobertura]] (falsos negativos) e a segunda lei de
manutenção do [[_arquitetura]] §5.1 — "não achar não é o mesmo que não existir".

### C-23 · Falso negativo — o conteúdo escondido atrás da grafia corrompida

**Pergunta:** Ele explica por que o framework S.C.E. é esses três princípios e
não outros?

**Resposta certa contém:** que sim, e onde. O racional falado está em
L4715-4767, **em outra aula**, e a busca literal por "S.C.E." falha porque o ASR
grafa **"SDE framework"**: `"So the SDE framework is going to be skimmable, clear
and concise and engaging."` (L4715-4717), seguido de exemplo trabalhado para
cada letra — skimmable com `"use of sections, quick copy, bolded points, just
making this super clear"` (L4717-4719) e a sequência até L4767, que fecha com o
papel dos infográficos. Reforço no deck de
campanhas (L5504-5512) e no deck de copy (L6558-6650).

O que de fato se perdeu, e a resposta nomeia: a transcrição da aula "The
Principles of Good Copy" — o marcador `Transcrição do Vídeo :` da L5615 é o
**único marcador de transcrição vazio do arquivo**. É perda de camada, não
ausência de assunto. Marcação de autoria: L4715-4767 cai em L4189-5154,
`outro-provavel`.

**Resposta errada típica:** "não há racional falado do S.C.E., só a lista dos
três princípios" — a busca textual não achou e a conclusão virou ausência.

**Se errar, quebrou:** recuperação e [[_cobertura]]. A causa raiz específica está
em [[_fontes]] §5 (grafia corrompida pelo ASR): antes de declarar lacuna,
procurar no outro registro, no outro módulo, na grafia corrompida e em imagem
embutida.

---

## Casos de borda

### C-24 · Recusa com aviso ativo — consentimento de SMS

**Pergunta:** Posso deixar o checkbox de SMS pré-marcado no checkout do Shopify?

**Resposta certa contém:** o que ele prescreve, o aviso de que ele não
fundamenta, e o que o corpus não tem.

Ele prescreve: `"We want it to be auto-checked so someone will be added to the
list."` (L9324). E, três seções depois, invoca a lei americana para limitar
frequência: `"In an ideal world I would love to send multiple cart abandon sms
messages, but it's actually illegal to do in the US lol… so we're only limited to
one message."` (L9461). Invoca a jurisdição para limitar envio e ignora a mesma
jurisdição ao prescrever consentimento pré-marcado, sem citar uma norma em
nenhum dos dois casos.

O que o corpus não tem, com a varredura: `TCPA` 0 · `CTIA` 0 · `10DLC` 0 ·
`short code` 0 · `toll-free` 0 ocorrências. `consent` tem 5 e **nenhuma sobre
SMS**; `carrier` tem 2 e as duas são "baby carriers" (L2076, L2080), copy de
exemplo.

E o agravante, que é o que fecha a resposta: os quatro passos sob
`"Instructions for Post Purchase Opt-Ins"` (L9328) são o procedimento de **email**
colado — L9330-9333 são byte-idênticos a L1118-1121 e mandam
`"in the Marketing options section, check Email"` e `"Check Preselected so that the
email marketing sign-up check box is preselected"`. **Nenhum passo executável
menciona telefone.** O corpus parece ensinar a capturar telefone no checkout e
não ensina.

**Resposta errada típica:** repetir "deixe pré-marcado" e listar os quatro
passos como se fossem de SMS. Variante oposta e também errada: recusar por
inteiro, quando o corpus tem posição declarada — só não tem fundamento.

**Se errar, quebrou:** [[_cobertura]] (§ compliance de SMS, a lacuna mais grave
do corpus, e § "entregue errado") e [[_conflitos]]
(`sms-instrucoes-de-optin-sao-de-email`, `sms-auto-check-e-a-lei`).

### C-25 · Ruído de ASR que fica como está

**Pergunta:** Qual o melhor horário para mandar SMS?

**Resposta certa contém:** os horários verbatim, **com o ruído preservado**.
`"the safest is midday around 11:00 a.m. to 2: p.m."` (L9256) — o `"2: p.m."`
é como o bruto escreve e não se limpa para "2:00 p.m."; `"then also early
evenings such as like 5:00 p.m."` (L9256) `"or 400 p.m. works well as well"`
(L9257) — `"400 p.m."` idem. Os limites: `"avoid sending before 10:00 a.m."` e
`"avoid messages past 7:30 p.m."` (L9257). Last chance: `"you can do last chance
SMS messages kind of around like 6:00 to 7:00 p.m."` (L9257). E a ressalva dele,
que abre o trecho: `"every audience is different so you need to test different
times of the day"` (L9256) — aqui o teste **é** dele, porque é preferência, não
eliminatório.

A resposta deve dizer também o que o corpus não trata: `timezone` e `time zone`
têm **0 ocorrências**. Os horários são absolutos, sem nenhuma palavra sobre fuso
do destinatário.

**Resposta errada típica:** normalizar para "das 11h às 14h e às 16h ou 17h" —
limpou o ruído e converteu a notação. Ou dar os horários como se valessem para
qualquer fuso, que é o que o corpus assume sem dizer.

**Se errar, quebrou:** [[_numeros]] (§ "Ruído de ASR que fica como está", que
lista `"11:00 a.m. to 2: p.m."` e `"400 p.m."` nominalmente) e regra 1 (verbatim,
nunca converter). Se anexou fuso horário, quebrou o guardrail.

---

# Como usar

## Rodar

Uma pergunta por conversa limpa, na ordem em que estão. Contexto acumulado
mascara falha de roteamento: se a nota certa já foi lida num caso anterior, o
caso seguinte não testa mais o índice, testa a memória da sessão.

Registrar, para cada caso: **passou / falhou**, e — quando falhou — qual campo
da "Resposta certa contém" não apareceu. O campo ausente é o diagnóstico; a
sensação de que "ficou fraco" não é.

Um caso só passa se **todos** os elementos obrigatórios aparecerem. Meia resposta
certa em caso de conflito é falha, não passe parcial: o valor da resposta está
justamente em mostrar as duas versões.

## O que fazer com cada tipo de falha

Mapeado aos limiares do [[_arquitetura]] §5, que foram definidos **antes** de
medir exatamente para que a decisão não seja racionalizada depois.

| Sintoma | Casos que o pegam | Peça a consertar | O que **não** mexer |
|---|---|---|---|
| **Erro de fato** — número errado, linha errada, conteúdo que existe declarado ausente | C-01 a C-08, C-21, C-22, C-23, C-25 | **Recuperação**: caminho de leitura, nomes de nota, frontmatter, tabelas de [[_numeros]] e o índice de slugs de [[_conflitos]] | prompt e modelo |
| **Soa genérico** — o fato está certo, a resposta poderia ser de qualquer consultor | C-19, C-20 | **[[persona]]**: aprofundar o expert reflection, principalmente §7 "o que Max nunca diria" e §2 "como ele decide" | recuperação |
| **Opina fora do corpus** — completa lacuna com boa prática de mercado | C-09, C-24 | **Guardrail** (regra 5 do [[_protocolo]] + [[_cobertura]]). É a falha mais grave da lista: indetectável para quem não conhece o assunto | nada mais, antes de fechar esta |
| **Perde coerência em conversa longa** — contradiz o que ele mesmo disse três turnos atrás | nenhum caso isolado pega; aparece rodando a bateria inteira numa sessão só | **Arquitetura de memória** — e só aqui | prompt, corpus, persona |

Três leituras que mudam o conserto e não estão na tabela:

**Recusa indevida conta como erro de fato, não como excesso de cautela.** C-07,
C-10, C-21 e C-22 existem para pegar isso. Quando o advisor recusa uma pergunta
que o corpus responde, o defeito é de recuperação, e é o mais caro de todos
porque é silencioso: ninguém audita uma resposta que nunca foi dada.

**Erro de atribuição é peça própria.** C-12, e o lado de atribuição de C-05,
C-08, C-11, C-15, C-18, C-21 e C-23. O fato pode estar certo e a resposta ainda
assim errada, se material de faixa `outro-provavel` sair como *"o Max diz"*. O
conserto é em [[_autoria]] e no frontmatter `registro:` das notas afetadas —
nunca em [[persona]].

**Corrigir a nota de controle não corrige a nota do assunto.** Primeira lei de
manutenção do [[_arquitetura]] §5.1. Índice e nota são cópias independentes da
mesma afirmação: toda correção derivada de uma falha aqui precisa de varredura
por texto no corpus inteiro, nunca de uma edição no lugar onde o erro apareceu.
Depois de corrigir, **rodar o caso de novo** — e rodar também os casos vizinhos
da mesma pasta, que é onde a cópia não corrigida costuma estar.

## Cobertura desta bateria

| Categoria | Casos |
|---|---|
| Roteamento simples | C-01 |
| Número com conflito | C-02 |
| Número sem conflito | C-03 |
| Armadilha de referente | C-04 |
| Número corrompido não citável | C-05, C-06 |
| Corrompido **com** versão limpa | C-07 |
| Rótulo que não é percentual | C-08 |
| Recusa total | C-09 |
| Recusa parcial | C-10 |
| Célula vazia | C-11 |
| Atribuição | C-12 |
| Procedimento datado | C-13 |
| Artefato verbatim | C-14 |
| Conflito entre módulos | C-15, C-16 |
| Conflito dentro do mesmo registro | C-17, C-18 |
| Voz | C-19, C-20 |
| Falso negativo | C-21, C-22, C-23 |
| Recusa com aviso ativo | C-24 |
| Ruído de ASR preservado | C-25 |

**O que esta bateria não mede.** Coerência em conversa de vários turnos, ordem
de leitura efetivamente percorrida (só o resultado é observável), e qualquer
coisa dos quatro módulos de fala não-Max apresentada como *voz* — porque ali não
há voz dele para comparar. Também não mede densidade: um caso por pasta não
prova que a pasta inteira está sã, prova que o caminho até aquela nota está.
