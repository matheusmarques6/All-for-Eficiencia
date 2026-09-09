---
tipo: indice
modulo: flows
assunto: conflitos-flows-pos-compra-e-winback
autor: max-sturtevant
conflitos: [post-purchase-escopo-temporal, replenishment-janela, replenishment-desconto, winback-cadencia, winback-definicao-do-segmento, flows-participacao-na-receita]
status: aprovado
---

Registro dos conflitos do módulo `flows` do corpus de Max Sturtevant sobre pós-compra e reativação: escopo temporal do post-purchase, janela e desconto do replenishment, cadência e definição do segmento do winback, e a participação dos flows na receita. Cada entrada lista os valores divergentes por registro e fecha com um "Como responder".


Faixa: L1307-3403 (transcrição) e L3404-4186 (slide GAMMA). `flows-onde-testar`
está em [[_conflitos#Conflitos entre módulos]].


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
| completa (fora da faixa) | "placed an order in the past 150 days, but they haven't made one in the last 90" | **outro-narrador** | L5057 |

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


