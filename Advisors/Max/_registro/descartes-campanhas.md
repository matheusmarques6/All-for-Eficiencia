---
tipo: staging
modulo: campanhas
fonte: "CONTEUDO BRUTO/max.md — L4187-5236 (transcrição), L5237-5599 (slide GAMMA)"
status: rascunho
---

# Descartes do módulo campanhas

O que não entrou nas notas, e por quê. Nada aqui foi reconstruído.

---

## 1. Loop de ASR — L4480-4488 (a lacuna real do módulo)

**A faixa.** Cinco parágrafos consecutivos (L4480, L4482, L4484, L4486, L4488;
com as linhas em branco intercaladas, L4480-4488) em que a frase
`If you're going to include those testimonials` se repete até o fim de cada
linha. Contagem de repetições por linha:

| Linha | Repetições | Abre com |
|---|---|---|
| L4480 | 7 | "If you're going to…" |
| L4482 | 10 | "If you're going to…" |
| L4484 | 11 | "If you're going to…" |
| L4486 | 10 | "If you're going to…" |
| L4488 | 12 | "So if you're going to…" |

**O contexto intacto de cada lado.** L4476-4478 fecha normalmente a abertura do
pilar Social Proof: *"Social proof, one of the biggest movers, high leverage,
talking through customer testimonials, anything that brings legitimacy to your
brand or your feature on the news, in a newspaper, in a magazine, whatever it
may be. Any of those publications that are featuring you want to include
those."* L4490 retoma já noutro assunto, a distribuição percentual mensal:
*"So if you send 10 emails a month, maybe you have 20% educational…"*

**O que exatamente se perdeu.** Apenas o **racional falado sobre como usar
testimonials** dentro do pilar Social Proof — provavelmente uma ou duas frases,
dado que a transcrição retoma no assunto seguinte. Não se perdeu:

- os cinco pilares, que estão íntegros nos bullets do módulo (L4426-4430) e no
  slide (L5338-5342), cada um com um exemplo;
- a definição de Social Proof, presente em L4476-4478 e em L5339;
- as 20 ideias de Social Proof da lista de 100 (L5381-5402), que cobrem
  testimonials, review, UGC e press em detalhe.

**Decisão:** registrado como lacuna delimitada em
`campanhas/os-cinco-pilares-de-conteudo.md` e em `campanhas/_index.md`. Não
reconstruído, não parafraseado, não preenchido por analogia com o slide.

**Nota de procedência.** O brief de construção localizava este loop em
L4293-4301. Está errado: L4293-4301 é conteúdo íntegro (fim do racional de
"revolving door" de subscribers e início da seção graphic vs text-based, que
alimenta `mix-grafico-e-texto.md`). Verificado com
`grep -n "include those testimonials"` e `sed -n '4290,4302p'`. A correção foi
confirmada pelo coordenador durante a execução.

---

## 2. Boilerplate de deck repetido

| Linhas | O que é |
|---|---|
| L4199, L4439, L4682, L4842 | "Link to document in video: https://gamma.app/docs/Email-Marketing-Campaigns-uefllw8w707qptn" — quatro vezes, mesmo link |
| L4201, L4441, L4684, L4844 | "Transcrição do Vídeo :" + "\# File-…" — marcador de seção |
| L5239, L5241, L5598 | "Email Marketing Campaigns" — título e rodapé do deck, repetidos |
| L5323 | "# " — heading vazio |

---

## 3. Placeholders sem imagem

| Linhas | O que é |
|---|---|
| L5309-5311 | "**Graphic Based Email**" / "**Text-Based Email**" — legendas de imagens que não existem no bruto |
| L5480-5486 | "**Step 1**" / "**Step 2**" / "**Step 3**" / "**Results**" — a demonstração visual do GPT; o processo falado está em L4550-4568 e foi preservado |
| L5488-5491 | "Example Calendar" — o calendário Nike é imagem; o que a fala descreve (L4622-4644) foi preservado em `montar-o-calendario.md` |
| L5514-5527 | "1. Skimmable" / "2. Clear and Concise" / "3. Engaging" / "Use Infographics!" — legendas de exemplos visuais; pertencem a `doutrina/` (S.C.E.) e a `copy/` |
| L5529-5532 | "Refer To The Email Copy and Design Guides" — ponteiro para outros módulos |

---

## 4. CTA comercial

