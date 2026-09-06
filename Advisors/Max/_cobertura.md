---
tipo: indice
assunto: cobertura-e-lacunas
autor: max-sturtevant
status: rascunho
---

# Para que serve

O [[_protocolo]] manda recusar tudo que estiver fora do corpus, e manda que a
recusa **nomeie a lacuna e ofereça o vizinho**. Esta nota é o que torna isso
possível: o mapa do que o corpus cobre, com que densidade, e — principalmente —
de que **tipo** é cada buraco.

O tipo é o que decide a forma da resposta. Um assunto que o corpus nunca tocou
se recusa por inteiro. Um assunto em que ele deu a finalidade e engoliu a
execução se responde pela metade, entregando a metade que existe. Uma promessa
que ele fez e não cumpriu se responde citando a promessa — porque o usuário vai
perguntar exatamente por ela. E um assunto que ele **entregou errado** exige o
oposto de uma recusa: exige o aviso.

Regra de leitura: consultar antes de recusar, nunca depois. "Não sei" não é
resposta aceitável deste advisor.

**Lacuna não é descarte.** Descarte é ruído que tiramos de propósito — pangrama
de teste de microfone, CTA de afiliado, contaminação de outra gravação. Está
todo listado em [[_fontes]] e nos `_staging/descartes-*`. Lacuna é conteúdo do
curso que **falta**. Nunca confundir os dois: nenhuma linha descartada vira
lacuna, e nenhuma lacuna se explica dizendo "isso a gente tirou".

---

# Mapa de densidade por assunto

**Como a densidade foi medida.** Por palavras, não por linhas — as linhas do
bruto variam de 3 a 300 palavras e a contagem de linha mente. Total do arquivo:
121.344 palavras ([[_fontes]]).

| Assunto | Pasta | Notas | Registro disponível | Densidade | Observação |
|---|---|---|---|---|---|
| Pilares, métricas-núcleo, glossário, escolha de ESP, estado do mercado | [[fundamentos/_index]] | 10 | ambos — 7.675 pal. fala + 2.490 slide | **média** | O glossário inteiro é slide **que ele declara não ter lido** (L217, L227). Três alvos existem só ali e não têm confirmação em lugar nenhum: bounce `<2%` (L437), list cleaning `60–90+ days` (L443), largura `600–700px` (L469). |
| Princípios transversais e processo de criação | [[doutrina/_index]] | 13 | ambos, faixa de todos os módulos | **média** | Pasta derivada, não modular. **8 das 13 notas saem de faixa não-Max** — é a pasta mais exposta ao problema de autoria, porque doutrina é justamente o que o advisor parafraseia na voz dele. |
| Pop-up, oferta, tipos de form, captação | [[list-growth/_index]] | 11 | ambos — 16.339 pal. fala + 1.486 slide | **alta** | Único módulo com **dois** walkthroughs de tela completos (Klaviyo mobile e desktop). Contrapeso: o deck tem duas seções de tutorial vazias, "Klaviyo Pop-Up Form Creation" (L1300) e "Alia Pop-Up Form Creation" com o placeholder `[need]` (L1302-1304). |
| Os 8 flows | [[flows/_index]] | 12 | ambos — 12.041 pal. fala + 4.921 slide | **alta para 7 flows · nula para o 8º** | Maior deck do corpus. Mas **nenhum dos oito flows tem filtro nem condição de saída declarados**, e cart/checkout abandon também não tem delay. O Sunset não tem aula (ver cobertura parcial). |
| Frequência, calendário, pilares de conteúdo, segmentação | [[campanhas/_index]] | 9 | ambos — 13.319 pal. fala + 3.859 slide | **média-alta** | **A fala inteira do módulo (L4189-5154) é `outro-provavel`.** O que sobra de Max escrito é o deck. Um loop de ASR come o racional de testimonials (L4480-4488). |
| S.C.E., subject line, preview text, infográficos, prompt de IA | [[copy/_index]] | 9 | ambos — 26.050 pal. fala + 2.111 slide | **enganosa: alta em palavra, média em doutrina** | 20.275 das 26.050 palavras são **dois teardowns de YouTube** (Gymshark, MrBeast) sobre emails de marcas específicas — narração, não doutrina. As aulas próprias somam 5.775 palavras. Agravante: o vídeo dos princípios de copy **não foi transcrito** (L5615, o único marcador de transcrição vazio do arquivo), e 30 rótulos de exemplo vieram sem imagem. |
| 3 princípios, doutrina por seção, transições, upload | [[design/_index]] | 13 | ambos — 11.422 pal. fala + 1.976 slide | **alta em doutrina · baixa em exemplo** | A doutrina está completa e é dupla-registrada. Nenhum dos 13 exemplos visuais do deck sobreviveu (L8173-8300). E a seção de transições promete métodos e não lista nenhum (L8302-8307). |
| Setup técnico, warming, reparo, auditoria | [[deliverability/_index]] | 9 | ambos — 6.818 pal. fala + 852 slide | **baixa** | Segundo menor módulo. **Toda a fala é `outro-provavel`** e o deck tem 113 linhas. É o único módulo com perda de áudio mensurável: dois cortes, 41s e 29s. Recusa provável. |
| Testes A/B | [[otimizacao/_index]] | 7 | ambos — 3.123 pal. fala + 825 slide | **baixa** | **O menor módulo do corpus.** O deck é cópia quase verbatim do deck de flows (L4141-4176 ≡ L9151-9180) — não conta como confirmação cruzada. Fala inteira `outro-provavel`. Treze testes listados sem um único número, vencedor ou caso. Recusa provável. |
| Doutrina de SMS, 5 flows, calendário, horários | [[sms/_index]] | 8 | ambos — 3.851 pal. fala + 2.184 slide | **baixa** | **Módulo invertido: o slide carrega mais que a fala.** A fala é um único vídeo de YouTube de ~16 min. Nenhum flow de SMS tem metric, trigger, filtro ou exclusão. Recusa provável, e é o módulo com o pior problema de compliance (ver §4). |

