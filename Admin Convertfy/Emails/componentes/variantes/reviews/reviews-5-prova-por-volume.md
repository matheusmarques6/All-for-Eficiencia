---
tipo: componente
slug: reviews-5-prova-por-volume
secao: reviews
nome_no_banco: "review 5"
variant_id: f8ed9f85-f0f3-47f3-879a-2dd65aba0f86
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [consideracao, reengajamento]
momento_vetado: [carrinho-abandonado, checkout-abandonado, transacional]

# --- eixos de ranking, na ordem do protocolo ---
objecao: [adesao-social]
registro: []
registro_vetado: []
paleta: [creme]
papel_na_peca: [meio, fecha]

# --- requisitos duros (eliminam) ---
exige: [foto-de-uso-real, reviews-curtos]

# --- capacidade e composição ---
product_slots: 0
itens: { min: 3, max: 3 }
peso: { altura_px: 1992, classe: pesado, fonte: medido }
convivencia: [raio-alto-nao-convive-com-canto-vivo]

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: balanced
schema_campos: 12
status: aprovada
---

## Descrição curta

Bloco de prova social por volume. Três depoimentos de clientes comuns, cada um com uma foto do produto na casa de quem escreveu, seguidos do título da seção e do CTA. Momento de uso: meio ou fim de e-mail de consideração, quando a objeção não é técnica e sim "outras pessoas compraram e gostaram?".

## Descrição detalhada

Copy de abertura sobre fundo claro; abaixo, três cards de review empilhados; depois deles, o título da seção e o CTA. Cada card é bipartido: foto vertical à esquerda, painel escuro à direita.  

Quatro mecanismos definem a variante:  

A foto é o produto em cena, não o rosto do depoente. Garrafa na bancada, latas na varanda, produto no ambiente de quem comprou. É prova de uso doméstico, não de autoridade — o oposto da variante de cards com credencial.  

Título e CTA vêm depois dos reviews. A prova antecede a chamada; quando o leitor chega ao botão, os três depoimentos já foram lidos. Subir o título para o topo inverte a lógica e transforma o bloco em seção de catálogo.  

CTA com sombra sólida. Botão branco com borda de 2px sobre um bloco preto deslocado 10px para baixo. Não é sombra de CSS: são duas tabelas empilhadas, e é isso que garante o efeito em Outlook.  

Três cards de altura idêntica. A foto fixa a altura em 346px, o que impõe um teto rígido ao depoimento. É a restrição que mantém os três cards visualmente iguais.

## Quando usar

Consideração e reengajamento, depois de o produto já ter sido apresentado.  
Quando existe volume de reviews de clientes comuns com nome e foto de uso.  
Alimentos, bebidas, casa, pet, beleza, produtos de consumo recorrente.  
Quando o argumento é adesão social — "muita gente gostou" — e não credencial técnica.  
Quando as fotos disponíveis mostram o produto em ambiente doméstico real.

## Quando NÃO usar

Objeção técnica ou de segurança — use a variante de cards com credencial, onde o rosto e o cargo carregam o argumento.  
Menos de três reviews — a variante depende do efeito de volume.  
Sem foto de uso real — packshot repetido três vezes vira grade de produto.  
Depoimentos longos demais — a altura fixa de 346px corta o texto.  
Carrinho, checkout, transacional, topo de e-mail.  
No mesmo e-mail que blocos de cantos vivos — a variante usa raio em duas medidas.

## Orientações de copy para a IA

Copy de abertura — posicionamento do produto em três linhas, caixa alta. Diz o que o produto entrega e para qual ocasião. É a única fala da marca no bloco.  

Depoimentos — fala de cliente em primeira pessoa, entre aspas, mencionando ocasião de uso ("aniversário", "noite de jogos", "beira da piscina"). Ocasião é mais persuasiva que atributo neste bloco. Os três precisam citar ocasiões diferentes — a repetição derruba a sensação de volume.  

Nomes — nome e sobrenome em caixa alta, precedidos de travessão. Sem cargo, sem credencial: aqui a força é ser gente comum.  

Título da seção — chamada em caixa alta que fecha o argumento e prepara o clique.  

CTA — verbo genérico em caixa alta.  

Proibições: credencial ou cargo nos nomes · depoimento acima do limite de caracteres · três depoimentos com a mesma ocasião · desconto ou cupom · CTA dentro do card · nota abaixo de cinco estrelas · título da seção acima dos reviews.

## Design system

Container 600px fixo, borda 1px   
#000000 opcional (flag has_border). Raio de 16px nos cards e 10px no CTA — variante com cantos arredondados.  

Estrutura  

| # | Elemento | Padding-top | Dimensão |  
|---|---|---|---|  
| 1 | Copy de abertura | 35px | 22/27px, padding lateral 83px |  
| 2 | Review 1 | 77px | 540px |  
| 3 | Review 2 | 48px | 540px |  
| 4 | Review 3 | 48px | 540px |  
| 5 | Título da seção | 97px | 30/33px bold, caixa alta |  
| 6 | CTA | 27px | 447 × 61px, com 80px de respiro na base |  

