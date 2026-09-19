---
tipo: componente
slug: products-10-winback-com-relato
variant_id: c43b3b63-88b8-4527-96d1-da10d19b840e
nome_no_banco: "produto 10"
secao: products
status: aprovada
fonte: catalogacao-2026-09-19
schema_campos: 7
product_slots: 1
objecao: [qualidade-eficacia]
aliviador: [prova_de_terceiro]
profundidade: prova_de_terceiro
registro: [premium-editorial]
registro_vetado: [volume-impulso]
paleta: [com-acento-definido]
papel_na_peca: [meio]
itens: { min: 1, max: 1 }
convivencia: [prova-social-nao-duplica-na-peca]
exige: [review-com-nome, 1-produto-com-link]
aprendizados: [[[depoimento-nao-repete-pessoa]], [[prova-de-terceiro-antes-do-cta]], [[posicao-muda-o-efeito-do-dispositivo]]]
---

## Descrição curta
Faz o leitor se reconhecer no problema antes de rever o produto: headline serifada com marca-texto, o sintoma nomeado, o desejo nomeado — e uma voz de cliente com nome fechando o arco sobre a foto do produto. Obriga headline em duas linhas, sintoma, desejo, review com autor e foto de um produto.

## Descrição detalhada
Headline em duas linhas de serifada com um marca-texto verde atrás da segunda (`winback_headline_1`, `winback_headline_2`), um parágrafo que nomeia o sintoma (`winback_symptom`), outro que nomeia o desejo (`winback_desire`), um review com autor (`winback_review`, `winback_review_author`) e a foto do produto (`winback_product_photo`, gerada). Um produto só, com arco emocional completo: sintoma → desejo → prova. O prefixo `winback_` diz o momento de origem: reconquista. É a única products do lote com prova de terceiro embutida — as vitrines (12–16) mostram; esta convence.

## Quando usar
Reconquista/reengajamento: quem já conheceu a marca e esfriou não precisa de catálogo — precisa de se reconhecer no sintoma e ouvir alguém como ela dizer que atravessou. Não há nota de intenção para flow de winback no vault (só welcome e abandoned_cart); até existir, o critério é este: toque tardio, contato frio, objeção madura. Exige review real com nome e um produto com link — o herói da reconquista, não um produto qualquer.

## Quando não usar
No [[welcome-2]]: a intenção veta prova de terceiro e prova por volume — o assunto do toque é decisão, não confiança, e este bloco é prova por desenho. Também não para contato que nunca comprou nem navegou: o arco "você sentiu X, queria Y" pressupõe histórico; num primeiro toque lê como presunção.

## Convivência
Não com bloco de reviews na mesma peça: a prova não se duplica ([[prova-social-nao-duplica-na-peca]]) — o review daqui JÁ é a prova da peça. O depoimento não repete pessoa usada em outro toque do mesmo flow.

## Notas de cadastro
Descrição do banco bate com a anatomia. `review-com-nome` e `1-produto-com-link` não existem em `requisitos/` (os vizinhos são `reviews-curtos`/`reviews-longos`/`produtos-com-pagina-propria`); listados no relatório. Sem HTML para medir altura — `peso` omitido.
