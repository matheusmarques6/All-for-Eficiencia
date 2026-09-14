---
tipo: componente
slug: offer-1-condicao-sem-imagem
secao: offer
nome_no_banco: "offer 1"
variant_id: 3cee424b-5278-4503-9fa7-2afca3b5d13f
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [campanha-promocional]
momento_vetado: []

# --- eixos de ranking, na ordem do protocolo ---
objecao: [preco-valor]
registro: []
registro_vetado: []
paleta: []
papel_na_peca: [fecha, ponte]

# --- requisitos duros (eliminam) ---
exige: []
diretivas_de_imagem: []

# --- capacidade e composição ---
product_slots: 0
itens: null
peso: { altura_px: 400, classe: leve, fonte: medido }
convivencia: [exige-hero-ou-contexto-acima]

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: null
schema_campos: 3
status: aprovada
---

## Descrição curta

Bloco de oferta sem nenhuma imagem, para quando a peça já mostrou o produto e o que falta é declarar a condição comercial e mandar clicar. Serve como fechamento de e-mail ou como ponte entre duas seções pesadas.

## Descrição detalhada

Três elementos empilhados e centralizados sobre fundo branco: headline, um parágrafo de corpo e um CTA sólido de largura quase total. Não há painel, borda, card, ícone, divisor ou imagem — a hierarquia vem inteira de tamanho de fonte e espaço em branco.  

Dois mecanismos sustentam o bloco:  

Respiro como hierarquia. Os vãos são maiores que os elementos: 67px entre headline e corpo, 63px entre corpo e CTA. O espaço é o que separa os três blocos, já que não existe nenhum recurso gráfico fazendo isso.  
CTA desproporcional de propósito. 490 de largura contra 600 do container e 70 de altura — é o elemento mais pesado da seção, mais largo que o próprio bloco de texto. Num bloco sem imagem, o botão é o único ponto de peso visual.

## Quando usar

Fechamento de e-mail depois de uma seção rica em imagem (hero, grade de produtos, prova social).  
Anúncio de condição comercial simples que se resolve em uma frase: percentual, frete, brinde, prazo.  
Ponte entre duas seções pesadas, para o e-mail não virar um bloco visual atrás do outro.  
Campanha em que a oferta é o argumento e não precisa de reforço visual.

## Quando NÃO usar


- (nota do cadastro) offer-1 nao exige cupom; a prosa so descreve a estrutura como incompativel com cupom em destaque ("a estrutura nao tem slot de cupom") -- e veto de uso com cupom, nao requisito de cupom
Como único bloco de oferta de um e-mail promocional. Sem imagem e sem destaque de cupom, o bloco não segura sozinho o peso de uma campanha.  
Quando a oferta tem código de desconto que precisa de destaque. A estrutura não tem slot de cupom — o código teria que ser embutido no corpo do texto ou no label do botão, e nos dois casos ele perde evidência.  
Quando a oferta tem mais de uma condição ou regra. O corpo comporta 3 a 5 linhas e não aguenta letra miúda.  
No topo do e-mail. O bloco não apresenta nada, só conclui.

## Orientações de copy para a IA

Orientações de copy para a IA  
A headline carrega o valor da oferta, não o nome da campanha. É o único elemento em corpo grande e é o que o leitor lê primeiro.  
Headline em uma linha. A largura útil é de 520px em corpo 40 — passar disso quebra em duas e desmonta o equilíbrio com o vão de 67px abaixo.  
O corpo diz o que fazer e até quando, em 3 a 5 linhas. É o único lugar onde cabem prazo, condição ou regra.  
Nada de repetir a headline no corpo. Com três elementos só, redundância aparece na hora.  
O label do CTA é a ação, curta. Num botão de 490px de largura, um label longo fica solto no meio de um vão enorme; label curto centralizado é o que funciona.  
Sem emoji, sem caixa alta gritada, sem exclamação dupla. O bloco é sóbrio por construção — o peso está no tamanho, não no tom.

## Design system

_(vazio)_

## Direção fotográfica

_(vazio)_

---

HTML: [[_html/offer-1-condicao-sem-imagem.html]] · Seção: [[_offer]] · Protocolo: [[_protocolo-de-selecao]]

