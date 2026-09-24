---
tipo: componente
slug: body-2-colagem-de-data-comemorativa
secao: body
nome_no_banco: "body 2 - bridge textos linha produtos"
variant_id: d5fb804f-8934-4c39-b011-950e20802498
ativa: true
dispositivo: cena_de_uso

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [sazonal-data-comemorativa]
momento_vetado: [carrinho-abandonado, checkout-abandonado, transacional]

# --- eixos de ranking, na ordem do protocolo ---
objecao: []  # "argumento é a cena, não o preço nem a especificação" -- nenhum valor do vocabulario de objecao descreve gatilho emocional/afeto de presente; ver relatorio
registro: [festivo]
registro_vetado: [premium-editorial]
paleta: [com-acento-definido]
papel_na_peca: []  # nenhuma frase de Quando usar/NÃO usar declara posição na peça

# --- requisitos duros (eliminam) ---
exige: [motivo-sazonal]
diretivas_de_imagem: [foto-com-pessoas]

# --- capacidade e composição ---
product_slots: 0
itens: { min: 2, max: 2 }
peso: { altura_px: 1665, classe: pesado, fonte: medido }
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

Duas fitas diagonais anunciam a data, um texto pinta a cena de uso e uma colagem de duas fotos inclinadas mostra a família com o produto. Momento de uso: Black Friday, Natal ou datas de presente, quando a compra é motivada por afeto e não por especificação.

## Descrição detalhada

Faixa de fitas diagonais, título em duas linhas, um parágrafo de cena, colagem de fotos, um parágrafo de urgência e o CTA.  

Quatro mecanismos definem a variante:  

Fitas e colagem são ativos de imagem, não CSS. transform:rotate() e position:absolute não funcionam em cliente de e-mail — o HTML de referência é preview de Figma, não peça enviável. A faixa de fitas vira um ativo de 600 × 200px e a colagem vira um ativo de 470 × 360px, ambos com as rotações e sombras já aplicadas.  

Dois parágrafos com funções opostas. O primeiro pinta a cena — "imagine sua família..." — e o segundo avisa que vai acabar. Emoção antes, urgência depois, com a colagem entre os dois servindo de prova visual da cena descrita.  

A colagem sobrepõe, não alinha. As duas fotos têm inclinações contrárias, alturas diferentes e se cruzam. Alinhá-las lado a lado transforma o bloco em grade de duas colunas e mata o ar de álbum.  

A repetição na fita é o ornamento. O nome da data se repete alternando peso regular e bold. Não há logo, não há selo — a fita é o único elemento de campanha.

## Quando usar

Moda infantil e familiar, pijamas, casa, brinquedos, pet — categorias de compra por afeto.  
Quando existe fotografia de família ou de grupo usando o produto.  
Quando a marca aceita ornamento gráfico forte no topo.  
Quando o argumento é a cena, não o preço nem a especificação.

## Quando NÃO usar

Sem fotografia de pessoas — packshot na colagem esvazia o bloco.  
Produto individual sem contexto de grupo — a colagem precisa de duas cenas que conversem.  
Marca premium ou editorial — fitas repetidas e fotos tortas são registro festivo.  
Fora de data comemorativa — a fita pede um nome de campanha; sem ele, vira enfeite.  
Carrinho, checkout, transacional, prova social, catálogo.  
Quando a produção não puder montar os ativos: sem eles, o bloco não se sustenta em HTML puro.

## Orientações de copy para a IA

Texto da fita — o nome da campanha repetido, separado por ponto médio, alternando peso regular e bold. Sete repetições cobrem a largura.  

Título — duas linhas ligando a data ao sentimento. Sem percentual, sem nome de produto.  

Parágrafo 1 — a cena, em segunda pessoa, começando por um convite a imaginar. Quatro linhas. É o único slot do arsenal onde exclamação é bem-vinda; até duas.  

Parágrafo 2 — a urgência, em três linhas, terminando na ruptura de estoque. Muda o registro de afetivo para prático.  

CTA — verbo + nome da campanha, caixa alta.  

Proibições: percentual ou cupom no título · parágrafos com a mesma função · nome de produto na fita · contagem regressiva · exclamação no parágrafo 2 · segundo botão.

## Design system

Container 600px fixo, borda 1px   
#000000. Raio de 5px no CTA; demais elementos com cantos vivos.  

Estrutura  

| # | Elemento | Padding | Dimensão |  
|---|---|---|---|  
| 1 | Faixa de fitas | 0 | 600 × 200px |  
| 2 | Título | 20px topo · 38px laterais | 28/31px bold, 2 linhas |  
| 3 | Parágrafo 1 | 22px topo · 56px laterais | 22/27px, 4 linhas |  
| 4 | Colagem | 44px topo · 40px base | 470 × 360px |  
| 5 | Parágrafo 2 | 56px laterais | 22/27px, 3 linhas |  
| 6 | CTA | 35px topo · 45px base | 350 × 55px, borda 2px, raio 5px |  

