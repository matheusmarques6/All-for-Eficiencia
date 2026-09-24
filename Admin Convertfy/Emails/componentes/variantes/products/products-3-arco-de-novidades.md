---
tipo: componente
slug: products-3-arco-de-novidades
secao: products
nome_no_banco: "produtos 3 - grid 4 produtos"
variant_id: a15a6331-8761-4025-8d70-574c18fcd40b
ativa: true
dispositivo: lineup_de_colecao

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [lancamento]
momento_vetado: [carrinho-abandonado, checkout-abandonado, transacional]

# --- eixos de ranking, na ordem do protocolo ---
objecao: [amplitude-de-catalogo]
registro: []
registro_vetado: []
paleta: [escuro-saturado]
papel_na_peca: [meio]

# --- requisitos duros (eliminam) ---
exige: []
diretivas_de_imagem: [foto-de-campanha-propria]

# --- capacidade e composição ---
product_slots: 1
itens: { min: 4, max: 4 }
peso: { altura_px: 1359, classe: pesado, fonte: medido }
convivencia: []

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: minimal
schema_campos: 9
status: aprovada
---

## Descrição curta

Bloco de anúncio de novidades. Uma foto de campanha recortada em arco ocupa o centro e uma lista de quatro linhas enumera o que entrou na coleção — sem preço, sem foto por item e sem botão individual. Momento de uso: campanha de lançamento ou reposição para base já engajada, quando basta contar o que chegou e mandar para a coleção inteira.

## Descrição detalhada

Título em duas linhas; abaixo, a foto em arco; depois, uma faixa de 290px com quatro linhas de novidade sobre uma imagem de folhagem; no fim, o CTA.  

Quatro mecanismos definem a variante:  

O arco é recorte do ativo, não CSS. Não existe border-radius que produza arco em cliente de e-mail. A foto sai do Figma já mascarada, com o fundo da peça preenchendo os cantos superiores.  

A lista não tem CTA por item. É informe, não catálogo. Quatro linhas de ícone e texto, um único botão no fim apontando para a coleção. Colocar botão por linha transforma o bloco em grade de produtos e muda a intenção.  

Duas cores e nada mais. Fundo escuro saturado e creme. O CTA é creme com texto no fundo — não há terceira cor, nem no ícone, nem no texto.  

Tracking largo como assinatura. Título e CTA com letter-spacing de 0.25em e text-indent compensando. É o que dá o registro editorial sem precisar de segunda família tipográfica.

## Quando usar

Moda, beachwear, joia, casa, beleza — categorias com variação de cor e modelo.  
Quando há quatro novidades que se explicam em uma frase cada.  
Quando a marca tem cor escura saturada de identidade e fotografia de campanha própria.  
Quando o destino é a coleção inteira, não produtos individuais.

## Quando NÃO usar

Quando cada item precisa de destino próprio — use uma grade de produtos com CTA por linha.  
Sem foto de campanha — a variante é 60% imagem.  
Base fria ou primeiro contato — não há apresentação de marca nem oferta.  
Mais de quatro novidades — a faixa de 290px não comporta a quinta linha.  
Carrinho, checkout, transacional, prova social.  
Quando a marca é clara: a peça depende do contraste creme sobre escuro.

## Orientações de copy para a IA

Título — duas linhas, caixa alta, anunciando a natureza da novidade ("NEW COLORS & SOULFUL EXTRAS"). Sem percentual, sem urgência, sem nome de produto.  

Linhas da lista — uma novidade por linha, em caixa mista, no formato produto + o que mudou. Citar a cor, a variação ou a quantidade nova. Máximo duas linhas de texto cada. Tom de conversa; reticências e prévias do que vem depois são bem-vindas.  

CTA — chamada para explorar a coleção, caixa alta com tracking largo. Sem verbo de compra direta e sem percentual.  

Proibições: preço em qualquer linha · desconto ou cupom · urgência · botão por item · quinta linha · nome da marca no título · exclamação em mais de uma linha.

## Design system

Container 600px fixo, sem borda. Zero raio, zero sombra, zero gradiente. Preheader oculto obrigatório.  

Estrutura  

| # | Elemento | Padding-top | Dimensão |  
|---|---|---|---|  
| 1 | Título | 33px | 32/35px, tracking +0.25em, caixa alta, 2 linhas, padding lateral 60px |  
| 2 | Foto em arco | 56px | 420 × 510px, centralizada |  
| 3 | Faixa de novidades | 0 | 600 × 290px, com imagem de folhagem ao fundo |  
| 4 | CTA | 31px | 381 × 54px, com 31px de respiro na base |  