| Linhas | O que é |
|---|---|
| L5204 | "click the link in the description, first link, you can book a call with us to see if we're fit to scale your email marketing channel" — venda de serviço |
| L5234 | "watch this next video and I will see you over there" — encadeamento de YouTube |
| L4548-4550 | "shameless plug, but the email brain really is awesome" — autopromoção; a ferramenta em si foi preservada porque é o passo 4 do calendário |
| L5477 | "It's free! You can claim access here »" — CTA de captação do GPT |
| L4420, L4825-4827, L4674 | "Feel free to hit us up with any questions", "shoot us over emails", "we're here for you" — fechamento de aula |

**Mantidos apesar do enquadramento promocional**, porque são números citados:
$255,000 e $100,000 de um email (L5182-5183) e "$200 million for brands"
(L5204). Estão em `numeros-campanhas.md` marcados como claim promocional. São
alegações do vídeo de YouTube, sem verificação no corpus.

---

## 5. Ruído de ASR menor (não destrói conteúdo)

| Linha | Bruto | Leitura |
|---|---|---|
| L4250-4252 | "you're emailing three or four times a month. / a month or three or four times a week, sorry" (a duplicação de "a month" é do bruto, na virada de linha) | autocorreção; vale "a week" |
| L4298 | "So whoops, graphic and text based email" | troca de slide em voz alta |
| L4598 | "I can't talk today. So I apologize guys." | filler |
| L4574-4576 | "Yeah. Not chocolate and dates, cacao and dates." | autocorreção |
| L4715 | "the SDE framework" | é S.C.E.; o slide (L5504) grafa correto |
| L4915-4917 | "And that's going to be very important." (L4915) e "And that's going to be very important because we'll talk more about this once we get to deliverability." (L4917) | gagueira de ASR |
| L5039 | "Pretty lot." | corrompido; pelo contexto (L5037, "what's the likelihood that they open") a resposta esperada seria negativa, mas **não reconstruído** |
| L5226 | "I just change it to Aerial" | é Arial |
| L5226 | "because it's very catchy bte" | corrompido; a justificativa para remover o em dash não sobreviveu. A instrução (trocar por vírgula ou reticências) sobreviveu e foi preservada |
| L5222, L5225 | "Claio", "Clavio" | é Klaviyo (ambas as grafias em L5222; "Clavio" de novo em L5225) |
| L4813 | "The mind, a picture, pictures worth a thousand words. Yeah, I think that's correct." | filler |

---

## 6. Demonstração de UI sem procedimento reproduzível

**L4222-4232** — passeio pela conta dummy da WellCopy no Klaviyo: onde ficam as
campanhas, escolher audiência, o mockup da Calvin Klein, "subject line, test,
preview text, test, WellCopy, max, next". Não há passo replicável nem
configuração — é narração de tela com dados de teste. O único fato retido dessa
faixa são as métricas de campanha (L4236), que foram para
`numeros-campanhas.md`.

---

## 7. Conteúdo que pertence a outra pasta

Lido, não escrito aqui, para não duplicar:

| Linhas | Assunto | Destino |
|---|---|---|
| L4676-4680, L4687-4757, L5493-5521 | S.C.E. (Skimmable / Clear & Concise / Engaging), cliente 2025-2026, 3 segundos de atenção | `doutrina/sce-o-framework-que-atravessa-tudo` |
| L4759-4813, L5523-5527 | Infográficos: checklist, feature diagram, timeline, numbered list, comparison chart, table, flow chart, graph | `copy/` ou `design/` |
| L4236 | Benchmarks de open rate, click rate, placed order rate | `otimizacao/` ou `deliverability/` — registrados em `numeros-campanhas.md` |
| L4889, L4919-4945 | Sender reputation, analogia do score de crédito, como o Gmail classifica | `deliverability/` — o essencial ficou em `segmentacao.md` porque é o argumento dele para segmentar |
| L5127 | "We'll talk about this more in the Sunset Flow" | promessa nunca cumprida no corpus; já registrada como lacuna conhecida em `_protocolo.md` |

---

## 8. Exemplos de terceiros usados como ilustração

Marcas citadas com copy alheia, preservadas na nota só quando ilustram uma
regra: Magic Mind (L4308-4320), Breeze (L4354-4368, L5187-5191), Live Fresh
(L4508-4510, L5199-5200), Snow (L5194-5196), Velvet Caviar (L5198), Seed
(L4753-4755, "92 days or 2000 hours of your life on the toilet"), Nike
(L4622-4644), The Conscious Bar (L4556-4592). A copy dessas marcas **não é
artefato do Max** e não foi tratada como tal.
