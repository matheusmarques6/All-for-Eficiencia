---
tipo: indice
assunto: conflitos-entre-modulos-onde-testar-frequencia-e-pontas-soltas
autor: max-sturtevant
status: aprovado
---

Os conflitos do corpus Max que atravessam pastas e envolvem onde testar e com que frequência enviar: campanha como campo de teste contra o teste de delay dentro do flow (`flows-onde-testar`), a frequência de email citada dentro do módulo de SMS (`sms-frequencia-de-email-comparada`) e a tabela de pontas soltas que exigem leitura cruzada — cadência, benchmark de pop-up, exit intent, stack de ferramentas, winback e credencial de receita — com o slug canônico de cada uma.

# Conflitos entre módulos — onde testar, frequência e pontas soltas


Os que atravessam pastas. São os mais perigosos porque o roteamento do [[mapa-do-corpus-do-max]]
manda ler **uma** pasta: quem entra por `design/` nunca vê a versão de
`deliverability/`. Toda entrada aqui tem que ser lida antes de responder na pasta de
origem.

## flows-onde-testar

Absorve `otimizacao-onde-testar`. As duas posições estão na **mesma página do mesmo
deck**, a poucas linhas de distância (L4128 e L4139) — e a segunda tem cópia idêntica
no deck de otimização.

| Posição | Verbatim | Registro | Linha |
|---|---|---|---|
| tirar o teste do flow | "Rather than have a ton of active tests in flows of all sorts of different triggers, trying out different **content**, etc / We mostly use campaigns as our testing ground. / Try new angles and A/B test frequently in your email blasts. / Rather than waiting for results like you have to do in flows, you can get near instant data with campaigns." | slide (deck de flows) | L4128-4131 |
| o motivo | "Considering you can have 30-50+ automated emails… It's overwhelming / Hard to monitor at scale / Difficult to track and report at scale / Documenting is difficult" | slide (deck de flows) | L4119-4124 |
| o que fazer com o vencedor | "We literally put full campaigns that perform well into our flows. / Go back and edit your flow emails across all triggers to include the angle you saw work." | slide (deck de flows) | L4132-4133 |
| testar dentro do flow | heading "**Flow Specific A/B Tests**" | slide (deck de flows) | L4139 |
| testar dentro do flow | "**Flow Time Delays** — This is the biggest lever I'd say. Testing the amount of time from the action of the customer and the first email they receive. Then also, the time delay between your flow messages." | slide (deck de flows) | L4141-4145 |
| testar dentro do flow | mesma frase, palavra por palavra | slide (deck de otimização) | L9176-9180 |

**Como responder:** não é contradição de valor, é **divisão de escopo — e o deck a
sinaliza duas vezes, ainda que nunca a formule numa frase só.** As duas âncoras que as
notas de origem tinham subestimado:

1. **L4128 nomeia o que sai do flow: "trying out different *content*".** A frase não
   diz "tirem os testes dos flows"; diz que não se deve manter muito teste de
   **conteúdo** ativo dentro deles, e o motivo dado logo acima é de escala e
   monitoramento (L4119-4124), não de mérito.
2. **L4139 é um heading que diz "Flow Specific A/B Tests"**, e é sob ele que o teste de
   delay aparece (L4141-4145). O deck classifica explicitamente esse teste como
   específico de flow.

Ou seja: **conteúdo se testa em campanha e migra pronto para o flow** (é literalmente o
que L4132-4133 mandam fazer); **timing só pode ser testado no flow**, porque não existe
delay em campanha. Ofereça essa leitura como leitura — o corpus **não a enuncia em uma
frase** —, mas **não diga que "o corpus nunca faz essa distinção"**: ele a faz duas
vezes, na palavra "content" (L4128) e no heading "Flow Specific" (L4139). O que falta é
a frase que amarra, não a evidência.

Registre também que "the biggest lever" (L4143) tem cópia idêntica no deck de
otimização (L9178), o que **não** o torna duas fontes: é o mesmo slide reaproveitado.
Ver `otimizacao-deck-duplicado`.

## sms-frequencia-de-email-comparada

