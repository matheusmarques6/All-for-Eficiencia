---
tipo: componente
slug: reviews-6-review-por-variante
secao: reviews
nome_no_banco: "review 6"
variant_id: 956b9e76-2c97-448e-bbfd-4a97f082e1dd
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: []
momento_vetado: []

# --- eixos de ranking, na ordem do protocolo ---
objecao: []
registro: []
registro_vetado: []
paleta: []
papel_na_peca: []

# --- requisitos duros (eliminam) ---
exige: []

# --- capacidade e composição ---
product_slots: 0
itens: null
peso: null
convivencia: []

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

Bloco de prova social para quando a loja precisa vender variedade de catálogo e não um produto único. Cada depoimento vem acompanhado do produto exato que o cliente comprou, então a seção funciona como prova social e vitrine ao mesmo tempo.

## Descrição detalhada

Título curto centralizado e três depoimentos empilhados em linhas idênticas de 598px: packshot vertical do produto à esquerda, coluna de texto centralizada à direita com régua de 5 estrelas, citação entre aspas e assinatura do cliente. Réguas horizontais pretas separam os depoimentos entre si, e um CTA sólido fecha a seção. A régua não aparece depois do terceiro depoimento — o CTA fecha o ritmo.  

Três mecanismos sustentam a seção:  

Um produto diferente por depoimento. A foto não ilustra o depoimento, ela é o SKU citado. É o que transforma três reviews em três oportunidades de compra sem virar grade de produtos.  
Coluna de texto centralizada verticalmente contra a foto. A foto tem altura fixa e o depoimento varia de 4 a 6 linhas; a centralização vertical mantém os três blocos alinhados sem ajuste manual. Medido na referência: os centros de texto e foto ficam a 8–14px um do outro nos três blocos, com o texto começando mais alto conforme cresce.  
Divisor como pausa, não como moldura. Uma régua preta curta e centralizada, sem card, sem fundo e sem borda. É o único elemento estrutural da seção.

## Quando usar

Marca com catálogo de variantes do mesmo tipo de produto (molho, sabor, fragrância, cor) e review escrito por variante.  
Softsell de catálogo, welcome com prova social, reengajamento de base fria ou cross-sell pós-compra.  
Produto com embalagem vertical e rótulo legível — a foto tem 293px de altura e 155 de largura.  
Loja com voz informal, que pode publicar o review do cliente sem editar.

## Quando NÃO usar

Menos de três depoimentos com produtos distintos. Repetir o mesmo produto nas três linhas anula o mecanismo.  
Depoimentos curtos (menos de 3 linhas). A coluna fica vazia ao lado de uma foto de 293px e o bloco desmonta.  
Produto sem packshot vertical: peça de roupa, item plano, serviço, assinatura.  
E-mail que já tem grade de produtos — a seção já cumpre esse papel e as duas juntas viram catálogo repetido.  
Marca de posicionamento sóbrio ou clínico. A variante depende de exagero e entusiasmo no texto do cliente.

## Orientações de copy para a IA

Um produto por depoimento, todos diferentes. Escolher reviews que citem variantes distintas do catálogo.  
Preservar o texto do cliente na íntegra, incluindo gíria, erro de pontuação e falta de vírgula. Não reescrever para "ficar limpo".  
Preservar a quebra de linha do review original quando ela existir. Na referência o terceiro depoimento abre com uma palavra isolada em linha própria, e é isso que dá o tom.  
Assinatura sempre abreviada: hífen + primeiro nome + inicial do sobrenome. Nunca nome completo, nunca @usuário.  
Título da seção em duas palavras, qualificando o depoimento pela categoria do produto. Não usar fórmula genérica do tipo "o que nossos clientes dizem".  
Sem selo de credencial nesta variante. Se a loja precisa de "compra verificada", usar outra variante de prova social.  
CTA aponta para o catálogo, não para um produto — a seção acabou de mostrar três.

## Design system

Container: 600px travado, fundo branco, sem borda.  

Tipografia principal: sans geométrica de peso alto para título e assinatura; o mesmo desenho, em regular, para a citação. Não há tipografia secundária. O template substitui por Arial, Helvetica, sans-serif como fallback web-safe.  

| Bloco | Tamanho / entrelinha | Peso | Alinhamento |  
|---|---|---|---|  
| Título da seção | 40 / 36 | 700 | Centralizado, ALTA |  
| Régua de estrelas | régua de 229 × 41 | — | Centralizado |  
| Citação | 22 / 26 | 400 | Centralizado |  
| Assinatura | 22 / 27 | 700 | Centralizado |  
| Label do CTA | 24 | 700 | Centralizado, ALTA, tracking 0.25em |  

Cores. Cor primária   
#000000 (título, citação, assinatura, divisor). Cor secundária   
#FFFFFF (fundo). Cor de acento   
#FEB801 — aplicada exclusivamente ao fundo do CTA, com label preto. É o único elemento colorido da seção fora das fotos.  

Grade e ritmo vertical (medido, normalizado para container de 600px):  

título da seção        centralizado, 1 linha  
   ↓ 91px  
DEPOIMENTO 1  linha de 598px — coluna foto 222px | coluna texto 376px  
              foto 155 × 293 (x 67–221) · texto centralizado vertical contra a foto  
              estrelas ↓30 citação ↓31 assinatura  
   ↓ 37px (medido a partir da BASE DA FOTO, não do texto)  
divisor        365 × 3, centralizado  
   ↓ 52px  
DEPOIMENTO 2  idêntico  
   ↓ 37px  
divisor        365 × 3  
   ↓ 59px  
DEPOIMENTO 3  idêntico, sem divisor depois  
   ↓ 38px  
CTA            201 × 48, fundo #FEB801, label preto  

Regras que não podem ser quebradas:  

Zero border-radius, zero sombra, zero gradiente, zero card, zero borda.  
A coluna de texto é centralizada verticalmente contra a foto (valign="middle"), nunca alinhada ao topo com padding fixo. É isso que faz depoimentos de 4 e de 6 linhas conviverem.  
O espaçamento até o divisor é medido a partir da base da foto, que é sempre o elemento mais alto da linha.  
Não existe divisor depois do último depoimento.  
As três fotos usam o mesmo slot, a mesma luz e o mesmo enquadramento. Variação entre elas quebra o ritmo da pilha.  
Todo o texto da coluna é centralizado — estrelas, citação e assinatura no mesmo eixo.  
display:block em toda <img> e célula da foto com font-size:0;line-height:0.

## Direção fotográfica

Packshot vertical do produto recortado em fundo branco puro (  
#FFFFFF), sem sombra projetada, sem superfície e sem cenário.  

Enquadramento: produto de frente, eixo vertical, rótulo inteiramente legível e centralizado no recorte. Sem rotação, sem perspectiva, sem inclinação.  
Escala: o produto ocupa 95–100% da altura do slot e é a altura que padroniza a pilha — as três fotos precisam terminar praticamente na mesma linha de base.  
Luz: difusa e frontal, alto-chave, com sombra própria suave nas laterais para separar a embalagem do branco. Sem realce especular no vidro, sem reflexo de softbox.  
Cor: a cor vem do rótulo do produto, não de tratamento. Sem filtro, sem viragem, sem saturação empurrada.  
Proibições: mão segurando, prato ou comida na cena, fundo colorido, sombra dura no chão, reflexo espelhado embaixo, moldura, recorte com halo cinza, produto deitado.

---

HTML: [[_html/reviews-6-review-por-variante.html]] · Seção: [[_reviews]] · Protocolo: [[_protocolo-de-selecao]]
