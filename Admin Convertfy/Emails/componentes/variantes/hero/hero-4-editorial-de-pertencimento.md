---
tipo: componente
slug: hero-4-editorial-de-pertencimento
secao: hero
nome_no_banco: "welcome - hero section 4"
variant_id: e447ef06-95e2-4c5d-9b6f-c3e0b895f8d2
ativa: true
dispositivo: codigo_entregue

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [welcome-1]
momento_vetado: [carrinho-abandonado, checkout-abandonado, browse-abandonment, transacional, catalogo-mais-vendidos, campanha-promocional]

# --- eixos de ranking, na ordem do protocolo ---
objecao: [pertencimento]
registro: [premium-editorial]
registro_vetado: []
paleta: [com-acento-definido]
papel_na_peca: [abre]

# --- requisitos duros (eliminam) ---
exige: [serif-ou-script-display, cupom-ativo, cor-de-acento-definida]
diretivas_de_imagem: [foto-de-campanha-propria]

# --- capacidade e composição ---
product_slots: 0
itens: null
peso: { altura_px: 1150, classe: medio, fonte: medido }
convivencia: []

# --- fios para o resto do vault ---
aprendizados: ["[[incentivo-precisa-existir-em-texto]]"]
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: null
schema_campos: 9
status: aprovada
---

## Descrição curta

Primeiro e-mail da régua de boas-vindas em registro editorial de moda. Acolhe o contato como membro de um grupo, entrega o cupom e apresenta a marca por meio de fotografia de campanha. Momento de uso: welcome #1 de marca com identidade visual forte, logo após o opt-in, quando o argumento é pertencimento e não desconto puro.

## Descrição detalhada

Uma imagem única de 1150px cobre o e-mail inteiro. Wordmark, lockup, tagline, linha do cupom, código e CTA são sobrepostos aos 43% superiores dessa imagem. Não há barra de logo, não há bloco de cor, não há emenda.  

Quatro mecanismos definem a variante:  

O lockup são duas linhas de famílias diferentes com sobreposição vertical. Um script caligráfico por cima de uma serif display, com as caixas se cruzando. É o elemento de identidade da peça e precisa ser entregue como PNG transparente ou queimado na foto — script não sobrevive a texto vivo em cliente de e-mail.  

Três famílias tipográficas com territórios rígidos. Script para a saudação, serif display para marca e nome do grupo, sans para tudo que é instrução. Nenhuma família invade o território da outra.  

A cor de acento vem do guarda-roupa da cena. O botão e o trecho destacado da linha do cupom usam a mesma cor da roupa da modelo. É o que amarra foto e interface.  

O código do cupom não tem contêiner. Sem caixa, sem borda, sem cor própria — só bold e o respiro em volta.

## Quando usar

marca com identidade visual forte e fotografia de campanha própria.  
Moda, beachwear, resort, lingerie, joia — categorias em que a foto de campanha carrega o posicionamento.  
Quando a marca tem script ou serif display de identidade que justifica o lockup.  
Quando a cena de campanha tem guarda-roupa em cor definida que pode virar o acento da interface.  
Quando o argumento é pertencimento a um grupo ("família", "clube", "círculo") e não só o percentual.

## Quando NÃO usar

Sem identidade tipográfica própria. Sem script + serif display, o lockup não se sustenta — use o welcome de fundo fotográfico simples.  
Sem foto de campanha. Banco de imagem em 598 × 1150 denuncia a marca.  
Sem cupom — a estrutura tem três slots dedicados à oferta.  
Carrinho, checkout, browse, transacional, catálogo.  
Campanha de urgência — o registro editorial não comporta prazo.  
Quando o lockup teria que ser texto vivo por restrição de produção.

## Orientações de copy para a IA

Wordmark — nome da marca, ativo de imagem ou texto vivo conforme a marca.  

Lockup — uma frase única quebrada entre duas famílias. Linha 1 em script é a saudação; linha 2 em serif é o nome do grupo. As duas nunca são frases independentes — a leitura tem que ser contínua ("welcome to the" + "royal family").  

Tagline — posicionamento em uma frase completa, com ponto final. É o elemento mais largo da peça.  

Linha do cupom — instrução com o valor da oferta em bold e na cor de acento, no meio da frase. O código vem na linha seguinte, isolado, em bold, sem caixa e sem cor própria.  

CTA — verbo genérico em caixa alta com tracking largo. Não repetir o desconto: ele já foi dito na linha do cupom.  

Tom: aspiracional e acolhedor, posicionando o cliente como membro. Sem urgência, sem exclamação, sem contagem regressiva.  

Proibições: lockup com duas frases independentes · desconto no botão · código em caixa · segunda oferta · exclamação · tagline em duas linhas (empurra o botão para dentro da zona do sujeito).

## Design system

6. Design system  

Container 600px fixo, borda 1px   
#000000 opcional (flag has_border). Zero raio, zero sombra, zero gradiente. Preheader oculto obrigatório.  

Estrutura — elemento único: hero como imagem de fundo, 598 × 1150px.  

Zonas internas  

| Zona | Faixa | Conteúdo |  
|---|---|---|  
| Limpa | 0 – 489px (topo 43%) | Superfície lisa da foto. Recebe todo o overlay. |  
| Sujeito | 489 – 1150px (base 57%) | Modelos e cenário. Nenhum elemento sobreposto. |  

Overlay  