**Total: 101 notas de conteúdo** em dez pastas, mais dez `_index.md` e as seis
notas de controle.

**Leitura operacional da coluna densidade.** Baixa não significa "não responda";
significa "a chance de a resposta exigir algo que não está lá é alta —
verifique a cobertura antes de formular". Os três módulos de densidade baixa
(deliverability, otimização, SMS) somam **17.653 palavras**, 14,5% do corpus,
e concentram desproporcionalmente as lacunas dos tipos abaixo.

---

# As lacunas, classificadas por tipo

## Lacuna total — o corpus não toca o assunto

Nem fala, nem slide, nem exemplo. Recusa inteira.

| Lacuna | Evidência da ausência |
|---|---|
| **Filtro e condição de saída de qualquer flow.** Nenhum dos oito. | Varredura das oito notas de flow: a linha `Filtros` / `Saída` da tabela está vazia em site abandon, browse abandon, cart/checkout, post-purchase, replenishment, winback e sunset. O welcome é o único com filtro declarado (`bounce less than two times`) e nem ele tem condição de saída. |
| **Delay de cart abandon e de checkout abandon.** | O deck de flows não declara delay nenhum para os dois, e a fala também não. Registrado em [[flows/otimizacao-de-flows]] (L124 da nota). **Nunca preencher por analogia com o welcome, que tem.** |
| **Os métodos de transição entre seções de email.** | L8302 abre `# **Email Transitions**`, L8307 diz "Here are a few methods to do this:" e a linha seguinte já é outro heading. Zero métodos listados no deck. Conflito registrado: `design-metodos-de-transicao-ausentes`. |
| **O racional falado do S.C.E.** | O marcador `Transcrição do Vídeo :` em L5615, sob "The Principles of Good Copy" (L5602), está **vazio** — o único do arquivo inteiro. L5617 já é a próxima seção. Só existem os bullets L5604-5611 e o link gamma. O framework que atravessa o corpus inteiro nunca foi explicado em voz. |
| **Critério de escolha dentro de catálogo.** Qual filler do welcome usar; qual dos 9 tipos de infográfico; qual dos 7 tipos de bridge; qual dos 4 métodos de list growth. | Existe catálogo, não existe ordem nem árvore de decisão. Confirmado nas quatro notas: [[flows/welcome-fillers]], [[copy/infograficos]], [[design/secao-bridge]], [[list-growth/os-quatro-metodos]]. |
| **Qualquer limiar estatístico de teste.** Amostra mínima, duração, significância, quantos testes em paralelo. | Os três módulos que tratam de teste — [[list-growth/os-sete-testes-de-form]], [[flows/otimizacao-de-flows]], [[otimizacao/quando-vale-testar]] — não têm nenhum. O único gate declarado no corpus inteiro é qualitativo: "depending on your site traffic" (L663). |
| **Janela de medição de qualquer métrica.** Se open rate é por envio, por 30 dias ou vitalício. | Nem a tabela de metas (L372-380), nem o glossário (L384-519), nem [[fundamentos/metricas-nucleo]], nem [[deliverability/metricas-alvo]] declaram janela. Nenhuma. |
| **Preço de qualquer ferramenta.** | `pricing` tem **uma** ocorrência no arquivo inteiro (L6001) e é sobre tiers de produto do cliente, não sobre custo de plataforma. Ver §4. |

