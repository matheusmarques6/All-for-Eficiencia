---
tipo: componente
slug: body-4-comparativo-em-duas-colunas
secao: body
nome_no_banco: "body 4 - bridge fundo cards"
variant_id: 63736c6c-7d1b-4c7c-83ea-bae15599f1d7
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [welcome-meio, welcome-tardio, consideracao, browse-abandonment]
momento_vetado: [transacional, pos-compra]

# --- eixos de ranking, na ordem do protocolo ---
objecao: [qualidade-eficacia, preco-valor]
registro: []
registro_vetado: []
paleta: []
papel_na_peca: [meio]

# --- requisitos duros (eliminam) ---
exige: []
diretivas_de_imagem: []

# --- capacidade e composição ---
product_slots: 0
itens: { min: 5, max: 6 }
peso: { altura_px: 820, classe: medio, fonte: medido }
convivencia: []

# --- fios para o resto do vault ---
aprendizados: ["[[posicao-muda-o-efeito-do-dispositivo]]", "[[cada-alegacao-e-uma-promessa-operacional]]"]
serve_estruturas: []

# --- proveniência ---
fonte: revisao-html-2026-09-09
densidade_no_banco: null
schema_campos: 18
status: aprovada
---

## Descrição curta

Comparativo direto contra a concorrência em duas colunas: a marca de um lado, "os outros" do outro, cada coluna com foto circular no topo, título e uma lista de atributos numerados — afirmativos na coluna da marca, o inverso na genérica. Fecha com uma linha-resumo e um CTA de compra.

## Descrição detalhada

Container fixo de 600px sobre fundo branco. Título de seção em caixa alta (56px, duas linhas) alinhado à esquerda no topo da coluna esquerda — não é centralizado nem atravessa a largura toda. Abaixo, duas colunas lado a lado (células de 290px e 308px), cada uma com um painel de 272px: o painel abre com uma imagem 5:4 (272 × 212px — o círculo com a foto e os cantos superiores arredondados vêm compostos no arquivo) e continua num bloco de cor sólida com cantos inferiores arredondados (26px) — painel A (marca, `#BEBEBE`) e painel B (genérico, `#D1D1D1`). Dentro de cada painel, um título em caixa alta e uma lista de atributos numerados em círculos brancos de 27px (5 na coluna A, 6 na B), uma linha de texto por atributo. O painel B começa a 79px do topo, ao lado do título; o painel A só começa depois do título (~230px) — o degrau faz parte do desenho: título e painel B dividem a primeira dobra, o painel A entra abaixo. Depois das colunas, uma linha de fechamento de até duas linhas resumindo a escolha e um CTA bulletproof de 418 × 59px (pílula preta, `SHOP NOW`). Sem media query: o container é `min-width: 600px` e as colunas não empilham no mobile. Sem slot de oferta, sem cupom, sem preço.

## Quando usar

Quando a dúvida do cliente já existe e é "por que essa e não a genérica / a mais barata": welcome do meio para o fim, consideração, browse abandonment. Categorias em que os atributos são objetivos e verificáveis (composição, garantia, durabilidade, prazo, suporte) — cada item da coluna A é uma alegação que a operação precisa sustentar. Funciona quando a marca tem de 5 a 6 diferenças concretas para listar; menos que isso, o painel fica ralo.

## Quando NÃO usar

Primeiro toque de qualquer flow: comparar antes de a dúvida existir é defensivo e planta a desconfiança que pretendia curar (ver [[posicao-muda-o-efeito-do-dispositivo]]). Campanha de venda ou oferta (não há slot de cupom nem de preço). Pós-compra e transacional. Quando os "atributos" seriam adjetivos e não fatos — a coluna B nunca nomeia concorrente, mas cada linha da A é promessa operacional (ver [[cada-alegacao-e-uma-promessa-operacional]]).

## Orientações de copy para a IA

Título de seção em caixa alta, até 20 caracteres, nomeando a diferença ("POR QUE A GENTE"). Título da coluna A = nome da marca em caixa alta; título da coluna B = termo genérico ("OS OUTROS", "MARCAS COMUNS"), nunca um concorrente. Itens: atributo afirmativo curto na A (até 48 caracteres) e o inverso correspondente na B, item a item — a leitura é em pares. Linha de fechamento: uma frase resumindo a escolha (até 88 caracteres). CTA em caixa alta remetendo à diferença, não a "comprar agora".

## Design system

Container 600px. Duas colunas de 272px com gutter central; imagem 272 × 212px no topo de cada coluna emendando sem respiro com o painel abaixo. Painéis com `border-radius: 0 0 26px 26px` (degrada reto no Outlook, sem prejuízo). Linhas de atributo com 27px de altura; numeração em texto. CTA como link-bloco de 418 × 59px, 23px, Arial/Helvetica. Cores dos painéis são as da referência (`#BEBEBE`/`#D1D1D1` no HTML base; `#FAF7F2`/`#EFEFEF` na direção de imagem) — a marca troca pela paleta dela mantendo o contraste A > B.

## Direção fotográfica

Duas imagens 5:4 geradas, 544 × 424px (2x), PNG < 110 KB. **Coluna A:** canvas na cor do painel A com os cantos superiores arredondados (52px), círculo de Ø304px centralizado contendo a foto do produto da marca em máscara circular — cor saturada, textura legível, fundo branco de estúdio, luz difusa, sem rosto e sem logo. **Coluna B:** mesma construção na cor do painel B, com a versão genérica do mesmo tipo de produto: cinza neutro, sem marca, sem textura, mesmo enquadramento e mesma luz — a diferença é de saturação e detalhe, nunca de qualidade técnica. Sem logo de concorrente, sem desfoque proposital.

---

HTML: [[_html/body-4-comparativo-em-duas-colunas.html]] · Seção: [[_body]] · Protocolo: [[_protocolo-de-selecao]]
