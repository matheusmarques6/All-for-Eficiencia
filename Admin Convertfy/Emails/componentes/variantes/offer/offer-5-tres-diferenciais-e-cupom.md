---
tipo: componente
slug: offer-5-tres-diferenciais-e-cupom
secao: offer
nome_no_banco: "offer 5"
variant_id: 5a34dbaf-6710-4282-8b7b-3c03921bd6fc
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [welcome-meio]
momento_vetado: [campanha-promocional]

# --- eixos de ranking, na ordem do protocolo ---
objecao: [preco-valor]
registro: [premium-editorial]
registro_vetado: []
paleta: []
papel_na_peca: []

# --- requisitos duros (eliminam) ---
exige: [cupom-ativo, tres-diferenciais-concretos]

# --- capacidade e composição ---
product_slots: 0
itens: null
peso: { altura_px: 691, classe: medio, fonte: medido }
convivencia: []

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: null
schema_campos: 11
status: aprovada
---

## Descrição curta

Bloco de diferenciação com cupom no fim, para quando o argumento de compra é a qualidade e não o preço. Lista três diferenciais em parágrafos densos e só entrega o código depois de o leitor ter lido os três.

## Descrição detalhada

Régua fina de cor no topo, headline em duas partes — a primeira dentro de uma etiqueta chapada e a segunda solta abaixo em corpo grande —, três parágrafos de diferencial com abertura em negrito, faixa de cupom bipartida e CTA sólido. Tudo centralizado, tudo em uma cor sobre branco, sem imagem.  

Três mecanismos sustentam o bloco:  

Headline partida entre etiqueta e texto solto. A primeira metade da frase fica invertida dentro de um bloco chapado; a segunda fica embaixo, em corpo quase o dobro, na cor de fundo da etiqueta. As duas partes formam uma frase só e a inversão de cor é o que marca a quebra.  
Abertura em negrito como sub-rótulo. Cada parágrafo começa com o nome do diferencial em negrito, terminado em dois-pontos, e emenda no texto explicativo na mesma linha. É o que permite três blocos densos de quatro linhas sem virar parede de texto.  
Cupom depois do argumento. O código só aparece no penúltimo elemento, depois dos três diferenciais. O bloco não abre com desconto — abre com qualidade.

## Quando usar

Objeção de preço em marca premium: o cliente achou caro e precisa entender o que está pagando.  
Welcome de segunda ou terceira posição, depois de a marca já ter se apresentado.  
Categoria em que os diferenciais são verificáveis: matéria-prima, garantia, logística, atendimento.  
Quando existem exatamente três diferenciais fortes. Dois deixam a peça curta, quatro cansam.

## Quando NÃO usar

Campanha promocional. O cupom aqui é fechamento, não manchete, e não há slot para percentual em destaque.  
Marca sem diferencial concreto. Três parágrafos de adjetivo expõem a falta de argumento.  
Público que ainda não sabe o que a loja vende — o bloco pressupõe categoria conhecida.  
Quando o produto precisa aparecer. Não há slot de imagem.

## Orientações de copy para a IA

A headline é uma frase só, partida entre a etiqueta e o texto solto. Escrever como sentença contínua e cortar onde a etiqueta termina.  
Cada diferencial tem uma abertura nomeada em negrito, de 3 a 5 palavras, terminada em dois-pontos. Ela nomeia o diferencial, não o benefício.  
Os três diferenciais cobrem eixos distintos: o produto (matéria-prima ou método), o risco (garantia, devolução) e a experiência (entrega, atendimento, embalagem). Três variações do mesmo eixo desperdiçam o bloco.  
Cada parágrafo fecha com uma frase curta e cortada, no ritmo de negação ou de reforço — é o que impede o texto denso de ficar monótono.  
Nada de percentual ou urgência nos parágrafos. A oferta só existe na faixa de cupom.  
CTA na primeira pessoa do cliente, referindo o desconto que ele acabou de receber, não a loja.

## Design system

Container: 600px travado, fundo branco chapado. Sem borda, painel ou card.  

Tipografia principal: Montserrat (fallback Arial, Helvetica, sans-serif), família única em todos os elementos. Não há tipografia secundária.  

| Bloco | Tamanho / entrelinha | Peso | Caixa |  
|---|---|---|---|  
| Texto da etiqueta | 27 | 600 | ALTA |  
| Headline | ~53 / 42 | 700 | ALTA |  
| Abertura do diferencial | 14 / 19 | 700 | Title Case |  
| Corpo do diferencial | 14 / 19 | 400 | Sentença |  
| Rótulo do cupom | 34 | 400 | ALTA |  
| Código do cupom | 33 | 400 | ALTA |  
| Label do CTA | 24 | 400 | ALTA |  

Cores. Cor primária   
#388261 — em tudo: régua do topo, fundo da etiqueta, headline, corpo, código do cupom e CTA. Cor secundária   
#FFFFFF, no fundo da peça e nos textos sobre verde. O contorno tracejado do cupom é a única exceção, em   
#472967 (ver divergência 2).  

Grade e ritmo vertical (medido):  

régua de cor            600 × 2, no topo absoluto da seção  
   ↓ 29px  
ETIQUETA                274 × 39 (x 162–436), chapada, cantos retos  
   ↓ 3px  
headline                y 72–109, uma linha  
   ↓ 29px  
diferencial 1           4 linhas, bloco de 509px (x 45–553), entrelinha 19  
   ↓ 24px  
diferencial 2           4 linhas  
   ↓ 24px  
diferencial 3           4 linhas  
   ↓ 38px  
FAIXA DE CUPOM          451 × 64 (x 76–527), cantos retos  
                        metade esquerda 192 — contorno tracejado, sem preenchimento  
                        metade direita 259 — bloco chapado, texto branco  
   ↓ 17px  
CTA                     356 × 74 (x 125–481), raio 8  
   ↓ 35px  

Regras que não podem ser quebradas:  

A etiqueta e a headline encostam — 3px entre a base do bloco chapado e o topo das letras. Elas são uma frase só e não podem respirar entre si.  
A headline tem entrelinha bem menor que o corpo da fonte (42 contra ~53). O aperto é o que dá peso ao bloco.  
As duas metades do cupom encostam sem folga e têm a mesma altura. O tracejado só existe na metade do rótulo.  
A abertura em negrito e o corpo do diferencial ficam na mesma linha, sem quebra entre eles.  
Uma cor só em tudo. Zero imagem, ícone, divisor ou borda de container.  
Cantos retos na etiqueta e na faixa de cupom; só o CTA tem raio, e pequeno (8).  
Tudo centralizado, incluindo os parágrafos densos.

## Direção fotográfica

_(vazio)_

---

HTML: [[_html/offer-5-tres-diferenciais-e-cupom.html]] · Seção: [[_offer]] · Protocolo: [[_protocolo-de-selecao]]
