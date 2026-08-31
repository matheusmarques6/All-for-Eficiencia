---
tipo: componente
slug: hero-5-cupom-em-tres-lugares
secao: hero
nome_no_banco: "welcome - hero section 5"
variant_id: 8858709f-ef36-45d8-98f4-7d8711628cba
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [welcome-1]
momento_vetado: [carrinho-abandonado, checkout-abandonado, browse-abandonment, transacional, sazonal-data-comemorativa, lancamento]

# --- eixos de ranking, na ordem do protocolo ---
objecao: [preco-valor]
registro: [volume-impulso, popular-informal]
registro_vetado: [premium-editorial]
paleta: []
papel_na_peca: [abre]

# --- requisitos duros (eliminam) ---
exige: [cupom-ativo, foto-com-pessoas]

# --- capacidade e composição ---
product_slots: 0
itens: null
peso: { altura_px: 2450, classe: peca-inteira, fonte: medido }
convivencia: [raio-alto-nao-convive-com-canto-vivo]

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

foco no resgate do cupom. O código aparece três vezes — barra do topo, pílula na linha da oferta e label do CTA — e a foto lifestyle entra na base como prova de uso. Momento de uso: welcome #1 de marca de volume ou ticket baixo, logo após o opt-in, quando o objetivo é conversão imediata e não construção de marca.

## Descrição detalhada

Barra de cupom de 69px no topo; abaixo, um bloco de 1217px cujo fundo é um ativo composto — faixa de cor chapada na parte superior e fotografia lifestyle na base. Logo, headline, descrição, linha do cupom e CTA são sobrepostos à faixa chapada.  

Quatro mecanismos definem a variante:  

Cantos arredondados em tudo. Pílula do código com raio de 50px, CTA com raio de 50px, imagem principal com raio de 55px. É a única variante do arsenal com raio — misturar com blocos de cantos vivos no mesmo e-mail quebra a peça.  

O código do cupom vive dentro de uma pílula sólida. Contêiner com fundo próprio e contraste invertido, ao lado do rótulo "Use code". É o inverso das variantes editoriais, onde o código não tem contêiner nenhum.  

O cupom se repete três vezes. Barra, pílula e CTA. A redundância é deliberada: quem escaneia pega o código em qualquer altura da peça.  

A foto entra por baixo do texto, dentro do mesmo ativo de fundo. A faixa chapada superior e a fotografia formam um arquivo só — não há emenda porque não há dois elementos.

## Quando usar

Email com cupom, em marca de volume, ticket baixo ou compra por impulso.  
Alimentos e bebidas, suplementos, pet, brinquedos, casa, moda casual.  
Quando o código é longo ou personalizado e precisa de contêiner para ser lido.  
Quando a marca tem identidade descontraída que comporta pílulas e cor saturada.  
Quando existe foto lifestyle com pessoa usando ou consumindo o produto.

## Quando NÃO usar

Marca premium ou editorial. Raio de 50px, cor saturada e cupom repetido três vezes derrubam o posicionamento.  
Sem cupom — a estrutura inteira gira em torno do código.  
No mesmo e-mail que blocos de cantos vivos — a mistura de raio e canto reto na mesma peça denuncia montagem.  
Carrinho, checkout, browse, transacional.  
Campanha sazonal ou lançamento — não há slot para tema.  
Quando a única foto disponível é packshot ou flat-lay: a variante pede pessoa em cena.

## Orientações de copy para a IA

Barra do topo — instrução com o código e o valor da oferta na mesma linha. É a primeira leitura da peça e tem que ser autossuficiente.  

Headline — duas linhas: linha 1 é a saudação curta, linha 2 é o nome do grupo ou da comunidade em caixa alta. Leitura contínua entre as duas ("Welcome" + "TO THE FLAVOR CLUB"). Sem ponto final.  

Descrição — duas a três linhas explicando o que o contato ganhou ao entrar, com o valor da oferta em bold. Tom de conversa, primeira pessoa do plural aceitável.  

Linha do cupom — rótulo curto ("Use code") + o código dentro da pílula. O rótulo nunca entra na pílula.  

CTA — verbo + valor da oferta. Aqui repetir o desconto no botão é o padrão: é o terceiro reforço e o fecho da peça.  

Proibições: contagem regressiva · exclamação em mais de um slot · brand story longa · segundo botão · código fora da pílula · headline em uma linha só.

## Design system

6. Design system  

Container 600px fixo, borda 1px   
#000000 opcional (flag has_border). Preheader oculto obrigatório. Raio de 50px em pílulas e CTA, 55px na imagem principal — esta variante é a exceção à regra de cantos vivos do arsenal.  

Estrutura  

| # | Elemento | Altura |  
|---|---|---|  
| 1 | Barra do cupom | 69px, cor sólida |  
| 2 | Corpo com ativo de fundo composto | 1217px |  

Zonas internas do corpo  

| Zona | Faixa | Conteúdo |  
|---|---|---|  
| Chapada | 0 – 585px (topo 48%) | Cor sólida dentro do ativo. Recebe todo o overlay. |  
| Fotografia | 585 – 1217px (base 52%) | Cena lifestyle. Nenhum elemento sobreposto. |  

Overlay  

