---
tipo: registro-de-aplicacao
assunto: aplicacao-do-laudo-de-autoria
autor: max-sturtevant
status: rascunho
---

# O que esta unidade fez

Aplicou [[_autoria]] às notas. O laudo estabelece **quem fala**; esta unidade
mudou `registro:`, a prosa de atribuição e os `_index.md` para que a saída do
advisor nunca cite como fala de Max o que não é.

**Nenhum conhecimento foi apagado.** Só mudou quem pode ser citado como autor.

## Como a exposição foi apurada

Não pelo laudo direto. Para cada nota: `fonte:` do frontmatter + **toda** âncora
`L####` do corpo, conferidas contra a estrutura do bruto com
`grep -n -E "^(# |Transcrição do Vídeo|\# File-)"`.

Isso revelou uma distinção que as faixas do laudo não separam e que decidiu vários
casos: **dentro de cada faixa de vídeo há um cabeçalho de bullets escritos** (do
mesmo doc GAMMA), antes do marcador `Transcrição do Vídeo :`. Esses bullets são
artefato escrito, não fala. As faixas de fala reais:

| Bloco | Bullets escritos | Fala |
|---|---|---|
| Campaign Strategy | L4189-4200 | **L4202-4421** |
| Campaign Calendar Creation | L4422-4440 | **L4444-4675** |
| Creating Great Campaigns | L4676-4683 | **L4686-4828** |
| Segmentation | L4829-4843 | **L4846-5154** |
| ChatGPT Copywriting | L5617-5664 (inclui o prompt L5627-5661) | **L5667-5866** |
| Utilizing Infographics | L5867-5885 | **L5888-6082** |
| Subject Lines & Preview Texts | L6083-6098 | **L6101-6248** |
| What is Deliverability? | L8365-8378 | **L8381-8517** |
| Warming Your Domain | L8518-8529 | **L8532-8646** |
| High Leverage A/B Tests | L8762-8770 | **L8773-9109** |

Consequência prática: `copy/principio-clear-e-conciso` (L5631, L5649) **não** tem
exposição — essas linhas caem dentro do prompt escrito, não na fala. Confere com
o laudo, que a lista como não afetada.

## Padrão do bloco `# Aviso de autoria`

Todo bloco traz, nesta ordem: **faixa** → **classificação com a certeza explícita**
→ **critério** → **o que na nota vem de onde**.

- `outro-provado` — "prova nominal, a única do corpus" (L5753), com a ressalva de
  ASR do §4.1.
- `outro-provavel` — "sem prova nominal, a classificação é estilométrica…
  `outro-provavel` não é `outro-provado`" (§7.3).

O critério citado é sempre **idioleto** (§2.1). Todo bloco diz explicitamente que
**a saudação de abertura não é critério e não pode ser citada como evidência**,
nomeando a contraprova (§5, L7603 + L7817).

---

# A tabela

## `deliverability/` — 9 de 9 + índice

