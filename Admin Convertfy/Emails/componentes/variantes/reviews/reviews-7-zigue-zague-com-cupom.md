---
tipo: componente
slug: reviews-7-zigue-zague-com-cupom
secao: reviews
nome_no_banco: "review 7"
variant_id: a8468e9f-c8d8-4c71-b416-6a4f6f5ca0f9
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [consideracao]
momento_vetado: [carrinho-abandonado, checkout-abandonado, transacional]

# --- eixos de ranking, na ordem do protocolo ---
objecao: [qualidade-eficacia]
registro: []
registro_vetado: []
paleta: [com-acento-definido]
papel_na_peca: [meio, fecha]

# --- requisitos duros (eliminam) ---
exige: [selo-compra-verificada, ativo-composto-faixa-inteira, cupom-ativo]

# --- capacidade e composição ---
product_slots: 0
itens: { min: 3, max: 3 }
peso: null
convivencia: []

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: null
schema_campos: 13
status: aprovada
---

## Descrição curta

Bloco de prova social em zigue-zague. Três depoimentos de compradores verificados, cada um com uma foto de produto que troca de lado a cada review, fechando com cupom e CTA. Momento de uso: meio ou fim de e-mail de consideração com oferta ativa, quando o argumento é atributo de produto confirmado por quem já usa.

## Descrição detalhada

Título centralizado; abaixo, três faixas de 451px cada, uma por review; no fim, a linha do cupom e o CTA de largura quase total.  

Quatro mecanismos definem a variante:  

A foto é imagem de fundo da faixa, não um <img> em coluna. Cada ativo tem 598 × 451px e já contém a composição inteira: o recorte fotográfico de um lado e a área lisa do outro. O texto é sobreposto por padding assimétrico. Isso muda a produção — não existe "foto do review" recortada, existe a faixa inteira.  

Alternância esquerda / direita / esquerda. A foto troca de lado no review do meio. O zigue-zague é o que dá ritmo ao empilhamento e distingue esta variante das seções de cards, onde todos os reviews têm a mesma orientação.  

Selo de comprador verificado em linha com o nome. Nome, espaçador de 10px, selo de 18px, espaçador de 6px, rótulo. Os espaçadores são fixos e white-space:nowrap impede a linha de quebrar. É a validação da variante — sem o selo, é depoimento sem procedência.  

Cupom e CTA fecham o bloco. Diferente das outras seções de prova social, esta termina em conversão com oferta: a linha do cupom vem em bold logo acima do botão.

## Quando usar

Consideração com oferta ativa — quando há cupom para entregar no fim do bloco.  
Quando o argumento é atributo de produto confirmado no uso: tecido, durabilidade, caimento, praticidade.  
Uniformes, activewear, moda funcional, calçado, casa, pet.  
Quando existem reviews de plataforma com selo de compra verificada.  
Quando as fotos podem ser produzidas já compostas em 598 × 451px, com metade livre para o texto.

## Quando NÃO usar

Sem selo de compra verificada — o mecanismo central fica vazio.  
Sem oferta — o bloco termina em cupom e CTA; sem eles, fecha no vazio.  
Fotos recortadas em coluna — a variante exige o ativo composto de faixa inteira. Se o acervo só tem recortes verticais, use uma seção de cards.  
Menos de três reviews — a alternância precisa dos três para formar o zigue-zague.  
Carrinho, checkout, transacional, topo de e-mail.  
Depoimento longo — o padding assimétrico deixa só 245px de largura útil.

## Orientações de copy para a IA

Título — o atributo validado em caixa alta, curto ("VET-APPROVED SCRUBS"). Diz quem aprova ou o que o produto resolve, não a marca.  

Depoimentos — fala em primeira pessoa focada em um atributo por review: o do primeiro fala do tecido, o do segundo da praticidade, o do terceiro do conforto em uso prolongado. Citar a situação profissional ou de rotina. Os três não podem repetir o mesmo atributo.  

Nomes — nome e sobrenome, ou só o primeiro nome. Caixa mista.  

Rótulo de verificação — texto fixo por loja ("Verified Buyer", "Compra verificada"). Não é copy variável por review.  

Linha do cupom — instrução com o código, em bold, uma linha.  

CTA — verbo + valor da oferta. Aqui repetir o desconto no botão é o padrão: o cupom já foi dito acima e o botão fecha.  

Proibições: três depoimentos sobre o mesmo atributo · rótulo de verificação variando entre reviews · depoimento acima do limite de caracteres · cargo ou credencial nos nomes · segundo botão · CTA dentro da faixa do review.

## Design system

Container 600px fixo, borda 1px   
#000000 opcional (flag has_border). Zero raio, zero sombra, zero gradiente aplicado por CSS.  

Estrutura  

| # | Elemento | Padding-top | Dimensão |  
|---|---|---|---|  
| 1 | Título | 59px | 34/33px bold, tracking +0.05em, caixa alta |  
| 2 | Review 1 — foto à esquerda | 49px | Faixa de 598 × 451px |  
| 3 | Review 2 — foto à direita | 44px | Faixa de 598 × 451px |  
| 4 | Review 3 — foto à esquerda | 44px | Faixa de 598 × 451px |  
| 5 | Linha do cupom | 62px | 22/25px bold |  
| 6 | CTA | 18px | 556 × 58px, com 30px de respiro na base |  

