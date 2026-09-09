---
tipo: indice
modulo: campanhas
assunto: conflitos-campanhas-segmentacao-e-janelas
autor: max-sturtevant
conflitos: [campanhas-limiar-vip, campanhas-suppress-list, campanhas-share-do-90-day-engaged, campanhas-janela-de-engajamento, campanhas-winback-janela, campanhas-janela-do-segmento-de-interesse, campanhas-limiar-de-hipersegmentacao, campanhas-encanador-ou-eletricista]
status: aprovado
---

Registro dos conflitos do módulo `campanhas` do corpus de Max Sturtevant sobre para quem enviar: limiar VIP, suppress list, share do 90-day engaged, janela de engajamento, janela do winback, janela do segmento de interesse, limiar de hipersegmentação e a analogia do encanador ou eletricista. Cada entrada lista os valores divergentes por registro e fecha com um "Como responder".


Faixa: L4187-5236 (transcrição) e L5237-5599 (slide GAMMA). **Atenção de
atribuição:** os quatro blocos de fala deste módulo (L4189-5154) são classificados
`outro-provavel` por [[_autoria]]. Onde a fala é o único lado de um conflito, isso
pesa.


## campanhas-limiar-vip

| Valor | Registro | Linha |
|---|---|---|
| "Someone has placed order at least **4 times** over all time" | slide (tabela) | L5590 |
| "if someone's placed **five** orders on the site, give them an additional discount" | **outro-narrador** | L5103 |

**Como responder:** especificação de segmento → slide vence: **4 pedidos**. Registre
que a fala diz 5 (**outro-narrador**). E registre o critério dado acima do número: "use
your gut on what counts as a VIP" (L5083, fala **outro-narrador**) e "use your gut on
what counts as a VIP customer" (L5590, **slide de Max** — é esta a versão citável como
dele), com a preferência declarada por contagem de pedidos em vez de LTV, porque
contagem é previsível e permite avisar o cliente quantas compras faltam (L5590).


## campanhas-suppress-list

| Valor | Registro | Linha |
|---|---|---|
| "received email at least 5 times over all time **AND** opened email zero times in the last 365 days **OR** bounced email at least 3 times over all time **OR** marked email as spam at least once over all time" | slide (tabela) | L5592 |
| "received at least five to ten emails over all time, opened zero times in the last year, bounced email, you know, multiple times, or marked as spam" | **outro-narrador** | L5129 |
| "Exclusion segments should include (but not be limited to): Bounced 3+ times" | resumo do módulo | L4839-4840 |

**Como responder:** o slide vence e é o único registro utilizável — a fala é
aproximada em dois dos quatro critérios ("five to ten", "multiple times"). Dê a
sintaxe do slide verbatim. O bullet do módulo confirma o 3+ de bounce e declara a
própria lista incompleta ("but not be limited to"), o que é lacuna assumida pelo
corpus, não erro de extração.


## campanhas-share-do-90-day-engaged

**Armadilha de leitura, não conflito.** A leitura ingênua das quatro linhas produz
uma contradição de quatro valores que não existe. Entrada mantida no registro
justamente para impedir essa leitura.

| Valor | Registro | Linha | Mede o quê |
|---|---|---|---|
| "accounting for **80%-90%** of your sales & engagement" | resumo do módulo | L4838 | share de **vendas** |
| "That's your **80%** list. That's where you're going to get the majority of your sales" | **outro-narrador** | L4652-4654 | **rótulo de Pareto** + afirmação qualitativa — não é percentual |
| "relying on this for **80-90%** of our sends" | **outro-narrador** | L5139 | share de **envios** |
| "just sending to our engaged list for **90%** of sends" | slide | L5597 | share de **envios** |

**Como responder:** são **duas grandezas diferentes**, e nenhum dos dois pares se
contradiz de fato.

