---
tipo: componente
slug: reviews-8-ugc-de-comunidade
secao: reviews
nome_no_banco: "review 8"
variant_id: d92f812f-d83e-4e82-99a6-11286eba0e07
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: []
momento_vetado: []

# --- eixos de ranking, na ordem do protocolo ---
objecao: [pertencimento]
registro: [comunidade-identitario]
registro_vetado: [premium-editorial, minimalista-leve, clinico-sobrio]
paleta: [creme]
papel_na_peca: [peca-inteira]

# --- requisitos duros (eliminam) ---
exige: [ugc-autorizado]

# --- capacidade e composição ---
product_slots: 0
itens: { min: 3, max: 3 }
peso: { altura_px: 2500, classe: peca-inteira, fonte: declarado }
convivencia: [peca-inteira-nao-e-bloco]

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: null
schema_campos: 18
status: aprovada
---

## Descrição curta

Bloco de prova social para marca de comunidade, onde a conversão vem de identificação com quem já usa e não com o produto. Usa foto de cliente real, selo de compra verificada e um CTA por depoimento para levar cada leitor ao item que ele viu na foto.

## Descrição detalhada

Título centralizado em duas linhas seguido de três depoimentos empilhados. Cada depoimento é uma composição de duas camadas: fotos de cliente montadas como polaroids giradas, sobrepostas e sangrando pelas duas bordas do container, e por cima delas um cartão de papel rasgado de altura fixa com avatar de inicial, selo de verificação, régua de estrelas, nome, depoimento e CTA próprio. Fecha com um CTA final de largura maior e cor diferente.  

Quatro mecanismos sustentam a seção:  

Foto de cliente, não de produto. As imagens são fotos enviadas pelo comprador, com a peça vestida em contexto real. É o mecanismo central: a prova é a pessoa, não o packshot.  
Montagem de polaroid girada e sangrada. Cada foto tem moldura branca, sombra suave e rotação de 2° a 5° em sentidos opostos, e ultrapassa as duas bordas do container. O recorte pelo limite de 600px é o que dá a aparência de foto solta em cima da mesa.  
Cartão de papel de altura fixa. O bloco de papel mede sempre 464 × 387 e sobrepõe o terço inferior das fotos. A altura não cresce com o texto — o depoimento tem que caber, e é isso que limita a copy a 5 ou 6 linhas.  
CTA por depoimento. Cada card tem seu próprio botão apontando para o item daquele review, e o CTA final, maior e em outra cor, aponta para a loja inteira.

## Quando usar

Marca de comunidade ou de nicho identitário (fé, esporte, causa, fandom), onde o cliente posta a peça em uso.  
Loja com acervo de UGC real — foto enviada pelo comprador, não campanha produzida.  
Reviews longos e emocionais, que falam de pertencimento e não de especificação técnica.  
Catálogo com três categorias distintas para linkar (camiseta, moletom, acessório na referência).

## Quando NÃO usar

Sem UGC autorizado. A seção inteira depende de foto de pessoa real; substituir por foto de estúdio derruba o mecanismo.  
Marca de posicionamento premium, minimalista ou clínico. Papel rasgado, polaroid girada e selo azul são deliberadamente informais.  
Reviews curtos ou técnicos. Menos de 4 linhas deixa o cartão de altura fixa com um vazio embaixo do texto.  
E-mail curto ou com pressa: a seção tem quase 2500px de altura, é uma peça inteira, não um bloco de apoio.  
Loja de produto único — os três CTAs por depoimento não teriam para onde apontar.

## Orientações de copy para a IA

Preservar o depoimento na íntegra, com erro de digitação, caixa baixa no meio da frase, gíria e excesso de exclamação. Na referência há um "(i'm wearing it rn)" e um "HWLF!!!" — é isso que autentica.  
Cada depoimento sobre um produto diferente, e o CTA daquele card aponta para o produto citado.  
Título fala do cliente, não da marca: o que a pessoa está fazendo ao usar a peça. Duas linhas, caixa alta.  
Nome sempre só o primeiro nome, sem sobrenome e sem inicial. A inicial já aparece no avatar.  
Selo de credencial fixo e igual nos três ("Verified" / "Compra verificada"). É texto de sistema, não copy.  
Limite rígido de 6 linhas no depoimento: o cartão não cresce. Se o review original for maior, cortar pelo fim mantendo a frase de fechamento emocional.  
CTA de card curto e igual nos três; CTA final carrega o nome da marca.

## Design system

