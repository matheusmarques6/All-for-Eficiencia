---
tipo: componente
slug: hero-7-campanha-sem-cupom
secao: hero
nome_no_banco: "welcome - hero section 7"
variant_id: c90713ff-9821-4d92-98c1-c22008fb9609
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [campanha-promocional, sazonal-data-comemorativa]
momento_vetado: [welcome-1, welcome-meio, welcome-tardio, carrinho-abandonado, checkout-abandonado, transacional]

# --- eixos de ranking, na ordem do protocolo ---
objecao: [preco-valor]
registro: []
registro_vetado: [premium-editorial]
paleta: [claro]
papel_na_peca: [abre]

# --- requisitos duros (eliminam) ---
exige: [desconto-automatico-sem-cupom, duas-ou-tres-cores-de-identidade, desconto-escalonado, foto-estudio-fundo-claro, terco-superior-liso]

# --- capacidade e composição ---
product_slots: 0
itens: null
peso: { altura_px: 1534, classe: pesado, fonte: medido }
convivencia: []

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: null
schema_campos: 5
status: aprovada
---

## Descrição curta

Abertura de campanha promocional. O percentual é a headline, uma linha de apoio explica a mecânica da oferta e três barras de cor no topo fazem o papel de assinatura visual da marca. Não há cupom: a oferta é automática. Momento de uso: campanha de desconto avulsa ou sazonal, para base já engajada que não precisa de apresentação.

## Descrição detalhada

Três barras de cor de 20px no topo; abaixo, uma imagem de fundo de 780px. Logo, eyebrow, headline, subhead e CTA são sobrepostos à metade superior dessa imagem.  

Quatro mecanismos definem a variante:  

As barras de cor substituem a barra de benefício. Três faixas de 200px cada, em cores da identidade, ocupando a largura total. É a assinatura da marca no topo — não carregam texto e não são clicáveis.  

O eyebrow é qualificador da oferta, não saudação. "Up to" existe para modular o percentual. Sem ele, o número vira promessa fechada e cria risco de expectativa.  

Escala tipográfica progressiva e centralizada. Eyebrow 31px → headline 53px → subhead 21px. O eyebrow é maior que o subhead, invertendo a hierarquia usual — o topo da leitura é a oferta, não a explicação.  

O CTA cai sobre o início dos sujeitos. Não existe respiro entre o botão e a cena; a base do CTA encosta na altura em que as figuras entram no quadro. É o que amarra o bloco de texto à fotografia.

## Quando usar

Campanha promocional com desconto automático, sem cupom.  
Uniformes, activewear, moda funcional, calçado, casa, pet — categorias em que a cena de movimento comunica uso.  
Quando a marca tem duas ou três cores de identidade que sustentam as barras do topo.  
Quando o desconto é escalonado ou por volume ("quanto mais compra, mais economiza") e precisa da linha de apoio.  
Base já engajada, que não precisa de apresentação de marca.

## Quando NÃO usar

Welcome — não há slot para cupom nem para acolhimento.  
Marca de uma cor só — as barras ficam sem função e viram ruído.  
Oferta com código — a variante não tem onde acomodar o código sem quebrar a escala.  
Foto sem fundo claro e uniforme no topo — o texto cinza escuro exige fundo alto.  
Carrinho, checkout, transacional, editorial de marca.  
Quando o desconto é fechado e não escalonado: sem "up to", o eyebrow perde a função e a escala desmonta.

## Orientações de copy para a IA

Eyebrow — qualificador do percentual em caixa alta ("Up to", "Até", "Ganhe até"). Duas ou três palavras. Nunca saudação, nunca nome de marca.  

Headline — o percentual + a categoria em uma linha, caixa alta ("35% OFF SCRUBS"). Duas linhas só se a categoria for longa. Sem ponto final, sem exclamação.  

Subhead — uma frase que explica a mecânica da oferta e um comando de estoque. Duas linhas. É o único slot com exclamação permitida, e no máximo uma.  

CTA — verbo genérico em caixa alta com tracking largo. Sem percentual: a headline já é o percentual.  

Proibições: código de cupom em qualquer slot · contagem regressiva · percentual no CTA · headline em caixa baixa · exclamação fora do subhead · nome da marca na headline.

## Design system

Container 600px fixo, sem borda. Zero raio, zero sombra, zero gradiente.  

Estrutura  

| # | Elemento | Altura |  
|---|---|---|  
| 1 | Barras de cor | 20px |  
| 2 | Hero com imagem de fundo | 780px |  

Barras: três células de 200px, sem espaçamento entre elas, ocupando os 600px. Nenhuma tem texto ou link.  

Zonas internas da hero  

| Zona | Faixa | Conteúdo |  
|---|---|---|  
| Limpa | 0 – 383px (topo 49%) | Fundo alto e uniforme da foto. Recebe todo o overlay. |  
| Sujeito | 383 – 780px (base 51%) | Figuras em movimento. Nenhum elemento sobreposto além da base do CTA. |  

