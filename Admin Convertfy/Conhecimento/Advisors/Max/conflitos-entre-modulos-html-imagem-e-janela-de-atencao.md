---
tipo: indice
assunto: conflitos-entre-modulos-html-imagem-e-janela-de-atencao
autor: max-sturtevant
status: aprovado
---

Os conflitos do corpus Max que atravessam pastas e envolvem a construção do email: design diz que não é preciso HTML nativo e deliverability diz que algum HTML ajuda o Google a ler (`design-html-vs-imagem`), e a janela de atenção do leitor tem três valores diferentes por módulo — 3 segundos, 2-3 e 2-4 (`doutrina-segundos-de-atencao`).

# Conflitos entre módulos — HTML contra imagem e a janela de atenção


Os que atravessam pastas. São os mais perigosos porque o roteamento do [[mapa-do-corpus-do-max]]
manda ler **uma** pasta: quem entra por `design/` nunca vê a versão de
`deliverability/`. Toda entrada aqui tem que ser lida antes de responder na pasta de
origem.

## design-html-vs-imagem

design (L8026) contra deliverability (L8500-8504). **As duas falas não têm o mesmo
dono:** L8026-8028 está no walkthrough de upload (L8009-8065), `max-provado`; já
L8500-8504 está em L8381-8646, `outro-provavel` por [[mapa-da-autoria]] — **não é fala de
Max**. O conflito continua de pé como conflito do *corpus*, mas um dos lados não é
citável como fala dele.

| Versão | Valor | Registro | Linha |
|---|---|---|---|
| Não precisa de HTML nativo | "There's some rumor in the space, someone started it like 8 years ago, and maybe it had some truth then that you need to have like HTML sections in your email. You need to have native text sections and whatnot. But that couldn't be farther from the truth." | transcricao (design) | L8026 |
| Prova oferecida (fala de Max) | "Look at how little HTML there is in this email (…) don't think that you need to have native text native text sections" | transcricao (design) | L8027-8028 |
| Google não lê imagem | "Google can't properly scan the image-based emails, but it can scan any of the alternate text or the text kind of behind it that is in the email. And that's what we would call HTML. Google read HTML. Image-based emails have a lot less HTML." | **outro-narrador** (deliverability) | L8500 |
| Um mínimo de HTML é necessário | "However, if you at least have a base amount of HTML for people that can't open the images or for Google to read, that's where your alt text comes into play." | **outro-narrador** (deliverability) | L8502 |
| Algum HTML melhora a entrega | "making sure you're including different bits of HTML in your email **will include deliverability** because it'll show different things that Google wouldn't pick up on if it was an image-only email" | **outro-narrador** (deliverability) | L8504 |

**Como responder:** as duas afirmações **não se anulam se lidas com cuidado**, mas
se anulam se citadas isoladamente — que é exatamente o que o roteamento por pasta
provoca. A distinção que reconcilia: em L8026 **Max** nega que **seções de texto
nativo** sejam necessárias **para vender**; em L8500-8504 **o outro narrador** afirma
que **algum** HTML ajuda o Google a ler o email, ou seja, é argumento de
**deliverability**, não de conversão. São duas perguntas diferentes com a mesma
palavra.

A ponte oferecida é o **alt text**: é HTML, é passo obrigatório do
upload (L8052-8053, este narrado por Max; L8496 e L8502 são do outro narrador), e é o que preenche o "base amount". Nunca responda
"não precisa de HTML" sem o alt text junto, nem "precisa de HTML" sem dizer que Max
rejeita explicitamente seções de texto nativo. **O corpus não diz quanto é "a base
amount"** (L8502) — se perguntarem quanto HTML basta, a resposta é que o corpus não
quantifica em lugar nenhum. Nota de verbatim: "will include deliverability" (L8504) é o texto do
bruto; a leitura óbvia é *improve*, mas a correção não está no corpus e não deve ser
citada como se estivesse.

## doutrina-segundos-de-atencao

Absorve `copy-janela-de-atencao` e `design-segundos-de-atencao`. A janela de atenção
tem **três valores diferentes**, divididos por módulo.

**Hoje:**

| Valor | Registro | Linha |
|---|---|---|
| "In 2025/2026, you *maybe* have 3 seconds" | slide (campanhas) | L5501 |
| "Todat, you *maybe* have 3 seconds" | slide (copy) | L6517 |
| "~3 seconds to hook your reader. Eliminate fluff." | resumo do módulo (copy) | L5605 |
| "if they can't skim it in 3 seconds, it won't get read" | slide (campanhas) | L5508 |
| "now you have about three" | **outro-narrador** (campanhas) | L4705 |
| "the first two to three seconds" | **outro-narrador** (campanhas) | L4707 |
| "attention spans that are really three seconds" | **outro-narrador** (copy) | L5891 |
| "you literally have two to four seconds to get your point across" | transcricao (design) | L7161 |
| "On average you have **2-4 seconds** to get your point across." | slide (design) | L8185 |
| "If we only get **3 seconds** of our viewers attention" | slide (design) | L8201 |

**Antes:**

| Valor | Registro | Linha |
|---|---|---|
| "Before, you could have had an average of **5-10 seconds** of attention per email." | slide (campanhas) | L5500 |
| "Before, you could have had an average of **5-10 seconds** of attention per email." | slide (copy) | L6516 |
| "before five, 10 seconds per email" | **outro-narrador** (campanhas) | L4703 |
| "used to be **three to five**, five to 10 maybe" | **outro-narrador** (copy) | L5891 |

**Como responder:** três valores para a mesma janela — 3 segundos, 2-3 segundos e 2-4
segundos. A divisão é quase limpa por módulo: **copy diz 3; design diz 2-4; campanhas
diz 3 no slide (L5501, L5508) e na fala (L4705), mas a mesma fala emenda "two to three"
duas linhas depois (L4707)** — o 2-3 tem uma única ocorrência e ela está em campanhas.
Ressalva de atribuição: as duas linhas faladas de campanhas (L4705, L4707) estão em
L4686-4828, `outro-provavel` por [[mapa-da-autoria]] — são do material do curso, não fala de Max.
Fora dessa emenda, a fala e o slide de cada módulo concordam entre si. Não é contradição
de registro, é contradição entre aulas. Nenhuma versão traz fonte, e duas trazem o
hedge "maybe" escrito por ele (L5501, L6517). A resposta honesta é dar a faixa completa
**2-4** e dizer de qual aula veio cada ponta. O "3 seconds" de L8201 é paráfrase interna
do próprio deck de design 16 linhas depois de L8185, dentro da faixa — não é quarto
valor independente.

**O "antes" também diverge, e isso é uma correção feita nesta consolidação.** Três
registros dizem 5-10 segundos (L4703, L5500, L6516), mas L5891 oferece "three to five"
como alternativa na mesma frase. Dê os dois valores do "antes" e não converta em faixa
única. Ressalva de atribuição: L5891 está no bloco L5867-6082 ("Utilizing
Infographics"), classificado `outro-provavel` por [[mapa-da-autoria]] — **a única versão que
quebra o consenso de 5-10 é a de atribuição mais fraca**. O número que importa
operacionalmente é o de hoje, e é ele que está em disputa entre módulos.