| Elemento | Padding-top | Dimensão |  
|---|---|---|  
| Logo | 57px | 152 × 48px |  
| Headline (2 linhas) | 57px | 50/57px, tracking −0.06em, padding lateral 24px |  
| Descrição | 34px | 25/30px, 2 linhas, padding lateral 58px |  
| Linha do cupom | 33px | Rótulo + gap de 24px + pílula 165 × 50px |  
| CTA | 43px | 523 × 78px |  
| Imagem principal | 70px | 534 × 534px, raio 55px |  

Paleta — três cores.  

| Papel | Hex (Cuso's) | Uso |  
|---|---|---|  
| Cor primária |  |  |  
| #000000 | Fundo da faixa chapada e do bloco de texto |  |  
| Cor secundária |  |  |  
| #CBB995 | Fundo da barra do topo e da pílula do código |  |  
| Acento |  |  |  
| #B9250B | Fundo do CTA e da pílula do código dentro da barra |  |  

Regras: a secundária e o acento nunca trocam de lugar — a secundária é sempre o contêiner passivo (barra, pílula no corpo) e o acento é sempre o elemento clicável ou o destaque na barra. O texto sobre a primária é branco; sobre a secundária, na cor primária; sobre o acento, branco.  

Pele alternativa (HTML base): faixa chapada branca, texto e pílulas pretos, barra   
#393737. Usar quando a marca não tem cor de acento saturada.  

Tipografia — três famílias.  

Principal: sans, fallback Arial → Helvetica. Cobre barra, linha 2 da headline, linha do cupom e CTA.  
Secundária: script pesado. Logo e linha 1 da headline.  
Terciária: serif. Descrição e código — opcional; a pele do HTML base usa a sans em todos os slots.  

Implementação. background no <td> + background-image inline + background-size:598px 1217px, background-color na cor primária como fallback, bloco VML v:rect/v:fill type="frame" para Outlook. Pílula e CTA exigem v:roundrect com arcsize="50%" no bloco condicional MSO — sem isso o Outlook renderiza retângulo. border-radius na <img> não funciona em Outlook; a imagem principal precisa ser exportada com os cantos já arredondados e background:#ABABAB como fallback. Hack u + .body .txt-blk para o Gmail iOS.  

Tags: PREHEADER, BANNER_TEXT, COUPON_CODE, OFFER_VALUE, LOGO_URL, HEADLINE_L1, HEADLINE_L2, HERO_DESCRIPTION, COUPON_LABEL, CTA_LABEL, CTA_URL, HERO_IMAGE_URL, MAIN_IMAGE_URL, MAIN_IMAGE_ALT.  

Erros que quebram o padrão: misturar cantos vivos e arredondados no mesmo e-mail · pílula sem v:roundrect no MSO · border-radius só via CSS na imagem · rótulo "Use code" dentro da pílula · trocar acento e secundária de papel · quarta cor · segundo botão · omitir o desconto do CTA (é o terceiro reforço) · emenda visível entre a faixa chapada e a foto.

## Direção fotográfica

Proporção 1:1 — slot de 598 × 632px na base do ativo de fundo, ativo final 1196 × 1264px (2x). JPG q80 ou WebP, < 280 KB. Gerar em 1:1 a 1264 × 1264 e cortar 68px de largura, 34px de cada lado, para chegar ao ativo final.  

Montagem: a fotografia é composta sob uma faixa chapada de 585px na cor primária para formar o ativo de fundo de 598 × 1217px. A transição entre faixa e foto é um corte reto, sem degradê — a foto tem que começar com uma linha visualmente calma para o corte não chamar atenção.  

Regra crítica: a foto não recebe nenhum texto. Toda a legibilidade está resolvida na faixa chapada acima, o que libera a fotografia para ter contraste alto e cor saturada.  

Composição. Pessoa em cena de consumo ou uso real, meio corpo, olhando para a câmera ou para o produto. O produto aparece grande e nítido nas mãos, ocupando o terço central do quadro. Enquadramento frontal ou levemente oblíquo.  

Cenário e luz. Ambiente real e reconhecível (quintal, cozinha, caçamba de picape, parque). Luz natural, contraste médio-alto. O fundo pode ser escuro e desfocado — não precisa de área calma, porque não recebe texto.  

Produto. Protagonista da cena. Preparado, servido ou em uso — não embalado. Cor viva.  

Proibições: packshot · flat-lay · foto sem pessoa · texto/preço/selo queimado · produto ainda na embalagem · fundo de estúdio · marca d'água.  

Adaptação por categoria — o que é a cena:  

| Categoria | Cena |  
|---|---|  
| Alimentos / bebidas | Pessoa servindo ou provando, tábua ou prato montado |  
| Suplementos | Preparo do shake, copo na mão, cozinha ou academia |  
| Pet | Tutor e animal interagindo com o produto |  
| Brinquedos | Criança em brincadeira, produto em uso |  
| Casa | Pessoa usando o item no ambiente vivido |  
| Moda casual | Pessoa vestindo a peça em contexto cotidiano |

---

HTML: [[_html/hero-5-cupom-em-tres-lugares.html]] · Seção: [[_hero]] · Protocolo: [[_protocolo-de-selecao]]
