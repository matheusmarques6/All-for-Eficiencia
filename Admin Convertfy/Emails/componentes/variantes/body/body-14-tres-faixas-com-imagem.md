---
tipo: componente
slug: body-14-tres-faixas-com-imagem
variant_id: 8d87af44-1d73-4e09-a019-ec6efc1196e4
nome_no_banco: "body 14"
secao: body
status: aprovada
fonte: catalogacao-2026-09-19
schema_campos: 8
product_slots: 0
objecao: [qualidade-eficacia]
aliviador: [demonstracao_de_mecanismo]
profundidade: mecanismo
registro: [comercial]
registro_vetado: [luxo]
paleta: [claro]
papel_na_peca: [meio]
itens: { min: 3, max: 3 }
peso: { altura_px: 823, classe: medio, fonte: medido }
convivencia: []
exige: []
aprendizados: [[[titulos-precisam-carregar-o-argumento]], [[cada-alegacao-e-uma-promessa-operacional]]]
---

## Descrição curta
Empilha três razões escaneáveis, cada uma mostrada além de dita: o leitor passa o olho por três faixas idênticas e sai com três argumentos, cada um ancorado numa imagem. Obriga um título em caixa alta, três faixas de texto + imagem e um CTA sólido.

## Descrição detalhada
Título centralizado em caixa alta (`list_title`), três faixas idênticas empilhadas e um CTA sólido (`list_cta_label`). Cada faixa é um retângulo de contorno com um texto (`list_item_N_text`) e uma imagem gerada (`list_item_N_image`). Família fixa de 3 — nem 2 nem 4. Entre as três listas enumeradas do lote, esta é a de 3 itens COM imagem por item: difere da [[body-18-cinco-itens-com-titulo]] (5 itens, só texto, título+texto por item) e da [[body-19-tres-cards-alternados-com-icone]] (3 cards com ícone sobre fundo de imagem, registro de alto contraste).

## Quando usar
Bridge de sustentação quando a tese já foi dita e o toque pede três provas visuais do "como" — o que tem dentro, como se usa, o que muda. A imagem por item permite que cada razão seja demonstrada, não só afirmada, o que serve toques de profundidade mínima `mecanismo` ([[welcome-3]], [[abandoned_cart-3]]). Fecha parcialmente a lacuna [[body-tese-3-itens-sem-cupom]]: título + 3 itens, sem slot de cupom, papel meio. Precisa de três razões de naturezas distintas — três variações da mesma qualidade não são varredura, são repetição.

## Quando não usar
No [[abandoned_cart-1]]: o primeiro toque do carrinho proíbe qualquer coisa além do item, do botão e do frete — três faixas de argumento ali são o bloco defensivo que a intenção manda guardar para o toque 3. Também não usar quando a loja só sustenta uma razão verificável: preencher três faixas com duas razões reais e uma inventada é promessa operacional sem lastro.

## Convivência
Não empilhar com outra lista enumerada (body 18 ou body 19): duas varreduras em sequência leem como redundância. O par natural acima é uma tese (hero ou body 12); abaixo, produto ou prova.

## Notas de cadastro
Descrição do banco bate com a anatomia (3 faixas, imagem por faixa, CTA). Sem HTML no vault para medir altura — `peso` omitido; ver relatório.
