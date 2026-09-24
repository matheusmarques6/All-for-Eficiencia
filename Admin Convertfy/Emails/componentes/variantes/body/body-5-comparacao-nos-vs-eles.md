---
tipo: componente
slug: body-5-comparacao-nos-vs-eles
secao: body
nome_no_banco: "body 5 - comparison table us vs them"
variant_id: 7d1c214a-abb1-44b6-bb5e-95777fb0f306
ativa: false
dispositivo: comparacao_pareada

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [welcome-meio, welcome-tardio, carrinho-abandonado, browse-abandonment]
momento_vetado: [campanha-promocional]

# --- eixos de ranking, na ordem do protocolo ---
objecao: [confianca-no-canal, preco-valor]
registro: [premium-editorial]
registro_vetado: []
paleta: [creme]
papel_na_peca: [meio, fecha]

# --- requisitos duros (eliminam) ---
exige: [quatro-criterios-objetivos]
diretivas_de_imagem: []

# --- capacidade e composição ---
product_slots: 0
itens: { min: 4, max: 5 }
peso: { altura_px: 1293, classe: pesado, fonte: medido }
convivencia: []

# --- fios para o resto do vault ---
aprendizados: ["[[cada-alegacao-e-uma-promessa-operacional]]", "[[posicao-muda-o-efeito-do-dispositivo]]"]
serve_estruturas: ["[[medicube-comparacao-categoria]]"]

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: balanced
schema_campos: 16
status: aprovada
---

## Descrição curta

Bloco de diferenciação para quando o cliente já entendeu a categoria e está decidindo entre marcas. Coloca a loja lado a lado com a concorrência genérica em cinco critérios e resolve a objeção de "por que pagar mais nesse".

## Descrição detalhada

Tabela de três colunas — critério à esquerda, a marca no meio, a concorrência à direita — com cinco linhas de comparação. A coluna do meio é um painel escuro que atravessa a tabela inteira e sobressai acima e abaixo dela, com uma foto circular do produto encaixada no topo. Cada célula das colunas de comparação traz um ícone de validação e uma frase curta. Fecha com um CTA sólido fora da tabela.  

Quatro mecanismos sustentam a seção:  

Coluna do meio como painel, não como célula. O bloco escuro de 192px atravessa toda a altura da tabela, ultrapassa 29px acima e 35px abaixo e tem cantos arredondados nas quatro pontas. Ele é lido como um objeto sobreposto à tabela, não como uma coluna dela.  
Foto circular ancorando a coluna. Um círculo de 118px com o produto se encaixa no topo do painel escuro, metade dentro e metade fora. É a única imagem de produto da seção e serve para dizer de quem é a coluna sem precisar de logo.  
Assimetria deliberada de copy. A célula da marca tem 2 a 4 linhas; a da concorrência tem 2 a 5. As linhas da direita são sempre mais longas — a desvantagem precisa de mais palavras que a vantagem, e é isso que dá altura à linha da tabela.  
Nenhuma marca concorrente é nomeada. A coluna da direita é "outras marcas", genérica. É o que permite a comparação sem risco.

## Quando usar

Categoria saturada em que o cliente compara preço com um genérico de farmácia ou marketplace.  
Produto com diferencial verificável em critérios objetivos: formulação, ingrediente, uso em pele sensível, sustentabilidade.  
Meio ou fim da régua de welcome, recuperação de carrinho de alto valor, ou e-mail de objeção depois de o cliente já ter visitado a página.  
Marca com posicionamento premium que precisa justificar preço sem falar de preço.

## Quando NÃO usar

Marca sem diferencial real nos critérios listados. A tabela expõe: cinco linhas de vantagem vaga soam falsas.  
Categoria em que a compra é por estética ou impulso, não por especificação.  
Quando existe um concorrente dominante identificável — a coluna genérica deixa de funcionar e nomear traz risco jurídico.  
Menos de quatro critérios. Com três linhas a tabela não justifica a estrutura.  
E-mail promocional com desconto: a seção é argumentativa e não tem slot de oferta nenhum.

## Orientações de copy para a IA

O rótulo do critério é uma palavra, no máximo duas, em caixa alta. É a única coisa em caixa alta da tabela.  
A coluna da marca afirma; a da concorrência descreve o problema. À esquerda "Long-Lasting Hydration", à direita "Often Leaves Brows Dry After Use". A vantagem é substantiva, a desvantagem é comportamental.  
A coluna da concorrência usa hedge obrigatório — "often", "may", "can", "not always". Nunca afirmação categórica sobre terceiros.  
Title Case em todas as células, nas duas colunas. É o que dá simetria visual a frases de tamanhos diferentes.  
Um critério deve ser não-funcional (sustentabilidade, ética, origem) para a tabela não virar só ficha técnica.  
Cabeçalhos em possessivo e genérico: "Our X" contra "Other Brands" ou equivalente. Nunca nomear concorrente.  
CTA nomeia a categoria comparada, não a loja inteira — o leitor acabou de decidir sobre um produto específico.

