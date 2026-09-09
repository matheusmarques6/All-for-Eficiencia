---
tipo: indice
assunto: conflitos-entre-modulos-metas-e-open-rate
autor: max-sturtevant
status: aprovado
---

Os conflitos do corpus Max que atravessam pastas e envolvem metas de métrica e open rate: o benchmark de 30% citado no módulo de SMS contra os 50%+ exigidos no resto (`sms-open-rate-de-email`), as duas tabelas de metas de decks diferentes que não batem (`entre-modulos-tabela-de-metricas`) e a disputa sobre o que move o open rate — segmentação ou subject line (`fundamentos-o-que-move-o-open-rate`).

# Conflitos entre módulos — metas e open rate


Os que atravessam pastas. São os mais perigosos porque o roteamento do [[mapa-do-corpus-do-max]]
manda ler **uma** pasta: quem entra por `design/` nunca vê a versão de
`deliverability/`. Toda entrada aqui tem que ser lida antes de responder na pasta de
origem.

## sms-open-rate-de-email

O módulo de SMS benchmarka o open rate de email em 30%. Todo o resto do corpus exige
mais de 50%.

| Valor | Papel | Registro | Linha |
|---|---|---|---|
| "**SMS marketing messages have an average open rate of 98%** (email has an average open rate of **30%**)" | comparativo retórico | slide (SMS) | L9291 |
| "\| Open Rates \| **Greater than 50%** \|" | meta operacional | slide (deliverability) | L8715 |
| "Open Rates — 50%+" | tabela de metas | slide (fundamentos) | L376 |
| "we need to be above 50%. This is the only one where it's like, okay, if you're below 50%, you're fucking something up" | linha de corte | transcricao (fundamentos) | L178 |
| "you ideally want to be in that 50 to 60% range, but anything over 40% is okay" | tolerância | **outro-narrador** (campanhas) | L4236 |
| "Target: 45%+ for engaged segments" | glossário | slide (fundamentos) | L430 |

**Como responder:** são **coisas diferentes usadas como se fossem a mesma**. Os 30%
são média de mercado, citados uma única vez e com função retórica: fazer o 98% do SMS
parecer maior. Os 50%+ são a meta dele para as contas que gere, e ele a trata como
linha de corte, com a ênfase mais forte do módulo de fundamentos (L178). **Nunca cite
30% como benchmark de email do Max** — é o número contra o qual ele mede o mercado,
não a régua dele. Se a pergunta for sobre qual open rate perseguir, a entrada que vale
é `deliverability-limiar-de-open-rate`, e o piso de 40% aparece lá com contexto. Nota:
nenhuma das duas médias de mercado (30% de email, 98% de SMS) tem fonte citada no
corpus.

## entre-modulos-tabela-de-metricas

**Conflito novo, registrado nesta consolidação.** O corpus tem **duas tabelas de metas
de métricas**, em dois decks diferentes, e elas não batem. Nenhuma das duas unidades
de origem comparou uma com a outra.

| Métrica | fundamentos (L372-380) | deliverability (L8713-8719) | glossário (L428-438) |
|---|---|---|---|
| Open rate | "50%+" (L376) | "Greater than 50%" (L8715) | "Target: 45%+ for engaged segments" (L430) |
| Click rate | "0.5%+ on campaigns 2%+ on flows" (L377) | "Greater than 0.75%" (L8716) | "Target: 2–4%+" (L431) |
| Bounce rate | *ausente* | "Less than 1%" (L8717) | "Target: \<2%" (L437) |
| Spam complaint | "\<0.01%" (L379) | "Less than 0.01%" (L8718) | "Target: \<0.1%" (L438) |
| Unsubscribe | "\<0.3%" (L378) | "Less than 0.4%" (L8719) | "Target: \<0.2%" (L436) |

**Como responder:** as duas tabelas **concordam em dois pontos e divergem em três**.

- **Concordam:** open rate (>50%) e spam complaint (<0,01%). Esses dois números são os
  mais sólidos do corpus inteiro — dois decks e a fala (L178, L192).
- **Divergem em click rate:** fundamentos separa por tipo de envio (0,5% campanha, 2%
  flow) e dá o motivo — "flows are higher converting, and they're more intent based"
  (L184); deliverability dá um número único e achatado (0,75%), que não é nem um nem
  outro; o glossário dá 2-4%+ sem distinguir; e a fala de campanhas dá ainda "somewhere
  between one and 3%" (L4236 — **outro-narrador**, não citável como fala de Max).
  **Quatro versões.** Responda com a separação de
  fundamentos, porque é a única que traz racional, e nomeie as outras.
- **Divergem em unsubscribe:** 0,3% (fundamentos, L378, e a fala três vezes em
  L186-190) contra 0,4% (deliverability, L8719) contra 0,2% (glossário, L436). **Vale
  0,3%** — é o valor mais repetido do corpus e o único com fala sustentando. O 0,4%
  aparece uma vez, na tabela do deck de deliverability, e vem colado ao rótulo
  "(doesn't affect deliverability)" — ver `deliverability-unsubscribe-afeta-ou-nao`.
- **Bounce rate só existe fora da tabela de fundamentos**, e as duas fontes que o dão
  divergem por 2x: 1% (L8717) contra 2% (L437). Vale 1%, pela mesma regra que desqualifica
  o glossário (ver [[conflitos-no-mesmo-registro-metas-e-open-rate]]).

**Nunca componha uma tabela única a partir das três.** Se a pergunta for "quais são as
metas", a resposta diz qual tabela está sendo citada e por quê. A tabela de fundamentos
é a que ele defendeu linha por linha na fala (L168-194); a de deliverability é a que
vale dentro do contexto de entrega.

## fundamentos-o-que-move-o-open-rate

| Posição | Registro | Linha |
|---|---|---|
| "It's not your subject line or preview text. It is your segmentation (…) they're going to open your email, **no matter what your subject line says**" | transcricao (fundamentos) | L180 |
| "at most you can get ~ 10% jump in opens" | slide (copy) | L6805 |
| "The biggest open rate difference we've had on an A-B test is… 10%, maybe 15" | **outro-narrador** (copy) | L6227-6229 |
| "our best, our best subject line and preview text, you maybe see a five, 10% bump in open rates" | **outro-narrador** (otimização) | L8934-8936 |
| "people should open your emails based off your sender name, NOT your Subject line" | resumo do módulo (copy) | L6093 |

**Como responder:** não é contradição frontal — 10 a 15 pontos não tiram uma conta de
30% para 50%, então "o conserto é segmentação" continua de pé **como prioridade**. Mas
a negação de L180 é **absoluta** e o resto do corpus não é: em três lugares o corpus
quantifica o efeito de subject line sobre abertura — **e só um dos três é dele**: o
slide de copy (L6805). As outras duas quantificações (L6227-6229 e L8934-8936) são
fala **outro-narrador** e não são citáveis como fala de Max. Responda na ordem: primeiro
segmentação, que é o que ele manda consertar (L180, faixa Max); depois o teto de 5-15%
que copy adiciona, dizendo de quem é cada ponta.
**Nunca cite L180 sozinho para afirmar que subject line não importa** — ele dedica um
módulo inteiro a subject lines. Ver `copy-open-rate-limite` e
`otimizacao-sl-julgar-por-abertura-ou-receita`.

