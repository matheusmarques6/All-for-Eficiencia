---
tipo: componente
slug: body-13-antes-e-depois-em-quadro
variant_id: 3789f525-7a72-4409-8c80-19cd3a1c1991
nome_no_banco: "body 13"
secao: body
status: aprovada
fonte: catalogacao-2026-09-19
schema_campos: 4
product_slots: 0
objecao: [qualidade-eficacia]
aliviador: [demonstracao_de_mecanismo]
profundidade: mecanismo
registro: [clinico-sobrio]
registro_vetado: [festivo]
paleta: [claro]
papel_na_peca: [meio]
peso: { altura_px: 528, classe: leve, fonte: medido }
convivencia: []
exige: [duas-fotos-comparaveis]
aprendizados: [[[cada-alegacao-e-uma-promessa-operacional]]]
ativa: true
dispositivo: antes_e_depois
---

## Descrição curta
Mostra o resultado em vez de afirmá-lo: o leitor compara duas fotos lado a lado e tira a conclusão sozinho, sem ler uma linha de argumento. Obriga duas imagens comparáveis e um rótulo curto para cada — não há texto corrido nem CTA.

## Descrição detalhada
Um quadro de 452px com borda preta de 2px — 528px de seção medidos, com o respiro externo —, dividido ao meio por um filete vertical da mesma espessura. Cada metade carrega uma foto (`compare_image_left`, `compare_image_right`) com seu rótulo (`compare_label_left`, `compare_label_right`). É a única variante do lote sem CTA e sem texto corrido: o bloco inteiro é a comparação. A prova é visual — antes e depois, com e sem, nosso e genérico — e por isso a profundidade é mecanismo por desenho, não por copy.

## Quando usar
No meio do e-mail, quando a objeção é "faz o que promete?" e a loja tem duas fotos genuinamente comparáveis: mesmo enquadramento, mesma luz, diferença visível. Serve o toque de convicção ([[welcome-3]], profundidade mínima de mecanismo) e o toque 3 do carrinho ([[abandoned_cart-3]]), onde a dúvida que trava pede um "como", não uma afirmação. Como não tem CTA próprio, precisa de um bloco com botão logo depois.

## Quando não usar
Categoria sem resultado visual (suplemento, serviço, gift card): sem duas fotos que se comparem de verdade, o par vira duas fotos soltas e o quadro promete uma prova que não entrega — e um antes/depois fabricado é alegação sem lastro operacional, problema de confiança e, em cosmético/saúde, jurídico. Também não usar como fecho do e-mail: sem CTA, ela deixa o leitor no ponto de decisão sem porta.

## Convivência
Nunca em sequência com outro bloco de comparação (body 16 ou outro antes/depois): duas comparações seguidas leem como insistência defensiva. Precisa de um bloco com CTA imediatamente abaixo — ela abre a conclusão, outro bloco fecha o clique.

## Notas de cadastro
Descrição do banco bate com a anatomia. O 452px do cadastro é a altura do quadro; a seção inteira mede 528px no HTML de produção (medição de 19/09) — é esse o valor de `peso`. `duas-fotos-comparaveis` não existe em `requisitos/`; listado no relatório.
