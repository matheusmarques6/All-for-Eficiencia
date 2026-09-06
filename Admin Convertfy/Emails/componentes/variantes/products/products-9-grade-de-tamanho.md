---
tipo: componente
slug: products-9-grade-de-tamanho
secao: products
nome_no_banco: "produtos 9 - 4 produtos"
variant_id: 2f115df3-1ddd-4ca4-bb45-e3337cef5546
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [queima-de-estoque]
momento_vetado: [carrinho-abandonado, checkout-abandonado, transacional, welcome-1, welcome-meio, welcome-tardio]

# --- eixos de ranking, na ordem do protocolo ---
objecao: [disponibilidade-urgencia]
registro: []
registro_vetado: [premium-editorial]
paleta: []
papel_na_peca: [meio]

# --- requisitos duros (eliminam) ---
exige: [estoque-integrado, grade-de-tamanho-real]

# --- capacidade e composição ---
product_slots: 4
itens: { min: 4, max: 4 }
peso: { altura_px: 2974, classe: peca-inteira, fonte: medido }
convivencia: []

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: balanced
schema_campos: 14
status: aprovada
---

## Descrição curta

Bloco de urgência por estoque. Quatro produtos, cada um com foto, nome e uma grade de tamanhos que mostra quais ainda existem — os esgotados aparecem apagados. Momento de uso: e-mail de queima de estoque ou última chamada, quando o argumento não é desconto e sim disponibilidade.

## Descrição detalhada

Título e subtítulo, quatro blocos de produto alternando o lado da foto, e um CTA de contorno fechando.  

Quatro mecanismos definem a variante:  

A grade de tamanhos tem estado. Dez quadrados de 46 × 31px por produto; os disponíveis ficam brancos com borda clara, os esgotados ficam preenchidos em cinza com o texto apagado. É a única variante do arsenal que expõe estoque — e é isso que produz a urgência sem precisar de contagem regressiva.  

A foto ultrapassa o card em 25px em cima e embaixo. Foto de 348px contra card de 298px. O desencaixe é o que dá a leitura de camada, com a foto por cima e o card por baixo.  

Meia moldura no card. A foto tem raio nos quatro cantos; o card tem borda em três lados e raio só nos dois cantos externos. O lado que encosta na foto fica aberto — os dois se encaixam como peça única.  

Escassez sem desconto. Não há preço, percentual nem cupom. O que faz correr é ver dois tamanhos sobrando.

## Quando usar

Queima de estoque, última chamada, fim de coleção — quando o argumento é disponibilidade.  
Moda, calçado, acessório — categorias com grade de tamanho real.  
Quando existe integração de estoque e a grade pode refletir a verdade. Grade estática mentindo é o pior uso possível desta variante.  
Quando a marca tem quatro peças com estoque irregular: a variação entre os produtos é o que torna a grade convincente.  
Base já engajada, que reconhece as peças.

## Quando NÃO usar

Sem dado de estoque real — a grade vira decoração e o e-mail promete o que não pode cumprir.  
Produto sem tamanho — beleza, alimentos, casa; a grade não tem o que mostrar.  
Todos os tamanhos disponíveis — sem esgotados, a grade não gera urgência e o bloco fica sem função.  
Quando o argumento é preço — não há slot para valor.  
Carrinho, checkout, transacional, prova social, welcome.  
Marca premium: expor ruptura de estoque é registro de outlet.

## Orientações de copy para a IA

Título — a condição de escassez em duas palavras, caixa alta.  

Subtítulo — uma linha de aviso com tom de marca. É o único slot com liberdade de voz na peça.  

Nome do produto — nome comercial completo em duas linhas. Nomes autorais funcionam melhor aqui do que descritivos, porque não há descrição para complementar.  

Rótulo da grade — palavra fixa seguida de dois-pontos, igual nos quatro.  

CTA de produto — verbo genérico, igual nos quatro.  

CTA final — chamada da sale, mais longa que os anteriores e em contraste invertido.  

Proibições: preço, percentual ou cupom · contagem regressiva · descrição por produto · rótulos de CTA diferentes entre produtos · afirmação de escassez que o estoque não sustenta · quinto bloco.

## Design system

Container 600px fixo, borda 1px   
#000000 opcional (flag has_border). Raio de 16px na foto e nos cantos externos do card; CTAs com cantos vivos.  

Estrutura  

| # | Elemento | Padding-top | Dimensão |  
|---|---|---|---|  
| 1 | Título | 20px | 35/35px bold, caixa alta |  
| 2 | Subtítulo | 17px | 23/25px regular |  
| 3 | Bloco 1 — foto à esquerda | 57px | 522px, padding lateral 38px |  
| 4 | Bloco 2 — foto à direita | 49px | 522px |  
| 5 | Bloco 3 — foto à esquerda | 52px | 522px |  
| 6 | Bloco 4 — foto à direita | 77px | 522px |  
| 7 | CTA final | 74px | 350 × 55px, borda 2px, com 62px de respiro na base |  

Anatomia do bloco: foto de 221 × 348px com borda de 2px e raio 16px na coluna de 225px; card de 297px com padding vertical de 25px, fundo branco, borda de 2px em três lados e raio 16px nos dois cantos externos.  

Interior do card, padding de 30px no topo e 23px à esquerda (25px nos blocos espelhados): nome 25/26px bold em 2 linhas · rótulo 11px abaixo, 15/17px · grade 11px abaixo · CTA 25px abaixo, 252 × 55px · respiro final de 31px.  

