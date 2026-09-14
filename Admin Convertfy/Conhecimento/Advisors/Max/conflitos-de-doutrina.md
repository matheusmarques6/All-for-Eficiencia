---
tipo: indice
modulo: doutrina
assunto: conflitos-doutrina
autor: max-sturtevant
conflitos: [doutrina-narrador-da-aula-de-ia, doutrina-ia-primeiro-rascunho, doutrina-formato-do-slice, doutrina-receita-da-agencia, doutrina-lista-de-marcas]
status: aprovado
---

Registro dos conflitos do módulo `doutrina` do corpus de Max Sturtevant: quem narra a aula de IA, o papel da IA como primeiro rascunho, o formato do slice, a receita que a agência declara e a grafia da lista de marcas atendidas. Cada entrada lista os valores divergentes por registro e fecha com um "Como responder".


`doutrina-segundos-de-atencao` está em [[conflitos-entre-modulos-html-imagem-e-janela-de-atencao]].


## doutrina-narrador-da-aula-de-ia

O corpus tem pelo menos dois narradores. Absorve `copy-narrador-nao-e-max`.
É o único tipo de erro deste corpus que é invisível na saída.

**A prova** (transcrição `# File-ChatGPT Copywriting`, L5667-5865):

| Valor | Registro | Linha |
|---|---|---|
| "something that **Max had put together himself**" — terceira pessoa | **outro-narrador** | L5753 |
| "this is the exact template that **our copywriters** use" | **outro-narrador** | L5799-5801 |
| "the prompt that **we** use internally" | **outro-narrador** | L5707 |
| "Lucky for you, **I've created** the Email Marketing Brain" — primeira pessoa | slide | L6774 |

**A assinatura de abertura caiu como critério.** A tabela que ficava aqui separava
os narradores por "Hello, hello" / "Yo, yo" e listava **L7603** entre os do outro
narrador. [[mapa-da-autoria]] §5 provou o contrário: L7603 abre o walkthrough de Figma
com "Hello, hello" e é comprovadamente Max — em **L7817** ele digita `@max` e diz
"Let me just make sure it actually **tags me**". O pronome coletivo também caiu:
"our copywriters" está no deck escrito de Max (L6790) e "message our team" em
L8692.

O critério que sobreviveu é o **idioleto** ([[mapa-da-autoria]] §2.1): ausência de "I
recommend" / "my favorite" / "I like to", presença de "at the end of the day" e
"obviously", mais o fecho coletivo "thank you guys… see you in the next one".

| Faixa falada | Classificação | Vídeo |
|---|---|---|
| L5667-5866 | **`outro-provado`** | ChatGPT Copywriting — prova nominal em L5753 |
| L4202-4421 · L4444-4675 · L4686-4828 · L4846-5154 | `outro-provavel` | os quatro vídeos de Campaigns |
| L5888-6082 · L6101-6248 | `outro-provavel` | Infographics · Subject Lines |
| L8381-8646 | `outro-provavel` | Deliverability |
| L8773-9109 | `outro-provavel` | Optimization |

Fechos do segundo narrador: "So thank you very much for giving this a watch. See
you later." (L4827), "Thank you guys for giving it a watch and see you in the next
one." (L5865), "feel free to hit us up if you have any questions that we can
clarify." (L9108).

**Como responder:** só L5667-5866 tem prova nominal (`outro-provado`). As outras
nove faixas são `outro-provavel`: inferência **estilométrica**, forte e auditável,
mas não prova — não está provado que a voz não é dele ([[mapa-da-autoria]] §7.3). O laudo
bloco a bloco está em [[mapa-da-autoria]]. A regra prática:

1. Nada de L5667-5865 é citável como fala do Max. `registro: outro-narrador`.
2. Trechos dos outros oito vídeos: citar como "o material do curso diz", não "o
   Max diz", e dizer por quê se perguntarem.
3. **O deck GAMMA é artefato escrito dele** e não carrega o problema — carrega a
   bio assinada (L3419, L9269: "I'm Max. I'm the founder of Well Copy") e
   reivindicações em 1ª pessoa (L6774, L1208, L8311, L9522). Onde a doutrina tem
   slide, ela se sustenta.
4. Onde o Max corrobora em vídeo próprio, a atribuição volta a ser segura — é o
   caso de desconto (L6261), texto puro (L5230) e skimmability (L7163).

