---
tipo: principio
modulo: copy
assunto: email-architect
autor: max-sturtevant
registro: [slide, outro-narrador]
fonte: "CONTEUDO BRUTO/max.md — L5725-5735 e L5803-5833 (transcrição, outro narrador), L6787-6792 (slide)"
conflitos: [copy-narrador-nao-e-max]
status: rascunho
---


# Aviso de autoria

**Faixa L5667-5866 (ChatGPT Copywriting) — `outro-provado`.**
**Prova nominal — a única do corpus.** Em L5753 o narrador fala de Max em terceira
pessoa: "So we have a email marketing brain, something that **Max had put together
himself**". Não é inferência estilométrica: é o falante se distinguindo de Max.
Ressalva registrada no laudo — L5753 vem de ASR ([[_autoria]] §4.1).

Critério: **idioleto** ([[_autoria]] §2.1) — ausência de "I recommend", "my favorite"
e "I like to", presença de "at the end of the day" e "obviously", e o fecho coletivo
"thank you guys… see you in the next one". **A saudação de abertura não é critério e
não pode ser citada como evidência:** o laudo testou e ela caiu — o walkthrough de
Figma abre com "Hello, hello" e é comprovadamente Max, que em L7817 digita `@max` e
diz "tags me" ([[_autoria]] §5).

Nesta nota: o diagnóstico, a regra e a evidência de resultado existem **também no
slide** (L6787-6792), artefato escrito de Max — e continuam citáveis por ali. Tudo
que sai de L5725-5735 e L5803-5833 é fala do outro narrador: o mecanismo do
descontrole de design, o mapeamento campo a campo, o Bridge Section como
infográfico e o "80% dos emails" **não são citáveis como fala de Max**. É o caso
particular registrado no laudo ([[_autoria]] §6.1): o conceito é dele, está no
deck; a formulação falada não.

# O problema que isso resolve

Copy entregue como tabela pura de campos produz design que não corresponde à
intenção do email. O diagnóstico, no slide:

> "We notice a lot of disconnect between copy and the design when we just write
> copy in table format." (L6789)

Na fala do outro narrador, com o mecanismo: "it takes a lot more direction when you're simply
putting things into a table. So something that's just listed as header or
subject line, preview text, header, subheader, CTA, because you're not really
giving any direction" (L5807-5811). O resultado observado: "the designers would
be really all over the place because they'd get a bunch of copy. And then the
designs would be, you know, X, Y, and Z and not at all with the original intent
of the email was" (L5811-5815).

O ponto é sutil e vale isolar: o problema **não** é a lista de campos. É a lista
de campos **sem indicação de aparência**. O designer recebe texto e nenhuma
instrução do que aquele texto deve virar.

# A regra

> "Instead, our copywriters act as 'Email Architects' and map out exactly how
> the email should look like. This gives copy more control over the finished
> design product as well as giving the design direction." (L6790-6791)

Na fala: "made our copywriters essentially the email architects, mapping out
exactly how the email should look. Gives… the copy a lot more control over the
finished product" (L5817-5819).

A troca é explícita — e essa formulação está no slide, logo é de Max: o
copywriter assume responsabilidade de layout e, em troca, ganha controle sobre o
produto final. Não é ampliação de escopo por
zelo — é quem decide a aparência passando a ser quem decide a mensagem.

# A evidência que ele oferece

> "Our final products became noticeably better when we started formatting
> things this way." (L6792)

Na fala, mais forte: "things just came exponentially better once we started
using it along these lines" (L5821). Não há número, teste ou período — é
julgamento de resultado, não medição.

# O esqueleto

Os oito campos, na ordem, são os mesmos de [[prompt-de-copy]]: Subject Line,
Preview Text, Headline, Subheadline, First CTA, Body Copy, Bridge Section,
Product Section.

> "Kind of the skeleton that I'd say 80% of emails followed to some extent.
> Obviously things will move around, but at the end of the day, these are at
> least the basics you're looking for. It can always add takeaway depending on
> what you got." (L5731-5735)

Três coisas ficam declaradas aí, e as três importam:

- **80%**, não 100%. É o padrão, não a regra.
- **"things will move around"** — a ordem é ponto de partida.
- **"can always add takeaway"** — o esqueleto é extensível; takeaway é o campo
  extra nomeado.

# Como o esqueleto conversa com o resto do módulo

A fala mapeia campo a campo (L5821-5833):

- headline + subheadline + CTA = "the most generic and most commonly used hero
  section" (L5823-5825);
- **Bridge Section = infográfico**. É onde entra o gráfico side-by-side myth
  versus fact, ou "more of a table layout, just outlining the reviews, average
  rating, five star reviews" (L5827-5831). Ver [[infograficos]];
- e o fecho amarra tudo no S.C.E.: "All the stuff we covered, talking about the
  infographics, keeping it skimmable, clear and concise, engaging" (L5831-5833).

O Bridge Section é o campo mais informativo do esqueleto: é o único que existe
para não ser texto.

# O que o corpus não diz

- **Não há um único exemplo do formato.** O slide tem só os rótulos "Example
  \#1" e "Example \#2" (L6794-6796), sem imagem. A fala descreve uma tela que
  não está no texto.
- Não há especificação do artefato: se é documento, Figma, tabela anotada ou
  wireframe. "Map out exactly how the email should look" nunca é definido em
  forma.
- Não há regra de quando os campos podem "move around", nem quais são
  obrigatórios dentro dos 80%.

# Ver também

[[prompt-de-copy]] · [[infograficos]] · [[design/_index]] ·
[[doutrina/o-processo-de-criacao]]