| Nota | Exposição encontrada | `registro:` antes → depois | O que mudou na prosa |
|---|---|---|---|
| `o-que-e` | fala L8382-8396, L8418-8422, L8621-8622 (`outro-provavel`); slide L8655-8679 | `[transcricao, slide]` → `[slide, outro-narrador]` | "o que **ele** chama de infraestrutura" → "o que o material chama"; "O exemplo **dele**" → "O exemplo apresentado"; "onde **ele** literalmente narra" → "onde a narração lê"; "**Ele** usa uma segunda analogia" → "O material usa"; "**Ele** lista os quatro juntos" → "Os quatro são listados" |
| `metricas-alvo` | fala L8430-8452; slide L8706-8719 | `[transcricao, slide]` → `[slide, outro-narrador]` | "**Ele** promete aprofundar" → "O material promete"; "nos flows **ele** não afirma, hesita" → "o material não afirma"; "O que **ele diz** que o unsubscribe serve" → "O que a fala diz". Aviso separa a tabela (slide, de Max) do resto |
| `setup-tecnico` | fala L8396-8398, L8408-8414; deck L8522-8526 e L8667-8692 | `[transcricao, slide]` → `[slide, outro-narrador]` | título "A posição **dele**" → "A posição do material"; "A fonte oficial que **ele** indica / Não é o material **dele**. **Ele** delega" → "A fonte oficial indicada / Não é material próprio. O curso delega"; "a agência **dele** manda" → "a agência manda", com marca de faixa não-Max |
| `so-envie-para-engajados` | fala L8456-8482; slide L8721-8734 | `[transcricao, slide]` → `[slide, outro-narrador]` | "a razão declarada de **ele** endurecer a regra" → "a razão declarada do endurecimento"; "**ele** não escolhe" → "a fala não escolhe" |
| `upload-para-deliverability` | fala L8490-8504; slide L8740-8748 | `[transcricao, slide]` → `[slide, outro-narrador]` | "**Ele mesmo** desvia da própria seção" → "A própria narração desvia", + nota de que o walkthrough longo (design, L8009-8065) é `max-provado`; "**Ele** chama de double-edged sword" → "O material chama"; "**Ele** nomeia os dois beneficiários" → "A fala nomeia"; "**Ele** promete" → "O material promete" |
| `auditoria-glockapps` | fala L8508-8514, L8414, L8641-8643; slide L8691, L8750-8757 | `[transcricao, slide]` → `[slide, outro-narrador]` | "**Ele** afirma que é at least free" → "A fala afirma"; "**Ele** acrescenta" → "A fala acrescenta"; "**ele** vai na mesma direção" → "A fala vai"; "em L8414 **ele** chama o Glockapps" → "em L8414 chama" |
| `reparo-de-reputacao` | **só fala** L8589-8597 | `[transcricao]` → **`[outro-narrador]`** | "O quadro que **ele** descreve" → "O quadro descrito na aula"; "O racional" → "O racional apresentado"; "A ressalva é **dele**" → "A ressalva é do material"; "**ele** aponta outra saída" → "o material aponta"; "Escopo declarado por **ele**" → "Escopo declarado na aula". Aviso diz que aqui **não sobra nada de Max** |
| `warming-casos-reais` | **só fala** L8607-8639 | `[transcricao]` → **`[outro-narrador]`** | "o topo que **ele próprio** declara" → "o topo declarado na mesma narração". Aviso: os dois casos são da agência narrada, não relatos pessoais dele |
| `warming-do-dominio` | fala L8532-8646; deck L8522-8526 e L8728 | `[transcricao, slide]` → `[slide, outro-narrador]` | "A imagem que **ele** usa" → "A imagem usada na aula"; "**ele** não lista as outras" → "as outras nunca são listadas"; "Ressalva **dele**" → "Ressalva do material"; "**ele diz** … Em 08:08 **ele diz**" → "a fala dá … dá"; "**Ele** não dá critério" → "O material não dá critério"; "a autocrítica **dele**" → "a autocrítica da equipe narrada"; "**ele** recomenda uma ferramenta" → "o material recomenda". Aviso registra que este é o procedimento com **menor lastro de autoria** do corpus |
| `_index` | pasta inteira | `[transcricao, slide]` → `[slide, outro-narrador]` | bloco `# Aviso de autoria — a pasta inteira` no topo; coluna `tipo` de cada linha marcada com `outro-narrador` / `só outro-narrador` |

## `otimizacao/` — 7 de 7 + índice

