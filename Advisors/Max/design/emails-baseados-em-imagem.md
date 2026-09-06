---
tipo: principio
modulo: design
assunto: email-de-imagem
autor: max-sturtevant
registro: [transcricao]
fonte: "CONTEUDO BRUTO/max.md — L8022-8032 (transcrição do vídeo de upload)"
conflitos: [design-html-vs-imagem]
status: rascunho
---

# O que é

A posição que sustenta todo o módulo de design: desenhar o email fora da
plataforma de envio e subir como imagem fatiada. É contra o consenso, e ele sabe
disso — a passagem é escrita como refutação.

# Contra o rumor

A refutação citada abaixo **não é fala de Max**: vem do módulo de deliverability
(L8381-8646), classificado `outro-provavel` por [[_autoria]] — outro narrador, por
estilometria, sem prova nominal. A nota é de Max (o núcleo sai de L8022-8032,
faixa `max-provado`); só esta citação é importada de faixa não-Max e entra como
material do curso, não como fala dele.

> There's some rumor in the space, someone started it like 8 years ago, and maybe
> it had some truth then that you need to have like HTML sections in your email.
> You need to have native text sections and whatnot. But that couldn't be farther
> from the truth. (L8026, verbatim)

Duas concessões dentro da própria refutação: o rumor tem ~8 anos e "maybe it had
some truth then". A negação é sobre hoje, não sobre a origem.

# A prova que ele apresenta

**Ridge.** É a única marca citada nominalmente como evidência:

> You go to a brand like Ridge who does hundreds of millions of dollars and
> they're doing millions from their email channel... That is an image. That is an
> image right there. They are using fully image slice based email. (L8026-8027)

O método de verificação que ele demonstra é o teste do cursor: o que dá para
selecionar com o mouse é HTML nativo, o que não dá é imagem — "I can highlight
it, but I can't highlight this. This is an image and I could literally save this
as an image if I wanted to" (L8027-8028).

E o argumento de autoridade por trás: "if these top brands and the fastest
growing brands in the space are doing image based emails, you can too"
(L8027).

# Por que desenhar fora

> you design emails on another platform. So you have a lot more capability on the
> design front and conversion rate optimization and just have more freedom with
> your emails. So we don't really want to just build emails into our sending
> platform. (L8023)

E a leitura de mercado que ele usa como aval:

> If you look at all of the top brands who are absolutely crushing and they're
> not stuck in the old ways, the brands that are growing fast in 2025, 2026, they
> are using image-based emails. (L8025)

# O risco, e é o único que ele admite

Email de imagem quebra por peso, não por HTML. Um slice único do email inteiro dá
"5 10 megabytes"; nesse tamanho o cliente abre e vê branco enquanto carrega
(L8031-8032). A mitigação é o fatiamento e a compressão — ver
[[upload-do-design]].

# Onde o corpus discorda de si mesmo

Fora do módulo de design, no de deliverability, ele qualifica a mesma posição em
sentido oposto:

> Google can't properly scan the image-based emails... Image-based emails have a
> lot less HTML. However, if you at least have a base amount of HTML for people
> that can't open the images or for Google to read, that's where your alt text
> comes into play... making sure you're including different bits of HTML in your
> email will include [improve] deliverability because it'll show different things
> that Google wouldn't pick up on if it was an image-only email. (L8500-8504)

Ou seja: "você não precisa de seções de texto nativo" (L8026, fala de Max) convive
com "algum HTML no email melhora a deliverability" (L8504, **outro-narrador**). O
alt text é a ponte oferecida entre as duas — e é por isso que virou passo
obrigatório do upload (L8052-8053), esse sim narrado por Max. → `design-html-vs-imagem`. A nota dona desse trecho está em
[[deliverability/_index]].

# O que o corpus não diz

Quanto HTML é "a base amount". Nenhum piso, nenhuma proporção imagem/texto para
email gráfico. Não confunda com a proporção 4:1 de graphic para plain text que
aparece no módulo de copy (L5174) — aquilo é sobre **tipos de campanha**, não
sobre a composição interna de um email.
