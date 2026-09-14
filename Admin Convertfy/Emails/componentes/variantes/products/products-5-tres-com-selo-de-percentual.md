---
tipo: componente
slug: products-5-tres-com-selo-de-percentual
secao: products
nome_no_banco: "produtos 5 - 3 produtos mesmo fundo"
variant_id: 7ef1a9f4-5141-4732-b58c-15628ac8e4a8
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [campanha-promocional]
momento_vetado: [carrinho-abandonado, checkout-abandonado, transacional]

# --- eixos de ranking, na ordem do protocolo ---
objecao: [escolha-variedade]
registro: [premium-editorial]
registro_vetado: []
paleta: []
papel_na_peca: [meio]

# --- requisitos duros (eliminam) ---
exige: [desconto-percentual]
diretivas_de_imagem: [canto-livre-para-selo]

# --- capacidade e composição ---
product_slots: 3
itens: { min: 3, max: 3 }
peso: { altura_px: 2994, classe: peca-inteira, fonte: medido }
convivencia: [exige-hero-ou-contexto-acima]

# --- fios para o resto do vault ---
aprendizados: ["[[titulos-precisam-carregar-o-argumento]]"]
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: null
schema_campos: 23
status: aprovada
---

## Descrição curta

Bloco de oferta em catálogo curto. Três produtos, cada um com foto, nome, três benefícios em lista e botão próprio, com um selo circular de percentual colado na foto. Momento de uso: campanha de desconto por categoria, quando o leitor escolhe entre poucas opções da mesma linha e o desconto vale para todas.

## Descrição detalhada

Três blocos de produto empilhados, alternando o lado da foto, sem título de seção e sem CTA final.  

Quatro mecanismos definem a variante:  

Cada bloco tem métrica própria. Larguras de 564, 598 e 531px; paddings de 72, 82 e 76px; fotos de 277 × 384, 244 × 406 e 244 × 400. Não é grade regular — é layout desenhado produto a produto, e é isso que tira o ar de tabela.  

O selo circular é HTML e CSS, e muda de posição em cada bloco. v:oval no Outlook, border-radius:55px nos demais. No produto 1 ele fica no canto inferior; nos produtos 2 e 3, no topo. A posição segue o espaço vazio da foto, não uma regra fixa.  

Sem título de seção e sem CTA final. O bloco começa direto no primeiro produto e termina no terceiro. É um trecho de catálogo, não uma seção fechada — precisa de um hero acima para ter contexto.  

Três benefícios por produto, marcados com +. O sinal é caractere de texto numa coluna de 12px, não ícone. Sempre três, sempre na mesma estrutura.

## Quando usar

Campanha de desconto por categoria com percentual igual para todos os itens.  
Beleza, skincare, suplementos, cuidado pessoal — categorias em que o benefício se explica em três linhas.  
Quando há três produtos da mesma linha com páginas próprias.  
Quando existe hero ou barra de contexto acima: o bloco não se apresenta sozinho.  
Quando as fotos são packshots recortados que podem ceder um canto vazio para o selo.

## Quando NÃO usar

Percentuais diferentes por produto — o selo repetido com valores distintos vira ruído; nesse caso, preço riscado por item resolve melhor.  
Sem desconto — o selo é o mecanismo e não há onde colocar preço.  
Como bloco isolado — sem hero acima, o e-mail começa sem contexto.  
Fotos sem canto livre — o selo cai sobre o produto.  
Carrinho, checkout, transacional, prova social.  
Mais de três produtos — a métrica é desenhada bloco a bloco e não escala por repetição.

## Orientações de copy para a IA

Nome do produto — nome comercial em duas linhas. A quebra é semântica: linha 1 é o atributo, linha 2 é a categoria.  

Benefícios — exatamente três por produto, uma linha cada sempre que possível, começando por verbo na terceira pessoa ("Brightens with...", "Hydrates and smooths"). Sem ponto final. Os três precisam ser diferentes entre si e entre produtos — é o que permite escolher.  

Selo — o percentual em duas linhas: valor e a palavra de desconto. Nada além disso.  

CTA — verbo genérico, igual nos três. A diferenciação está no nome e nos benefícios.  

Proibições: preço em qualquer slot · benefícios repetidos entre produtos · quarto benefício · percentual diferente entre selos · prazo no selo · rótulos de botão diferentes entre produtos · ponto final nos benefícios.

## Design system

Container 600px fixo, borda 1px   
#000000 opcional (flag has_border). Raio de 55px no selo; CTA e demais elementos com cantos vivos.  

Estrutura — três blocos com métrica própria.  

| Bloco | Padding do bloco | Largura interna | Foto | Posição do selo | Padding do texto |  
|---|---|---|---|---|---|  
| Produto 1 | 72px topo · 34px esquerda | 564px | 277 × 384px, à esquerda | Canto inferior: 275px do topo | 21px topo |  
| Produto 2 | — | 598px | 244 × 406px, à direita | Canto superior: 28px da esquerda | 82px topo · 69px esquerda |  
| Produto 3 | 67px esquerda · 28px base | 531px | 244 × 400px, à esquerda | Canto superior: 56px da esquerda | 76px topo |  

