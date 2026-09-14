---
tipo: componente
slug: hero-8-lineup-com-lembrete-de-oferta
secao: hero
nome_no_banco: "welcome - hero sectiion 8"
variant_id: 43f9b0ec-9ebc-4657-b1ef-9cfd5a521895
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [welcome-meio, welcome-tardio, newsletter, sazonal-data-comemorativa, cross-sell, browse-abandonment]
momento_vetado: [carrinho-abandonado, checkout-abandonado, transacional]

# --- eixos de ranking, na ordem do protocolo ---
objecao: [amplitude-de-catalogo]
registro: []
registro_vetado: [luxo, premium-editorial]
paleta: [claro]
papel_na_peca: [meio]

# --- requisitos duros (eliminam) ---
exige: []
diretivas_de_imagem: [foto-estudio-fundo-claro, terco-superior-liso]

# --- capacidade e composição ---
product_slots: 0
itens: null
peso: { altura_px: 1151, classe: medio, fonte: medido }
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

Bloco de meio de e-mail. Anuncia uma rotina, kit ou linha completa e leva à coleção correspondente; o argumento é o conjunto, não o produto individual. Momento de uso: descoberta e educação — quando o cliente está conhecendo a amplitude do catálogo, não decidindo uma compra específica.

## Descrição detalhada

Módulo de seção, nunca topo de e-mail. Ordem fixa: título → subtítulo → CTA → imagem.  

Três mecanismos definem a variante:  

CTA antes da imagem. O leitor recebe promessa, justificativa e botão; a foto confirma o que ele já decidiu clicar. Com a imagem acima do botão, o bloco vira banner.  

Fundo do container e fundo da foto no mesmo branco. A emenda entre texto e imagem fica invisível e o bloco lê como peça única.  

Texto 100% vivo em HTML. Título, subtítulo e label não são queimados na imagem — é o único padrão do arsenal que sobrevive inteiro a imagem bloqueada e a dark mode.

## Quando usar

Rotina, kit, linha ou coleção — o argumento é "conjunto".  
Beleza, skincare, haircare, suplementos, pet, casa: nichos onde o portfólio é o argumento.  
2º/3º bloco de welcome; newsletter e campanha sazonal; cross-sell; browse abandonment.  
Quando a marca tem fotografia de estúdio em fundo claro e embalagem colorida.

## Quando NÃO usar

Carrinho e checkout abandonado — convida à descoberta e concorre com o CTA de recuperação.  
Hero de abertura — não tem barra de marca; o e-mail começa sem identidade.  
Produto único de ticket alto, ou marca de luxo editorial (o botão preto é comercial demais).  
Foto com fundo colorido, escuro ou de ambiente — aparece a emenda.  
Foto com texto, selo ou preço queimado.  
Urgência, countdown, flash sale, transacional.

## Orientações de copy para a IA

Título — promessa de resultado, caixa alta, voz do benefício. Sem nome de produto, sem preço, sem desconto, sem ponto final. Subtítulo — uma frase com o como: o que ganha e por qual mecanismo. Não repete o título. Ponto final. CTA — verbo + objeto da coleção, caixa alta. Preferir específico ao genérico. Nunca repetir desconto.  

Sequência: título promete o resultado → subtítulo dá a condição → CTA nomeia o caminho. Se os três dizem a mesma coisa, está errado.  

Proibições: desconto ou cupom em qualquer slot, contagem regressiva, "clique aqui", superlativo sem lastro. Em PT-BR, evitar imperativo traduzido ao pé da letra ("COMPRE A ROTINA" → "MONTE SUA ROTINA").

## Design system

Container 600px fixo, fundo   
#FFFFFF, borda 1px   
#000000 opcional (flag has_border). Zero raio, zero sombra, zero gradiente.  

| Elemento | Padding-top | Dimensão |  
|---|---|---|  
| Título | 59px | 35/39px, útil 490px (padding lateral 55px) |  
| Subtítulo | 24px | 24/27px, caixa travada em 357px |  
| CTA | 36px | 401 × 82px |  
| Imagem | 55px | 598 × 489px, full-bleed |  

Hierarquia de largura: título > botão > subtítulo. A caixa de 357px do subtítulo força duas linhas curtas — não alargar.  

Paleta — duas cores. Cor primária   
#000000 (título, subtítulo, fundo do botão); cor secundária   
#FFFFFF (container, fundo da foto, label do botão). Sem acento: toda a cor vem da fotografia.  

Tipografia. Principal: Arial → Helvetica, nos três slots. Título 35px regular em caixa alta (o impacto vem do corpo, não do bold); subtítulo 24px regular; CTA 30px bold. Secundária não existe no template base — se a loja tem serif display de marca, ela entra só no título (é o que a Cocunat faz).  

Implementação. color-scheme: light only + hack u + .body .txt-blk (Gmail iOS). Botão bulletproof, nunca imagem. <img> sempre display:block — sem isso o gap do Outlook expõe a emenda. Imagem em 2x servida na largura de exibição.  

Tags: SECTION_TITLE, SECTION_SUBTITLE, CTA_LABEL, CTA_URL, IMAGE_URL, IMAGE_LINK_URL, IMAGE_ALT.  

Erros que quebram o padrão: imagem acima do botão · fundo da foto fora do branco do container · texto queimado na imagem · título em bold · subtítulo alargado · botão com raio ou mais largo que o título · terceira cor · segundo botão · <img> sem display:block.

## Direção fotográfica

7. Direção fotográfica  

598 × 489px (1,22:1) · exportar 1196 × 978 (2x) · JPG q80 ou WebP · < 200 KB · full-bleed.  

Regra crítica: o terço superior tem que ser branco de estúdio uniforme, no mesmo valor do container. É o que apaga a emenda.  

Composição. Cluster central de 6 a 9 itens da mesma família, alturas escalonadas em arco, sobreposição parcial, ao menos um item deitado. Sangra na base do quadro e pode sangrar de leve nas laterais. Terço superior livre.  

Cenário e luz. Superfície branca contínua com parede branca, sem linha dura de horizonte; faixa de piso levemente mais fria na base (≈   
#DEDEE0). Luz difusa frontal-superior, sombras curtas e macias. Sem vinheta, sem reflexo espelhado.  

Produto. Rótulos da frente legíveis e voltados para a câmera. A cor da embalagem é a única cor da peça — o casting precisa formar paleta coerente.  

Proibições: fundo colorido ou de ambiente · texto/preço/selo queimado · produto único centralizado (vira packshot) · fileira simétrica · sombra dura · pessoa ou mão · prop de ambiente · marca d'água.  

Adaptação por categoria — o que compõe o cluster:  

| Categoria | Itens |  
|---|---|  
| Haircare / skincare | Frascos, bisnagas, séruns, pote, acessório de tecido |  
| Suplementos | Potes, sachês, doseador, cápsula solta |  
| Casa / limpeza | Refis, borrifadores, panos, embalagem-mãe |  
| Pet | Sachês, potes, brinquedo, coleira |  
| Alimentos / bebidas | Latas e garrafas, em pé e deitadas |  
| Beleza / maquiagem | Batons, compactos, pincéis em leque |  


Checklist: terço superior livre · branco idêntico ao container · cluster sangrando na base · 6-9 itens · alturas escalonadas · rótulos legíveis · sem texto/pessoa · sombras macias · 1196px e < 200 KB.

---

HTML: [[_html/hero-8-lineup-com-lembrete-de-oferta.html]] · Seção: [[_hero]] · Protocolo: [[_protocolo-de-selecao]]