Grade de tamanhos: duas fileiras de cinco células de 46 × 31px, gap de 5px entre colunas e 8px entre fileiras, largura total 250px. Disponível: fundo branco, borda 1px   
#E2E2E2, texto preto. Esgotado: fundo   
#E3E3E3, texto cinza claro.  

Paleta — três cores.  

| Papel | Hex (referência) | Uso |  
|---|---|---|  
| Cor primária |  |  |  
| #316D89 | Fundo da seção |  |  
| Cor secundária |  |  |  
| #FFFFFF | Fundo dos cards, título, subtítulo e CTA final |  |  
| Neutro de estado |  |  |  
| #E3E3E3 | Preenchimento dos tamanhos esgotados |  |  

Os CTAs de produto são pretos com label branco; o CTA final é branco com borda e label pretos. O contraste se inverte no último botão, como nas outras variantes de catálogo do arsenal.  

Pele alternativa (HTML base): fundo   
#BEBEBE, título e subtítulo pretos. Usar quando a marca não tem cor de fundo própria.  

Tipografia. Principal: Arial → Helvetica em todos os slots. Título 35px bold caixa alta; subtítulo 23px regular; nome 25px bold; rótulo e tamanhos 15px regular; CTAs 23px bold caixa alta. Secundária não existe.  

Implementação. O text-shadow do título não renderiza em Outlook nem em vários clientes — é ganho opcional, não pode ser o que garante legibilidade; o contraste do texto contra o fundo precisa funcionar sem ele. border-radius parcial no card degrada para retângulo no Outlook; a foto, por ser <img>, precisa sair do Figma com o raio e a borda de 2px já no arquivo. font-size:0;line-height:0 na célula da foto e em todos os espaçadores da grade. A grade é tabela de células com borda, nunca imagem — é ela que precisa mudar por produto e por reposição.  

Tags: PREHEADER, SECTION_TITLE, SECTION_SUBTITLE, PRODUCT_N_IMAGE_URL, PRODUCT_N_IMAGE_ALT, PRODUCT_N_NAME, PRODUCT_N_SIZES, SIZES_LABEL, PRODUCT_CTA_LABEL, PRODUCT_N_CTA_URL, FINAL_CTA_LABEL, FINAL_CTA_URL.  

Erros que quebram o padrão: grade com todos os tamanhos disponíveis · grade como imagem · grade estática que não reflete o estoque · foto sem raio e borda no arquivo · card com borda nos quatro lados · foto alinhada ao card em vez de ultrapassar · preço acrescentado · quinto bloco · CTA final sólido.

## Direção fotográfica

Proporção 2:3 — slot de 221 × 348px, ativo final 442 × 696px (2x). PNG, < 150 KB cada. Gerar em 2:3 na altura de 696px (464 × 696) e cortar 22px de largura.  

Regra crítica: o ativo sai com a borda de 2px e o raio de 16px já aplicados, porque border-radius em <img> não renderiza no Outlook. O fundo interno é claro e neutro, próximo do branco do card.  

Composição. Modelo real vestindo a peça, corpo parcial, cortado pelo topo e pela base. O enquadramento muda conforme o produto: meio corpo quando a peça é superior, corpo inteiro quando é vestido ou casaco, recorte de quadril quando é peça inferior. A peça sempre preenche o eixo central do quadro.  

Casting. Corpos variados entre os quatro blocos — é o que dá sentido à grade de tamanhos que vai até 5XL. Repetir o mesmo tipo físico nos quatro contradiz o argumento da seção.  

Cenário e luz. Estúdio, fundo claro liso, sem cenário. Luz difusa frontal, sombras suaves. Pose parada, olhar para a câmera ou levemente fora.  

Proibições: fundo escuro ou colorido · cenário reconhecível · foto sem borda e raio no arquivo · peça fora do eixo central · corpos idênticos entre os quatro blocos · texto/preço/selo queimado · marca d'água.  

Adaptação por categoria — o que é o enquadramento:  

| Categoria | Enquadramento |  
|---|---|  
| Peça superior | Meio corpo, do quadril ao topo da cabeça |  
| Vestido / casaco | Corpo quase inteiro, cortado nos pés |  
| Peça inferior | Recorte do quadril às coxas |  
| Calçado | Pernas e pés, do joelho para baixo |  
| Acessório | Recorte do corpo com o item em destaque |  
| Lingerie | Meio corpo, enquadramento fechado |  

Prompt para IA:  

Studio photograph of a model wearing [PRODUTO], [ENQUADRAMENTO: half  
body / almost full body cropped at the feet / hip-to-thigh crop], the  
garment filling the central axis of a tall frame, cropped by the top and  
bottom edges. Flat light neutral studio background close to white. Soft  
frontal diffused light, gentle shadows, still pose, looking at camera or  
slightly off. Body type distinct from the other products in the set. No  
setting, no props, no text, no logos, no price badges, no watermark.  
Aspect ratio 2:3. High resolution.  

Montagem final: aplicar borda de 2px preta e raio de 16px nos quatro cantos, no arquivo, e exportar a 442 × 696px.  

Checklist: borda e raio aplicados no arquivo · fundo claro próximo do branco do card · peça no eixo central · enquadramento adequado ao tipo de peça · corpos diferentes entre os quatro blocos · sem cenário e sem texto queimado · 442px de largura e < 150 KB.

---

HTML: [[_html/products-9-grade-de-tamanho.html]] · Seção: [[_products]] · Protocolo: [[_protocolo-de-selecao]]