Overlay  

| Elemento | Padding-top | Dimensão |  
|---|---|---|  
| Logo | 51px | 148 × 47px |  
| Eyebrow | 30px | 31/37px, tracking +0.05em, caixa alta |  
| Headline | 22px | 53/56px, tracking +0.05em, caixa alta, padding lateral 18px |  
| Subhead | 22px | 21/24px, 2 linhas, padding lateral 43px |  
| CTA | 22px | 287 × 52px |  
| Área livre do sujeito | — | 397px |  

Paleta — quatro cores, e é a única variante do arsenal com quatro.  

| Papel | Hex (Mediclo) | Uso |  
|---|---|---|  
| Cor primária |  |  |  
| #373737 | Todo o texto do overlay — cinza escuro, nunca preto puro |  |  
| Cor secundária |  |  |  
| #6B906E | Fundo do CTA, com label branco |  |  
| Barra 1 |  |  |  
| #646874 | Faixa esquerda |  |  
| Barra 3 |  |  |  
| #BC394B | Faixa direita |  |  

A barra do meio é sempre   
#FFFFFF — ela separa as outras duas e amarra com o fundo claro da foto. As barras 1 e 3 são cores da identidade e não aparecem em nenhum outro elemento da peça. O fundo vem da foto: cinza claro alto, também background-color de fallback.  

Pele alternativa (HTML base): CTA preto, barra 3 preta. Usar quando a marca só tem uma cor de identidade além do neutro.  

Tipografia. Principal: Arial → Helvetica em todos os slots. Eyebrow e headline em caixa alta com tracking +0.05em; subhead em caixa mista sem tracking; CTA 23px bold com tracking +0.15em. Secundária não existe.  

Implementação. Barras como três <td> de 200px com font-size:0;line-height:0 — sem isso o Outlook insere altura fantasma. background no <td> da hero + background-image inline + background-size:600px 780px, background-color na cor de fundo da foto como fallback, bloco VML v:rect/v:fill type="frame" para Outlook. Botão bulletproof. Hack u + .body .hero-txt travando o cinza   
#373737 no Gmail iOS. &nbsp; entre o percentual e "Off" na headline para impedir quebra em ponto errado.  

Tags: HERO_IMAGE_URL, LOGO_URL, OFFER_QUALIFIER, OFFER_VALUE, OFFER_CATEGORY, HERO_SUBHEAD, CTA_LABEL, CTA_URL, BRAND_BAR_1, BRAND_BAR_3.  

Erros que quebram o padrão: barras de larguras desiguais · texto ou link nas barras · usar as cores das barras em outro elemento · barra do meio em cor · preto puro no texto · respiro entre o CTA e a entrada dos sujeitos · subhead maior que o eyebrow · percentual repetido no CTA · segundo botão · botão com raio.

## Direção fotográfica

7. Direção fotográfica  

Proporção 3:4 — slot de 600 × 780px, ativo final 1200 × 1560px (2x). JPG q80 ou WebP, < 260 KB, full-bleed. Gerar em 3:4 na largura de 1200px (1200 × 1600) e cortar 40px de altura pelo topo — é fundo liso e não carrega informação.  

Regra crítica: a metade superior tem que ser fundo claro, alto e uniforme, com luminância acima de 85%. O texto é cinza escuro, não branco — fundo médio ou escuro inviabiliza a peça.  

Composição. Duas figuras em movimento suspenso — corrida, salto, passada larga — entrando pelas laterais e cortadas pelas bordas laterais e pela base. Direções opostas ou convergentes. Nenhuma figura sobe acima da metade do quadro. Elemento vegetal entrando pelos cantos inferiores como moldura.  

Cenário e luz. Fundo infinito claro, sem horizonte visível, com leve sombreamento nos cantos inferiores para assentar as figuras. Luz de estúdio difusa, sombras suaves sob os pés. Sem cenário reconhecível.  

Produto. Vestido pelas figuras, em cor média que contrasta com o fundo claro. Detalhes funcionais visíveis (bolsos, cordões, aviamento) — é o que prova a categoria.  

Proibições: fundo escuro ou médio · figura acima da metade do quadro · cenário reconhecível · pose estática · texto/preço/selo queimado · sombra dura · marca d'água.  

Adaptação por categoria — o que é a cena:  

| Categoria | Cena |  
|---|---|  
| Uniforme / activewear | Duas figuras em corrida ou salto, roupa técnica |  
| Moda funcional | Figuras em passada larga, peça em movimento |  
| Calçado | Figuras em salto, pés em destaque na base |  
| Casa | Figuras carregando ou usando o item em movimento |  
| Pet | Tutor e animal em corrida, produto vestido |  
| Infantil | Crianças em brincadeira ativa, fundo claro |

---

HTML: [[_html/hero-7-campanha-sem-cupom.html]] · Seção: [[_hero]] · Protocolo: [[_protocolo-de-selecao]]
