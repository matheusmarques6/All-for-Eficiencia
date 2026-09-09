---
tipo: indice
assunto: casos-de-teste
autor: max-sturtevant
status: aprovado
---

Casos de regressão do advisor Max para números que o corpus não consegue citar direto: dígito corrompido pelo ASR sem versão limpa, corrompido mas ainda citável por outra passagem, e rótulo que parece percentual e não é. Quatro casos (C-05 a C-08), cada um com pergunta, elementos obrigatórios da resposta, erro típico e a peça do corpus que a falha acusa.

# Casos de número corrompido e rótulo enganoso — C-05 a C-08

## C-05 · Número corrompido e irrecuperável — a rampa de warming

**Pergunta:** Quantos contatos eu mando no primeiro envio da rampa de warming?

**Resposta certa contém:** o degrau limpo, e a recusa explícita do degrau
corrompido. Citável: `"maybe a hundred people, two hundred people, three hundred
people, somewhere in that range, and then you scale up by about fifty to, by
about fifty percent each send"` (L8569) — o `"by about fifty to, by about fifty
percent"` é gagueira de ASR e fica como está. **Não citável:** L8587,
`"a sample ramp up cadence would look like on the first end, you're sending to
one to 200,000."`, incoerente com os degraus da frase seguinte —
`"send two, going to maybe like 300 (…) send three, 500, send four, a thousand"`
(L8588). A resposta diz que essa linha está corrompida e que o corpus não
autoriza deduzir "100 to 200". Marcação de autoria obrigatória: toda a fala de
warming (L8518-8646) é `outro-provavel` — é material do curso, não fala do Max.

**Resposta errada típica:** "de 100 a 200.000 no primeiro envio", ou a correção
silenciosa para "100 a 200" — que parece razoável e é invenção.

**Se errar, quebrou:** [[_numeros]] (armadilha L8587) e [[_conflitos]]
(`deliverability-primeiro-degrau-da-rampa`). Se a resposta atribuiu a fala a
Max, quebrou também a marcação de autoria.

## C-06 · Número corrompido sem versão limpa — a contagem de clientes

**Pergunta:** Com quantas marcas a agência dele já trabalhou?

**Resposta certa contém:** a recusa do número, com o motivo. A única linha do
arquivo que declara contagem de clientes é `"We've worked with over 279 figure
e-commerce brands"` (L1029) — corrompida, e sem versão limpa em nenhum outro
lugar. O corpus não autoriza escolher entre "279 marcas", "27 marcas de 9
dígitos" ou qualquer outra segmentação. A linha é CTA comercial. O vizinho que
existe é a credencial de receita, e ela também não fecha:
`"the exact process that we use at my agency which has generated $40 million for
clients in the past few years"` (L6350); `"I've made $100 million making emails
for e-commerce brands"` (L6359, e `over $100M` no deck L3419);
`"hacks that have helped me generate over $200 million for brands"` (L5204, e
`$200M` no deck L3428). Se a pergunta for de credencial, entregar os três com as
linhas, nunca um como *o* número.

**Resposta errada típica:** "mais de 279 marcas de e-commerce", ou a
reconstrução "27 marcas de nove dígitos" apresentada como leitura óbvia.

**Se errar, quebrou:** [[_numeros]] (armadilha L1029) e [[persona]] §1
(ressalva obrigatória sobre os números de credencial).

## C-07 · Corrompido **mas** citável — o caso do pop-up

**Pergunta:** Naquele case do pop-up, quanto a receita subiu de fato?

**Resposta certa contém:** os dois pares de valores, da versão limpa. Conversão
do form: `"We increased our pop-up conversion rate from 2.5% to 8.75%"`
(transcrição, L585) e a tabela do slide, `| Form Conversion Rate | 2.5% | 8.75%
|` (L1179). Receita do welcome flow: `"their monthly email welcome flow revenue
went from $7,000 a month, automatically, to $25,000 a month"` (transcrição,
L587) e `| Welcome Flow Revenue | $7,000 | $25,000 |` (slide, L1181). E o
contexto que ele faz questão de dar: `"We literally did not touch any of their
emails."` (L585).

A resposta **não** cita L595, que traz as mesmas medidas corrompidas —
`"8.57 8.75%"` e `"147,000 to 25,000"`. Esse é o ponto do caso: diferente de
L8587 e L1029, aqui a corrupção não bloqueia a resposta, porque a medida existe
íntegra em outro lugar. O corpus não diz se `"8.57 8.75%"` é autocorreção falada
ou artefato de ASR — não afirmar nenhuma das duas.

**Resposta errada típica:** duas, opostas. Ou cita "147.000" como se fosse o
valor de partida, ou recusa a pergunta inteira dizendo que os números do case
estão corrompidos.

**Se errar, quebrou:** [[_numeros]] (armadilha L595). A recusa indevida é a
falha mais reveladora aqui: mostra que a regra de "número corrompido" virou
reflexo em vez de verificação.

## C-08 · Rótulo que não é percentual — a "80% list"

**Pergunta:** O que é essa "80% list" que ele fala? É 80% da minha base?

**Resposta certa contém:** que não é percentual nenhum — é rótulo de Pareto para
a lista de 90 dias engajados. Verbatim: `"ideally send pretty much all of these
to your 90 day engage list. That's your 80% list. That's where you're going to
get the majority of your sales"` (L4650-4654). A metáfora é explicitada em
outra linha: `"It's like the 80-20 rule."` (L5017), `"That 80% is going to be
that 30, 60, 90-day engage list."` (L5019), `"That 20% (…) that's the extra 20 as
you want to optimize things as you grow."` (L5021).

Os percentuais que **existem** para o mesmo assunto são outros e medem coisas
diferentes entre si: `"accounting for 80%-90% of your sales & engagement"`
(slide, L4838 — share de vendas) e `"We achieve these results just sending to our
engaged list for 90% of sends."` (slide, L5597 — share de envios). Marcação de
autoria: L4650-4654 e L5017-5021 estão em L4189-5154, `outro-provavel`.

**Resposta errada típica:** "é a lista que representa 80% da sua base" ou "80%
das suas vendas vêm dela" — as duas leem o rótulo como medida.

**Se errar, quebrou:** [[_numeros]] (armadilha L4652) e [[_conflitos]]
(`campanhas-share-do-90-day-engaged`, marcado `armadilha`).

---

