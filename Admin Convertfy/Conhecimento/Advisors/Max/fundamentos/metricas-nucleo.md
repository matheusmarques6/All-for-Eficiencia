---
tipo: especificacao
modulo: fundamentos
assunto: metricas-nucleo
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L166-196 (transcrição); L368-380 (slide)"
conflitos: [fundamentos-open-rate-glossario, fundamentos-unsubscribe-glossario, fundamentos-spam-glossario, fundamentos-click-rate-glossario, fundamentos-limiar-de-escalar-aquisicao, fundamentos-piso-de-email-share, fundamentos-o-que-move-o-open-rate, list-growth-benchmark-de-form, list-growth-time-delay]
status: aprovado
---

# A tabela, verbatim do slide (L372-380)

| Metric | Target |
| :---- | :---- |
| **Email % of Total Store Revenue** | 40**%** (Goal)30–50% is healthy\>55% \= time to scale acquisition |
| **Campaigns vs Flows** | **Campaigns:** 40–60% of email revenue**Flows:** 40–60% of email revenue If you're too reliant on one, you're leaving easy revenue on the table from the other. |
| **Open Rates** | 50%+ |
| **Click Rates** | Varies on many things… campaign or flow type, list size, etc. In general: 0.5%+ on campaigns 2%+ on flows |
| **Unsubscribe Rates** | \<0.3% |
| **Spam Complaint Rates** | \<0.01% |
| **Pop-Up Form Submission Rate** | 6-12% |

A ressalva que abre a aula vale para a tabela inteira: "everything is contextual.
You can't just take all these" (L166). E a lista é deliberadamente curta:
"there are lots of different metrics that you can shoot for. These are really
all that matter in my eyes" (L176).

# O racional falado, métrica por métrica

**Email % da receita da loja.** Meta 40%, "that sweet spot" (L168-170). Faixa
saudável 30-50%: "you're not messing anything up too hard" (L170). Acima de 55%
o problema não é o email — é aquisição: "we need to scale our acquisition (…) if
we still have profitability problems then that's a separate issue. Like our email
channels are doing pretty solid" (L170-172). Abaixo de 30%, "we need to be doing
better with our email marketing" (L172).

**Campanhas vs flows.** 40-60% cada. O critério é simetria, não o número: "If you
go anything over and you're too reliant on one, you're probably leaving some
revenue on the table by the other one not being optimized" (L174). O split tem
três formulações no corpus — ver [[os-tres-e-meio-pilares]].

**Open rate.** A única métrica onde ele crava erro:

> Open rates are the most important because you can actually really control these
> and across every brand, we need to be above 50%. This is the only one where
> it's like, okay, if you're below 50%, you're fucking something up and you need
> to fix that. (L178)

E o conserto declarado **não é copy**:

> How do you fix your open rates? It's not your subject line or preview text. It
> is your segmentation. If you send to the right people, they're going to open
> your email, no matter what your subject line says. (L180)

O motivo do piso de 50% é deliverability, não vaidade. O mecanismo, na voz dele:
"If we send emails and Google takes a look at that, and we're getting less than
50% opens, then Google says, whoa, this brand sends an email, and less than half
people who receive it open it. Probably, people don't want to receive this
brand's emails, let's send them to spam" (L180-182).

**Click rate.** 0,5% em campanhas, 2% em flows. O motivo da diferença é intenção:
"flows are higher converting, and they're more intent based, and so we want those
to be higher" (L184). Ele admite que o número é frouxo: "There's, like, I review
accounts and they get 1% click rates and I'm like, okay, I don't feel like that's
healthy (…) it's really hard to say, but if you're anything, like, below these
numbers, then I would be concerned" (L186).

**Unsubscribe < 0,3%.** Diagnóstico de causa única: "if you have a lot of
unsubscribes, then you have a content problem and you need to fix your content"
(L190). Nesse ponto ele corrige o próprio slide ao vivo, porque a tela mostrava
o inverso do que ele queria dizer — ele não detalha o quê, e a frase do meio é
ininteligível no áudio: "that should be the other way around (…) Um let me
actually fix that right now" (L188). O slide publicado já sai corrigido
(`<0.3%`, L378), então não há como saber o que estava na tela antes.

**Spam complaint < 0,01%.** Duas causas, e a segunda é hesitante: "then you have
a content problem, potentially a segmentation problem" (L192).

