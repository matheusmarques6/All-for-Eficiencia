---
tipo: componente
slug: products-2-tres-ingredientes
secao: products
nome_no_banco: "produtos 2 - Three Ingredients. Zero Fillers"
variant_id: 8ef65206-2f01-408f-ab07-c17f57cc136c
ativa: true
dispositivo: mecanismo_apontado

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [consideracao]
momento_vetado: [carrinho-abandonado, checkout-abandonado, transacional]

# --- eixos de ranking, na ordem do protocolo ---
objecao: [composicao-formulacao]
registro: []
registro_vetado: []
paleta: []
papel_na_peca: [meio]

# --- requisitos duros (eliminam) ---
exige: [tres-provas-verificaveis, produto-com-composicao-relevante]
diretivas_de_imagem: [corredores-livres-nas-laterais]

# --- capacidade e composição ---
product_slots: 0
itens: { min: 3, max: 3 }
peso: { altura_px: 716, classe: medio, fonte: medido }
convivencia: []

# --- fios para o resto do vault ---
aprendizados: ["[[titulos-precisam-carregar-o-argumento]]"]
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: null
schema_campos: 6
status: aprovada
---

## Descrição curta

Bloco de educação sobre composição. Uma foto do produto ocupa o centro e três marcadores apontam para o que ele tem dentro — ingrediente, origem, certificação — encerrando com um CTA. Momento de uso: consideração ou e-mail de USP, quando a objeção é "o que exatamente tem nisso" e a resposta é a formulação.

## Descrição detalhada

Headline em três linhas; abaixo, uma faixa de 494px com a foto do produto como imagem de fundo e três marcadores sobrepostos; no fim, o CTA.  

Quatro mecanismos definem a variante:  

Os marcadores são HTML, não infográfico queimado na imagem. Cada um é um pino circular de 31px com sinal de mais, mais um rótulo de 199 × 56px logo abaixo — tabelas com fundo, borda e raio. O texto é vivo, traduzível e trocável sem refazer arte.  

Alternância esquerda / direita / esquerda. O produto fica no eixo central e os marcadores se distribuem em zigue-zague pelas laterais. É o que impede a leitura de virar lista.  

Cada rótulo cita uma prova verificável. Certificação, origem geográfica, grau ou ausência de algo. Não é benefício — é composição.  

A headline é um manifesto de três linhas curtas. Cada linha termina em ponto. A cadência entrecortada é o registro da variante; frase corrida derruba o efeito.

## Quando usar

Consideração e e-mail de USP, quando o argumento é formulação, material ou origem.  
Skincare, suplementos, alimentos, bebidas, limpeza, pet — categorias com rótulo e certificação.  
Quando existem três provas verificáveis distintas para apontar.  
Quando o produto é fotografável em plano único com o rótulo legível.  
Quando a marca quer texto vivo em vez de infográfico — traduzível para várias lojas.

## Quando NÃO usar

Sem provas verificáveis — três marcadores com adjetivo genérico ("suave", "poderoso") esvaziam o bloco.  
Produto sem composição relevante — moda, acessório, eletrônico de consumo.  
Foto sem corredores livres nas laterais — os rótulos caem sobre o produto e nada fica legível.  
Carrinho, checkout, transacional, topo de e-mail.  
Mais de três provas — a faixa de 494px não comporta um quarto marcador sem apertar.  
Quando a marca prefere entregar o infográfico como imagem única: aí o bloco perde a razão de existir.

## Orientações de copy para a IA

Headline — três linhas curtas, caixa alta, cada uma terminando em ponto. Estrutura recomendada: quantidade → o que tem → o que não tem ("THREE INGREDIENTS. ZERO FILLERS."). A negação na última linha é o que fecha o argumento.  

Rótulos dos marcadores — cada um em duas linhas, caixa mista. Citar prova concreta: selo de certificação, origem geográfica, grau de qualidade, ausência declarada. Um por marcador, nunca repetir a mesma categoria de prova nos três.  

CTA — verbo + benefício, caixa alta ("NOURISH YOUR SKIN"). Diferente das variantes de catálogo, aqui o botão fala do resultado, não da compra.  

Proibições: adjetivo genérico no lugar de prova · claim de saúde não sustentado · três marcadores da mesma categoria · headline em frase corrida · desconto ou cupom · segundo botão · rótulo em uma linha só.

## Design system

Container 600px fixo, borda 1px   
#000000 opcional (flag has_border). Raio de 16px no pino, 5px no rótulo e 100px no CTA.  

Estrutura  

| # | Elemento | Padding-top | Dimensão |  
|---|---|---|---|  
| 1 | Headline | 46px | 50/50px bold, tracking +0.03em, caixa alta, 3 linhas, padding lateral 54px |  
| 2 | Faixa da foto com marcadores | 0 | 598 × 494px |  
| 3 | CTA | 52px | 418 × 59px, com 66px de respiro na base |  