## Design system

Container: 600px travado. O fundo da seção inteira é um ativo de imagem: foto desfocada e clara no topo que se dissolve num bege chapado   
#EBDFC9 a partir de ~y160 na esquerda e ~y360 na direita.  

Tipografia principal: sans humanista para rótulos, células e CTA. Tipografia secundária: uma serifada em itálico, usada exclusivamente nos dois cabeçalhos de coluna ("Our Aftercare" / "Other Brands"). É o único ponto da seção com segunda família — e é ele que separa o cabeçalho do conteúdo sem precisar de fundo ou régua.  

| Bloco | Tamanho / entrelinha | Peso | Caixa |  
|---|---|---|---|  
| Cabeçalho de coluna (serifada) | 24 / 24 | 400 itálico | Title Case |  
| Rótulo do critério | 17 / 18 | 700 | ALTA |  
| Texto da célula | 20 / 20 | 400 | Title Case |  
| Label do CTA | 22, tracking ~0.12em | 700 | ALTA |  

Cores. Cor primária   
#140E32 — azul-marinho quase preto, usado no painel central, no CTA, nas bordas e em todo o texto escuro. Não existe preto puro na peça. Cor secundária   
#FFFFFF (fundo da tabela e texto sobre o painel). Fundo da seção   
#EBDFC9. Dois acentos com função única:   
#00C109 no ícone de validação e   
#E90000 no ícone de negação.  

Grade e ritmo vertical (medido):  

fundo fotográfico → bege  
   círculo Ø118 centrado em x285, topo em y20  
   painel escuro 192 × 908 (x 189–380, y 71–978), raio 23 nas 4 pontas  
TABELA BRANCA  533 × 845 (x 34–566, y 102–945), raio 23, borda 1px #1C1638  
   colunas: 154 | 192 (painel) | 185  
   cabeçalho          y 171–187, sem separador abaixo  
   linha 1  HYDRATION       cabeçalho+linha = 248 de altura  
   ── separador 1px  
   linha 2  STRENGTH        120  
   ── separador  
   linha 3  SENSITIVE SKIN  142   (rótulo em 2 linhas)  
   ── separador  
   linha 4  INGREDIENTS     147  
   ── separador  
   linha 5  SUSTAINABILITY  186  
   ícone 23 × 23 no topo da célula, ~34px até a primeira linha de texto  
   ↓ 55px da base do painel  
CTA  419 × 75 (x 91), cantos retos, fundo #140E32  

Regras que não podem ser quebradas:  

As três células de cada linha são centralizadas verticalmente. A altura da linha é ditada pela célula mais alta, que é quase sempre a da concorrência.  
O painel central sobressai da tabela em cima e embaixo e tem raio nas quatro pontas. Encaixá-lo como célula comum destrói a variante.  
Os separadores horizontais atravessam só as colunas brancas — nunca cruzam o painel.  
Não há separador abaixo do cabeçalho. A primeira régua aparece só depois da linha 1.  
Os ícones são blocos chapados de 23×23, não emoji de fonte. Emoji renderiza diferente em cada cliente e quebra a única cor da seção.  
Verde só no ícone de validação, vermelho só no de negação. Nenhum dos dois aparece em texto, borda ou fundo.  
Todo o escuro da peça é o mesmo   
#140E32 — painel, CTA, bordas e texto. Preto puro endurece a composição contra o bege.

## Direção fotográfica

Dois ativos com funções opostas: um retrato de produto nítido e fechado, e um fundo que precisa desaparecer.  

Círculo de produto: vários frascos ou unidades do item espalhados sobre superfície clara, vistos de cima, luz natural difusa, com brilho de vidro e metal. Enquadramento fechado o bastante para os rótulos serem sugeridos mas não lidos. Composição espalhada, sem centro óbvio — o círculo corta o quadro e o assunto precisa preencher todas as bordas.  

Fundo: a mesma cena fotografada bem desfocada e superexposta, ocupando só o terço superior e se dissolvendo num bege chapado antes de chegar à tabela. Nada reconhecível: o que sobra é textura e temperatura de cor.  

Paleta: creme, dourado claro, branco quente. A foto tem que conversar com o bege do fundo, não contrastar com ele.  
Luz: natural, alta, sem sombra dura e sem fundo colorido.  
Proibições: modelo, mão, fundo escuro, produto isolado em fundo branco de e-commerce, sombra projetada forte, qualquer elemento nítido no ativo de fundo.

---

HTML: [[_html/body-5-comparacao-nos-vs-eles.html]] · Seção: [[_body]] · Protocolo: [[_protocolo-de-selecao]]