Anatomia do card — duas colunas, 540px no total.  

| Coluna | Largura | Conteúdo |  
|---|---|---|  
| Foto | 241px | Imagem 241 × 346px, raio 16px só à esquerda |  
| Painel | 299px | Fundo escuro, raio 16px só à direita |  

Interior do painel, padding 40px no topo, 34px à direita, 49px na base e 26px à esquerda: estrelas 15px com tracking +7px · depoimento 27px abaixo, 22/27px, entre aspas · nome 26px abaixo, 20/27px bold, com recuo de 7px.  

CTA com sombra sólida: tabela externa de 447px na cor primária com raio 10px, contendo a tabela do botão (fundo claro, borda de 2px, raio 10px) e uma linha de 10px abaixo dela. O <a> mede 443 × 57px para caber dentro da borda.  

Paleta — três cores.  

| Papel | Hex (Willie's) | Uso |  
|---|---|---|  
| Cor primária |  |  |  
| #374256 | Fundo do painel do card e todo o texto sobre o fundo claro |  |  
| Cor secundária |  |  |  
| #FAF7F0 | Fundo da seção — off-white quente |  |  
| Neutro invertido |  |  |  
| #FFF8EE | Estrelas, depoimento e nome dentro do painel |  |  

O branco do painel é off-white, não   
#FFFFFF — casa com o fundo da seção e tira a dureza do contraste. Não existe cor de acento: as estrelas usam o mesmo branco do texto.  

Pele alternativa (HTML base): seção branca, painel   
#000000, texto preto sobre o fundo. Usar quando a marca é neutra.  

Tipografia. Principal: Arial → Helvetica em todos os slots. Copy de abertura e título em caixa alta; depoimento em caixa mista; nome em bold. Secundária não existe.  

Implementação. border-radius parcial não renderiza em Outlook: a foto precisa sair do Figma com o canto esquerdo já arredondado e o painel degrada para retângulo. background:#EFEFEF na <img> como fallback. font-size:0;line-height:0 na célula da foto. Estrelas em &#9733; com tracking, nunca imagem. O CTA com sombra depende de duas tabelas aninhadas — não substituir por box-shadow. Hacks u + .body .txt-blk e u + .body .txt-wht.  

Tags: PREHEADER, SECTION_INTRO, REVIEW_N_IMAGE_URL, REVIEW_N_IMAGE_ALT, REVIEW_N_QUOTE, REVIEW_N_NAME, SECTION_TITLE, CTA_LABEL, CTA_URL.  

Erros que quebram o padrão: raio nos quatro cantos de cada metade · cards com alturas diferentes · box-shadow no lugar da tabela empilhada · branco puro no painel · título da seção antes dos reviews · CTA dentro do card · dois cards em vez de três · foto horizontal · packshot em fundo branco.

## Direção fotográfica

7. Direção fotográfica  

Proporção 2:3 — slot de 241 × 346px, ativo final 482 × 692px (2x). JPG q80 ou WebP, < 120 KB por card. Gerar em 2:3 a 482 × 723 e cortar 31px de altura pela base.  

Regra crítica: o produto tem que estar em ambiente doméstico real, não em estúdio. Bancada, mesa de varanda, parapeito de janela, deck de madeira. É o que separa este bloco de uma grade de produtos.  

Composição. Produto em primeiro plano, vertical, ocupando o terço central do quadro. Contexto ao redor: fruta, copo servido, utensílio, elemento da ocasião. Enquadramento fechado — sem espaço negativo estrutural, já que a foto não recebe texto.  

Cenário e luz. Luz natural de janela ou ambiente externo. Sombras suaves. Fundo de madeira, azulejo, pedra ou vegetação, levemente desfocado.  

Produto. Rótulo legível e voltado para a câmera. Pode aparecer sozinho ou em conjunto (garrafa, latas, kit).  

Os três quadros precisam ser distintos. Ocasiões, cenários e horários diferentes — um interior, um exterior, um de detalhe. Três fotos com o mesmo enquadramento anulam o efeito de volume que a variante existe para criar.  

Proibições: fundo branco de estúdio · packshot flutuando · pessoa em primeiro plano · texto/preço/selo queimado · foto horizontal · três quadros com a mesma composição · marca d'água.  

Adaptação por categoria — o que é a cena:  

| Categoria | Cena |  
|---|---|  
| Bebidas | Garrafa ou lata servida, fruta e copo ao lado |  
| Alimentos | Prato montado na mesa de casa |  
| Casa | Item instalado ou em uso no ambiente |  
| Beleza | Produto na bancada do banheiro, luz de janela |  
| Pet | Produto ao lado do animal, chão de casa |  
| Ferramenta | Ferramenta na bancada com o trabalho ao redor |

---

HTML: [[_html/reviews-5-prova-por-volume.html]] · Seção: [[_reviews]] · Protocolo: [[_protocolo-de-selecao]]
