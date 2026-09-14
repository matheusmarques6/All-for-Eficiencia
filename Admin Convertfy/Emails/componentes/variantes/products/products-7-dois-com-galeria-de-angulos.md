---
tipo: componente
slug: products-7-dois-com-galeria-de-angulos
secao: products
nome_no_banco: "produtos 7 - dois produtos"
variant_id: cee34b0a-030c-43df-93b6-c54de6f00569
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [lancamento]
momento_vetado: [carrinho-abandonado, checkout-abandonado, transacional]

# --- eixos de ranking, na ordem do protocolo ---
objecao: [qualidade-eficacia]
registro: []
registro_vetado: [volume-impulso]
paleta: []
papel_na_peca: [meio]

# --- requisitos duros (eliminam) ---
exige: [acervo-por-angulo, colecao-ou-kit]

# --- capacidade e composição ---
product_slots: 2
itens: { min: 2, max: 2 }
peso: { altura_px: 3298, classe: peca-inteira, fonte: medido }
convivencia: []

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: null
schema_campos: 16
status: aprovada
---

## Descrição curta

Bloco de apresentação profunda de produto. Dois produtos, cada um em um painel com foto grande, três miniaturas de outros ângulos, uma frase técnica e botão próprio, fechando com um CTA de coleção. Momento de uso: lançamento ou destaque de coleção, quando o leitor precisa ver o produto de vários ângulos antes de clicar.

## Descrição detalhada

Dois painéis cinza empilhados, cada um seguido do seu CTA, e um terceiro botão apontando para a coleção.  

Quatro mecanismos definem a variante:  

Galeria de ângulos, não de produtos. As três miniaturas são o mesmo item visto de outra forma — frente, costas, detalhe em uso. Colocar produtos diferentes ali transforma o painel em grade e destrói o argumento de profundidade.  

Espelhamento completo entre os dois blocos. No bloco 1 a foto grande fica à esquerda e a copy alinha à direita; no bloco 2 tudo inverte, inclusive o text-align da copy. O alinhamento do texto acompanha o lado — é o detalhe que faz o espelho parecer intencional.  

O CTA fica fora do painel. Cada botão tem 556px e encosta na base do painel cinza, sem entrar nele. É o que separa "conteúdo do produto" de "ação".  

Três botões, com o último em peso menor. Dois CTAs sólidos de produto e um terceiro, mais claro, para a coleção. A hierarquia é de contraste, não de tamanho — os três têm a mesma largura.

## Quando usar

Lançamento ou destaque de coleção com dois produtos que merecem apresentação individual.  
Moda, uniformes, activewear, calçado, casa, acessório — categorias em que caimento e detalhe de acabamento importam.  
Quando existe acervo de fotos por ângulo do mesmo item: frente, costas, detalhe.  
Quando cada produto tem página própria e existe uma coleção que os agrupa.  
Quando a marca vende variação de cor: os dois blocos podem mostrar a mesma peça em cores diferentes.

## Quando NÃO usar

Sem acervo de ângulos — três miniaturas com a mesma foto recortada denunciam a montagem.  
Produtos que não compartilham coleção — o CTA final fica sem destino coerente.  
Mais de dois produtos — o padrão é profundidade, não amplitude; para amplitude, use uma grade.  
Produto sem variação visual — se frente e costas são iguais, as miniaturas não acrescentam.  
Carrinho, checkout, transacional, prova social.  
Ticket baixo e compra por impulso: o volume de imagem é desproporcional à decisão.

## Orientações de copy para a IA

Título — linha de família ou atributo do produto, curta. É o mesmo nos dois blocos quando eles são variações da mesma peça.  

Subtítulo — nome do modelo ou tipo, em corpo menor. Título e subtítulo formam o nome completo lido em duas linhas.  

Copy — uma frase técnica sobre material, construção ou caimento, e o que isso entrega em uso. Quatro a cinco linhas. As duas copies precisam falar de aspectos diferentes — uma do material, outra do corte; repetir o argumento desperdiça o segundo bloco.  

CTA de produto — verbo genérico, igual nos dois.  

CTA final — nomeia a coleção ou a ocasião, mais longo que os anteriores. É o que justifica ele existir depois de dois botões.  

Proibições: preço em qualquer slot · copies com o mesmo argumento · título e subtítulo diferentes entre blocos quando o produto é o mesmo · rótulos de CTA de produto diferentes entre si · desconto · terceiro bloco.

## Design system

Container 600px fixo, borda 1px   
#000000 opcional (flag has_border). Zero raio, zero sombra, zero gradiente.  

Estrutura  

| # | Elemento | Padding do bloco | Dimensão |  
|---|---|---|---|  
| 1 | Painel 1 — foto grande à esquerda | 26px topo · 21px direita · 19px esquerda | 558px |  
| 2 | CTA 1 | 27px topo · 21px laterais | 556 × 58px |  
| 3 | Painel 2 — foto grande à direita | 41px topo · 21px direita · 19px esquerda | 558px |  
| 4 | CTA 2 | 21px topo · 21px laterais | 556 × 58px |  
| 5 | CTA final | 47px topo · 49px base | 556 × 58px |  

Interior do painel — padding de 39px no topo (40px no painel 2), 27px à esquerda e 15px à direita; tabela interna de 516px em duas colunas.  

