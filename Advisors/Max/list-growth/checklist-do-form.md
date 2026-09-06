---
tipo: especificacao
modulo: list-growth
assunto: checklist-do-popup
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L653-663 (transcrição), L1248-1256 (slide)"
conflitos: [list-growth-time-delay, list-growth-botao-x, list-growth-popup-vs-full-page]
status: rascunho
---

# A especificação

Checklist verbatim do slide, "4. Successful Pop-Up Checklist" (L1250-1256):

> * Only asks for one input per step (ask for email then sms in separate steps)
> * Time delay is 4-12 seconds
> * Form loads instantly after delay with no lag
> * Form covers at least 75% of screen
> * Under 10 words of copy
> * Offer is the largest aspect of the form
> * OPTIONAL: There is no "x" button, rather a "Close Form" button underneath
>   the submit button

# Item a item, com o racional dele

**Um input por passo.** "We don't want to ask for email and SMS on the same
step" (L653). O motivo é carga percebida: quem vê email e telefone juntos pensa
"Oh my gosh, this is so much work. I'm not going to opt in" (L1001). A sequência
correta é pedir email, e só depois, no passo seguinte, o SMS (L655) — ver
[[copy-do-form]].

**Time delay.** Ele proíbe explicitamente valores fora da faixa: "Don't use any
other time delay. I just recommend doing 4 seconds, 12 seconds, 8 seconds, 10
seconds. One of those" (L655). O racional dos dois lados da faixa está no
YouTube: disparar imediato é ruim porque "the customer hasn't even seen your
products" (L1033); esperar 30 ou 40 segundos é ruim porque pouca gente fica
tanto tempo na página (L1034). **Três faixas diferentes no corpus — ver abaixo.**

**Carrega instantâneo.** "a lot of times you'll see pop-up forms that are massive
file sizes, they load slowly, and it just causes issues in the customer
experience" (L657). A contramedida operacional é comprimir a imagem — ver
[[criar-form-no-klaviyo]] (L856).

**≥75% da tela.** "We don't want a tiny, little, puny form. We want a big one.
The bigger ones perform better" (L657-659).

**<10 palavras.** "The less copy we can have, the better" (L659). Exceção
declarada: "on some of the quiz ones, you can get away with a little bit more"
(L659). Na versão do YouTube o princípio é ainda mais duro: "the key to getting
the most amount of optins with your copy on your pop-up form... is cut as much
copy as possible", porque "Every little piece that we add is going to increase
the odds that somebody churns off of this form" (L1036-1037).

**A oferta é o maior elemento visual.** "15% off, big in your face, 10% off right
in your face, that's what we want right there. It's the biggest part, that's all
people care about" (L661).

**Esconder o X.** Marcado OPTIONAL no slide (L1256), mas a fala não trata como
opcional: "Hide that X and just have a no thanks closed form button instead.
Always performs better" (L663). O racional é comportamental: ao ver um pop-up a
pessoa entra em "zombie mode, just go to the top right corner and try to find the
X" (L750); escondendo o X ela é forçada a decidir entre pegar o desconto ou
recusar (L752, L1046-1047). O botão de recusa é obrigatório — "we're going to get
a lot more opt-ins if we don't give people an option. But that's going to be bad
for website conversion rates. We need to give people an option" (L1047). Copy
sugerida em [[copy-do-form]].

# Onde o corpus discorda

**Time delay — três faixas, nenhuma é média das outras:**

| Faixa | Registro | Linha |
|---|---|---|
| 4 a 6 segundos (junto do benchmark de 6-12%) | transcrição | L194 |
| 4 a 12 segundos | transcrição + slide | L655, L820, L1251, L1274 |
| 4 a 8 segundos, tipicamente 6 | transcrição (YouTube) | L1033 |

Ver `list-growth-time-delay`. O único valor que aparece nas três é **4
segundos**, e é o que ele manda usar como ponto de partida (L820: "you can start
off with four and then test from there").

**Botão X.** OPTIONAL no checklist (L661, L1256) contra tratamento obrigatório na
execução (L663, L840, L1046-1049). Ver `list-growth-botao-x`.

**Tamanho.** O checklist pede ≥75% da tela, mas na execução ele recusa o
full-page e escolhe pop-up (L708, L834). Ver `list-growth-popup-vs-full-page`.

# O que o corpus não diz

O checklist não fixa dimensão em pixels — isso só aparece na execução no Klaviyo
(750x500 mobile, 1000x600 desktop; L710, L840). Também não define o que conta
como "instantâneo", nem dá limite de peso de arquivo.
