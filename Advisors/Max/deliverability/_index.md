---
tipo: indice
modulo: deliverability
assunto: mapa-local
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L8363-8646 (transcrição), L8647-8759 (slide)"
status: rascunho
---

# A pasta de maior risco do corpus

Aqui não é opinião de copy. É procedimento operacional com números que, errados,
quebram a conta de email de uma marca. **Nenhum número desta pasta pode ser
arredondado, interpolado ou completado com boa prática de mercado.** Onde o
corpus dá dez valores para a mesma coisa — e dá —, a resposta dá os dez.

# As notas

| Nota | tipo | O que responde |
|---|---|---|
| [[o-que-e]] | principio | onde o email cai e por quê; a analogia do credit score; só duas coisas afetam |
| [[setup-tecnico]] | procedimento · **datado** | SPF/DMARC/DKIM no DNS, branded sending domain, verificação. **Bloqueio: sem isso, não envie nada** |
| [[metricas-alvo]] | especificacao | a tabela de metas verbatim; soft vs hard bounce; o conflito do unsubscribe |
| [[so-envie-para-engajados]] | especificacao | a definição verbatim do 90 Day Engaged List; quando apertar e quando alargar |
| **[[warming-do-dominio]]** | procedimento · **datado** | **a nota operacional da pasta.** Quando se aplica, fundação, segmentos-semente, rampa, cronograma, batching, correção de rota |
| [[warming-casos-reais]] | procedimento | os dois casos que ele narra — volumes verbatim, com os números que não fecham marcados |
| [[reparo-de-reputacao]] | procedimento · **datado** | conta já caindo em spam: segmento curto, 2-3 semanas, alvo 60-80%, text-based |
| [[upload-para-deliverability]] | procedimento · **datado** | os 5 passos de upload e por que alt text existe |
| [[auditoria-glockapps]] | procedimento · **datado** | teste de placement, lista de 100+ endereços, ~1x/mês se houver problema |

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
- Sunset flow ou limpeza de lista — o corpus não trata aqui.
- SMS deliverability. Nada nesta faixa.
- O que fazer quando click rate, bounce rate ou spam complaint furam o alvo. Há
  meta, não há protocolo de reação — só para o caso de spam
  ([[reparo-de-reputacao]]).
