---
tipo: lacuna
sobre: conteudo
descoberta_em: 2026-08-31
status: aberta
---

# O que falta

Das 44 variantes do catálogo, nenhuma pertence à seção `header`. A distribuição
real é `hero` 9 · `body` 9 · `products` 9 · `reviews` 7 · `offer` 6 ·
`footer` 4 — seis seções, zero variantes de `header`. A pasta
`variantes/header/` não existe; a seção só aparece como stub em [[_header]].

# Por que importa

`secoes:` no frontmatter de uma [[_protocolo-de-selecao|estrutura]] pede
`header` com a mesma naturalidade com que pede `hero` ou `footer` — é uma das
oito categorias de bloco que o vocabulário do vault reconhece. Quando o
Blueprint (agente #4 do pipeline de geração) monta a lista de blocos de um
e-mail e um deles é `header`, o Curador não tem nenhuma candidata para
rankear. O pipeline não trata isso como erro: ele cai no `email_reference_templates`
(template global), e segue sem deixar rastro de que a seção pedida não
tinha variante nenhuma. Ver [[o-que-o-curador-ainda-nao-tem]] para o que o
Curador de fato recebe e verifica hoje.

# O que se perde hoje

Toda vez que um blueprint pede `header`, a loja recebe o header genérico do
template global — nunca uma peça escolhida para a marca, a objeção ou o
momento daquele e-mail. E como a queda é silenciosa, ninguém audita quantas
vezes isso acontece nem em quais lojas: não existe contador, log nem alerta
para "seção pedida sem candidata".

# Fora do escopo desta entrega

Desenhar ou aprovar variantes de `header`. Registrar o gap no código do
pipeline (log ou métrica de fallback silencioso). Ambos ficam para quem for
expandir o catálogo ou instrumentar o Montador.
