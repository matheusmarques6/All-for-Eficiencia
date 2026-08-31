---
tipo: componente
slug: hero-6-percentual-gigante
secao: hero
nome_no_banco: "welcome - hero section 6"
variant_id: 72c32ec8-bbd2-4d2c-a938-3c24b65848cd
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: []
momento_vetado: []

# --- eixos de ranking, na ordem do protocolo ---
objecao: []
registro: []
registro_vetado: []
paleta: []
papel_na_peca: []

# --- requisitos duros (eliminam) ---
exige: []

# --- capacidade e composição ---
product_slots: 0
itens: null
peso: null
convivencia: []

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: null
schema_campos: 9
status: aprovada
---

## Descrição curta

Primeiro e-mail da régua de boas-vindas em que o percentual de desconto é o maior elemento da peça. A foto de campanha ocupa o topo, uma caixa sólida com a oferta assenta na borda inferior dela, e a instrução de resgate fica numa área branca abaixo. Momento de uso: welcome #1 logo após o opt-in, quando o desconto é o argumento principal e a marca ainda precisa se apresentar visualmente.

## Descrição detalhada

Um bloco de 707px com imagem de fundo, seguido de uma área branca com a linha do cupom e o CTA. Saudação, wordmark e caixa do desconto são sobrepostos à imagem.  

Quatro mecanismos definem a variante:  

A caixa do desconto termina exatamente onde a imagem termina. A borda inferior da caixa e a borda inferior da foto coincidem — não há respiro entre elas nem sobreposição parcial. É o que costura o bloco fotográfico à área branca.  

O percentual é o maior elemento tipográfico da peça. 60px bold, maior que o wordmark. A hierarquia é invertida de propósito: a oferta domina a marca.  

Instrução e ação vivem fora da imagem. Linha do cupom e CTA ficam sobre branco, em texto vivo. Com imagem bloqueada, o e-mail perde a foto e a caixa mas mantém o caminho de conversão.  

O texto assenta sobre o sujeito, não sobre área vazia. Diferente das variantes de zona limpa, aqui a foto é ocupada de ponta a ponta e a legibilidade vem de a cena inteira ser monocromática — fundo e guarda-roupa na mesma cor.

## Quando usar

desconto de captação, quando o percentual é o argumento central.  
Moda, activewear, beachwear, beleza, acessório — categorias com foto de campanha em cor chapada.  
Quando a marca tem wordmark tipográfico que funciona em caixa alta com tracking largo.  
Quando existe foto monocromática (fundo e roupa na mesma família de cor) que aceita texto branco sobreposto sem área reservada.  
Quando o código é dinâmico e precisa aparecer em texto vivo.

## Quando NÃO usar

Foto com fundo variado ou contraste alto — sem monocromia, o texto sobre o sujeito some.  
Marca premium que não desconta — o percentual em 60px define a peça.  
Sem cupom.  
Carrinho, checkout, browse, transacional.  
Campanha sazonal ou lançamento — não há slot para tema.  
Quando a marca precisa que o nome apareça maior que a oferta.

## Orientações de copy para a IA

Saudação — "Welcome to" ou equivalente, uma linha, sem o nome da marca (ele vem no wordmark logo abaixo).  

Wordmark — nome da marca em caixa alta com tracking largo, em uma ou duas linhas. É ativo de marca, não copy livre.  

Caixa do desconto — três linhas fixas: eyebrow curto ("Enjoy"), o valor em bold e grande, e o rodapé com a condição ("your first order"). Nenhuma das três admite frase longa; a caixa é um cartaz, não um parágrafo.  

Linha do cupom — instrução com o código em bold e a condição de resgate. Fica fora da imagem, sobre branco.  

CTA — verbo + nome da marca ou da coleção. Não repetir o percentual: ele já é o maior elemento da peça.  

Proibições: percentual no CTA · contagem regressiva · brand story · segundo botão · frase longa em qualquer linha da caixa · nome da marca na saudação.

## Design system

Container 600px fixo, borda 1px   
#000000 opcional (flag has_border). Zero raio, zero sombra, zero gradiente.  

Estrutura  

| # | Elemento | Altura |  
|---|---|---|  
| 1 | Bloco com imagem de fundo | 707px |  
| 2 | Linha do cupom | 8px de respiro + 26px |  
| 3 | CTA | 20px de respiro + 63px |  
| 4 | Respiro final | 45px |  

Overlay sobre a imagem  

| Elemento | Padding-top | Dimensão |  
|---|---|---|  
| Saudação | 183px | 30/34px, padding lateral 24px |  
| Caixa do wordmark | 45px | 310 × 98px, borda 2px |  
| Caixa do desconto | 174px | 405px de largura, ~173px de altura |  

