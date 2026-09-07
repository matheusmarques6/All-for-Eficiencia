---
tipo: procedimento
modulo: list-growth
assunto: montar-popup-no-klaviyo-mobile
autor: max-sturtevant
registro: [transcricao]
fonte: "CONTEUDO BRUTO/max.md — L684-824 (transcrição)"
conflitos: [list-growth-time-delay, list-growth-exit-intent, list-growth-teaser, list-growth-imagem-lateral, list-growth-popup-vs-full-page]
status: aprovado
---

> **PROCEDIMENTO DATADO.** Gravação de tela do Klaviyo. Nomes de menu, posições
> de botão e defaults de template mudam sem aviso. Trate os **valores**
> (dimensão, delay, frequência) como a doutrina e os **cliques** como
> aproximação.

Esta nota cobre o form **mobile**. O desktop está em
[[criar-form-no-klaviyo-desktop]].

# A regra que precede tudo

**Um form para mobile e outro para desktop, sempre.** "I always recommend just
creating separate forms for each, it's going to be easier to analyze the data"
(L690); "the mobile form has to be completely different to our desktop form"
(L1032).

# Montagem

**Base.** Começar de template, mas "You don't want to take these as is"
(L684-686). Ele abre o *multi-step email and SMS full page form* (L686) e escolhe
a lista de newsletter e a de SMS na criação (L686-688).

**Dispositivo.** Targeting and behavior → display on mobile only (L690-692).

**Estilo e dimensão.** Tipos disponíveis: pop-up, full page, flyout, embed —
"pretty much the same except for how they come in" (L706). Ele fica no **pop-up**
(L708). Dimensão: **750x500** (L710).

**Imagem lateral no mobile: não.** "side image kind of messes up the sizing... it
changes the formatting for whatever reason on mobile" (L712); a saída é deixar a
imagem em *show on desktop only* (L714-716).

**Copy e hierarquia.** Apagar tudo que não é a oferta — "The more copy you add...
it's going to increase churn, it's going to scare people off" (L724-726). Logo
pequeno no topo (L736-738). A oferta cresce até dominar: ele sobe o número de 25
para 45, 55 e **60**, com 35 no resto do texto (L732-742), e usa padding (50
abaixo do logo, 30 no fim) para centralizar (L746, L768).

**Esconder o X.** Opacidade a zero — "it's pretty much a hidden X. You can't see
it" (L752-754). Em troca, um botão próprio de saída embaixo do submit: *no
thanks*, fundo transparente, texto preto (L756-764). O submit vira *Claim 10%
off* (L760). Ver [[copy-do-form]].

**Micro-commit (opcional).** Clonar o passo de email para herdar a formatação,
renomear, arrastar para primeiro, apagar o campo de email e trocar a pergunta
para *Do you want 10% off your first order?* (L776-780). Ação do botão: **Show
next step** (L782). "if you don't want the microcommit, you can just delete
this... It's a great first test to do" (L816).

**Passo de SMS.** Clonar, renomear, trocar o input por phone number (L786-788). O
aviso legal é obrigatório mas encolhe: "you have to put this for to be legal...
let's just make it like size eight" (L790). Copy: *Almost there. Claim 10% off
below.* (L792-800).

**Sucesso.** *Thanks for signing up* + instrução de conferir o dispositivo, e um
botão **close form** (*start shopping*) — porque com o X invisível a pessoa fica
presa sem ele (L806-812).

# Disparo e frequência

| Opção (targeting and behavior) | Veredito |
|---|---|
| Show immediately | "which I don't recommend" (L818) |
| Exit intent | "I don't recommend. Exit intent isn't very good... sometimes it'll misfire" (L818-820) |
| **After time delay** | **recomendado — "something between 4 to 12 seconds, you can start off with four"** (L820) |
| After scroll / after N pages | citadas, sem recomendação (L820) |

Reexibição depois de fechado: **5 dias** (L822). Devices: mobile only (L822).

**Teaser** — o lembrete que reaparece depois do form fechado. "Typically, I don't
use these because they can get in the way of a customer shopping" (L700); ele
deleta o do template (L702).

# Onde o corpus discorda

Time delay (três faixas: L194, L655/L820, L1033), exit intent (aqui rejeitado sem
ressalva; em L1035 o problema é só no mobile), teaser (aqui não usa; em L1073 usa
no desktop) e imagem lateral (aqui atrapalha; testada e vencedora à direita em
L852). Ver `_conflitos` e [[checklist-do-form]].

# O que o corpus não diz

Não diz o que fazer quando o SMS está fora do Klaviyo além de "reach out to that
different platform and see how you can get it onto a Klaviyo form" (L694). Não
define single vs double opt-in aqui, nem valores de padding fora dos exemplos,
nem o que o teaser deve dizer.
