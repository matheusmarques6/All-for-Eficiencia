---
tipo: artefato
assunto: componentes-recorrentes
autor: convertfy
status: aprovado
fonte: 'Figma "ESTRUTURA FIGMA — RIDE NATION" — implementação Convertfy, 34 peças, extraído em 2026-09'
---

A Convertfy não desenha e-mail do zero: monta cada peça a partir de uma biblioteca pequena de blocos que se repetem verbatim entre flows diferentes. No arquivo da Ride Nation, quatro componentes aparecem em 22 das 23 peças desenhadas em português — barra de navegação, slot de descadastro, bloco de cupom e, em 12 delas, a barra de confiança. Esta nota conta em quantas peças cada bloco aparece, transcreve a copy exata de cada um e separa o que é reutilizável em outra marca do que não é. A distinção é o ponto: **os componentes são reutilizáveis; a copy deles não é.**

O universo são 34 peças. Sete são "TEXTO PURO" — templates em inglês com placeholders (`[Brand Name]`, `WELCOME10`) que não passaram por design e não carregam nenhum componente da biblioteca. Quatro são transacionais de status de pedido (`Pedido pago`, `Pedido em separação`, `Pedido em coleta`, `Pedido enviado`), extraídas quase vazias e ainda com produtos de demonstração em dólar (`Gather Phone Stand`, `$39.00`). Sobram **23 peças desenhadas em português**, e é sobre elas que a contagem faz sentido.

# A contagem — o que prova que é biblioteca

| Componente | Peças | Sobre 23 desenhadas | Flows |
|---|---|---|---|
| Barra de navegação | **22** | 22/23 | Browse 5/5 · Cart 6/6 · Welcome 6/7 · Post Purchase 3/3 · Site Abandon 1/1 · Winback 1/1 |
| Slot `Unsub Info` | **22** | 22/23 | idêntico ao da navegação, peça a peça |
| Bloco de cupom | **22** | 22/23 | todas menos Winback #1 (a única sem oferta) |
| Barra de confiança | **12** | 12/23 | Browse #4, #5 · Cart #3, #4, #5, #6 · Welcome #1, #4, #6 · Post Purchase #3 · Site Abandon #1 · Winback #1 |
| Bloco de produto dinâmico | **11** | 11/23 | só Browse (5/5) e Cart (6/6) |
| Depoimento nominal | **10** | 10/23 | Browse #3 · Cart #1, #4, #7 · Post Purchase #1, #2 · Welcome #1, #4, #6 · Winback #1 |
| Contador regressivo | **3** | 3/23 | Cart #3, #5 · Post Purchase #2 |
| Prova social agregada | **1** | 1/23 | Welcome #1 apenas |

**A leitura.** Navegação, `Unsub Info` e cupom aparecem no mesmo conjunto de 22 peças, com uma exceção cada: a navegação e o `Unsub Info` faltam só em Welcome #7 (a peça mais curta do arquivo), e o cupom falta só em Winback #1 (a única peça sem oferta). Isso não é coincidência de copywriting — é componente instanciado. A prova mais forte é posicional: **`Unsub Info` está em `y=415` em todas as 22 peças**, independentemente da altura total, que varia de 1549px a 4837px. Um bloco que cai no mesmo pixel em 22 layouts de altura diferente é componente colado, não texto redigitado.

A barra de confiança tem cobertura menor (12) mas atravessa **seis flows diferentes** com a copy idêntica caractere a caractere. Um bloco que aparece em Browse, Cart, Welcome, Post Purchase, Site Abandon e Winback com a mesma redação é biblioteca.

# Os componentes, verbatim

## Barra de navegação — 22 peças, sempre em `y=16`

`MAIS VENDIDOS` · `MASCULINO` · `MOLETOM` · `FEMININO`

Quatro itens, sempre nesta ordem, sempre em caixa alta. Em Browse Abandon #2 a extração traz junto um resíduo de layers em inglês de um template comprado (`Track your order`, `Biggest Sale`, `Accessories`, `Best seller`, `All shop`, `Contact us`), cada um triplicado — não é conteúdo da marca, é sujeira que sobrou do arquivo original.

## Barra de confiança — 12 peças, três colunas