Container: 600px travado. Fundo em gradiente vertical sutil de verde-sálvia claro (  
#F1F3E8 no topo →   
#E3EADA no meio →   
#FAF9F4 na base) — não é branco chapado.  

Tipografia principal: sans humanista de peso alto (perfil Asap/Inter) em todos os blocos. Não há tipografia secundária. O template substitui por Arial, Helvetica, sans-serif.  

| Bloco | Tamanho / entrelinha | Peso | Caixa |  
|---|---|---|---|  
| Título da seção | 40 / 46 | 700 | ALTA, centralizado |  
| Inicial do avatar | ~40 | 700 | ALTA |  
| Régua de estrelas | régua de 152 × 25 | — | ★ ×5 |  
| Selo de verificação | ~17 dentro de chip 85 × 25 | 700 | Sentença |  
| Nome | ~24 | 700 | Sentença |  
| Depoimento | 22 / 23 | 400 | Sentença |  
| Label dos CTAs | ~20 | 700 | ALTA |  

Cores. Cor primária   
#0B0A07 (título, nome, depoimento — praticamente preto, não cinza). Cor secundária   
#FFFFFF (moldura das polaroids e label dos CTAs de card). Três acentos com função fixa:   
#F3B137 nas estrelas,   
#009CCD no chip de verificação,   
#859274 no CTA de cada depoimento. O CTA final usa   
#FAAFCE com label preto. Papel do cartão em bege texturizado   
#E5D9C9.  

Grade e ritmo vertical (medido):  

título (2 linhas)          centralizado  
   ↓ 22px  
REVIEW 1   fotos: 2 polaroids giradas, sangrando x=0 e x=599  
           cartão de papel 464 × 387 (x 65–528), sobrepondo o terço inferior das fotos  
             +32  avatar 79 × 79 (x 108)  
             +36  estrelas 152 × 25 (x 215)  
             +78  chip "Verified" 85 × 25 + nome ao lado  
             +136 depoimento — 5 a 6 linhas, x 108–500, entrelinha 23  
             CTA 327 × 59 (x 136), ancorado ~40px acima da base do cartão  
   ↓ 75px  
REVIEW 2   idêntico  
   ↓ 84px  
REVIEW 3   uma foto só, sem moldura e quase sem giro; mesmo cartão  
   ↓ 73px  
CTA FINAL  495 × 59 (x 52), fundo #FAAFCE, label preto  
   ↓ 96px  

Regras que não podem ser quebradas:  

O cartão de papel tem altura fixa (387). O texto se adapta ao cartão, nunca o contrário.  
As fotos sangram pelas duas bordas do container e são recortadas pelo limite de 600px. Contê-las dentro da largura anula o efeito.  
Rotações sempre em sentidos opostos entre as duas fotos do mesmo review, entre 2° e 5°. Nunca alinhar ao eixo.  
Todos os botões têm borda preta de 1px e raio de 5px. Os CTAs de card são verdes e iguais entre si; o CTA final é maior e de outra cor.  
Cada acento tem um dono: dourado é estrela, azul é verificação, verde é CTA de card, rosa é CTA final. Nenhum deles aparece em outro lugar.  
O texto do depoimento é preto, não cinza. O cinza tira a legibilidade contra o papel bege.  
O avatar carrega a inicial do nome e o selo circular de check no canto inferior direito — os dois juntos, sempre.

## Direção fotográfica

Foto enviada pelo cliente, não produzida. É o único bloco do arsenal em que grão, enquadramento torto e luz irregular são desejáveis.  

Cena: ambiente real e cotidiano — praia, cafeteria, campo, rua. Nunca fundo infinito ou estúdio.  
Pessoa: corpo inteiro ou três quartos, de costas, de lado ou com o rosto parcialmente cortado. A peça é o assunto; a identificação vem da postura, não do rosto.  
Peça: vestida e legível — estampa, cor e caimento reconhecíveis à distância de miniatura.  
Luz: natural, hora do dia qualquer, com estouro e sombra dura permitidos.  
Par de fotos: as duas do mesmo review mostram o mesmo produto em ângulos diferentes (frente e costas, ou perto e longe). Não usar duas fotos quase idênticas.  
Tratamento: moldura branca de ~12px em volta, sombra suave difusa embaixo, rotação leve. Sem filtro, sem viragem de cor, sem borda preta.  
Proibições: foto de banco de imagem, modelo profissional posando, packshot em fundo branco, colagem com texto sobreposto, marca d'água de rede social.

---

HTML: [[_html/reviews-8-ugc-de-comunidade.html]] · Seção: [[_reviews]] · Protocolo: [[_protocolo-de-selecao]]