| Elemento | Padding-top | Dimensão |  
|---|---|---|  
| Wordmark | 27px | 152 × 48px |  
| Lockup (2 linhas sobrepostas) | 52px | 50/57px, tracking −0.06em, padding lateral 24px |  
| Tagline | 52px | 22/27px, padding lateral 30px |  
| Linha do cupom | 20px | 22/27px |  
| Código | 15px | 22/27px, bold |  
| CTA | 26px | 311 × 54px |  
| Área livre do sujeito | — | 661px |  

Paleta — três cores.  

| Papel | Hex (Royal Codes) | Uso |  
|---|---|---|  
| Cor primária |  |  |  
| #997754 | Fundo — vem da foto, não de CSS |  |  
| Cor secundária |  |  |  
| #FFFFFF | Wordmark, lockup, tagline, linha do cupom, código, label do botão |  |  
| Acento |  |  |  
| #5C1725 | Fundo do botão e o valor da oferta dentro da linha do cupom |  |  

Regras: a primária é pipetada da parede da foto e entra como background-color de fallback. O acento é retirado do guarda-roupa da cena — é regra obrigatória no briefing de imagem, porque é o detalhe que um fotógrafo nunca adivinha. Não existe quarta cor.  

Pele alternativa (HTML base): fundo branco, texto e botão pretos, wordmark em caixa com borda de 1px, sem cor de acento. Usar quando a marca não tem cena de campanha com cor definida.  

Tipografia — três famílias com territórios rígidos.  

Principal: sans geométrica (perfil Montserrat), fallback Arial → Helvetica. Cobre tagline, linha do cupom, código e label do botão — 4 dos 6 blocos.  
Secundária: serif display de alto contraste (perfil Playfair). Só o wordmark e a linha 2 do lockup.  
Terciária: script caligráfico. Uso único: linha 1 do lockup.  

Script dá o tom, serif dá a marca, sans dá as instruções. As duas linhas do lockup se sobrepõem em ~27px; ambas centralizadas, mas o eixo óptico do script cai um pouco à direita pela inclinação natural da caligrafia — não forçar alinhamento matemático. CTA 18px com tracking +0.25em e text-indent compensando.  

Implementação. background no <td> + background-image inline + background-size:598px 1150px, background-color na cor primária como fallback, bloco VML v:rect/v:fill type="frame" para Outlook. O lockup entra como PNG transparente sobreposto ou queimado na foto. Tagline, linha do cupom, código e botão ficam vivos em HTML. O valor da oferta é um <span> na cor de acento com font-weight:700. Botão bulletproof. Com imagem bloqueada a peça perde o lockup — o alt deve carregar a frase de acolhimento.  

Tags: PREHEADER, HERO_IMAGE_URL, BRAND_NAME, LOCKUP_IMAGE_URL, HERO_TAGLINE, OFFER_VALUE, COUPON_CODE, CTA_LABEL, CTA_URL. O lockup não tem tag de texto — é ativo de imagem. Se precisar variar por loja, vira etapa de design, não de merge.  

Erros que quebram o padrão: separar script e serif sem sobreposição · renderizar o script como texto vivo · barra de logotipo acima do wordmark · sujeito invadindo a zona limpa · guarda-roupa fora da paleta de acento · código em caixa tracejada · repetir o desconto no botão · quarta cor · botão com raio ou com a largura da caixa de texto · overlay escuro sobre a foto.

## Direção fotográfica

7. Direção fotográfica  

Proporção 9:16 — slot de 598 × 1150px, ativo final 1196 × 2300px (2x). JPG q80 ou WebP, < 320 KB, full-bleed. Gerar em 9:16 na altura de 2300px (1294 × 2300) e cortar 98px de largura, 49px de cada lado, para chegar ao ativo final.  

Regra crítica: os 43% superiores têm que ser uma superfície lisa e uniforme — parede, céu, areia ao longe. É ela que recebe wordmark, lockup, tagline, cupom e botão. Nenhum objeto, nenhuma sombra dura, nenhuma variação de cor forte nessa faixa.  

Regra obrigatória de produção: o guarda-roupa da cena tem que estar na cor de acento da interface. Botão e destaque do cupom são pipetados do look. Sem isso, a peça se desmonta em duas metades que não conversam.  

Composição. Duas figuras ou uma, ocupando a base do quadro, em corpo parcial — cortadas pela borda inferior. Pose relaxada, olhar para a câmera. Elemento vegetal ou arquitetônico entrando por um canto inferior. Sombra projetada nas laterais da metade inferior.  

Cenário e luz. Parede lisa em tom neutro quente ocupando o topo; superfície clara na base (areia, piso, tecido). Luz natural quente, contraste médio, sem estourar as altas na zona do texto. Paleta monocromática quente, com o guarda-roupa sendo o único ponto de cor saturada.  

Proibições: objeto ou textura forte na zona limpa · sujeito subindo acima de 43% · fundo de estúdio · guarda-roupa fora da paleta de acento · texto/preço/selo queimado (exceto o lockup, quando queimado por decisão de produção) · overlay ou vinheta · marca d'água.  

Adaptação por categoria — o que é a cena:  

| Categoria | Cena |  
|---|---|  
| Moda / resort | Duplas em look de coleção, parede e areia |  
| Beachwear | Corpo parcial, piscina ou duna ao fundo |  
| Lingerie | Interior de tom quente, luz de janela |  
| Joia | Busto e mãos em cena de lifestyle, parede lisa |  
| Beleza | Retrato de meio corpo, fundo de parede texturizada |  
| Casa | Ambiente vivido com pessoa em uso, parede lisa acima |

---

HTML: [[_html/hero-4-editorial-de-pertencimento.html]] · Seção: [[_hero]] · Protocolo: [[_protocolo-de-selecao]]
