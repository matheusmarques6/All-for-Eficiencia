---
tipo: componente
slug: hero-3-cupom-de-captacao
secao: hero
nome_no_banco: "welcome - hero section 3"
variant_id: d9e34a1f-7bc7-47e8-9081-53600b104dd2
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [welcome-1]
momento_vetado: [carrinho-abandonado, checkout-abandonado, browse-abandonment, transacional, sazonal-data-comemorativa, lancamento]

# --- eixos de ranking, na ordem do protocolo ---
objecao: [preco-valor]
registro: []
registro_vetado: [luxo]
paleta: [claro]
papel_na_peca: [abre]

# --- requisitos duros (eliminam) ---
exige: [cupom-ativo, foto-estudio-fundo-claro, terco-superior-liso]

# --- capacidade e composição ---
product_slots: 0
itens: null
peso: { altura_px: 903, classe: medio, fonte: medido }
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

Primeiro e-mail da régua de boas-vindas. Entrega o cupom de captação e apresenta a marca; a headline é a oferta, o código aparece em texto e o CTA repete o valor. Momento de uso: welcome #1, logo após o opt-in, quando o contato ainda não comprou e o objetivo é a primeira conversão.

## Descrição detalhada

Uma imagem única de 949px cobre o e-mail inteiro. Lockup de marca, headline, linha do cupom e CTA são sobrepostos ao terço superior dessa imagem. Não há barra de logo, não há bloco de cor, não há emenda.  

Três mecanismos definem a variante:  

O fundo do texto é a área desfocada da própria foto. O terço superior da fotografia é fora de foco e uniforme; é ele que faz as vezes de bloco de cor. Trocar por um bloco chapado cria emenda visível.  

Headline em dois pesos na mesma família. Linha 1 em regular, linha 2 em bold, mesmo corpo e mesmo tracking negativo. A hierarquia vem do peso, não de tamanho nem de cor.  

O código do cupom não tem contêiner. Sem caixa, sem borda tracejada, sem cor própria — só bold dentro da linha de instrução. O destaque vem do respiro em volta.

## Quando usar

em qualquer nicho com fotografia de produto própria.  
Beleza, skincare, joia, acessório, casa — categorias em que o flat-lay comunica o kit inteiro.  
Quando a marca não tem logo em arquivo ou prefere lockup tipográfico: o slot do topo aceita wordmark em texto vivo.  
Quando existe uma foto com região desfocada ou lisa no terço superior.  
Quando o desconto é o argumento central e não há necessidade de brand story no mesmo bloco.

## Quando NÃO usar

Sem cupom. A variante inteira gira em torno do código; sem ele, a headline e o CTA ficam vazios.  
Foto sem área desfocada ou lisa no topo — o texto cai em cima de detalhe e some.  
Marca de luxo que não desconta — headline de percentual descaracteriza posicionamento.  
Carrinho, checkout, browse, transacional.  
Campanha sazonal ou lançamento — não há onde acomodar tema nem urgência.  
Quando a marca precisa de identidade visual forte no topo e só tem logo em imagem de baixa resolução.

## Orientações de copy para a IA

Eyebrow + nome da marca — lockup de duas linhas: uma saudação curta em cima ("Welcome To") e o nome da marca embaixo, com régua de 1px na largura exata do nome. Leitura contínua entre as duas linhas.  

Headline — a oferta em duas linhas: linha 1 abre com o valor, linha 2 diz a que se aplica. Linha 2 em bold. Sem ponto final. Não repetir o nome da marca.  

Linha do cupom — instrução com o código em bold no meio, seguida de uma segunda linha curta com a condição ("at checkout" / "no checkout"). O código nunca ocupa linha própria com destaque gráfico.  

CTA — verbo + o valor da oferta, caixa alta com tracking largo. Repetir o percentual aqui é o padrão: o botão fecha o que a headline abriu.  

Proibições: contagem regressiva · exclamação · brand story dentro do bloco · segundo botão · código em caixa tracejada · headline em uma linha só · nome de produto na headline.

## Design system

Container 600px fixo, borda 1px   
#000000 opcional (flag has_border). Zero raio, zero sombra, zero gradiente. Preheader oculto obrigatório.  

Estrutura — elemento único: hero como imagem de fundo, 598 × 949px.  

Zonas internas  

| Zona | Faixa | Conteúdo |  
|---|---|---|  
| Limpa | 0 – 480px (topo 51%) | Área desfocada da foto. Recebe todo o overlay. |  
| Produto | 480 – 949px (base 49%) | Flat-lay em foco. Nenhum elemento sobreposto. |  

Overlay  