Sobreposição do texto na faixa  

| Review | Padding do bloco de texto | Largura útil |  
|---|---|---|  
| 1 e 3 (foto à esquerda) | 103px topo · 41px direita · 312px esquerda | 245px |  
| 2 (foto à direita) | 128px topo · 334px direita · 19px esquerda | 245px |  

Assinatura 25px abaixo do depoimento: nome · espaçador 10px · selo 18 × 18px · espaçador 6px · rótulo. Todos os textos com white-space:nowrap.  

Paleta — três cores.  

| Papel | Hex (referência) | Uso |  
|---|---|---|  
| Cor primária |  |  |  
| #373737 | Título e depoimentos — cinza escuro, nunca preto |  |  
| Cor secundária |  |  |  
| #000000 | Nome do comprador e selo |  |  
| Acento |  |  |  
| #658A68 | Fundo do CTA, com label branco |  |  

O nome é a única coisa em preto puro no bloco; o depoimento é cinza. A diferença de valor é o que separa fala de assinatura sem precisar de peso ou tamanho.  

Pele alternativa (HTML base): CTA preto sem cor de acento. Usar quando a marca não tem cor definida.  

Tipografia. Principal: Arial → Helvetica em todos os slots. Título 34px bold em caixa alta com tracking; depoimento 22/25px regular; nome e rótulo 18/21px regular; cupom 22px bold; CTA 25px bold com tracking +0.15em e text-indent compensando. Secundária não existe.  

Implementação. Cada faixa usa background no <td> + background-image inline com background-position: left <padding-top> e background-size:598px 451px, mais bloco VML v:rect/v:fill type="frame" para Outlook. height fixo de 451px na célula. A linha da assinatura é uma <table> com <td> espaçadores de largura fixa — não usar margin entre elementos inline, que o Outlook ignora. Selo como <img> de 18px com alt vazio: é decorativo, o rótulo textual ao lado já carrega o significado. Hacks u + .body .txt-gry e u + .body .txt-blk.  

Tags: PREHEADER, SECTION_TITLE, REVIEW_N_IMAGE_URL, REVIEW_N_QUOTE, REVIEW_N_NAME, VERIFIED_LABEL, VERIFIED_BADGE_URL, COUPON_LINE, COUPON_CODE, CTA_LABEL, CTA_URL.  

Erros que quebram o padrão: três reviews com a foto do mesmo lado · foto entregue como recorte em coluna em vez de faixa composta · texto invadindo a metade da foto · nome e depoimento na mesma cor · selo sem o rótulo textual ao lado · quebra de linha na assinatura · CTA dentro da faixa · botão com raio.

## Direção fotográfica

Proporção 4:3 — slot de 598 × 451px, ativo final 1196 × 902px (2x). JPG q80 ou WebP, < 200 KB por faixa. Gerar em 4:3 a 1204 × 903 e cortar 8px de largura, 4px de cada lado.  

Regra crítica: cada ativo é a faixa inteira composta, não um recorte de produto. Metade do quadro é o recorte fotográfico; a outra metade é superfície lisa e clara que vai receber o texto. A divisão é vertical e reta, sem degradê na emenda.  

Lado da foto: review 1 à esquerda, review 2 à direita, review 3 à esquerda. Produzir cada ativo já espelhado — não confiar em background-position para inverter.  

Composição. Recorte fechado do produto vestido: detalhe de peça, meio corpo, ou corpo parcial cortado pelas bordas. O enquadramento é vertical dentro da metade que ocupa. Fundo do recorte claro e neutro, próximo ao da metade lisa.  

Luz. Estúdio difuso, contraste baixo, sombras suaves. A metade lisa precisa de luminância acima de 88% para o cinza   
#373737 do texto assentar.  

Os três recortes precisam mostrar partes diferentes: um detalhe de tecido ou acabamento, um corpo inteiro ou meio corpo, um recorte de outra peça da linha. Três enquadramentos iguais anulam o efeito.  

Proibições: faixa entregue sem a metade lisa · emenda em degradê · fundo escuro ou saturado · texto/preço/selo queimado (exceto o selo de atributo, quando houver) · foto no lado errado do quadro · três recortes com o mesmo enquadramento · marca d'água.  

Adaptação por categoria — o que é o recorte:  

| Categoria | Recorte |  
|---|---|  
| Uniforme / activewear | Detalhe de bolso e tecido, meio corpo, calça e calçado |  
| Moda | Caimento, aviamento, look completo |  
| Calçado | Solado, pé calçado em pé, par lado a lado |  
| Casa | Textura do material, item no ambiente, detalhe de acabamento |  
| Pet | Coleira no animal, detalhe de fecho, animal em uso |  
| Beleza | Textura na pele, aplicador, embalagem em mão |

---

HTML: [[_html/reviews-7-zigue-zague-com-cupom.html]] · Seção: [[_reviews]] · Protocolo: [[_protocolo-de-selecao]]
