---
tipo: indice
assunto: porta-de-entrada
autor: max-sturtevant
status: aprovado
---

# Onde você está

Corpus de conhecimento de Max Sturtevant (Well Copy) sobre email e SMS
marketing para e-commerce, extraído de um curso de 9 módulos. Fonte única:
`CONTEUDO BRUTO/max.md`, **9.545 linhas** — `wc -l` conta 9.544 porque o arquivo
termina sem quebra de linha, e a L9545 carrega um PNG em base64 com a definição
do segmento do Sunset Flow. Ver [[armadilhas-da-fonte-bruta]].

Este corpus é **isolado**. Não referencia nem é referenciado por
`Admin Convertfy/Emails/` — aquilo é outra doutrina, de outro autor, sobre o
mesmo assunto. Não misturar.

Ele também não é a base inteira. É **um** dos quatro corpora de
`Conhecimento/`, e o que menos pesa quando há medição nossa: veja
[[mapa-do-conhecimento]] para a precedência entre doutrina, decisão da
Convertfy, referência de mercado e pesquisa. Regra curta: **o que a Convertfy
mediu vence o que este curso ensina** — e quando as duas fontes divergem, a
resposta cita as duas e diz qual é qual.

# Leia sempre, antes de responder qualquer coisa

- [[_protocolo]] — como responder, na ordem, e o que nunca fazer.
- [[persona]] — a voz, os critérios de julgamento, o que Max nunca diria.

Só estes dois são carregados sempre. Todo o resto é sob demanda, pelo
roteamento abaixo.

# Roteamento por tipo de pergunta

| A pergunta é sobre... | Leia, nesta ordem |
|---|---|
| "por onde eu começo", visão geral da disciplina | [[mapa-dos-fundamentos]] |
| que taxa eu deveria bater, o que é saudável | [[fundamentos/metricas-nucleo]] → [[mapa-dos-conflitos]] → [[mapa-dos-conflitos-por-modulo]] se o slug tiver entrada lá |
| número, prazo, taxa, contagem, frequência | [[numeros-de-email-marketing-mais-pedidos]] → [[mapa-dos-conflitos]] → nota do assunto. Só descer para [[mapa-dos-numeros-por-modulo]] se a medida não estiver entre as dezessete mais pedidas, e para [[mapa-dos-conflitos-por-modulo]] se o slug tiver entrada lá |
| montar ou corrigir um flow | [[mapa-dos-flows]] → a nota do flow → [[mapa-dos-conflitos]] (→ [[mapa-dos-conflitos-por-modulo]]) |
| campanha, calendário, segmentação | [[mapa-das-campanhas]] |
| escrever copy, subject line, exemplo | [[mapa-de-copy]] → bloco Templates da nota do assunto |
| layout, seção do email, imagem | [[mapa-de-design]] |
| caixa de spam, domínio, warming | [[mapa-de-deliverability]] |
| o que testar, A/B | [[mapa-de-otimizacao]] |
| SMS | [[mapa-de-sms]] |
| pop-up, captar lista | [[mapa-de-list-growth]] |
| "por que ele defende isso" | [[mapa-da-doutrina]] |
| configurar ferramenta (Klaviyo, Figma, Shopify) | nota `tipo: procedimento` — sempre datada, avisar antes |
| "isso é mesmo ele falando?", quem disse o quê | [[mapa-da-autoria]] |
| algo que parece fora do corpus | [[mapa-da-cobertura]] → recusar nomeando a lacuna |

# As dez pastas

| Pasta | O que tem dentro |
|---|---|
| [[mapa-dos-fundamentos]] | os 3,5 pilares, métricas-núcleo, glossário, escolha de ESP, estado do mercado |
| [[mapa-da-doutrina]] | princípios transversais e o processo de criação dele |
| [[mapa-de-list-growth]] | pop-up, oferta, tipos de form, A/B de captação |
| [[mapa-dos-flows]] | os 8 flows: gatilho, delays, filtros, sequência, template |
| [[mapa-das-campanhas]] | frequência, calendário, pilares de conteúdo, segmentação |
| [[mapa-de-copy]] | S.C.E., subject line, preview text, infográficos, prompt de IA |
| [[mapa-de-design]] | 3 princípios, doutrina por seção, transições, upload |
| [[mapa-de-deliverability]] | setup técnico, rampa de warming, reparo, auditoria |
| [[mapa-de-otimizacao]] | testes A/B: o que compara e quando vale rodar |
| [[mapa-de-sms]] | doutrina, 5 flows, calendário, horários de envio |

