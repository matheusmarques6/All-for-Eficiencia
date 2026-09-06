---
tipo: procedimento
modulo: design
assunto: upload-do-design
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L8009-8063 (slide + transcrição do vídeo), L8740-8748 (segunda versão do slide, módulo deliverability)"
conflitos: [design-klaviyo-vs-omnisend, design-altura-do-slice, design-passos-do-upload]
status: rascunho
---

> **Procedimento datado.** Extraído do corpus em 2026-09-06. Depende de telas de
> Figma, iloveimg e de uma plataforma de envio — qualquer uma delas pode ter
> mudado. Avise antes de aplicar.

# Leia isto antes de qualquer passo

A seção do curso se chama **"Uploading Designs From Figma To Klaviyo"** (L8009) e
o passo 4 do slide diz "Upload your sections as images into **Klaviyo**"
(L8014). **Nenhum passo é demonstrado no Klaviyo.** O vídeo inteiro é feito no
**Omnisend** (L8044), com link de afiliado e 30% de desconto declarados duas
vezes (L8044, L8063). O próprio título do vídeo é neutro: "How to Upload Email
Designs Properly into ANY Email Sending Platform" (L8019). A segunda versão do
slide, no módulo de deliverability, diz "your email platform" (L8746) — e mesmo
assim mantém "Klaviyo" no título (L8742).

Conclusão prática: os passos 1-3 são de Figma e iloveimg e valem sem ressalva. Os
passos 4-5 descrevem a interface do Omnisend. → `design-klaviyo-vs-omnisend`

# Os 5 passos (slide, verbatim)

> 1. Slice your emails into different sections using Figma's slice tool
> 2. Save your sections as images
> 3. Compress your images using a site like https://www.iloveimg.com/compress-image
> 4. Upload your sections as images into Klaviyo
> 5. Add your links and alt texts :) (L8011-8015)

A segunda versão (L8744-8748) separa alt text e link em dois passos e troca
Klaviyo por "your email platform". → `design-passos-do-upload`

# Regras de tamanho

| Regra | Valor verbatim | Linha |
|---|---|---|
| Altura máxima do slice | "try not to go over kind of like 800ish or so" | L8033 |
| Altura recomendada | "I'd probably maybe go to like 720 right here" | L8033 |
| Altura esticada, na prática | "maybe I can extend this and kind of like push it to like the thousand" | L8036 |
| Largura do slice | "make sure it's 600 width and it's perfectly lined up with this email" | L8034 |
| Qualidade de export | "I like to export on 2x quality just to make sure that we don't sacrifice quality" | L8034 |
| Formato | "You can do a PNG or a JPEG. Honestly, it really doesn't matter." | L8035 |

800 e 720 saem na mesma frase, e mil aparece duas falas depois quando o link é o
mesmo ao longo do trecho. → `design-altura-do-slice`

# A regra que governa o corte

Um slice por área de link distinto:

> when we're doing these image slices, we can't just have an image slice that
> captures all of this because these have different buttons. So, if we upload
> this image into our sending platform, we put links on our images... And these
> have different links. And so, we need to have different slices for different
> areas of our email that are going to have different links. (L8036-8037)

Corolário dele: se o link é o mesmo, dá para esticar o slice (L8036). Se muda,
corta. Onde não há botão, "Doesn't need to be absolutely perfect" (L8038).

# Compressão

O caso concreto do vídeo: o email inteiro saiu de **3.98 megabytes** e ficou em
**963 kilobytes** — "77% smaller" — com a qualidade avaliada como igual
(L8042-8043). Ele exportou oito camadas nesse email (L8040).

Motivo, e é o único de peso técnico do módulo: um slice único do email inteiro dá
"5 10 megabytes"; com arquivo desse tamanho o cliente abre e vê tela em branco
enquanto carrega, principalmente com Wi-Fi ruim (L8031-8032). Fatiar faz o email
carregar de cima para baixo, parte por parte.

# Padding

Remover **todo** o padding, nos dois lugares onde ele aparece:

- na seção/coluna, "just remove all the padding so that the image goes across the
  whole entire email" (L8049);
- na imagem, senão sobra faixa branca entre as imagens (L8051).

# Links e alt text

> Every single image, you need to have a link. Make sure you always have a link
> for every single image. (L8056, verbatim)

Alt text em todas as imagens. O motivo declarado: aparece se a imagem não
carregar ou se a pessoa bloqueou imagens — "which not many people do" — e "it
helps with some deliverability" (L8052-8053). O exemplo dele é curto: "Welcome to
Calvin Klein. take 10% off with code..." e depois só o destino de cada botão —
shop best sellers, shop underwear, shop woman, shop men, shop kids
(L8054-8055). "You really don't need to do much here" (L8054).

# Fecho

Rodapé com preferences/unsubscribe entra por bloco pronto da plataforma, que
autopopula com os dados da marca (L8059-8060). Antes de enviar: preview em
celular e tablet, teste de todos os links, e opcionalmente um test email
(L8061-8062).

Ver [[emails-baseados-em-imagem]] para a posição doutrinária por trás disso, e
[[figma-para-email]] para o slice tool.