| Valor | Registro | Linha |
|---|---|---|
| Email: "four to five messages a week" sem backlash | transcricao (SMS) | L9226 |
| Email: "With email you can easily send 4-5 email campaigns per week without getting much backlash" | slide (SMS) | L9364 |
| Email: "like four times a week" | transcricao (SMS) | L9248 |
| Email: "we see the best results and engagement sending 4x per week (every other day)" | slide (SMS) | L9490 |
| Email: tabela por faturamento, 2x a 5-6x/semana | slide (campanhas) | L5295-5298 |
| Email: "two to four times per week is really hitting the sweet spot" | **outro-narrador** (campanhas) | L4242 |

**Como responder:** os números de email citados **dentro do módulo de SMS** são
comparativos de argumento, não a especificação de email — existem para dizer que SMS é
menos. A especificação está no módulo de campanhas, que decide por tier de faturamento
ou tráfego (L5295-5298) e cujo sweet spot declarado é 2-4x (L4242 — **outro-narrador**,
não citável como fala de Max) ou 3x (L5255, slide de Max). Ver [[mapa-da-autoria]] §6.2: o
"two to four … sweet spot" falado muda de dono; a regra sobrevive pelo slide.
**Nunca responda "4-5 por semana" citando L9226/L9364.** Note que 4-5x e "4x every
other day" também estouram a faixa 2-4 do módulo dono — é o mesmo tipo de atrito
registrado em `campanhas-cadencia-alta-vs-tier-1m`, e o corpus não o comenta.
## Os que atravessam pastas e estão registrados no módulo dono

Pontas soltas que exigem leitura cruzada, mas cuja entrada canônica vive na pasta que
possui o assunto:

| Assunto | Módulos que discordam | Slug canônico |
|---|---|---|
| Cadência de campanha | campanhas (2-4x, 3x) · otimização (3-4x como pré-condição) · deliverability (3-4x, L8557) · SMS (4-5x, 4x — comparativos) · flows (3-4x, 3x) | `campanhas-sweet-spot-de-frequencia` + `otimizacao-frequencia-precondicao` + `sms-frequencia-de-email-comparada` |
| Benchmark do pop-up | fundamentos (6-12%) · list-growth (a escada) · SMS (2-3% / 8-10%) | `list-growth-benchmark-de-form` (+ `fundamentos-benchmark-do-form` para o denominador) |
| Delay do pop-up | fundamentos (4-6s) · list-growth (4-12s, 4-8s, 5s) · SMS (6-10s) | `list-growth-time-delay` |
| Exit intent | list-growth (rejeição geral, rejeição no mobile) · SMS (rejeição sem qualificar) | `list-growth-exit-intent` |
| Subject line move ou não o open rate | fundamentos (L180: não move) · copy (5-15%) · otimização (5-10%) | `fundamentos-o-que-move-o-open-rate` + `copy-open-rate-limite` |
| Stack de ferramentas | fundamentos (Klaviyo é o melhor) · list-growth (Klaviyo não performa em form; Alia é superior) · design (título Klaviyo, demo Omnisend) | `fundamentos-klaviyo-melhor-ou-pior` + `list-growth-alia-vs-klaviyo` + `design-klaviyo-vs-omnisend` |
| Denominador da receita de flows | fundamentos (loja vs email, mesma linha) · flows (20% loja vs 50% email) | `fundamentos-denominador-dos-80` + `flows-participacao-na-receita` |
| Definição do winback | flows (sem o teto de 150 dias) · campanhas (150/90 completo) | `winback-definicao-do-segmento` + `campanhas-winback-janela` |
| Janela da lista base | campanhas (90) · deliverability (90 no slide, 60 na fala) | `campanhas-janela-de-engajamento` + `deliverability-lista-base-padrao` |
| Checkbox pré-marcado do Shopify | list-growth (texto que se anula) · SMS (procedimento de email sob título de SMS) | `list-growth-checkbox-preselecionado` + `sms-instrucoes-de-optin-sao-de-email` |
| Grafia de nomes de marca | doutrina · design · copy | `doutrina-lista-de-marcas` |
| Credencial de receita | doutrina ($40M, $100M) · flows ($100M, $200M) · campanhas ($200M) | `doutrina-receita-da-agencia` |

