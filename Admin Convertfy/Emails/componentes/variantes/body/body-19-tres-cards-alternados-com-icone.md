---
tipo: componente
slug: body-19-tres-cards-alternados-com-icone
variant_id: d6fb99f3-6243-4f33-92c9-d90105900c98
nome_no_banco: "body 19"
secao: body
status: aprovada
fonte: catalogacao-2026-09-19
schema_campos: 8
product_slots: 0
objecao: [qualidade-eficacia]
aliviador: [demonstracao_de_mecanismo]
profundidade: mecanismo
registro: [bold-alto-contraste]
registro_vetado: [luxo, clinico-sobrio]
paleta: [full-dark]
papel_na_peca: [meio]
itens: { min: 3, max: 3 }
peso: { altura_px: 944, classe: medio, fonte: medido }
convivencia: []
exige: []
aprendizados: [[[titulos-precisam-carregar-o-argumento]]]
---

## Descrição curta
Entrega três razões em ritmo visual: o leitor desce em zigue-zague por três cards claros sobre fundo escuro, cada um com um ícone que nomeia o argumento antes do texto. Obriga headline, fundo de imagem, três cards com título + texto alternando de lado; o lugar do ícone é uma célula de texto fixa do layout, não imagem gerada.

## Descrição detalhada
Headline branca sobre fundo preto (`feat_headline`), imagem de fundo gerada (`feat_background_image`) e três cards claros de contorno preto alternando entre direita e esquerda, cada um com título (`feat_card_N_title`), texto (`feat_card_N_text`); o lugar do ícone de cada card é uma célula de texto fixa do layout (sem campo de imagem). Família fixa de 3. Difere das irmãs de lista do lote pelo registro: a [[body-14-tres-faixas-com-imagem]] é faixa reta sobre fundo claro e a [[body-18-cinco-itens-com-titulo]] é só texto; esta é a versão de alto contraste, com fundo de campanha e alternância que quebra a coluna central.

## Quando usar
Bridge de três razões em peça de registro forte — campanha, lançamento, marca jovem — quando o toque pede o "como" em três pontos e a hero acima já é escura ou de campanha: a paleta full-dark emenda sem costura. Serve toques de mecanismo ([[welcome-3]], [[abandoned_cart-3]]) quando a categoria tolera tom enérgico. Fecha parcialmente a lacuna [[body-tese-3-itens-sem-cupom]] no desenho (3 itens, sem cupom, papel meio), no registro oposto ao que a body 14 cobre.

## Quando não usar
Loja de registro luxo ou clínico-sóbrio: contorno grosso, fundo preto e ícones gritam onde essas marcas sussurram — o veto é de registro, legível no frontmatter. E não usar como terceira seção escura em sequência: full-dark atrás de full-dark vira um bloco só e a alternância dos cards perde a função de ritmo.

## Convivência
Não empilhar com outra lista enumerada (body 14, body 18). Entre duas seções full-dark, inserir uma clara — o contraste é o mecanismo do bloco, e some quando tudo ao redor é preto.

## Notas de cadastro
`nome_no_banco` copiado com o espaço final que existe no banco ("body 19 ") — erro de cadastro a corrigir no admin, não aqui. Descrição do banco bate com a anatomia. Sem HTML no vault para medir altura — `peso` omitido; ver relatório.

**Conserto de 19/09 (admin, auditor de âncoras)**: saíram `feat_card_1..3_icon` (os ícones são fixos no HTML). 11 → 8 campos.
