---
tipo: componente
slug: hero-9-atendimento-proativo
secao: hero
nome_no_banco: "welcome - hero section 9"
variant_id: 85006b06-b7db-498e-af9d-4db11be4fd5f
ativa: true
dispositivo: oferta_de_ajuda

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [browse-abandonment, reengajamento]
momento_vetado: [carrinho-abandonado, checkout-abandonado, welcome-1, sazonal-data-comemorativa, lancamento]

# --- eixos de ranking, na ordem do protocolo ---
objecao: [suporte-duvida]
registro: [clinico-sobrio]
registro_vetado: [comercial, volume-impulso]
paleta: [monocromatico, cinza-neutro]
papel_na_peca: [abre]

# --- requisitos duros (eliminam) ---
exige: [duas-acoes-de-suporte]
diretivas_de_imagem: [foto-monocromatica, terco-superior-liso]

# --- capacidade e composição ---
product_slots: 0
itens: null
peso: { altura_px: 1476, classe: pesado, fonte: medido }
convivencia: []

# --- fios para o resto do vault ---
aprendizados: ["[[um-cta-dominante-em-email-curto]]"]
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: null
schema_campos: 6
status: aprovada
---

## Descrição curta

E-mail de atendimento proativo. Pergunta se o contato precisa de ajuda, reconhece a visita ao site e oferece dois caminhos em escada: a ação principal em botão sólido e uma alternativa de menor comprometimento em botão de contorno. Não há oferta nem desconto. Momento de uso: browse abandonment ou pós-visita sem conversão, quando o objetivo é remover objeção e não empurrar compra.

## Descrição detalhada

Barra preta de logo no topo; abaixo, uma imagem única de 1199px cobrindo o resto. Título, copy e os dois botões são sobrepostos ao terço superior dessa imagem.  

Quatro mecanismos definem a variante:  

Os dois CTAs são hierárquicos, não paralelos. O primário é sólido preto; o secundário tem fundo claro e contorno de 1px. Mesma largura e altura, peso visual diferente. É o oposto do hero de campanha com duplo CTA, onde os dois são idênticos e bifurcam público — aqui há uma ação preferida e uma saída de menor atrito.  

O cinza de fundo é o fundo de estúdio da foto. Não existe bloco de cor separado nem emenda. A ausência total de costura é o efeito; montar como "bloco cinza + banner embaixo" transforma a peça em newsletter comum.  

Título em caixa baixa, com pergunta. Registro de atendimento, não de venda. Caixa alta ou ponto de exclamação derrubam o tom.  

Nenhum slot de oferta. Sem cupom, sem percentual, sem urgência. A variante existe para o momento em que vender seria contraproducente.

## Quando usar

reativação suave.  
Atendimento proativo, "posso ajudar?", redução de objeção antes da compra.  
Beleza, skincare, joia, moda, eletrônico — categorias com dúvida técnica ou de escolha antes da conversão.  
Quando existem duas ações reais de suporte com pesos diferentes (conta e central de ajuda, chat e FAQ, consultoria e catálogo).  
Marca com identidade monocromática e fotografia de estúdio própria.

## Quando NÃO usar

Qualquer e-mail com oferta. Promoção, cupom, lançamento e urgência não têm onde entrar.  
Uma ação só — sem a segunda alternativa, o botão de contorno fica vazio de função.  
Carrinho e checkout abandonado — intenção alta pede caminho único e itens do carrinho.  
Welcome com cupom, campanha sazonal, grade de produtos, prova social.  
Quando a foto disponível não tem fundo de estúdio liso no terço superior.  
Marca de volume ou tom promocional: o registro contido soa desconexo.

## Orientações de copy para a IA

Título — pergunta curta em caixa baixa, na voz do atendimento ("can we help?", "posso ajudar?"). Interrogação obrigatória. Sem nome de marca, sem produto, sem oferta.  

Copy — três linhas: reconhecer a visita, oferecer ajuda com a escolha, convidar ao contato. Frases curtas, uma por linha. Tom de pessoa, não de sistema.  

CTA primário — a ação de maior valor para a marca, em caixa alta com tracking largo. É onde a conta, o chat ou a consultoria entram.  

CTA secundário — a alternativa de menor comprometimento: central de ajuda, FAQ, catálogo. Nunca o mesmo destino do primário e nunca mais persuasivo que ele.  

Proibições: percentual ou cupom em qualquer slot · urgência · exclamação em mais de uma linha · caixa alta no título · CTA secundário apontando para o mesmo lugar do primário · nome do produto.

## Design system

6. Design system  

Container 600px fixo, borda 1px   
#000000 opcional (flag has_border). Zero raio, zero sombra, zero gradiente. Preheader oculto obrigatório.  

Estrutura  

| # | Elemento | Altura |  
|---|---|---|  
| 1 | Barra do logo (preta, opaca) | 139px |  
| 2 | Corpo com imagem de fundo | 1199px |  

Zonas internas do corpo  

| Zona | Faixa | Conteúdo |  
|---|---|---|  
| Limpa | 0 – 463px (topo 39%) | Fundo de estúdio da foto. Recebe todo o overlay. |  
| Sujeito | 463 – 1199px (base 61%) | Pessoa e produto. Nenhum elemento sobreposto. |  