**Pop-up form submission 6-12%.** Vem com uma condição embutida no benchmark —
"if we do a four to six second time delay trigger" — e com uma escada: "We want
a minimum 6%, ideally 10% plus. We've some brands where we're getting 20 to 30%
opt-in rates" (L194). Assunto do módulo de list growth; os dois números conflitam
com ele. Ver [[por-que-o-popup-decide]] e os slugs
`list-growth-benchmark-de-form` e `list-growth-time-delay`.

# O que ele se recusa a especificar

Revenue per recipient. Ele nomeia a métrica e não dá guideline:

> There's revenue per recipient, there's um all sorts of crazy shit, but
> everything's way too contextual. (L176)

O glossário define RPR (L434) sem alvo. Nenhum outro lugar do corpus fixa um
valor. Se perguntarem, a resposta é a recusa dele, não um número.

# Onde o corpus discorda

**Quatro conflitos entre esta tabela e o glossário do mesmo módulo.** Os dois são
slide, no mesmo deck: é conflito **dentro** do mesmo registro, e a precedência
do [[mapa-do-corpus-do-max]] ("slide vence em especificação") **não se aplica** — ela só vale
entre registros diferentes. O desempate aqui é por evidência de autoria dentro
do próprio material: em L217 ele declara que vai pular o glossário ("So I am
going to gloss over this glossary… You can use these if you want"), enquanto
defendeu esta tabela linha por linha na fala (L168-194). **A tabela é material
que ele sustentou; o glossário é material que ele entregou — onde os dois
divergem, vale a tabela.** Registrar os dois lados sempre, e nunca dar a
divergência como faixa: `<0.01%` é a posição sustentada, `<0.1%` é registro
divergente. Ver [[mapa-dos-conflitos]] § "Conflitos dentro do mesmo registro".

| Métrica | Tabela + fala | Glossário |
|---|---|---|
| Open rate | "50%+" (L376) · "above 50%" (L178) | "Target: 45%+ for engaged segments" (L430) |
| Unsubscribe | "\<0.3%" (L378, L186-190) | "Target: \<0.2%" (L436) |
| Spam complaint | "\<0.01%" (L379, L192) | "Target: \<0.1%" (L438) — **uma ordem de grandeza** |
| Click rate | "0.5%+ on campaigns 2%+ on flows" (L377, L184) | "Target: 2–4%+" (L431), sem separar |

**Mais dois, dentro da própria fala.** O limiar de "escalar aquisição" é ">55%"
na aula de métricas e no slide (L170, L374), mas "say you're at like 60 percent"
no walkthrough do dashboard (L56). E o piso sai como "less than like 30%" (L172)
contra "anywhere under 30%, um 40%" (L56-58).

**Um cross-módulo.** L180 nega que subject line mova open rate. Os módulos de
copy e otimização quantificam exatamente esse efeito: "at most you can get \~ 10%
jump in opens" (L6805, slide de Max) e "10%, maybe 15" (L6229 — **importado de
faixa não-Max**: está em L6101-6248, `outro-provavel` por [[mapa-da-autoria]], logo é o
módulo de subject lines que diz isso, não Max). Não é contradição frontal — um
salto de 10 pontos não tira ninguém de 30% para 50% — mas a negação de L180 é
absoluta e o resto do corpus não é. Ver `copy-open-rate-limite` e
`otimizacao-teto-de-abertura`.

# O que o corpus não diz

Nenhuma métrica aqui vem com janela de medição declarada — não se diz se open
rate é por envio, por 30 dias ou por conta. **Correção de escopo (varredura de
falsos negativos):** o corpus **tem** duas janelas declaradas, só que nenhuma
delas é a janela dos alvos desta tabela — e a diferença é a resposta, não a
recusa. São elas: a **janela de atribuição de receita**, 3 a 5 dias após o
clique ("they say somebody clicks an email and they purchase within three to
five days, they count it as email revenue", L54), e a **janela de leitura do
painel**, 30 dias contra os 30 anteriores ("the comparison period is just the
prior 30-day period", L64). As duas estão em [[dashboard-do-klaviyo]]. **Nunca
transpor a janela do painel para o alvo** — quem pergunta "open rate de 30%
medido em quanto tempo?" recebe as duas janelas que existem e a informação de
que a tabela de metas não declara a sua. Não há alvo de conversion rate,
CTOR, EPC nem bounce nesta tabela; bounce só aparece no glossário, "\<2%" (L437).
E não há critério de tamanho de lista: os mesmos números valem, no texto, "across
every brand" (L178).