## Cobertura parcial — existe finalidade e falta execução, ou vice-versa

Aqui a recusa é **parcial**: entrega-se o que existe e nomeia-se o que falta.
Recusar por inteiro o que o corpus cobre pela metade é erro tão grave quanto
inventar.

**Sunset Flow — o caso-escola.** O corpus dá a finalidade e o segmento, e não dá
nada da execução.

| O que existe | Onde |
|---|---|
| Finalidade, verbatim: "**Sunset Flow** – Triggered when a contact is no longer engaging. Removes or suppresses inactive users." | L411, slide (glossário) |
| Recomendação de uso — está na lista dos oito "recommended flows when just starting out" | L92, L94, transcrição |
| **Definição do segmento**, lida do PNG embutido na L9545 (referenciado por `![][image1]` na L3402): 180 dias sem abrir · 180 dias sem clicar · ao menos 10 emails recebidos · zero pedidos over all time | L9545, print |
| O vizinho mais próximo: o critério de suppression list que ele descreve ao prometer o sunset | L5129, transcrição |

O que **não** existe: sequência, contagem de emails, delay, subject line,
template, copy, filtro, condição de saída. Nem aula (L3398-3403 é título + link
+ imagem) nem seção no deck (o `# GAMMA FLOWS` começa em L3404 e vai do Winback
direto para Flow Optimization). O deck próprio do Sunset
(`Sunset-Flow-v13borkcrsurvpv`, L3400) não está no corpus. E o glossário diz
"removes **or** suppresses" e nunca escolhe entre os dois. Ver [[flows/sunset]].

Outros casos de cobertura parcial:

| Assunto | Tem | Falta |
|---|---|---|
| **Setup técnico de deliverability** | as siglas listadas (SPF, DKIM, DMARC, MX) e a instrução de onde ler | o que cada uma faz — nunca explicadas; nenhum valor de registro, nenhuma tela, nenhum tempo de propagação. O procedimento inteiro é "leia o artigo do Klaviyo, cheque no Glockapps". Ver [[deliverability/setup-tecnico]] |
| **Segmentos de exclusão** | "Exclusion segments should include (**but not be limited to**): Bounced 3+ times" (L4839-4840) | a lista nunca é completada. A própria frase declara que está incompleta. Ver [[campanhas/segmentacao]] |
| **Email Architect** | o conceito, o racional e a regra dos 80% | **nenhum exemplo do formato**, e nenhuma definição do artefato (documento? Figma? wireframe?). Os dois slots "Example \#1/\#2" (L6794-6796) vieram vazios. Ver [[copy/email-architect]] |
| **Alia como alternativa ao Klaviyo** | julgamento forte ("the ROI is worth it every time", L1243) e um walkthrough falado | preço, limiar de lista ou faturamento em que passa a valer, e o material do deck — que é o placeholder `[need]` (L1304). Ver [[list-growth/alia-e-a-alternativa]] |
| **Warming do domínio** | a rampa em duas fases e dois casos reais | o teto de frequência (a frase que o carregava foi truncada, L8560), o nome da ferramenta de HTML (corte de 41s), a duração total do warming — "weeks 1 to 3", "weeks 3 to 12" e uma "60 day window" não são a mesma unidade |
| **Captura de telefone no checkout** | a intenção declarada e o argumento | o procedimento — o que está lá é o de email, colado. Ver *Entregue errado*, abaixo |

## Promessa não cumprida — o material anuncia e não entrega

O usuário vai perguntar por estes itens **porque o material os prometeu**. A
resposta cita a promessa e diz que o objeto não veio.

