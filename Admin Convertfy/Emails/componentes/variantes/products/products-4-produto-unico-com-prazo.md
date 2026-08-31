---
tipo: componente
slug: products-4-produto-unico-com-prazo
secao: products
nome_no_banco: "produtos 4 - um produto"
variant_id: 7bd9e98b-f016-4495-8245-88df69b8f4e1
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [campanha-promocional]
momento_vetado: [carrinho-abandonado, checkout-abandonado, transacional, welcome-1, welcome-meio, welcome-tardio]

# --- eixos de ranking, na ordem do protocolo ---
objecao: [preco-valor]
registro: []
registro_vetado: [luxo]
paleta: [escuro-saturado, com-acento-definido]
papel_na_peca: [meio]

# --- requisitos duros (eliminam) ---
exige: [prazo-real]

# --- capacidade e composição ---
product_slots: 1
itens: { min: 1, max: 1 }
peso: { altura_px: 963, classe: medio, fonte: medido }
convivencia: []

# --- fios para o resto do vault ---
aprendizados: ["[[deadline-falso-queima-o-proximo]]"]
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: média
schema_campos: 10
status: aprovada
---

## Descrição curta

Bloco de oferta de produto único. Dois parágrafos explicam o que o produto é, um card mostra nome, preço antes e depois, e um selo circular carrega o prazo da promoção. Momento de uso: campanha de oferta com data-limite para produto de entrada — kit, starter pack, bundle — quando é preciso justificar antes de mostrar o preço.

## Descrição detalhada

Título em duas linhas, dois parágrafos de copy, um card de produto com selo sobreposto e o CTA.  

Quatro mecanismos definem a variante:  

O selo circular é 100% HTML e CSS, sem imagem. v:oval no bloco condicional do Outlook e border-radius de 69px nos demais clientes. O prazo é texto vivo — muda por campanha sem passar pelo design.  

O selo sangra para fora do card. Ele ocupa o canto superior direito e transborda a borda. É o que impede o card de parecer um bloco fechado e dá a leitura de adesivo colado.  

Setup longo, oferta curta. Dois parágrafos antes do card e nenhum texto de venda dentro dele. O card só tem nome, preço riscado, preço novo e a foto — a persuasão inteira já aconteceu acima.  

Preço antes e depois na mesma linha. Riscado em peso regular, novo em bold, separados por dois espaços não quebráveis. Sem etiqueta de percentual: a economia se lê pela diferença.

## Quando usar

Oferta com prazo para produto único de entrada: kit, starter pack, bundle, caixa de degustação.  
Alimentos, bebidas, suplementos, beleza, pet, assinatura — categorias com produto de entrada definido.  
Quando o produto precisa ser explicado antes de precificado — os dois parágrafos existem para isso.  
Quando há prazo real para colocar no selo.  
Quando a marca tem cor escura saturada e uma cor de destaque vibrante.

## Quando NÃO usar

Sem prazo real — o selo é o mecanismo central e prazo falso corrói confiança.  
Sem desconto — o par de preços fica vazio.  
Mais de um produto — a variante tem um card só; para várias opções, use uma grade.  
Produto autoexplicativo — os dois parágrafos ficam sobrando e o bloco alonga sem função.  
Carrinho, checkout, transacional, prova social, welcome.  
Marca de luxo: selo de prazo e preço riscado são registro promocional.

## Orientações de copy para a IA

Título — o que o produto entrega, em duas linhas, caixa mista. Fala do benefício ou da praticidade, não do preço.  

Copy 1 — o que é o produto e para quem. Uma frase, tom de conversa.  

Copy 2 — o que ele resolve na rotina, terminando em dois-pontos para emendar no card. É a ponte entre argumento e oferta.  

Nome do produto — nome comercial curto, bold.  

Preços — valor cheio riscado e valor promocional em bold. Sem "de/por", sem percentual, sem "economize".  

Selo — três linhas curtas: um rótulo em bold ("P.S.") e o prazo em duas linhas. Data explícita, nunca "por tempo limitado".  

CTA — chamada com urgência leve ligada à oferta, caixa alta.  

Proibições: percentual em qualquer slot · prazo vago no selo · texto de venda dentro do card · segundo produto · contagem regressiva além do selo · exclamação.

## Design system

Container 598px fixo. Raio de 14px no card, 69px no selo e 4px no CTA — três raios diferentes, cada um com função.  

Estrutura  

| # | Elemento | Padding-top | Dimensão |  
|---|---|---|---|  
| 1 | Título | 48px | 34/33px bold, tracking +0.05em, padding lateral 40px |  
| 2 | Copy 1 | 36px | 25/28px, padding lateral 85px |  
| 3 | Copy 2 | 20px | 25/28px, padding lateral 85px |  
| 4 | Card de produto | 92px | 351px de largura, raio 14px |  
| 5 | CTA | 48px | 368 × 59px, raio 4px, com 65px de respiro na base |  

