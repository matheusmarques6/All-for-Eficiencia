---
tipo: indice
assunto: casos-de-teste
autor: max-sturtevant
status: aprovado
---

Casos de regressão do advisor Max para números que o corpus consegue citar: valor com conflito entre versões, valor limpo com âncora de linha, e a armadilha de referente onde percentuais iguais falam de coisas diferentes. Três casos (C-02 a C-04), cada um com pergunta, elementos obrigatórios da resposta, erro típico e a peça do corpus que a falha acusa.

# Casos de número íntegro — C-02 a C-04


## C-02 · Número com conflito — as duas versões, nunca a média

**Pergunta:** Quantos emails eu coloco no meu welcome flow?

**Resposta certa contém:** o piso e a dispersão, separados. Piso, nos dois
registros: `"We need to have at least three emails in our welcome flow."`
(transcrição, L1436) e `"At least 3 emails long"` (slide, L3493). Preferência
declarada: `"I like to do like four to five emails."` (L1440). Faixas do slide:
`"Some welcome flows can we 3-4 emails others should be 6-8 emails."` (L3502).
Extremo: `"I have some welcome flows that are like 15 emails, but at least three
emails long."` (L1446). E o critério, que não é numérico — o corpus registra que
ele se recusa a dar template fixo porque `"a brand that's selling $10,000 saunas
is going to be different than a brand selling protein supplements"` (L1378).

**Resposta errada típica:** "cerca de 5 emails" ou "entre 4 e 6". Média
inventada a partir de 3, 4-5, 6-8 e 15 — indistinguível de conhecimento real e
impossível de auditar depois.

**Se errar, quebrou:** [[numeros-de-email-marketing-mais-pedidos]] regra 3 e [[mapa-dos-conflitos]]
(`welcome-contagem-de-emails`). Se a resposta deu só um dos valores, o passo 4
do [[_protocolo]] não rodou.

## C-03 · Número sem conflito — o valor verbatim com a linha

**Pergunta:** Qual é o limite de caracteres de um SMS, e o que acontece se eu
passar?

**Resposta certa contém:** os valores verbatim do slide de SMS.
`"In each SMS you only have 160 characters, which is NOT a lot…"` (L9390);
`"You can go over, but it's more expensive."` (L9391); `"If you go over by even 1
character to 161, the price of your message doubles."` (L9392). Em seguida, o
custo do MMS, que é a pergunta imediata: `"MMS messages are usually 2-3x MORE
expensive than sending an sms."` (L9383) e a exigência que ele deriva disso —
`"you'd have to make 2x-3x more revenue with your mms messages to outperform sms
message ROI"` (L9384), com a recomendação `"sticking to SMS text only messages"`
(L9386). E o emoji: `"the equivalent of 35-50 characters in your message"`
(L9405). Registro: tudo slide. Não existe entrada em [[mapa-dos-conflitos]] para
nenhum destes valores.

**Resposta errada típica:** arredondar ("uns 160, mais ou menos"), converter
("mais ou menos 2 a 3 linhas de texto") ou responder em português traduzindo os
verbatins.

**Se errar, quebrou:** [[numeros-de-email-marketing-mais-pedidos]] regra 1 (verbatim). Se a resposta inventou
um conflito que não existe, quebrou o passo 4 — [[mapa-dos-conflitos]] não tem entrada
para tamanho de mensagem.

## C-04 · Armadilha de referente — os três "75%" do design

**Pergunta:** Vi em algum lugar que 75% do email tem que ficar acima da dobra.
É isso mesmo?

**Resposta certa contém:** a correção do referente antes de qualquer número. O
corpus tem **três** "75%" no módulo de design e eles medem coisas diferentes:

- esforço de produção alocado na hero section — `"Most people will only read the
  top section so 75% of your efforts should go to this."` (slide, L8235; a mesma
  frase na fala, L7258);
- proporção de emails que precisam de botão acima da dobra — `"Button above the
  fold for 75% of your email."` (transcrição, L7027);
- marcas auditadas sem botão por produto — `"75% of the brands I audit don't have
  individual shop now [buttons]"` (transcrição, L7089).

E existe um quarto, em outro módulo: `"Form covers at least 75% of screen"`
(slide, L1253; fala L657), que é cobertura de tela do pop-up. Nenhum deles diz
que 75% do email fica acima da dobra.

**Resposta errada típica:** "sim, 75% do conteúdo tem que estar acima da dobra"
— cita o número sem o referente e funde os três numa regra que o corpus não tem.

**Se errar, quebrou:** [[armadilhas-ao-citar-numero]] (seção Armadilhas de número) e
[[mapa-dos-conflitos]] (`design-tres-usos-de-75-por-cento`, marcado `armadilha`, não
`conflito`).

