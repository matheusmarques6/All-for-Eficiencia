---
tipo: lacuna
sobre: vocabulario
descoberta_em: 2026-08-31
status: aberta
---

# O que falta

Nove cláusulas de "Quando NÃO usar", em nove variantes, são eliminatórias
por natureza — descrevem uma condição que, se verdadeira, exclui a
variante — e ainda assim não têm requisito correspondente no vocabulário de
`requisitos/`:

- [[products-4-produto-unico-com-prazo]] — "sem desconto" (existem três
  requisitos específicos de desconto — `desconto-percentual`,
  `desconto-escalonado`, `desconto-automatico-sem-cupom` — nenhum genérico
  que cubra "algum desconto, qualquer tipo")
- [[products-7-dois-com-galeria-de-angulos]] — "produto sem variação visual
  entre ângulos" (distinto de `acervo-por-angulo`, que exige a foto
  existir, não que o produto varie visualmente entre ângulos)
- [[products-8a-quatro-recomendacoes]] — "produtos sem diferença de
  finalidade"
- [[reviews-8-ugc-de-comunidade]] — "loja de produto único"
- [[body-2-colagem-de-data-comemorativa]] — "produto individual sem
  contexto de grupo"
- [[body-10-listicle-educativo]] — "material educativo aprovado"
- [[hero-2-pergunta-comparativa]] — grade de produtos / prova social como
  contexto vetado (não há valor de `momento` para "tipo de bloco
  concorrente na mesma seção")
- [[products-6-vitrine-de-sale]] — "categorias de ticket alto" (não há
  valor de `registro` para faixa de ticket)
- [[offer-4-manifesto-antes-do-cupom]] e
  [[offer-5-tres-diferenciais-e-cupom]] — "público que ainda não sabe o que
  a loja vende" (nenhum campo do vocabulário representa audiência sem
  contexto de categoria conhecida)

# Por que importa

`exige:` no frontmatter é um requisito duro — elimina a candidata antes do
ranking, sem ambiguidade. As nove condições acima são exatamente esse tipo
de sinal (eliminatório, binário), mas como não há valor de vocabulário para
representá-las, elas só existem em prosa livre, dentro de "Quando NÃO
usar". O Curador hoje lê `when_use`/`when_not_use` como critério de corte
(ver [[o-que-o-curador-ainda-nao-tem]]), então em tese consegue aplicar
essas nove condições ao ler a prosa inteira — mas nenhum consumidor que
trabalhe só com campos estruturados (`exige`/`momento`/`registro`) tem
onde gravar "sem desconto de qualquer tipo" ou "produto único na loja".

# O que se perde hoje

Nove vetos reais ficam presos em texto que só um leitor humano (ou um LLM
lendo a prosa inteira) consegue aplicar. Qualquer consumidor do vault que
trabalhe só com os campos estruturados do frontmatter — um script de
filtro, um pré-ranking determinístico, um agente com contexto limitado —
não tem como saber que `products-4` não serve uma loja sem nenhum tipo de
desconto, ou que `reviews-8` não serve uma loja de produto único.

# Fora do escopo desta entrega

Desenhar os nove conceitos que faltam no vocabulário (um requisito
genérico de desconto, um eixo de faixa de ticket, um sinal de "produto
único na loja", um sinal de audiência sem contexto de categoria, etc.) e
retroalimentar as nove variantes com eles. É expansão de vocabulário —
mesma categoria de trabalho de [[estruturas-de-welcome-sem-variantes]],
fora desta entrega.