Overlay  

| Elemento | Padding-top | Dimensão |  
|---|---|---|  
| Logo (dentro da barra) | 45px | 152 × 48px |  
| Título | 66px | 48/55px, caixa baixa, padding lateral 40px |  
| Copy | 45px | 24/26px, 3 linhas, padding lateral 34px |  
| CTA primário | 49px | 330 × 75px |  
| CTA secundário | 20px | 330 × 75px, borda 1px |  
| Área livre do sujeito | — | 736px |  

Paleta — quatro valores, nenhum deles cor.  

| Papel | Hex | Uso |  
|---|---|---|  
| Cor primária |  |  |  
| #000000 | Barra do logo, título, fundo do CTA primário, borda e label do CTA secundário |  |  
| Cor secundária |  |  |  
| #DADDDD | Fundo — vem da foto, também background-color de fallback |  |  
| Neutro de texto |  |  |  
| #565352 | Copy — cinza médio, nunca preto |  |  
| Neutro do botão |  |  |  
| #E8E9ED | Fundo do CTA secundário — mais claro que o fundo da peça |  |  

A variante é monocromática por definição. Introduzir qualquer cor saturada, inclusive no CTA primário, descaracteriza o padrão. O   
#E8E9ED do botão secundário é deliberadamente mais claro que o   
#DADDDD do fundo — é assim que ele se destaca sem ganhar peso.  

Tipografia. Principal: Arial → Helvetica em todos os slots. Título 48px regular em caixa baixa — o impacto vem do corpo, nunca do bold. Copy 24px regular. CTAs 24px regular em caixa alta. Secundária não existe; o ar de monoespaçado nos botões vem de tracking largo na própria sans. Exceção controlada: se a loja tem um monoespaçado de marca, ele pode entrar apenas nos labels de CTA — nunca no título, nunca na copy.  

Implementação. background no <td> + background-image inline + background-size:598px 1199px, background-color em   
#DADDDD como fallback, bloco VML v:rect/v:fill type="frame" para Outlook. Barra do logo opaca e fora da imagem — com imagem bloqueada a marca continua visível. Botões bulletproof; no secundário, o <a> mede 328 × 73px para caber dentro da borda de 1px. Hacks u + .body .txt-blk e u + .body .txt-gry travando as duas cores de texto no Gmail iOS.  

Tags: PREHEADER, LOGO_URL, SITE_URL, HERO_IMAGE_URL, HERO_HEADLINE, HERO_COPY, CTA_PRIMARY_LABEL/CTA_PRIMARY_URL, CTA_SECONDARY_LABEL/CTA_SECONDARY_URL.  

Erros que quebram o padrão: montar como bloco de cor + banner separado · background-color diferente do cinza real da foto · dois CTAs com o mesmo peso visual · CTA secundário sólido · título em caixa alta ou em bold · copy em preto puro · botão secundário mais escuro que o fundo · qualquer cor saturada · terceiro botão · botão com raio · sujeito invadindo a zona limpa.

## Direção fotográfica

7. Direção fotográfica  

Proporção 9:16 — slot de 598 × 1199px, ativo final 1196 × 2398px (2x). JPG q80 ou WebP, < 320 KB, full-bleed. Gerar em 9:16 na altura de 2398px (1349 × 2398) e cortar 153px de largura, 77px de cada lado, para chegar ao ativo final.  

Regra crítica: os 39% superiores têm que ser fundo de estúdio liso e uniforme, em cinza claro, sem vinheta e sem degradê perceptível. Essa faixa é o "fundo" da peça inteira e o background-color de fallback é pipetado dela. Qualquer variação de tom ali cria a emenda que o padrão existe para evitar.  

Composição. Uma figura em gesto de uso do produto, entrando pela base do quadro em meio corpo. Perfil ou três quartos, olhar baixo e concentrado — nunca para a câmera. O produto ocupa menos de 15% do quadro e está nas mãos, em uso. Nenhuma figura sobe acima de 39%.  

Cenário e luz. Fundo infinito cinza claro, sem horizonte. Luz difusa lateral, sombra suave de um lado do rosto. Sem cenário, sem prop, sem mobiliário.  

Produto. Em uso, nas mãos, com o rótulo parcialmente legível. Nunca apresentado à câmera, nunca em packshot.  

Proibições: fundo colorido, escuro ou de ambiente · vinheta ou degradê no fundo · olhar para a câmera · sorriso aberto · produto apresentado à câmera · figura acima de 39% do quadro · texto/preço/selo queimado · marca d'água.  

Adaptação por categoria — o que é o gesto:  

| Categoria | Gesto |  
|---|---|  
| Skincare | Aplicação de sérum ou creme no rosto |  
| Cabelo | Aplicação no comprimento, cabelo em movimento |  
| Joia | Fechando um colar ou ajustando um anel |  
| Moda | Ajustando a peça no corpo, mão no tecido |  
| Eletrônico | Manuseio do aparelho, foco nas mãos |  
| Casa | Manuseio do item em gesto de uso |

---

HTML: [[_html/hero-9-atendimento-proativo.html]] · Seção: [[_hero]] · Protocolo: [[_protocolo-de-selecao]]