| Nota | Exposição encontrada | `registro:` antes → depois | O que mudou na prosa |
|---|---|---|---|
| `quando-vale-testar` | fala L8774-8828, L9096-9108; slide L9116-9141 | `[transcricao, slide]` → `[slide, outro-narrador]` | "A pergunta que **ele diz** receber" → "que o material diz receber"; "**Ele** aplica isso a si mesmo" → "O material aplica isso ao próprio caso" |
| `send-time` | fala L8828-8860; slide L9143-9149 | `[transcricao, slide]` → `[slide, outro-narrador]` | "O raciocínio **dele**" → "O raciocínio apresentado"; "Leitura **dele**" → "Leitura da aula"; "**ele** chama o teste de a time delay test" → "a fala chama"; "em categorias **ele lê** a mesma coluna" → "a mesma coluna é lida" |
| `grafico-vs-texto` | fala L8862-8888; slide L9151-9157 | `[transcricao, slide]` → `[slide, outro-narrador]` | "**Ele** trata o formato como já coberto" → "O material trata"; título "Onde **ele** manda usar cada um" → "Onde o material manda"; "A regra que **ele** fecha" → "A regra de fechamento". Aviso remete a doutrina/texto-puro, que tem âncora `max-provado` |
| `categorias-vs-produtos` | fala L8890-8918; slide L9159-9163 | `[transcricao, slide]` → `[slide, outro-narrador]` | "O exemplo é" → "O exemplo apresentado é"; "O motivo pelo qual **ele valoriza**" → "o material valoriza"; "que **ele descreve** como gerador de dado" → "descrito como"; "fica como **ele falou**" → "fica como foi falado" |
| `testar-subject-line-por-receita` | fala L8918-8944; slide L9165-9174 | `[transcricao, slide]` → `[slide, outro-narrador]` | "O teste se decide por receita" → "No material, o teste se decide"; marcadas como não-Max as referências cruzadas à fala de copy (L6121), e como slide de Max o teto de L6805 e a ressalva L9167 |
| `flow-time-delays` | fala L8946-8970; slide L9176-9180 (= L4141-4145 no deck de flows) | `[transcricao, slide]` → `[slide, outro-narrador]` | "**ele** repete cart abandoned duas vezes" → "cart abandoned aparece duas vezes"; "A hesitação **dele**" → "A hesitação … é do narrador da aula, não de Max"; "o aviso" → "o aviso, na aula" |
| `outros-testes` | fala L8972-9094; slide L9182-9209 | `[transcricao, slide]` → `[slide, outro-narrador]` | "**Ele** atravessa tudo depressa" → "A narração atravessa"; "**Ele** encerra citando" → "A aula encerra citando"; o "we" do mystery discount marcado como equipe narrada |
| `_index` | pasta inteira | `[transcricao, slide]` → `[slide, outro-narrador]` | **aviso pré-laudo substituído** — o antigo dizia "aqui é inferência por assinatura"; o novo dá faixa, classificação estilométrica, contagem de marcadores de idioleto e declara que "o Yo, yo de L8774 não prova nada". "the tests that our team runs" (L8798) marcado como declaração da equipe |

## `campanhas/` — 8 de 9 + índice