| Promessa | Onde é feita | Estado |
|---|---|---|
| **Swipe file de 30 SMS** — "in the description in the doc I have a swipe file of 30 SMS messages which I handpicked with the help of attentive" | L9258 (fala) e L9520-9523 (slide: "I went through Attentive's SMS database and picked 30 of my favorite SMS messages") | O deck tem o título `# **30 SMS Campaigns Swipe File**` e duas frases de racional. **As 30 mensagens não estão no corpus.** |
| **Swipe file de 84 emails** — "84 different emails in here. Very useful. We'll of course attach these" | L4506 (fala) e L5351 (slide: "Use this swipe file of 84 high-converting email campaigns handpicked by me a $100M email marketer") | O slide traz um link de Google Drive. **Os 84 emails são externos ao corpus.** |
| **Documento externo de A/B tests** — "there's another document we have that outlines some of the higher leverage AB tests with a little bit more info on it as well" | L9094-9096 (fala) | Não está em `CONTEUDO BRUTO/max.md`. É a lacuna declarada pelo próprio autor no módulo mais raso do corpus. |
| **"We'll talk about this more in the Sunset Flow, obviously, as well."** | L5127 (fala, dentro da aula de segmentação) | Nunca cumprida. Não há aula nem deck de Sunset. É a promessa que fecha o caso-escola acima. |
| "We'll have examples for you" — sobre como o split por número de compras muda a copy do post-purchase | L3084 (fala) | Não entrega na faixa. Ver [[flows/post-purchase]] |
| "I'll list the other ones" — os demais flows de alta intenção durante o warming | L8545 (fala) | **Nunca lista.** |
| "maybe I'll attach a resource down below on this one" (bounce rate) · "we can maybe get more into the weeds on that in another video" (hard vs soft bounce) · "maybe we'll have a more in-depth video just talking about the importance there" (alt text / HTML) | L8438 · L8446 · L8504 | Três recursos ausentes, todos em deliverability. |
| Seções de walkthrough anunciadas e vazias: `# **Design Walkthroughs**` · `# **Copywriting Walkthroughs**` · `# **2 Copywriting ONLY Live Examples**` · `# **Copy + Design Creation Videos**` | L8357 · L6851 · L6853 · L6855, L8359 | Títulos sem uma linha de conteúdo abaixo. |
| Tutoriais de pop-up do deck: "Klaviyo Pop-Up Form Creation" e "Alia Pop-Up Form Creation" | L1300 e L1302-1304 | O primeiro vazio; o segundo com o marcador de produção `[need]` deixado no export. |
| Ponteiros de SMS para vídeo e doc externos ("I break this all down in the video", "I'll have a link to the document below it has like all the copy for you") | L9238, L9242-9243, L9246-9247, L9250 | O material apontado não está no corpus. Não confundir com lacuna nova — é a mesma lacuna, apontada cinco vezes. |

## Perda por falha técnica — o conteúdo existiu e sumiu

Estas não são omissões do autor. São falhas de ASR, de export ou de corte de
vídeo. Importa distinguir, porque a resposta muda: aqui não se diz "ele não
fala disso", se diz "o registro se perdeu".

**Os dois cortes de transcrição em deliverability.** No vídeo de warming
(L8531-8645) a mediana entre marcas de tempo é 11s e o p90 é 18s. Dois saltos
fogem da distribuição — e são o primeiro e o segundo maiores do vídeo inteiro:

