---
tipo: componente
slug: hero-2-pergunta-comparativa
secao: hero
nome_no_banco: "welcome - hero section 2"
variant_id: 3e241d7f-5f84-4017-a553-880736a450dc
ativa: true
dispositivo: pergunta_ao_leitor

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [consideracao, reengajamento]
momento_vetado: [carrinho-abandonado, checkout-abandonado, transacional]

# --- eixos de ranking, na ordem do protocolo ---
objecao: [qualidade-eficacia]
registro: []
registro_vetado: []
paleta: [escuro-saturado, com-acento-definido]
papel_na_peca: [abre]

# --- requisitos duros (eliminam) ---
exige: [cor-de-acento-definida, desconto-percentual]
diretivas_de_imagem: [macro-de-produto]

# --- capacidade e composição ---
product_slots: 0
itens: null
peso: { altura_px: 727, classe: medio, fonte: medido }
convivencia: []

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: null
schema_campos: 4
status: aprovada
---

## Descrição curta

Abertura de e-mail de proposta de valor. A headline faz uma pergunta comparativa que posiciona a marca contra a concorrência, com o diferencial destacado em peso e cor; o CTA já carrega a oferta. Momento de uso: meio da régua de welcome ou consideração — o cliente já conhece a marca e precisa de um motivo para escolher esta e não outra.

## Descrição detalhada

Barra branca de 80px com o logo; abaixo, uma imagem de fundo de 567px cobrindo o resto. Headline e CTA são sobrepostos à metade inferior dessa imagem.  

Três mecanismos definem a variante:  

Macro do produto no topo, zona limpa embaixo. O produto sangra nas laterais e no topo, cortado agressivamente, e ocupa a metade superior. A metade inferior é fundo liso escuro e recebe todo o texto. É o espelho do hero de campanha, onde o sujeito fica embaixo.  

Destaque por peso e cor, nunca por tamanho. A headline é regular; 2 a 3 palavras no meio recebem bold e a cor de acento. Aumentar o corpo do trecho enfatizado quebra o ritmo da caixa alta.  

A oferta vive no botão, não na headline. A headline é argumento; o desconto aparece só no label do CTA. É o inverso do hero de campanha, onde a oferta fica numa barra e o botão é genérico.

## Quando usar

régua de consideração, reengajamento com argumento.  
Quando o diferencial é material, acabamento ou processo e a foto pode provar isso em macro.  
Joias, relógios, calçado, moda com aviamento visível, beleza com textura, eletrônico com acabamento.  
Quando a marca tem fundo escuro saturado na identidade e uma cor de acento definida.  
Quando existe oferta ativa que cabe no botão sem virar o argumento.

## Quando NÃO usar

Sem macro de produto disponível. Packshot inteiro centralizado transforma a peça em catálogo.  
Foto de fundo claro ou pouco saturado — o texto branco morre e o botão some.  
Produto sem diferencial visível. Se a qualidade não aparece em close, a headline promete o que a foto não entrega.  
Marca sem cor de acento definida — o destaque da headline fica sem onde apoiar.  
Carrinho, checkout, transacional, grade de produtos, prova social.  
Quando não há oferta: sem desconto, o CTA fica genérico e a variante perde o fecho.

## Orientações de copy para a IA

Headline — pergunta comparativa em caixa alta, três linhas. Estrutura: por que [marca] [diferencial] mais que [categoria concorrente]? O trecho destacado é o verbo do diferencial, não o nome da marca nem a categoria. Ponto de interrogação obrigatório. Sem preço, sem percentual, sem nome de produto.  

Trecho em destaque — 2 a 3 palavras contíguas, no meio da frase, nunca no começo nem no fim. É o que a marca faz melhor, em uma ação ("SHINE HARDER", "LASTS LONGER", "FITS BETTER").  

CTA — verbo + oferta ("SHOP 10% OFF"). Aqui o desconto no botão é o padrão, não erro: a headline não pode carregá-lo.  

Proibições: headline afirmativa em vez de pergunta · destaque em mais de 3 palavras · destaque na primeira ou última palavra · desconto na headline · exclamação · segunda pergunta.

## Design system

Container 600px fixo, sem borda. Zero raio, zero sombra, zero gradiente aplicado por CSS. Preheader oculto obrigatório.  

Estrutura  

| # | Elemento | Altura |  
|---|---|---|  
| 1 | Barra do logo (branca, opaca) | 80px |  
| 2 | Hero — imagem de fundo full-bleed | 567px |  

Zonas internas da hero  