| Nota | Exposição encontrada | `registro:` antes → depois | O que mudou na prosa |
|---|---|---|---|
| `frequencia-de-envio` | fala L4220, L4238-4296, L4404-4406; bullets L4191-4192; slide L5247-5298 | `[transcricao, slide]` → `[slide, outro-narrador]` | "segundo **ele**" → "segundo a aula"; "**ele diz** para não enviar 5-6x" → "o material manda não enviar"; sweet spot falado marcado "fala — não-Max". Aviso registra §6.2: o "two to four … sweet spot" deixa de ser citável como fala dele; a regra sobrevive pelo slide L5255 e por L2367 (faixa Max) |
| `ocupar-espaco-mental` | fala L4244-4250; bullet L4194; slide L5278-5284 | `[transcricao, slide]` → `[slide, outro-narrador]` | "o termo **dele**" → "o termo aparece nos dois registros (fala não-Max; slide de Max)"; título "O racional **dele**" → "O racional apresentado"; **"Atribuída ao pai dele"** → "O narrador a atribui ao próprio pai — e o narrador não é Max"; "O cenário que **ele** descreve" → "O cenário descrito"; "O contraste que **ele** desenha" → "O contraste desenhado na aula"; "**ele mesmo** declara que varia por estudo" → "a própria fala declara" |
| `mix-grafico-e-texto` | **três origens**: fala não-Max L4298-4370 · fala Max L5174-5175 e L5230-5233 · slide L5300-5311 | `[transcricao, slide]` → **`[transcricao, slide, outro-narrador]`** | aviso separa as três origens item a item; coluna `Registro` da tabela de ratios trocada de "transcrição" para `outro-narrador` / `transcricao (Max)`; "O argumento circular que **ele faz questão de fechar**" → "O argumento circular, no material", + ponte para L5230, que é fala dele |
| `os-cinco-pilares-de-conteudo` | fala L4372-4376, L4472-4490, L4538-4542; bullets L4426-4430; slide L5318-5345 | `[transcricao, slide]` → `[slide, outro-narrador]` | título "O que **ele diz** de cada um" → "O que o material diz de cada um (fala, não-Max)"; "a fonte que **ele** nomeia" → "nomeada na aula"; "**Ele** volta a esses pilares" → "A narração volta"; "o ponto **dele**" → "o ponto da aula" |
| `montar-o-calendario` | fala L4441-4674; bullets L4424-4437; slide L5325-5491 | `[transcricao, slide]` → `[slide, outro-narrador]` | "**Ele** é explícito" → "A aula é explícita"; "Como **ele** usa" → "Como o material demonstra"; título "O prompt que **ele** demonstra" → "O prompt demonstrado"; "**Ele** responde com" → "A resposta digitada na demonstração"; "Refinamentos que **ele** pede" → "Refinamentos pedidos … (não-Max)"; "**Ele** avisa" → "A demonstração avisa"; degrau de 180 dias marcado como fala não-Max |
| `cem-ideias-de-email` | fala L4516-4542; slide L5356-5472 | `[slide, transcricao]` → `[slide, outro-narrador]` | "**ele** declara que não vai lê-las" → "o narrador (não-Max) declara"; "os únicos itens que **ele comenta**" → "os únicos itens comentados"; "O enquadramento **dele**" → "O enquadramento", + ponteiro para [[doutrina/roubar-e-o-metodo]], que é a versão com lastro de Max. **O artefato (as 100 ideias) é slide e continua intacto** |
| `segmentacao` | fala L4844-5153; bullets L4829-4840; slide L5534-5598 | `[transcricao, slide]` → `[slide, outro-narrador]` | "O teste que **ele** dá" → "O teste dado"; "o que **ele trata** como decisivo" → "o que o material trata"; "A analogia **dele**" → "A analogia usada", + nota de que a mesma imagem abre deliverability, também não-Max; "**Ele** prefere contagem de pedidos" → "O slide prefere"; "o Sunset Flow, que **ele promete** em L5127" → "prometido em L5127 … e a promessa é do outro narrador" |
| `nao-hipersegmentar` | fala L4993-5021, L5135-5151; slide L5571-5597 | `[transcricao, slide]` → `[slide, outro-narrador]` | "mesmo assim **ele** recomenda não fazer" → "o material recomenda"; "O custo que **ele** nomeia" → "O custo nomeado"; "**Ele** enquadra isso como 80-20" → "A fala enquadra". Aviso registra que o argumento inteiro tem lastro de slide |
| `email-de-texto-puro` | **nenhuma** — L5155-5236 é `max-provado` | não mexido | — |
| `_index` | 8 de 9 | (sem `registro:`) → `[slide, outro-narrador]` | bloco `# Aviso de autoria — 8 das 9 notas` no topo, com as quatro faixas e a contagem de marcadores; coluna `tipo` marcada por nota; cabeçalho da tabela de frequência passa a dizer "Slide de Max" × "Fala **não-Max**" |

## `copy/` — 6 de 9 (o laudo dizia 5 + 1) + índice

