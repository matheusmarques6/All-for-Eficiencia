---
tipo: indice
modulo: fundamentos
assunto: mapa-local
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L1-236 (transcrição), L237-522 (slide GAMMA)"
status: rascunho
---

# Esta é a porta conceitual do corpus

Quem não sabe por onde começar lê duas notas, nesta ordem:

1. **[[os-tres-e-meio-pilares]]** — o mapa que organiza os outros oito módulos.
2. **[[metricas-nucleo]]** — os números que dizem se cada pilar está funcionando.

Com essas duas, qualquer pergunta do corpus tem endereço. Sem elas, as pastas
seguintes parecem uma lista de táticas soltas.

Faixa de origem: aulas 1 a 6 do curso (L1-236) e o deck GAMMA correspondente
(L237-522).

# As notas

| Nota | tipo | O que resolve |
|---|---|---|
| [[os-tres-e-meio-pilares]] | principio | list growth, flows, campanhas e o meio pilar de deliverability; o split 50/50 e suas três formulações |
| [[metricas-nucleo]] | especificacao | a tabela de metas verbatim e o racional de cada meta; onde ele crava erro e onde se recusa a dar número |
| [[estado-do-mercado]] | principio | o diagnóstico datado de conjuntura que sustenta "por que email" |
| [[escolha-do-esp]] | principio | Klaviyo vs Omnisend, a objeção de preço, e o conflito de interesse dos links |
| [[dashboard-do-klaviyo]] | procedimento | como ler o painel como diagnóstico; criar segmento passo a passo. **Datado** |
| [[glossario]] | artefato | índice das 4 partes; 99 termos em 12 categorias, verbatim em inglês |
| ↳ [[glossario-receita-e-flows]] | artefato | 💰 receita · 📬 tipos de email · 🔄 os 8 flows |
| ↳ [[glossario-segmentos-e-metricas]] | artefato | 🎯 segmentação · 📈 métricas de performance |
| ↳ [[glossario-deliverability-e-plataforma]] | artefato | 🧼 saúde de lista e deliverability · 🛠 plataforma e design |
| ↳ [[glossario-copy-e-estrategia]] | artefato | 🧠 copy · 🧪 testes · 📊 analytics · 🔐 compliance · 💡 estratégia |

# Os pilares e onde cada um é desenvolvido

Esta pasta define os quatro. Nenhum deles é executado aqui.

| Pilar | Definido em | Executado em |
|---|---|---|
| #1 List growth | L295-319 | [[list-growth/_index]] |
| #2 Flows | L321-332 | [[flows/_index]] |
| #3 Campanhas | L334-339 | [[campanhas/_index]] |
| #3.5 Deliverability | L341-349 | [[deliverability/_index]] |

Os módulos de [[copy/_index]], [[design/_index]], [[otimizacao/_index]] e
[[sms/_index]] atravessam os quatro pilares em vez de pertencer a um.

# Princípios que nascem desta faixa e moram em `doutrina/`

Não estão nesta pasta de propósito — são crenças transversais, não fundamentos do
módulo:

- [[o-custo-do-anuncio-e-travado-o-valor-do-clique-nao]] (L9-13)
- [[crescimento-de-lista-vence-tamanho-de-lista]] (L21-22, L295-319)
- [[o-inscrito-novo-e-mais-quente-que-o-atual]] (L22)

# Antes de responder qualquer número desta pasta

Esta faixa é a mais conflitante do corpus em proporção ao tamanho: onze entradas
em [[_conflitos-completo#fundamentos]] e mais cinco em [[_conflitos]] — as quatro
entre a tabela de metas e o glossário do **mesmo deck**, mais
`fundamentos-o-que-move-o-open-rate`. Abrir [[_numeros]] e [[_conflitos]] antes da nota,
sempre — em especial para open rate, unsubscribe, spam complaint e click rate.

# O que esta pasta declaradamente não cobre

- Preço de qualquer ferramenta. Nenhum valor, em nenhum registro.
- Revenue per recipient — ele nomeia a métrica e recusa dar guideline (L176).
- Setup técnico do Klaviyo (conexão com Shopify, domínio, importação de lista):
  o único passo prescrito é seguir o onboarding da própria plataforma (L36).
- Ordem de construção dos pilares. Eles são numerados, mas ele nunca diz o que
  fazer primeiro numa conta zerada.
