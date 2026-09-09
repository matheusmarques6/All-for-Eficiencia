---
tipo: indice
modulo: design
assunto: conflitos-design-estrutura-e-cta
autor: max-sturtevant
conflitos: [design-botao-above-the-fold-sempre, design-repeticao-de-cta, design-quantidade-de-produtos, design-quantidade-de-bridges, design-bridge-e-product-opcionais, design-altura-do-slice, design-blocky, design-metodos-de-transicao-ausentes, design-tres-usos-de-75-por-cento]
status: aprovado
---

Registro dos conflitos do módulo `design` do corpus de Max Sturtevant sobre a estrutura do email e o CTA: botão above the fold, repetição de CTA, quantidade de produtos e de bridges, seções bridge e product opcionais, altura do slice, o estilo blocky, métodos de transição ausentes e os três usos do número 75%. Cada entrada lista os valores divergentes por registro e fecha com um "Como responder".


`design-html-vs-imagem` está em [[_conflitos#Conflitos entre módulos]];
`design-cta-por-produto` em [[_conflitos#Conflitos dentro do mesmo registro]];
`design-segundos-de-atencao` e `design-nomes-de-marca` resolvem para outros slugs.


## design-botao-above-the-fold-sempre

| Versão | Valor | Registro | Linha |
|---|---|---|---|
| Sempre | "Most users won't scroll. Put a CTA button in the hero section so every reader sees it immediately." | slide | L8135 |
| Sempre | "Not every customer will scroll on your email, so you want a button available in the hero section. This way EVERY customer has the ability to visit the site" | slide | L8154-8155, repetido em L8250-8251 |
| Sempre | "we always need to give people the option to click" | transcricao | L7021 |
| 75% dos emails | "Button above the fold for 75% of your email. Don't need to include it in every single one, but I'd recommend majority of them." | transcricao | L7027-7029 |

**Como responder:** a posição mais sustentada é botão above the fold **sempre** —
está em três lugares do deck (L8135, L8154, L8250) e no começo da própria fala
(L7021). A exceção é uma frase só, dele, imediatamente depois de afirmar o contrário
(L7027-7029), e ele mesmo já a enfraquece com "I'd recommend majority of them".
Responda: a regra é sempre; ele admite abrir mão em até um quarto dos emails, sem
dizer em quais. O corpus não dá critério para escolher esse quarto. Cuidado com o
número: ver `design-tres-usos-de-75-por-cento`.


## design-repeticao-de-cta

| Versão | Valor | Registro | Linha |
|---|---|---|---|
| 2-3 vezes | "Repeat your CTA 2–3 times throughout the email." | slide | L8137 |
| sem número | "repeat your CTA throughout the email"; e o contrapeso "Don't confuse that with throwing a shit ton of buttons in your email. That's going to overwhelm the customer." | transcricao | L7051-7059 |

**Como responder:** o número é do slide e vale como especificação: 2-3. Mas a fala
acrescenta o limite superior que o número não carrega — repetir não é encher. O
exemplo dele de repetição correta tem botão na hero, no meio, no fim, mais os botões
individuais de produto (L7063-7065), o que já passa de três se contar os de produto.
Ou seja: 2-3 vale para o CTA **principal**, não para o total de botões do email.


## design-quantidade-de-produtos

| Versão | Valor | Registro | Linha |
|---|---|---|---|
| livre | "You can feature however many products that you want." | transcricao | L7486 |
| poucos | "Ideally not that many." | transcricao | L7488 |
| um | "You can have a product section be just one product as well" | transcricao | L7490 |
| oito | "You can have eight products if you want." | transcricao | L7492 |
| testar | "Just test it." | transcricao | L7494 |
| silêncio | nenhum número | slide | L8274-8290 |

**Como responder:** cinco respostas em oito linhas da mesma fala, e o slide não
arbitra. O que é estável não é a quantidade, é a estrutura: cada produto com botão
próprio e um botão geral no fim (L7496). Responda com a faixa inteira — 1 a 8, com
preferência declarada por poucos — e com o critério real, que é teste, não número.


## design-quantidade-de-bridges

| Versão | Valor | Registro | Linha |
|---|---|---|---|
| 0 ou 1 | "You don't always need a bridge. You could go straight to the product section if you want." | transcricao | L7368-7370 |
| 0, 1 ou 2 | "In some cases you won't have a bridge, in some you'll have two." | slide | L8260 |

**Como responder:** é especificação, então vale o slide: até dois bridges. Mas
registre que a fala nunca menciona dois e não dá exemplo de email com dois, e que o
corpus não diz em que caso o segundo entra.


## design-bridge-e-product-opcionais

| Versão | Valor | Registro | Linha |
|---|---|---|---|
| Opcional, sem frequência | "Bridge is optional, product section is optional, every email is going to have a hero section." | transcricao | L7238 |
| Opcional, mas frequente | "Not every email will have a bridge or a product section, but most will." | slide | L8229 |

**Como responder:** não são versões incompatíveis — são a mesma regra com e sem
frequência declarada. Responda: obrigatória só a hero; bridge e product são opcionais
e, segundo o deck, presentes na maioria dos emails. Footer é universal (L7500, L8293),
o que é diferente de obrigatório por email: é o mesmo bloco em todos.


## design-altura-do-slice

| Versão | Valor | Registro | Linha |
|---|---|---|---|
| 800ish | "I recommend try not to go over kind of like 800ish or so" | transcricao | L8033 |
| 720 | "I recommend doing something like I'd probably maybe go to like 720 right here" | transcricao | L8033 |
| mil | "maybe I can extend this and kind of like push it to like the thousand before we move on to the next section because we're going to be using the same link across this" | transcricao | L8036 |

**Como responder:** os três números saem do mesmo vídeo, e 800 e 720 saem da mesma
linha. Não existe versão do slide para arbitrar. Responda: o teto que ele enuncia é
~800, o valor que ele executa é 720, e ele estica até mil quando o trecho inteiro
compartilha o mesmo link. O critério que governa **não é a altura — é o link**: um
slice por área de link distinto (L8036-8037). A altura é a consequência. Ver
`doutrina-formato-do-slice` para o 2x de exportação e o formato.


## design-blocky

| Versão | Valor | Registro | Linha |
|---|---|---|---|
| Errada, corrigida em cena | "we don't want things to be too blocky because it'll be too easy for someone to scroll" | transcricao | L7538 |
| Correção | "Or excuse me. We if you have sections that are super blocky people might reach the end of a section and not want to move on to the next section." | transcricao | L7540-7542 |
| Confirmação | "Having separate sections that are blocky and unrelated will lead to churn." | slide | L8305 |

**Como responder:** vale a correção, confirmada pelo slide. Seções muito demarcadas
criam ponto de parada — a pessoa acha que acabou e sai. A primeira formulação inverte
a causa e não deve ser citada. Registrado aqui porque a frase errada está no bruto e
um agente que leia só L7538 responde ao contrário.


## design-metodos-de-transicao-ausentes

| Versão | Valor | Registro | Linha |
|---|---|---|---|
| Promete e não entrega | "Here are a few methods to do this:" e nada depois | slide | L8307 |
| Quatro métodos | gradiente; formas/quebras de linha; fundo consistente com elementos em primeiro plano; transição atrás de foto | transcricao | L7552-7586 |

**Como responder:** **lacuna do slide.** Os quatro métodos só existem na fala. Se
alguém pedir "o que o deck diz sobre transições", a resposta é: o deck define o que
são e por que importam (L8304-8306), lista zero métodos, e os quatro vêm da aula. Não
é contradição de conteúdo — mas responder como se fosse do deck seria erro de
atribuição.


## design-tres-usos-de-75-por-cento

**Armadilha de leitura, não conflito.** O mesmo número mede três coisas incompatíveis
dentro do mesmo módulo.

| Referente | Valor | Registro | Linha |
|---|---|---|---|
| Esforço na hero | "75% of your efforts should go to this" | slide + transcricao | L8235 / L7258 |
| Emails com botão above the fold | "Button above the fold for 75% of your email" | transcricao | L7027 |
| Marcas auditadas sem botão por produto | "75% of the brands I audit don't have individual shop now buttons" | transcricao | L7089 |

**Como responder:** **nunca cite "75%" sem o referente.** Não é contradição — é
armadilha de recuperação: uma busca por "75%" devolve três linhas que parecem falar
da mesma coisa e não falam. Há um quarto uso, fora do módulo: "Form covers at least
75% of screen" (L1253, L657) — ver `list-growth-popup-vs-full-page`.

---


