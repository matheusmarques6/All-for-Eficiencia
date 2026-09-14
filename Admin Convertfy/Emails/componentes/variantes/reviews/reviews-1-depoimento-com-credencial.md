---
tipo: componente
slug: reviews-1-depoimento-com-credencial
secao: reviews
nome_no_banco: "review 1"
variant_id: d48deaa4-6d8b-4a09-95fb-e512b676c8d8
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [consideracao, welcome-meio, reengajamento]
momento_vetado: [carrinho-abandonado, checkout-abandonado, transacional]

# --- eixos de ranking, na ordem do protocolo ---
objecao: [qualidade-eficacia]
registro: []
registro_vetado: []
paleta: [com-acento-definido]
papel_na_peca: [meio]

# --- requisitos duros (eliminam) ---
exige: []
diretivas_de_imagem: []
requisitos_de_reviews: [depoimento-com-credencial, foto-do-depoente]

# --- capacidade e composição ---
product_slots: 0
itens: { min: 2, max: 2 }
peso: { altura_px: 1009, classe: medio, fonte: medido }
convivencia: [raio-alto-nao-convive-com-canto-vivo]

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: null
schema_campos: 10
status: aprovada
---

## Descrição curta

Bloco de meio de e-mail que resolve objeção de confiança com depoimento de autoridade. Cada card traz o rosto de quem fala, o depoimento, a nota em estrelas e — o que define a variante — o cargo ou credencial da pessoa. Momento de uso: consideração, quando o produto já foi apresentado e o que falta é alguém confiável dizendo que funciona.

## Descrição detalhada

Título e copy introdutória sobre fundo claro; abaixo, dois cards de depoimento empilhados. Cada card é bipartido: fotografia vertical à esquerda, painel escuro com o texto à direita.  

Quatro mecanismos definem a variante:  

Cantos arredondados só nas bordas externas. Raio de 22px na esquerda da foto e na direita do painel; a emenda entre os dois é reta. O card lê como uma peça só, não como dois elementos encostados.  

Contraste invertido em relação à seção. A seção é clara e os cards são escuros. É o que faz o depoimento saltar sem precisar de borda, sombra ou moldura.  

O slot de credencial é obrigatório. Nome e cargo em linhas separadas, com o cargo em corpo muito menor. Sem a credencial, o bloco vira prova social genérica e perde a função — o argumento é a autoridade de quem fala, não a satisfação do cliente.  

Slot repetível de dois cards. Estrutura idêntica; muda só o conteúdo. Um card sozinho não sustenta o padrão, três alongam demais a peça.

## Quando usar

Consideração, depois de o produto já ter sido apresentado no mesmo e-mail ou na régua.  
Quando existe prova social de autoridade real — profissional, especialista, técnico certificado.  
Pet, suplementos, saúde, beleza clínica, eletrônico, casa — categorias com objeção de eficácia ou segurança.  
Welcome #3 ou #4, e-mail de USP, reengajamento com argumento.  
Quando há foto do depoente disponível: o rosto é metade do argumento.

## Quando NÃO usar

Sem credencial. Depoimento de cliente comum não sustenta a variante — o slot de cargo fica vazio e a estrutura perde o sentido.  
Sem foto do depoente. Placeholder ou avatar genérico derruba a credibilidade que o bloco existe para construir.  
Topo de e-mail — não tem logo, headline de campanha nem CTA.  
Carrinho, checkout, transacional.  
Categoria sem objeção de eficácia — em compra por impulso ou estética, o bloco alonga sem converter.  
Quando só existe um depoimento: um card sozinho parece erro de montagem.

## Orientações de copy para a IA

Título — quem recomenda, em uma linha ("Recommended by Vets", "Aprovado por dermatologistas"). É a promessa de autoridade e precisa ser verificável.  

Copy introdutória — dois parágrafos curtos: o primeiro contextualiza quem são os depoentes e o que observaram; o segundo projeta o resultado para o leitor. Frases curtas.  

Depoimento — fala em primeira pessoa, específica sobre o que o produto resolve. Mencionar ingrediente, mecanismo ou situação de uso. Sem superlativo vago.  

Nome — nome do depoente com o tratamento profissional quando houver ("Dr. Carin Beene").  

Função — credencial ou cargo, abreviado. É o slot que legitima; nunca deixar vazio nem preencher com "Cliente".  

Estrelas — sempre cinco. Nota menor dentro de um bloco de recomendação envia sinal contraditório.  

Proibições: depoimento inventado ou não atribuível · credencial genérica ("Cliente satisfeito") · desconto ou cupom em qualquer slot · CTA dentro do card · nota abaixo de cinco estrelas · superlativo sem objeto.

## Design system

Container 600px fixo, borda 1px   
#000000 opcional (flag has_border). Raio de 22px nos cards — variante com cantos arredondados; não combinar no mesmo e-mail com blocos de cantos vivos.  

Estrutura  

| # | Elemento | Padding-top | Dimensão |  
|---|---|---|---|  
| 1 | Título | 60px | 25/37px, caixa alta, padding lateral 69px |  
| 2 | Copy introdutória | 35px | 20/29px, padding lateral 69px |  
| 3 | Card de review 1 | 45px | 541px de largura, padding lateral 28/29px |  
| 4 | Card de review 2 | 31px | 541px, com 70px de respiro na base |  

