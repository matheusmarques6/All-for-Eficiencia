---
tipo: componente
slug: offer-2-duas-ofertas-sazonais
secao: offer
nome_no_banco: "offer 2"
variant_id: 304bf7ce-6a23-4c68-b3a5-c37f551aaa5f
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
product_slots: 0
itens: null
peso: null
convivencia: []

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: null
schema_campos: 12
status: aprovada
---

## Descrição curta

Bloco de oferta para data comemorativa, quando a campanha tem duas ofertas diferentes rodando ao mesmo tempo. Empilha um desconto percentual e um combo de preço fechado em caixas separadas, sobre uma foto de cena que ocupa a seção inteira.

## Descrição detalhada

Faixa decorativa de estrelas no topo, sobrescrito e headline centralizados, duas caixas de oferta empilhadas, uma linha de prazo solta e um CTA com estrelas nas pontas — tudo flutuando sobre uma única foto de cena que se estende do topo ao fim da seção e cuja metade inferior fica livre, sem nenhum elemento por cima.  

Quatro mecanismos sustentam o bloco:  

Duas ofertas com papéis diferentes, em caixas diferentes. A branca carrega o desconto percentual e a mecânica ("aplicado automaticamente"); a azul carrega o combo de preço fechado e a especificação do que vem nele. São duas ofertas simultâneas, não uma oferta e um reforço.  
O prazo fica fora das caixas. A urgência é a única linha de texto solta sobre a foto entre a caixa azul e o CTA. Condição comercial dentro da caixa, prazo fora dela — a separação é o que impede a leitura de "letra miúda".  
A foto é a seção, não um elemento dela. Não há fundo próprio: um único ativo de imagem cobre os 1440px e a metade inferior é deixada respirando, com a comida em primeiro plano e nada escrito por cima.  
Motivo sazonal repetido em duas escalas. A faixa de estrelas no topo e as duas estrelas nas pontas do CTA são o mesmo elemento em tamanhos diferentes, amarrando o topo e a base sem precisar de mais nenhuma decoração.

## Quando usar

Data comemorativa com identidade visual óbvia (feriado nacional, Black Friday, Natal) onde um motivo decorativo simples já situa a campanha.  
Campanha com duas ofertas simultâneas: um desconto geral e um combo ou kit de preço fechado.  
Categoria em que a foto de cena vende sozinha — alimento, bebida, churrasco, mesa posta, decoração.  
Quando existe um prazo real e curto para declarar.

## Quando NÃO usar

Uma oferta só. Com uma caixa a estrutura fica desequilibrada e a segunda vira enchimento.  
Produto que precisa ser mostrado isolado ou em detalhe. A foto aqui é ambiente, não packshot.  
Marca sem motivo sazonal para usar na faixa e no CTA — sem ele a seção perde o que a amarra.  
Campanha sem prazo. A linha de urgência é estrutural: sem ela sobra um vão de 55px entre a caixa azul e o CTA.  
E-mail de conteúdo ou educativo. A seção é comercial da primeira à última linha.

## Orientações de copy para a IA

Sobrescrito é a data, headline é o evento. "4th Of July" em cima, "BBQ Blowout Is Live" embaixo. O sobrescrito nunca repete a palavra da headline.  
A headline declara que está no ar, não convida. É estado, não chamada — quem chama é o CTA.  
A caixa branca junta valor e mecânica: o percentual e sobre o quê, e logo abaixo como o desconto é aplicado. Se o desconto é automático, dizer — é o que remove a objeção do cupom.  
A caixa azul abre com o preço, curto e sem enrolação, e depois especifica o que está incluso em itens objetivos: quantidade, peso, formato, estado. Nada de adjetivo nessa lista.  
Title Case em toda a seção, incluindo as especificações e o prazo. Só o sobrescrito e a headline ficam em caixa alta.  
O prazo traz data e a segunda condição: "até tal dia, ou antes se acabar". A dupla condição vale mais que o relógio sozinho.  
CTA nomeia a promoção, não a loja.

## Design system

Container: 600px travado. A seção inteira é uma imagem de fundo de 600 × 1440 — não há cor de fundo própria. A cor média para fallback é   
#E4DCD1.  