Paleta — três cores.  

| Papel | Hex (Holy Pals) | Uso |  
|---|---|---|  
| Cor primária |  |  |  
| #DFDAE0 | Fundo da seção |  |  
| Cor secundária |  |  |  
| #151515 | Título, CTA e o texto sobre a fita |  |  
| Acento |  |  |  
| #FAE25E | Fundo das fitas |  |  

O corpo dos parágrafos usa preto puro; o título usa o   
#151515, quase preto. O acento aparece só nas fitas — é o único ponto de saturação da peça, e é ele que marca a campanha.  

Pele alternativa (HTML base): fundo   
#F3F3F3, fitas pretas com texto branco. Usar quando a marca não tem cor de campanha definida.  

Tipografia. Principal: Arial → Helvetica em todos os slots. Título 28px bold; parágrafos 22px regular; fita 20px alternando regular e bold; CTA 25px bold com tracking −0.25px. Secundária não existe.  

Implementação. Este é o ponto crítico da variante: o HTML de referência usa position:absolute, transform:rotate(), box-shadow e object-fit, e nenhum deles é confiável em cliente de e-mail. A conversão obrigatória:  

A faixa de fitas vira uma <img> de 600 × 200px.  
A colagem inteira vira uma <img> de 470 × 360px, com as duas fotos, rotações, molduras e sombras compostas no arquivo.  
O CTA usa v:roundrect com arcsize="9%" no bloco MSO.  
A media query de 620px pode ficar, mas o container de 600px do arsenal não depende dela.  

Com a colagem virando ativo único, o bloco perde texto vivo em dois pontos — o alt da colagem precisa carregar a descrição da cena.  

Tags: RIBBON_TEXT, RIBBON_IMAGE_URL, SECTION_TITLE, SECTION_COPY_1, COLLAGE_IMAGE_URL, COLLAGE_IMAGE_ALT, SECTION_COPY_2, CTA_LABEL, CTA_URL.  

Erros que quebram o padrão: manter transform:rotate() no HTML enviado · fotos da colagem alinhadas em vez de sobrepostas · colagem como duas <img> separadas · fita sem repetição · acento fora das fitas · parágrafo de urgência antes da colagem · segundo botão · CTA sem v:roundrect.

## Direção fotográfica

Colagem  

Proporção 4:3 — slot de 470 × 360px, ativo final 940 × 720px (2x). PNG, < 260 KB.  

O ativo é composto, não fotografado: duas fotos de 200 × 255px em molduras brancas, inclinadas em sentidos contrários, sobrepostas, com sombra projetada suave. Fundo transparente não é confiável — o arquivo sai com o fundo já na cor primária da seção.  

Montagem: foto da esquerda rotacionada −4°, posicionada a 20px da borda esquerda e 30px do topo; foto da direita rotacionada +6°, a 20px da borda direita e 70px do topo. Moldura branca de 14px em volta de cada uma, sombra de 4px de deslocamento e 11px de desfoque a 25% de opacidade.  

Fotos base — proporção 4:5  

Slot de 200 × 255px cada, dentro da colagem. Ativo de 400 × 510px (2x) antes da montagem.  

Composição. Cena doméstica real com pessoas usando o produto. As duas precisam mostrar escalas diferentes de vínculo: uma em plano fechado, com duas pessoas em contato — abraço, colo, rosto junto —, e outra em plano aberto com o grupo completo posado.  

Cenário e luz. Interior de casa, luz natural de janela, tons claros e quentes. Chão, tapete, cama, sofá. Nada de estúdio.  

Produto. Vestido por todos os presentes na cena, em estampa ou cor coordenada. É o que faz o argumento de "família combinando" funcionar sem precisar dizer.  

Proibições: fundo de estúdio · pessoas sem o produto · as duas fotos na mesma escala · sombra dura · texto/preço/selo queimado · marca d'água.  

Adaptação por categoria — o que são as duas cenas:  

| Categoria | Plano fechado | Plano aberto |  
|---|---|---|  
| Pijama / moda familiar | Abraço entre dois | Grupo completo posado |  
| Brinquedos | Criança concentrada no brinquedo | Família brincando junto |  
| Casa | Detalhe de uso na mesa | Ambiente com todos reunidos |  
| Pet | Tutor e animal juntos | Família com o pet |  
| Alimentos | Momento de provar | Mesa posta com todos |  
| Presentes | Mão abrindo a caixa | Troca de presentes |

---

HTML: [[_html/body-2-colagem-de-data-comemorativa.html]] · Seção: [[_body]] · Protocolo: [[_protocolo-de-selecao]]
