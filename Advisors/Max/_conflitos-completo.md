---
tipo: indice
assunto: conflitos-do-corpus-completo
autor: max-sturtevant
status: rascunho
---

# O que é este arquivo

As **108 entradas de conflito por módulo**, na íntegra. Só se chega aqui pelo
[[_conflitos]]: a abertura, a regra de ouro, o como-ler-uma-entrada e o **índice dos
126 slugs canônicos** (mais os 18 redundantes e seus ponteiros) estão lá, e valem aqui
sem repetição. As outras **18** entradas canônicas — as duas seções transversais,
"Conflitos entre módulos" e "Conflitos dentro do mesmo registro" — também ficam em
[[_conflitos]], porque são as que têm de ser lidas antes de responder em qualquer
pasta. 108 + 18 = 126; **nenhuma entrada existe nos dois arquivos.**

**A regra de ouro, repetida porque é a única que não pode faltar em lugar nenhum:
nenhum conflito é resolvido por média.** Nem por arredondamento, conversão ou
interpolação. Onde o corpus não permite desempate, o "Como responder" diz isso com
todas as letras — e há casos em que diz.

**Precedência** ([[_INDEX]]): slide vence em especificação, fala vence em julgamento.
Ela só funciona **entre** registros; para os conflitos slide-contra-slide, ver
[[_conflitos#Conflitos dentro do mesmo registro]].

**Atribuição:** onde um lado do conflito cai num bloco `outro-provavel` ou
`outro-provado` do laudo [[_autoria]], a entrada avisa — isso muda o peso da versão e
às vezes decide.

---

# fundamentos

As quatro entradas `*-glossario` estão na seção
[[_conflitos#Conflitos dentro do mesmo registro]], porque são slide contra slide no mesmo
deck. `fundamentos-o-que-move-o-open-rate` está em [[_conflitos#Conflitos entre módulos]].

## fundamentos-roi-do-email

| Valor | Registro | Linha |
|---|---|---|
| "Email average is $36 plus in return for every $1 spent" | transcricao | L13 |
| "Email averages **$36+ return for every $1 spent**" | slide | L285 |
| "Email typically delivers ~40x ROI when done right" | slide (glossário) | L393 |

**Como responder:** **$36+ por $1** — duas ocorrências, dois registros, redação
quase idêntica. O 40x do glossário é uma terceira formulação sem fonte e com uma
condicional que as outras não têm ("when done right"). Nenhum dos três vem com
estudo citado. Se o número for usado, vá junto do contraste que ele faz na mesma
frase: anúncio devolve "2 to 3 dollar" e há marcas satisfeitas com 0.8 ROAS (L13).

## fundamentos-split-campanhas-flows

| Valor | Registro | Linha |
|---|---|---|
| "roughly 50% (…) 60/40, 40/60, depends on the brand a little bit. In general, you want to be around 50/50" | transcricao | L22 |
| "around 50/50 or 40/60, 60/40 anywhere in that range" | transcricao | L60 |
| "We want it to be 40 to 60% each so 40% campaigns, 60% flows. or 60% campaigns, 40% follows" | transcricao | L172-174 |
| "around 50% of your total email revenue with the other 50% coming from campaigns" | slide | L326 |
| "**Campaigns:** 40–60% of email revenue **Flows:** 40–60% of email revenue" | slide | L375 |

**Como responder:** o **centro é 50/50** e isso é unânime — está nos dois
registros e nas três falas. A divergência é na tolerância: "40/60 ou 60/40" (L22,
L60) descreve dois pontos discretos; "40 a 60% cada" (L172, L375) descreve um
intervalo contínuo. Não é a mesma afirmação, mas as duas produzem a mesma faixa
operacional. Dê o centro e a faixa, e diga que ele nunca formula isso duas vezes
do mesmo jeito. O critério de decisão **não é numérico**: "So it's going to take a
little bit of context" (L22). O uso prático é diagnóstico, não meta: 14% em flows
significa "the flows could use a lot of improvement" (L62).

## fundamentos-denominador-dos-80

| Valor | Denominador | Registro | Linha |
|---|---|---|---|
| "flows generating 80% of the total store revenue" | receita da **loja** | transcricao | L22 |
| "roughly 50% of your total email revenue" | receita de **email** | transcricao | L22 |
| "They should make up around 50% of your total email revenue" | receita de **email** | slide | L326 |

**Como responder:** as duas primeiras frases estão **na mesma linha do bruto** e
trocam de denominador no meio. O pilar #2 define flows como percentual da receita
de email; o caso extremo citado na frase seguinte é percentual da receita da loja.
80% da receita total da loja vindos de flows é um número extraordinário; 80% da
receita de email é apenas um desequilíbrio dentro do próprio modelo dele. **Não
escolher.** Cite a frase com o denominador que está escrito e sinalize que ela
contradiz a definição do pilar duas frases antes.

**A comparação que faltava, e que muda a resposta.** Este slug e
`flows-participacao-na-receita` **não são a mesma contradição** — aqui o defeito é a
troca de denominador **dentro de uma linha**; lá são dois números com denominadores
diferentes no mesmo deck. Mas os dois slugs guardam, cada um, **um valor de flows sobre
a receita da loja**, e esses dois valores nunca foram postos lado a lado: **80%** (L22)
contra **20%** (L3408, o título do deck de flows). Mesmo denominador, **4x de
diferença**. O corpus não os reconcilia. A leitura possível — e é leitura, não texto —
é que 20% é a promessa do deck e 80% é o caso extremo que ele mesmo qualifica ("some
brands that are very healthy (…) it's a small list, or the list just doesn't respond as
well as campaigns", L22). **Nunca dê um dos dois sozinho como "quanto flows devem
gerar".**

**Proveniência:** o 50% de receita de email não tem duas fontes de slide. L326
(fundamentos) e L3438 (flows) são **a mesma frase, palavra por palavra**, num bloco
"What Are Email Flows?" reaproveitado inteiro entre os dois decks (L324-326 = L3436-3438).
Slide repetido não é segunda fonte. Conflito irmão: `flows-participacao-na-receita`.

## fundamentos-limiar-de-escalar-aquisicao

| Valor | Registro | Linha |
|---|---|---|
| "If you're over that, say you're at like 60 percent, that tells you, okay, let's funnel some of our profits back into paid ads" | transcricao | L56 |
| "If you get over 55%, you're kind of like at 60%, then it's like, okay, we need to scale our acquisition" | transcricao | L170 |
| "\>55% \= time to scale acquisition" | slide | L374 |

**Como responder:** **55%** — está no slide, que vence em especificação, e na fala
da aula de métricas. Os 60% do walkthrough não são erro: L170 mostra que na cabeça
dele os dois números são vizinhos. Dê 55% como gatilho e 60% como o exemplo que ele
usa. O racional é o mesmo nas duas versões e é o que importa: acima da faixa o
problema **não é o email**, é aquisição (L172).

## fundamentos-piso-de-email-share

| Valor | Registro | Linha |
|---|---|---|
| "If you're anywhere under 30%, um 40%, then that tells you, okay, our email systems can be improved" | transcricao | L56-58 |
| "if we have less than like 30% then we need to be doing better with our email marketing" | transcricao | L172 |
| "30–50% is healthy" | slide, transcricao | L374, L170 |

**Como responder:** **30%** é o piso, sustentado pela aula de métricas e pela faixa
saudável dos dois registros. O "under 30%, um 40%" de L56-58 é hesitação de fala:
ele começa em 30 e emenda 40 sem completar a frase. Não trate 40% como piso
alternativo — 40% é a **meta** (L168, L374, L388), não o piso.

## fundamentos-anuncios-por-dia

| Valor | Registro | Linha |
|---|---|---|
| "over 70 different e-commerce brand ads every single day" | transcricao | L9 |
| "70+ ecom ads per day" | slide | L252 |
| "this is, like, really low balling. I have some studies that say people see, like, 250" | transcricao | L9 |

**Como responder:** ele desmonta o próprio número na frase seguinte a dizê-lo. Dê
os dois: 70+ é o que vai no slide, 250 é o que ele diz acreditar, com a condição
"if you're on, like, a lower—lower demographic". Nenhum dos dois tem fonte citada
("I have some studies" não nomeia estudo nenhum). Se a pergunta depender do número
para uma decisão, diga que o corpus não sustenta nem um nem outro — a função do
dado no argumento dele é retórica, não analítica.

## fundamentos-formula-da-lucratividade

| Valor | Registro | Linha |
|---|---|---|
| "Increased Cost Per Acquisition x Lower LTV x Tariffs \= Lower Profitability" | slide | L268 |
| "increased cost per acquisition plus dec decrereased LTV plus tariffs, you got lower profitability" | transcricao | L9 |

**Como responder:** conflito de formulação, não de conclusão — mas registrado
porque produto e soma não são a mesma coisa e alguém pode citar a fórmula do slide
como se fosse modelo. Não é: nenhum dos três termos é quantificado em lugar nenhum
do corpus. Cite a versão do slide se o pedido for o artefato, a da fala se o pedido
for o raciocínio.

## fundamentos-smart-sending

| Valor | Registro | Linha |
|---|---|---|
| "skip recently emailed profiles, typically you want to send that off" — dito montando uma **campanha** | transcricao | L78 |
| "Smart Sending – Klaviyo feature that skips sending to people recently emailed. **Turn off for flows**\!" | slide (glossário) | L447 |

**Como responder:** os dois dizem para desligar; discordam sobre **onde**. A fala
está no meio do fluxo de criação de campanha e não menciona flows; o glossário
manda desligar em flows e não menciona campanhas — com exclamação, único item do
glossário inteiro com instrução imperativa. "send that off" em L78 é ruído de ASR
para *turn that off*. Responda: ele manda desligar nos dois contextos, cada um
registrado uma vez, e o corpus nunca trata os dois na mesma frase. Não infira uma
regra geral a partir das duas.

## fundamentos-benchmark-do-form

| Valor | Registro | Linha |
|---|---|---|
| "you want to shoot for six to 12% of your total **email revenue**" | transcricao | L104 |
| "or 6 to 12% of your total **site traffic**" — autocorreção na linha seguinte | transcricao | L106 |
| "6-12%" | slide | L380 |

**Como responder:** o denominador correto é **tráfego do site**, não receita de
email — ele se corrige sozinho em L106 e a aritmética que faz em seguida confirma
("if you have 1000 people viewing your site, you want to have at least 60 to, um,
120 people", L108). Trate L104 como lapso de fala, não como posição. A faixa 6-12%
em si tem escada própria e conflito próprio: ver `list-growth-benchmark-de-form`.
Nunca responda o 6-12% isolado.

## fundamentos-klaviyo-melhor-ou-pior

| Posição | Registro | Linha |
|---|---|---|
| "I highly recommend using Klaviyo. It is the best option (…) Klaviyo is just the best" — como **ESP** | transcricao | L32-34 |
| "I highly recommend Klaviyo, it is the best option" | slide | L357 |
| "but Clavio (…) It's just not going to perform as well" — como plataforma de **pop-up** | transcricao | L617 |
| "Oly is my recommended pop-up platform" | transcricao | L617 |
| "it's the superior option. It will always perform better" — sobre Alia | transcricao | L647 |
| "The most used eCommerce email platform, especially for Shopify" | slide (glossário) | L458 |

**Como responder:** não é contradição lógica — é stack de duas camadas, Klaviyo
como ESP e Alia como camada de pop-up — mas produz duas assinaturas pagas, e a
recomendação de fundamentos não avisa disso. Cite sempre as duas camadas juntas. O
único suporte factual que o corpus dá ao "it is the best option" é a linha do
glossário, e ela afirma **market share**, não qualidade. Conflitos irmãos:
`list-growth-alia-vs-klaviyo` e `design-klaviyo-vs-omnisend`. Os links de ESP são
de afiliado (L34, L358, L360) — declarar sempre.

## fundamentos-deliverability-e-facil

| Posição | Registro | Linha |
|---|---|---|
| "Deliverability is like a half. Just because it's so easy" | transcricao | L21 |
| "Why only a 3.5 pillar? Because it's easy\!" | slide | L348 |
| "with health and deliverability. This is where things get a little bit comm- complicated" | transcricao | L225 |
| "if you do struggle with it, that's what we will walk you through here in this program" | transcricao | L22 |

**Como responder:** as quatro linhas estão na mesma faixa, a 200 linhas de
distância. A tese do meio pilar é dele e é sustentada nos dois registros — mas a
condição que ele anexa ("as long as you only send to engaged profiles and send
good content", L349) é justamente o que o módulo de deliverability leva centenas de
linhas para ensinar, com rampa de warming, registros DNS e reparo. Responda: para
ele deliverability é meio pilar porque a **condição de sucesso é subproduto** dos
outros três, não porque o assunto seja simples — e ele próprio chama a terminologia
de complicada (L225) e abre exceção para quem já está em apuros (L22).

---

# doutrina

`doutrina-segundos-de-atencao` está em [[_conflitos#Conflitos entre módulos]].

## doutrina-narrador-da-aula-de-ia

O corpus tem pelo menos dois narradores. Absorve `copy-narrador-nao-e-max`.
É o único tipo de erro deste corpus que é invisível na saída.

**A prova** (transcrição `# File-ChatGPT Copywriting`, L5667-5865):

| Valor | Registro | Linha |
|---|---|---|
| "something that **Max had put together himself**" — terceira pessoa | transcricao | L5753 |
| "this is the exact template that **our copywriters** use" | transcricao | L5799-5801 |
| "the prompt that **we** use internally" | transcricao | L5707 |
| "Lucky for you, **I've created** the Email Marketing Brain" — primeira pessoa | slide | L6774 |

**A assinatura de abertura caiu como critério.** A tabela que ficava aqui separava
os narradores por "Hello, hello" / "Yo, yo" e listava **L7603** entre os do outro
narrador. [[_autoria]] §5 provou o contrário: L7603 abre o walkthrough de Figma
com "Hello, hello" e é comprovadamente Max — em **L7817** ele digita `@max` e diz
"Let me just make sure it actually **tags me**". O pronome coletivo também caiu:
"our copywriters" está no deck escrito de Max (L6790) e "message our team" em
L8692.

O critério que sobreviveu é o **idioleto** ([[_autoria]] §2.1): ausência de "I
recommend" / "my favorite" / "I like to", presença de "at the end of the day" e
"obviously", mais o fecho coletivo "thank you guys… see you in the next one".

| Faixa falada | Classificação | Vídeo |
|---|---|---|
| L5667-5866 | **`outro-provado`** | ChatGPT Copywriting — prova nominal em L5753 |
| L4202-4421 · L4444-4675 · L4686-4828 · L4846-5154 | `outro-provavel` | os quatro vídeos de Campaigns |
| L5888-6082 · L6101-6248 | `outro-provavel` | Infographics · Subject Lines |
| L8381-8646 | `outro-provavel` | Deliverability |
| L8773-9109 | `outro-provavel` | Optimization |

Fechos do segundo narrador: "So thank you very much for giving this a watch. See
you later." (L4827), "Thank you guys for giving it a watch and see you in the next
one." (L5865), "feel free to hit us up if you have any questions that we can
clarify." (L9108).

**Como responder:** só L5667-5866 tem prova nominal (`outro-provado`). As outras
nove faixas são `outro-provavel`: inferência **estilométrica**, forte e auditável,
mas não prova — não está provado que a voz não é dele ([[_autoria]] §7.3). O laudo
bloco a bloco está em [[_autoria]]. A regra prática:

1. Nada de L5667-5865 é citável como fala do Max. `registro: outro-narrador`.
2. Trechos dos outros oito vídeos: citar como "o material do curso diz", não "o
   Max diz", e dizer por quê se perguntarem.
3. **O deck GAMMA é artefato escrito dele** e não carrega o problema — carrega a
   bio assinada (L3419, L9269: "I'm Max. I'm the founder of Well Copy") e
   reivindicações em 1ª pessoa (L6774, L1208, L8311, L9522). Onde a doutrina tem
   slide, ela se sustenta.
4. Onde o Max corrobora em vídeo próprio, a atribuição volta a ser segura — é o
   caso de desconto (L6261), texto puro (L5230) e skimmability (L7163).

**Ressalva de cobertura deste arquivo:** a aplicação do laudo cobriu as notas das
cinco pastas afetadas, não este registro entrada por entrada. Restam aqui cerca de
uma dúzia de trechos que ainda dizem "ele" sobre faixa `outro-provavel` —
concentrados em `campanhas-*`, `deliverability-warming-*` e `otimizacao-*`. Antes
de citar qualquer conflito como fala de Max, confira a linha contra a tabela de
faixas acima.

Consequência para este registro: onde um lado de um conflito cai num bloco
`outro-provavel`, a entrada avisa. Isso decide pelo menos um conflito —
`otimizacao-peso-do-basico` — e muda a natureza de outro,
`doutrina-ia-primeiro-rascunho`.

## doutrina-ia-primeiro-rascunho

Absorve `copy-papel-da-ia`.

| Valor | Registro | Linha |
|---|---|---|
| "hiring a junior copywriter. And you can get the first draft" | outro-narrador | L5691-5693 |
| "the intention isn't to give you the finished product, is to be used as a guide, a framework" | outro-narrador | L5689-5691 |
| "use it as a framework builder, not a first draft machine" | outro-narrador | L5855 |
| "junior copywriting assistant. Great for brainstorming… skeleton drafts" | outro-narrador | L5845 |
| "ChatGPT isn't going to give you the finished product for your copy. Rather, you should use it as a guide and as a framework." | slide | L6733-6735 |
| "I'm literally just going to have chat GPT like do this all for me or at least help me create like the whole outline of this email" | transcricao (Feastables) | L6399 |
| pede e usa headline, sub-headline, body copy, bullets e subject line gerados | transcricao (walkthrough) | L6386-6411 |
| usa a IA só para dois períodos de body copy, depois do layout pronto | transcricao (Gymshark) | L6274-6276 |

**Como responder:** desde `doutrina-narrador-da-aula-de-ia`, este conflito mudou de
natureza. **Não é o Max se contradizendo** — a regra (L5689-5691, L5855) está
dentro do bloco provado de outro narrador; a prática (L6386-6411) é dele, em bloco
`max-provado`. E a regra se contradiz sozinha: L5691-5695 prescreve "you can get
the first draft" e L5855 proíbe "first draft machine", mesmo vídeo, 164 linhas de
distância. O slide (L6733-6735) é dele e sustenta a versão fraca ("guide and
framework"), não a proibição.

A leitura mais fiel: a regra sobrevive na **iteração e na edição**, não na origem do
texto. Nos dois walkthroughs ele nunca publica saída direta — descarta metade
(L6394), pede variações (L6393, L6405), costura os pedaços à mão (L6397). O que a
prática contradiz é a proibição do primeiro rascunho, não a exigência de reescrita.
Diga as duas coisas; não escolha. Ele também data a própria posição: "with where
we're currently at" (L5683-5685), prevendo que a regra deixa de valer.

## doutrina-formato-do-slice

| Valor | Registro | Linha |
|---|---|---|
| "for the type of file I like to do a JPEG you can do whatever you want really" | transcricao (Gymshark) | L6337 |
| "we're going to save them as image slices as PGs" | transcricao (Calvin Klein) | L6489 |
| "You can do a PNG or a JPEG. Honestly, it really doesn't matter." | transcricao (upload) | L8035 |
| "export everything to XPNG. Export eight layers." | transcricao (upload) | L8040 |

**Como responder:** ele declara explicitamente que tanto faz (L8035) e demonstra
JPEG num vídeo e PNG noutro. Não há especificação a defender. O que é constante nos
três é o **2x na exportação** (L6337, L6489, L8034) e o teto de altura de ~800
(L6489, L8033) — esses sim são a regra. "PGs" em L6489 é ruído de ASR; não deduzir
se ele disse PNG ou JPEG ali. Ver `design-altura-do-slice`.

## doutrina-receita-da-agencia

Absorve `flows-receita-da-agencia`. **Três valores de credencial.**

| Valor | Registro | Linha |
|---|---|---|
| "coming from a $40 million email marketer" | transcricao (Gymshark) | L6260 |
| "which has generated $40 million for clients in the past few years" | transcricao (Gymshark) | L6350 |
| "I've made $100 million making emails for e-commerce brands" | transcricao (Calvin Klein) | L6359 |
| "over $100M in email attributed revenue for clients" | slide (deck de flows) | L3419 |
| "an email marketer who has generated $200M for brands in their platform" | slide (deck de flows) | L3428 |
| credencial de "$200 million" em 1ª pessoa | transcricao (masterclass YT) | L5204 |

**Como responder:** $40M, $100M e $200M, em vídeos e decks diferentes, sempre como
credencial de abertura. Os dois números do deck de flows estão a nove linhas de
distância um do outro, sem reconciliação — e o de $200M aparece dentro de um bloco
de recomendação paga do Klaviyo (L3426-3429). O corpus não datou os vídeos, então
não dá para dizer se é crescimento ou inconsistência. Nenhum é auditável. Se a
credencial for citada, cite todas com a linha, ou não cite nenhuma — **nunca
escolha a maior**.

## doutrina-lista-de-marcas

Absorve `design-nomes-de-marca`.

| Marca | Fala | Slide |
|---|---|---|
| Brez / Breeze | "Breeze" (L8003) | "Brez" (L8347) |
| Munk Pack | "Monk Pack" (L8003) | "Munk pack" (L8339) |
| Bite / Byte | "Byte" (L7881-7885), "Bite" (L8003) | "Bite" (L8348) |

**Como responder:** grafia de nome próprio em transcrição de áudio não é confiável.
Vale a grafia do slide, que é texto escrito — é especificação, alguém vai buscar a
marca. A lista canônica é: Casely, Munk pack, Kizik, Duck Camp, Magic Mind, Magic
Spoon, Olipop, Dr. Squatch, Seed, Brez, Bite (L8338-8348) — as mesmas 11 marcas na
mesma ordem nos dois registros. "Breeze" aparece também no módulo de copy (L5189)
como nome de produto numa peça de exemplo.

---

# list-growth

Registro `transcricao (YT)` = aula 6, L986-1084, vídeo público, não a aula do
curso. Três entradas desta pasta absorvem versões vindas dos módulos de SMS e de
fundamentos — estão marcadas.

## list-growth-tipos-de-form

| Valor | Registro | Linha |
|---|---|---|
| "there are four different types of pop-up forms that we typically will like to run" | transcricao (YT) | L998 |
| "Use one of the 5 form types to pick a starting point" | slide | L1200 |
| Quatro nomeados: classic, micro-commit, quiz, spin-to-win | transcricao | L639-645, L998-1016 |
| "Great Examples" rotula quatro cards: Quiz, Micro-Commit, Micro-Commit, The Classic — repete um e omite spin-to-win | slide | L1292-1298 |

**Como responder:** são **quatro**. O slide promete cinco (L1200), mas o corpus
inteiro só nomeia quatro, e a fala é explícita na contagem (L998). Diga os quatro e
diga que o slide anuncia um quinto que não aparece em lugar nenhum. Não invente o
quinto: full page e flyout aparecem como *estilos de exibição do Klaviyo* (L667,
L706, L1266), não como tipos de form, e promovê-los a quinto tipo seria preencher
a lacuna por analogia.

## list-growth-time-delay

Absorve `sms-delay-do-popup` e `fundamentos-time-delay-do-form`. **Oito
formulações.**

| Valor | Registro | Linha |
|---|---|---|
| "a four to six second time delay trigger" | transcricao (fundamentos) | L194 |
| "Time delay 4 to 12 seconds. Don't use any other time delay" | transcricao | L655 |
| "something between 4 to 12 seconds, you can start off with four" | transcricao | L820 |
| "Time delay is 4-12 seconds" | slide | L1251 |
| "Try 4 second vs 12 second to start" | slide | L1274 |
| "a plain time delay of 4 to 8 seconds. Typically, in most cases, I'm doing a 6second delay" | transcricao (YT) | L1033 |
| "it's based after 5 seconds" — trigger default que ele mostra no Alia | transcricao | L982 |
| "you want your trigger to be around 6 to 10 seconds after page load (…) I usually just like to set a time delay like 6 seconds" | transcricao (SMS) | L9239-9240 |

**Como responder:** a faixa mais sustentada é **4-12 segundos** — está na fala do
curso (L655, L820) e no slide, duas vezes (L1251, L1274). O piso de **4 segundos**
é o único valor comum a todas as faixas do módulo e é o que ele manda usar como
ponto de partida (L820). O valor que ele **efetivamente executa** é 6 segundos, e
isso aparece em dois vídeos diferentes (L1033, L9240). Dê 6s como default e 4-12s
como espaço de teste. Nunca diga "cerca de 8 segundos" — a média das faixas não
existe no corpus. O critério de decisão dele é o teste, e a métrica é submissões
totais, não taxa (L1274).

Detalhe que vem de fundamentos e não pode se perder: **L194 amarra o benchmark de
conversão a um delay que o módulo dono do assunto não usa** — os 6-12% de opt-in
foram medidos, segundo aquela linha, com 4-6s, enquanto a prescrição operacional é
4-12s. No módulo de SMS a faixa vira 6-10s (L9239), que é a única que não começa
em 4.

## list-growth-benchmark-de-form

Absorve `sms-benchmark-de-form`. **Não há um número; há uma escada, e ela é o
ponto.**

| Valor | Papel da frase | Registro | Linha |
|---|---|---|---|
| "a lot of people still end up with 3 to 5% optin rates when we want to be 10% plus" | onde a maioria empaca | transcricao (YT) | L1028 |
| "around 2 to 3% of website visitors" | o que ele audita no mercado | transcricao (SMS) | L9238 |
| "around 6 to 12%... minimum 6%, ideally 10% plus" | piso e faixa-alvo | transcricao | L194 |
| "I gave the KPI of 6 to 12% opt-in rates" | KPI nomeado | transcricao | L597 |
| "6-12%" | tabela de metas | slide | L380 |
| "8% to 10%" | alcançável no vídeo dele | transcricao (SMS) | L9239 |
| "It's only through testing... that you reach 10%+ opt in rates" | resultado de iteração | slide | L1186 |
| "Even your 10%+ forms should continue to be tested to try to reach 20%+" | meta seguinte | slide | L1187 |
| "We've some brands where we're getting 20 to 30% opt-in rates" | teto que ele diz ter | transcricao | L194 |
| Case do vídeo: "a submission rate of 28%" | caso único | transcricao (YT) | L994 |
| Case do slide: 2.5% → 8.75% | caso único | slide | L1175-1181 |

**Como responder:** responda com a escada inteira e com o papel de cada número.
**6%** é o piso declarado (L194). **6-12%** é a faixa-alvo nomeada de KPI (L194,
L597) e o que vai na tabela de metas (L380). **10%+** é o que ele chama de
resultado de iteração (L1186, L1028). **20%+** é a meta seguinte para quem já
chegou a 10% (L1187). **2-3%** e **3-5%** não são meta: é onde ele diz que a
maioria está (L9238, L1028). Nunca dê um valor único e nunca some faixas. O
racional que amarra tudo: "set and forget = burning cash" (L1183). Sobre o
denominador (tráfego do site, não receita de email), ver
`fundamentos-benchmark-do-form`.

## list-growth-botao-x

| Valor | Registro | Linha |
|---|---|---|
| "OPTIONAL: There is no 'x' button, rather a 'Close Form' button underneath the submit button" | slide | L1256 |
| "optional there's no X button, but rather a close form button underneath the submit button. Something I highly recommend you guys test" | transcricao | L661 |
| "Hide that X and just have a no thanks closed form button instead. Always performs better" | transcricao | L663 |
| Executa como padrão no mobile: opacidade a zero + botão "no thanks" | transcricao | L752-764 |
| Executa como padrão no desktop: "Highly recommend doing that. It's going to improve conversions" | transcricao | L840 |
| "I like to do it in every chance that I can because it always converts better" | transcricao (YT) | L1049 |

**Como responder:** o rótulo é OPTIONAL, o comportamento é obrigatório. Em duas
frases seguidas ele diz "optional… something I highly recommend you guys test" e
depois "Always performs better" (L661-663), e nas três demonstrações de tela ele
faz sempre. Responda: está marcado como opcional no checklist, mas ele executa em
100% dos casos demonstrados e usa "always performs better" duas vezes. O que **não**
é opcional em nenhuma versão é dar uma saída explícita ao usuário — "We need to
give people an option" (L1047).

## list-growth-exit-intent

Absorve `sms-exit-intent`.

| Valor | Registro | Linha |
|---|---|---|
| "when a visitor is exiting, which I don't recommend. Exit intent isn't very good... sometimes it'll misfire" — sem ressalva de dispositivo | transcricao | L818-820 |
| "Exit intent pop-ups work good on desktop, but for mobile, they misfire a lot and I'm not a fan of them" | transcricao (YT) | L1035 |
| "I wouldn't recommend doing like scrolling or anything like that or exit intent because sometimes it can misfire" | transcricao (SMS) | L9240 |

**Como responder:** a rejeição é geral em dois trechos (L818-820, L9240) e
condicionada a dispositivo num terceiro (L1035). A versão mais específica explica as
outras: o problema é mobile — e L818 acontece justamente dentro do tutorial
**mobile**, onde L1035 também rejeitaria. Responda: ele não usa exit intent, o
motivo explícito é misfire, e a única distinção por dispositivo que o corpus faz
está em L1035, que salva o desktop. O que ele usa nos dois casos é time delay.

## list-growth-teaser

| Valor | Registro | Linha |
|---|---|---|
| "Typically, I don't use these because they can get in the way of a customer shopping. So, in a lot of cases, I recommend not using it" | transcricao | L700 |
| "It's usually not the best on mobile. Oftent times I won't even have a teaser. You can just delete it. But desktop I usually like to have it" | transcricao (YT) | L1073 |

**Como responder:** mesma forma do exit intent: a rejeição genérica (L700) está no
tutorial mobile, e a versão com ressalva (L1073) confirma o mobile e libera o
desktop. Responda com as duas linhas. O racional contra é sempre o mesmo — o teaser
atrapalha quem está comprando (L700).

## list-growth-imagem-lateral

| Valor | Registro | Linha |
|---|---|---|
| "side image kind of messes up the sizing... it changes the formatting for whatever reason on mobile" | transcricao | L712-716 |
| "We have actually tested this and right image typically works best. You could also do left" | transcricao | L852 |
| "You can also do no image" | transcricao | L854 |
| "You should even test the placement of photos either next to the form or as a backdrop to the form" | slide | L1278 |

**Como responder:** não é o mesmo assunto visto duas vezes: L712 é uma queixa de
**layout no mobile** e L852 é um **resultado de teste no desktop**. Responda: sem
imagem lateral no mobile (quebra o dimensionamento), imagem à direita no desktop —
uma das poucas afirmações do módulo em que ele nomeia um teste como origem (as
outras: L615, L1007, L1041). A menção a *placement* e *backdrop* é só do slide
(L1278); a fala cita apenas "test the different imagery" (L669).

## list-growth-alia-url-e-oferta

| Valor | Registro | Linha |
|---|---|---|
| `olealearn.com` | transcricao | L984 |
| `alialearn.com` | slide | L1246 |
| `aliapops.com` | transcricao (YT) | L1053 |
| "you do get a 30-day free trial" | transcricao | L649 |
| "Say Max sent you when you book a call and you'll get a gift ;)" | slide | L1245 |
| "Just say that Max sent you a 30-day free trial" | transcricao (YT) | L1014 |
| Grafia do nome, oito variantes: Aulia, Oly, Olla, allia, Allie, Ollia, Olea, Alia | transcricao | L615, L617, L647, L651, L966, L974, L984, L1013 |

**Como responder: nunca afirmar uma URL.** Liste as três e diga que o corpus dá
três. `olealearn.com` vem de ASR de áudio falado e é a menos confiável;
`alialearn.com` é o único que aparece como link escrito, no slide; `aliapops.com`
é falado no vídeo e parece ser a galeria de exemplos, não a página de cadastro — mas
o corpus não confirma isso. Sobre a oferta: trial de 30 dias aparece em dois
registros (L649, L1014), o "gift" ao mencionar o nome dele numa call aparece só no
slide (L1245); ambas podem coexistir e o corpus não diz se coexistem. Em qualquer
resposta sobre Alia, inclua a declaração de conflito de interesse dele (L649).

## list-growth-alia-vs-klaviyo

| Valor | Registro | Linha |
|---|---|---|
| "I highly recommend using Klaviyo. It is the best option" / "Klaviyo is just the best" (como ESP) | transcricao | L32 / L34 |
| Klaviyo para form: "It's just not going to perform as well" | transcricao | L617 |
| "Oly is my recommended pop-up platform" | transcricao | L617 |
| "it's the superior option. It will always perform better" | transcricao | L647 |
| "Alia is the superior option and will perform much better, but it's an extra cost (the ROI is worth it every time)" | slide | L1242-1243 |
| Todos os tutoriais gravados são no Klaviyo | transcricao | L684-858, L1030-1081 |

**Como responder:** não é contradição, é uma stack de duas camadas — Klaviyo como
ESP, Alia como camada de pop-up — mas produz duas ferramentas pagas e precisa ser
dito assim. O critério de decisão que ele dá é econômico e está inteiro em L651:
"run the free trial, and then then run just a plain Klaviyo offer and see if the
increase in opt-ins is worth it". Ele nunca quantifica a diferença. Sempre
acompanhar do conflito de interesse (L649). Ver `fundamentos-klaviyo-melhor-ou-pior`.

## list-growth-popup-vs-full-page

| Valor | Registro | Linha |
|---|---|---|
| "Form covers at least 75% of screen" | slide + transcricao | L1253, L657 |
| Template de partida é o "multi-step email and SMS full page form" | transcricao | L686 |
| "typically, I am going to recommend just doing a pop-up" | transcricao | L708 |
| "usually the bigger your form is the better converting, but you have to sacrifice some customer experience... So I typically will do a popup" | transcricao | L834 |
| "pop-up vs full page vs flyout" é um dos A/B tests | slide + transcricao | L1266, L667 |

**Como responder:** a regra é ≥75% da tela, não 100%. Ele parte de um template
chamado "full page" mas troca o estilo para pop-up nas duas demonstrações (L708,
L834), e declara o trade-off: full page converte mais e custa experiência. O corpus
resolve isso mandando testar (L1266). Não diga que ele recomenda full page só
porque o nome do template diz isso.

## list-growth-checkbox-preselecionado

Conflito dentro da própria linha do slide. Ver também
`sms-instrucoes-de-optin-sao-de-email`, que encontra o mesmo defeito reaproveitado
na seção de SMS (L9332).

| Valor | Registro | Linha |
|---|---|---|
| "Check **Preselected** so that the email marketing sign-up check box is preselected at the checkout by default for customers without an account or customers who are on your email subscription list" | slide | L1120 |
| "The email marketing sign-up check box isn't preselected for customers who have opted out of email marketing **or who aren't on your email subscription list**" | slide | L1120 |
| "We want it to be auto-checked so someone will be added to the list" | slide + transcricao | L1115, L537 |

**Como responder:** a segunda metade de L1120 anula a primeira: se não é
pré-marcado para quem não está na lista, o checkbox não serve para captar novos —
que é exatamente o objetivo declarado (L537, L1116). O texto é colado da
documentação do Shopify e não foi revisado. Responda: a intenção dele é inequívoca
(auto-marcado, L537/L1115), mas o passo a passo do slide contém uma ressalva que
contradiz o objetivo, e o comportamento real do Shopify tem que ser verificado na
plataforma — nota `procedimento`, datada, e o próprio corpus avisa que "Shopify
changes this a lot" (L537).

## list-growth-friccao-na-signup-page

| Valor | Registro | Linha |
|---|---|---|
| "In the subheading field, enter a short description of what your customer will receive by subscribing" | slide | L1134, L1146 |
| "Enter a heading for your newsletter signup. For example, 'Subscribe to our newsletter'" | slide | L1133, L1146 |
| "Tip: Remove as much friction as possible\!" | slide | L1127 |
| "Screw the events, screw the product drops, screw the exclusive content... What they want to know is what am I going to get right now?" | transcricao | L549 |
| "Give us your email for 10% off. Enter email. That's all we want" | transcricao | L549 |
| até campo de gênero derruba conversão | transcricao | L551 |

**Como responder:** a fala vence — é julgamento, não especificação, e o slide se
contradiz sozinho (dá a dica de remover fricção em L1127 e manda escrever subheading
em L1134). Os passos do Shopify em L1129-1135 são documentação copiada, não doutrina
dele; são idênticos aos passos de embed em L1142-1148. Responda: a headline é o
desconto, e "Subscribe to our newsletter" é exatamente o tipo de copy que ele
descarta (L547-549).

## list-growth-lista-de-ofertas

| Valor | Registro | Linha |
|---|---|---|
| Main: % OFF, $ OFF, Free Shipping, Free X Gift w/ Order. BONUS: Mystery Discount. Other: Giveaway Entry, Free Guide, Early Access | slide | L1221-1230 |
| mesma lista, mesma ordem | transcricao | L627-639 |
| "some sort of variation of a percent off, dollar off, mystery discount, or free gift" — sem free shipping, com mystery promovido a principal | transcricao (YT) | L1019 |

**Como responder:** a lista completa é a do slide (L1221-1230), e a fala do curso a
confirma item por item. A versão do YouTube é um resumo de quatro que omite free
shipping e trata mystery discount como opção de primeira linha em vez de bônus.
Diferença de ênfase, não de doutrina — mas se perguntarem "quais são as opções",
responda a lista de sete do slide, com a separação Main/Other preservada, porque ele
declara que o segundo grupo converte pior (L637-639).

---

# flows

Faixa: L1307-3403 (transcrição) e L3404-4186 (slide GAMMA). `flows-onde-testar`
está em [[_conflitos#Conflitos entre módulos]].

## welcome-contagem-de-emails

| Valor | Registro | Linha |
|---|---|---|
| "at least three emails" | transcricao | L1436 |
| "At least 3 emails long" | slide | L3493 |
| "ideally more" | transcricao | L1438 |
| "four to five emails (…) the sweet spot" | transcricao | L1440-1442 |
| "you could also do six" | transcricao | L1444 |
| "some welcome flows that are like 15 emails" | transcricao | L1446 |
| "three to four emails (…) some can be six to eight" | transcricao | L1520-1522 |
| "3-4 emails others should be 6-8 emails" | slide | L3502 |

**Como responder:** o piso é **3** e é a única posição que aparece nos dois
registros e na lista de non-negotiables (L3493) — comece por ela. Acima do piso ele
oscila entre 4-5, 6, 3-4/6-8 e casos de 15. **Não faça média.** O critério que ele
dá não é numérico (L1524-1534): o que importa para o cliente, quais são as objeções,
e se a compra é impulso ou decisão demorada. Produto de impulso pede menos email;
decisão demorada e produto complicado pedem mais.

## welcome-cadencia

| Valor | Registro | Linha |
|---|---|---|
| "our email is one to two days apart" | transcricao | L1458 |
| "Emails 1-2 days apart" | slide | L3494 |
| "let's hit them every single day right when they opt in (…) we need to hit them every day" | transcricao | L1468-1472 |

**Como responder:** 1-2 dias é a posição sustentada — está na fala e é
non-negotiable no slide. O "every single day" aparece 10 linhas depois, na mesma
fala, justificado pela janela de 5 dias (L1460): se a conversão fica difícil depois
do quinto dia, um email por dia cabe na janela e um a cada dois dias usa-a inteira.
As duas leituras são compatíveis com o argumento dele; o corpus nunca escolhe.
Mostre as duas e cite a janela de 5 dias como o critério real.

## welcome-estrutura-da-sequencia

| Desenho | Emails | Registro | Linha |
|---|---|---|---|
| "Base strategy" — E1 welcome+desconto, E2 lembrete da oferta, E3 "expires in 40 hours" + categorias + bloco de suporte, E4 text-based do founder | 4 fixos, sem filler | transcricao | L1548-1586 |
| "Template" — Welcome #1 → 1-5 fillers → Last Chance → Text Based Support | 4 a 8 | transcricao + slide | L1596-1646, L3511-3528 |
| Recap final — welcome → "Maybe we have three filler emails" (L2310) → "absolute last chance" → "is everything okay?" (L2314) | 6 | transcricao | L2308-2318 |

**Como responder:** o "template" é o desenho que existe nos dois registros e o
único que o slide formaliza — é a resposta padrão. Mas registre que a "base
strategy" da mesma aula é outra coisa: tem bloco de suporte dentro do email 3 e
prazo de 40 horas, que o template não tem, e não usa filler. E que o recap com o
qual ele fecha a aula (L2308-2318) fixa três fillers, número que nenhum dos dois
desenhos anteriores fixa. O slide promete "**Base Strategy:**" em L3509 e não
entrega nada — o diagrama que reconciliaria os dois não sobreviveu.

## welcome-contagem-de-fillers

| Valor | Registro | Linha |
|---|---|---|
| "One to five filler emails" | transcricao | L1612 |
| "One to five filler emails" | transcricao | L2178 |
| "1-5 Filler Emails" (heading do template) | slide | L3517 |
| "Insert 1-4 Filler Emails" (heading da seção) | slide | L3544 |
| "the 1–5 educational emails" (corpo da mesma seção) | slide | L3547 |

**Como responder:** **1-5**. Três ocorrências contra uma, e a única ocorrência de
1-4 é um heading contrariado pelo próprio corpo do slide duas linhas abaixo (L3544
vs L3547). É o caso mais limpo de erro de digitação do módulo — mas registre-o como
conflito mesmo assim, porque a regra do corpus é nunca corrigir o material em
silêncio.

## welcome-catalogo-de-fillers

| Valor | Registro | Linha |
|---|---|---|
| 21 ângulos catalogados | slide | L3558-3578 |
| 14 ângulos citados | transcricao | L2136-2166 |

**Como responder:** o slide vence, é artefato. A lista falada é subconjunto estrito
da do slide, sem nenhum item exclusivo ("even more testimonials", L2148, é o
`Testimonials` do slide, L3563). Não inclui Research Study Highlight, Media
Publications, Behind The Scenes, Tips and Tricks, UGC Content, Staff Picks nem Brand
Values. Não há hierarquia entre os ângulos em nenhum dos dois: é catálogo, não
ranking. A única preferência explícita do corpus inteiro é pelo Our Story — "I love
to include these" (L1854-1856).

## welcome-prazo-da-oferta

| Valor | Onde no flow | Registro | Linha |
|---|---|---|---|
| "The welcome offer expires in 40 hours" | email 3 da base strategy | transcricao | L1560 |
| "Welcome discount expires tonight" | variação text-based do last chance | transcricao | L2244 |
| "I extended it for 24 more hours" | text-based support email | transcricao | L2292 |

**Como responder:** os três são prazos, em três emails diferentes, e o corpus nunca
os reconcilia nem diz qual é o padrão. 40 horas é o único que aparece como
especificação de sequência; os outros dois são leitura de exemplo de marca. Se
alguém pedir "qual prazo usar no welcome", a resposta honesta é que o corpus dá 40
horas uma vez e nunca mais volta ao assunto.

## welcome-valor-do-desconto

| Valor | Registro | Linha |
|---|---|---|
| 20%, $10, $20, 10%, 15% — todos como exemplo de marca | transcricao | L1476, L1726, L2208, L2218, L2248 |
| nenhuma regra em nenhum registro | — | — |

**Como responder: recusar.** O corpus não fixa valor de desconto para o welcome, nem
dá critério para escolher. O que existe é a exigência de que o desconto seja lembrado
em todos os emails (L1474-1480, L3495) e a de que o primeiro email o entregue
imediatamente (L1426). O valor é decisão da marca e o corpus não opina.

## site-abandon-delay-so-na-fala

| Valor | Registro | Linha |
|---|---|---|
| "I like to wait four hours (…) usually performs the best, but test it for your brand" | transcricao | L2369-2375 |
| "a one hour time delay" (variante agressiva) | transcricao | L2371 |
| nenhum delay | slide | L3607-3664 |

**Como responder:** 4 horas como padrão, 1 hora como variante agressiva, e diga que
o número vem só da fala — o slide não especifica delay para este flow. Ele mesmo
enquadra como testável, não como regra. Não há delay declarado entre o email 1 e o
email 2 em nenhum dos dois registros.

## browse-abandon-janela-de-delays

| Valor | Registro | Linha |
|---|---|---|
| "wait one hour and then one day between the rest of these emails" | transcricao | L2476-2478 |
| "**4 emails works well here**, spaced out over 3-4 days" | slide | L3678 |

**Como responder:** os dois são a mesma janela vista de ângulos diferentes. Não é
contradição de valor, é diferença de granularidade. Use a fala, que é a única
acionável, e cite o slide como confirmação da ordem de grandeza. Registre que os
intervalos entre os emails 2, 3 e 4 nunca são especificados separadamente.

## browse-abandon-definicao-do-gatilho

| Valor | Registro | Linha |
|---|---|---|
| "they click onto a product page, but they didn't go any further" | transcricao | L2446 |
| "views a product on your site but doesn't add anything to their cart" | slide | L3669 |

**Como responder:** o trigger é o mesmo nos dois (`Viewed Product`); o que muda é a
condição implícita de permanência. "Didn't go any further" é mais amplo que "doesn't
add anything to cart" — pela versão do slide, quem adiciona ao carrinho sai do browse
abandon; pela versão da fala, sai qualquer um que avance de qualquer forma. Nenhum
dos dois registros declara essa condição de saída como configuração. Diga que o
corpus não especifica.

## cart-checkout-conteudo-igual-ou-diferente

| Posição | Verbatim | Registro | Linha |
|---|---|---|---|
| não precisa ser diferente | "we really don't need different content for cart abandoned and checkout abandoned. You really don't." | transcricao | L2689-2691 |
| a agência sempre faz diferente | "we always do for our clients. We make them different, slightly different." | transcricao | L2693-2695 |
| o ideal é diferente, mas não é necessário | "ideally, if you can make the content a little bit different, that would be best, but not completely necessary" | transcricao | L3015 |
| meio-termo | "To save time, you can use the same emails for both of these flows. If you have time, try to make them slightly different." | slide | L3795 |

**Como responder:** a posição de referência é a do slide, porque é a única que
concilia as três falas: mesmo conteúdo é aceitável, conteúdo diferente é melhor, e o
que decide é tempo disponível. Mas mostre que na fala ele diz as três coisas em
minutos — inclusive que a própria agência dele sempre faz diferente, o que contradiz
na prática o conselho que ele acabou de dar. O que **não** muda entre os dois flows é
o bloco dinâmico (L3885-3913). Ver `cart-checkout-bloco-dinamico`.

## cart-checkout-ausencia-total-de-delays

| Campo | Cart | Checkout | Registro | Linha |
|---|---|---|---|---|
| Delay do 1º | ausente | ausente | transcricao e slide | L2618-3019, L3777-3914 |
| Delays seguintes | ausente | ausente | transcricao e slide | idem |
| Filtros | ausente | ausente | transcricao e slide | idem |
| Condição de saída | ausente | ausente | transcricao e slide | idem |

**Como responder:** não é conflito, é **lacuna** — e é a lacuna mais cara do módulo,
porque estes são os dois flows de maior intenção e o corpus especifica quatro emails
com subject lines e quick tips para eles sem dizer quando disparam. **Nunca preencher
por analogia com browse abandon.** Se perguntarem o delay do cart abandon, a resposta
é que o corpus não informa, e o vizinho mais próximo é o princípio geral de que time
delay é "the biggest lever" (L4143) e deve ser testado.

## cart-checkout-bloco-dinamico

| Flow | Bloco | Fonte da imagem | Registro | Linha |
|---|---|---|---|---|
| Browse | `Table` | `{{ event.ImageURL }}` | slide | L3767-3770 |
| Browse | "you create a split (…) create a table block" | — | transcricao | L2598-2600 |
| Cart | `Split` | `{{ event.ImageURL }}` | slide | L3885-3888 |
| Cart | "we are using a split dynamic image on the left" | — | transcricao | L2971 |
| Checkout | `Table` + `Dynamic` + `Row collection` | `{% if item.product.variant.images.0.src %}…` | slide | L3901-3907 |

**Como responder:** vale o slide, é artefato. A hesitação da fala em L2598-2600
("split… table block") é ruído. A diferença real entre browse/cart e checkout é
estrutural: os dois primeiros lêem variável de evento único, o terceiro itera
`event.extra.line_items`. Já a diferença `Table` (browse) vs `Split` (cart) para o
mesmo tipo de dado não tem explicação técnica no corpus — ele mesmo diz "it's going
to be a little bit different for whatever reason (…) this is what we've always done"
(L2987-2991).

## post-purchase-escopo-temporal

| Janela | Verbatim | Registro | Linha |
|---|---|---|---|
| 7 dias | "those next seven days is like the warmest this person ever is" | transcricao | L3040 |
| 14 dias | "post-purchase flow as within 14 days" | transcricao | L3162 |
| 14 dias | "relevant in the first 14 days after a customer purchase" | slide | L3971 |
| ~3 semanas | "a couple of weeks after somebody bought (…) it's been nearly three weeks" | transcricao | L3194-3198 |

**Como responder:** 14 dias é o escopo do flow — é o único número que aparece nos
dois registros (L3162, L3971) e é onde o slide enquadra os emails opcionais. Os 7
dias não são o escopo: são a janela de temperatura máxima do cliente, o argumento
para os dois primeiros emails serem rápidos. O exemplo de ~3 semanas está dentro da
lista que o slide diz ser de 14 dias — é a inconsistência real, e é do próprio
material. Registre que L3162 vem truncada na transcrição e que o slide é quem
confirma o número.

## replenishment-janela

| Valor | Registro | Linha |
|---|---|---|
| "days 30 through 60-ish, 21 through 60-ish" (autocorreção no ar) | transcricao | L3233-3235 |
| "just wait 21 days" | transcricao | L3251 |
| "Set whatever time delay you want" | transcricao | L3289 |
| nenhuma janela | slide | L3982-4039 |

**Como responder:** 21 dias é o único número que ele fixa (L3251), e a autocorreção
em L3233-3235 mostra que ele hesitou entre 30 e 21 no mesmo fôlego. Mas o critério
que ele dá é o produto, não o calendário: "whenever somebody needs to replenish
typically" (L3251-3253), com os três exemplos de duração de consumo (L3996-3998). E
no segundo email ele abandona a especificação de vez (L3289). Responda com 21 dias,
a hesitação e o critério de produto — nesta ordem.

## replenishment-desconto

| Posição | Verbatim | Registro | Linha |
|---|---|---|---|
| sem desconto pesado | "Drives repeat purchases without heavy discounts" | slide | L3992 |
| sem desconto pesado | "drives repeat purchases without heavy discounts" | transcricao | L3247 |
| com 15% | "we're also giving you 15% off" | transcricao | L3299 |
| com 15% | "15% Off Your Next Refill\!" / código "COOL15" | slide | L4035-4037 |

**Como responder:** a contradição está **dentro de cada registro**, não entre eles —
os dois prometem o flow como alternativa ao desconto e os dois dão 15% off no segundo
email. Não há precedência para aplicar. A conciliação possível é a que ele mesmo
sugere sem nomear: o email 1 "leans on timing and convenience" (L4004), o desconto só
entra depois de o lembrete sem desconto falhar, e ele marca esse email como opcional
(L3269). "Without heavy discounts" pode ser lido como "sem depender de desconto", não
"sem desconto". Ofereça a leitura marcando que é leitura, não texto.

## winback-cadencia

| Valor | Registro | Linha |
|---|---|---|
| "email one, day zero" e nada depois | transcricao | L3326 |
| "Email 1 (Day 0) · Email 2 (Day 7) · Email 3 (Day 10)" | slide | L4063-4065 |

**Como responder:** use o slide, é a única especificação completa. Registre que a
fala não dá nenhum intervalo além do Day 0, e que o slide encurta o segundo intervalo
(3 dias) em relação ao primeiro (7 dias) sem explicar por quê — o racional que ele dá
é qualitativo, a progressão emocional → incentivo → urgência (L4066), não temporal.

## winback-definicao-do-segmento

| Versão | Verbatim | Registro | Linha |
|---|---|---|---|
| slot vazio | "**Segment Definition for 90 Day Winback Flow:**" seguido de nada | slide | L4057 |
| metade recente | "placed an order at least once, but they've placed an order zero times in the last 90 days" | transcricao | L3318 |
| completa (fora da faixa) | "subscribed **AND** placed order at least once in the past 150 days **AND** placed order zero times in the last 90 days" | slide | L5589 |
| completa (fora da faixa) | "placed an order in the past 150 days, but they haven't made one in the last 90" | transcricao | L5057 |

**Como responder:** a definição completa é a de L5589 — tem as três condições e está
no registro de slide. A versão da aula de flows (L3318) omite o teto de 150 dias, o
que muda o segmento materialmente: sem o teto, entra também quem comprou uma vez há
três anos. Diga que o módulo de flows dá a versão incompleta e que a completa está no
módulo de segmentação. O slide de flows promete a definição (L4057) e entrega um slot
vazio. Ver `campanhas-winback-janela`.

## flows-participacao-na-receita

| Valor | Denominador | Registro | Linha |
|---|---|---|---|
| "20% of Total Shopify Revenue from Automated Emails" | receita total da loja | slide | L3408 |
| "around 50% of your total email revenue" | receita de email | slide | L3438 |

**Como responder:** não são o mesmo número — 20% da receita da loja e 50% da receita
de email têm denominadores diferentes e podem coexistir. Mas o corpus nunca os
relaciona, então não infira a receita total de email a partir dos dois. Cite ambos com
o denominador explícito.

**O que este slug não resolve sozinho.** Os 20% de L3408 têm um par no módulo de
fundamentos com **o mesmo denominador**: "flows generating **80%** of the total store
revenue" (L22). Mesma medida, 4x de diferença, e nenhum dos dois registros comenta o
outro — a comparação está escrita em `fundamentos-denominador-dos-80` e tem que ser
lida junto desta. Os dois slugs continuam separados de propósito: aqui o defeito é
**dois números no mesmo deck**, lá é **um denominador que troca no meio de uma linha**.
Não funda um no outro.

**Proveniência:** L3438 não é fonte independente de L326 (fundamentos) — é a mesma
frase, dentro do mesmo bloco "What Are Email Flows?" copiado entre os dois decks
(L324-326 = L3436-3438). Conflito irmão: `fundamentos-denominador-dos-80`.

---

# campanhas

Faixa: L4187-5236 (transcrição) e L5237-5599 (slide GAMMA). **Atenção de
atribuição:** os quatro blocos de fala deste módulo (L4189-5154) são classificados
`outro-provavel` por [[_autoria]]. Onde a fala é o único lado de um conflito, isso
pesa.

## campanhas-sweet-spot-de-frequencia

Absorve `flows-frequencia-de-campanha` e o ponteiro `campanhas-cadencia-semanal`.

| Valor | Registro | Linha |
|---|---|---|
| "two to four campaigns per week is generally going to be the sweet spot" | transcricao | L4220 |
| "the two to four times per week is really hitting the sweet spot" | transcricao | L4242 |
| "Send between 2x - 4x per week" | resumo do módulo | L4192 |
| "a consistent cadence of 2-4 email campaigns per week" | slide | L5249 |
| "**3x per week** is typically the sweet spot" | slide | L5255 |
| "I wouldn't recommend going lower than 2x per week no matter your ecom store size" | slide | L5256 |
| "three to four campaigns per week, which is more likely than not what we're looking for" | transcricao (prompt de IA) | L4554-4556 |
| "three to four campaigns per week" | transcricao (flows) | L2367 |
| "people are receiving them three times per week" | transcricao (flows) | L3386 |

**Como responder:** **2-4x/semana** é a posição sustentada — aparece nos dois
registros, quatro vezes, incluindo o bullet-resumo do módulo e a página de abertura
do próprio slide que depois diz 3x. O "3x" de L5255 é uma frase única, dentro da
faixa 2-4, e lê melhor como *ponto de partida* que como contradição: a mesma página
mantém 2-4 como cadência e 2x como piso inegociável (L5256). Diga a faixa, aponte o
3x como o número que ele escolhe quando forçado a um só, e cite o critério real, que
não é numérico — porte, tamanho de lista e capacidade criativa da equipe (L4244,
L4276). As duas linhas do módulo de flows (L2367, L3386) aparecem só como premissa
de outro argumento e não acrescentam posição.

## campanhas-tier-250k-1m

| Valor | Registro | Linha |
|---|---|---|
| "4x per week" | slide (tabela) | L5297 |
| "probably in that three to four emails a week, just depending on what's going on" | transcricao | L4268-4270 |

**Como responder:** é especificação de tabela, então o slide vence: **4x por
semana**. Mas registre que a fala abre para 3-4 e condiciona a "what's going on" — é
o único tier onde os dois registros divergem; os outros três batem.

## campanhas-o-que-determina-a-frequencia

| Valor | Registro | Linha |
|---|---|---|
| receita **OU** visitantes mensais — só isso | slide | L5290 |
| receita e tráfego, **mais** tamanho de lista ("if you have a smaller list, 5,000, 10,000, 20,000 people, you're not going to want to send five or six times a week") | transcricao | L4276-4280 |
| receita e tráfego, **mais** carga de trabalho criativa da equipe | transcricao | L4244 |

**Como responder:** use a tabela como entrada, mas não pare nela. A fala acrescenta
dois gates que a tabela não tem, e ambos são de corte, não de elevação: lista pequena
e equipe pequena puxam para baixo mesmo quando a receita autorizaria subir. O piso de
2x/semana (L5256) não é negociável em nenhum dos dois registros.

## campanhas-cadencia-alta-vs-tier-1m

**Conflito novo, registrado nesta consolidação.** O mesmo deck lista 5-7x/semana
como faixa danosa e, 30 linhas depois, prescreve 5-6x/semana para o tier de topo. A
faixa prescrita está **dentro** da faixa condenada.

| Valor | Registro | Linha |
|---|---|---|
| "**Sending 5-7x Per Week**" seguido de "Higher unsubscribes / Customers can get annoyed / Dilutes the power of your messaging / Revenue plateaus" | slide | L5264-5269 |
| tabela: "\| $1M/mo+ \| 250k/mo+ \| **5-6x per week** \|" | slide (tabela) | L5298 |
| "If you go to five, five to seven times per week, **there are cases where this might fly and we'll get into that in a sec.** But generally what you risk here, you're going to get higher unsubscribes and upset customers" | transcricao | L4240 |
| "a mil a month plus, you can kind of start getting more creative at the five to six times a week, simply because your list is going to be growing more likely than not. You have a lot of skews and can get a lot more creative with the segmentation. **So even if you're sending five to six times per week, it might not be to the same people every time.**" | transcricao | L4270-4276 |

**Como responder:** o slide **não reconcilia** — ele condena 5-7x numa página e
prescreve 5-6x na tabela três seções adiante, sem uma palavra ligando as duas. Quem
ler só o deck sai com uma contradição fechada. A reconciliação existe uma única vez
no corpus inteiro, e é **falada**: em L4240 ele anuncia a exceção ("there are cases
where this might fly") e em L4270-4276 a entrega — a 5-6x/semana o envio **não vai
para as mesmas pessoas todas as vezes**, porque a lista é grande o bastante e o
catálogo variado o bastante para segmentar. Ou seja, o que torna 5-6x seguro não é o
faturamento, é a segmentação que o faturamento viabiliza.

Ao responder: dê os dois números do slide com as linhas, diga que o próprio deck se
contradiz, e entregue a condição falada como condição — não como parte da tabela,
porque ela não está lá. Duas ressalvas obrigatórias: (a) a fala deste módulo é
classificada `outro-provavel` em [[_autoria]], então a única reconciliação
disponível vem do registro mais fraco; (b) a mesma condição aparece escrita no deck
de **SMS**, para o mesmo tipo de exceção — "If you are sending more you need to make
sure you're really segmenting your list to only send to extremely engaged segments"
(L9368) —, o que mostra que o mecanismo é doutrina dele, mas o deck de campanhas
nunca o escreveu. Não trate 5-6x como recomendação livre para quem fatura $1M/mês.

## campanhas-ratio-grafico-texto

Ponteiro alternativo: `campanhas-proporcao-grafico-texto`.

| Valor | Registro | Linha |
|---|---|---|
| "80-20 (…) Favoring graphics, 75-25 maybe, depending on the brand" | transcricao | L4346-4348 |
| "roughly four graphic based emails to one textbased email. Maybe a 5:1" | transcricao (masterclass) | L5232 |
| "aim for a **4:1 graphic to plain text ratio**" | notas do masterclass (timestamp 13:18) | L5174 |

**Como responder:** três versões, e é sério — 80-20 é 4:1, 75-25 é 3:1, e o
masterclass oferece 4:1 ou 5:1. A única faixa que os três cobrem é **maioria
gráfico, com texto puro entre 1 em 4 e 1 em 5**. O 75-25 (3:1) é o outlier e vem com
a ressalva "depending on the brand". Nenhum registro tem precedência clara: o
masterclass é vídeo de YouTube anexado, não o deck; e as notas com timestamp são
resumo editorial, não fala dele. **Nunca dê um número só.**

## campanhas-frequencia-de-texto-puro

| Valor | Registro | Linha |
|---|---|---|
| proporção do mix (4:1 / 5:1 / 80-20 / 75-25) | transcricao + notas | L4346-4348, L5232, L5174 |
| "at least send **twoish** textbased emails every single month" | transcricao | L5232 |
| "Send at least **two plain text emails per month** (one educational, one promotional)" | notas do masterclass | L5175 |

**Como responder:** as duas regras estão na mesma frase (L5232) e não fecham. Um piso
de 2/mês e um ratio de 4:1 só coincidem por volta de 10 envios no mês — que é
exatamente o volume do calendário-exemplo dele (L4490, L5345). A 2x por semana o ratio
pede menos de dois e o piso ganha; a 5-6x por semana o ratio pede cinco ou mais e o
piso vira irrelevante. Responda dizendo qual regra morde em qual frequência, nunca
escolhendo uma. Isso é observação de aritmética sobre os números citados, **não
posição dele**: o corpus nunca faz essa conta.

## campanhas-distribuicao-dos-pilares

| Valor | Registro | Linha |
|---|---|---|
| "a good cadence is having an **even amount** of emails for these 5 pillars" | slide | L5344 |
| "if you send 10 emails a month; you could have 2 (…) 2 (…) 2 (…) 2 (…) then 1 sale that takes 2 emails" | slide | L5345 |
| "Again, there's **no exact formula or method**" | transcricao | L4490 |
| "you might want to send four or five sale emails throughout the month" (mês da maior promoção do ano) | transcricao | L4490 |

**Como responder:** os números batem — o desacordo é sobre o *status* da regra. O
slide apresenta divisão par como cadência recomendada; a fala, no mesmo exemplo, nega
que exista fórmula e abre exceção para mês de promoção grande. Conflito de julgamento,
então a fala vence: divisão par é ponto de partida, não regra.

## campanhas-limiar-vip

| Valor | Registro | Linha |
|---|---|---|
| "Someone has placed order at least **4 times** over all time" | slide (tabela) | L5590 |
| "if someone's placed **five** orders on the site, give them an additional discount" | transcricao | L5103 |

**Como responder:** especificação de segmento → slide vence: **4 pedidos**. Registre
que a fala diz 5. E registre o critério que ele mesmo dá acima do número: "use your
gut on what counts as a VIP" (L5083) e "use your gut on what counts as a VIP customer"
(L5590), com a preferência declarada por contagem de pedidos em vez de LTV, porque
contagem é previsível e permite avisar o cliente quantas compras faltam (L5590).

## campanhas-suppress-list

| Valor | Registro | Linha |
|---|---|---|
| "received email at least 5 times over all time **AND** opened email zero times in the last 365 days **OR** bounced email at least 3 times over all time **OR** marked email as spam at least once over all time" | slide (tabela) | L5592 |
| "received at least five to ten emails over all time, opened zero times in the last year, bounced email, you know, multiple times, or marked as spam" | transcricao | L5129 |
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
| "That's your **80%** list. That's where you're going to get the majority of your sales" | transcricao | L4652-4654 | **rótulo de Pareto** + afirmação qualitativa — não é percentual |
| "relying on this for **80-90%** of our sends" | transcricao | L5139 | share de **envios** |
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
| "opened or clicked emails in the last **30, 60, 90** days, depending on how wide you want to get" | transcricao | L4949 |
| "your **30-, 60-, 90-day** engage list, depending on how old the Klaviyo account is" | transcricao | L5151 |
| "That 80% is going to be that **30, 60, 90-day** engage list" | transcricao | L5017-5019 |

**Como responder:** 90 dias é o padrão e o que se digita — está na tabela e no
fechamento do slide. A fala não contradiz: ela dá o **critério de variação**, e o
critério é útil — largura desejada do alcance (L4949) e **idade da conta Klaviyo**
(L5151), que é o único fator que ele oferece para justificar 30 ou 60 em vez de 90.
Conta nova, janela mais curta. Responda com 90 e ofereça o critério. Ver
`deliverability-lista-base-padrao`, onde a fala usa 60 como envio normal.

## campanhas-winback-janela

| Valor | Registro | Linha |
|---|---|---|
| "placed order at least once in the past **150 days** AND placed order zero times in the last **90 days**" | slide (tabela) | L5589 |
| "people who have placed an order in the past **150 days**, but they haven't made one in the last **90**" | transcricao | L5057 |
| "placed an order zero times in the last **hundred days** (…) but placed an order at least once in the last **180**" | transcricao | L5071 |

**Como responder:** 150/90 é canônico — está nos dois registros. O 100/180 não é
contradição, é alternativa que ele mesmo oferece e condiciona: "Maybe your brand has a
longer buying lifecycle and that makes sense" (L5075). O título da linha do slide já
avisa: "Time frames will vary based on your store and how soon people typically come
back" (L5589). Dê 150/90 como default e 100/180 como o ajuste declarado para ciclo de
compra longo. A leitura conceitual dele é "right in that three to six month mark"
(L5059).

## campanhas-janela-do-segmento-de-interesse

| Valor | Registro | Linha |
|---|---|---|
| "at least once **over all time**" (viewed / added to cart / started checkout / placed order) | slide (tabela) | L5591 |
| "viewed creatine at least once **over time**, added creatine to cart at least once **over time**" | transcricao | L5119-5121 |
| "viewed creatine **in the last 30 days**, added creatine to their cart **in the last 30 days**, or proceeded to check out with creatine **in the last 30 days**" | transcricao | L4965 |

**Como responder:** slide vence — **over all time**, e a fala confirma em L5119-5121.
O "last 30 days" de L4965 aparece antes, num exemplo improvisado durante a explicação
de casos de uso, não na parte em que ele define o segmento. Trate como versão inicial
descartada pela definição posterior, mas registre.

## campanhas-limiar-de-hipersegmentacao

| Valor | Registro | Linha |
|---|---|---|
| "Don't be concerned with any other segments until you are doing **$1M/mo** or have very specific use cases" | slide | L5583 |
| "this changes (…) as you're doing **a million a month, 10 million a month, seven, eight figures**" | transcricao | L5007 |

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

# copy

`copy-janela-de-atencao` está em [[_conflitos#Conflitos entre módulos]] (dentro de
`doutrina-segundos-de-atencao`). `copy-numeracao-dos-principios` e
`copy-takeaways-por-email` estão em [[_conflitos#Conflitos dentro do mesmo registro]].
`copy-medir-por-abertura`, `copy-papel-da-ia` e `copy-narrador-nao-e-max`
resolvem para outros slugs — ver o índice.

## copy-subject-line-comprimento

| Valor | Registro | Linha |
|---|---|---|
| "2-5 words in Length" | slide | L6817 |
| os 4 exemplos do slide: 4, 2, 3 e 4 palavras — todos dentro da regra | slide | L6824-6827 |
| escrita ao vivo: "no fuss dumbbell back exercises" (5 palavras) + "no gym no problem" emendado | transcricao | L6341 |
| elogiada ao vivo, saída de IA: "This bar will ruin all chocolate for you" (8 palavras) | transcricao | L6401 |

**Como responder:** o framework (2-5) é o que ele prescreve e o que os exemplos
curados cumprem. Ao vivo ele ultrapassa: emenda duas frases numa SL só (L6341) e
chama de "pretty cool subject line ideas" uma saída de 8 palavras (L6400-6401).
Ressalva honesta: em L6401 ele **não** confirma que escolheu aquela SL — o que ele
diz mais adiante que vai usar é uma headline, não a subject line (L6402). O corpus
prova que ele tolera SL fora da regra; não prova que ele publique uma de 8 palavras.

## copy-subject-line-reticencias

| Valor | Registro | Linha |
|---|---|---|
| SL termina em emoji; "…" é regra de preview text | slide | L6820, L6838 |
| SL "something ending in dot, dot, dot, maybe a question" | transcricao | L6155-6157 |
| "Starting with the question is great. Ending with dot, dot, dot" | transcricao | L6197 |
| ao vivo, SL emendada: "end with DOT do dot" (ASR) | transcricao | L6341 |
| nenhum dos 4 exemplos de SL do slide termina em "…" | slide | L6824-6827 |

**Como responder:** vale o slide para especificação de artefato — SL em Title Case
terminando em emoji opcional; "…" no preview text. A fala e a prática ao vivo colocam
"…" e pergunta também na SL. Registre os dois; não escolha em nome da limpeza.

## copy-open-rate-limite

Absorve `otimizacao-teto-de-abertura`.

| Valor | Registro | Linha |
|---|---|---|
| "at most you can get ~ 10% jump in opens" | slide | L6805 |
| "The biggest open rate difference we've had on an A-B test is… 10%, maybe 15" | transcricao | L6227-6229 |
| "our best, our best subject line and preview text, you maybe see a five, 10% bump in open rates" | transcricao (otimização) | L8934-8936 |

**Como responder:** o slide fixa **~10%**; a fala do módulo de copy estende para
cima ("10%, maybe 15") e a fala do módulo de otimização abre para baixo ("five,
10%"). Dê as três formulações. **Nunca diga "cerca de 12%"** nem ache o teto em 10%
sem dizer que existe a versão 5-10% e a versão 10-15%. Ver
`fundamentos-o-que-move-o-open-rate` para o que isso significa na prioridade.

## copy-multiplicador-de-vendas

| Valor | Registro | Linha |
|---|---|---|
| "generate 3x more than others (same email copy and design)" | slide | L6809 |
| "Subject line A/B test resulting in 3x more sales" | slide | L6811 |
| "generate three to five times as many sales in different AB tests" | transcricao | L6121 |
| teste 1: "3x the placed order rate", "almost 4x the amount of revenue" | transcricao | L6133 |
| teste 2: "nearly 4x the amount of orders" | transcricao | L6133 |

**Como responder:** o slide fixa 3x; a fala abre 3-5x e descreve dois testes com
resultados diferentes (3x placed order rate / quase 4x receita; quase 4x pedidos).
São métricas diferentes — placed order rate, receita, pedidos — e o corpus não diz se
são os mesmos testes. **Cite a métrica junto do número, sempre.**

## copy-preview-text-obrigatorio

| Valor | Registro | Linha |
|---|---|---|
| framework prescreve preview text para todo email | slide | L6829-6838 |
| "preview text expands or reinforces the subject line; use wisely (not just filler)" | resumo do módulo | L6090 |
| "send a subject line and then just no preview text… it actually has worked really well" | transcricao | L6209-6215 |

**Como responder:** os dois valem, em camadas. O framework é o default; a ausência é
jogada de disrupção, e ela só funciona **porque** todo mundo usa preview text ("if you
look in any email, there's preview text for all of these", L6211-6213). Aplicar a
ausência como regra a mata. O corpus não diz com que frequência usá-la.

## copy-nao-complique-vs-framework

| Valor | Registro | Linha |
|---|---|---|
| "Don't overthink it" | resumo do módulo | L6095 |
| "Don't overthink it." (abrindo o framework de PT) | slide | L6831 |
| "\# Don't Overthink It" (slide inteiro) | slide | L6847 |
| "don't have to over complicate it. It's not reinventing the wheel" | transcricao | L6163-6165 |
| dois frameworks prescritivos de 4 regras cada | slide | L6817-6820, L6835-6838 |

**Como responder:** não é contradição real, é hierarquia de esforço. O framework
existe para **eliminar** deliberação, não para adicioná-la: quatro regras que se
aplicam em segundos. O "don't overthink it" ataca a otimização obsessiva de SL,
coerente com a tese de que SL não move abertura (L6805). A resposta correta cita os
dois: siga o framework, não itere além dele.

## copy-nomes-dos-infograficos

| Valor | Registro | Linha |
|---|---|---|
| "Icons" / "Comparison Charts" | resumo do módulo | L5874, L5878 |
| "Icon Graphics" / "Comparison Chart" | slide (deck) | L6668, L6697 |

**Como responder:** mesmos nove tipos, mesma ordem, dois nomes ligeiramente
diferentes. Use o nome do deck. Conflito menor, registrado só para que uma busca por
"Icons" não pareça uma lacuna.

## copy-email-marketing-brain-tamanho

**Conflito novo, registrado nesta consolidação.** O mesmo custom GPT é descrito com
duas unidades diferentes de tamanho, e a fala carrega um dado de tempo que o slide
não tem.

| Valor | Registro | Linha |
|---|---|---|
| "a custom GPT trained with over **500 pages** of email marketing knowledge which can be used to write copy, make calendars, come up with email ideas, and answer email questions you may have" | slide | L6775 |
| "I actually made this with over **500 docs** of email marketing trainings and tons of back and forth and development **over the past 6 months**" | transcricao | L6387 |

**Como responder:** **"pages" e "docs" não são a mesma unidade** — 500 documentos e
500 páginas descrevem corpora de ordens de grandeza diferentes, e o corpus não
converte nem reconcilia. Dê as duas formulações verbatim com a linha e diga que a
unidade diverge. Nunca escolha uma nem produza uma terceira ("cerca de 500 arquivos").

O "**past 6 months**" existe **só em L6387**: é o único dado de tempo de
desenvolvimento do artefato em todo o corpus, e o slide não o repete. Se a pergunta
for sobre quanto tempo o GPT levou para ser construído, a resposta é essa linha e
só ela — e vale lembrar que ela não vem datada, então "6 meses antes" não é
conversível numa data.

Duas notas de atribuição, porque este artefato é o epicentro do problema de autoria:
L6387 está no bloco `max-provado` (MrBeast, L6353-6500) e é primeira pessoa; L6775
é deck, artefato escrito dele. **As duas versões são dele.** Isso contrasta com
L5753 ("something that Max had put together himself"), que fala do mesmo GPT em
terceira pessoa e é a prova do segundo narrador — ver
`doutrina-narrador-da-aula-de-ia`. Ou seja: o mesmo objeto tem três descrições, duas
citáveis como dele e uma não.

---

# design

`design-html-vs-imagem` está em [[_conflitos#Conflitos entre módulos]];
`design-cta-por-produto` em [[_conflitos#Conflitos dentro do mesmo registro]];
`design-segundos-de-atencao` e `design-nomes-de-marca` resolvem para outros slugs.

## design-botao-above-the-fold-sempre

| Versão | Valor | Registro | Linha |
|---|---|---|---|
| Sempre | "Most users won't scroll. Put a CTA button in the hero section so every reader sees it immediately." | slide | L8135 |
| Sempre | "Not every customer will scroll on your email, so you want a button available in the hero section. This way EVERY customer has the ability to visit the site" | slide | L8154-8155, repetido em L8250-8251 |
| Sempre | "we always need to give people the option to click" | transcricao | L7021 |
| 75% dos emails | "Button above the fold for 75% of your email. Don't need to include it in every single one, but I'd recommend majority of them." | transcricao | L7027-7029 |

**Como responder:** a posição mais sustentada é botão above the fold **sempre** —
está em três lugares do deck (L8135, L8154, L8250) e no começo da própria fala
(L7021). A exceção é uma frase só, dele, imediatamente depois de afirmar o contrário
(L7027-7029), e ele mesmo já a enfraquece com "I'd recommend majority of them".
Responda: a regra é sempre; ele admite abrir mão em até um quarto dos emails, sem
dizer em quais. O corpus não dá critério para escolher esse quarto. Cuidado com o
número: ver `design-tres-usos-de-75-por-cento`.

## design-repeticao-de-cta

| Versão | Valor | Registro | Linha |
|---|---|---|---|
| 2-3 vezes | "Repeat your CTA 2–3 times throughout the email." | slide | L8137 |
| sem número | "repeat your CTA throughout the email"; e o contrapeso "Don't confuse that with throwing a shit ton of buttons in your email. That's going to overwhelm the customer." | transcricao | L7051-7059 |

**Como responder:** o número é do slide e vale como especificação: 2-3. Mas a fala
acrescenta o limite superior que o número não carrega — repetir não é encher. O
exemplo dele de repetição correta tem botão na hero, no meio, no fim, mais os botões
individuais de produto (L7063-7065), o que já passa de três se contar os de produto.
Ou seja: 2-3 vale para o CTA **principal**, não para o total de botões do email.

## design-quantidade-de-produtos

| Versão | Valor | Registro | Linha |
|---|---|---|---|
| livre | "You can feature however many products that you want." | transcricao | L7486 |
| poucos | "Ideally not that many." | transcricao | L7488 |
| um | "You can have a product section be just one product as well" | transcricao | L7490 |
| oito | "You can have eight products if you want." | transcricao | L7492 |
| testar | "Just test it." | transcricao | L7494 |
| silêncio | nenhum número | slide | L8274-8290 |

**Como responder:** cinco respostas em oito linhas da mesma fala, e o slide não
arbitra. O que é estável não é a quantidade, é a estrutura: cada produto com botão
próprio e um botão geral no fim (L7496). Responda com a faixa inteira — 1 a 8, com
preferência declarada por poucos — e com o critério real, que é teste, não número.

## design-quantidade-de-bridges

| Versão | Valor | Registro | Linha |
|---|---|---|---|
| 0 ou 1 | "You don't always need a bridge. You could go straight to the product section if you want." | transcricao | L7368-7370 |
| 0, 1 ou 2 | "In some cases you won't have a bridge, in some you'll have two." | slide | L8260 |

**Como responder:** é especificação, então vale o slide: até dois bridges. Mas
registre que a fala nunca menciona dois e não dá exemplo de email com dois, e que o
corpus não diz em que caso o segundo entra.

## design-bridge-e-product-opcionais

| Versão | Valor | Registro | Linha |
|---|---|---|---|
| Opcional, sem frequência | "Bridge is optional, product section is optional, every email is going to have a hero section." | transcricao | L7238 |
| Opcional, mas frequente | "Not every email will have a bridge or a product section, but most will." | slide | L8229 |

**Como responder:** não são versões incompatíveis — são a mesma regra com e sem
frequência declarada. Responda: obrigatória só a hero; bridge e product são opcionais
e, segundo o deck, presentes na maioria dos emails. Footer é universal (L7500, L8293),
o que é diferente de obrigatório por email: é o mesmo bloco em todos.

## design-altura-do-slice

| Versão | Valor | Registro | Linha |
|---|---|---|---|
| 800ish | "I recommend try not to go over kind of like 800ish or so" | transcricao | L8033 |
| 720 | "I recommend doing something like I'd probably maybe go to like 720 right here" | transcricao | L8033 |
| mil | "maybe I can extend this and kind of like push it to like the thousand before we move on to the next section because we're going to be using the same link across this" | transcricao | L8036 |

**Como responder:** os três números saem do mesmo vídeo, e 800 e 720 saem da mesma
linha. Não existe versão do slide para arbitrar. Responda: o teto que ele enuncia é
~800, o valor que ele executa é 720, e ele estica até mil quando o trecho inteiro
compartilha o mesmo link. O critério que governa **não é a altura — é o link**: um
slice por área de link distinto (L8036-8037). A altura é a consequência. Ver
`doutrina-formato-do-slice` para o 2x de exportação e o formato.

## design-blocky

| Versão | Valor | Registro | Linha |
|---|---|---|---|
| Errada, corrigida em cena | "we don't want things to be too blocky because it'll be too easy for someone to scroll" | transcricao | L7538 |
| Correção | "Or excuse me. We if you have sections that are super blocky people might reach the end of a section and not want to move on to the next section." | transcricao | L7540-7542 |
| Confirmação | "Having separate sections that are blocky and unrelated will lead to churn." | slide | L8305 |

**Como responder:** vale a correção, confirmada pelo slide. Seções muito demarcadas
criam ponto de parada — a pessoa acha que acabou e sai. A primeira formulação inverte
a causa e não deve ser citada. Registrado aqui porque a frase errada está no bruto e
um agente que leia só L7538 responde ao contrário.

## design-metodos-de-transicao-ausentes

| Versão | Valor | Registro | Linha |
|---|---|---|---|
| Promete e não entrega | "Here are a few methods to do this:" e nada depois | slide | L8307 |
| Quatro métodos | gradiente; formas/quebras de linha; fundo consistente com elementos em primeiro plano; transição atrás de foto | transcricao | L7552-7586 |

**Como responder:** **lacuna do slide.** Os quatro métodos só existem na fala. Se
alguém pedir "o que o deck diz sobre transições", a resposta é: o deck define o que
são e por que importam (L8304-8306), lista zero métodos, e os quatro vêm da aula. Não
é contradição de conteúdo — mas responder como se fosse do deck seria erro de
atribuição.

## design-klaviyo-vs-omnisend

| Versão | Valor | Registro | Linha |
|---|---|---|---|
| Klaviyo, no título | "Uploading Designs From Figma To Klaviyo" | slide | L8009 |
| Klaviyo, no passo 4 | "Upload your sections as images into Klaviyo" | slide | L8014 |
| Klaviyo, no título da segunda versão | "How To Properly Upload Emails To Klaviyo for Deliverability" | slide | L8742 |
| Plataforma genérica | "Upload compressed slices into your email platform" | slide | L8746 |
| Plataforma genérica, no título do vídeo | "How to Upload Email Designs Properly into ANY Email Sending Platform" | transcricao | L8019 |
| Omnisend, na demonstração | "for this video, I'm going to do to use Omnisend. You can sign up for Omnisend. I'll put the link below. You get a 30% discount if you use me." | transcricao | L8044 |

**Como responder:** o [[_protocolo]] já registra este caso como exemplo da regra 4.
**Nenhum passo é feito no Klaviyo.** Diga sempre, antes de listar os passos: os passos
1-3 são Figma e iloveimg e valem em qualquer contexto; os passos 4-5 descrevem a
interface do Omnisend, plataforma na qual ele tem link de afiliado (L8044, L8063).

## design-passos-do-upload

| Versão | Valor | Registro | Linha |
|---|---|---|---|
| Cinco passos, links e alt text juntos | slice no Figma / salvar como imagens / comprimir no iloveimg / subir no Klaviyo / "Add your links and alt texts :)" | slide | L8011-8015 |
| Cinco passos, alt text e link separados | fatiar e baixar em JPG ou PNG / comprimir no iloveimg / subir na sua plataforma / alt text em todos os slices / link em todos os slices | slide | L8744-8748 |

**Como responder:** mesmo procedimento, duas redações. A segunda é mais explícita em
dois pontos e deve ser preferida: diz "your email platform" em vez de Klaviyo, e
separa alt text de link, que é como o vídeo executa. A primeira omite que o formato
tanto faz — isso só aparece em L8744 e na fala (L8035).

## design-plugins-do-figma

| Versão | Valor | Registro | Linha |
|---|---|---|---|
| Plug-ins como razão principal | "Figma is the best design platform for email on the market for a few reasons. Mainly around your design capabilities, use of Figma app plug-ins, and your file organization." | slide | L8354 |
| Quase não usa | sobre widgets e alignment: "again, I don't even really use those"; sobre effects: "A lot of this stuff is advanced and you really won't really use it"; sobre layer filters: "I rarely use that and I create emails all day, every day" | transcricao | L7799-7803, L7681, L7685-7687 |

**Como responder:** é julgamento sobre ferramenta, então vale a fala. Ele cita dois
plugins pela função (criar GIFs, screenshots to designs — L7797) e descarta widgets. O
escopo real que ele declara é frames, shapes e muitas fotos (L7825-7827). Não venda
plug-ins como razão para adotar Figma.

## design-tres-usos-de-75-por-cento

**Armadilha de leitura, não conflito.** O mesmo número mede três coisas incompatíveis
dentro do mesmo módulo.

| Referente | Valor | Registro | Linha |
|---|---|---|---|
| Esforço na hero | "75% of your efforts should go to this" | slide + transcricao | L8235 / L7258 |
| Emails com botão above the fold | "Button above the fold for 75% of your email" | transcricao | L7027 |
| Marcas auditadas sem botão por produto | "75% of the brands I audit don't have individual shop now buttons" | transcricao | L7089 |

**Como responder:** **nunca cite "75%" sem o referente.** Não é contradição — é
armadilha de recuperação: uma busca por "75%" devolve três linhas que parecem falar
da mesma coisa e não falam. Há um quarto uso, fora do módulo: "Form covers at least
75% of screen" (L1253, L657) — ver `list-growth-popup-vs-full-page`.

---

# deliverability

Faixa: L8363-8646 (transcrição) e L8647-8759 (slide). **Atenção de atribuição:** os
dois blocos de fala (L8365-8517, L8518-8646) são classificados `outro-provavel` por
[[_autoria]]. `deliverability-limiar-de-open-rate`,
`deliverability-unsubscribe-afeta-ou-nao` e `deliverability-registros-dns` estão em
[[_conflitos#Conflitos dentro do mesmo registro]].

## deliverability-passo-de-escalonamento

Quanto se aumenta o volume a cada envio durante o warming.

| Valor | Contexto | Registro | Linha |
|---|---|---|---|
| "gradually increase from 25 to 50 percent percent based on performance" (*"percent percent" = gagueira de ASR*) | "the formula", 05:30 | transcricao | L8556 |
| "you scale up by about fifty to, by about fifty percent each send, as long as you're still getting the metrics that you want" | primeiro envio de 100-300, 08:08 | transcricao | L8569 |

**Como responder:** dê os dois, sem escolher. **Os dois são transcrição** — o deck de
warming nunca foi exportado, então nenhum dos dois tem o peso de slide e a regra de
precedência do protocolo não se aplica. Em L8554 ele diz "the formula, and it's pretty
self-explanatory", o que *sugere* que L8556 esteja sendo lido de um slide — mas o
corpus não diz isso e a hipótese não pode virar registro.

Não diga que "50% é o teto e 25% é o padrão": o corpus não hierarquiza. L8556 dá uma
faixa condicionada a desempenho ("based on performance"); L8569 dá um passo único
(~50%) igualmente condicionado ("as long as you're still getting the metrics that you
want"). A diferença operacional é real e composta: o passo é reaplicado a cada envio,
então 25% e 50% produzem rampas que divergem a cada degrau. O critério que ele próprio
oferece não é numérico: "I always err on the side of caution" (L8569) e "it's much
easier to build your sender reputation (…) than it is to fix it when it's already in a
poor position" (L8555).

## deliverability-primeiro-degrau-da-rampa

| Valor | Contexto | Registro | Linha |
|---|---|---|---|
| "on the first end, you're sending to one to 200,000" | cadência de rampa | transcricao | L8587 |
| "maybe a hundred people, two hundred people, three hundred people, somewhere in that range" | primeiro envio | transcricao | L8569 |
| degraus seguintes: 300 → 500 → 1.000 → 2.000 → 4.000 → 6.000 → 6.000 | mesma cadência | transcricao | L8588 |

**Como responder:** o "200,000" de L8587 é **erro de transcrição, não dado**. É
incoerente com o degrau imediatamente seguinte (300) e com o primeiro envio declarado
em L8569 (100-300 pessoas). O número real do degrau 1 não é recuperável. Responda com
**100-300 pessoas** (L8569) e declare que a linha da cadência está corrompida. Nunca
reproduza "200.000" como primeiro envio — é o erro que quebra a conta.

## deliverability-lista-base-padrao

| Valor | Registro | Linha |
|---|---|---|
| "90 Day Engaged List (You can use any time frame, 90 is recommended to start)" — "This is your base segment for sending all your email campaigns to" | slide | L8734 |
| "for a normal send or normal sends, you might only want to send to your 60 day engage list" | transcricao | L8462 |

**Como responder:** slide vence em especificação — **90 dias para começar** (L8734),
com a ressalva explícita de que a janela é parametrizável ("You can use any time
frame"). A fala usa 60 como envio normal (L8462) e, no exemplo de correção de rota,
também aponta 60 como o lugar seguro para onde voltar (L8474). O critério real não é o
número e sim o resultado: a lista certa é a que entrega 50-60% de abertura (L8727,
L8468) — ou seja, os dois valores são pontos de partida, não regras. Ver
`campanhas-janela-de-engajamento`; a definição do segmento em L8734 é **a mesma linha
de tabela** de L5587, reaproveitada, e não conta como segunda fonte.

## deliverability-caso-mailchimp-escala-final

| Valor | Contexto | Registro | Linha |
|---|---|---|---|
| "a hundred thousand people" | tamanho da lista importada | transcricao | L8611 |
| "about 120,000 people per cent" (*"per cent" = ruído de ASR; o bruto não traz a palavra corrigida*) | volume ao fim da janela de 60 dias | transcricao | L8611 |
| "all the way up to about 100,000" | topo da escala final | transcricao | L8619 |
| "And then we go up to 4,000. 14,000." | degrau após 12.000 | transcricao | L8618 |
| "this got sent out to 40,000, 14,000 people and 7,000 people opened it" | leitura do Google | transcricao | L8621 |

**Como responder:** cite os números verbatim e diga que o caso é **narrado de
memória, com números que não fecham**. 120.000 por envio (L8611) é maior que a lista
importada de 100.000 (L8611) e que o topo declarado de 100.000 (L8619). O "4,000.
14,000" de L8618 é regressão impossível (o degrau anterior já era 12.000) — é gagueira
de ASR corrigindo-se para 14.000. Em L8621 o par "40,000, 14,000" é a mesma gagueira:
7.000 aberturas sobre 14.000 fecham os 50% que ele está demonstrando. **Use o caso
como ilustração de método, nunca como benchmark de volume.** O único número limpo e
verificável do caso é o open rate do primeiro envio: **46.22%** (L8614).

## deliverability-salto-de-45

**Lacuna, não conflito.** Em L8631, "we sent to all the active people, which was about
45" — a **unidade está ausente**. O contexto (degrau anterior de ~26.000, e o
resultado descrito como "a steep jump" que derrubou as aberturas) sugere 45.000, mas o
corpus não diz. **Não completar.** Responda: "about 45", unidade não informada.

---

# otimizacao

Faixa: L8760-9109 (transcrição) e L9110-9211 (slide GAMMA). O registro `resumo do
módulo` é o bloco de bullets da página do curso (L8760-8769) que antecede a
transcrição e termina no link para o deck (L8769) — **não é slide GAMMA**. Essa
distinção decide o primeiro conflito abaixo. `otimizacao-onde-testar` resolve para
`flows-onde-testar` ([[_conflitos#Conflitos entre módulos]]);
`otimizacao-sl-julgar-por-abertura-ou-receita` está em [[#Conflitos dentro do mesmo
registro]]; `otimizacao-teto-de-abertura` resolve para `copy-open-rate-limite`.

## otimizacao-peso-do-basico

Absorve `doutrina-proporcao-basico-avancado`. **Veredicto arbitrado nesta
consolidação** — as duas unidades divergiam; ver a seção
[[#Colisões de slug e veredictos arbitrados]].

| Valor | Registro | Linha |
|---|---|---|
| "90% of results are driven by basics, 10% come from the advanced 'stuff.'" | resumo do módulo | L8764 |
| "80, 90% of the results are driven by the basics. The 10, 20% come from that advanced stuff." | transcricao (`outro-provavel`) | L8778-8780 |
| "90% of the results are driven by the basics. / 10% come from the advanced stuff." | slide | L9120-9121 |
| "that 80% of your results are going to come from setting up the basis" | transcricao (`outro-provavel`) | L9098 |

**Como responder:** **90/10** é o número de registro. Três motivos, nesta ordem:

1. É a versão do deck GAMMA (L9120-9121), que é artefato escrito dele, e do bloco de
   resumo da página do curso que aponta para esse mesmo deck (L8764 → L8769). Não são
   duas fontes independentes: são o deck e o resumo do deck.
2. O conflito é sobre **número**, e a precedência do [[_INDEX]] dá o slide.
3. As duas versões que dizem 80% (L8778-8780 e L9098) estão dentro do bloco de fala
   L8762-9109, classificado **`outro-provavel`** por [[_autoria]] — por **idioleto**:
   zero "I recommend" / "my favorite" / "I like to", "obviously" 9×, fecho coletivo
   "hit us up" em L9108. Não são citáveis como fala do Max.

Dê 90/10 e registre que a fala do módulo abre a faixa para "80, 90%" na abertura e
fecha em 80% no encerramento — marcando que essa fala é de atribuição duvidosa.
**Nunca dar "85%" nem "cerca de 90%".** O ponto que não muda em versão nenhuma é a
consequência prática, e é ela que importa mais que o número: A/B test é etapa 2, e a
etapa 1 é a lista de básicos de L8786-8790 e L9098-9100.

## otimizacao-frequencia-precondicao

Ver também [[_conflitos#Conflitos entre módulos]], onde a frequência de campanha aparece com
todas as versões dos cinco módulos.

| Valor | Registro | Linha |
|---|---|---|
| "getting three to four campaigns a week up and running" (pré-condição para testar) | transcricao | L8788 |
| "We need a consistent cadence of 2-4 email campaigns per week" | slide (campanhas) | L5249 |
| "two to four campaigns per week is generally going to be the sweet spot" | transcricao (campanhas) | L4220 |
| "3x per week is typically the sweet spot" | slide (campanhas) | L5255 |
| tabela por faturamento: 2x / 3x / 4x / 5-6x por semana | slide (campanhas) | L5295-5298 |
| "ideally 3 to 4 times per week" | transcricao (deliverability) | L8557 |

**Como responder:** a faixa oficial do corpus é **2-4/semana** e pertence ao módulo
de campanhas (`campanhas-sweet-spot-de-frequencia`). O módulo de otimização usa
**3-4** como o patamar que precisa estar rodando **antes** de abrir testes — é uma
pergunta diferente (pré-condição de teste, não cadência recomendada), mas os números
não batem, e responder "2-4" a quem pergunta "quando posso começar a testar" perde a
informação. Dê as duas com o papel de cada uma. O critério real dele não é número
único: é faturamento e tamanho de lista (tabela L5295-5298).

## otimizacao-lista-pequena-quantas-repeticoes

| Valor | Registro | Linha |
|---|---|---|
| com "5,000, 10,000, 20,000 people", testar "shouldn't be the primary focus" | transcricao | L8782-8786 |
| com lista de "5,000 to 10,000", testar "three or four times" para concluir | transcricao | L8810-8812 |

**Como responder:** não é conflito de número, é de prioridade — a mesma faixa de lista
aparece como "não é onde você deve gastar tempo" e, um minuto depois, com receita de
repetição. Leitura consistente: com lista pequena o custo de concluir é repetir 3-4
vezes, e é por isso que ele diz que não deve ser o foco. Registre as duas frases; não
escolha.

## otimizacao-horarios-a-testar

| Valor | Registro | Linha |
|---|---|---|
| "Typically, we've found around 11am-12pm to perform the best" | slide | L9148 |
| "Main times to test would be 9am, 12pm, 2pm, and 4pm" | slide | L9149 |
| caso real: 1:45pm bate 11am com ~5x placed orders | transcricao | L8848-8852 |
| público blue collar: "eight or 9 a.m." ou "between four and six" | transcricao | L8844-8846 |
| SMS: "midday from 11am-2pm or evening around 5pm"; evitar antes de 10am e depois de 7:30pm | slide (SMS) | L9509-9516 |

**Como responder:** horário é **output de teste, não input** — a própria aula mostra o
caso em que o horário "que costuma performar melhor" perde por ~5x em placed orders. A
lista do slide (9am, 12pm, 2pm, 4pm) é ponto de partida; a fala amplia para 8am e
4-6pm conforme a rotina do público; e o canal SMS tem grade própria. Nunca apresente
11am-12pm como recomendação fechada.

## otimizacao-lista-redundante

| Item | Registro | Linha |
|---|---|---|
| "Long-Form vs. Short-Form Emails" — "Find the ideal balance of info and brevity." | slide | L9192-9193 |
| "Email Length: Short vs. Long-Form" — "Short emails may drive faster clicks. Longer emails may convert better after building more context." | slide | L9208-9209 |
| "Campaign Send Time" como teste de topo | slide | L9143-9149 |
| "Send Time and Day of Week" de novo na lista de fechamento | slide | L9194-9195 |

**Como responder:** **proveniência, não doutrina.** A lista de fechamento repete o par
long/short duas vezes, com racionais diferentes, e repete send time, que já é teste de
topo. É redundância de deck — mas qualquer contagem de "quantos testes ele recomenda"
sai inflada por isso, e **nenhuma contagem é número do corpus**.

## otimizacao-grafico-numero-de-variantes

| Valor | Registro | Linha |
|---|---|---|
| duas vias: "Graphic vs Text Based" | slide | L9151-9156 |
| três vias: "Graphic vs. Plain Text vs. Branded Plain Text" | slide | L9186-9187 |
| a fala descreve a terceira via (template Klaviyo com nome de marca e footer, montado com blocos) | transcricao | L8982-8990 |

**Como responder:** é o mesmo teste com granularidade diferente. Para "o que testar",
a resposta completa tem três variantes; o branded plain text só é descrito na fala, e
o slide de topo o ignora.

## otimizacao-metricas-do-print

| Leitura | Registro | Linha |
|---|---|---|
| "three X, the number of recipients" (send time) | transcricao | L8850-8852 |
| "about six times the amount of recipients also buying" (categorias) | transcricao | L8916 |

**Como responder:** **lacuna.** Num A/B de split igual o número de destinatários não
muda; a leitura do caso de categorias ("recipients also buying") indica que a coluna
lida é de destinatários que **compraram**. O corpus não define a métrica e nenhum dos
prints está nele. Cite verbatim e diga que a métrica não é definida.

## otimizacao-from-name-testar-ou-prescrever

| Posição | Registro | Linha |
|---|---|---|
| "From Name and Sender Identity" listado como A/B test | slide | L9200-9201 |
| nenhuma menção na fala do módulo — ele salta de curiosity/clarity para CTA text | transcricao | L9052-9054 |
| "update the sender name to be an actual human's name so that it stands out in the inbox" | transcricao | L2413 |
| "Update the sender name to the founders name for a more personal feel" | slide | L3661 |
| "people should open your emails based off your sender name, NOT your Subject line" | resumo do módulo (copy) | L6093 |

**Como responder:** fora deste slide o corpus não trata sender name como variável de
teste, e sim como **prescrição** (nome humano, de preferência o do fundador). O item
existe só no deck de otimização e não tem fala — se citado, marque que é registro
exclusivo de slide, sem julgamento dele por trás.

## otimizacao-deck-duplicado

**Proveniência, não conflito de conteúdo.** Quatro dos cinco testes de topo do deck de
otimização já existiam no deck de flows, sob o heading "Flow Specific A/B Tests"
(L4139). Diff par a par:

| Bloco | No deck de flows | No deck de otimização | Diff do corpo |
|---|---|---|---|
| Flow Time Delays | L4141-4145 | L9176-9180 | idêntico |
| SLs and PTs (as 5 variáveis) | L4153-4162 | L9165-9174 | **1 palavra**: "Ilusing" (L4160) vs "Using" (L9172); "exlcuding" nos dois |
| Graphic vs Text Based | L4164-4170 | L9151-9157 | idêntico |
| Promoting Categories vs Products | L4172-4176 | L9159-9163 | idêntico salvo um espaço duplo em L9162 |
| Long Form vs Short Form | L4147-4151 | *(não existe lá)* | ver abaixo |
| Campaign Send Time | *(não existe lá)* | L9143-9149 | — |

Nos quatro pares o nível de heading muda (`##` no deck de flows, `#` no de
otimização); o corpo é o mesmo. "Long Form vs Short Form" **não** é um quinto par: o
deck de otimização não repete a seção, só cita o tema em dois bullets da lista de
fechamento (L9192-9193, L9208-9209), com redação inteiramente outra.

**Como responder:** importa por dois motivos. Primeiro, "Long Form vs Short Form"
carrega no deck de flows um racional que sumiu no de otimização: "Especially for
flows, we want to test longer form content vs shorter form (…) especially in flows
like abandonments when people have objections. Sometimes it makes sense to be quick
and get an impulse purchase, other times it makes sense to spend time working through
objections" (L4149-4151). Segundo, **o único teste exclusivo do módulo de otimização é
o de send time** — os outros quatro já eram doutrina de flow. Ao responder "o que ele
manda testar", cite a origem, porque o deck de flows contém também a ressalva de que o
campo de teste preferido são as campanhas (`flows-onde-testar`). Slide repetido não é
segunda fonte; o mesmo vale para a linha de tabela do 90 Day Engaged List, idêntica em
L5587 e L8734.

---

# sms

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

# Colisões de slug e veredictos arbitrados

Registro de auditoria da consolidação. Onze arquivos de staging registraram parte dos
mesmos conflitos com slugs diferentes. Regra aplicada: **canônico é o slug do módulo
que possui o registro onde a contradição vive** — quando os dois lados estão no mesmo
deck, é o dono do deck; quando o conflito é transversal por natureza, é `doutrina`.

| Conflito | Slugs concorrentes | Canônico | Situação |
|---|---|---|---|
| Onde testar | `otimizacao-onde-testar` · `flows-onde-testar` | `flows-onde-testar` | veredictos iguais; **os dois lados estão no deck de flows** (L4128 e L4141), o de otimização só carrega a cópia (L9176-9180) |
| Peso do básico | `otimizacao-peso-do-basico` · `doutrina-proporcao-basico-avancado` | `otimizacao-peso-do-basico` | **veredictos divergentes — arbitrado, ver abaixo** |
| Numeração S.C.E. | `copy-numeracao-dos-principios` · `doutrina-sce-numeracao-dos-principios` | `copy-numeracao-dos-principios` | duplicata declarada pela própria unidade de doutrina |
| Benchmark de form | `sms-benchmark-de-form` · `list-growth-benchmark-de-form` | `list-growth-benchmark-de-form` | complementares: as versões de SMS (2-3%, 8-10%) entraram na escada |
| Delay do pop-up | `sms-delay-do-popup` · `list-growth-time-delay` · `fundamentos-time-delay-do-form` | `list-growth-time-delay` | **três slugs para um conflito**; fundamentos era ponteiro puro |
| Exit intent | `sms-exit-intent` · `list-growth-exit-intent` | `list-growth-exit-intent` | complementar: L9240 entrou como terceira versão |
| Checkbox pré-marcado | `sms-instrucoes-de-optin-sao-de-email` · `list-growth-checkbox-preselecionado` | **os dois mantidos** | achados distintos (canal errado × texto que se anula); o defeito compartilhado é descrito uma vez só, em list-growth |
| Narrador da aula de IA | `copy-narrador-nao-e-max` · `doutrina-narrador-da-aula-de-ia` | `doutrina-narrador-da-aula-de-ia` | **colisão nova**; doutrina tem o superconjunto (assinaturas de 9 vídeos) |
| IA como primeiro rascunho | `copy-papel-da-ia` · `doutrina-ia-primeiro-rascunho` | `doutrina-ia-primeiro-rascunho` | **colisão nova**; mesmas linhas, doutrina acrescenta o Gymshark |
| Julgar SL por abertura ou receita | `copy-medir-por-abertura` · `otimizacao-sl-julgar-por-abertura-ou-receita` | `otimizacao-sl-julgar-por-abertura-ou-receita` | **colisão nova**; a versão de otimização acrescenta L8926-8944 |
| Teto do ganho de abertura | `copy-open-rate-limite` · `otimizacao-teto-de-abertura` | `copy-open-rate-limite` | **colisão nova**; o número está no deck de copy (L6805) |
| Credencial de receita | `doutrina-receita-da-agencia` · `flows-receita-da-agencia` | `doutrina-receita-da-agencia` | **colisão nova**; quatro valores num registro só |
| Grafia de nomes de marca | `doutrina-lista-de-marcas` · `design-nomes-de-marca` | `doutrina-lista-de-marcas` | **colisão nova**; a própria unidade de design já apontava para doutrina |
| Cadência de campanha | `campanhas-sweet-spot-de-frequencia` · `flows-frequencia-de-campanha` | `campanhas-sweet-spot-de-frequencia` | **colisão nova**; a entrada de flows era ponteiro |
| Janela de atenção | `doutrina-segundos-de-atencao` · `copy-janela-de-atencao` · `design-segundos-de-atencao` | `doutrina-segundos-de-atencao` | **colisão nova, três vias**; o "antes" de copy e o L8201 de design entraram na tabela única — **veredictos divergentes, ver abaixo** |

**15 colisões resolvidas · 18 slugs redundantes · 126 entradas canônicas.**

## Veredicto arbitrado 1 — peso do básico

**A divergência:** a unidade de `otimizacao` classificou L8764 como `resumo do módulo` e
**recusou-se a resolver** ("as quatro versões são dele, e o ponto é o mesmo em qualquer
número"). A unidade de `doutrina` classificou L8764 como `slide (lista do módulo)` e
**resolveu por precedência** ("está nos dois slides (…) como o conflito é sobre número,
vale o slide").

**A arbitragem, com o bruto aberto:**

1. **L8764 não é slide GAMMA.** O deck de otimização começa em L9110 (`# GAMMA
   OPTIMIZATION`). L8760-8769 é o bloco de bullets da página do curso, e termina em
   L8769 com "Link to document in video: [gamma.app/docs/AB-Testing-Optimization…]" —
   ele **aponta para** o deck. A classificação de `otimizacao` está certa; a de
   `doutrina` está errada. Não são "dois slides": é o deck e o resumo do deck, uma
   fonte contada duas vezes.
2. **Mas isso não sustenta o "não resolver".** Sobra um slide (L9120-9121, 90/10) contra
   duas falas (L8778-8780 "80, 90%" e L9098 "80%"). Conflito de número entre registros
   → a precedência do [[_INDEX]] se aplica → **vale o slide**.
3. **E há um desempate mais forte que a precedência.** O bloco de fala L8762-9109 é
   classificado **`outro-provavel`** por [[_autoria]] (bloco 40): "obviously" 9×, "at
   the end of the day" 3× e **zero** "I recommend" / "my favorite" / "I like to" em
   3.121 palavras, mais o fecho coletivo "feel free to hit us up" em L9108. A saudação
   "Yo, yo" de L8774 **não conta** — o critério caiu (§5). **As duas
   versões que dizem 80% não são citáveis como fala do Max.**

**Veredicto: 90/10.** Registrado em `otimizacao-peso-do-basico`, com as versões de 80%
preservadas e marcadas como atribuição duvidosa. Nenhuma das duas unidades tinha os
três elementos — uma acertou o registro e errou a conclusão, a outra errou o registro e
acertou a conclusão pelo motivo errado.

## Veredicto arbitrado 2 — a janela de atenção "antes"

**A divergência:** a unidade de `doutrina` afirmou que o valor "antes" **não conflita**
("Os três registros dizem 5-10 segundos (L4703, L5500, L6516). Quem responder não deve
inventar divergência aí"). A unidade de `copy` registrou que **conflita** (slide fixa
5-10; a fala hesita entre 3-5 e 5-10).

**A arbitragem:** `copy` está certa e `doutrina` trabalhou com um conjunto incompleto.
L5891 diz, verbatim: "used to be **three to five**, five to 10 maybe". É uma quarta
linha, e ela oferece 3-5. A afirmação de que os três registros concordam é verdadeira
para as três linhas que doutrina listou e falsa para o corpus.

**Veredicto: o "antes" conflita**, com a ressalva de que a única versão discordante
(L5891) está no bloco L5867-6082, classificado `outro-provavel` — ou seja, é a de
atribuição mais fraca. Registrado assim em `doutrina-segundos-de-atencao`. A instrução
"não inventar divergência aí" foi removida; a instrução "não converter em faixa única"
permanece.

## Correções aplicadas a entradas herdadas

| Entrada | O que estava errado | O que passou a valer |
|---|---|---|
| `sms-frequencia` | resolvia por média ("7 mensagens em 31 dias dá menos de 2/semana"), violando a regra 2 do protocolo | dá as versões e os quatro critérios dele (evento · lacuna < 1 semana · dias consecutivos para evento grande · segmentar acima do teto, L9368); a leitura das datas registra que a semana do lançamento passa do teto |
| `flows-onde-testar` / `otimizacao-onde-testar` | as duas afirmavam que "o corpus nunca faz essa distinção" | o deck faz a distinção duas vezes — a palavra "**content**" em L4128 e o heading "**Flow Specific A/B Tests**" em L4139. O que falta é a frase que amarra, não a evidência |
| `campanhas-share-do-90-day-engaged` | apresentado no índice de campanhas como conflito | reclassificado como **armadilha de leitura**: L4838 e L4652 medem vendas, L5139 e L5597 medem envios, e **L4652 nem é percentual** — é rótulo de Pareto (confirmado por L5017-5021) |
| `doutrina-proporcao-basico-avancado` | classificava L8764 como slide GAMMA | L8764 é resumo da página do curso e aponta para o deck (L8769); ver veredicto arbitrado 1 |
| `doutrina-segundos-de-atencao` | afirmava que o "antes" não conflita | conflita; ver veredicto arbitrado 2 |

## Conflitos novos, abertos nesta consolidação

| Slug | Por que ninguém tinha aberto |
|---|---|
| `campanhas-cadencia-alta-vs-tier-1m` | a faixa danosa (L5264-5269) e o tier de topo (L5298) estão a 30 linhas de distância no mesmo deck, em seções com títulos diferentes; a reconciliação está só na fala (L4240, L4270-4276), num bloco `outro-provavel` |
| `copy-email-marketing-brain-tamanho` | "500 pages" (L6775, slide) e "500 docs" (L6387, fala) parecem o mesmo número; a divergência é de **unidade**. O "past 6 months" de L6387 não existe em nenhum outro lugar do corpus |
| `entre-modulos-tabela-de-metricas` | cada unidade comparou a sua tabela com o glossário; ninguém comparou a tabela de fundamentos (L372-380) com a de deliverability (L8713-8719). Divergem em click rate (0,5%/2% vs 0,75%) e unsubscribe (0,3% vs 0,4%) |

## O que parece conflito e não é

Registrado para que ninguém abra entrada nova por engano.

- **Prazo da janela de honeymoon.** A fala dá 30 dias (L22), o slide não dá prazo nenhum
  (L319). Omissão, não contradição.
- **Desconto.** A regra contra desconto vale para campanhas (L4197, L4372-4378); os
  descontos do welcome flow (L3495-3497) e o email de sale do Calvin Klein (L6364-6365)
  estão em outro escopo. Ele delimita, não se contradiz.
- **S.C.E. grafado "SDE"** em L4715 — erro de ASR. O slide (L5504) dá a forma correta.
- **Email share de 40%.** Tabela (L374) e glossário (L388) concordam.
- **Slide reaproveitado não é segunda fonte.** A linha de tabela do 90 Day Engaged List
  é idêntica em L5587 e L8734; os quatro testes de topo são idênticos entre L4141-4176 e
  L9151-9180. Ver `otimizacao-deck-duplicado`.
- **Ordem do S.C.E.** O acrônimo está certo em três lugares; só a numeração erra.
