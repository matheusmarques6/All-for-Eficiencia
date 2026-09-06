# Conflitos — fundamentos

Dezesseis entradas. Faixa: L1-236 (transcrição) e L237-522 (slide GAMMA).
Linhas de fora da faixa aparecem quando o conflito atravessa módulos.

**Particularidade desta faixa:** quatro conflitos são internos ao **mesmo deck** —
a tabela de metas (L372-380) contra o glossário (L384-519). Não é slide contra
fala. É slide contra slide, o que desarma a regra de precedência do protocolo.
O desempate disponível é o de L217: ele **não leu o glossário**, declarou que ia
pular, e a tabela de metas ele defendeu linha por linha na fala. Onde os dois
divergem, a tabela tem fala sustentando; o glossário não tem.

Registro: `T` = transcrição · `S` = slide (tabela de metas ou aula) ·
`S-GL` = slide, seção glossário.

---

## fundamentos-open-rate-glossario

O piso de open rate.

| Valor | Registro | Linha |
|---|---|---|
| "we need to be above 50%. This is the only one where it's like, okay, if you're below 50%, you're fucking something up" | T | L178 |
| "50%+" | S | L376 |
| "Target: 45%+ for engaged segments" | S-GL | L430 |

**Como responder:** **50%** é a posição sustentada — está na fala com a ênfase
mais forte do módulo inteiro e na tabela de metas. Os 45% do glossário aparecem
uma vez, sem fala, numa lista que ele declarou pular (L217). Mas há um detalhe
que não é ruído: o glossário qualifica o alvo — "for engaged segments" — e a
tabela não qualifica nada. Se a pergunta for sobre segmento engajado, dizer que
existem dois números e que o mais exigente é o que ele defendeu. Nunca responder
"47,5%". Este conflito conversa com `deliverability-limiar-de-open-rate`, onde o
mesmo número aparece com **seis** formulações — se a pergunta for sobre warming
ou alargamento de lista, é aquela entrada que vale, não esta.

---

## fundamentos-unsubscribe-glossario

O teto de unsubscribe.

| Valor | Registro | Linha |
|---|---|---|
| "Unsubscribe rates, less than 0.3%" | T | L186 |
| "we want it to be less than 0.3%" (repetido três vezes em L188-190) | T | L188-190 |
| "\<0.3%" | S | L378 |
| "Target: \<0.2%" | S-GL | L436 |