# As nove notas de controle

| Nota | Para quê |
|---|---|
| [[numeros-de-email-marketing-mais-pedidos]] | as três regras de uso, as 17 medidas mais pedidas e as armadilhas de número. É esta que se abre |
| [[mapa-dos-numeros-por-modulo]] | as 44 tabelas por domínio — todo número do corpus, verbatim. Só sob demanda, a partir de [[numeros-de-email-marketing-mais-pedidos]] |
| [[mapa-dos-conflitos]] | o índice dos 126 slugs de contradição + as duas seções transversais na íntegra. É esta que se abre |
| [[mapa-dos-conflitos-por-modulo]] | as 108 entradas por módulo e o registro de arbitragem. Só sob demanda, a partir de [[mapa-dos-conflitos]] |
| [[mapa-da-cobertura]] | o que falta no corpus, classificado por tipo de lacuna. A densidade por assunto está em [[densidade-do-corpus-por-assunto]] |
| [[mapa-das-fontes]] | mapa linha→módulo→registro, e o que foi descartado, com motivo |
| [[mapa-da-autoria]] | o laudo de quem fala em cada um dos 41 blocos. É o que decide se uma frase sai como "o Max diz" ou "o material do curso diz" — o único erro deste corpus que é invisível na saída |
| [[mapa-dos-casos-de-teste]] | as perguntas de verificação |
| [[arquitetura-decisoes-e-leis-de-manutencao]] | por que este corpus é construído assim |

# `_registro/` — auditoria, não rota de resposta

[[mapa-do-registro]] guarda o rastro de construção que as notas de controle
prometem mas não carregam: os dez `descartes-<modulo>.md` (linha a linha, o que
ficou de fora e por quê — é o detalhe que [[mapa-das-fontes]] resume), o
as quatro notas de [[mapa-da-aplicacao-de-autoria]] (como o laudo de
[[mapa-da-autoria]] foi aplicado, nota por nota) e `sunset-segmento-L9545.png`, o print extraído da L9545 de onde saiu a
definição do segmento do Sunset Flow.

**Não é rota de resposta.** Nenhuma pergunta do roteamento acima desce até aqui.
Serve para auditar uma decisão depois — por que uma linha não virou nota, por
que uma atribuição mudou — e para provar que o descarte foi deliberado.

# Convenções

**`tipo:` diz o que a nota é, e muda como ela pode ser usada:**

| tipo | O que é | Como usar |
|---|---|---|
| `principio` | uma crença dele, com racional | pode parafrasear |
| `especificacao` | gatilho, delay, filtro, limiar | exato ou não serve |
| `artefato` | subject line, template, código Klaviyo | verbatim, em inglês, nunca traduzir |
| `procedimento` | passo a passo de ferramenta | datado; avisar que pode ter mudado |

**`registro:` diz de onde veio, e isso decide a precedência:**

- `transcricao` — ele falando. Onde estão julgamento, exceção, o porquê, a voz.
- `slide` — o deck gamma. Onde estão número de tabela, template, código, checklist.
- `outro-narrador` — trecho em que a voz não é a do Max. Não citável como fala dele.

Quando os dois primeiros discordam sobre **especificação**, vale o slide e
abre-se entrada em [[mapa-dos-conflitos]]. Quando discordam sobre **julgamento**, vale
a fala.

**`fonte:` carrega a linha do bruto.** Toda afirmação é rastreável até
`CONTEUDO BRUTO/max.md`. Se o agente errar um fato, abra a linha: dá para ver
se o erro é da nota ou do corpus.

# O que este corpus não é

Não é manual de boas práticas de email marketing. É o que **um** profissional
diz, com as contradições dele preservadas. Onde ele se contradiz, o corpus
mostra as duas versões. Onde ele não fala, o corpus diz que não fala.
