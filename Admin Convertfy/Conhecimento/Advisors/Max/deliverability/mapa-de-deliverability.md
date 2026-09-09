---
tipo: indice
modulo: deliverability
assunto: mapa-local
autor: max-sturtevant
registro: [slide, outro-narrador]
fonte: "CONTEUDO BRUTO/max.md — L8363-8646 (transcrição), L8647-8759 (slide)"
status: aprovado
---

# Aviso de autoria — a pasta inteira

**Toda a fala deste módulo (L8381-8646) é `outro-provavel`: não é Max.** As nove
notas derivam dela em maior ou menor grau; [[reparo-de-reputacao]],
[[warming-casos-reais]] e quase todo [[warming-do-dominio]] derivam **só** dela.
O que resta de Max é o deck L8647-8759 — 113 linhas, que cobrem o-que-e,
setup-tecnico, metricas-alvo, so-envie-para-engajados, upload e auditoria, e que
**não** cobrem warming nem reparo.

Sem prova nominal: a classificação é **estilométrica**, não provada — o bloco não
traz um só marcador do idioleto de Max ("I recommend", "my favorite", "I like to")
e traz os do outro aglomerado ("at the end of the day" 5×, fechos coletivos em
L8516 e L8645). `outro-provavel` **não é** `outro-provado`: não está provado que a
voz não é dele, só que é altamente improvável ([[_autoria]] §7.3).

Critério: idioleto ([[_autoria]] §2.1). **Saudação de abertura não é critério** —
o laudo testou e derrubou: o walkthrough de Figma abre com "Hello, hello" e é
comprovadamente Max, porque em L7817 ele digita `@max` e diz "tags me"
([[_autoria]] §5). Ao responder a partir do registro
`transcricao` deste módulo, dizer "o material do curso diz", nunca "o Max diz".

# A pasta de maior risco do corpus

Aqui não é opinião de copy. É procedimento operacional com números que, errados,
quebram a conta de email de uma marca. **Nenhum número desta pasta pode ser
arredondado, interpolado ou completado com boa prática de mercado.** Onde o
corpus dá dez valores para a mesma coisa — e dá —, a resposta dá os dez.

# As notas

| Nota | tipo | O que responde |
|---|---|---|
| [[o-que-e]] | principio · **outro-narrador** | onde o email cai e por quê; a analogia do credit score; só duas coisas afetam |
| [[setup-tecnico]] | procedimento · **datado** · **outro-narrador** | SPF/DMARC/DKIM no DNS, branded sending domain, verificação. **Bloqueio: sem isso, não envie nada** |
| [[metricas-alvo]] | especificacao · **outro-narrador** | a tabela de metas verbatim; soft vs hard bounce; o conflito do unsubscribe |
| [[so-envie-para-engajados]] | especificacao · **outro-narrador** | a definição verbatim do 90 Day Engaged List; quando apertar e quando alargar |
| **[[warming-do-dominio]]** | procedimento · **datado** · **outro-narrador** | **a nota operacional da pasta.** Quando se aplica, fundação, segmentos-semente, rampa, cronograma, batching, correção de rota |
| [[warming-casos-reais]] | procedimento · **só outro-narrador** | os dois casos narrados — volumes verbatim, com os números que não fecham marcados |
| [[reparo-de-reputacao]] | procedimento · **datado** · **só outro-narrador** | conta já caindo em spam: segmento curto, 2-3 semanas, alvo 60-80%, text-based |
| [[upload-para-deliverability]] | procedimento · **datado** · **outro-narrador** | os 5 passos de upload e por que alt text existe |
| [[auditoria-glockapps]] | procedimento · **datado** · **outro-narrador** | teste de placement, lista de 100+ endereços, ~1x/mês se houver problema |

# A ordem de execução

O corpus não a declara como lista, mas a dependência está explícita:

1. **[[setup-tecnico]]** — "If this isn't done, do this before sending ANY
   emails" (L8526). É pré-condição do warming (L8523).
2. **[[warming-do-dominio]]** — só depois do setup, e antes de qualquer campanha
   de volume. Dentro dele, a fundação (flows de alta intenção + pop-up
   convertendo) vem antes da primeira campanha (L8545-8551).
3. **[[so-envie-para-engajados]]** — o regime permanente que o warming existe
   para destravar: "so you have your 30, 60, 90 day engaged audiences
   established" (L8556).
4. **[[reparo-de-reputacao]]** — só quando já quebrou.

[[metricas-alvo]], [[upload-para-deliverability]] e [[auditoria-glockapps]] são
transversais: valem em qualquer etapa. [[warming-casos-reais]] é ilustração —
método, nunca benchmark de volume.

# Os três limiares que não devem ser confundidos

| Situação | Número | Linha |
|---|---|---|
| operação normal | `Open Rates — Greater than 50%` | L8715 |
| escolher ou alargar a lista | 40 / 40-50 / 45-50+ / 50 / 50+ / 50-60 / 50-70 / 60%+ — **dez formulações, ver conflito** | L8436, L8468, L8579, L8580, L8582, L8588, L8604, L8725, L8727, L8728 |
| reparo de conta em spam | 60-80% para começar a puxar | L8592 |

O único ponto em que nenhum registro discorda: **abaixo de 40% não se alarga a
lista** — "If it starts dipping below 40, I definitely wouldn't be expanding it"
(L8580), e em 40% o slide já manda apertar (L8729), assim como a fala (L8470).

# As duas lacunas declaradas

1. **O deck de warming nunca foi exportado.** O link existe (L8520) e o conteúdo
   não. Todo o conhecimento de rampa, cronograma e casos vive só na transcrição
   falada — é a única parte crítica do corpus **sem segundo registro** para
   conferir número. Declarado em [[warming-do-dominio]].
2. **A ferramenta de otimização de HTML nunca é nomeada.** Ele a recomenda para
   quem cai em promotions (L8641-8643) e a transcrição pula ~41 segundos
   exatamente onde o nome estaria. Irrecuperável. Nunca deduzir.

# O que esta pasta não cobre

- Como escrever o email. Isso é `copy/` e `design/`.
- Sunset flow ou limpeza de lista — **esta pasta** não trata. Os dois existem
  fora dela e são o vizinho: [[flows/sunset]] (finalidade em L411, segmento no
  print da L9545) e a **Suppress List** completa do deck de campanhas, ≥5 emails
  recebidos AND 0 aberturas em 365 dias OR ≥3 bounces OR ≥1 spam (L5592) — ver
  [[campanhas/segmentacao]]. O glossário ainda dá um alvo de `List Cleaning`,
  "60–90+ days" (L443), que **só existe ali** ([[fundamentos/glossario]]).
- SMS deliverability. Nada nesta faixa.
- O que fazer quando click rate, bounce rate ou spam complaint furam o alvo. Há
  meta, não há protocolo de reação — só para o caso de spam
  ([[reparo-de-reputacao]]).
