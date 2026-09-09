---
tipo: indice
assunto: conflitos-no-mesmo-registro-metas-e-open-rate
autor: max-sturtevant
status: aprovado
---

Os conflitos do corpus Max em que o material discorda de si mesmo dentro do mesmo registro, na parte das metas de métrica e do open rate: a tabela de metas de fundamentos contra o glossário do mesmo deck, com quatro divergências e uma de dez vezes (`fundamentos-open-rate-glossario`, `fundamentos-unsubscribe-glossario`, `fundamentos-spam-glossario`, `fundamentos-click-rate-glossario`), e as doze formulações do limiar de open rate do deck de deliverability (`deliverability-limiar-de-open-rate`).

# Conflitos dentro do mesmo registro — metas e open rate

A precedência do [[mapa-do-corpus-do-max]] — slide vence em especificação, fala vence em julgamento —
só funciona quando os **dois registros discordam entre si**. Boa parte dos conflitos
deste corpus é slide contra slide, no mesmo deck, às vezes na mesma linha. Aqui a
precedência não resolve, e o desempate, quando existe, é por **evidência de autoria
dentro do próprio material**.

**Consequência geral: não presuma que o slide fala com uma voz só.**

## A tabela de metas contra o glossário — quatro divergências, uma de dez vezes

Mesmo deck de fundamentos. A tabela está em L372-380; o glossário, em L384-519. Quatro
métricas divergem.

| Métrica | Tabela de metas (L372-380) | Glossário (L384-519) | Diferença |
|---|---|---|---|
| Open rate | "50%+" (L376) | "Target: 45%+ **for engaged segments**" (L430) | 5 pontos, e o glossário qualifica |
| Click rate | "In general: 0.5%+ on campaigns 2%+ on flows" (L377) | "Target: 2–4%+" — sem distinguir (L431) | 4x a 8x o alvo de campanha |
| Unsubscribe | "\<0.3%" (L378) | "Target: \<0.2%" (L436) | glossário é mais estrito |
| Spam complaint | "\<0.01%" (L379) | "Target: \<0.1%" (L438) | **dez vezes** |

**O desempate, e por que ele existe aqui:** em **L217** ele declara que vai pular o
glossário — "So I am going to gloss over this glossary, I'm going to be gloss over-ing
this email marketing glossary in key terms. You can use these if you want" — enquanto a
tabela de metas ele defendeu linha por linha na fala, com racional, em L168-194. **A
tabela é material que ele sustentou; o glossário é material que ele entregou.** Onde os
dois divergem, vale a tabela.

**Como responder, por slug:**

