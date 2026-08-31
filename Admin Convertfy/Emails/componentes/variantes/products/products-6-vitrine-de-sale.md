---
tipo: componente
slug: products-6-vitrine-de-sale
secao: products
nome_no_banco: "produtos 6"
variant_id: fc41efe6-a2dc-493a-ab92-75e30fd13198
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
product_slots: 2
itens: null
peso: null
convivencia: []

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: baixa
schema_campos: 8
status: aprovada
---

## Descrição curta

Bloco de vitrine de promoção. Uma faixa xadrez marca o início, um título anuncia a lista e dois produtos aparecem com foto, nome e uma frase de descrição — sem preço, sem selo e sem botão individual. Momento de uso: e-mail de sale semanal ou recorrente, quando o objetivo é dizer o que entrou em promoção e mandar todo mundo para a mesma página.

## Descrição detalhada

Faixa xadrez de 98px, título, dois blocos de produto em linha e um CTA único.  

Quatro mecanismos definem a variante:  

A faixa xadrez é 100% HTML. Vinte e duas células de 49px em duas linhas alternadas, cada uma com font-size:0;line-height:0. Nenhuma imagem — o ornamento de marca sobrevive a imagem bloqueada e muda de cor por loja sem passar pelo design.  

A foto sangra na borda esquerda do container. Padding zero à esquerda: a imagem encosta na borda e o texto ocupa os 332px restantes. Isso dá leitura de lista corrida, não de card.  

Nenhum preço, selo ou botão por item. Só nome e uma frase. O bloco diz o que está em promoção, não por quanto — o preço fica na página de destino.  

O nome do produto é regular, não bold. A hierarquia contra a descrição vem só do tamanho, 30px contra 24px. Colocar bold no nome achata a diferença e o bloco vira catálogo.

## Quando usar

Sale recorrente — promoção semanal, "o que entrou essa semana", liquidação de categoria.  
Alimentos, bebidas, açougue, mercearia, casa, pet — categorias de compra frequente.  
Quando os produtos compartilham o mesmo destino e não precisam de página própria.  
Quando a marca tem um ornamento gráfico de identidade que se resolve em módulos quadrados.  
Quando basta nomear o produto e dar uma frase: a decisão acontece na página.

## Quando NÃO usar

Quando o preço é o argumento — não há slot para valor nem para percentual.  
Produtos com destinos diferentes — o CTA é único.  
Mais de dois produtos — o padrão é uma lista curta; a partir do terceiro, use uma grade.  
Marca sem ornamento gráfico — a faixa xadrez precisa fazer parte da identidade, senão vira enfeite solto.  
Carrinho, checkout, transacional, prova social, welcome.  
Categorias de ticket alto: a densidade baixa e a ausência de preço soam informais demais.

## Orientações de copy para a IA

Título — anuncia a lista, em caixa alta, terminando em dois-pontos. O sinal é o que emenda no que vem abaixo.  

Nome do produto — nome comercial curto, uma linha. Pode incluir a medida ou o peso quando isso identifica o item.  

Descrição — uma frase em duas linhas dizendo como é ou para que serve. Adjetivos concretos e o uso pretendido. Ponto final obrigatório. As duas descrições precisam ter estrutura diferente entre si — se as duas seguirem o mesmo molde, a lista fica mecânica.  

CTA — verbo genérico apontando para a sale inteira, caixa alta com tracking largo.  

Proibições: preço ou percentual em qualquer slot · nome do produto em bold · descrição com mais de duas linhas · terceiro produto · CTA por item · exclamação.

## Design system

Container 600px fixo, borda 1px   
#000000 opcional (flag has_border). Zero raio, zero sombra, zero gradiente.  

Estrutura  

| # | Elemento | Padding-top | Dimensão |  
|---|---|---|---|  
| 1 | Faixa xadrez | 29px topo · 30px esquerda · 29px direita | 539 × 98px |  
| 2 | Título | 53px | 40/46px bold, caixa alta, padding lateral 40px |  
| 3 | Produto 1 | 51px | Linha de 598px |  
| 4 | Produto 2 | 22px | Linha de 598px |  
| 5 | CTA | 66px | 415 × 67px, com 29px de respiro na base |  

