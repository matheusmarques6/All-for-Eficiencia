---
tipo: indice
assunto: casos-de-teste
autor: max-sturtevant
status: aprovado
---

Mapa da bateria de regressão do advisor Max: vinte e cinco casos de teste, divididos por categoria em oito notas, mais a nota de como rodar. Cada caso é uma pergunta com a resposta esperada e a peça do corpus que a falha acusa. Comece por aqui para achar a categoria certa; os casos em si estão nas notas listadas na tabela.

# O que este arquivo é

O eval do corpus. Não é uma lista de perguntas bonitas: é o conjunto de
perguntas que, **se o advisor errar, provam que alguma peça específica
quebrou** — e cada caso diz qual.

Vinte e cinco casos. Cada um tem quatro campos: a pergunta como um usuário real
faria, os elementos obrigatórios da resposta certa com âncora de linha, o erro
concreto que o caso pega, e a peça do corpus que a falha acusa.

**Toda âncora foi conferida abrindo a linha em `CONTEUDO BRUTO/max.md`.** Onde
o caso pede verbatim, o verbatim está aqui em inglês, como no bruto — inclusive
o ruído de ASR. Prosa em português, artefato em inglês: a mesma regra do
[[_protocolo]].

**Como ler o campo "Se errar, quebrou".** As peças possíveis são: roteamento
([[mapa-do-corpus-do-max]] + [[_protocolo]] passos 1-2), [[numeros-de-email-marketing-mais-pedidos]] (passo 3),
[[mapa-dos-conflitos]] (passo 4), [[mapa-da-cobertura]] (passo 6), [[persona]] (passo 7),
marcação de autoria ([[mapa-da-autoria]]) e verbatim (regra 3 do [[_protocolo]]).
Erro de mais de uma peça é comum e está registrado quando acontece.

---

# Onde estão os casos

| Nota | Que categoria de caso | Casos |
|---|---|---|
| [[casos-de-teste-de-roteamento-e-borda]] | Roteamento simples (resolve em 3 notas, não em 12) e casos de borda: recusa com aviso ativo, ruído de ASR preservado | 3 — C-01, C-24, C-25 |
| [[casos-de-teste-de-numero-integro]] | Número que o corpus cita: com conflito, sem conflito, e armadilha de referente | 3 — C-02, C-03, C-04 |
| [[casos-de-teste-de-numero-corrompido-e-rotulo]] | Número corrompido pelo ASR (irrecuperável, sem versão limpa, citável por outra passagem) e rótulo que não é percentual | 4 — C-05, C-06, C-07, C-08 |
| [[casos-de-teste-de-cobertura-e-recusa]] | Recusa total, recusa parcial, célula vazia que não se preenche e atribuição | 4 — C-09, C-10, C-11, C-12 |
| [[casos-de-teste-de-procedimento-e-artefato]] | Procedimento datado de ferramenta e artefato que só vale verbatim | 2 — C-13, C-14 |
| [[casos-de-teste-de-conflito]] | Conflito entre módulos e conflito dentro do mesmo registro | 4 — C-15, C-16, C-17, C-18 |
| [[casos-de-teste-de-voz-e-doutrina]] | Voz (regra dura sem hedge) e doutrina qualificada | 2 — C-19, C-20 |
| [[casos-de-teste-de-falso-negativo]] | Falso negativo: o corpus responde e o advisor recusa | 3 — C-21, C-22, C-23 |
| [[como-rodar-a-bateria-de-casos-de-teste]] | Não tem caso: como rodar, o que fazer com cada tipo de falha, cobertura da bateria | — |

Total: **25 casos**, C-01 a C-25, sem sobreposição entre as notas.
