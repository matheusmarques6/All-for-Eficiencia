---
tipo: componente
slug: body-16-tabela-nos-x-eles
variant_id: 3c462f82-795f-4d85-8e5d-7b6e7b3b8125
nome_no_banco: "body 16"
secao: body
status: aprovada
fonte: catalogacao-2026-09-19
schema_campos: 23
product_slots: 0
objecao: [confianca-no-canal, preco-valor]
aliviador: [comparacao_de_categoria]
profundidade: mecanismo
registro: [comercial]
registro_vetado: [luxo]
paleta: [claro]
papel_na_peca: [meio]
itens: { min: 6, max: 6 }
peso: { altura_px: 1339, classe: pesado, fonte: medido }
convivencia: [raio-alto-nao-convive-com-canto-vivo]
exige: [6-diferencas-defensaveis]
aprendizados: [[[cada-alegacao-e-uma-promessa-operacional]], [[posicao-muda-o-efeito-do-dispositivo]]]
ativa: true
dispositivo: comparacao_pareada
---

## Descrição curta
Faz o leitor reconhecer os medos da categoria e ver a loja fora de todos eles, linha a linha: seis atributos, coluna "eles" contra coluna "nós", com selo de fechamento. Obriga título sublinhado, cabeçalhos das duas colunas, seis trios atributo/eles/nós, um CTA em pílula e um selo.

## Descrição detalhada
Título sublinhado (`compare_title`), três colunas de cantos arredondados lado a lado com bordas próprias — a coluna de atributos (`compare_feature_1..6`), a coluna deles (`compare_header_them`, `compare_them_1..6`) e a nossa (`compare_header_us`, `compare_us_1..6`) — mais CTA em pílula (`compare_cta_label`) e selo (`compare_badge`). 23 campos (22 de texto real + o selo, única imagem gerada); família fixa de 6 linhas. É a sucessora anatômica de [[body-5-comparacao-nos-vs-eles]] (inativa, 4-5 critérios): mesma objeção, grade maior e selo próprio.

## Quando usar
No quinto toque do welcome ([[welcome-5]]), quando quem ainda abre está comparando e a objeção é "por que comprar de VOCÊS?" — a comparação contra a experiência genérica da categoria, nunca contra concorrente nomeado. Também serve [[abandoned_cart-3]] quando a trava é de canal. Exige seis diferenças defensáveis com lastro operacional: cada linha riscada na coluna "eles" é uma promessa na coluna "nós". Esta variante devolve cobertura ativa à objeção `confianca-no-canal`, hoje servida só pela body-5 inativa (ver [[welcome-5-sem-variante-ativa]]).

## Quando não usar
No [[welcome-1]] ou no primeiro toque de qualquer flow: comparar cedo é defensivo — a marca se justificando antes da acusação planta a dúvida que pretendia curar ([[posicao-muda-o-efeito-do-dispositivo]]). E não usar quando a loja não tem seis diferenças defensáveis: a copy comparativa é a que mais inverte sentido no encurtador — linha fraca ou falsa numa tabela de seis contamina as cinco verdadeiras.

## Convivência
Nunca depois de outra comparação (body 13 em modo "nós vs. genérico", body 4/5): comparação depois de comparação lê como ataque, não como alívio. Cantos arredondados e pílula: não convive com blocos de canto vivo na mesma peça ([[raio-alto-nao-convive-com-canto-vivo]]).

## Notas de cadastro
Descrição do banco bate com a anatomia (23 campos conferem). `peso` medido no HTML de produção em 19/09. `6-diferencas-defensaveis` não existe em `requisitos/`; listado no relatório. Fecha, no eixo, a lacuna de `confianca-no-canal` ativa; a flag `ativa` é do banco, não desta nota.

**Conserto de 19/09 (admin, auditor de âncoras)**: só o `<title>` do HTML mudou; schema intacto.
