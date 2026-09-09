---
tipo: indice
assunto: autoria
autor: max-sturtevant
status: aprovado
---

A parte operacional do laudo de autoria: quais faixas da fonte não são fala de Max (L5617–5866, L4189–5154, L5867–6248, L8365–8646, L8762–9109 — 24,98% de toda a fala), quais notas de cada pasta derivam delas, qual número muda de dono (a frequência de campanhas), e os seis pontos que continuam indeterminados.

# 6. Consequência prática por pasta

Faixas não-Max, para a correção posterior:

- **`outro-provado`** — L5617–5866
- **`outro-provavel`** — L4189–5154, L5867–6248, L8365–8646, L8762–9109

Total: **2.228 linhas de fala** (recontadas com `wc` faixa a faixa:
250+966+382+282+348), 25.141 palavras — **24,98%** de toda a fala do
corpus (25.141 de 100.640 palavras faladas; o total de 121.344 do arquivo inclui
20.704 palavras de deck, que não são fala). A revisão da `persona.md` mediu esse
percentual; a versão anterior desta linha arredondava para 26%. As faixas de slide correspondentes (L5237–5599, L6501–6858, L8647–8759,
L9110–9212) **não** estão em causa: são artefato escrito de Max.

## 6.1 Notas afetadas, por pasta

**`deliverability/` — 9 de 9 notas. A pasta inteira.**
`auditoria-glockapps` (L8508) · `metricas-alvo` (L8430) · `o-que-e` (L8382) ·
`reparo-de-reputacao` (L8589) · `setup-tecnico` (L8396) ·
`so-envie-para-engajados` (L8456) · `upload-para-deliverability` (L8492) ·
`warming-casos-reais` (L8607) · `warming-do-dominio` (L8518, L8522).
Toda a fala do módulo (L8365–8646) é `outro-provavel`. O que sobra de Max é o
deck L8647–8759 — que é curto (113 linhas) e que também diz "our team" (L8692).

**`otimizacao/` — 7 de 7 notas. A pasta inteira.**
`categorias-vs-produtos` (L8890) · `flow-time-delays` (L8946) ·
`grafico-vs-texto` (L8862) · `outros-testes` (L8972) · `quando-vale-testar`
(L8774, L9096) · `send-time` (L8828) · `testar-subject-line-por-receita` (L8918).
Agravante já registrado em `_fontes`: o deck de Optimization (L9110–9212) é cópia
quase verbatim do deck de Flows. Ou seja, a pasta é fala não-Max mais um deck
duplicado.

**`campanhas/` — 8 de 9 notas.**
`cem-ideias-de-email` (L4516) · `frequencia-de-envio` (L4220, L4238, L4404,
L4191) · `mix-grafico-e-texto` (L4298) · `montar-o-calendario` (L4441, L4424) ·
`nao-hipersegmentar` (L4993, L5135) · `ocupar-espaco-mental` (L4244, L4194) ·
`os-cinco-pilares-de-conteudo` (L4372, L4426, L4472, L4538) · `segmentacao`
(L4844, L4829). Escapa apenas `email-de-texto-puro`, que vem de L5155–5235
(`max-provado`).

**`copy/` — 6 de 9 notas.**
`email-architect` (L5725, L5803) · `infograficos` (L5886, L5867) ·
`preview-texts` (L6171, L6090) · `principio-skimmable` (L5889) · `prompt-de-copy`
(L5627, L5667) · `subject-lines` (L6099, L6083). Escapam `o-que-evitar`,
`principio-clear-e-conciso` e `principio-engaging`, que saem do deck.
Caso particular: **`email-architect`** deriva de L5803, que é o narrador de
L5617–5866 lendo o slide L6790 — o conceito é de Max (está no deck), a
formulação falada não é dele.

**`doutrina/` — 8 de 13 notas.**
`a-ia-e-um-copywriter-junior` (L5667) · `desconto-constante-barateia-a-marca`
(L4372, L4191) · `disruptor-vence-no-inbox` (L6191, L6103) ·
`o-basico-entrega-90-por-cento` (L8778, L9098, L8764) ·
`o-numero-decide-nao-a-opiniao` (L6227, L8792) ·
`otimize-para-a-varredura-nao-para-a-leitura` (L4703) ·
`sce-o-framework-que-atravessa-tudo` (L4703, L4819) ·
`texto-puro-funciona-porque-e-raro` (L4326).
Esta é a pasta mais sensível: doutrina é exatamente o registro que o advisor
parafraseia na voz dele. `a-ia-e-um-copywriter-junior` sai de L5667 — o bloco
`outro-provado`.

**`flows/` — 1 de 12 notas.** Só `winback` (L5057, dentro de Segmentation).
O resto do módulo é `max-provavel` sem contraevidência.