Interior da caixa do desconto: eyebrow 22/26px com 20px de padding superior · valor 60/72px bold · rodapé 22/28px com 27px de padding inferior.  

A soma dos paddings coloca a base da caixa em 707px — a mesma linha da base da imagem. Qualquer alteração nos espaçamentos acima quebra a ancoragem e precisa ser recalculada.  

Paleta — três cores.  

| Papel | Hex (ILUS Label) | Uso |  
|---|---|---|  
| Cor primária |  |  |  
| #7A0000 | Fundo — vem da foto, também background-color de fallback |  |  
| Cor secundária |  |  |  
| #EEE4DC | Fundo da caixa do desconto |  |  
| Acento |  |  |  
| #921B1C | O valor do desconto dentro da caixa |  |  

O CTA usa   
#393737 fixo em ambas as peles. Texto sobre a primária é branco; dentro da caixa, na cor primária escura, com o valor no acento. O acento é uma variação escura da primária — não uma cor complementar.  

Pele alternativa (HTML base): caixa do desconto   
#E0E0E0 com todo o texto em preto, sem cor de acento, wordmark dentro de caixa branca com borda de 2px.  

Tipografia. Principal: Arial → Helvetica em todos os slots. Saudação 30px regular · wordmark 49px com tracking −0.06em (na referência, tracking largamente positivo — ver seção 12) · valor do desconto 60px bold · demais slots 22px regular · CTA 22px regular com tracking +0.1em, caixa alta. Secundária não existe.  

Implementação. background no <td> + background-image inline + background-size:598px 707px, background-color na cor primária como fallback, bloco VML v:rect/v:fill type="frame" para Outlook. Linha do cupom e CTA fora do bloco de imagem, em <tr> próprios sobre branco. Botão bulletproof. Hack u + .body .txt-blk para o Gmail iOS.  

Tags: HERO_IMAGE_URL, WELCOME_EYEBROW, BRAND_NAME, OFFER_EYEBROW, OFFER_VALUE, OFFER_FOOTNOTE, COUPON_CODE, COUPON_HINT, CTA_LABEL, CTA_URL.  

Erros que quebram o padrão: respiro entre a base da caixa e a base da imagem · caixa do desconto ultrapassando a imagem · wordmark maior que o valor do desconto · foto com fundo de cor variada · percentual repetido no CTA · linha do cupom dentro do bloco de imagem · quarta cor · segundo botão · botão com raio.

## Direção fotográfica

Proporção 4:5 — slot de 598 × 707px, ativo final 1196 × 1414px (2x). JPG q80 ou WebP, < 280 KB, full-bleed. Gerar em 4:5 na largura de 1196px (1196 × 1495) e cortar 81px de altura pela base — essa faixa fica atrás da caixa do desconto.  

Regra crítica: a cena tem que ser monocromática — fundo e guarda-roupa na mesma família de cor, em tom escuro e saturado. Não existe área reservada para o texto: a legibilidade vem da uniformidade cromática da cena inteira. Cena com fundo variado ou contraste alto inviabiliza a variante.  

Composição. Uma figura ocupando o quadro inteiro, cortada pelo topo e pelas laterais. Pose de ação ou postura firme, olhar para a câmera ou fora dele. O sujeito preenche a peça — não há espaço negativo estrutural. Objeto de contexto (bola, prop de esporte, acessório) pode entrar por um canto inferior.  

Cenário e luz. Fundo chapado ou levemente vinhetado na cor da marca. Luz de estúdio direcional, contraste médio nas peles e baixo no fundo. Sem cenário reconhecível — a cor é o cenário.  

Produto. Vestido ou usado pela figura, na mesma cor do fundo. O produto se distingue por textura e recorte, não por contraste de cor.  

Proibições: fundo variado ou de ambiente · alto contraste na faixa central · texto/preço/selo queimado · packshot · vinheta pesada · marca d'água · cor de guarda-roupa fora da paleta.  

Adaptação por categoria — o que é a cena:  

| Categoria | Cena |  
|---|---|  
| Activewear | Figura em pose de esporte, prop da modalidade |  
| Moda | Figura em look completo, fundo na cor da peça |  
| Beachwear | Figura em pé, fundo chapado quente |  
| Beleza | Retrato de meio corpo, fundo na cor do produto |  
| Acessório | Figura com o acessório em destaque, mesma família de cor |  
| Lingerie | Figura em interior de tom único |

---

HTML: [[_html/hero-6-percentual-gigante.html]] · Seção: [[_hero]] · Protocolo: [[_protocolo-de-selecao]]