| Zona | Faixa | Conteúdo |  
|---|---|---|  
| Produto | 0 – 265px (topo 47%) | Macro sangrando no topo e nas laterais. Nenhum texto. |  
| Limpa | 265 – 567px (base 53%) | Fundo liso. Recebe headline e CTA. |  

Overlay  

| Elemento | Padding-top | Dimensão |  
|---|---|---|  
| Logo (dentro da barra) | 14px | 145 × 52px |  
| Headline | 352px | 32/36px, 3 linhas, padding lateral 58px (útil 484px) |  
| CTA | 25px | 306 × 70px |  
| Respiro final | — | 12px |  

Paleta — três cores.  

| Papel | Hex (IceCartel) | Uso |  
|---|---|---|  
| Cor primária |  |  |  
| #012A61 | Fundo — pipetado da própria foto, também background-color de fallback |  |  
| Cor secundária |  |  |  
| #42B0F0 | Fundo do botão, com label branco |  |  
| Acento |  |  |  
| #FFBC49 | Exclusivo do trecho destacado da headline |  |  

Regras: a cor primária é sempre pipetada da foto (trocou a foto, trocou o token). O acento nunca aparece no botão, e a cor secundária nunca aparece no texto. Luminância do fundo abaixo de 25% — acima disso o texto branco falha.  

Pele alternativa (HTML base): CTA branco com label preto, sem cor de acento — o destaque da headline fica só no bold. Usar quando a marca não tem cor de acento definida.  

Tipografia. Principal: Arial → Helvetica nos dois slots. Headline 32px regular em caixa alta, com <strong> no trecho destacado. CTA 32px bold, caixa alta, mesmo corpo da headline. Secundária não existe: o logo é ativo de imagem e cada marca traz o seu.  

Implementação. background no <td> + background-image inline + background-size:600px 567px, background-color na cor primária como fallback, bloco VML v:rect/v:fill type="frame" para Outlook. Hack u + .body .txt-wht para travar o branco no Gmail iOS dark mode. Botão bulletproof. Barra do logo opaca e fora da imagem — com imagem bloqueada a marca continua visível sobre branco.  

Tags: PREHEADER, LOGO_URL, SITE_URL, HERO_IMAGE_URL, HEADLINE, HEADLINE_HIGHLIGHT, CTA_LABEL, CTA_URL.  

Erros que quebram o padrão: background-color diferente do azul real da foto · packshot em vez de macro · fundo claro ou pouco saturado · destaque em mais de 3 palavras · aumentar o corpo do trecho destacado em vez do peso · usar o acento no botão · headline em caixa baixa ou em 4+ linhas · selo de desconto sobre a foto · segundo botão · botão com raio ou com a largura da caixa de texto.

## Direção fotográfica

7. Direção fotográfica  

Proporção 1,06:1 — 600 × 567px de exibição, ativo final 1200 × 1134px (2x). JPG q80 ou WebP, < 220 KB, full-bleed. Geradores não aceitam essa razão: gere em 1:1 a 1200 × 1200 e corte 66px de altura pelo topo — o produto já sangra ali, e a base precisa ficar intacta.  

Regra crítica: a metade inferior (265–567px) tem que estar completamente livre de produto, sem brilho especular e sem sombra dura. É onde a headline e o botão assentam.  

Composição. Macro extremo do produto, cortado nas laterais e no topo, preenchendo a metade superior em arco diagonal. Nada centralizado, nada com respiro em volta. Profundidade de campo rasa.  

Cenário e luz. Fundo monocromático escuro e saturado, com textura sutil de veludo ou tecido — nunca chapado digital. Luz dirigida no produto com brilho especular forte, caindo rápido em direção à base do quadro. Sem vinheta.  

Produto. Detalhe que prova o diferencial: elos, cravação, engate, costura, textura. Marca d'água ou repetição de logo no fundo é aceitável se ficar fora da faixa central inferior.  

Proibições: packshot centralizado · fundo branco ou claro · fundo chapado sem textura · produto na metade inferior · brilho ou sombra dura na zona limpa · texto/preço/selo queimado · pessoa no quadro · colagem ou split.  

Adaptação por categoria — o que é o macro:  

| Categoria | Detalhe |  
|---|---|  
| Joia | Elos da corrente, cravação, engate |  
| Relógio | Mostrador, bisel, malha |  
| Moda | Trama do tecido, costura, zíper, aviamento |  
| Beleza | Textura do produto, gota, creme, aplicador |  
| Eletrônico | Acabamento, porta, grafia, junção de materiais |  
| Calçado | Costura, sola, textura do couro |

---

HTML: [[_html/hero-2-pergunta-comparativa.html]] · Seção: [[_hero]] · Protocolo: [[_protocolo-de-selecao]]
