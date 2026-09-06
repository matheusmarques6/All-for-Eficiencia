---
tipo: procedimento
modulo: deliverability
assunto: upload-para-deliverability
autor: max-sturtevant
registro: [slide, outro-narrador]
fonte: "CONTEUDO BRUTO/max.md — L8492-8504 (transcrição), L8740-8748 (slide)"
validade: "procedimento — o corpus não data a gravação. Extraído em 2026-09-06. Telas do Klaviyo e do iLoveIMG podem ter mudado."
status: rascunho
---


# Aviso de autoria

**Faixa L8381-8646 (toda a fala do módulo de deliverability) — `outro-provavel`.**
Sem prova nominal. A classificação é **estilométrica**: o bloco pertence ao aglomerado
do único bloco `outro-provado` e não traz um só marcador do idioleto de Max.
`outro-provavel` não é `outro-provado` — não está provado que a voz não é dele, está
estabelecido que é muito improvável ([[_autoria]] §7.3).

Critério: **idioleto** ([[_autoria]] §2.1) — ausência de "I recommend", "my favorite"
e "I like to", presença de "at the end of the day" e "obviously", e o fecho coletivo
"thank you guys… see you in the next one". **A saudação de abertura não é critério e
não pode ser citada como evidência:** o laudo testou e ela caiu — o walkthrough de
Figma abre com "Hello, hello" e é comprovadamente Max, que em L7817 digita `@max` e
diz "tags me" ([[_autoria]] §5).

Nesta nota: os 5 passos (L8744-8748) são **slide** — artefato de Max, e continuam
valendo como procedimento. Todo o "porquê" — a definição de slice, os motivos da
compressão, e sobretudo o racional do alt text (L8498-8504) — vem da faixa não-Max
e **não é citável como fala dele**. O walkthrough longo a que o material remete
está no módulo de design (L8009-8065), esse sim `max-provado`.

> **Procedimento datado.** Depende de telas do Klaviyo e de um serviço externo
> de compressão. Avise antes de executar.

# Os 5 passos

Slide, verbatim (L8744-8748):

> * Slice email design into sections and download the sections as JPG or PNG
>   (doesn't really matter)
> * Upload the slices into
>   [https://www.iloveimg.com/compress-image](https://www.iloveimg.com/compress-image)
>   to decrease file size
> * Upload compressed slices into your email platform
> * Add alt text to all of your slices
> * Add a link to all of your slices

A própria narração desvia da seção: "I won't go into this too, too much. Because
there's a much longer and better walkthrough here" (L8490-8492) — o walkthrough
mais longo está no módulo de design, não aqui, e aquele é fala de Max.

# O que a fala acrescenta a cada passo

**Slice.** A definição está só na fala (L8492): "slice is when you take a
section of the email, export it, and then put it into Klaviyo." As fatias saem
do Figma.

**Compressão.** O slide dá só a ferramenta; a fala dá os dois motivos
(L8494) — "Klaviyo does not like huge images" e "it's also going to take forever
for your customers to load". O material chama de "double-edged sword" (L8496). Nenhum
tamanho-alvo em KB ou MB é dado.

**Formato.** JPG ou PNG, "doesn't really matter" (L8744). A fala não toca no
assunto.

**Plataforma.** O slide diz "your email platform" (L8746); a fala diz Klaviyo
(L8492, L8496).

**Alt text.** Onde fica, na fala (L8496): "there's a section in Klaviyo where
after you upload an image, there will be alternative text."

**Link.** "adding links to all your slices as well" (L8496). Nenhum registro
explica por que **todas** as fatias precisam de link.

# O porquê do alt text — só existe na fala

O slide lista `Add alt text to all of your slices` (L8747) e **não dá nenhuma
justificativa**. Essa é a lacuna mais significativa entre os dois registros
nesta nota: quem só tiver o deck não sabe por que o passo existe.

A explicação, na fala (L8498-8500):

> the way that inbox providers work is an email goes to the inbox and Google
> starts to scan it. Now, Google can't properly scan the image-based emails, but
> it can scan any of the alternate text or the text kind of behind it that is in
> the email. And that's what we would call HTML. Google read HTML. Image-based
> emails have a lot less HTML.

O encadeamento é: **Google não lê imagem** → um email 100% imagem oferece pouco
HTML para ler → alt text repõe um mínimo de HTML legível. A fala nomeia os dois
beneficiários (L8502): "for people that can't open the images or for Google to
read".

E generaliza para além do alt text (L8504):

> making sure you're including different bits of HTML in your email will
> [increase] deliverability because it'll show different things that Google
> wouldn't pick up on if it was an image-only email.

*(O ASR grafa "will include deliverability" onde o sentido é* increase*.)*

É o mesmo raciocínio que sustenta a preferência por email text-based durante
warming e reparo — ver [[reparo-de-reputacao]], L8594-8597.

# O que o corpus não diz

- Qual tamanho de arquivo é aceitável. "Too big" e "a large amount of megabytes"
  (L8494) são os únicos parâmetros.
- O que escrever no alt text. Nenhum exemplo, nenhuma regra de conteúdo.
- Para onde os links das fatias devem apontar.
- Quanto HTML é "a base amount" (L8502).
- Se o processo muda para email text-based, que por definição não tem fatias.
- O material promete "a more in-depth video just talking about the importance
  there" (L8504) — não está nesta faixa do corpus.
