---
tipo: indice
modulo: otimizacao
assunto: mapa-local
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L8760-9109 (transcrição), L9110-9211 (slide)"
status: rascunho
---

# O que tem nesta pasta

A mecânica de teste: quando ligar um A/B test, como saber que ele concluiu, e os
testes que ele diz rodar sempre. O princípio que sustenta o módulo — o básico
entrega a maior parte do resultado — não mora aqui: está em
[[doutrina/o-basico-entrega-90-por-cento]].

Os cinco testes de topo não são uma lista teórica: são, na descrição da aula,
"the tests that our team runs consistently that we always run with our new
accounts" (L8796-8798).

**Aviso de autoria.** A transcrição deste módulo (L8774-9108) abre com "Yo, yo,
what is going on?" (L8774) e fecha com "feel free to hit us up" (L9108) — o par
de assinaturas que `doutrina-narrador-da-aula-de-ia` atribui ao **segundo
narrador**, não a Max. Só L5667-5865 tem prova textual; aqui é inferência por
assinatura. As notas desta pasta ainda dizem "ele" e trazem
`autor: max-sturtevant`, como o resto do corpus. Ao responder a partir do
registro `transcricao` deste módulo, dizer "o material do curso diz", não "o Max
diz". O registro `slide` (L9110-9211) é neutro e não carrega o problema.

| Nota | Para quê |
|---|---|
| [[quando-vale-testar]] | pré-condição para testar e a regra de conclusividade por volume |
| [[send-time]] | horário de envio: horários a testar, perfil demográfico, caso real |
| [[grafico-vs-texto]] | gráfico vs text-based e onde cada um entra numa sale |
| [[categorias-vs-produtos]] | vitrine por categoria vs por produto; dado reaproveitável fora do email |
| [[testar-subject-line-por-receita]] | as 5 variáveis de SL/PT e a regra de julgar por receita |
| [[flow-time-delays]] | o delay do primeiro email de abandono; a maior alavanca declarada |
| [[outros-testes]] | os 13 testes restantes do slide, com o racional de cada um |

# Os testes, lado a lado

| Teste | O que compara | Alavanca declarada | Caso real citado |
|---|---|---|---|
| Flow time delays | 30 min vs 4 horas até o 1º email de abandono (L8952-8954) | "This is the biggest lever I'd say" (L9178) | site abandon: 4h vence, "10 to 15% higher placed order rate" e "about a thousand dollars in extra revenue"; click rate marginalmente melhor nos 30 min (L8958-8962) |
| Campaign send time | mesmo email em horários diferentes (L8828-8830) | "highest leverage test" é o primeiro da lista da aula (L8826) | 11am vs 1:45pm: "about five X, the amount of placed orders and three X, the number of recipients" (L8848-8852) |
| Graphic vs text based | layout gráfico vs texto puro (L8866-8870) | "can really vary across accounts" (L9153) | slide anuncia "Example of Text Based sale email winner" (L9157) — sem número, imagem ausente |
| Categorias vs produtos | vitrine por categoria vs produto individual (L8890-8892) | "gets you a lot of very interesting data", reaproveitável em paid ads e site (L8908-8912) | categorias vencem: revenue "10 to 15 times higher", "about six times the amount of recipients also buying" (L8914-8916) |
| SLs e PTs | 5 variáveis: desconto, emojis, "…", time delays, ALL CAPS (L9170-9174) | alto por email, mas "hard to take the learnings and apply to future emails" (L9167) | nenhum nesta faixa; teto de abertura "five, 10%" (L8936) |
| Os outros 13 | ver [[outros-testes]] | "Other High-Impact A/B Tests to Run" (L9182) | nenhum |

**Célula vazia é informação**: de todos os testes listados no módulo, só três
trazem caso real (send time, categorias, flow delay) e nenhum traz o print — as
telas lidas em voz alta estão ausentes do corpus.

# A ordem que ele declara

1. Ter o básico de pé antes de testar ([[quando-vale-testar]]; L8786-8790, L9122).
2. Começar pelo teste de maior alavanca (L8826, L9140-9141).
3. Julgar por placed order rate e receita, não por abertura (L8926-8934, L8942-8944).
4. Repetir até o resultado se repetir (L8820, L8854, L9139).

# Conflitos abertos neste módulo

`otimizacao-peso-do-basico` · `otimizacao-frequencia-precondicao` ·
`otimizacao-lista-pequena-quantas-repeticoes` · `otimizacao-onde-testar` ·
`otimizacao-horarios-a-testar` · `otimizacao-lista-redundante` ·
`otimizacao-grafico-numero-de-variantes` · `otimizacao-metricas-do-print` ·
`otimizacao-sl-julgar-por-abertura-ou-receita` · `otimizacao-teto-de-abertura` ·
`otimizacao-from-name-testar-ou-prescrever` · `otimizacao-deck-duplicado`

Todos detalhados em [[_conflitos]]; números em [[_numeros]].

# O que o módulo não cobre

Nada de estatística (significância, amostra mínima, duração). Nada sobre como
montar o teste dentro da ferramenta — o módulo cita "experiments, which is just
A/B tests" no Klaviyo uma vez, em outro ponto do corpus (L140), e nunca mostra a
tela. E ele encerra apontando para um documento externo com mais testes que não
está no corpus (L9094-9096).

**Exceção de tamanho**: [[outros-testes]] passa dos 4 KB por ser catálogo dos 13
itens com racional verbatim de cada um; foi mantida inteira de propósito.
