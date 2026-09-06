---
tipo: artefato
modulo: fundamentos
assunto: glossario
autor: max-sturtevant
registro: [slide]
fonte: "CONTEUDO BRUTO/max.md — L384-519 (slide); L217-229 (transcrição)"
conflitos: [fundamentos-open-rate-glossario, fundamentos-unsubscribe-glossario, fundamentos-spam-glossario, fundamentos-click-rate-glossario, fundamentos-roi-do-email]
status: rascunho
---

# O que é

O glossário do deck GAMMA, aula 6. Medido no bruto: **99 termos em 12
categorias**, L384-519. É o único artefato de referência puramente terminológico
do corpus inteiro.

Está quebrado em quatro notas porque o bloco inteiro tem 9,2 KB. As categorias
ficaram na ordem original e nenhuma foi partida ao meio.

| Parte | Categorias | Termos | Linhas |
|---|---|---|---|
| [[glossario-receita-e-flows]] | 💰 Revenue Attribution & Metrics · 📬 Email Types · 🔄 Core Automated Flows | 6 + 4 + 8 = 18 | L386-411 |
| [[glossario-segmentos-e-metricas]] | 🎯 Segmentation & Targeting · 📈 Performance Metrics | 12 + 10 = 22 | L413-439 |
| [[glossario-deliverability-e-plataforma]] | 🧼 List Health & Deliverability · 🛠 Platform & Design Terms | 12 + 13 = 25 | L441-470 |
| [[glossario-copy-e-estrategia]] | 🧠 Copywriting & Content · 🧪 Testing & Optimization · 📊 Analytics & Attribution · 🔐 Compliance & Consent · 💡 Strategy & Frameworks | 8 + 4 + 6 + 7 + 9 = 34 | L472-519 |

# A ressalva mais importante: ele não leu isto

A transcrição correspondente (L217-229) é quase toda meta-comentário: ele declara
que vai pular a leitura e lista os títulos das categorias em voz alta. **Só dois
dos 99 termos ganham definição falada**, e os dois na mesma linha (L225): warmup
— "so process of gradually rebuilding your center reputation" — e DKIM/SPF/DMARC
— "which are just like authentication protocols". Nenhuma métrica, nenhum alvo
numérico e nenhum flow é definido em voz alta.

> So I am going to gloss over this glossary, I'm going to be gloss over-ing this
> email marketing glossary in key terms. You can use these if you want (L217)

E depois rebaixa parte do conteúdo:

> compliance and consent. which you really don't, don't need to know these, but
> if you ever mention it, you can check back to this (L229)

O único uso que ele prescreve é consulta pontual: "if you ever don't know
anything that I mentioned, you can refer to this" (L219-221). Ele também antecipa
que boa parte é óbvia — "some of these are going to be pretty straightforward"
(L221) — e admite que uma categoria é a parte difícil: "with health and
deliverability. This is where things get a little bit comm- complicated" (L225).

**Consequência prática:** o glossário é `registro: slide` puro. Fora das duas
exceções de L225, nenhuma definição aqui tem fala do Max por trás — e **nenhum
alvo numérico do glossário é falado em lugar nenhum do corpus**. Onde uma
definição do glossário discordar de algo que ele **falou**, a fala vence, porque
ele nunca defendeu estas linhas.

# Onde o glossário contradiz o próprio módulo

Quatro metas numéricas do 📈 Performance Metrics discordam da tabela de metas do
mesmo deck e da fala da aula 5. Tabela completa em [[metricas-nucleo]]; entradas
em `_staging/conflitos-fundamentos.md`.

| Métrica | Glossário | Tabela / fala |
|---|---|---|
| Open Rate | "Target: 45%+ for engaged segments" (L430) | "50%+" (L376) · "we need to be above 50%" (L178) |
| Unsubscribe Rate | "Target: \<0.2%" (L436) | "\<0.3%" (L378, L186-190) |
| Spam Complaint Rate | "Target: \<0.1%" (L438) | "\<0.01%" (L379, L192) — uma ordem de grandeza |
| Click Rate | "Target: 2–4%+" (L431), sem distinguir | "0.5%+ on campaigns 2%+ on flows" (L377, L184) |

Mais um, fora das métricas: o ROI do email aparece como **"$36+ return for every
$1 spent"** na fala e no slide de abertura (L13, L285) e como **"\~40x ROI"** no
glossário (L393).

# O que o corpus não diz

O glossário traz três alvos que **não existem em nenhum outro lugar do corpus** e
que, portanto, não têm fala nem tabela para confirmar: `Bounce Rate` "\<2%"
(L437), `List Cleaning` "60–90+ days" (L443) e `Email Width` "600–700px" (L469).
Citáveis, sempre marcando que a origem é exclusivamente o glossário.

Também não há definição de `Sunset Flow` além da linha do glossário (L411) — o
resto do corpus tem só o título.