| Elemento | Padding-top | Dimensão |  
|---|---|---|  
| Lockup de marca | 75px | 152 × 48px |  
| Headline (2 linhas) | 31px | 50/57px, tracking −0.06em, padding lateral 24px |  
| Linha do cupom | 34px | 25/30px, padding lateral 58px |  
| CTA | 43px | 389 × 75px |  
| Área livre do produto | — | 469px |  

Paleta — duas cores.  

| Papel | Hex (London Brow) | Uso |  
|---|---|---|  
| Cor primária |  |  |  
| #D2BBA7 | Fundo — vem da foto, não de CSS |  |  
| Cor secundária |  |  |  
| #130E31 | Todo o texto, a régua do lockup e o fundo do botão |  |  

A cor primária é pipetada da faixa desfocada da foto e usada como background-color de fallback. Trocou a foto, trocou o token. A secundária é uma só e faz tudo: lockup, régua, headline, cupom e preenchimento do botão. Não existe cor de acento — o destaque vem de peso tipográfico.  

Pele alternativa (HTML base): fundo branco, texto e botão pretos, lockup dentro de caixa com borda de 1px. Usar quando a foto tem topo claro neutro.  

Tipografia. Principal: Arial → Helvetica em todos os slots. Headline 50/57px com tracking −0.06em, linha 1 regular e linha 2 em <strong>. Cupom 25/30px regular com o código em <strong>. CTA 25px regular, caixa alta, tracking +0.15em com text-indent compensando. Secundária: se a loja tem serif display de marca, ela entra apenas na headline e no nome da marca — é o que a London Brow faz.  

Implementação. background no <td> + background-image inline + background-size:598px 949px, background-color na cor primária como fallback, bloco VML v:rect/v:fill type="frame" para Outlook. Hack u + .body .txt-blk para o Gmail iOS. Botão bulletproof. Com imagem bloqueada, o texto continua legível sobre a cor primária de fallback — por isso o bgcolor é obrigatório e não opcional.  

Tags: PREHEADER, HERO_IMAGE_URL, BRAND_NAME, WELCOME_EYEBROW, HEADLINE_L1, HEADLINE_L2, COUPON_CODE, COUPON_HINT, OFFER_VALUE, CTA_LABEL, CTA_URL.  

Erros que quebram o padrão: bloco de cor chapado em vez do topo desfocado da foto · background-color diferente da faixa desfocada · objeto em foco na zona limpa · código do cupom em caixa ou com cor própria · régua mais larga ou mais estreita que o nome da marca · headline em uma linha · terceira cor · segundo botão · botão com raio · tracking positivo na headline.

## Direção fotográfica

7. Direção fotográfica  

Proporção 2:3 — slot de 598 × 949px, ativo final 1196 × 1898px (2x). JPG q80 ou WebP, < 300 KB, full-bleed. Gerar em 2:3 na altura de 1898px (1265 × 1898) e cortar 69px de largura, 35px de cada lado, para chegar ao ativo final.  

Regra crítica: o terço superior (0–480px) tem que estar fora de foco e uniforme, numa cor só. É esse desfoque que faz as vezes de bloco de cor e apaga a emenda. Qualquer objeto nítido ali expõe o corte e derruba a legibilidade do texto.  

Composição. Flat-lay em ângulo alto — não perpendicular — com o kit de produtos espalhado na metade inferior. Itens em diagonal, sobrepostos parcialmente, alguns cortados pelas bordas laterais e pela base. O foco cai da metade para baixo; a transição de desfoque é gradual, não uma linha.  

Cenário e luz. Superfície têxtil ou de couro em tom neutro quente, com textura visível. Luz natural difusa lateral, sombras longas e macias. Paleta monocromática quente — a foto define a cor da peça inteira.  

Produto. Kit completo, não produto único: sachês, aplicadores, frascos, ferramentas. Rótulos legíveis nos itens em foco. Nenhuma mão, nenhuma pessoa.  

Proibições: topo nítido · fundo branco de estúdio · flat-lay perpendicular e simétrico · produto único · texto/preço/selo queimado · pessoa ou mão · sombra dura · vinheta.  

Adaptação por categoria — o que compõe o flat-lay:  

| Categoria | Itens |  
|---|---|  
| Beleza / skincare | Sachês, frascos, pincéis, pinça, aplicadores |  
| Joia / acessório | Peças soltas, estojo aberto, flanela, cartão |  
| Casa | Têxteis dobrados, velas, utensílio, embalagem |  
| Moda | Peça dobrada, cinto, óculos, etiqueta |  
| Papelaria / kit | Cadernos, canetas, adesivos, envelope |  
| Pet | Sachês, brinquedo, coleira, escova |

---

HTML: [[_html/hero-3-cupom-de-captacao.html]] · Seção: [[_hero]] · Protocolo: [[_protocolo-de-selecao]]