**Como responder:** **0,3%**. É o valor mais repetido do módulo — ele o diz três
vezes seguidas, e no meio disso corrige o próprio slide ao vivo porque o sinal
estava invertido na tela ("that should be the other way around (…) let me
actually fix that right now", L188). O 0,2% do glossário não tem defesa falada. O
diagnóstico associado vale para os dois: muitos unsubscribes = problema de
conteúdo (L190).

---

## fundamentos-spam-glossario

O teto de spam complaint. **Uma ordem de grandeza de diferença.**

| Valor | Registro | Linha |
|---|---|---|
| "we want it to be less than 0.01%" | T | L192 |
| "\<0.01%" | S | L379 |
| "Target: \<0.1%" | S-GL | L438 |

**Como responder:** o conflito mais grave da pasta em consequência prática: 0,1%
é **dez vezes** mais permissivo que 0,01%, e é a diferença entre uma conta
saudável e uma conta em risco de bloqueio. **0,01%** é a posição sustentada —
fala e tabela concordam. Dar o 0,1% do glossário apenas como registro divergente,
nunca como faixa ("entre 0,01 e 0,1%" seria média inventada e a mais perigosa
deste corpus). Diagnóstico associado: "you have a content problem, potentially a
segmentation problem" (L192) — note a hesitação dele no segundo termo.

---

## fundamentos-click-rate-glossario

O alvo de click rate, e se ele se separa por tipo de envio.

| Valor | Registro | Linha |
|---|---|---|
| "In general 0.5% on campaigns and 2% click rates on flows" | T | L184 |
| "In general: 0.5%+ on campaigns 2%+ on flows" | S | L377 |
| "Target: 2–4%+" — sem distinguir campanha de flow | S-GL | L431 |

**Como responder:** o conflito não é só de número, é de **estrutura**. Fala e
tabela separam por tipo de envio e dão o motivo — "flows are higher converting,
and they're more intent based" (L184). O glossário dá um número único, quatro a
oito vezes maior que o alvo de campanha. Responder com a separação: 0,5% em
campanhas, 2% em flows, e citar que o glossário registra 2-4%+ achatado.
Acrescentar a tolerância declarada dele: 1% em campanha ele já considera doente
("I don't feel like that's healthy", L186), e ele mesmo diz que o número é frouxo
("it's really hard to say", L186).

---

## fundamentos-roi-do-email

Quanto o email devolve por dólar.

| Valor | Registro | Linha |
|---|---|---|
| "Email average is $36 plus in return for every $1 spent" | T | L13 |
| "Email averages **$36+ return for every $1 spent**" | S | L285 |
| "Email typically delivers \~40x ROI when done right" | S-GL | L393 |

**Como responder:** **$36+ por $1** — duas ocorrências, dois registros, redação
quase idêntica. O 40x do glossário é uma terceira formulação sem fonte e com
uma condicional que as outras não têm ("when done right"). Nenhum dos três vem
com estudo citado. Se o número for usado, ir junto com o contraste que ele faz na
mesma frase: anúncio devolve "2 to 3 dollar" e há marcas satisfeitas com 0.8 ROAS
(L13).

---

## fundamentos-split-campanhas-flows

Como a receita de email se divide entre campanhas e flows. **Três formulações que
não fecham.**

| Valor | Registro | Linha |
|---|---|---|
| "roughly 50% (…) 60/40, 40/60, depends on the brand a little bit. In general, you want to be around 50/50" | T | L22 |
| "around 50/50 or 40/60, 60/40 anywhere in that range" | T (dashboard) | L60 |
| "We want it to be 40 to 60% each so 40% campaigns, 60% flows. or 60% campaigns, 40% follows. Usually like we want to be in that 60 40 range for both" | T (métricas) | L172-174 |
| "around 50% of your total email revenue with the other 50% coming from campaigns" | S | L326 |
| "**Campaigns:** 40–60% of email revenue **Flows:** 40–60% of email revenue" | S | L375 |

**Como responder:** o **centro é 50/50** e isso é unânime — está nos dois
registros e nas três falas. A divergência é na tolerância: "40/60 ou 60/40"
(L22, L60) descreve dois pontos discretos; "40 a 60% cada" (L172, L375) descreve
um intervalo contínuo. Não é a mesma afirmação, mas as duas produzem a mesma
faixa operacional — 40% a 60% para cada lado. Responder com o centro e a faixa,
e dizer que ele nunca formula isso duas vezes do mesmo jeito. O critério de
decisão que ele dá **não é numérico**: "So it's going to take a little bit of
context" (L22). O uso prático é diagnóstico, não meta: 14% em flows significa
"the flows could use a lot of improvement" (L62), e desequilíbrio significa
"you're probably leaving some revenue on the table by the other one not being
optimized" (L174).

---

## fundamentos-denominador-dos-80

Os 80% em flows são de qual receita.

| Valor | Denominador | Registro | Linha |
|---|---|---|---|
| "flows generating 80% of the total store revenue" | receita da **loja** | T | L22 |
| "They should make up around 50% of your total email revenue" | receita de **email** | S | L326 |
| "roughly 50% of your total email revenue" | receita de **email** | T | L22 |

**Como responder:** as duas frases estão **na mesma linha do bruto** e trocam de
denominador no meio. O pilar #2 define flows como percentual da receita de email;
o caso extremo que ele cita na frase seguinte é percentual da receita da loja.
80% da receita total da loja vindos de flows é um número extraordinário — se for
o que ele quis dizer — e 80% da receita de email é apenas um desequilíbrio dentro
do próprio modelo dele. **Não escolher.** Citar a frase com o denominador que
está escrito e sinalizar que ele contradiz a definição do pilar duas frases
antes. Conflito irmão em `flows-participacao-na-receita`, que registra o mesmo
problema de denominador entre "20% of Total Shopify Revenue" (L3408) e "around
50% of your total email revenue" (L3438).

---

## fundamentos-limiar-de-escalar-aquisicao

A partir de que share de email ele manda voltar a investir em anúncio.

| Valor | Registro | Linha |
|---|---|---|
| "If you're over that, say you're at like 60 percent, that tells you, okay, let's funnel some of our profits back into paid ads" | T (dashboard) | L56 |
| "If you get over 55%, you're kind of like at 60%, then it's like, okay, we need to scale our acquisition" | T (métricas) | L170 |
| "\>55% \= time to scale acquisition" | S | L374 |

**Como responder:** **55%** — está no slide, que vence em especificação, e na
fala da aula de métricas. Os 60% do walkthrough não são erro: L170 mostra que na
cabeça dele os dois números são vizinhos ("over 55%, you're kind of like at
60%"). Dar 55% como gatilho e 60% como o exemplo que ele usa. O racional é o
mesmo nas duas versões e é o que importa: acima da faixa o problema **não é o
email**, é aquisição — "our email channels are doing pretty solid" (L172).

---

## fundamentos-piso-de-email-share

Abaixo de que share o email é o problema.

| Valor | Registro | Linha |
|---|---|---|
| "If you're anywhere under 30%, um 40%, then that tells you, okay, our email systems can be improved" | T (dashboard) | L58 |
| "if we have less than like 30% then we need to be doing better with our email marketing" | T (métricas) | L172 |
| "30–50% is healthy" | S, T | L374, L170 |

**Como responder:** **30%** é o piso, sustentado pela aula de métricas e pela
faixa saudável dos dois registros. O "under 30%, um 40%" de L58 é hesitação de
fala: ele começa em 30 e emenda 40 sem completar a frase. Não tratar 40% como
piso alternativo — 40% é a **meta** (L168, L374, L388), não o piso.

---

## fundamentos-anuncios-por-dia

Quantos anúncios de ecom o consumidor vê.

| Valor | Registro | Linha |
|---|---|---|
| "over 70 different e-commerce brand ads every single day" | T | L9 |
| "70+ ecom ads per day" | S | L252 |
| "this is, like, really low balling. I have some studies that say people see, like, 250" | T | L9 |

**Como responder:** ele desmonta o próprio número na frase seguinte a dizê-lo.
Dar os dois: 70+ é o que vai no slide, 250 é o que ele diz acreditar, com a
condição "if you're on, like, a lower—lower demographic". Nenhum dos dois tem
fonte citada ("I have some studies" não nomeia estudo nenhum). Se a pergunta
depender do número para uma decisão, dizer que o corpus não sustenta nem um nem
outro — a função do dado no argumento dele é retórica, não analítica.

---

## fundamentos-formula-da-lucratividade

Como os três problemas se combinam.

| Valor | Registro | Linha |
|---|---|---|
| "Increased Cost Per Acquisition x Lower LTV x Tariffs \= Lower Profitability" | S | L268 |
| "increased cost per acquisition plus dec decrereased LTV plus tariffs, you got lower profitability" | T | L9 |

**Como responder:** conflito menor e de formulação, não de conclusão — mas
registrado porque produto e soma não são a mesma coisa e alguém pode citar a
fórmula do slide como se fosse modelo. Não é: nenhum dos três termos é
quantificado em lugar nenhum do corpus. É retórica de slide. Citar a versão do
slide se o pedido for o artefato, a da fala se o pedido for o raciocínio.

---

## fundamentos-smart-sending

Desligar o "skip recently emailed profiles" em campanha, em flow, ou nos dois.

| Valor | Registro | Linha |
|---|---|---|
| "skip recently emailed profiles, typically you want to send that off" — dito montando uma **campanha** | T | L78 |
| "Smart Sending – Klaviyo feature that skips sending to people recently emailed. **Turn off for flows**\!" | S-GL | L447 |

**Como responder:** os dois dizem para desligar; discordam sobre **onde**. A fala
está no meio do fluxo de criação de campanha e não menciona flows; o glossário
manda desligar em flows e não menciona campanhas — com exclamação, único item do
glossário inteiro com instrução imperativa. Note que "send that off" em L78 é
ruído de ASR para *turn that off*. Responder: ele manda desligar nos dois
contextos, cada um registrado uma vez, e o corpus nunca trata os dois na mesma
frase. Não inferir uma regra geral a partir das duas.

---

## fundamentos-benchmark-do-form

O 6-12% do pop-up é sobre o quê, e vale quanto.

| Valor | Registro | Linha |
|---|---|---|
| "you want to shoot for six to 12% of your total **email revenue**" | T | L104 |
| "or 6 to 12% of your total **site traffic**" — autocorreção na linha seguinte | T | L106 |
| "around 6 to 12% (…) minimum 6%, ideally 10% plus" | T | L194 |
| "6-12%" | S | L380 |

**Como responder:** o denominador correto é **tráfego do site**, não receita de
email — ele se corrige sozinho em L106 e a aritmética que faz em seguida confirma
(1.000 visitantes → 60 a 120 cadastros, L108). Tratar L104 como lapso de fala,
não como posição. A faixa 6-12% em si tem escada própria e conflito próprio no
módulo de list growth: ver `list-growth-benchmark-de-form`, que registra 6%,
6-12%, 10%+, 20%+, 20-30% e 3-5%. Nunca responder o 6-12% isolado.

---

## fundamentos-time-delay-do-form

Quantos segundos antes de disparar o pop-up.

| Valor | Registro | Linha |
|---|---|---|
| "if we do a four to six second time delay trigger" | T | L194 |
| "Time delay 4 to 12 seconds. Don't use any other time delay" | T (list growth) | L655 |
| "Time delay is 4-12 seconds" | S (list growth) | L1251 |

**Como responder:** encaminhar para `list-growth-time-delay`, que tem as sete
formulações. O que importa registrar **aqui** é que L194 amarra o benchmark de
conversão a um delay que o módulo dono do assunto não usa: o benchmark de 6-12%
foi medido, segundo esta linha, com 4-6s, e a prescrição operacional é 4-12s. O
piso de **4 segundos** é o único valor comum a todas as versões.

---

## fundamentos-klaviyo-melhor-ou-pior

Klaviyo é a melhor plataforma ou a pior.

| Posição | Registro | Linha |
|---|---|---|
| "I highly recommend using Klaviyo. It is the best option (…) Klaviyo is just the best" — como **ESP** | T | L32-34 |
| "I highly recommend Klaviyo, it is the best option" | S | L357 |
| "but Clavio (…) It's just not going to perform as well" — como plataforma de **pop-up** | T | L617 |
| "Oly is my recommended pop-up platform" | T | L615 |
| "it's the superior option. It will always perform better" — sobre Alia | T | L647 |
| "The most used eCommerce email platform, especially for Shopify" | S-GL | L458 |

**Como responder:** não é contradição lógica — é stack de duas camadas, Klaviyo
como ESP e Alia como camada de pop-up — mas produz duas assinaturas pagas e a
recomendação de fundamentos não avisa disso. Sempre citar as duas camadas juntas.
Detalhe adicional: o único suporte factual que o corpus dá ao "it is the best
option" é a linha do glossário, e ela afirma **market share**, não qualidade.
Conflitos irmãos: `list-growth-alia-vs-klaviyo` e `design-klaviyo-vs-omnisend`
(o módulo que promete Klaviyo no título e demonstra tudo no Omnisend). E os dois
links de ESP são de afiliado (L34, L358, L360) — declarar sempre.

---

## fundamentos-deliverability-e-facil

Deliverability é fácil ou é a parte complicada.

| Posição | Registro | Linha |
|---|---|---|
| "Deliverability is like a half. Just because it's so easy" | T | L21 |
| "Why only a 3.5 pillar? Because it's easy\!" | S | L348 |
| "with health and deliverability. This is where things get a little bit comm- complicated" | T | L225 |
| "if you do struggle with it, that's what we will walk you through here in this program" | T | L21 |

**Como responder:** as quatro linhas estão na **mesma faixa**, a 200 linhas de
distância. A tese do meio pilar é dele e é sustentada nos dois registros — mas a
condição que ele anexa ("as long as you only send to engaged profiles and send
good content", L349) é justamente o que o módulo de deliverability leva centenas
de linhas para ensinar, com rampa de warming, registros DNS e reparo. Responder:
para ele deliverability é meio pilar porque a **condição de sucesso é
subproduto** dos outros três, não porque o assunto seja simples — e ele próprio
chama a terminologia de complicada (L225) e abre exceção para quem já está em
apuros (L21). Ver [[deliverability/_index]].

---

## fundamentos-o-que-move-o-open-rate

Se subject line afeta open rate.

| Posição | Registro | Linha |
|---|---|---|
| "It's not your subject line or preview text. It is your segmentation (…) they're going to open your email, **no matter what your subject line says**" | T | L180 |
| "at most you can get \~ 10% jump in opens" | S (copy) | L6805 |
| "The biggest open rate difference we've had on an A-B test is… 10%, maybe 15" | T (copy) | L6229 |
| "our best, our best subject line and preview text, you maybe see a five, 10% bump in open rates" | T (otimização) | L8934-8936 |

**Como responder:** não é contradição frontal — 10 a 15 pontos não tiram uma
conta de 30% para 50%, então "o conserto é segmentação" continua de pé como
prioridade. Mas a negação de L180 é **absoluta** e o resto do corpus não é: em
três lugares ele quantifica o efeito de subject line sobre abertura. Responder na
ordem: primeiro segmentação, que é o que ele manda consertar; depois o teto de
5-15% que copy adiciona. Nunca citar L180 sozinho para afirmar que subject line
não importa — ele dedica um módulo inteiro a subject lines. Conflitos irmãos:
`copy-open-rate-limite`, `otimizacao-teto-de-abertura`,
`otimizacao-sl-julgar-por-abertura-ou-receita`.
