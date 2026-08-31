---
tipo: componente
slug: body-10-listicle-educativo
secao: body
nome_no_banco: "body 10 - listicle educativo 3 dicas"
variant_id: 42c883e5-6c4a-43df-b18f-e7ee866e4ae7
ativa: false

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [nutricao-de-conteudo, welcome-meio, reengajamento]
momento_vetado: [campanha-promocional, abertura, welcome-1]

# --- eixos de ranking, na ordem do protocolo ---
objecao: [uso-aprendizado]
registro: []
registro_vetado: []
paleta: [creme]
papel_na_peca: []

# --- requisitos duros (eliminam) ---
exige: []  # veta tipo de campanha, marca sem material educativo aprovado (sem valor correspondente no vocabulario -- ver relatorio) e publico frio; nenhum vira exige hoje

# --- capacidade e composição ---
product_slots: 0
itens: { min: 3, max: 3 }
peso: { altura_px: 1355, classe: pesado, fonte: medido }
convivencia: []

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: média
schema_campos: 14
status: aprovada
---

## Descrição curta

Bloco de conteúdo educativo para quando a venda depende de o cliente entender um contexto antes de comprar. Entrega uma lista numerada de três itens com explicação e miniatura, e só converte no CTA depois de ter ensinado alguma coisa

## Descrição detalhada

Texto de abertura centralizado dentro de um painel arredondado, seguido de três cards empilhados dentro do mesmo painel, cada um com miniatura vertical à esquerda, título numerado e parágrafo explicativo alinhados à esquerda. Abaixo do painel, fora dele, dois parágrafos de fechamento centralizados e um CTA sólido.  

Quatro mecanismos sustentam a seção:  

Painel como delimitador de conteúdo. A lista vive dentro de um painel de fundo levemente distinto; a abertura contextual e o fechamento ficam soltos sobre o fundo da peça. A moldura separa visualmente "o que estou ensinando" de "o que estou dizendo".  
Card que cresce com o texto. Os três cards medem 496 de largura e alturas diferentes — 257, 232 e 228 na referência. Nenhum campo é truncado para caber.  
Miniatura em faixa vertical que acompanha o card. A imagem tem largura fixa de 77px e altura igual à do card menos 20px de folga em cima e embaixo (217, 194 e 187 na referência). Não é um crop de tamanho fixo: é uma tira que estica.  
Ressalva em negrito dentro do parágrafo. O aviso de responsabilidade aparece como trecho grifado no meio da frase de fechamento, não como bloco separado nem como letra miúda. É o único negrito fora dos títulos dos cards.

## Quando usar

Categoria em que o cliente precisa entender um mecanismo antes de comprar: suplemento, skincare ativo, saúde, nutrição, equipamento técnico.  
E-mail de nutrição de lista, welcome educativo ou reengajamento por conteúdo — a venda vem depois da informação.  
Marca que tem autoridade a demonstrar e um dado concreto para citar.  
Quando existe uma ressalva legítima a fazer (consultar profissional, restrição de uso) e ela precisa aparecer sem quebrar o tom.

## Quando NÃO usar

Campanhas promocionais (zero slot de oferta — o CTA é institucional). Marcas sem material educativo aprovado (a IA não pode gerar claims de saúde do zero). Públicos frios de topo de funil que ainda não conhecem a marca (o formato pressupõe interesse no tema).

## Orientações de copy para a IA

O conteúdo é sobre o mundo do cliente, não sobre o produto. Na referência, uma marca de recuperação pós-cirúrgica fala sobre alimentos, não sobre os próprios suplementos. O produto só aparece no CTA.  
O número faz parte do título e vem escrito no texto ("1. ", "2. ", "3. "), não como enfeite gráfico.  
Título nomeia o item em 2 a 4 palavras. O terceiro item pode quebrar o padrão com um gancho, como na referência, para o leitor não abandonar a lista no meio.  
Cada parágrafo explica o mecanismo, não só afirma o benefício: o que a coisa faz no corpo, por que funciona. Um dado numérico verificável em um dos três itens dá peso aos outros dois.  
Abertura em duas partes: uma frase que aponta o erro ou a lacuna, e uma que anuncia o que vem a seguir e fecha com dois-pontos.  
Fechamento em dois parágrafos: o primeiro traz a ressalva em negrito inline e devolve a permissão; o segundo projeta o resultado.  
CTA nomeia a marca, não a ação genérica.

## Design system

Container: 600px travado. Fundo   
#FAFAFA até a altura do CTA, onde transiciona para um gradiente quente (  
#EADDCC →   
#D7BC95) que continua na seção seguinte.  