**`design/`, `fundamentos/`, `list-growth/`, `sms/` — 0 notas afetadas.**
As quatro pastas estão inteiramente em faixa Max, e cada uma tem ao menos um
bloco `max-provado` como âncora (L7817/L8044 · L34 · L631/L1014 · L9258).

## 6.2 O número que muda de dono

Consequência concreta e imediata para `_numeros` e `_conflitos`: **a frequência
de campanhas**. As formulações faladas estão quase todas em faixa não-Max:

| Linha | Bloco | Classificação | Verbatim |
|---|---|---|---|
| L4220 | Campaign Strategy | `outro-provavel` | "two to four campaigns per week is generally going to be the sweet spot" |
| L4268 | Campaign Strategy | `outro-provavel` | "three to four emails a week" |
| L8557 | Warming Your Domain | `outro-provavel` | "ideally 3 to 4 times per week" |
| L8788 | High Leverage A/B Tests | `outro-provavel` | "three to four campaigns a week" |
| L2367 | Site Abandon Flow | `max-provavel` | "three to four campaigns per week from you" |
| **L5255** | **slide GAMMA CAMPAIGNS** | **Max (escrito)** | **"3x per week is typically the sweet spot"** |

A regra sobrevive — o slide de Max diz 3×/semana e L2367 corrobora —, mas o
"two to four … sweet spot" de L4220 deixa de ser citável como fala dele. Vale a
regra do `_protocolo`: quando os registros discordam sobre especificação, vale o
slide.

Não afetados, para tranquilidade: o piso de emails do welcome flow (L1440
"four to five", L1520 "three to four") está em `max-provavel`, e o alvo de 40%
de atribuição de receita (L170) também.

---

# 7. O que continua indeterminado

1. **Quem é o segundo narrador.** O laudo prova que L5617–5866 não é Max. Não
   prova quem é. O arquivo nunca o nomeia; ele nunca se apresenta; nenhum bloco
   diz "meu nome é X". Provavelmente alguém da Well Copy — L4224 mostra que tem
   acesso à conta Klaviyo da agência ("This is just a dummy account for WellCopy.
   Do some things in here for our team"), e L5801/L6019/L8798 falam de "our
   copywriters"/"our team" de dentro. Mas é inferência, não prova.

2. **Se o aglomerado B é uma pessoa ou mais de uma.** Os dez blocos são
   estilometricamente homogêneos e os quatro módulos são contíguos, mas nada
   exclui dois colaboradores com hábitos parecidos. Nenhum teste feito aqui
   separa B em sub-grupos.

3. **Os nove blocos `outro-provavel` não estão provados.** A base é
   estilométrica, não nominal. A probabilidade de acaso é baixíssima (§2.1), mas
   o padrão de prova deste laudo reserva `provado` para auto-identificação, e
   nenhum deles a tem — nem a favor, nem contra. Se aparecer, num desses nove,
   uma linha do tipo de L7817, o bloco sobe para `max-provado` e o aglomerado
   inteiro precisa ser reavaliado. Foi exatamente isso que aconteceu com
   DE-Figma.

4. **Os vinte blocos `max-provavel`.** Mesma ressalva na direção oposta. Onze
   deles não têm nenhum marcador em nenhuma direção porque são curtos demais
   (INTRO-A2, A5, A6, LG-A1, LG-A2, FL-Replenishment, FL-Winback,
   DE-Importance). Em bloco curto, ausência de marcador não é sinal.

5. **Se o narrador B escreveu algum slide.** Os decks trazem a bio de Max e
   reivindicações em 1ª pessoa dele, mas também "our copywriters" (L6790) e "our
   team" (L8692). Não há como distinguir "Max escreveu usando 'nós'" de "a
   equipe escreveu e Max assinou". Para efeito prático não muda nada — o deck é
   artefato oficial dele em qualquer dos dois casos —, mas convém não citar um
   slide como "ele disse".

6. **L5753 e o ASR.** Ver a ressalva em §4.1. É a única linha do arquivo que
   sustenta uma classificação `outro-provado`, e ela vem de transcrição
   automática. Se alguém recuperar o áudio original e a frase for outra, este
   laudo inteiro precisa ser refeito — porque sem L5753 não sobra prova nominal
   de segundo narrador, só estilometria.


---

O padrão de prova (§2) está em [[autoria-o-criterio-de-prova]]. A classificação
bloco a bloco (§3) está em [[autoria-tabela-mestra-de-quem-narra]]. As provas
(§4) e a refutação da hipótese da assinatura (§5) estão em
[[autoria-evidencias-e-o-que-caiu]]. Visão geral e regra de aplicação:
[[mapa-da-autoria]].
