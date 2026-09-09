---
tipo: indice
modulo: fundamentos
assunto: conflitos-fundamentos-plataforma-e-operacao
autor: max-sturtevant
conflitos: [fundamentos-smart-sending, fundamentos-benchmark-do-form, fundamentos-klaviyo-melhor-ou-pior, fundamentos-deliverability-e-facil]
status: aprovado
---

Registro dos conflitos do módulo `fundamentos` do corpus de Max Sturtevant sobre plataforma e operação de envio: smart sending, o benchmark de conversão do formulário, se a Klaviyo é melhor ou pior que as concorrentes e se deliverability é fácil ou difícil. Cada entrada lista os valores divergentes por registro e fecha com um "Como responder".


As quatro entradas `*-glossario` estão na seção
[[_conflitos#Conflitos dentro do mesmo registro]], porque são slide contra slide no mesmo
deck. `fundamentos-o-que-move-o-open-rate` está em [[_conflitos#Conflitos entre módulos]].


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


