---
tipo: componente
slug: products-8a-quatro-recomendacoes
secao: products
nome_no_banco: "produto 8 - 4 produtos"
variant_id: 640b0a34-8632-4041-8378-38fe804c1516
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [cross-sell, catalogo-mais-vendidos]
momento_vetado: [carrinho-abandonado, checkout-abandonado, welcome-1, transacional]

# --- eixos de ranking, na ordem do protocolo ---
objecao: [escolha-variedade]
registro: []
registro_vetado: [luxo, premium-editorial]
paleta: []
papel_na_peca: [meio]

# --- requisitos duros (eliminam) ---
exige: [fragmentos-de-contorno]

# --- capacidade e composição ---
product_slots: 4
itens: { min: 4, max: 4 }
peso: { altura_px: 2196, classe: peca-inteira, fonte: medido }
convivencia: []

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: média
schema_campos: 13
status: aprovada
---

## Descrição curta

Bloco de recomendação de produtos com quatro itens, cada um com nome, indicação de uso e botão próprio, fechando com um CTA de coleção. Momento de uso: e-mail de catálogo, guia de presentes ou cross-sell, quando o leitor precisa escolher entre opções e não seguir um caminho único.

## Descrição detalhada

Título em duas linhas; abaixo, quatro linhas de produto de 271px cada; no fim, um CTA de contorno com a largura quase total.  

Quatro mecanismos definem a variante:  

O contorno do card é metade HTML, metade imagem. A coluna de texto carrega a borda de três lados; os outros pedaços da linha vêm dentro do ativo de imagem. É a exigência de produção mais rígida do arsenal: a foto não é só a foto, é a foto mais os fragmentos do contorno.  

A foto sangra para fora do contorno. O retângulo é quebrado do lado onde a imagem entra. Sem esse transbordo, o bloco vira uma tabela de produtos comum.  

Alternância 2 + 2, não em zigue-zague. Produtos 1 e 2 com a foto à esquerda, 3 e 4 com a foto à direita. É ritmo de blocos: dois de cada lado, com o respiro maior na virada.  

Cinco botões no bloco. Um por produto, mais o CTA final. Os quatro primeiros são sólidos e apontam para produtos; o último é de contorno e aponta para a coleção — a hierarquia é de preenchimento, não de tamanho.

## Quando usar

Guia de presentes, catálogo sazonal, cross-sell, "nossos mais vendidos".  
Quando há quatro produtos distintos com indicações de uso diferentes entre si.  
Beleza, cuidado pessoal, casa, pet, ferramenta, papelaria — categorias onde a escolha é por finalidade.  
Quando cada produto tem página própria para receber o clique.  
Quando o acervo permite produzir os ativos com os fragmentos de contorno embutidos.

## Quando NÃO usar

Ação única. Cinco botões destroem qualquer e-mail com um objetivo só — carrinho, checkout, welcome com cupom.  
Menos de quatro produtos — a alternância 2 + 2 não se forma.  
Produtos sem diferença de finalidade — se as quatro indicações forem iguais, a grade não ajuda a escolher.  
Sem ativos com fragmentos de contorno — colar uma foto comum deixa a moldura aberta.  
Topo de e-mail, transacional, prova social.  
Marca de luxo editorial: quatro botões sólidos e um contornado é registro de catálogo.

## Orientações de copy para a IA

Título — duas linhas, caixa alta, com o gancho da ocasião ou do público. Pode ser bem-humorado; é o único slot com liberdade de tom no bloco.  

Nome do produto — o nome comercial em duas linhas, caixa alta. Quebra semântica: linha 1 é a família, linha 2 é a variante.  

Descrição — prefixo fixo em bold seguido da indicação de uso ("BEST FOR: REMOVING BUILD-UP"). Duas linhas, caixa alta, sem verbo de venda. As quatro indicações precisam ser diferentes — é o que faz a grade funcionar como ferramenta de escolha.  

CTA de produto — verbo genérico igual nos quatro. A diferenciação está no nome e na indicação, não no botão.  

CTA final — chamada da coleção ou da ocasião ("TREAT DAD"), não repete o verbo dos botões acima.  

Proibições: quatro indicações de uso iguais · preço em qualquer slot · botões de produto com rótulos diferentes entre si · desconto · descrição com verbo de venda · nome de produto em uma linha só quando cabe em duas.

## Design system

Container 600px fixo, borda 1px   
#000000 opcional (flag has_border). Raio de 100px nos botões (pílula) — variante com cantos arredondados nos botões e cantos vivos nos cards.  

Estrutura  

| # | Elemento | Padding-top | Dimensão |  
|---|---|---|---|  
| 1 | Título | 34px | 35/39px bold, caixa alta, 2 linhas, padding lateral 100px |  
| 2 | Produto 1 — foto à esquerda | 51px | Linha de 532px, padding lateral 33px |  
| 3 | Produto 2 — foto à esquerda | 25px | Linha de 532px |  
| 4 | Produto 3 — foto à direita | 35px | Linha de 532px |  
| 5 | Produto 4 — foto à direita | 25px | Linha de 532px |  
| 6 | CTA final | 39px | 525 × 56px, com 34px de respiro na base |  