- **21:52 → 22:33, L8641 → L8642, ~41 segundos.** Levou **o nome da ferramenta
  de otimização de HTML** que ele recomenda para quem cai na aba de promoções.
  Ele descreve a ferramenta, diz que trabalha com marcas conhecidas, e nunca a
  nomeia. **Irrecuperável — nunca deduzir nem sugerir um nome.** Evidência
  independente do corte dentro da própria linha: L8641 emenda duas frases de
  assuntos diferentes sem pontuação ("questions that I can help If your emails
  are landing in spam").
- **13:04 → 13:33, L8593 → L8594, ~29 segundos.** Cai no meio do raciocínio de
  reparo de reputação.

**O loop de ASR — L4480-4488.** Cinco linhas de fala (L4480, 4482, 4484, 4486,
4488) em que o reconhecimento travou repetindo *"If you're going to include
those testimonials"* — 7, 10, 11, 10 e 12 vezes, com truncamento no fim de cada
uma. Perdeu-se **o racional falado sobre como usar testimonials** dentro do
pilar Social Proof. O contexto de cada lado está íntegro: L4476-4478 fecha a
abertura do pilar, L4490 retoma já na distribuição percentual mensal.
Recuperação parcial: os bullets L4424-4430 preservam os cinco pilares com um
exemplo cada; as 20 ideias de social proof da lista de 100 (L5381-5402) cobrem
testimonial, review, UGC e press. **O racional falado não existe** — se a
pergunta for essa, recusar.

**Os ~77 rótulos de exemplo sem imagem.** O export do GAMMA trouxe as legendas e
deixou as figuras para trás. Todos dentro de blocos de slide. Distribuição
verificada em [[_fontes]]:

- **12 `**Email Example:**` em GAMMA FLOWS** — L3642, 3663 (site abandon);
  L3700, 3721, 3742, 3763 (browse abandon); L3817, 3838, 3859, 3881
  (cart/checkout); L3948, 3966 (post-purchase). É o exemplo visual de **cada
  email de cada flow de abandono** que não existe.
- **25 em GAMMA COPY** — 9 `**Ex. …**` (L6550-6650) e 16 `**Example \#1/\#2**`
  (L6676-6727, L6794-6796). Sete dos nove tipos de infográfico têm só rótulo;
  Checklists e Icon Graphics não têm nem rótulo.
- **13 legendas em GAMMA DESIGN** — os quatro exemplos de botão (L8173-8179),
  os três de complexidade (L8207-8211), os dois de hero (L8253-8255), os dois
  de footer (L8298-8300) e duas frases de abertura de exemplo (L8230, L8272).
  São **âncoras vazias: não sustentam afirmação nenhuma.**
- **8 `**Step 1/2/3**`** — L5480-5484 (calendário com IA), L6779-6783 (prompt de
  copy), L9348-9350 (captação de SMS), fechando `**Results**` (L5486) e
  `**Output**` (L6785). O processo do Email Marketing Brain não é demonstrável.
- O resto: L6811 (a tabela do teste de subject line "resulting in 3x more
  sales"), L9354-9355, L1292-1298, L4170/L9157, L4176/L9163, L5309-5311,
  L9397-9399.

**Os placeholders vazios.** Dois doem mais que os outros porque anunciam
especificação, não exemplo:

- **`**Base Strategy:**` — L3509.** No deck do welcome. A linha seguinte já é o
  próximo heading. Era o diagrama que reconciliaria as duas sequências do
  welcome. Não sobreviveu.
- **`**Segment Definition for 90 Day Winback Flow:**` — L4057.** Anuncia a
  definição de segmento e entrega nada. Existe uma definição de winback em
  L5589, mas está em outro módulo e com outra janela — não é a mesma coisa e
  não deve ser transposta.

**Frases truncadas que levaram número.** A mais custosa: **L8560** —
"that doesn't mean send, You have to emails in 7 days". O teto de frequência do
warming estava nessa frase e se perdeu. Registrado como valor ausente, nunca
como valor estimado.

**Campos de link vazios.** L42 (`link do gamma app :`) e L988
(`Link do gamma :`) — os dois únicos do arquivo. A aula de YouTube Pop-Ups não
tem seção nenhuma no deck.

## Entregue errado — o material promete uma coisa e entrega outra

O caso mais perigoso, porque **não parece lacuna**. Quem lê rápido acha que tem
a resposta. A resposta correta aqui não é recusa: é aviso.

**1. O procedimento de captura de telefone no checkout é o procedimento de
email, colado.** Sob o título `# **Checkout Page SMS Sign Up**` (L9320), dentro
de `# **How To Grow Your SMS List**` (L9318), o subtítulo
`# **Instructions for Post Purchase Opt-Ins**` (L9328) abre quatro passos.

Os quatro passos, **L9330-9333, são byte-idênticos a L1118-1121** — o
procedimento de opt-in de email do módulo de list growth. Verificado com `diff`:
zero diferenças. E os passos dizem, verbatim:

> * To add a sign-up checkbox to your checkout, in the **Marketing options**
>   section, check **Email**.
> * Check **Preselected** so that the **email** marketing sign-up check box is
>   preselected at the checkout by default…

O parágrafo de abertura tem exatamente **uma palavra trocada**: L1113 diz
"sign up someone's **email** for receiving marketing", L9322 diz "sign up
someone's **number**". Só isso. Nenhum dos passos executáveis menciona
telefone. **O corpus não ensina a capturar telefone no checkout** — ele parece
ensinar. Conflito registrado: `sms-instrucoes-de-optin-sao-de-email`.

**2. O upload "para Klaviyo" é demonstrado inteiro no Omnisend.** A seção
**L8009 — "Uploading Designs From Figma To Klaviyo"** lista 5 passos
(L8011-8015) e o passo 4 manda "Upload your sections as images into
**Klaviyo**". A demonstração — L8044 a L8063, ela inteira — é feita no
**Omnisend**. O narrador anuncia a troca em L8044 ("for this video I'm going to
use Omnisend… you get a 30% discount if you use me") e fecha em L8063 com o link
de afiliado. **Não há um único passo executado em Klaviyo.** Toda resposta
derivada daqui sai datada e dizendo qual plataforma foi realmente demonstrada —
é a regra 4 do [[_protocolo]]. Ver [[design/upload-do-design]].

**3. O deck de Optimization repete o deck de Flows.** Três seções aparecem duas
vezes, quase verbatim: *Flow Time Delays* (L4141-4145 ≡ L9176-9180), *SLs and
PTs* (L4153-4162 ≡ L9165-9174) e *Graphic vs Text Based* + *Promoting Categories
vs Products* (L4164-4176 ≡ L9151-9163). A única diferença material é um typo
("Ilusing" em L4160, "Using" em L9172). **Não são duas fontes independentes.**
Nunca tratar a repetição como confirmação cruzada — o módulo mais raso do corpus
parece maior do que é por causa disso.

---

# Assuntos que o corpus NÃO cobre e vão ser perguntados

Derivados do próprio material, não do senso comum. Cada um com a varredura que
prova a ausência.

## Consentimento e compliance de SMS — a lacuna mais grave do corpus

**A varredura.** No arquivo inteiro, 9.544 linhas:

| Termo | Ocorrências |
|---|---|
| `TCPA` | **0** |
| `CTIA` | **0** |
| `10DLC` / `10 DLC` | **0** |
| `short code` / `shortcode` | **0** |
| `toll-free` | **0** |
| `carrier` | 2 — e **as duas são "baby carriers"** (L2076, L2080), copy de exemplo de uma marca. Zero como operadora. |
| `consent` | 5 — e **nenhuma sobre SMS**: L219 e L229 são o narrador citando o índice do glossário, L499 é o cabeçalho `### 🔐 **Compliance & Consent**`, L503 é a definição de GDPR, L1414 é navegação de UI do Klaviyo ("go to settings, list settings, consent"). |

> **Correção de brief.** `consent` e `carrier` **não** têm zero ocorrências, ao
> contrário do que a especificação desta nota supunha. Têm 5 e 2. O que é
> verdade — e é o que importa — é que **nenhuma delas trata de consentimento de
> SMS**. A lacuna se sustenta; a formulação "zero ocorrências" não. Registrado
> aqui para que ninguém a repita como fato.

**O que existe, e é só isto.** Uma seção do glossário, `### 🔐 **Compliance &
Consent**` (L499-507), com sete definições de uma linha — Opt-In, Double Opt-In,
GDPR, CAN-SPAM, CASL, Unsubscribe Link, Preference Center. **Todas de email.**
E a fala que acompanha o glossário descarta a seção explicitamente:

> **L229** — "compliance and consent. **which you really don't, don't need to
> know these**, but if you ever mention it, you can check back to this"

**E mesmo assim o corpus prescreve nos dois sentidos, sem conciliar:**

- **L9324** (slide de SMS): "We want it to be **auto-checked** so someone will
  be added to the list." Checkbox pré-marcado, sobre a captação de telefone.
- **L9461** (slide de SMS, três seções depois): "In an ideal world I would love
  to send multiple cart abandon sms messages, but it's actually **illegal to do
  in the US** lol… so we're only limited to one message."

Ou seja: ele invoca a lei americana para **limitar** a frequência de envio e
ignora a mesma jurisdição ao prescrever consentimento pré-marcado — e não cita
uma única norma em nenhum dos dois casos. Conflito registrado:
`sms-auto-check-e-a-lei`.

**Como responder.** Esta é a única lacuna do corpus em que a recusa deve vir
acompanhada de aviso ativo, e não só do vizinho: o material recomenda uma
prática de consentimento e não cobre o regime que a governa. Entregar o que ele
diz, marcar que ele não fundamenta, e nomear que o corpus não tem TCPA, CTIA,
10DLC, short code nem texto de consentimento. Ver [[sms/setup-e-plataforma]] e
[[sms/crescer-a-lista]].

## Preço de qualquer ferramenta

`pricing` tem **uma** ocorrência (L6001) e é sobre tiers de produto do cliente.
Não há preço de Klaviyo, Omnisend, Alia, Glockapps, Attentive nem Postscript, em
nenhum registro. O mais específico que o corpus chega:

- Klaviyo vs Omnisend: "Omnisend is a solid budget option" (L34, L357-358) —
  "budget option" nunca é definido.
- Alia: "the ROI is worth it every time" (L1243) — afirmação sem número.
- Attentive vs Postscript: "relatively same price" (L9236, L9315).
- Glockapps: existe plano gratuito e plano pago; o corpus não diz o preço nem o
  que o gratuito limita.

Corolário: **não há limiar de tamanho de lista nem de faturamento para escolher
entre plataformas**, e não há instrução de migração. Ver
[[fundamentos/escolha-do-esp]].

## B2B, assinatura e qualquer coisa que não seja DTC de Shopify

`B2B` = **0 ocorrências**. `wholesale` = **0**. Todo o corpus pressupõe
e-commerce direto ao consumidor em Shopify — a integração Shopify é assumida
como dada em segmentação, em flows e no dashboard, e nunca é discutida como
escolha. O público declarado é ainda mais estreito: marcas acima de **$50k/mês**
(L4184, L9259, L9542).

## Mercados fora dos EUA

`Europe`, `European`, `UK`, `Canada`, `Australia`, `Germany`, `Brazil`,
`international` = **0 ocorrências cada**. `timezone` / `time zone` = **0** — e
isso importa, porque [[sms/calendario-e-horarios]] e [[otimizacao/send-time]]
dão horários em absoluto, sem nenhuma palavra sobre fuso do destinatário.
`currency` aparece uma vez e é a variável Klaviyo `currency_format` (L3910).

O diagnóstico de mercado é frontalmente americano — "stimulus checks back in
2020", "we apply that to, like, 2025 where tariffs come into play" (L9);
"Increased Cost Per Acquisition x Lower LTV x **Tariffs** = Lower Profitability"
(L268) — e é apresentado como universal, sem recorte geográfico. Ver
[[fundamentos/estado-do-mercado]].

## Plataformas que não Klaviyo, Omnisend e Shopify

Varredura, ocorrências no arquivo inteiro: `ActiveCampaign` 0 · `Sendlane` 0 ·
`Braze` 0 · `HubSpot` 0 · `Salesforce` 0 · `Drip` 0 · `ConvertKit` 0 ·
`Beehiiv` 0 · `WooCommerce` 0 · `BigCommerce` 0 · `Magento` 0 · `Yotpo` 0 ·
`Recharge` 0 · `Gorgias` 0 · `Triple Whale` 0 · `Northbeam` 0.

As três exceções, todas incidentais:

- **Mailchimp** — 3 menções, nenhuma avaliativa: exemplo dentro da definição de
  ESP no glossário (L459) e origem de migração em dois trechos de warming
  (L8563, L8607). Nunca comparado, nunca julgado.
- **Attentive e Postscript** — nomeados como "the two other main options" para
  SMS e "both are great" (L9236, L9314). Zero walkthrough, zero critério de
  escolha, zero preço.
- **Alia** — tem walkthrough falado e julgamento, mas o material de deck é o
  placeholder `[need]` (L1304).

## Outros canais e disciplinas adjacentes

`WhatsApp` 0 · `push notification` 0 · `direct mail` 0 · `sms deliverability` 0.
`landing page` 2 e `retargeting` 1, ambos de passagem. A analogia com CRO de
site é feita uma vez (L6896) e nunca desenvolvida — ver
[[design/por-que-design-importa]]. **Deliverability de SMS não existe no corpus**,
apesar de o módulo inteiro de deliverability de email existir.

---

# O limite de autoria

**~26% da fala do corpus não é do Max.** São 2.462 linhas, ~25.141 palavras,
distribuídas em cinco faixas ([[_autoria]]):

| Faixa | Módulo | Classificação |
|---|---|---|
| L5617-5866 | Copywriting (ChatGPT) | **`outro-provado`** — L5753 fala de Max em terceira pessoa |
| L4189-5154 | Campaigns (fala inteira) | `outro-provavel` |
| L5867-6248 | Copywriting (infográficos, subject lines) | `outro-provavel` |
| L8365-8646 | Deliverability (fala inteira) | `outro-provavel` |
| L8762-9109 | Optimization (fala inteira) | `outro-provavel` |

**O que isso significa na prática, e o que não significa.**

Não significa que o material seja inválido. Significa exatamente uma coisa: **é
material do curso, não é fala dele.** O curso é dele — ele o compilou, o
entregou e o assina. A doutrina continua utilizável, os números continuam
válidos, as especificações continuam valendo. O que muda é a **forma da
atribuição**: nada dessas faixas pode sair como *"Max diz que…"*, *"na visão
dele…"* ou entre aspas atribuídas a ele. Sai como *"o material do curso diz"*.

Isto **não é uma lacuna** e não gera recusa. É a distinção entre responder e
citar. Se a pergunta é "o que fazer", responda. Se a pergunta é "o que **ele**
acha", entregue o conteúdo marcando que essa parte do curso não é fala dele.

**Onde bate mais forte:** [[deliverability/_index]] (9 de 9 notas),
[[otimizacao/_index]] (7 de 7), [[campanhas/_index]] (8 de 9),
[[copy/_index]] (6 de 9), [[doutrina/_index]] (8 de 13). Somando: os dois
módulos de densidade baixa que mais concentram lacunas são também os dois em
que **nenhuma linha falada é citável como dele**.

**O que não está em causa:** os nove decks GAMMA. São artefato escrito de Max —
carregam a bio assinada (L3419, L9269) e reivindicações em primeira pessoa
(L358, L1208, L5475, L6774, L8311, L9522). Ressalva de [[_autoria]] §7.5: não
dá para distinguir "Max escreveu usando 'nós'" de "a equipe escreveu e Max
assinou", e por isso convém não citar um slide como *"ele disse"* — o deck é
artefato dele, não fala dele.

**E o inverso também vale.** Os quatro módulos sem contaminação nenhuma —
[[design/_index]], [[fundamentos/_index]], [[list-growth/_index]],
[[sms/_index]] — têm cada um ao menos um bloco `max-provado` como âncora
(L7817/L8044 · L34 · L631/L1014 · L9258). Quando a pergunta pedir a voz dele,
estas quatro pastas são o terreno seguro.

---

# Datação

**O corpus não declara data de gravação em lugar nenhum.** Nenhum bloco, nenhum
deck, nenhum marcador. O que existe são âncoras internas.

**A data conhecida mais recente é `Nov 13, 2024, 9:49 AM`** — o carimbo do print
do segmento `WC | Sunset`, no PNG embutido na L9545, lido por ampliação em
[[flows/sunset]]. O dia é incerto entre 13 e 18: o glifo tem 7 px de altura. Não
há nada mais recente no material.

Outras âncoras temporais, todas verificadas:

| Âncora | Linha |
|---|---|
| "People had lots of money from the stimulus checks back in **2020**" | L9 |
| "we apply that to, like, **2025** where tariffs come into play" | L9 |
| "Increased Cost Per Acquisition x Lower LTV x **Tariffs** = Lower Profitability" | L268 (slide) |
| Título do vídeo de SMS: "Everything You Need to Know About SMS Marketing **in 2025**" | L9220 |
| Exemplo de copy: "if you got the new **iphone 16** you're at a 100 plus cases for it" | L2425 |
| "a lot has changed in the e-com world in the **past 5 years**" | L9 |

**O que apodrece, em ordem de velocidade:**

1. **Telas de ferramenta.** Todas as notas `tipo: procedimento` — os dois
   walkthroughs de form no Klaviyo, o dashboard, o Alia, o Figma, o upload
   (que é Omnisend), o Glockapps, o setup de checkout no Shopify. Interface
   muda sem aviso. Toda resposta que dependa de uma tela sai com o carimbo
   **antes** dos passos, nunca depois — regra 4 do [[_protocolo]].
2. **Os links de afiliado.** `omnisend.com/max`, o link Klaviyo com
   `utm_source=001Nu0000022YR4IAM`, `aliapops.com`, `alialearn.com`,
   `wellcopy.net/gpt`, o Skool. Todos descartados como CTA ([[_fontes]]), mas
   registrados aqui porque as **ofertas** que eles prometem ("30% OFF first 3
   months", L358/L8044; "Say Max sent you when you book a call and you'll get a
   gift ;)", L1245) são datadas e podem não existir mais.
3. **O diagnóstico de mercado.** Stimulus checks de 2020, tarifas de 2025, "70
   anúncios por dia" e "250 num estudo", CPM em alta. Nenhum tem fonte, e o
   argumento inteiro é conjuntural e americano. Ver
   [[fundamentos/estado-do-mercado]].
4. **Exemplos ancorados em lançamento.** O iPhone 16 (L2425) como gancho de
   campanha. A copy é boa; a âncora vence.
5. **Números de conta de exemplo.** Os 93.726 perfis e a data do print do
   Sunset são de uma conta de cliente num dia específico. Não são
   especificação e nunca devem ser citados como alvo.

**O que não apodrece:** princípio, framework, estrutura de flow, doutrina de
design, S.C.E., os pilares de conteúdo. Onde a resposta for de julgamento e não
de tela, a datação não muda nada.