Tipografia principal: sans geométrica de peso alto. Não há tipografia secundária. O template substitui por Arial, Helvetica, sans-serif.  

| Bloco | Tamanho aproximado | Peso | Caixa |  
|---|---|---|---|  
| Sobrescrito | ~38 | 700 | ALTA |  
| Headline | ~43 (tracking negativo) | 700 | ALTA |  
| Valor do desconto | ~34 | 700 no percentual, 400 no resto | Title Case |  
| Nota do desconto | ~18 | 400 | Sentença, entre parênteses |  
| Preço do combo | ~34 | 400 | Title Case |  
| Especificação do combo | ~20 / 35 | 400 | Title Case |  
| Prazo | ~24 / 35 | 400 | Title Case |  
| Label do CTA | ~23 | 700 | ALTA |  

Cores. Cor primária   
#A61D24 — vermelho usado no sobrescrito e no fundo do CTA, e em mais nada. Cor secundária   
#0A4A6D, o azul da caixa de combo.   
#FFFFFF na caixa de desconto, nas estrelas e nos textos sobre azul e vermelho;   
#000000 na headline, no valor do desconto e no prazo. A dupla vermelho/azul sobre bege é a paleta inteira.  

Grade e ritmo vertical (medido):  

faixa de estrelas   3 fileiras (y 19–97), 20 estrelas de ~18px por fileira,  
                    passo 30, fileira do meio deslocada meio passo  
   ↓  
sobrescrito         y 162–188, centralizado  
   ↓ 29px  
headline            y 217–247, centralizado  
   ↓ 40px  
CAIXA BRANCA        471 × 134 (x 64–534), cantos retos  
                      +37  valor do desconto  
                      +51  nota entre parênteses  
   ↓ 31px  
CAIXA AZUL          469 × 229 (x 64–532), cantos retos  
                      +45  preço do combo  
                      +103 especificação — 3 linhas, entrelinha 35  
   ↓ 59px  
prazo               2 linhas, entrelinha 35, solto sobre a foto  
   ↓ 40px  
CTA                 430 × 61 (x 90), cantos retos, fundo #A61D24  
                    estrela ~17px a 38px de cada borda, label centralizado  
   ↓ 553px          área livre — só a foto, nada por cima  

Regras que não podem ser quebradas:  

Zero border-radius. Caixas e CTA têm cantos retos, e as duas caixas têm a mesma largura.  
A metade inferior da seção fica livre. Escrever sobre a comida destrói a variante.  
O prazo nunca entra dentro de uma das caixas.  
Vermelho só no sobrescrito e no CTA. Azul só na caixa de combo. Nenhuma das duas cores aparece em mais nenhum lugar.  
As estrelas do CTA ficam nas duas pontas, simétricas, e são o mesmo desenho da faixa do topo.  
A faixa de estrelas tem fileiras alternadas com deslocamento de meio passo. Alinhar as três em grade reta deixa o padrão mecânico.  
Tudo centralizado. Não há alinhamento à esquerda nesta variante.

## Direção fotográfica

Uma foto só, vertical e muito alta, com dois terços de respiro em cima e a cena inteira embaixo.  

Cena: mesa posta em uso, vista em perspectiva baixa e diagonal, com o produto principal em primeiro plano sobre tábua de madeira e elementos de contexto ao redor — copos, pratos, guarnição, bebida.  
Enquadramento: a comida ancorada na base do quadro e cortada pelas bordas inferior e laterais. Nada centralizado, nada isolado.  
Terço superior: parede lisa e desfocada, sem objeto nenhum, servindo de área para o texto. É onde todo o conteúdo da seção vai ficar, então precisa estar limpa e uniforme.  
Luz: natural lateral, quente, com sombra suave. Profundidade de campo curta — o fundo desfoca, o primeiro plano fica nítido.  
Cor: paleta quente de madeira, pão e bege. A foto tem que aceitar vermelho e azul chapados por cima sem competir.  
Proibições: pessoa na cena, fundo escuro, foto de estúdio em fundo branco, produto isolado, gradiente artificial, textura de fundo com padrão.

---

HTML: [[_html/offer-2-duas-ofertas-sazonais.html]] · Seção: [[_offer]] · Protocolo: [[_protocolo-de-selecao]]