Anatomia do card: faixa superior com duas colunas — nome e preços em 214px (padding 28px no topo e à esquerda) e o selo em 137px. Abaixo, a foto do produto de 292 × 332px, centralizada, com 1px acima e 37px de respiro na base.  

Selo: círculo de 137 × 137px, border-radius:69px, padding lateral de 14px, texto 20/21px centralizado em três linhas com mso-line-height-rule:exactly.  

Paleta — quatro cores.  

| Papel | Hex (SmoothieBox) | Uso |  
|---|---|---|  
| Cor primária |  |  |  
| #0D402F | Fundo da seção e todo o texto sobre o card |  |  
| Cor secundária |  |  |  
| #FAFCEE | Fundo do card e todo o texto sobre o fundo escuro |  |  
| Acento A |  |  |  
| #BAD432 | Fundo do selo e o preço riscado |  |  
| Acento B |  |  |  
| #CBD505 | Fundo do CTA |  |  

Os dois acentos são vizinhos na mesma família — não são cores opostas. O texto do selo e o do CTA usam a cor primária, nunca branco. O preço riscado usa o acento A: é o único lugar do bloco onde cor marca informação, não superfície.  

Pele alternativa (HTML base): fundo   
#B1B3B6, card   
#F2F2F2, selo e CTA pretos com texto branco, sem acentos. Usar quando a marca não tem par de cores vibrantes.  

Tipografia. Principal: Arial → Helvetica em todos os slots. Título bold com tracking positivo; copies regular; nome do produto e preço novo bold com tracking −0.03em; preço riscado regular com text-decoration:line-through; selo 20px com o rótulo em bold; CTA 24px bold. Secundária não existe.  

Implementação. O selo exige as duas versões: v:oval com fillcolor e v:textbox no bloco [if mso], e a tabela com border-radius no [if !mso]. Sem o VML, o Outlook renderiza quadrado — e um quadrado nesse canto quebra a leitura de adesivo. mso-line-height-rule:exactly no selo para o Outlook não esticar as três linhas. O CTA usa v:roundrect com arcsize="7%". &nbsp;&nbsp; entre os dois preços — margem inline não é confiável. background:#E8E8E8 na <img> como fallback de carregamento.  

Tags: SECTION_TITLE, SECTION_COPY_1, SECTION_COPY_2, PRODUCT_NAME, PRICE_OLD, PRICE_NEW, PRODUCT_IMAGE_URL, PRODUCT_IMAGE_ALT, BADGE_LABEL, BADGE_DEADLINE, CTA_LABEL, CTA_URL.  

Erros que quebram o padrão: selo como imagem · selo contido dentro do card, sem sangrar · selo quadrado no Outlook por falta do VML · texto de venda dentro do card · percentual ao lado dos preços · acentos de famílias opostas · texto branco no selo ou no CTA · segundo card · foto com fundo diferente do card.

## Direção fotográfica

7. Direção fotográfica  

Proporção 4:5 — slot de 292 × 332px, ativo final 584 × 664px (2x). PNG, < 160 KB. Gerar em 4:5 na altura de 664px (531 × 664) e ampliar para 584px de largura.  

Regra crítica: o fundo do ativo é a cor do card, chapado, não branco nem transparente. A foto tem que desaparecer dentro do card — qualquer diferença de tom cria um retângulo visível.  

Composição. Grade 2 × 2 dos itens que compõem o kit, cada um com a quantidade indicada ao lado em número grande. As embalagens são frontais, alinhadas, com o mesmo tamanho aparente. É inventário visual, não cena.  

Cenário e luz. Sem cenário. Cada embalagem recortada, sombra suave ou nenhuma. Luz frontal uniforme.  

Produto. Rótulos legíveis a 292px de largura — o que significa embalagem com nome curto e cor de fundo distinta entre os quatro itens. É a cor de cada sachê que diferencia os sabores.  

Números de quantidade. Fazem parte do ativo, não do HTML: ficam à esquerda de cada embalagem, na cor primária, em corpo grande.  

Proibições: fundo branco ou transparente · cena de uso · embalagens em tamanhos diferentes · sombra dura · quatro itens da mesma cor · texto além dos multiplicadores · marca d'água.  

Adaptação por categoria — o que compõe a grade:  

| Categoria | Itens |  
|---|---|  
| Alimentos / bebidas | Sachês ou embalagens de sabores diferentes |  
| Suplementos | Potes ou sticks da linha |  
| Beleza | Miniaturas do kit |  
| Pet | Sachês ou petiscos por sabor |  
| Casa | Refis ou aromas do conjunto |  
| Assinatura | Itens da caixa do mês |

---

HTML: [[_html/products-4-produto-unico-com-prazo.html]] · Seção: [[_products]] · Protocolo: [[_protocolo-de-selecao]]
