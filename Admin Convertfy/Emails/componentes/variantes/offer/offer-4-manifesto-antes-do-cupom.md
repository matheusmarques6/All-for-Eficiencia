---
tipo: componente
slug: offer-4-manifesto-antes-do-cupom
secao: offer
nome_no_banco: "offer 4"
variant_id: 69ede46f-1534-431c-bdab-2d7be60ce236
ativa: false

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [welcome-1]
momento_vetado: [campanha-promocional]

# --- eixos de ranking, na ordem do protocolo ---
objecao: [pertencimento]
registro: [premium-editorial]
registro_vetado: [popular-informal]
paleta: []
papel_na_peca: [peca-inteira, fecha]

# --- requisitos duros (eliminam) ---
exige: [cupom-ativo, manifesto-de-marca-escrito]

# --- capacidade e composição ---
product_slots: 0
itens: null
peso: { altura_px: 682, classe: medio, fonte: medido }
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

Bloco de boas-vindas para marca de posicionamento premium, quando o cupom precisa vir depois de um argumento de marca e não antes dele. Declara a missão em três parágrafos e só então entrega o código, sem nenhuma imagem.

## Descrição detalhada

Headline em duas escalas, três parágrafos curtos de manifesto, uma faixa de cupom dividida em duas metades de tratamento oposto, uma linha de aviso e um CTA sólido. Tudo centralizado, tudo em uma única cor sobre branco, sem imagem, borda de container, ícone ou divisor.  

Três mecanismos sustentam o bloco:  

Headline em duas escalas na mesma frase. A primeira linha vem em corpo reduzido e a continuação em corpo grande — não é sobrescrito mais título, é uma frase só que muda de tamanho no meio. A leitura atravessa a quebra.  
Cupom bipartido. O rótulo fica numa metade de contorno tracejado e sem preenchimento; o código fica na outra metade em bloco chapado com texto invertido. As duas metades encostam e formam uma faixa única — é a única figura geométrica da peça.  
Cor única em tudo. O mesmo verde aparece no texto, no tracejado, no bloco do código e no CTA. Sem segunda cor e sem preto, o bloco fica leve o bastante para o cupom não parecer promoção agressiva.

## Quando usar

Welcome de marca premium, onde o cupom precisa vir depois do argumento e não como manchete.  
Categoria em que a compra é por identificação com a marca: moda autoral, couro, joalheria, perfumaria, decoração.  
Quando a marca tem uma missão escrita que se sustenta em três frases.  
Como e-mail inteiro e curto, ou como fechamento de uma peça que já mostrou produto.

## Quando NÃO usar

Campanha promocional com percentual alto. O bloco esconde o desconto atrás de três parágrafos e não tem nenhum slot para o valor da oferta.  
Marca sem discurso próprio. Sem manifesto real, os três parágrafos viram texto de preenchimento e a peça fica vazia.  
Quando o produto precisa aparecer. Não existe slot de imagem.  
Público frio que ainda não sabe o que a loja vende. O manifesto pressupõe contexto.  
Marca informal ou popular — o tom da variante é contido por construção.

## Orientações de copy para a IA

A headline é uma frase só, quebrada em duas escalas. A primeira parte é curta e abre a ideia; a segunda fecha em corpo grande. Escrever como sentença contínua e depois decidir onde cortar — nunca escrever a primeira parte como rótulo.  
Três parágrafos com funções fixas: o primeiro declara a missão e cita matéria-prima ou método; o segundo diz o que o cliente ganha ao escolher; o terceiro fecha no detalhe e na pessoa.  
Cada parágrafo cabe em 2 ou 3 linhas. É a única regra rígida da copy aqui — o bloco perde a leveza com parágrafo de 4 linhas.  
Frase de manifesto, não de venda. Sem verbo no imperativo até chegar no CTA, sem percentual, sem urgência dentro dos parágrafos.  
O rótulo do cupom é uma palavra com dois-pontos. Nunca "use o código" ou frase completa — a metade tracejada é estreita.  
O aviso de prazo é vago de propósito e fica em caixa alta e corpo pequeno. É a única urgência da peça e ela não pode competir com o manifesto.  
CTA de descoberta, não de compra. "Descobrir", "conhecer", "explorar" — coerente com um bloco que não mostrou produto nenhum.

## Design system

Container: 600px travado, fundo branco chapado. Sem borda, painel, card ou divisor.  

Tipografia principal: Montserrat (fallback Arial, Helvetica, sans-serif), uma única família em todos os elementos. Não há tipografia secundária.  

| Bloco | Tamanho / entrelinha | Peso | Caixa |  
|---|---|---|---|  
| Primeira linha da headline | ~23 | 400 | ALTA |  
| Headline | ~54 / 48 | 400 | ALTA |  
| Parágrafos do manifesto | 23 / 23 | 400 | Sentença |  
| Rótulo do cupom | 30 | 400 | ALTA |  
| Código do cupom | 30 | 700 | ALTA |  
| Aviso de prazo | 17 | 400 | ALTA, tracking 0.02em |  
| Label do CTA | 24 | 400 | ALTA |  

Cores. Cor primária   
#388261 — o mesmo verde em absolutamente tudo: texto, tracejado, bloco do código e fundo do CTA. Cor secundária   
#FFFFFF, usada no fundo da peça, no código dentro do bloco verde e no label do CTA. Não há terceira cor e não há preto.  

Grade e ritmo vertical (medido):  

   ↓ 37px  
primeira linha da headline   y 37–52, centralizada  
   ↓ 11px  
headline                     2 linhas, y 63–149, entrelinha 48  
   ↓ 43px  
parágrafo 1                  3 linhas, bloco de 464px  
   ↓ 24px  
parágrafo 2                  2 linhas  
   ↓ 24px  
parágrafo 3                  3 linhas  
   ↓ 51px  
FAIXA DE CUPOM               464 × 66 (x 67–530), cantos retos  
                             metade esquerda 197 — contorno tracejado, sem preenchimento  
                             metade direita 267 — bloco chapado #388261, texto branco  
   ↓ 13px  
aviso de prazo               y 545–556, centralizado  
   ↓ 39px  
CTA                          293 × 61 (x 153–446), raio 5, fundo #388261  
   ↓ 81px  

Regras que não podem ser quebradas:  

Uma cor só. Qualquer segundo tom quebra a variante.  
As duas metades do cupom encostam sem folga e têm a mesma altura. O tracejado só existe na metade do rótulo.  
O código do cupom é a única coisa em peso 700 da peça inteira. Headline, parágrafos, rótulo e CTA são todos regulares.  
A headline tem entrelinha menor que o corpo da fonte (48 contra ~54). O aperto é o que dá a aparência editorial.  
Zero imagem, zero ícone, zero divisor, zero borda de container.  
O CTA tem raio pequeno (5) e a faixa de cupom tem canto reto. Nenhum elemento é arredondado de verdade.  
Tudo centralizado.

## Direção fotográfica

_(vazio)_

---

HTML: [[_html/offer-4-manifesto-antes-do-cupom.html]] · Seção: [[_offer]] · Protocolo: [[_protocolo-de-selecao]]
