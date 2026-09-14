---
tipo: componente
slug: products-8b-grade-3x3
secao: products
nome_no_banco: "produtos 8 - 9 produtos"
variant_id: 9c00bf11-22e4-4675-98aa-499aee857d7d
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [catalogo-mais-vendidos]
momento_vetado: []

# --- eixos de ranking, na ordem do protocolo ---
objecao: [amplitude-de-catalogo]
registro: []
registro_vetado: []
paleta: []
papel_na_peca: [apoio, fecha]

# --- requisitos duros (eliminam) ---
exige: []
diretivas_de_imagem: []

# --- capacidade e composição ---
product_slots: 9
itens: { min: 6, max: 9 }
peso: { altura_px: 3071, classe: peca-inteira, fonte: medido }
convivencia: [exige-hero-ou-contexto-acima]

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: rich
schema_campos: 29
status: aprovada
---

## Descrição curta

Bloco de catálogo amplo. Nove produtos em grade regular, cada um com foto, nome e botão próprio, sem preço e sem descrição. Momento de uso: e-mail de catálogo, mais vendidos ou coleção completa, quando o leitor já conhece a marca e precisa escolher entre muitas variações — tipicamente de aroma, sabor ou cor.

## Descrição detalhada

Título, duas linhas de copy e três fileiras de três produtos.  

Quatro mecanismos definem a variante:  

Amplitude máxima, profundidade mínima. Nove produtos e nenhum tem descrição, preço ou selo. Só foto, nome e botão. É o oposto das variantes de painel: aqui o bloco não convence, apenas apresenta o cardápio.  

Nove botões, nenhum de coleção. Cada produto leva ao seu destino e não existe CTA final. Quem chega ao fim da grade sem clicar já viu tudo que havia.  

Ênfase por sublinhado. A copy usa text-decoration:underline em uma palavra por linha. É o único recurso de ênfase da peça — não há bold, não há cor, não há tamanho diferente.  

A grade só funciona com nomes do mesmo tamanho. Nome de uma linha numa coluna e de duas em outra desalinha os botões da fileira. A célula do nome precisa de altura fixa de 50px, equivalente a duas linhas.

## Quando usar

Catálogo, mais vendidos, coleção completa para base que já conhece a marca.  
Beleza, suplementos, alimentos, bebidas, papelaria, pet — categorias com muitas variações do mesmo produto.  
Quando a diferença entre os itens é visual e imediata: aroma, sabor, cor, fragrância.  
Quando cada produto tem página própria.  
Quando existe hero ou contexto acima: o bloco não se apresenta sozinho.

## Quando NÃO usar


- (nota do cadastro) products-8b nao declara nenhum ativo eliminatorio na prosa; a restricao e estrutural (itens min/max e papel_na_peca apoio/fechamento, nao abre sozinha)
Menos de 6 produtos (grid 3-col com 3–4 itens fica ralo — usar lista simples ou zigzag). Produtos que precisam de explicação ou preço para converter. Como seção única de e-mail promocional — sem oferta nem urgência, é seção de apoio/fechamento.

## Orientações de copy para a IA

Título — anuncia o recorte da lista, caixa alta, terminando em dois-pontos.  

Copy — duas linhas paralelas na mesma estrutura, cada uma com a primeira palavra sublinhada. O paralelismo é o que sustenta o recurso: "Trusted By Thousands. / Verified By Science." Ponto final nas duas.  

Nome do produto — o que diferencia aquela variação, não o nome da linha. Se todos são shampoo, o nome é o aroma, não "shampoo". Caixa alta. Todos os nomes de uma mesma fileira devem ocupar o mesmo número de linhas.  

CTA — verbo genérico curto, igual nos nove.  

Proibições: preço ou percentual · descrição por produto · nome de linha repetido nos nove · sublinhado fora das duas linhas de copy · CTA de coleção acrescentado · nomes com alturas diferentes na mesma fileira.

## Design system

Container 600px fixo, borda 1px   
#000000 opcional (flag has_border). Zero raio, zero sombra, zero gradiente.  

Estrutura  

| # | Elemento | Padding-top | Dimensão |  
|---|---|---|---|  
| 1 | Título | 47px | 40/45px bold, caixa alta, padding lateral 40px |  
| 2 | Copy | 25px | 25/29px, 2 linhas |  
| 3 | Fileira 1 | 98px | 524px, padding 38px esquerda · 36px direita |  
| 4 | Fileira 2 | 54px | 524px |  
| 5 | Fileira 3 | 54px | 524px, com 47px de respiro na base |  