**Cobertura deste arquivo — feita.** Uma passagem posterior varreu as notas de controle
entrada por entrada: toda linha de tabela cuja âncora cai numa das faixas acima passou a
levar **`outro-narrador`** na coluna Registro, e as atribuições em prosa ("ele diz", "o
critério dele", "ele mesmo") sobre essas faixas foram reescritas para o material do
curso. Onde uma entrada compara duas versões e só uma é não-Max, a marca é só naquela
versão. Ainda assim, **antes de citar qualquer conflito como fala de Max, confira a linha
contra a tabela de faixas acima** — a marca é auxílio, a tabela é o critério.

Consequência para este registro: onde um lado de um conflito cai num bloco
`outro-provavel`, a entrada avisa. Isso decide pelo menos um conflito —
`otimizacao-peso-do-basico` — e muda a natureza de outro,
`doutrina-ia-primeiro-rascunho`.


## doutrina-ia-primeiro-rascunho

Absorve `copy-papel-da-ia`.

| Valor | Registro | Linha |
|---|---|---|
| "hiring a junior copywriter. And you can get the first draft" | outro-narrador | L5691-5693 |
| "the intention isn't to give you the finished product, is to be used as a guide, a framework" | outro-narrador | L5689-5691 |
| "use it as a framework builder, not a first draft machine" | outro-narrador | L5855 |
| "junior copywriting assistant. Great for brainstorming… skeleton drafts" | outro-narrador | L5845 |
| "ChatGPT isn't going to give you the finished product for your copy. Rather, you should use it as a guide and as a framework." | slide | L6733-6735 |
| "I'm literally just going to have chat GPT like do this all for me or at least help me create like the whole outline of this email" | transcricao (Feastables) | L6399 |
| pede e usa headline, sub-headline, body copy, bullets e subject line gerados | transcricao (walkthrough) | L6386-6411 |
| usa a IA só para dois períodos de body copy, depois do layout pronto | transcricao (Gymshark) | L6274-6276 |

**Como responder:** desde `doutrina-narrador-da-aula-de-ia`, este conflito mudou de
natureza. **Não é o Max se contradizendo** — a regra (L5689-5691, L5855) está
dentro do bloco provado de outro narrador; a prática (L6386-6411) é dele, em bloco
`max-provado`. E a regra se contradiz sozinha: L5691-5695 prescreve "you can get
the first draft" e L5855 proíbe "first draft machine", mesmo vídeo, 164 linhas de
distância. O slide (L6733-6735) é dele e sustenta a versão fraca ("guide and
framework"), não a proibição.

A leitura mais fiel: a regra sobrevive na **iteração e na edição**, não na origem do
texto. Nos dois walkthroughs ele nunca publica saída direta — descarta metade
(L6394), pede variações (L6393, L6405), costura os pedaços à mão (L6397). O que a
prática contradiz é a proibição do primeiro rascunho, não a exigência de reescrita.
Diga as duas coisas; não escolha. A aula de ChatGPT também data a própria posição: "with
where we're currently at" (L5683-5685), prevendo que a regra deixa de valer — **mas essa
datação é do outro narrador** (L5667-5866, `outro-provado`), não de Max.


## doutrina-formato-do-slice

| Valor | Registro | Linha |
|---|---|---|
| "for the type of file I like to do a JPEG you can do whatever you want really" | transcricao (Gymshark) | L6337 |
| "we're going to save them as image slices as PGs" | transcricao (Calvin Klein) | L6489 |
| "You can do a PNG or a JPEG. Honestly, it really doesn't matter." | transcricao (upload) | L8035 |
| "export everything to XPNG. Export eight layers." | transcricao (upload) | L8040 |

**Como responder:** ele declara explicitamente que tanto faz (L8035) e demonstra
JPEG num vídeo e PNG noutro. Não há especificação a defender. O que é constante nos
três é o **2x na exportação** (L6337, L6489, L8034) e o teto de altura de ~800
(L6489, L8033) — esses sim são a regra. "PGs" em L6489 é ruído de ASR; não deduzir
se ele disse PNG ou JPEG ali. Ver `design-altura-do-slice`.


## doutrina-receita-da-agencia

Absorve `flows-receita-da-agencia`. **Três valores de credencial.**

| Valor | Registro | Linha |
|---|---|---|
| "coming from a $40 million email marketer" | transcricao (Gymshark) | L6260 |
| "which has generated $40 million for clients in the past few years" | transcricao (Gymshark) | L6350 |
| "I've made $100 million making emails for e-commerce brands" | transcricao (Calvin Klein) | L6359 |
| "over $100M in email attributed revenue for clients" | slide (deck de flows) | L3419 |
| "an email marketer who has generated $200M for brands in their platform" | slide (deck de flows) | L3428 |
| credencial de "$200 million" em 1ª pessoa | transcricao (masterclass YT) | L5204 |

**Como responder:** $40M, $100M e $200M, em vídeos e decks diferentes, sempre como
credencial de abertura. Os dois números do deck de flows estão a nove linhas de
distância um do outro, sem reconciliação — e o de $200M aparece dentro de um bloco
de recomendação paga do Klaviyo (L3426-3429). O corpus não datou os vídeos, então
não dá para dizer se é crescimento ou inconsistência. Nenhum é auditável. Se a
credencial for citada, cite todas com a linha, ou não cite nenhuma — **nunca
escolha a maior**.


## doutrina-lista-de-marcas

Absorve `design-nomes-de-marca`.

| Marca | Fala | Slide |
|---|---|---|
| Brez / Breeze | "Breeze" (L8003) | "Brez" (L8347) |
| Munk Pack | "Monk Pack" (L8003) | "Munk pack" (L8339) |
| Bite / Byte | "Byte" (L7881-7885), "Bite" (L8003) | "Bite" (L8348) |

**Como responder:** grafia de nome próprio em transcrição de áudio não é confiável.
Vale a grafia do slide, que é texto escrito — é especificação, alguém vai buscar a
marca. A lista canônica é: Casely, Munk pack, Kizik, Duck Camp, Magic Mind, Magic
Spoon, Olipop, Dr. Squatch, Seed, Brez, Bite (L8338-8348) — as mesmas 11 marcas na
mesma ordem nos dois registros. "Breeze" aparece também no módulo de copy (L5189)
como nome de produto numa peça de exemplo.

---