- **Share de vendas/engajamento:** só existe um número, "80%-90%" (L4838). O "80%" de
  L4652 **não é um percentual de vendas**: é o rótulo Pareto da lista ("your 80%
  list"), confirmado por L5017-5021 — "It's like the 80-20 rule. That 80% is going to
  be that 30, 60, 90-day engage list. That 20%…". A afirmação de vendas ao lado dele é
  qualitativa ("the majority of your sales"). **Não cite L4652 como número.**
- **Share de envios:** "80-90%" (L5139) e "90%" (L5597) — um valor pontual dentro de
  uma faixa que o contém. Diga a faixa.

Nunca misture as duas grandezas nem produza um quinto número a partir delas. O que as
quatro linhas sustentam sem exceção: a 90 day engaged list é a base de quase tudo.


## campanhas-janela-de-engajamento

| Valor | Registro | Linha |
|---|---|---|
| "90 Day Engaged List (**You can use any time frame, 90 is recommended to start**)" | slide | L5587 |
| "Just send email campaigns to your **90 Day** Engaged List" | slide | L5596 |
| "opened or clicked emails in the last **30, 60, 90** days, depending on how wide you want to get" | **outro-narrador** | L4949 |
| "your **30-, 60-, 90-day** engage list, depending on how old the Klaviyo account is" | **outro-narrador** | L5151 |
| "That 80% is going to be that **30, 60, 90-day** engage list" | **outro-narrador** | L5017-5019 |

**Como responder:** 90 dias é o padrão e o que se digita — está na tabela e no
fechamento do slide. A fala — **outro-narrador** nas três linhas — não contradiz: ela dá
o **critério de variação**, e o critério é útil: largura desejada do alcance (L4949) e
**idade da conta Klaviyo** (L5151), que é o único fator oferecido no corpus para
justificar 30 ou 60 em vez de 90. Conta nova, janela mais curta. Responda com 90 (slide,
Max) e ofereça o critério marcando que ele vem do material do curso, não da fala de Max.
Ver `deliverability-lista-base-padrao`, onde a fala — também **outro-narrador** — usa 60
como envio normal.


## campanhas-winback-janela

| Valor | Registro | Linha |
|---|---|---|
| "placed order at least once in the past **150 days** AND placed order zero times in the last **90 days**" | slide (tabela) | L5589 |
| "people who have placed an order in the past **150 days**, but they haven't made one in the last **90**" | **outro-narrador** | L5057 |
| "placed an order zero times in the last **hundred days** (…) but placed an order at least once in the last **180**" | **outro-narrador** | L5071 |

**Como responder:** 150/90 é canônico — está nos dois registros. O 100/180 não é
contradição, é alternativa que a própria aula oferece e condiciona: "Maybe your brand has
a longer buying lifecycle and that makes sense" (L5075). O título da linha do slide já
avisa: "Time frames will vary based on your store and how soon people typically come
back" (L5589). Dê 150/90 como default e 100/180 como o ajuste declarado para ciclo de
compra longo. A leitura conceitual dada na aula é "right in that three to six month mark"
(L5059). **Atribuição:** L5057, L5071, L5075 e L5059 estão em L4846-5154,
`outro-provavel` — só a versão do slide (L5589) é citável como material de Max.


## campanhas-janela-do-segmento-de-interesse

| Valor | Registro | Linha |
|---|---|---|
| "at least once **over all time**" (viewed / added to cart / started checkout / placed order) | slide (tabela) | L5591 |
| "viewed creatine at least once **over time**, added creatine to cart at least once **over time**" | **outro-narrador** | L5119-5121 |
| "viewed creatine **in the last 30 days**, added creatine to their cart **in the last 30 days**, or proceeded to check out with creatine **in the last 30 days**" | **outro-narrador** | L4965 |

**Como responder:** slide vence — **over all time**, e a fala confirma em L5119-5121.
O "last 30 days" de L4965 aparece antes, num exemplo improvisado durante a explicação
de casos de uso, não na parte em que a aula define o segmento. Trate como versão inicial
descartada pela definição posterior, mas registre. **As duas linhas faladas (L4965 e
L5119-5121) são `outro-provavel`** — a definição citável como de Max é a do slide.


## campanhas-limiar-de-hipersegmentacao

| Valor | Registro | Linha |
|---|---|---|
| "Don't be concerned with any other segments until you are doing **$1M/mo** or have very specific use cases" | slide | L5583 |
| "this changes (…) as you're doing **a million a month, 10 million a month, seven, eight figures**" | **outro-narrador** | L5007 |

**Como responder:** $1M/mês é o corte declarado e é o número a dar. A fala não o
contradiz — ela descreve uma rampa contínua ("the higher you get, the bigger your list
get, the more opportunities"), não um segundo limiar. O slide também abre uma segunda
porta: "or have very specific use cases", sem definir quais. A ausência de definição é
informação: se perguntarem quais casos, o corpus não diz.


## campanhas-encanador-ou-eletricista

| Valor | Registro | Linha |
|---|---|---|
| "the **plumber** that you're going to choose is the one knocking at your door when you have a problem" (o narrador a atribui ao **próprio pai** — e o narrador **não é Max**) | **outro-narrador** | L4250 |
| "Who are you going to call when your power goes out? The **electrician** who's knocking at your door" | resumo do módulo | L4194 |

**Como responder:** não é conflito de especificação, é a mesma analogia com dois
ofícios. A versão falada tem procedência ("my dad used to say this to me all the
time") — **mas o "my dad" é do outro narrador, não de Max**. A versão citável como
material de Max é a do resumo escrito do módulo (L4194, o eletricista). Não invente
uma terceira profissão, não funda as duas e não atribua o pai a Max.

---