Gap entre foto e texto: 26px nos blocos 1 e 3; no bloco 2 a foto fica à direita, com 39px de respiro na borda.  

Coluna de texto (261px nos blocos 1 e 3, 315px no bloco 2): nome 30/33px bold caixa alta em 2 linhas · lista com 24px acima, largura 209px, coluna do + com 12px e espaçador de 25px, itens 20/23px separados por 10px · CTA 20px acima, 164 × 43px.  

Paleta — três cores.  

| Papel | Hex (Colleen Rothschild) | Uso |  
|---|---|---|  
| Cor primária |  |  |  
| #443A31 | Fundo do selo, nome, benefícios e contorno do CTA |  |  
| Cor secundária |  |  |  
| #EDEAE3 | Fundo da seção |  |  
| Neutro invertido |  |  |  
| #FFFFFF | Texto dentro do selo |  |  

O selo é o único elemento sólido da peça. Não existe cor de acento — a cor vem das embalagens.  

Pele alternativa (HTML base): fundo branco, selo   
#D9D9D9 com texto   
#28252B, CTA preto sólido com label branco. Usar quando a marca não tem par de neutros próprio.  

Tipografia. Principal: Arial → Helvetica em benefícios, selo e CTA. Secundária: serif com itálico, usada apenas no nome do produto — é o que dá o registro de beleza premium. Nome em caixa mista quando há serif; caixa alta bold na pele do HTML base.  

Implementação. Cada foto é background-image do <td> com background-size próprio e bloco VML v:rect/v:fill type="frame", porque o selo fica sobreposto a ela. O selo exige as duas versões: v:oval no [if mso] e tabela com border-radius no [if !mso] — sem o VML, o Outlook renderiza quadrado. O + é caractere numa <td> de largura fixa, nunca imagem. Hack u + .body .txt-prim.  

Tags: PREHEADER, PRODUCT_N_IMAGE_URL, PRODUCT_N_NAME, PRODUCT_N_FEATURE_1, PRODUCT_N_FEATURE_2, PRODUCT_N_FEATURE_3, BADGE_TEXT, PRODUCT_CTA_LABEL, PRODUCT_N_CTA_URL.  

Erros que quebram o padrão: selo como imagem · selo quadrado no Outlook por falta do VML · selo na mesma posição nos três blocos · três blocos com a mesma métrica · quarto benefício · rótulos de botão diferentes entre produtos · preço no bloco · título de seção ou CTA final acrescentados · + como ícone.

## Direção fotográfica

Três slots com proporções diferentes — a variante não usa medida única.  

| Slot | Proporção | Slot em px | Ativo final |  
|---|---|---|---|  
| Produto 1 | 3:4 | 277 × 384 | 554 × 768 (2x) |  
| Produto 2 | 9:16 | 244 × 406 | 488 × 812 (2x) |  
| Produto 3 | 9:16 | 244 × 400 | 488 × 800 (2x) |  

PNG, < 150 KB cada.  

Regra crítica: o fundo do ativo é a cor da seção, chapado — não branco, não transparente. E cada foto precisa de um canto livre de 109 × 109px para o selo: inferior esquerdo no produto 1, superior esquerdo nos produtos 2 e 3.  

Composição. Packshot recortado em ângulo, flutuando, com sombra projetada longa e suave. O produto ocupa a diagonal do quadro e sangra por pelo menos uma borda. Rótulo legível e voltado para a câmera.  

Variação entre os três. Um com o produto inteiro e vertical; um com a embalagem aberta e a tampa separada, mais elementos soltos em volta (gotas, texturas); um com o produto tombado ou visto de cima, mostrando o conteúdo. Três packshots iguais em ângulos iguais anulam o layout orgânico.  

Luz. Direcional suave, sombra projetada visível — é ela que dá volume ao recorte sobre o fundo chapado.  

Proibições: fundo branco ou transparente · cenário · produto centralizado e alinhado ao eixo · sombra dura · selo ou texto queimado · três ângulos iguais · marca d'água.  

Adaptação por categoria — o que é o packshot:  

| Categoria | Enquadramento |  
|---|---|  
| Skincare | Frasco em ângulo, tampa separada, gotas de textura |  
| Suplementos | Pote inclinado, cápsulas ou pó soltos |  
| Cabelo | Bisnaga tombada, produto escorrendo |  
| Casa | Frasco em ângulo, superfície sugerida pela sombra |  
| Pet | Embalagem inclinada, petiscos soltos |  
| Maquiagem | Compacto aberto, swatch ao lado |

---

HTML: [[_html/products-5-tres-com-selo-de-percentual.html]] · Seção: [[_products]] · Protocolo: [[_protocolo-de-selecao]]