| Nota | Exposição encontrada | `registro:` antes → depois | O que mudou na prosa |
|---|---|---|---|
| `prompt-de-copy` | **`outro-provado`** L5667-5865; prompt escrito L5627-5661 = L6739-6770 | `[slide, outro-narrador]` (mantido) | **aviso pré-laudo substituído.** O antigo era só "Atenção" no meio do corpo; o novo vai ao topo, nomeia `outro-provado`, dá o critério e explicita que **o prompt é artefato escrito e continua verbatim e citável**. A seção antiga virou "# A triangulação sobre o Email Marketing Brain", com as quatro reivindicações em 1ª pessoa (L5212, L6387, L6774, L5475) contra L5753. "onde está o trabalho" marcado como leitura do material |
| `email-architect` | **`outro-provado`** L5725-5735, L5803-5833; slide L6787-6792 | `[slide, outro-narrador]` (mantido) | **aviso pré-laudo substituído** e movido para o topo; a seção "Atenção: a voz desta transcrição não é a do Max" foi removida (redundante). "Na fala, com o mecanismo" → "Na fala do outro narrador"; "A troca é explícita" ganhou marca de que a formulação está no slide, logo é de Max |
| `infograficos` | fala L5886-6081; slide L5867-5882, L6652-6727 | `[slide, transcricao]` → `[slide, outro-narrador]` | "frequência atribuída" → "atribuída à equipe que narra, não a Max"; "um teste A/B que **ele diz** rodar" → "que a aula diz rodar"; "um flow chart que **ele mesmo** não identifica" → "que a própria narração não identifica" |
| `subject-lines` | **três origens**: slide L6798-6827 e L6083-6095 · fala não-Max L6101-6247 · **fala Max L6341 e L6400** | `[slide, transcricao]` → **`[transcricao, slide, outro-narrador]`** | aviso separa as três; título "# A evidência de A/B" → "(registro: outro-narrador)"; "A evidência negativa que **ele oferece contra si mesmo**" → "que o slide oferece contra a própria alavanca"; "O ponto que **ele extrai**" → "O ponto extraído na aula"; no conflito de comprimento, marcado que as SLs que **ele** escreve ao vivo são a única fala dele na nota |
| `preview-texts` | fala L6171-6217; bullet L6090; slide L6829-6845 | `[slide, transcricao]` → `[slide, outro-narrador]` | "**Ele** narra a reação pretendida" → "A aula narra … (fala não-Max)"; "A fala prescreve o oposto" → "A fala — não-Max — prescreve"; "o princípio que **ele chama** de o melhor" → "que a mesma fala chama" |
| `principio-skimmable` | fala L5889-5891 (pontual); slide L6578-6598, L5607 | `[slide, transcricao]` → `[slide, outro-narrador]` | título "# Como isso aparece na fala" → "(registro: outro-narrador)", com "que **não** é fala de Max"; "o critério **dele** para infográfico" → "o critério que ali se dá" |
| `principio-engaging` | **1 citação**: L6219, fala `outro-provavel` | `[slide]` → `[slide, outro-narrador]` | L6219 marcada "frase do outro narrador, não de Max". **Discrepância com o laudo — ver abaixo** |
| `o-que-evitar` | **nenhuma** — L6509-6548 é slide; L5611 é bullet escrito | não mexido | — |
| `principio-clear-e-conciso` | **nenhuma** — L5631 e L5649 caem dentro do prompt escrito L5627-5661, não na fala | não mexido | — |
| `_index` | 6 de 9 | (sem `registro:`) → `[slide, transcricao, outro-narrador]` | bloco `# Aviso de autoria — 6 das 9 notas` com as três faixas; ⚠ por linha na tabela; o item 2 de "Dois merecem aviso" reescrito para cobrir as três faixas, não só L5667-5866 |

## `doutrina/` — 8 de 13 (+ 1 aviso anulado) + índice

Esta pasta tinha **nove avisos escritos antes do laudo**, e todos argumentavam
pela assinatura de abertura. **Os nove foram reescritos.**

