---
tipo: procedimento
modulo: design
assunto: figma-para-email
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L7590-7840 (transcrição), L8350-8355 (slide)"
conflitos: [design-plugins-do-figma]
status: aprovado
---

> **Procedimento datado.** Extraído do corpus em 2026-09-06. É um passeio ao vivo
> pela interface do Figma; menus e nomes podem ter mudado. Avise antes de aplicar.

# O que é

O vídeo é declaradamente introdutório e ele mesmo relativiza: "you're just way
better off just exploring yourself and messing around inside of the platform"
(L7605-7607). O que importa aqui é a hierarquia de arquivo e o slice — o resto é
tour.

# A hierarquia obrigatória

É a única regra estrutural do vídeo:

> typically when we're talking about email design, we're going to be using a
> frame as a singular design. So your designs are going to be frames, whereas you
> have groups within your frames. So you have groups within your emails, which is
> frame. (L7707-7711, verbatim)

| Nível | O que é | Linha |
|---|---|---|
| Frame | um email inteiro. "kind of frame is like a level up from a group" | L7699-7709 |
| Group | uma seção do email ("logo section", "copy section") | L7689-7705, L7733, L7769 |
| Layer | cada elemento; aparece na coluna da esquerda | L7619-7635 |

Agrupar: shift + clique esquerdo, e escolher group ou frame (L7693-7697).

# Dimensões

> typically for your emails, you want it to be 600 width (L7713-7715)

600 de largura é a única medida declarada como regra. A altura do exemplo — "let's
make it like 800 tall" (L7717) — é do exercício, não regra; a mesma ordem de
grandeza reaparece como teto de slice no upload (L8033). Ver [[upload-do-design]].

O fundo do email é o **fill do frame**: "you want a specific background for your
emails. So you can add a fill to your frame and have this be like the background"
(L7723-7725).

Imagem entra por **file > place image** (L7737-7739); depois é redimensionar
(proporções travadas pelo cadeado, L7645-7651) e arrastar para dentro do frame
(L7749-7751).

# O slice tool

O único recurso do vídeo que existe por causa do processo de envio:

> what a slice does is you can slice anything you want and essentially just be
> able to export just a slice... And that's how we are going to be uploading
> emails. (L7805-7811)

Os parâmetros de uso (largura 600, altura, export 2x) estão em
[[upload-do-design]], não aqui.

# O escopo real que ele declara usar

> The main stuff you're going to be using is creating your frames, adding in
> shapes, adding in a ton of photos and all of that good stuff. (L7825-7827)

E antes: "That's really the extent of what you use in Figma" (L7771-7773). Retângulo é
a forma padrão: "More often than not, you will be using something like a
rectangle" (L7625).

# O que ele diz que quase não usa

| Recurso | O que ele diz | Linha |
|---|---|---|
| Effects (shadow, layer blur, background blur, inner shadow) | "A lot of this stuff is advanced and you really won't really use it" | L7671-7681 |
| Ajuste de layers / filtros | "I rarely use that and I create emails all day, every day" | L7683-7687 |
| Widgets e alignment | "again, I don't even really use those" | L7799-7803 |
| Sections (o recurso do Figma) | "which are a little bit different, but we don't even really use them" | L7787 |
| Edição de foto | "You can change your photos. We don't need that" | L7827-7829 |

Ele usa alguns **plugins**, e nomeia a função, não o nome: criar GIFs, screenshots
to designs (L7795-7799).

# Onde o corpus discorda

O slide vende o Figma por três motivos, e o segundo é justamente o que a fala
minimiza:

> Figma is the best design platform for email on the market for a few reasons.
> Mainly around your design capabilities, use of Figma app plug-ins, and your
> file organization. (L8354, verbatim)

Plug-ins aparecem como razão principal no deck; na fala são uma menção de
passagem e widgets são descartados (L7799-7803). → `design-plugins-do-figma`

O slide também remete o aprendizado para fora do corpus:
https://designlab.com/figma-101-course/introduction-to-figma (L8355).

# O que o corpus não diz

Nada sobre biblioteca de componentes, auto layout, estilos de texto, variáveis ou
templates reutilizáveis. Os valores de tipografia que ele digita — sub-headline
24 bold, body copy 18 (L7757-7765) — são da demonstração, **não são regra**.

Recursos de arquivo cobertos de passagem: comentário com menção, resolver
comentário, share (L7815-7823). Os arquivos de swipe/template que ele linka
(Pop-Up Swipe File, DWY Campaigns, DWY Flows) estão em L7594-7598.
