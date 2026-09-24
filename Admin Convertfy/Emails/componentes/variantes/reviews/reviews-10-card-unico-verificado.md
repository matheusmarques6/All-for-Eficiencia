---
tipo: componente
slug: reviews-10-card-unico-verificado
variant_id: 32476827-5458-4cc6-af26-f7e428f81521
nome_no_banco: "review 10"
secao: reviews
status: aprovada
fonte: catalogacao-2026-09-19
schema_campos: 5
product_slots: 0
objecao: [qualidade-eficacia]
aliviador: [prova_de_terceiro]
profundidade: prova_de_terceiro
registro: [bold-alto-contraste]
registro_vetado: [luxo]
paleta: [cinza-neutro]
papel_na_peca: [meio]
itens: { min: 1, max: 1 }
peso: { altura_px: 658, classe: medio, fonte: medido }
convivencia: [prova-social-nao-duplica-na-peca]
exige: [review-com-nome]
aprendizados: [[[depoimento-nao-repete-pessoa]], [[prova-de-terceiro-antes-do-cta]]]
ativa: true
dispositivo: prova_por_relato
---

## Descrição curta
Entrega uma voz de cliente com peso de manchete: o leitor vê um único card branco de contorno grosso sobre fundo cinza, lê o depoimento, o nome e o selo de compra verificada — uma prova, dita alto. Obriga título, texto do review, autor, rótulo de verificado e CTA.

## Descrição detalhada
Fundo cinza chapado em toda a seção. Título em duas linhas de caixa alta (`cardrev_title`), um card branco de contorno grosso e cantos arredondados com o depoimento (`cardrev_text`), o autor (`cardrev_author`) e o rótulo de verificado (`cardrev_verified_label`), e um CTA em pílula (`cardrev_cta_label`, example "SHOP NOW"). Um depoimento só — o selo "verificado" é rótulo de compra confirmada, não credencial de autoridade: quem tem credencial de CARGO é a [[reviews-1-depoimento-com-credencial]]; esta prova que a compra existiu, não que o autor é especialista. Difere da [[reviews-9-card-com-estrelas]] (mesmo dispositivo) pelo peso visual: contorno grosso e fundo cinza contra contorno fino e pílula de estrelas.

## Quando usar
Quando UM depoimento certo vale mais que três genéricos — o espelho do cético do [[welcome-4]] (alguém que declara ter tido a dúvida de quem lê) merece exatamente este palco: card único, sem concorrência visual. Também no fechamento com prova colada na pressão ([[welcome-6]]) e em [[abandoned_cart-2]] como a prova secundária que o toque admite. Exige review real com nome; o selo só entra se a compra for verificável na plataforma.

## Quando não usar
No [[welcome-2]]: a intenção veta prova de terceiro — o assunto é decisão, não confiança. E não usar quando o argumento do toque é volume ("todo mundo aprova"): um card único diz o oposto de massa — para volume, a certa é a reviews-8 com nota agregada.

## Convivência
Prova social não se duplica na peça ([[prova-social-nao-duplica-na-peca]]): não com reviews-8/9 nem com products-10 (que já embute relato). O depoente não repete pessoa usada em outro toque do flow.

## Notas de cadastro
Descrição do banco bate com a anatomia. Conforme a ficha: credencial aqui é selo de verificação, NÃO cargo — não classificar como autoridade (valor que nem existe no vocabulário). `review-com-nome` sem nota em `requisitos/` (vizinhos: `selo-compra-verificada`, `reviews-curtos`); relatório. `peso` medido no HTML de produção em 19/09.

**Conserto de 19/09 (admin, auditor de âncoras)**: example de `cardrev_cta_label` = "SHOP NOW" (o HTML dizia "CTA", que não ancorava por ser curto demais).