- **`fundamentos-open-rate-glossario`** — **50%** é a posição sustentada: está na fala
  com a ênfase mais forte do módulo inteiro ("if you're below 50%, you're fucking
  something up", L178) e na tabela. Os 45% aparecem uma vez, sem fala. Mas há um detalhe
  que não é ruído: o glossário **qualifica** o alvo ("for engaged segments") e a tabela
  não qualifica nada. Se a pergunta for sobre segmento engajado, diga que existem dois
  números e que o mais exigente é o que ele defendeu. **Nunca responda "47,5%".** Se a
  pergunta for sobre warming ou alargamento de lista, a entrada que vale é
  `deliverability-limiar-de-open-rate`, não esta.
- **`fundamentos-unsubscribe-glossario`** — **0,3%**. É o valor mais repetido do módulo:
  ele o diz três vezes seguidas (L186, L188, L190) e no meio disso corrige o próprio
  slide ao vivo porque a tela mostrava o inverso do que ele queria dizer, sem detalhar o
  quê ("that should be the other way around (…) let me actually fix that right now",
  L188). O 0,2% do glossário não tem defesa falada. O diagnóstico associado vale para os
  dois: muitos unsubscribes = problema de conteúdo (L190). Há ainda uma terceira versão,
  0,4%, no outro deck — ver `entre-modulos-tabela-de-metricas`.
- **`fundamentos-spam-glossario`** — **o conflito mais grave da pasta em consequência
  prática.** 0,1% é **dez vezes** mais permissivo que 0,01%, e é a diferença entre uma
  conta saudável e uma conta em risco de bloqueio. **0,01%** é a posição sustentada —
  fala (L192), tabela (L379) e a tabela de deliverability (L8718) concordam. Dê o 0,1%
  do glossário apenas como registro divergente, **nunca como faixa** ("entre 0,01 e
  0,1%" seria a média inventada mais perigosa deste corpus). Diagnóstico associado: "you
  have a content problem, potentially a segmentation problem" (L192) — note a hesitação
  dele no segundo termo.
- **`fundamentos-click-rate-glossario`** — o conflito não é só de número, é de
  **estrutura**. Fala e tabela separam por tipo de envio e dão o motivo — "flows are
  higher converting, and they're more intent based" (L184). O glossário dá um número
  único, quatro a oito vezes maior que o alvo de campanha. Responda com a separação:
  0,5% em campanhas, 2% em flows, e cite que o glossário registra 2-4%+ achatado.
  Acrescente a tolerância declarada dele: 1% em campanha ele já considera doente ("I
  don't feel like that's healthy", L186), e ele mesmo diz que o número é frouxo ("it's
  really hard to say", L186). Há uma quinta e uma sexta versão fora do deck — ver
  `entre-modulos-tabela-de-metricas`.

Uma métrica **não** diverge e não deve ser apresentada como se divergisse: email share,
"40% (Goal)" na tabela (L374) e "Target is ~40%" no glossário (L388).

## O deck de deliverability dá três números de open rate em quatro linhas

`deliverability-limiar-de-open-rate` — **doze formulações**, sete na fala e cinco no
slide. É o número que decide qual lista usar e quando alargá-la.

| Valor | Contexto | Registro | Linha |
|---|---|---|---|
| "above 50%. 50% to 70% is ideal. If you're above 40%, you're probably okay" | meta geral | **outro-narrador** | L8436 |
| "consistently receiving 50 to 60% opens" | saber se a lista está certa | **outro-narrador** | L8468 |
| "ideally 50 plus open rates and then you know you're good to jump to a wider segment" | **a "golden rule"** do warming | **outro-narrador** | L8579 |
| "anywhere between 40 to 50 percent. If it starts dipping below 40, I definitely wouldn't be expanding it" | tolerância, **linha seguinte** | **outro-narrador** | L8580 |
| "you're hitting, again, 45 to 50% plus (…) that's a good indicator that we can expand" | expandir de 14 para 30 dias | **outro-narrador** | L8582 |
| "as long as you're hitting those, those 40 to 50% open rates" | cadência de rampa | **outro-narrador** | L8588 |
| "And that keeps us at a 40 to 50% mark" | após recuar de 30→60 para 30→45 | **outro-narrador** | L8604 |
| "This is how we can get consistent **50%** open rates" | o que enviar só para engajados entrega | **slide** | L8725 |
| "Whatever list gets you **50-60%** opens" | escolha da lista, **duas linhas depois** | **slide** | L8727 |
| "If you start to get **60%+** opens, widen your list to a larger timeframe" | **alargar**, **três linhas depois** | **slide** | L8728 |
| "If you start to get 40% opens, tighten your list to a smaller timeframe" | apertar | **slide** | L8729 |
| "\| Open Rates \| Greater than 50% \|" | tabela de metas do mesmo deck | **slide** | L8715 |

Duas adjacências agravam o conflito e são a prova de que ele não é artefato de recorte:

- **L8579 e L8580 são linhas consecutivas** e já discordam entre si: "50 plus" vira "40
  a 50" na frase imediatamente seguinte, dentro da mesma respiração.
- **L8725, L8727 e L8728 estão no mesmo slide**, a uma e duas linhas de distância: o
  slide promete "consistent 50%", manda escolher a lista por "50-60%" e depois exige
  "60%+" para alargar. **O registro que vence em especificação pelo protocolo tem três
  números em quatro linhas.**

**Como responder:** dê os valores todos, na ordem em que aparecem, e nomeie os dois
pontos em que **nenhuma das formulações contradiz as outras**: (a) **abaixo de 40%
nunca se alarga** (L8580; L8729 e L8470 mandam apertar em 40%); (b) o alvo de operação
é `Greater than 50%` (L8715). O slide é o mais exigente na hora de alargar — 60%+
(L8728) — **mas não é um bloco coerente**. Aqui não existe material sustentado contra
material entregue, como no caso do glossário: é a mesma tela. **Não há desempate.**

Se a pergunta for "posso alargar com 45%?", a resposta honesta é: pelo gatilho do slide
não (60%+), pela fala talvez (L8582 diz 45-50+), e o corpus nunca reconcilia. O critério
de segurança que a própria aula dá não é numérico — "I always err on the side of caution"
(L8569) e "it's much easier to build your sender reputation (…) than it is to fix it
when it's already in a poor position" (L8555). **Na dúvida, o número mais alto.**

**Atribuição, e ela pesa aqui:** as sete formulações faladas desta tabela (L8436 a
L8604) estão em L8381-8646, `outro-provavel` por [[mapa-da-autoria]] — **nenhuma é citável
como fala de Max**. O que sobra dele é o deck (L8715-8729), e é justamente o deck que
dá três números em quatro linhas. Não há lado de Max para preferir neste conflito.

