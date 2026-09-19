---
tipo: componente
slug: reviews-8-tres-cards-com-nota
variant_id: a6a84ff1-3068-4ab4-8ced-9cd0f30fe661
nome_no_banco: "review 8"
secao: reviews
status: aprovada
fonte: catalogacao-2026-09-19
schema_campos: 12
product_slots: 0
objecao: [adesao-social]
aliviador: [prova_por_volume, prova_de_terceiro]
profundidade: prova_de_terceiro
registro: [premium-editorial]
registro_vetado: [volume-impulso]
paleta: [claro]
papel_na_peca: [meio]
itens: { min: 3, max: 3 }
peso: { altura_px: 1359, classe: pesado, fonte: medido }
convivencia: [prova-social-nao-duplica-na-peca]
exige: [3-reviews-com-nome, nota-real]
aprendizados: [[[depoimento-nao-repete-pessoa]], [[numeros-de-escassez-precisam-de-backing]], [[ausencia-de-prova-social-assume-abertura]]]
---

## Descrição curta
Responde "sou só eu considerando isso?" com massa e rosto ao mesmo tempo: o leitor lê a nota agregada no subtítulo e três vozes nomeadas nos cards — o volume prova que não está sozinho, os nomes provam que o volume é gente. Obriga headline, subtítulo de nota, três reviews com nome, rótulos de verificado e CTA.

## Descrição detalhada
Headline serifada em duas linhas (`social_headline`) com um subtítulo de NOTA logo abaixo (`social_subtitle` — o agregado: "4,9 de 5 em N avaliações"), três cards de contorno preto empilhados — cada um com nome (`social_review_N_name`) e texto (`social_review_N_text`), com rótulo de verificado (`social_verified_label`, `_2`, `_3`) — e um CTA sólido (`social_cta_label`). É o caso legítimo de dois aliviadores: o subtítulo realiza `prova_por_volume`, os cards realizam `prova_de_terceiro`. NÃO confundir com [[reviews-8-ugc-de-comunidade]] — outra variante, já com nota, peça-inteira de UGC; esta é bloco de meio com cards de texto. Da vizinha [[reviews-5-prova-por-volume]], difere pelo agregado em subtítulo colado na headline.

## Quando usar
No toque de confirmação por terceiros ([[welcome-4]]: prova cirúrgica + massa estatística para os casos não parecerem escolhidos a dedo — este bloco é essa dupla em anatomia). Cada card fecha uma objeção de natureza distinta já atacada pelo flow. Exige três reviews reais com nome E uma nota agregada com lastro: número de avaliações vindo de dado, não de texto fixo.

## Quando não usar
No [[welcome-2]] (veta prova de terceiro e por volume) e em loja sem massa real: nota agregada inventada é o número sem backing que [[numeros-de-escassez-precisam-de-backing]] proíbe — se a loja tem 12 avaliações, o subtítulo desmente os cards. Ali, um card único (reviews-9/10) prova sem expor a base pequena.

## Convivência
Prova social não se duplica na peça: não com reviews-9/10, products-10 nem UGC. Três pessoas distintas nos cards, e nenhuma repetida de outro toque do flow ([[depoimento-nao-repete-pessoa]]).

## Notas de cadastro
Slug distinto de `reviews-8-ugc-de-comunidade` (variante diferente, 18 campos, peça-inteira) — sem colisão, mas o nome "review 8" no banco convida à confusão; endereçar por `variant_id`. `3-reviews-com-nome` e `nota-real` sem nota em `requisitos/` (vizinho: `tres-reviews-distintos`); relatório. `peso` medido no HTML de produção em 19/09.