| Coluna | Largura | Conteúdo |  
|---|---|---|  
| Grande | 314px | Título 25/29px · subtítulo 5px abaixo, 18/21px · foto 314 × 733px, 37px abaixo |  
| Galeria | 202px | Três fotos de 160 × 182px com gaps de 7px e 9px · copy 47px abaixo, 18/27px |  

Padding da coluna de galeria: 41px à esquerda no painel 1; 42px à direita no painel 2. A copy alinha à direita no painel 1 e à esquerda no painel 2.  

Paleta — três cores.  

| Papel | Hex (referência) | Uso |  
|---|---|---|  
| Cor primária |  |  |  
| #DBDBDB | Fundo dos painéis |  |  
| Cor secundária |  |  |  
| #6B906E | Fundo dos CTAs de produto, com label branco |  |  
| Neutro de texto |  |  |  
| #373737 | Título e subtítulo — cinza, nunca preto |  |  

A copy usa preto puro; título e subtítulo usam o cinza. A diferença de valor é o que separa identificação de argumento. O CTA final é branco com label escuro — contraste invertido em relação aos outros dois.  

Pele alternativa (HTML base): CTAs de produto pretos e CTA final   
#BEBEBE com label branco. Usar quando a marca não tem cor própria.  

Tipografia. Principal: Arial → Helvetica em todos os slots. Título 25px regular com tracking +0.05em; subtítulo 18px regular com o mesmo tracking; copy 18/27px regular sem tracking; CTAs 25px bold com tracking +0.15em e text-indent compensando. Secundária não existe.  

Implementação. Todas as fotos são <img> com display:block e background:#EFEFEF como fallback; nenhuma é background-image. font-size:0;line-height:0 em todas as células e <div> que contêm só imagem — com oito imagens no bloco, um gap de Outlook em cada uma desalinharia a galeria inteira. Os gaps de 7px e 9px entre as miniaturas são desiguais de propósito e vêm do arquivo original; padronizá-los muda a altura total da coluna. Hacks u + .body .txt-gry e u + .body .txt-blk.  

Tags: PANEL_N_TITLE, PANEL_N_SUBTITLE, PANEL_N_COPY, PANEL_N_MAIN_IMAGE_URL, PANEL_N_THUMB_A_URL, PANEL_N_THUMB_B_URL, PANEL_N_THUMB_C_URL, PRODUCT_CTA_LABEL, PANEL_N_CTA_URL, FINAL_CTA_LABEL, FINAL_CTA_URL.  

Erros que quebram o padrão: miniaturas com produtos diferentes · copy com o mesmo alinhamento nos dois painéis · CTA dentro do painel · CTA final com o mesmo peso dos de produto · título em preto puro · gaps das miniaturas padronizados · imagem sem font-size:0 na célula · terceiro painel.

## Direção fotográfica

Dois tamanhos de slot, com proporções diferentes.  

| Slot | Proporção | Slot em px | Ativo final |  
|---|---|---|---|  
| Foto grande | 9:16 | 314 × 733 | 628 × 1466 (2x) |  
| Miniatura | 4:5 | 160 × 182 | 320 × 364 (2x) |  

PNG ou JPG q80. Foto grande < 220 KB; miniaturas < 90 KB cada.  

A foto grande é mais estreita que 9:16: gere em 9:16 na altura de 1466px (825 × 1466) e corte 197px de largura, 98px de cada lado. A miniatura: gere em 4:5 na altura de 364px (291 × 364) e amplie para 320px.  

Regra crítica: o fundo de todos os oito ativos é o mesmo cinza do painel, chapado. Nenhum deles tem moldura, então qualquer diferença de tom desenha retângulos dentro do painel.  

Composição da foto grande. Modelo em meio corpo, de frente, cortado pelo topo e pela base do quadro. Enquadramento estreito e alto — o produto ocupa a largura toda. Olhar para a câmera, pose parada.  

Composição das miniaturas. Três ângulos do mesmo item e da mesma cor: detalhe lateral ou de acabamento, costas em corpo inteiro, e o produto em uso mostrando a parte que a foto grande não mostra (calça, calçado, movimento). A ordem importa — do mais fechado ao mais aberto, de cima para baixo.  

Luz e cenário. Estúdio, fundo liso, sem cenário. Luz difusa frontal, sombras suaves. Os oito ativos precisam da mesma temperatura de cor e do mesmo tratamento — eles aparecem lado a lado.  

Entre os dois painéis. Modelo diferente e cor diferente do produto, mantendo o mesmo enquadramento e a mesma luz. É o que faz os dois blocos lerem como variações e não como peças distintas.  

Proibições: fundo branco ou colorido · cenário reconhecível · miniaturas de produtos diferentes · miniatura repetindo o ângulo da foto grande · sombra dura · texto/preço/selo queimado · modelos com poses muito diferentes entre os painéis · marca d'água.  

Adaptação por categoria — o que são os três ângulos:  

| Categoria | Miniaturas |  
|---|---|  
| Uniforme / activewear | Detalhe lateral, costas, calça e calçado |  
| Moda | Detalhe de tecido, costas, look completo |  
| Calçado | Solado, perfil, pé calçado em movimento |  
| Casa | Detalhe de material, item completo, item em uso |  
| Acessório | Fecho ou aviamento, verso, uso no corpo |  
| Bolsa | Interior, verso, uso a tiracolo |

---

HTML: [[_html/products-7-dois-com-galeria-de-angulos.html]] · Seção: [[_products]] · Protocolo: [[_protocolo-de-selecao]]
