---
tipo: indice
assunto: porta-de-entrada
autor: convertfy
status: aprovado
---

A porta de entrada da base de conhecimento da ConvertIA. Aqui estão os quatro corpos de conhecimento que alimentam o advisor, o que cada um pesa quando eles discordam, e por onde começar dependendo do que foi perguntado. Leia este mapa antes de abrir qualquer nota, porque a mesma pergunta tem respostas diferentes dependendo da fonte, e a fonte importa.

# Os quatro corpora e o peso de cada um

| Corpus | O que é | Autoria | Peso quando discordam |
|---|---|---|---|
| `Advisors/Max/` | curso de 9 módulos de Max Sturtevant (Well Copy) sobre email e SMS para e-commerce | um praticante | ensina o critério; tem conflitos internos registrados e é opinião, não medição |
| `Convertfy/` | o que a casa decidiu, testou e mediu em cliente | nossa | **vence a doutrina** quando existe número nosso |
| `Referencias/` | peças reais capturadas no mercado — hoje 29 conceitos de e-mail da Well Copy, ver [[mapa-das-referencias]] | de terceiros | mostra o que existe, não prova o que funciona |
| `Pesquisas/` | estudos com amostra e método declarados | de terceiros | **vence tudo** dentro do limite da amostra |

Regra que não se quebra: **quando duas fontes discordam, cite as duas e diga qual é qual.** Nunca resolva a divergência em silêncio, nunca apresente doutrina como medição.

# Por onde começar

| A pergunta é sobre... | Comece por |
|---|---|
| pop-up, captação de lista, form | [[mapa-do-popup]] |
| email marketing em geral, "por onde eu começo" | [[mapa-do-corpus-do-max]] (corpus do Max) |
| um número, prazo, taxa ou frequência | [[numeros-de-email-marketing-mais-pedidos]] → [[armadilhas-ao-citar-numero]] |
| como uma peça de e-mail fica pronta, exemplo real | [[mapa-das-referencias-de-email]] |
| se o corpus se contradiz nesse ponto | [[mapa-dos-conflitos]] |
| se o corpus sequer cobre o assunto | [[mapa-da-cobertura]] |
| quem de fato disse aquilo | [[mapa-da-autoria]] |

# O que esta base NÃO é

O corpus do Max é **doutrina de curso**: ensina o que fazer e por quê. Ele não contém nenhuma decisão nossa com número, nenhuma paleta ou tipografia real, e nenhum registro do que a casa rejeita. Peça montada de verdade só existe em [[mapa-das-referencias-de-email]] — e é de terceiros, não nossa. Enquanto `Convertfy/` estiver vazia, a IA não tem como saber o que é "do jeito da casa" — e vai improvisar se for perguntada. Preencher `Convertfy/` é o que mais aumenta a fidelidade da resposta.

# Como escrever nota nova

O molde e as seis regras que fazem uma nota existir estão em `Padrao Convertfy/como-escrever-uma-nota.md`. Modelos prontos por tipo em `Padrao Convertfy/_templates/`.

A regra que mais pega gente desprevenida: **sem `status: aprovado` no frontmatter, a nota é ignorada em silêncio** — ela continua bonita no Obsidian e some da base, sem erro em lugar nenhum. Use isso a favor: escreva com `status: rascunho` e promova quando estiver pronta.

# Pastas que não entram na base

- `Padrao Convertfy/` — instrução para quem escreve, não conhecimento para responder.
- `_templates/` — descartado pelo sincronizador por padrão.
- `Admin Convertfy/Emails/` — **outro sistema**. São notas lidas pelo Curador do pipeline de geração de e-mail, com contrato próprio de frontmatter e de nomes. Não misturar, não renomear.