| Nota | Exposição encontrada | `registro:` antes → depois | O que mudou na prosa |
|---|---|---|---|
| `a-ia-e-um-copywriter-junior` | **`outro-provado`** L5667-5865; slide L6731-6774; **fala Max** L6386-6411 | `[outro-narrador, slide, transcricao]` → `[transcricao, slide, outro-narrador]` | **aviso reescrito**: passa a nomear `outro-provado`, dar o critério de idioleto e derrubar a saudação; mantém a prova L5753 e explicita que o walkthrough do Calvin Klein (L6386-6411) é `max-provado`, o que sustenta a seção "O que sobra e é atribuível" |
| `desconto-constante-barateia-a-marca` | fala não-Max L4372-4392; **fala Max** L6260-6261, L6350, L6364-6414; slide L5313-5321, L4197 | `[transcricao, slide]` → `[transcricao, slide, outro-narrador]` | **aviso reescrito** — o antigo dizia "vem do vídeo aberto com Hello, hello em L4204"; o novo dá faixa e classificação estilométrica. "O mecanismo, na fala" → "na fala do outro narrador"; "os ângulos que **ele** lista" → "listados no material"; "o que **ele chama** de marketing" → "o que a mesma fala chama"; "**Ele** não proíbe desconto" → "O material não proíbe"; Gymshark e Calvin Klein marcados `max-provado` |
| `disruptor-vence-no-inbox` | **só fala não-Max** L6191-6229 | `[transcricao]` → **`[outro-narrador]`** | **aviso reescrito** — o antigo citava "Hello, hello. So got one more for you" (L6103) como evidência e dizia "não há prova …, só a assinatura compartilhada". O novo dá a faixa L6101-6248 e a classificação estilométrica. "A analogia que **ele** usa" → "A analogia usada"; "A tese" → "do material, não dele"; "Restrição que **ele** impõe" → "imposta"; título "Onde **ele mesmo** relativiza" → "Onde o próprio material relativiza"; "**Ele** desinfla" → "A aula desinfla" |
| `o-basico-entrega-90-por-cento` | fala não-Max L8778-9102; **fala Max** L22; slide L8764-8765, L9118-9123 | `[transcricao, slide]` → `[transcricao, slide, outro-narrador]` | **aviso reescrito** — o antigo abria com "abre com Yo, yo, what is going on? (L8774) — a assinatura do narrador". O novo dá faixa e idioleto, e nomeia o que sobrevive: as duas versões de slide e o pilar #3 de L22. Coluna `Registro` da tabela de proporções: "transcrição" → **outro-narrador** nas duas linhas faladas; "as duas listas que **ele** dá" → "as duas listas faladas — ambas na faixa não-Max"; "**Ele** não manda parar de testar" → "A aula não manda" |
| `o-numero-decide-nao-a-opiniao` | fala não-Max L6227-6229, L8792; **fala Max** L21-22; slide L9127-9131 | `[transcricao, slide]` → `[transcricao, slide, outro-narrador]` | **aviso reescrito** — o antigo identificava a versão de Max por "aberta com Welcome back, my beautiful eCommerce folk (L21)" e as outras por "Yo, yo" e "Hello, hello". O novo mantém L22 como a versão dele, mas por classificação de bloco (`max-provavel`, idioleto), não por saudação. L8792 e L6227 marcadas **outro-narrador** nas citações; "O teto … **ele mesmo** dá" → "vem do material, não dele" |
| `otimize-para-a-varredura-nao-para-a-leitura` | fala não-Max L4703-4707; **fala Max** L7157-7169; slides L5500, L6516-6598, L8183-8195 | `[transcricao, slide]` → `[transcricao, slide, outro-narrador]` | **aviso reescrito** — o antigo dizia que a fala de design "abre Alrighty …, a assinatura dele". O novo sustenta a mesma conclusão pelo idioleto ("I'd recommend majority of them", L7029) e pela âncora `max-provado` L7817. Linha "2-3 segundos" da tabela marcada **fala não-Max**; "**Ele** dá a consequência de falhar" → "A consequência … é dada … e essa formulação é do outro narrador"; título "Onde **ele mesmo** relativiza" → "Onde o corpus relativiza" |
| `sce-o-framework-que-atravessa-tudo` | fala não-Max L4703-4767, L4819-4821; **fala Max** L7007, L7155; slides L5495-5525, L6558-6660 | `[transcricao, slide]` → `[transcricao, slide, outro-narrador]` | **aviso reescrito** — o antigo dizia "vêm do vídeo aberto com Hello, hello em L4687, a assinatura do narrador que …". O novo dá faixa e idioleto. "**Ele** explica por que repete" → "A aula explica … e essa fala é do outro narrador"; "E fecha a aula" → "(mesma faixa não-Max)"; "o infográfico … **ele** chama de the cheat code" → separado: L5525 é slide de Max, L4759 é fala não-Max |
| `texto-puro-funciona-porque-e-raro` | fala não-Max L4326-4352; **fala Max** L2256-2274, L5178-5232; slide L5300-5307 | `[transcricao, slide]` → `[transcricao, slide, outro-narrador]` | **aviso reescrito e fortalecido.** O antigo dizia "O núcleo está na voz do Max — **por inferência, não por prova**", porque a masterclass "é vídeo de YouTube sem assinatura de abertura". Pelo laudo, L5155-5236 é **`max-provado`** (L5212, "my custom GPT"): a nota passa a dizer "agora por prova, não por inferência". Marcadas as citações não-Max de L4326-4352 |
| `roubar-e-o-metodo` | **nenhuma** | `[transcricao, slide]` (mantido) | **aviso pré-laudo anulado.** O antigo `# Nota de autoria` dizia que o vídeo "não traz nenhuma das assinaturas" e que "vem logo depois de um vídeo do outro narrador (L7603)" — **L7603 é comprovadamente Max** (L7817). O novo declara "sem exposição", explica que o critério antigo caiu e re-sustenta a atribuição pelo idioleto ("my favorite" 4×, "my websites" L7871 ≡ slide L8311) |
| `_index` | 8 de 13 | (sem `registro:`) | **a tabela de assinaturas de abertura foi removida** e substituída por uma tabela de faixas com classificação (`outro-provado` × `outro-provavel`), mais o critério de idioleto e a declaração de que saudação e pronome coletivo caíram. ⚠ por linha nas tabelas temáticas. Entrada `doutrina-narrador-da-aula-de-ia` marcada "**Superado por [[_autoria]]** nas partes que argumentam por assinatura" |

