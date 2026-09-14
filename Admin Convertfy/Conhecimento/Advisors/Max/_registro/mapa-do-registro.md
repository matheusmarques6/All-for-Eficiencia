---
tipo: indice
assunto: auditoria-da-construcao
autor: max-sturtevant
status: aprovado
---

# O que é esta pasta

O rastro de como o corpus foi construído: o que **não** virou nota e por quê, e
como o laudo de autoria foi aplicado. É o material que [[mapa-das-fontes]] e [[mapa-da-autoria]]
resumem — aqui está o detalhe linha a linha.

**Não é rota de resposta.** Nenhuma entrada do roteamento do [[mapa-do-corpus-do-max]] termina
aqui. Não se abre para responder pergunta de usuário; abre-se para auditar uma
decisão depois.

Nada nesta pasta é fonte de número, verbatim ou especificação. Para isso são
[[numeros-de-email-marketing-mais-pedidos]] / [[mapa-dos-numeros-por-modulo]] e [[mapa-dos-conflitos]] / [[mapa-dos-conflitos-por-modulo]].

# O que tem dentro

| Arquivo | Para quê |
|---|---|
| `descartes-<modulo>.md` (10) | por módulo, as linhas do bruto que **não** entraram em nota nenhuma, com o motivo: ruído de ASR, CTA comercial, placeholder morto, título que mente. Também registra o que foi **mantido apesar de parecer descartável**, que é a parte mais útil |
| [[mapa-da-aplicacao-de-autoria]] | o registro de como o laudo de [[mapa-da-autoria]] foi aplicado nota por nota: que `registro:` mudou, que frase da prosa mudou, e o que foi deliberadamente **não** tocado |
| `sunset-segmento-L9545.png` | o PNG de 624×169 embutido em base64 na L9545 do bruto, referenciado por `![][image1]` em L3402. É de onde saiu a definição do segmento do Sunset Flow (180 dias sem abrir, 180 dias sem clicar, ao menos 10 emails recebidos, zero pedidos). Evidência, não ilustração — ver [[flows/sunset]] |

# Por que existe

[[mapa-das-fontes]] promete rastreabilidade linha a linha e um motivo declarado para
cada descarte. A promessa só vale se o registro existir em algum lugar: sem ele,
"isso a gente tirou de propósito" é indistinguível de "isso a gente perdeu".

Os dez `descartes-*` são também a defesa contra o erro inverso — transformar
descarte em lacuna. [[mapa-da-cobertura]] depende dessa separação: linha descartada
**nunca** vira lacuna, e lacuna **nunca** se explica dizendo que foi descartada.
