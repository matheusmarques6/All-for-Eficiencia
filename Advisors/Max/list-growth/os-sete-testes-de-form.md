---
tipo: especificacao
modulo: list-growth
assunto: ab-tests-de-form
autor: max-sturtevant
registro: [slide, transcricao]
fonte: "CONTEUDO BRUTO/max.md — L1258-1287 (slide), L663-671 (transcrição)"
conflitos: [list-growth-time-delay]
status: rascunho
---

# O que é

"Top 7 Best A/B Tests To Run On Your Forms" (L1258). Os sete são os mesmos nos
dois registros e aparecem na mesma ordem (slide L1260-1286; fala L663-671).

Cadência declarada só na fala: "You should be doing these depending on your site
traffic, but at least for like bi-weekly. Once every two weeks, run some sort of
test" (L663).

# Os sete, em ordem de alavanca

**1. Offer** — "Highest lever you can test. Try the different offers outlined
above and even try doing a 'Mystery Offer'" (L1262). Na fala é o mais forte que
ele diz do módulo inteiro: **"Changing your offer can literally be the difference
of like decreasing your CAC by 15%. It's huge"** (L665). Ver
[[a-oferta-e-o-componente-principal]].

**2. Form Type** — "Another large lever. Try the different form types above. You
can even test out using a pop-up vs full page vs flyout inside of Klaviyo"
(L1266, L665-667). Ver [[os-tipos-de-form]].

**3. Close Form Functionality** — "Try using a close form button vs an x in the
corner of your form. You can even test the placement of your close buttons or x"
(L1270). A fala é mais específica sobre direção: **"test an X from the top right
corner to the top left, usually top left performs better for whatever reason.
Everybody's used to seeing an X in the top right corner, so moving it to the
left, it makes people like rethink things"** (L667).

**4. Time Delay** — "Use different time delays to see what maximizes TOTAL
submits, not conversion rate. Try 4 second vs 12 second to start then start
closing the gap" (L1274). A fala confirma a métrica: "do four seconds versus
twelve seconds and look at the total submits" (L669). O critério de decisão é
explícito nos dois registros — **submissões totais, não taxa** —, mas o corpus
não diz por quê: ele dá a métrica sem dar o racional.

**5. Photo Content** — "Some photos may appeal more than others. You should even
test the placement of photos either next to the form or as a backdrop to the
form" (L1278, L669).

**6. Copy** — "Try longer forms vs shorter forms with copy varying from 'Unlock
my offer' to 'You've got xyz'" (L1282, L671). Ver [[copy-do-form]].

**7. Colors** — "Not a massive lever, but can make a difference. Typically the
less colors the better" (L1286). Na fala só "colors as well you can test your
colors" (L671).

# O racional dele

O teste não é opcional nem terminal. "It's only through testing, iterating,
improving, etc that you reach 10%+ opt in rates. Even your 10%+ forms should
continue to be tested to try to reach 20%+" (L1186-1187). Ver
[[por-que-o-popup-decide]].

Ordem prática sugerida na execução: o primeiro teste que ele monta é oferta
(10% off contra mystery discount, L1074-1076), e o segundo é tipo de form (quiz
contra ir direto ao email, L1077-1078).

# Onde o corpus discorda

O teste 4 herda o conflito de faixa do time delay: o par a testar é 4s vs 12s
(L1274, L669), mas em outro trecho a recomendação de operação é 4-8s com típico
de 6s (L1033) e em outro 4-6s (L194). Ver `list-growth-time-delay` e
[[checklist-do-form]].

# O que o corpus não diz

Não diz como priorizar entre os sete além da ordem em que estão listados —
oferta e tipo de form são explicitamente chamados de alavancas maiores (L1262,
L1266) e cor explicitamente de alavanca pequena (L1286); os quatro do meio ficam
sem ranking.

**Correção de escopo (varredura de falsos negativos).** Uma versão anterior desta
nota dizia "não há tamanho mínimo de amostra, duração mínima de teste, nem
limiar de significância. O único gate declarado é qualitativo: 'depending on your
site traffic' (L663)". **Duas coisas erradas nessa frase.**

1. **A citação de L663 estava cortada na metade.** A linha continua e dá um gate
   quantitativo: "You should be doing these depending on your site traffic, **but
   at least for like bi-weekly. Once every two weeks, run some sort of test**"
   (L663) — como o próprio corpo desta nota já registra em "O que é". Cadência
   mínima declarada: uma quinzena.
2. **A régua de amostra existe, em outro módulo.** L8800-8820 (otimização) define
   conclusividade por número de destinatários: lista de 1.000 partida 500/500 "is
   not enough data"; 100k-500k resolve em um ou dois envios; 5k-10k exige repetir
   três ou quatro vezes; e a regra explícita "Base it off the number of
   recipients that are receiving". Ver [[otimizacao/quando-vale-testar]]. Não é
   régua de form — é de campanha —, mas é o vizinho, e recusar sem oferecê-lo é
   erro.

O que **de fato** falta: nenhum nível de significância, nenhum p-valor, nenhuma
duração em dias, e nenhuma régua de amostra específica para **form** (a de
L8800-8820 conta destinatários de email, não visitantes de site).