## `flows/` — 2 notas (fora das cinco pastas do escopo; ver ressalva)

| Nota | Exposição encontrada | `registro:` antes → depois | O que mudou na prosa |
|---|---|---|---|
| `winback` | **1 citação**: L5057, fala `outro-provavel` | `[transcricao, slide]` → `[transcricao, slide, outro-narrador]` | "A fala do mesmo módulo confirma" → "confirma — mas essa fala **não é de Max**". A definição que vale continua sendo o slide L5589 |
| `sunset` | **2 citações**: L5127 e L5129, fala `outro-provavel`; L5127 está no `fonte:` | `[transcricao, slide]` → `[transcricao, slide, outro-narrador]` | "**ele** promete: We'll talk about this more in the Sunset Flow" → "o material promete … e quem a faz não é Max"; linha da tabela `Suppress list (fala)`: "transcrição" → **outro-narrador**; "**ele** os apresenta juntos" → "o corpus os apresenta juntos" |

## `_staging/conflitos-doutrina.md`

Entrada `doutrina-narrador-da-aula-de-ia` recebeu banner **SUPERADO EM PARTE POR
[[_autoria]]**: a conclusão de dois narradores fica, a tabela de assinaturas fica
como registro do que foi tentado, **não como evidência**.

---

# Onde o laudo e a âncora real discordaram