Interior da faixa de novidades: bloco de 466px com padding de 28px no topo e 134px à esquerda. Cada linha é ícone de 20 × 20px · espaçador de 10px · texto 22/27px. Entre as linhas, 47px.  

Paleta — duas cores.  

| Papel | Hex (referência) | Uso |  
|---|---|---|  
| Cor primária |  |  |  
| #5B1724 | Fundo de toda a peça |  |  
| Cor secundária |  |  |  
| #F7F1ED | Título, texto das novidades, ícones e fundo do CTA |  |  

O label do CTA usa a cor primária sobre o creme. Não existe cor de acento: o único ponto de cor da peça é a fotografia.  

Pele alternativa (HTML base): fundo   
#000000 com o mesmo creme. Usar quando a marca não tem cor escura saturada própria.  

Tipografia. Principal: Proxima Nova → Arial → Helvetica em todos os slots. Título 32px regular caixa alta com tracking +0.25em; novidades 22px regular caixa mista sem tracking; CTA 18px bold caixa alta com tracking +0.25em. Secundária não existe — a diferenciação é toda por tracking e caixa.  

Implementação. Fonte web não renderiza em Outlook nem em boa parte do Gmail: testar a degradação para Arial no título, que é onde o tracking largo mais altera a largura. background no <td> da faixa de novidades + background-image inline + background-size:600px 290px, com background-color na cor primária como fallback e bloco VML v:rect/v:fill type="frame" para Outlook. text-indent igual ao letter-spacing para compensar o espaço extra no fim da linha. font-size:0;line-height:0 nas células de ícone e espaçador. Hack u + .body .txt-creme travando o creme sobre o escuro no dark mode.  

Tags: PREHEADER, SECTION_TITLE, ARCH_IMAGE_URL, ARCH_IMAGE_ALT, FOLIAGE_IMAGE_URL, FEATURE_ICON_URL, FEATURE_1_TEXT, FEATURE_2_TEXT, FEATURE_3_TEXT, FEATURE_4_TEXT, CTA_LABEL, CTA_URL.  

Erros que quebram o padrão: tentar produzir o arco por CSS · fundo do arco diferente da cor primária · CTA por linha de novidade · terceira cor · ícones diferentes entre as linhas · tracking no texto das novidades · quinta linha · botão com raio · faixa de folhagem sem background-color de fallback.

## Direção fotográfica

Foto em arco  

Proporção 4:5 — slot de 420 × 510px, ativo final 840 × 1020px (2x). PNG, < 260 KB. Gerar em 4:5 na altura de 1020px (816 × 1020) e ampliar para 840px de largura.  

Regra crítica: o ativo sai já mascarado em arco — topo semicircular, laterais retas, base reta — com os cantos superiores preenchidos na cor primária da peça. Não é PNG transparente: a transparência não é confiável em Outlook, então o fundo vai chapado no arquivo.  

Composição. Uma ou duas figuras em pé, corpo inteiro, centralizadas no eixo do arco, com folga acima da cabeça para o topo curvo não cortar. Pose relaxada, olhar para a câmera. Cenário arquitetônico com profundidade — porta, parede, vão.  

Cenário e luz. Luz natural quente, sombras suaves, paleta terrosa. Vegetação real na cena, em uma das laterais. O cenário precisa ter contraste tonal com a cor primária da peça — arco escuro sobre fundo escuro desaparece.  

Produto. Vestido pelas figuras, em cor que se destaque do cenário. As novidades citadas na lista precisam estar visíveis na foto.  

Proibições: cabeça encostando no topo curvo · figura fora do eixo do arco · fundo transparente no PNG · cenário de estúdio · texto queimado · marca d'água.  

Folhagem de fundo das novidades  

Proporção 2:1 — slot de 600 × 290px, ativo final 1200 × 580px (2x). PNG com o fundo já na cor primária, < 120 KB.  

Ideia: ramo de folhagem entrando pelo canto inferior esquerdo, ocupando no máximo 130px de largura — o texto começa em 134px e não pode ser tocado. Resto do quadro chapado na cor primária. Folhagem em verde natural, iluminada como se pertencesse à mesma cena da foto em arco.  

Adaptação por categoria — o que é a cena do arco:  

| Categoria | Cena |  
|---|---|  
| Beachwear / resort | Duplas em vão de porta, parede e vegetação |  
| Moda | Figura em pé em cenário arquitetônico |  
| Joia | Busto e mãos, parede texturizada ao fundo |  
| Casa | Ambiente vivido enquadrado pelo arco |  
| Beleza | Retrato de meio corpo, luz de janela |  
| Infantil | Criança em cena de brincadeira, cenário real |

---

HTML: [[_html/products-3-arco-de-novidades.html]] · Seção: [[_products]] · Protocolo: [[_protocolo-de-selecao]]