O respiro de 35px antes do produto 3 é maior que os 25px dos demais: marca a virada do lado.  

Anatomia da linha de produto — duas colunas, 532px no total.  

| Coluna | Largura | Conteúdo |  
|---|---|---|  
| Imagem | 214px | Ativo de 214 × 271px com a foto e os fragmentos do contorno |  
| Texto | 318px | Borda de 1px em três lados, padding-top 47px |  

Bordas da coluna de texto: topo, direita e base quando a foto está à esquerda; topo, esquerda e base quando está à direita. Padding esquerdo de 23px nas linhas 1-2 e 30px nas linhas 3-4.  

Interior da coluna: nome 30/33px bold em 2 linhas · descrição 9px abaixo, 13/15px · botão 18px abaixo, 257 × 55px.  

Paleta — duas cores.  

| Papel | Hex (NOTICE) | Uso |  
|---|---|---|  
| Cor primária |  |  |  
| #28252B | Título, nome, descrição e o contorno dos cards |  |  
| Cor secundária |  |  |  
| #1E3344 | Fundo dos botões de produto e borda do CTA final |  |  

O fundo é branco. O label dos botões de produto é branco; o do CTA final é a cor primária. Não existe cor de acento — a cor vem das fotos.  

Tipografia. Principal: Arial → Helvetica em todos os slots. Título e nome em bold caixa alta; descrição em regular caixa alta a 13px, com o prefixo em bold; botões 22px bold com tracking +0.07em e text-indent compensando. Secundária não existe.  

Implementação. Botões com border-radius:100px exigem v:roundrect com arcsize="50%" no bloco MSO — sem isso, retângulo no Outlook. O CTA final usa strokecolor e strokeweight no VML para reproduzir o contorno. font-size:0;line-height:0 na célula da imagem. O ativo de imagem precisa sair do Figma com os fragmentos de contorno já desenhados — não existe forma de fechar a moldura por CSS quando a foto transborda. Hack u + .body .txt-blk travando   
#28252B.  

Tags: SECTION_TITLE, PRODUCT_N_IMAGE_URL, PRODUCT_N_IMAGE_ALT, PRODUCT_N_NAME, PRODUCT_N_DESCRIPTION, PRODUCT_N_CTA_URL, PRODUCT_CTA_LABEL, FINAL_CTA_LABEL, FINAL_CTA_URL.  

Erros que quebram o padrão: imagem sem os fragmentos de contorno · foto contida dentro do retângulo em vez de transbordar · borda nos quatro lados da coluna de texto · alternância em zigue-zague em vez de 2 + 2 · botões de produto com raio diferente do CTA final · rótulos de botão diferentes entre produtos · preço no card · CTA final sólido.

## Direção fotográfica

Proporção 4:5 — slot de 214 × 271px, ativo final 428 × 542px (2x). PNG ou JPG q80, < 130 KB por produto. Gerar em 4:5 na altura de 542px (434 × 542) e cortar 6px de largura.  

Regra crítica de montagem: o ativo entregue não é só a fotografia. Ele contém a foto do produto e os fragmentos da linha de contorno que fecham a moldura acima e abaixo da imagem, na cor primária e com 1px de espessura. Isso é feito no Figma, na exportação — nunca em CSS.  

Regra crítica de composição: a foto transborda o retângulo do lado externo. No ativo, isso significa que o produto ocupa a borda externa até o limite do quadro, sem margem.  

Composição. Alternar entre dois tipos ao longo dos quatro slots: packshot em cena (produto e embalagem sobre superfície neutra) e produto em uso (mão segurando, gesto de aplicação, parte do corpo). Nunca quatro do mesmo tipo — a grade fica monótona e a leitura desliza.  

Cenário e luz. Fundo liso em tom neutro quente ou cinza claro, sem cenário reconhecível. Luz difusa, sombras curtas. A paleta dos quatro ativos precisa ser coerente entre si: mesma temperatura de cor e mesmo tratamento.  

Produto. Rótulo legível quando é packshot; textura e cor em evidência quando é uso.  

Proibições: foto sem os fragmentos de contorno · margem entre a foto e a borda externa do quadro · fundo branco puro (some contra o container) · quatro fotos do mesmo tipo · texto/preço/selo queimado · cenário reconhecível · marca d'água.  

Adaptação por categoria — o par de tipos:  

| Categoria | Packshot em cena | Produto em uso |  
|---|---|---|  
| Cuidado pessoal | Kit e caixa abertos | Barra na mão, gesto de aplicação |  
| Beleza | Frascos agrupados | Textura na pele, aplicador |  
| Casa | Item sobre superfície | Item sendo usado no ambiente |  
| Pet | Embalagem e acessório | Produto no animal |  
| Ferramenta | Ferramenta e estojo | Ferramenta na mão em trabalho |  
| Papelaria | Conjunto disposto | Mão escrevendo ou usando |

---

HTML: [[_html/products-8a-quatro-recomendacoes.html]] · Seção: [[_products]] · Protocolo: [[_protocolo-de-selecao]]