Três casos. Em nenhum deles a discordância inverte a conclusão do laudo — todas
são notas que o laudo classificou como **não afetadas** e que, pela âncora do
corpo, têm exposição pontual.

### 1. `copy/principio-engaging` — o laudo diz que escapa; a âncora diz que não

O laudo (§6.1) lista as notas de `copy/` afetadas e conclui: "Escapam
`o-que-evitar`, `principio-clear-e-conciso` e `principio-engaging`, que saem do
deck." A nota **de fato sai do deck** — mas cita, como reforço do argumento sobre
repetição, a frase **L6219** ("people are so accustomed to seeing the same thing
over and over and over and over"), que é fala dentro de L6101-6248,
`outro-provavel`.

**Resolvido a favor da âncora:** `registro: [slide, outro-narrador]`, aviso
mínimo, uma frase marcada. O corpo doutrinário da nota não muda.

### 2. `flows/sunset` — o laudo lista `winback`, não `sunset`

O laudo (§6.1) diz "`flows/` — 1 de 12 notas. Só `winback` (L5057, dentro de
Segmentation)". Mas `flows/sunset` traz **L5127 dentro do próprio `fonte:`** e
cita L5127 e L5129 no corpo, ambas dentro de L4846-5154 (`outro-provavel`), com
atribuição direta ("ele promete").

**Resolvido a favor da âncora**, com o mesmo tratamento pontual de `winback`.

### 3. Três notas em pastas declaradas limpas — **não tocadas, por instrução**

A varredura de âncoras encontrou citações de faixa não-Max em três notas de
pastas que o laudo declara limpas e que esta unidade foi instruída a não alterar.
**Nenhuma foi modificada.** Ficam registradas para quem for revisar o laudo:

| Nota | Linha citada | Faixa | Como a nota a usa |
|---|---|---|---|
| `design/emails-baseados-em-imagem` | L8500, L8504 | L8381-8646, `outro-provavel` | citação longa em blockquote sobre HTML e deliverability, dentro do conflito `design-html-vs-imagem` |
| `fundamentos/metricas-nucleo` | L6229 | L6101-6248, `outro-provavel` | "10%, maybe 15" usado como contraponto quantitativo a L180 |
| `sms/frequencia` | L4242 | L4202-4421, `outro-provavel` | "sweet spot de 2-4x" citado como referência cruzada ao módulo de campanhas |

O laudo está correto no que afirma — nenhuma dessas pastas **deriva** de faixa
não-Max. A divergência é de referência cruzada: as notas importam uma frase de
fora. Se o critério for "nenhuma frase de faixa não-Max sem marca", as três
precisam de uma linha; se for "nenhuma nota derivada de faixa não-Max", o laudo
está certo e não há o que fazer.

### Confirmação por amostragem das pastas limpas

`design/`, `fundamentos/`, `list-growth/` e `sms/` foram varridas por âncora
(todas as ocorrências `L####` de todas as notas, classificadas contra as faixas do
laudo). Resultado: **`list-growth/` está limpa; `design/`, `fundamentos/` e
`sms/` têm exatamente as três referências cruzadas da tabela acima e nada mais.**
Nenhuma dessas notas tem `fonte:` em faixa não-Max.

---

# O que esta unidade deliberadamente não fez

- **Não apagou conhecimento.** Nenhuma afirmação, número, verbatim ou racional
  saiu de nota nenhuma. Só mudou a atribuição.
- **Não mexeu em `_numeros`, `_conflitos` nem `_cobertura`.** A consequência de
  §6.2 (a frequência de campanhas muda de dono) está registrada no aviso de
  `campanhas/frequencia-de-envio` e no `_index` da pasta; propagá-la para as notas
  de controle é trabalho de outra unidade.
- **Não tocou em `design/`, `fundamentos/`, `list-growth/` e `sms/`**, por
  instrução — ver o caso 3 acima.
- **Não reescreveu `_staging/conflitos-doutrina.md`**, só marcou a parte superada.
