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
do segmento do Sunset Flow. Ver [[_fontes]].

Este corpus é **isolado**. Não referencia nem é referenciado por
`Admin Convertfy/Emails/` — aquilo é outra doutrina, de outro autor, sobre o
mesmo assunto. Não misturar.

# Leia sempre, antes de responder qualquer coisa

- [[_protocolo]] — como responder, na ordem, e o que nunca fazer.
- [[persona]] — a voz, os critérios de julgamento, o que Max nunca diria.

Só estes dois são carregados sempre. Todo o resto é sob demanda, pelo
roteamento abaixo.

# Roteamento por tipo de pergunta

| A pergunta é sobre... | Leia, nesta ordem |
|---|---|
| "por onde eu começo", visão geral da disciplina | [[fundamentos/_index]] |
| que taxa eu deveria bater, o que é saudável | [[fundamentos/metricas-nucleo]] → [[_conflitos]] → [[_conflitos-completo]] se o slug tiver entrada lá |
| número, prazo, taxa, contagem, frequência | [[_numeros]] → [[_conflitos]] → nota do assunto. Só descer para [[_numeros-completo]] se a medida não estiver entre as dezessete mais pedidas, e para [[_conflitos-completo]] se o slug tiver entrada lá |
| montar ou corrigir um flow | [[flows/_index]] → a nota do flow → [[_conflitos]] (→ [[_conflitos-completo]]) |
| campanha, calendário, segmentação | [[campanhas/_index]] |
| escrever copy, subject line, exemplo | [[copy/_index]] → bloco Templates da nota do assunto |
| layout, seção do email, imagem | [[design/_index]] |
| caixa de spam, domínio, warming | [[deliverability/_index]] |
| o que testar, A/B | [[otimizacao/_index]] |
| SMS | [[sms/_index]] |
| pop-up, captar lista | [[list-growth/_index]] |
| "por que ele defende isso" | [[doutrina/_index]] |
| configurar ferramenta (Klaviyo, Figma, Shopify) | nota `tipo: procedimento` — sempre datada, avisar antes |
| "isso é mesmo ele falando?", quem disse o quê | [[_autoria]] |
| algo que parece fora do corpus | [[_cobertura]] → recusar nomeando a lacuna |

# As dez pastas

| Pasta | O que tem dentro |
|---|---|
| [[fundamentos/_index]] | os 3,5 pilares, métricas-núcleo, glossário, escolha de ESP, estado do mercado |
| [[doutrina/_index]] | princípios transversais e o processo de criação dele |
| [[list-growth/_index]] | pop-up, oferta, tipos de form, A/B de captação |
| [[flows/_index]] | os 8 flows: gatilho, delays, filtros, sequência, template |
| [[campanhas/_index]] | frequência, calendário, pilares de conteúdo, segmentação |
| [[copy/_index]] | S.C.E., subject line, preview text, infográficos, prompt de IA |
| [[design/_index]] | 3 princípios, doutrina por seção, transições, upload |
| [[deliverability/_index]] | setup técnico, rampa de warming, reparo, auditoria |
| [[otimizacao/_index]] | testes A/B: o que compara e quando vale rodar |
| [[sms/_index]] | doutrina, 5 flows, calendário, horários de envio |

# As nove notas de controle

| Nota | Para quê |
|---|---|
| [[_numeros]] | as três regras de uso, as 17 medidas mais pedidas e as armadilhas de número. É esta que se abre |
| [[_numeros-completo]] | as 44 tabelas por domínio — todo número do corpus, verbatim. Só sob demanda, a partir de [[_numeros]] |
| [[_conflitos]] | o índice dos 126 slugs de contradição + as duas seções transversais na íntegra. É esta que se abre |
| [[_conflitos-completo]] | as 108 entradas por módulo e o registro de arbitragem. Só sob demanda, a partir de [[_conflitos]] |
| [[_cobertura]] | o que o corpus cobre, com que densidade, e o que falta |
| [[_fontes]] | mapa linha→módulo→registro, e o que foi descartado, com motivo |
| [[_autoria]] | o laudo de quem fala em cada um dos 41 blocos. É o que decide se uma frase sai como "o Max diz" ou "o material do curso diz" — o único erro deste corpus que é invisível na saída |
| [[_casos-de-teste]] | as perguntas de verificação |
| [[_arquitetura]] | por que este corpus é construído assim |

# `_registro/` — auditoria, não rota de resposta

[[_registro/_index]] guarda o rastro de construção que as notas de controle
prometem mas não carregam: os dez `descartes-<modulo>.md` (linha a linha, o que
ficou de fora e por quê — é o detalhe que [[_fontes]] resume), o
`aplicacao-autoria.md` (como o laudo de [[_autoria]] foi aplicado, nota por
nota) e `sunset-segmento-L9545.png`, o print extraído da L9545 de onde saiu a
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
abre-se entrada em [[_conflitos]]. Quando discordam sobre **julgamento**, vale
a fala.

**`fonte:` carrega a linha do bruto.** Toda afirmação é rastreável até
`CONTEUDO BRUTO/max.md`. Se o agente errar um fato, abra a linha: dá para ver
se o erro é da nota ou do corpus.

# O que este corpus não é

Não é manual de boas práticas de email marketing. É o que **um** profissional
diz, com as contradições dele preservadas. Onde ele se contradiz, o corpus
mostra as duas versões. Onde ele não fala, o corpus diz que não fala.