Faixa xadrez: duas linhas de 11 células de 49 × 49px. Na linha superior, as colunas ímpares são preenchidas; na inferior, as pares. Isso dá 6 células cheias em cima e 5 embaixo — a assimetria é o que faz o padrão parecer contínuo apesar de só ter duas fileiras.  

Linha de produto: foto de 266 × 217px encostada na borda esquerda, sem padding; coluna de texto de 332px com padding de 64px no topo (62px no produto 2), 39px à esquerda e 20px à direita. Nome 30/34px regular; descrição 15px abaixo, 24/29px em duas linhas.  

Paleta — duas cores.  

| Papel | Hex (referência) | Uso |  
|---|---|---|  
| Cor primária |  |  |  
| #A51E24 | Faixa xadrez e fundo do CTA |  |  
| Cor secundária |  |  |  
| #000000 | Título, nome e descrição |  |  

O fundo é branco e o label do CTA também. A cor primária aparece só nos dois elementos gráficos — faixa e botão — e nunca em texto corrido. É o que amarra o topo ao rodapé do bloco.  

Pele alternativa (HTML base): faixa e CTA em preto, sem cor de marca. Usar quando a loja não tem cor própria definida.  

Tipografia. Principal: Arial → Helvetica em todos os slots. Título 40px bold caixa alta; nome 30px regular; descrição 24px regular; CTA 18px regular caixa alta com tracking +0.25em e text-indent compensando. Secundária não existe.  

Implementação. Cada célula do xadrez precisa de width, height, font-size:0 e line-height:0 — sem isso o Outlook insere altura fantasma e o padrão desalinha. A <img> com display:block e background:#EFEFEF como fallback. font-size:0;line-height:0 na célula da foto. Hack u + .body .txt-blk.  

Tags: CHECKER_COLOR, SECTION_TITLE, PRODUCT_N_IMAGE_URL, PRODUCT_N_IMAGE_ALT, PRODUCT_N_NAME, PRODUCT_N_DESCRIPTION, CTA_LABEL, CTA_URL.  

Erros que quebram o padrão: xadrez como imagem · célula sem font-size:0 · as duas fileiras do xadrez com o mesmo número de células cheias · foto com padding à esquerda · nome do produto em bold · preço no bloco · CTA por produto · terceiro produto · cor primária em texto.

## Direção fotográfica

Proporção 5:4 — slot de 266 × 217px, ativo final 532 × 434px (2x). PNG, < 120 KB cada. Gerar em 5:4 na altura de 434px (543 × 434) e cortar 11px de largura.  

Regra crítica: fundo branco puro, igual ao do container. A foto não tem moldura nem borda, então qualquer diferença de tom desenha um retângulo à esquerda do texto.  

Composição. Produto isolado, sem prato, sem tábua, sem prop. Centralizado no quadro com folga em volta — diferente das variantes de packshot sangrado, aqui a imagem respira porque não há contorno que a segure.  

Luz. Difusa e frontal, sombra mínima. Nada de sombra projetada longa: ela criaria uma linha visível contra o branco do container.  

Produto. Cru, montado ou porcionado conforme a categoria, mostrado como o cliente vai receber. Textura em primeiro plano — é o único argumento visual, já que não há preço nem selo.  

Os dois quadros precisam ter escalas diferentes. Um mais fechado, com o produto ocupando pouco do quadro, e outro mais aberto, preenchendo quase toda a área. É o que evita que a lista pareça duas fotos do mesmo lote.  

Proibições: fundo colorido ou cinza · sombra projetada longa · prop, prato ou tábua · texto/preço/selo queimado · produto sangrando nas bordas · dois quadros na mesma escala · marca d'água.  

Adaptação por categoria — o que é o produto:  

| Categoria | Enquadramento |  
|---|---|  
| Açougue / carnes | Corte cru embalado ou porção pronta |  
| Mercearia | Embalagem frontal |  
| Bebidas | Garrafa ou lata isolada |  
| Casa | Item avulso, sem ambiente |  
| Pet | Embalagem ou petisco solto |  
| Padaria | Peça inteira ou fatiada |

---

HTML: [[_html/products-6-vitrine-de-sale.html]] · Seção: [[_products]] · Protocolo: [[_protocolo-de-selecao]]