Anatomia do card — duas colunas, 541px no total.  

| Coluna | Largura | Conteúdo |  
|---|---|---|  
| Foto | 241px | Imagem 241 × 349px, raio 22px só à esquerda |  
| Painel | 300px | Fundo escuro, raio 22px só à direita |  

Interior do painel, padding 30px no topo e 19/20px nas laterais:  

| Elemento | Padding-top | Dimensão |  
|---|---|---|  
| Aspas | 0 | Serif 52px bold, line-height 17px, recuo de 11px |  
| Depoimento | 31px | 20/27px |  
| Estrelas | 18px | 21px, tracking +9px |  
| Nome | 16px | 20/27px |  
| Função | 4px | 10/14px |  
| Respiro final | — | 36px |  

Paleta — quatro cores.  

| Papel | Hex (Wuffes) | Uso |  
|---|---|---|  
| Cor primária |  |  |  
| #17443D | Fundo do painel do card |  |  
| Cor secundária |  |  |  
| #F7ECE1 | Fundo da seção |  |  
| Acento |  |  |  
| #C5FB54 | Aspas e estrelas |  |  
| Neutro invertido |  |  |  
| #FFFFFF | Depoimento, nome e função |  |  

O acento aparece apenas nas aspas e nas estrelas — dois elementos gráficos, nunca em texto corrido nem em fundo. O título usa a cor primária sobre a secundária.  

Pele alternativa (HTML base): seção   
#E1DEDE, painel   
#404040, aspas e estrelas em branco, sem cor de acento. Usar quando a marca não tem cor de acento saturada.  

Tipografia. Principal: Arial → Helvetica em título, copy, depoimento, estrelas, nome e função. Secundária: serif (Georgia → Times New Roman) em uso único — as aspas de abertura. Título 25px em caixa alta com tracking −0.011em; função em 10px, metade do corpo do nome. A hierarquia nome/função é de tamanho, não de peso.  

Implementação. border-radius parcial (22px 0 0 22px / 0 22px 22px 0) não renderiza em Outlook: a foto precisa sair do Figma com o canto esquerdo já arredondado e o painel degrada para retângulo — degradação aceita, não corrigir com imagem de fundo. background:#EFEFEF na <img> como fallback de carregamento. font-size:0;line-height:0 na célula da foto para matar o gap do Outlook. Estrelas em caractere Unicode &#9733; com tracking, não imagem. Hacks u + .body .txt-blk e u + .body .txt-wht travando as duas cores no Gmail iOS.  

Tags: SECTION_TITLE, SECTION_COPY, REVIEW_N_IMAGE_URL, REVIEW_N_IMAGE_ALT, REVIEW_N_QUOTE, REVIEW_N_NAME, REVIEW_N_ROLE.  

Erros que quebram o padrão: raio nos quatro cantos de cada metade · painel e foto com alturas diferentes · slot de função vazio · acento em texto corrido · CTA dentro do card · borda ou sombra no card · três ou mais cards · nota abaixo de cinco estrelas · foto horizontal.

## Direção fotográfica

Proporção 2:3 — slot de 241 × 349px, ativo final 482 × 698px (2x). JPG q80 ou WebP, < 120 KB por card. Gerar em 2:3 na altura de 698px (465 × 698) e ampliar para 482px de largura, ou gerar em 2:3 a 482 × 723 e cortar 25px de altura pela base.  

Regra crítica: retrato real do depoente, não modelo genérico nem banco de imagem. A variante inteira depende de o rosto ser atribuível ao nome e à credencial embaixo.  

Composição. Retrato vertical, meio corpo ou busto, figura centralizada e olhando para a câmera. Expressão aberta e confiante. O enquadramento é estreito — o rosto ocupa o terço superior e precisa sobreviver a 241px de largura.  

Cenário e luz. Contexto que reforce a credencial: jaleco, estetoscópio, ambiente de trabalho, campo. Luz natural, fundo desfocado. Não é estúdio: o cenário é parte da prova.  

Elemento de credencial. Ao menos um marcador visual da profissão no quadro. É o que casa a foto com o slot de função.  

Proibições: foto de banco de imagem genérica · retrato sem contexto profissional · foto horizontal ou quadrada · rosto fora do terço superior · texto ou selo queimado · avatar ilustrado · marca d'água.  

Adaptação por categoria — qual é a autoridade:  

| Categoria | Depoente e contexto |  
|---|---|  
| Pet | Veterinário, jaleco e ambiente clínico ou de campo |  
| Suplementos | Nutricionista ou médico, consultório |  
| Beleza clínica | Dermatologista ou esteticista, clínica |  
| Eletrônico | Técnico ou instalador, bancada de trabalho |  
| Casa | Arquiteto ou marceneiro, ambiente de obra |  
| Esporte | Preparador físico, academia ou quadra |

---

HTML: [[_html/reviews-1-depoimento-com-credencial.html]] · Seção: [[_reviews]] · Protocolo: [[_protocolo-de-selecao]]