Célula de produto: 164px de largura, gap de 16px entre colunas. Foto 164 × 186px · nome 20px abaixo, 20/25px bold, altura fixa de 50px · CTA 9px abaixo, 164 × 43px.  

O respiro antes da primeira fileira (98px) é quase o dobro dos 54px entre fileiras: separa o cabeçalho da grade.  

Paleta — duas cores.  

| Papel | Hex (Routine) | Uso |  
|---|---|---|  
| Cor primária |  |  |  
| #00227C | Título, copy e nome dos produtos |  |  
| Cor secundária |  |  |  
| #EE4037 | Fundo dos nove botões, com label branco |  |  

O fundo é branco. A cor secundária aparece só nos botões — nove blocos idênticos de cor formando um ritmo vertical que é, na prática, o segundo elemento gráfico da peça.  

Pele alternativa (HTML base): título, copy e nomes em preto; botões pretos. Usar quando a marca não tem par de cores próprio.  

Tipografia. Principal: Arial → Helvetica em todos os slots. Título 40px bold caixa alta; copy 25px regular com text-decoration:underline na palavra enfatizada; nome 20px bold caixa alta; CTA 20px bold. Secundária não existe.  

Implementação. font-size:0;line-height:0 na célula de cada foto e em todos os espaçadores de 16px — com nove imagens, um gap de Outlook em qualquer uma desalinha a fileira. A célula do nome precisa de height:50px explícito: sem isso, um nome de uma linha sobe o botão daquela coluna em 25px em relação aos vizinhos. Botões bulletproof. Hack u + .body .txt-blk.  

Tags: SECTION_TITLE, SECTION_COPY, PRODUCT_N_IMAGE_URL, PRODUCT_N_IMAGE_ALT, PRODUCT_N_NAME, PRODUCT_N_CTA_URL, PRODUCT_CTA_LABEL.  

Erros que quebram o padrão: célula do nome sem altura fixa · nomes de alturas diferentes na mesma fileira · preço ou descrição acrescentados · CTA de coleção no fim · sublinhado no nome ou no título · gap diferente de 16px entre colunas · fileira incompleta · fundo colorido nas fotos.

## Direção fotográfica

Proporção 4:5 — slot de 164 × 186px, ativo final 328 × 372px (2x). PNG, < 90 KB cada. Gerar em 4:5 na altura de 372px (298 × 372) e ampliar para 328px de largura.  

Regra crítica: os nove ativos precisam de enquadramento e escala idênticos. O produto ocupa a mesma altura relativa em todos, alinhado no mesmo eixo. É a única forma de a grade parecer grade — variação de escala entre células destrói o alinhamento óptico mesmo com as caixas certas.  

Composição. Packshot recortado sobre fundo branco puro, centralizado, com folga em volta. Quando o item é um conjunto (frasco duplo, kit), os dois elementos aparecem lado a lado com leve sobreposição, sempre na mesma disposição em todas as células.  

O que diferencia as células. A cor da embalagem, o rótulo e — quando houver — os elementos decorativos ao redor: flores, frutas, ingredientes da variação. Esses adereços são o que faz a grade ser legível em 164px de largura, já que o texto do rótulo não é legível nesse tamanho.  

Luz. Frontal difusa, sombra suave e curta. Idêntica nos nove.  

Proibições: fundo colorido ou cinza · escalas diferentes entre células · sombra dura ou projetada longa · cenário · modelo ou mão · texto/preço/selo queimado além do rótulo real · variações que só se distinguem pelo texto do rótulo · marca d'água.  

Adaptação por categoria — o que diferencia as variações:  

| Categoria | Diferenciador visual |  
|---|---|  
| Beleza / cabelo | Cor do rótulo + ingrediente botânico ao redor |  
| Suplementos | Cor da tampa e do rótulo |  
| Alimentos | Cor da embalagem + ingrediente cru ao lado |  
| Bebidas | Cor da lata + fruta correspondente |  
| Papelaria | Cor da capa |  
| Pet | Cor do sachê + petisco visível |

---

HTML: [[_html/products-8b-grade-3x3.html]] · Seção: [[_products]] · Protocolo: [[_protocolo-de-selecao]]

