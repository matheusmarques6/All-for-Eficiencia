---
tipo: componente
slug: offer-3-lembrete-de-cupom
secao: offer
nome_no_banco: "offer 3"
variant_id: da0b6e11-c681-48af-ae88-316429e25c05
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [browse-abandonment, carrinho-abandonado]
momento_vetado: []

# --- eixos de ranking, na ordem do protocolo ---
objecao: []
registro: []
registro_vetado: []
paleta: []
papel_na_peca: [peca-inteira]

# --- requisitos duros (eliminam) ---
exige: [cupom-ativo]

# --- capacidade e composição ---
product_slots: 0
itens: null
peso: { altura_px: 1201, classe: pesado, fonte: medido }
convivencia: []

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: null
schema_campos: 7
status: aprovada
---

## Descrição curta

Bloco de lembrete de cupom para quem já recebeu o código e não usou. Repete o código, o percentual e a condição em quatro linhas curtas, com o produto embaixo e um botão único — serve como e-mail inteiro de reforço, não como seção de apoio.

## Descrição detalhada

Card arredondado de fundo claro flutuando sobre um fundo em gradiente de cor da marca, com quatro elementos de texto no terço superior, a foto do produto no meio e um botão em pílula que atravessa a borda inferior do card. O código de desconto vive dentro de uma pílula colorida encaixada no meio de uma frase, com a palavra seguinte ao lado dela na mesma linha.  

Três mecanismos sustentam o bloco:  

Cupom inline, não empilhado. A pílula do código fica dentro da frase, com a preposição seguinte ao lado dela na mesma linha. O leitor lê "use o código X para" numa tacada só, em vez de ler três blocos separados.  
Botão atravessando a borda do card. A pílula do CTA fica metade dentro e metade fora do card — 33px acima da borda e 35px abaixo. É o que impede o card de parecer uma caixa fechada e leva o olho para fora dela.  
Cor invertida entre pílula e botão. A pílula do código é a cor da marca com texto claro; o botão é claro com texto escuro. As duas âncoras da peça não competem entre si.

## Quando usar

Lembrete de cupom não usado, dois a quatro dias depois do welcome ou do pop-up de captura.  
Recuperação de navegação ou de carrinho quando o desconto já foi concedido e só falta ser aplicado.  
Marca com produto pequeno e colorido que aparece bem em pilha ou grupo — acessório, cosmético, papelaria, snack.  
Como e-mail curto e único, não como bloco dentro de uma peça longa.

## Quando NÃO usar

Sem cupom. A pílula do código é o centro da variante e não tem substituto.  
Produto grande ou que precisa de contexto de uso. A foto aqui é um agrupamento em fundo neutro, não uma cena.  
Campanha com mais de uma condição ou regra. Só há quatro linhas de texto e nenhuma delas comporta letra miúda.  
Primeiro contato com a oferta. O bloco pressupõe que o leitor já conhece o código.

## Orientações de copy para a IA

A primeira linha assume que já foi dito antes: "não esqueça de usar", nunca "aqui está seu código". É lembrete, não entrega.  
A frase atravessa a pílula. O texto antes do código e a preposição depois dele fazem parte da mesma frase — escrever os dois pedaços como se a pílula fosse uma palavra no meio.  
A palavra depois da pílula é curta, uma preposição de até 4 caracteres. Ela precisa caber ao lado da pílula na mesma linha.  
A linha do percentual é só o percentual, em corpo grande, sem qualificador.  
A última linha diz sobre o que o desconto vale, e é a única que carrega a exclamação da peça.  
Title Case nas quatro linhas. O código fica em caixa alta.  
CTA genérico e curto. A oferta já foi declarada três vezes acima; o botão só precisa levar.

## Design system

Container: 600px travado, altura 639. O fundo é um gradiente vertical na cor da marca, do topo (  
#2C7D83) para a base (  
#379998).  

Card: 558 × 517 (x 21–579, y 45–561), raio ~19, fundo azul-claro   
#C7D6EB. Margem de 21px para as bordas laterais do container, 45 no topo e 78 na base.  

Tipografia principal: sans geométrica. Não há tipografia secundária. O template substitui por Arial, Helvetica, sans-serif.  

| Bloco | Tamanho aproximado | Peso | Caixa |  
|---|---|---|---|  
| Linha de introdução | ~25 | 400 | Title Case |  
| Código na pílula | ~28 | 700 | ALTA |  
| Palavra ao lado da pílula | ~25 | 400 | Title Case |  
| Linha do percentual | ~55 | 700 | ALTA |  
| Linha de fechamento | ~28 | 400 | Title Case |  
| Label do CTA | ~22 | 700 | ALTA |  

Cores. Cor primária   
#012B46 — azul-marinho escuro em todo o texto sobre o card e no label do CTA. Cor secundária   
#C7D6EB (fundo do card). Cor de acento   
#379898, usada no gradiente de fundo e no preenchimento da pílula do código — é a mesma cor nos dois lugares.   
#FFFFFF no código dentro da pílula e no preenchimento do CTA.  

Grade e ritmo vertical (medido, já normalizado para 600px):  

fundo em gradiente        600 × 639  
CARD                      558 × 517 (x 21–579, y 45–561), raio 19  
   ↓ 31px do topo do card  
linha de introdução       y 76–100, centralizada  
   ↓ 6px  
PÍLULA DO CÓDIGO          218 × 35 (x 156–373), totalmente arredondada  
                          + palavra ao lado, x 384–418, alinhada ao centro da pílula  
   ↓ 17px  
linha do percentual       y 157–201  
   ↓ 21px  
linha de fechamento       y 222–243  
   ↓ 27px  
área da foto do produto   ~260px livres, produto agrupado e centralizado  
CTA                       496 × 69 (x 52–548), pílula, fundo branco  
                          topo 33px acima da base do card, base 35px abaixo dela  
   ↓ 43px até o fim da peça  

Regras que não podem ser quebradas:  

O CTA atravessa a borda inferior do card, dividido praticamente ao meio por ela. Encaixá-lo dentro do card fecha a composição.  
A pílula do código e a palavra seguinte ficam na mesma linha. Empilhar quebra a frase.  
A pílula do código é preenchida na cor de acento com texto claro; o CTA é claro com texto escuro. A inversão entre os dois é obrigatória.  
Tudo centralizado, com exceção do conjunto pílula + palavra, que é centralizado como um bloco só.  
Cantos: o card tem raio pequeno (19), a pílula e o CTA são totalmente arredondados. Não há canto reto na peça.  
A foto do produto não recebe texto por cima e fica na metade inferior do card

## Direção fotográfica

Agrupamento do produto sobre superfície neutra clara, fotografado de frente e ligeiramente de cima.  

Composição: várias unidades do mesmo produto empilhadas ou encostadas umas nas outras, formando um monte compacto no centro. Nada alinhado em grade, nada isolado.  
Variação: cada unidade em uma estampa ou cor diferente, para o agrupamento mostrar o catálogo sem precisar de grade de produtos.  
Superfície: clara, lisa e sem textura, com sombra de contato suave logo abaixo da pilha. O fundo tem que se dissolver no azul-claro do card.  
Luz: difusa e frontal, sem sombra dura e sem realce especular.  
Escala: o agrupamento ocupa cerca de metade da largura do card, deixando respiro dos dois lados.  
Proibições: modelo, mão, cena de uso, fundo colorido, sombra projetada forte, produto cortado pelas bordas.

---

HTML: [[_html/offer-3-lembrete-de-cupom.html]] · Seção: [[_offer]] · Protocolo: [[_protocolo-de-selecao]]