Posição dos marcadores dentro da faixa  

| Marcador | Alinhamento | Padding |  
|---|---|---|  
| 1 | Esquerda | 45px topo · 31px esquerda |  
| 2 | Direita | 50px topo · 15px direita |  
| 3 | Esquerda | 78px topo · 31px esquerda · 60px base |  

Anatomia do marcador: pino de 31 × 31px com borda de 1px e raio 16px, contendo um + de 21px; abaixo dele, rótulo de 199 × 56px com borda de 1px, raio 5px, texto 15/15px centralizado em duas linhas.  

Paleta — quatro cores.  

| Papel | Hex (Shelter Skin) | Uso |  
|---|---|---|  
| Cor primária |  |  |  
| #28100E | Headline e fundo do CTA |  |  
| Cor secundária |  |  |  
| #EEE6E0 | Fundo da seção — vem da foto |  |  
| Marcador A |  |  |  
| #B3CFEC | Fundo dos marcadores 1 e 3 |  |  
| Marcador B |  |  |  
| #FFE1A0 | Fundo do marcador 2 |  |  

O CTA usa a cor primária, não preto puro. As duas cores de marcador são pastéis de famílias opostas — uma fria, uma quente — e o pino acompanha a cor do rótulo. O texto dentro dos marcadores é sempre preto com borda de 1px preta.  

Pele alternativa (HTML base): os três marcadores em   
#D1D1D1, CTA preto. Usar quando a marca não tem par de pastéis definido.  

Tipografia. Principal: Arial → Helvetica em todos os slots. Headline 50px bold caixa alta; rótulos 15px regular com tracking +0.03em; CTA 23px bold com tracking +0.07em e text-indent compensando. Secundária não existe.  

Implementação. background no <td> + background-image inline + background-size:598px 494px, background-color na cor secundária como fallback, bloco VML v:rect/v:fill type="frame" para Outlook. Pino e rótulo com border-radius degradam para retângulo no Outlook — degradação aceita, o marcador continua legível. O CTA exige v:roundrect com arcsize="50%". font-size:0;line-height:0 nas células que só contêm o pino. Hacks u + .body .txt-prim e u + .body .txt-blk.  

Tags: PREHEADER, HEADLINE_L1, HEADLINE_L2, HEADLINE_L3, PRODUCT_IMAGE_URL, MARKER_1_LABEL, MARKER_2_LABEL, MARKER_3_LABEL, CTA_LABEL, CTA_URL.  

Erros que quebram o padrão: marcadores queimados na imagem · rótulo sobre o produto em vez do corredor lateral · pino descolado do rótulo · três marcadores do mesmo lado · pino em cor diferente do rótulo · quarto marcador · headline em frase corrida · CTA em preto puro quando a marca tem cor primária.

## Direção fotográfica

7. Direção fotográfica  

Proporção 5:4 — slot de 598 × 494px, ativo final 1196 × 988px (2x). JPG q80 ou WebP, < 220 KB, full-bleed. Gerar em 5:4 na altura de 988px (1235 × 988) e cortar 39px de largura, 20px de cada lado.  

Regra crítica: a foto precisa de três corredores laterais livres, nas alturas em que os marcadores caem — dois à esquerda (topo e base) e um à direita (meio). Cada corredor tem cerca de 230px de largura por 90px de altura. Produto, mão ou sombra dura nessas áreas tornam o rótulo ilegível.  

Composição. Produto único no eixo central vertical, ocupando a faixa do meio de ponta a ponta. Segurado por uma mão que entra pela base, ou apoiado — em qualquer caso, o conjunto não invade os corredores. Rótulo do produto legível e voltado para a câmera.  

Cenário e luz. Fundo liso em tom neutro quente, sem textura forte. Luz difusa frontal, sombras suaves. O fundo é a cor secundária da peça e precisa ser uniforme o bastante para virar background-color de fallback.  

Produto. Em destaque, com detalhe de textura ou material visível — gota escorrendo, brilho do vidro, grão. É a prova visual do que os marcadores afirmam.  

Proibições: produto fora do eixo central · elemento nos corredores dos marcadores · fundo com padrão ou cenário reconhecível · texto ou selo queimado · sombra dura nas laterais · packshot recortado sem contexto de mão · marca d'água.  

Adaptação por categoria — o que é o plano central:  

| Categoria | Plano |  
|---|---|  
| Skincare | Frasco na mão, gota escorrendo |  
| Suplementos | Pote em pé, cápsulas ou pó ao lado |  
| Alimentos | Embalagem em pé, ingrediente cru na base |  
| Bebidas | Garrafa ou lata em pé, condensação visível |  
| Limpeza | Frasco em uso, superfície ao fundo |  
| Pet | Embalagem em pé, ração ou petisco em detalhe |

---

HTML: [[_html/products-2-tres-ingredientes.html]] · Seção: [[_products]] · Protocolo: [[_protocolo-de-selecao]]
