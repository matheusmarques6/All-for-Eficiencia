---
tipo: componente
slug: offer-6-carrinho-preto-e-branco
secao: offer
nome_no_banco: "offer 6"
variant_id: 1e45ed32-01c4-487c-bb60-f986623a3270
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [carrinho-abandonado, checkout-abandonado]
momento_vetado: []

# --- eixos de ranking, na ordem do protocolo ---
objecao: []
registro: [bold-alto-contraste]
registro_vetado: []
paleta: [preto-e-branco]
papel_na_peca: [peca-inteira]

# --- requisitos duros (eliminam) ---
exige: [cupom-ativo, bloco-dinamico-de-carrinho]

# --- capacidade e composição ---
product_slots: 0
itens: null
peso: { altura_px: 852, classe: medio, fonte: medido }
convivencia: []

# --- fios para o resto do vault ---
aprendizados: ["[[cada-alegacao-e-uma-promessa-operacional]]"]
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: null
schema_campos: 9
status: aprovada
---

## Descrição curta

E-mail inteiro de recuperação de carrinho para marca de contraste alto, dividido em dois blocos de fundo oposto: o branco mostra o que ficou no carrinho, o preto entrega o cupom e chama de volta. As duas metades são separadas por uma faixa de papel rasgado.

## Descrição detalhada

Faixa rasgada no topo, bloco branco com o título do carrinho e o bloco dinâmico de produto, segunda faixa rasgada como transição, e bloco preto com headline, sublinha da oferta, caixa de cupom em branco chapado, linha de apoio e CTA em pílula clara.  

Três mecanismos sustentam a peça:  

Inversão de fundo como divisão de função. O branco é informativo — lembra o que o cliente escolheu. O preto é persuasivo — reabre a oferta e chama. A troca de fundo faz a virada sem precisar de headline de seção.  
Faixa rasgada como emenda. As duas transições são ativos de imagem de 600 × 70 com borda irregular, não réguas retas nem cantos arredondados. É o único elemento decorativo da peça.  
Frase que atravessa a caixa do cupom. A linha depois da caixa começa em minúscula e continua a sentença iniciada dentro dela. O cupom é lido como parte da frase, não como bloco isolado.

## Quando usar

Recuperação de carrinho ou de checkout com desconto ativo.  
Marca de identidade preto e branco, com contraste alto e sem paleta autoral.  
Categoria funcional em que o cliente compra por problema resolvido — controle de praga, ferramenta, limpeza, manutenção.  
Quando o e-commerce tem bloco dinâmico de produto configurado e o carrinho pode ser exibido de verdade.

## Quando NÃO usar

Sem bloco dinâmico funcionando. O bloco branco existe para mostrar o item salvo; com placeholder estático ele perde a razão de ser.  
Sem cupom. A caixa branca no bloco preto é o centro da metade de baixo.  
Marca com paleta de cor. A peça inteira depende da inversão branco/preto e não tem onde acomodar uma terceira cor.  
Como seção dentro de outro e-mail. As duas faixas rasgadas pressupõem que a peça começa e termina nela mesma.

## Orientações de copy para a IA

O título do bloco branco nomeia o que está ali, com dois-pontos, e nada além disso. Ele apresenta o bloco dinâmico, não vende.  
A headline do bloco preto é uma pergunta curta que devolve a decisão ao cliente, sem pressão e sem prazo.  
A sublinha reafirma que o desconto continua valendo, no presente. É lembrete de algo já concedido, não oferta nova.  
A caixa de cupom abre uma frase que a linha seguinte fecha. Escrever as duas partes juntas: a linha de apoio começa em minúscula e emenda na anterior.  
A linha de apoio fala do problema, não do produto — o que o cliente para de enfrentar ao concluir a compra.  
O CTA devolve ao carrinho, com posse ("seu carrinho"), não à loja.

## Design system

Container: 600px travado. Dois blocos de fundo:   
#FFFFFF na metade de cima e   
#000000 na de baixo, emendados por faixas rasgadas de 600 × 70.  

Tipografia principal: sans, uma única família em todos os elementos.  

| Bloco | Tamanho / entrelinha | Peso | Caixa |  
|---|---|---|---|  
| Título do carrinho | 32 / 33 | 400 | ALTA |  
| Headline do bloco preto | 40 / 60 | 400 | ALTA |  
| Sublinha da oferta | 32 / 48 | 400 | Sentença |  
| Texto do cupom | 32 / 44 | 400 | ALTA |  
| Linha de apoio | 24 / 33 | 400 | Sentença |  
| Label do CTA | 25 | 400 | Title Case |  

Cores. Cor primária   
#000000 e cor secundária   
#FFFFFF, invertendo de papel entre os dois blocos.   
#BBBBBB no preenchimento do CTA, com label preto — é o único tom intermediário da peça (ver divergência 3).  

Grade e ritmo vertical:  

faixa rasgada         600 × 70  
BLOCO BRANCO  
   ↓ 46px  
título do carrinho    centralizado  
   ↓ 60px  
bloco dinâmico        455 × 200, borda 1px #090909, cantos retos  
   ↓ 51px  
faixa rasgada         600 × 70  
BLOCO PRETO  
   ↓ 21px  
headline              centralizada  
   ↓ 25px  
sublinha da oferta  
   ↓ 28px  
CAIXA DO CUPOM        430 × 64, branco chapado, cantos retos, texto #171717  
   ↓ 28px  
linha de apoio  
   ↓ 43px  
CTA                   346 × 63, pílula, fundo #BBBBBB, label preto  
   ↓ 92px  

Regras que não podem ser quebradas:  

As faixas rasgadas são ativos de imagem, nunca borda ou raio. Cada uma tem que casar exatamente com a cor do bloco de cima e a do de baixo.  
O bloco dinâmico tem borda fina e canto reto. Ele é uma moldura para conteúdo de terceiro, não um card de design.  
A caixa do cupom é branco chapado sobre o preto, com canto reto — a inversão máxima da peça e o único retângulo claro dentro do bloco escuro.  
Só o CTA é arredondado, e totalmente (pílula). Todo o resto tem canto reto.  
Tudo centralizado nos dois blocos.  
Zero cor além de preto, branco e o cinza do CTA.

## Direção fotográfica

Não se aplica a fotografia — os dois slots de imagem são gráficos, não fotos.  

Faixas rasgadas: borda irregular de papel rasgado, com fibras e microrrasgos visíveis, sem sombra e sem textura de papel no corpo da faixa. Cada faixa é bicolor e chapada: metade da altura na cor do bloco de cima, metade na do de baixo, com o rasgo atravessando no meio. A da transição inverte a ordem em relação à do topo.

---

HTML: [[_html/offer-6-carrinho-preto-e-branco.html]] · Seção: [[_offer]] · Protocolo: [[_protocolo-de-selecao]]
