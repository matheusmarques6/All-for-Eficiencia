---
tipo: indice
modulo: deliverability
assunto: conflitos-deliverability
autor: max-sturtevant
conflitos: [deliverability-passo-de-escalonamento, deliverability-primeiro-degrau-da-rampa, deliverability-lista-base-padrao, deliverability-caso-mailchimp-escala-final, deliverability-salto-de-45]
status: aprovado
---

Registro dos conflitos do módulo `deliverability` do corpus de Max Sturtevant sobre o warming de domínio e a rampa de envio: passo de escalonamento, primeiro degrau da rampa, lista base padrão, o caso Mailchimp na escala final e o salto de 45. Cada entrada lista os valores divergentes por registro e fecha com um "Como responder".


Faixa: L8363-8646 (transcrição) e L8647-8759 (slide). **Atenção de atribuição:** os
dois blocos de fala (L8365-8517, L8518-8646) são classificados `outro-provavel` por
[[_autoria]]. `deliverability-limiar-de-open-rate`,
`deliverability-unsubscribe-afeta-ou-nao` e `deliverability-registros-dns` estão em
[[_conflitos#Conflitos dentro do mesmo registro]].


## deliverability-passo-de-escalonamento

Quanto se aumenta o volume a cada envio durante o warming.

| Valor | Contexto | Registro | Linha |
|---|---|---|---|
| "gradually increase from 25 to 50 percent percent based on performance" (*"percent percent" = gagueira de ASR*) | "the formula", 05:30 | **outro-narrador** | L8556 |
| "you scale up by about fifty to, by about fifty percent each send, as long as you're still getting the metrics that you want" | primeiro envio de 100-300, 08:08 | **outro-narrador** | L8569 |

**Como responder:** dê os dois, sem escolher. **Os dois são transcrição** — o deck de
warming nunca foi exportado, então nenhum dos dois tem o peso de slide e a regra de
precedência do protocolo não se aplica. Em L8554 o narrador diz "the formula, and it's
pretty self-explanatory", o que *sugere* que L8556 esteja sendo lido de um slide — mas o
corpus não diz isso e a hipótese não pode virar registro. **E os dois são
`outro-narrador`** (L8532-8646): este conflito não tem nenhum lado citável como fala de
Max, nem slide para arbitrar.

Não diga que "50% é o teto e 25% é o padrão": o corpus não hierarquiza. L8556 dá uma
faixa condicionada a desempenho ("based on performance"); L8569 dá um passo único
(~50%) igualmente condicionado ("as long as you're still getting the metrics that you
want"). A diferença operacional é real e composta: o passo é reaplicado a cada envio,
então 25% e 50% produzem rampas que divergem a cada degrau. O critério que a própria
aula oferece não é numérico: "I always err on the side of caution" (L8569) e "it's much
easier to build your sender reputation (…) than it is to fix it when it's already in a
poor position" (L8555).


## deliverability-primeiro-degrau-da-rampa

| Valor | Contexto | Registro | Linha |
|---|---|---|---|
| "on the first end, you're sending to one to 200,000" | cadência de rampa | **outro-narrador** | L8587 |
| "maybe a hundred people, two hundred people, three hundred people, somewhere in that range" | primeiro envio | **outro-narrador** | L8569 |
| degraus seguintes: 300 → 500 → 1.000 → 2.000 → 4.000 → 6.000 → 6.000 | mesma cadência | **outro-narrador** | L8588 |

**Como responder:** o "200,000" de L8587 é **erro de transcrição, não dado**. É
incoerente com o degrau imediatamente seguinte (300) e com o primeiro envio declarado
em L8569 (100-300 pessoas). O número real do degrau 1 não é recuperável. Responda com
**100-300 pessoas** (L8569) e declare que a linha da cadência está corrompida. Nunca
reproduza "200.000" como primeiro envio — é o erro que quebra a conta.


## deliverability-lista-base-padrao

| Valor | Registro | Linha |
|---|---|---|
| "90 Day Engaged List (You can use any time frame, 90 is recommended to start)" — "This is your base segment for sending all your email campaigns to" | slide | L8734 |
| "for a normal send or normal sends, you might only want to send to your 60 day engage list" | **outro-narrador** | L8462 |

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
| "a hundred thousand people" | tamanho da lista importada | **outro-narrador** | L8611 |
| "about 120,000 people per cent" (*"per cent" = ruído de ASR; o bruto não traz a palavra corrigida*) | volume ao fim da janela de 60 dias | **outro-narrador** | L8611 |
| "all the way up to about 100,000" | topo da escala final | **outro-narrador** | L8619 |
| "And then we go up to 4,000. 14,000." | degrau após 12.000 | **outro-narrador** | L8618 |
| "this got sent out to 40,000, 14,000 people and 7,000 people opened it" | leitura do Google | **outro-narrador** | L8621 |

**Como responder:** cite os números verbatim e diga que o caso é **narrado de
memória, com números que não fecham**. 120.000 por envio (L8611) é maior que a lista
importada de 100.000 (L8611) e que o topo declarado de 100.000 (L8619). O "4,000.
14,000" de L8618 é regressão impossível (o degrau anterior já era 12.000) — é gagueira
de ASR corrigindo-se para 14.000. Em L8621 o par "40,000, 14,000" é a mesma gagueira:
7.000 aberturas sobre 14.000 fecham os 50% que a demonstração está fazendo. **Use o caso
como ilustração de método, nunca como benchmark de volume.** O único número limpo e
verificável do caso é o open rate do primeiro envio: **46.22%** (L8614). **O caso
inteiro é `outro-narrador`** (L8532-8646): é um caso da agência narrada, não um relato
de Max, e não pode sair como experiência dele.


## deliverability-salto-de-45

**Lacuna, não conflito.** Em L8631, "we sent to all the active people, which was about
45" — a **unidade está ausente**. O contexto (degrau anterior de ~26.000, e o
resultado descrito como "a steep jump" que derrubou as aberturas) sugere 45.000, mas o
corpus não diz. **Não completar.** Responda: "about 45", unidade não informada.

---