Painel: x 28–571 (544 de largura), cantos arredondados ~20px, mesmo   
#FAFAFA do fundo, separado apenas por uma sombra difusa nas laterais e na base. Base do painel em y 1075, com 47px de folga abaixo do último card.  

Tipografia principal: sans humanista (perfil Asap/Inter). Não há tipografia secundária. O template substitui por Arial, Helvetica, sans-serif.  

| Bloco | Tamanho / entrelinha | Peso | Alinhamento |  
|---|---|---|---|  
| Abertura do painel | 22 / 24 | 400 | Centralizado |  
| Título do card | 24 / 24 | 700 | Esquerda |  
| Corpo do card | 22 / 24 | 400 | Esquerda |  
| Fechamento | 22 / 24 | 400 com trecho em 700 | Centralizado |  
| Label do CTA | ~28 | 700 | Centralizado, ALTA |  

Cores. Cor primária   
#0B2532 — um azul-petróleo escuro usado em todo o texto, títulos e corpo, nunca preto puro. Cor secundária   
#FAFAFA (fundo e painel). Card em   
#F3ECE4, um bege quente que é a única superfície colorida da lista. Cor de acento   
#941409 no CTA, com label branco. Nenhum outro elemento usa o acento.  

Grade e ritmo vertical (medido):  

PAINEL  x 28–571, raio 20  
   ↓ ~46px do topo do painel  
abertura parte 1        3 linhas, centralizado, largura de quebra ~410  
   ↓ 28px  
abertura parte 2        2 linhas, centralizado  
   ↓ 40px  
CARD 1  496 × 257 (x 53–548), raio 13, fundo #F3ECE4  
          +19  miniatura 77 × 217 (x 73–149), raio ~8  
          +23  título numerado (x 172)  
          +31  corpo — 7 linhas, x 172–515, entrelinha 24  
          26px de folga até a base do card  
   ↓ 40px  
CARD 2  496 × 232 — miniatura 77 × 194  
   ↓ 38px  
CARD 3  496 × 228 — miniatura 77 × 187  
   ↓ 47px  base do painel  
   ↓ 85px  
fechamento parágrafo 1  5 linhas, centralizado, x 65–535  
   ↓ 27px  
fechamento parágrafo 2  4 linhas, centralizado  
   ↓ 44px  
CTA     379 × 70 (x 111), fundo #941409, raio ~16  

Regras que não podem ser quebradas:  

O card cresce com o texto e a miniatura acompanha essa altura. Altura fixa quebra a variante.  
A miniatura tem largura fixa de 77px em todos os cards, sempre com 20px de folga em cima e embaixo dentro do card.  
Título e corpo do card são alinhados à esquerda; abertura e fechamento são centralizados. Essa troca de alinhamento é o que separa lista de discurso.  
A abertura e o fechamento ficam FORA do painel visualmente — a abertura dentro dele, o fechamento abaixo. Só a lista é emoldurada.  
Todo o texto é azul-petróleo   
#0B2532, nunca preto. O bege do card não tem contraste suficiente para preto puro sem endurecer o bloco.  
Só duas coisas em negrito: os títulos dos cards e o trecho de ressalva dentro do fechamento. Corpo, abertura e fechamento são regulares.  
Nenhum badge, ícone, seta, divisor ou borda. A hierarquia vem só de fundo, peso e alinhamento.

## Direção fotográfica

Macro de ingrediente ou material, recortado pela tira vertical estreita. A imagem é lida em 77px de largura — o que importa é textura e cor, não composição.  

Enquadramento: plano muito fechado, o assunto preenchendo o quadro inteiro. Nada de espaço negativo, nada de objeto inteiro com margem.  
Assunto: o ingrediente cru e reconhecível pela textura mesmo em miniatura — escama, casca, grão, fatia.  
Luz: natural e difusa, com sombra suave que dê volume. Sem flash duro, sem reflexo especular.  
Cor: cada uma das três miniaturas em uma faixa cromática distinta (na referência: prateado frio, marrom quente, amarelo saturado), para a pilha não virar um bloco só.  
Corte: o ativo é gerado quadrado e cortado verticalmente ao centro na montagem. Compor com o assunto no centro do quadro, porque as bordas superior e inferior serão descartadas.  
Proibições: prato montado, mão na cena, fundo branco de estúdio, produto da marca, texto ou selo sobreposto, imagem de banco genérica com aparência de anúncio.

---

HTML: [[_html/body-10-listicle-educativo.html]] · Seção: [[_body]] · Protocolo: [[_protocolo-de-selecao]]
