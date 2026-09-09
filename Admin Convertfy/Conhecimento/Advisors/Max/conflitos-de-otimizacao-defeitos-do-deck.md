---
tipo: indice
modulo: otimizacao
assunto: conflitos-otimizacao-defeitos-do-deck
autor: max-sturtevant
conflitos: [otimizacao-lista-redundante, otimizacao-grafico-numero-de-variantes, otimizacao-metricas-do-print, otimizacao-from-name-testar-ou-prescrever, otimizacao-deck-duplicado]
status: aprovado
---

Registro dos conflitos do módulo `otimizacao` do corpus de Max Sturtevant sobre defeitos e proveniência do deck de otimização: lista redundante de testes, número de variantes no teste de gráfico contra texto, métricas do print, from name testar ou prescrever e o deck duplicado do módulo de flows. Cada entrada lista os valores divergentes por registro e fecha com um "Como responder".


Faixa: L8760-9109 (transcrição) e L9110-9211 (slide GAMMA). O registro `resumo do
módulo` é o bloco de bullets da página do curso (L8760-8769) que antecede a
transcrição e termina no link para o deck (L8769) — **não é slide GAMMA**. Essa
distinção decide o primeiro conflito abaixo. `otimizacao-onde-testar` resolve para
`flows-onde-testar` ([[_conflitos#Conflitos entre módulos]]);
`otimizacao-sl-julgar-por-abertura-ou-receita` está em [[#Conflitos dentro do mesmo
registro]]; `otimizacao-teto-de-abertura` resolve para `copy-open-rate-limite`.


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
| a fala descreve a terceira via (template Klaviyo com nome de marca e footer, montado com blocos) | **outro-narrador** | L8982-8990 |

**Como responder:** é o mesmo teste com granularidade diferente. Para "o que testar",
a resposta completa tem três variantes; o branded plain text só é descrito na fala, e
o slide de topo o ignora.


## otimizacao-metricas-do-print

| Leitura | Registro | Linha |
|---|---|---|
| "three X, the number of recipients" (send time) | **outro-narrador** | L8850-8852 |
| "about six times the amount of recipients also buying" (categorias) | **outro-narrador** | L8916 |

**Como responder:** **lacuna.** Num A/B de split igual o número de destinatários não
muda; a leitura do caso de categorias ("recipients also buying") indica que a coluna
lida é de destinatários que **compraram**. O corpus não define a métrica e nenhum dos
prints está nele. Cite verbatim e diga que a métrica não é definida.


## otimizacao-from-name-testar-ou-prescrever

| Posição | Registro | Linha |
|---|---|---|
| "From Name and Sender Identity" listado como A/B test | slide | L9200-9201 |
| nenhuma menção na fala do módulo — a narração salta de curiosity/clarity para CTA text | **outro-narrador** | L9052-9054 |
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