| Título | Subtítulo |
|---|---|
| `"ENTREGA PRA TODO O BRASIL"` | `"Frete calculado no checkout. Sem surpresa no final, como tem que ser."` |
| `"TROCA SEM BUROCRACIA"` | `"7 dias. Sem formulário de 3 páginas. Sem drama. Só avisa a gente."` |
| `"PAGAMENTO SEGURO"` | `"Checkout protegido. Cartão, Pix ou boleto do jeito que você preferir."` |

Sempre as três colunas, sempre nesta ordem, sempre com esta redação. Nas 12 peças o bloco fica na metade inferior, depois do CTA principal — é fechamento de objeção, não abertura.

## Bloco de cupom — 22 peças

Estrutura fixa: rótulo `CUPOM:` + código em display + botão. Aparece **33 vezes** ao todo, porque peças longas repetem o cupom duas, três ou quatro vezes (Welcome #2 traz quatro instâncias, Cart #3 e Post Purchase #1 trazem três).

O rótulo tem duas caixas no mesmo arquivo: `CUPOM:` em 26 ocorrências e `cupom:` em 7. Códigos por peça: `BEMVINDO10` (7), `DESCONTO10` (4), `ESPECIAL` (3), `EXCLUSIVO12` (3), `EXCLUSIVO14` (2), `DESCONTO12` (2), `VOLTEI12` (1). Um código por flow, com o desconto embutido no nome — exceto `ESPECIAL`, que não carrega número. Em Browse Abandon #3 o código aparece grafado `EXCLUSIVo12`, com o "o" minúsculo, contra `EXCLUSIVO12` nas outras duas peças do mesmo flow: **é o mesmo cupom escrito de dois jeitos**, e se o código for case-sensitive no checkout, é falha funcional, não estética.

## Slot `Unsub Info` — 22 peças, sempre em `y=415`

Marcador de layer, não copy final — o texto de descadastro que vai ao ar não está na fonte. `[não consta na fonte]`. Em Browse Abandon #2 o marcador aparece 7 vezes na mesma peça, provável duplicação de layer.

## Bloco de produto dinâmico — 11 peças

Marcador `[in-klaviyo Dynamic Product section]`, exclusivo de Browse e Cart — os dois flows em que o e-mail sabe qual produto a pessoa viu. Nenhuma peça de Welcome, Post Purchase, Site Abandon ou Winback usa. Cinco peças trazem duas seções na mesma peça. Confirma Klaviyo como ESP desta implementação.

## Prova social — o que a instrução supunha e o que a fonte mostra

O bloco `"+25,000"` / `"clientes satisfeitOs"` / `"4.8/5 de 2,847 reviews verificados"` / `"Cliente verificado"` **aparece em uma única peça: Welcome #1.** Não é componente recorrente; é bloco único. Transcrito verbatim, com o `O` maiúsculo indevido em `"satisfeitOs"` preservado como está na fonte — é erro de digitação do original, não da transcrição.

O que recorre é a **função**, não o bloco: dez peças provam socialmente, mas com números que não conversam entre si.

| Peça | Número exibido |
|---|---|
| Welcome #1 | `"+25,000"` / `"clientes satisfeitOs"` · `"4.8/5 de 2,847 reviews verificados"` |
| Cart Abandon #7 | `"+50.000"` / `"PESSOAS JÁ VESTEM A CENA"` |
| Cart Abandon #4 | `"4.9/5 (12.847 avaliações)"` |
| Post Purchase #1 | `"4.9/5.0"` / `"avaliação média dos nossos clientes"` |

Base de clientes de 25 mil e de 50 mil, nota 4.8 e 4.9, 2.847 e 12.847 avaliações — no mesmo arquivo. **Números de prova social não foram tratados como componente e por isso divergiram.** Se um assinante receber Welcome #1 e Cart Abandon #7, vê duas versões do tamanho da mesma marca. Corrigir antes de replicar.

O que de fato se repete é o **formato do depoimento** (10 peças): aspas + nome com inicial (`Rafael M.`, `Lucas M.`, `Diego M.`), às vezes com nota `5.0` (5 peças) e, só em Post Purchase #1, com cidade (`Rafael M. - São Paulo/SP`). Formato reutilizável; nomes e falas, não.

# O tom de voz que emerge

A copy é marcada e consistente. `crew` aparece em 8 peças, `rolê` em 9, `garimpar` em 4, `pista` e `cena` como sinônimos de comunidade. A negação é a figura preferida: `"sem firula"`, `"Sem drama"`, `"Sem formulário de 3 páginas"`, `"sem call center e sem discurso de política"`, `"Sem postura de grife, sem discurso de lifestyle forçado"`, `"Não é papo de marketing"`, `"Não é papo, é dado"`. A marca se define pelo que recusa.

Segunda pessoa informal e contração oral: `"Teu carrinho ainda tá aqui."`, `"TUA PEÇA TÁ AQUI."`, `"A decisão é tua."`, `"Bora de novo?"`. Frases curtas, ponto final no lugar de vírgula: `"Quando sumir, sumiu."`, `"O tempo não espera."` O antagonista é sempre o mesmo — fast fashion e marca gringa: `"Camiseta bonita por 60 reais que desbota na terceira lavagem não é economia — é desperdício."`

Este tom é o que faz a copy da biblioteca funcionar. `"7 dias. Sem formulário de 3 páginas. Sem drama. Só avisa a gente."` não é uma política de troca escrita de forma neutra — é a política de troca escrita **nesta voz**, com a mesma estrutura de negação do resto do arquivo.

# Componentes reutilizáveis, copy não — o ponto da nota

Ao replicar esta estrutura em outra marca, a linha de corte é limpa:

**Reutilize sem alterar (a arquitetura):**
- Barra de navegação com quatro categorias em caixa alta, topo da peça, `y=16`.
- Barra de confiança de três colunas: entrega, troca, pagamento — nesta ordem, na metade inferior, depois do CTA.
- Bloco de cupom com rótulo + código + botão, repetido a cada ~700-900px em peça longa.
- Slot de descadastro em posição fixa.
- Produto dinâmico só em Browse e Cart.
- Depoimento com aspas + nome com inicial.

**Reescreva do zero (a copy):**
- Todo o texto entre aspas desta nota. `"Sem drama. Só avisa a gente."` numa marca de skincare premium ou numa fintech soa desleixado, não próximo. `"ENTREGA PRA TODO O BRASIL"` é abrangência nacional dita com orgulho de marca de nicho — em marca de luxo, abrangência não é argumento.
- As categorias da navegação, que são o catálogo desta loja.
- Os nomes de cupom, que embutem tanto o desconto quanto a voz (`VOLTEI12`, `BEMVINDO10`).
- Todos os números de prova social.

**O erro previsível** é herdar o arquivo e trocar só logo e cores. O resultado é uma marca falando com voz emprestada em 12 peças ao mesmo tempo — e a barra de confiança, justamente por ser a copy mais reaproveitável do ponto de vista funcional, é a que mais denuncia, porque aparece em seis flows.

**O teste prático:** para cada bloco reaproveitado, pergunte "esta frase existiria se ninguém tivesse escrito a Ride Nation?". Se a resposta for não, o slot fica, a frase sai.

# Um sinal de que a biblioteca ainda não fechou

Doze das 23 peças desenhadas ainda têm placeholders não preenchidos — `Headline`, `Body Copy`, `Subheadline` aparecem literalmente na extração (Post Purchase #1 e #3 e Site Abandon #1 com três cada). Somadas às 7 peças de texto puro em inglês e às 4 transacionais com produto de demonstração em dólar, o arquivo entregue está **parcialmente instanciado**. Os componentes fixos estão colados em toda parte; o conteúdo variável, não. Ao replicar, conte com essa lacuna: a biblioteca resolve o esqueleto, não a peça.

# O que este material não prova

1. **É uma implementação, não uma amostra.** Um cliente, a Ride Nation, um arquivo Figma, 34 peças. A recorrência documentada é interna a este arquivo. Nada aqui mostra que a Convertfy use os mesmos componentes em outros clientes — isso é afirmação da casa, não do documento.
2. **Não há nenhum número anexado.** Nem abertura, nem clique, nem receita, nem A/B, nem período. Não existe evidência de que a barra de confiança em 12 peças tenha convertido melhor do que a ausência dela nas outras 11.
3. **Os números que aparecem são copy, não medição.** `"+25,000"`, `"4.8/5 de 2,847"`, `"387 pessoas"`, `"27 unidades vendidas nas últimas 24h"` são argumentos de venda dentro das peças — e, como mostrado acima, contradizem uns aos outros.
4. **Esta nota é padrão de execução, não medição.** Serve para reproduzir a estrutura com fidelidade. Não use como base para afirmar que esta biblioteca converte mais que outra.
