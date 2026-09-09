---
tipo: artefato
assunto: manual-da-marca-ride-nation
autor: convertfy
status: aprovado
fonte: 'Figma "ESTRUTURA FIGMA — RIDE NATION" — prancha MANUAL DA MARCA, implementação Convertfy, extraído em 2026-09'
---

O manual da marca da Ride Nation, na prancha MANUAL DA MARCA do Figma da Convertfy, define quatro cores, duas fontes, dois níveis de botão e três selos de confiança. Ele tem dois defeitos que quebram qualquer leitura automática: o swatch rotulado "Azul · #0018FF" está renderizado preto, e o swatch rotulado "Branco" tem o hex `#000000`. Use esta nota como a versão corrigida e anotada do manual — os hexadecimais declarados não podem ser copiados direto para código ou prompt sem passar pelas ressalvas registradas abaixo. O sistema que os e-mails realmente usam é preto, branco e dois cinzas; o azul declarado não aparece em nenhum botão da prancha.

Cliente: Ride Nation, streetwear/ciclismo, ticket R$ 100-250, Brasil. Implementação da Convertfy. Todas as citações abaixo estão verbatim, em português, com os erros de digitação e de caixa preservados como estão na fonte.

# Os dois defeitos confirmados na prancha

Ambos foram conferidos contra a imagem renderizada da prancha, não só contra a estrutura do arquivo.

**Defeito 1 — o "Azul" é preto.** Na prancha, o primeiro swatch de Cores Primárias é um círculo **preto sólido**, e ao lado dele está escrito `Azul` com o hex `#0018FF` embaixo. `#0018FF` é um azul saturado; o que se vê é preto. Ou o preenchimento do círculo foi trocado, ou o rótulo/hex é resíduo de uma versão anterior da paleta. **Não é possível decidir pela fonte qual dos dois é a verdade.** `[não consta na fonte]`

**Defeito 2 — o "Branco" tem hex de preto.** O segundo swatch de Cores Primárias é um círculo **branco**, corretamente branco na renderização, mas o texto embaixo diz `Branco` / `#000000`. Deveria ser `#FFFFFF`. Este é o defeito mais perigoso dos dois: a renderização está certa e só o texto está errado, então um humano que olhe a prancha não percebe nada — mas **uma IA ou um dev que leia o hex literalmente produz preto onde se quer branco**, e o erro passa silencioso até alguém abrir o e-mail e ver texto preto sobre fundo preto.

**Regra de uso:** ao passar esta paleta para qualquer ferramenta automática, substitua `#000000` por `#FFFFFF` no "Branco" e trate o "Azul" como não-confiável até confirmação do cliente.

# Cores primárias

| Nome na prancha | Hex declarado | O que a prancha realmente mostra | Ação |
|---|---|---|---|
| `Azul` | `#0018FF` | Círculo **preto sólido** — nenhum azul visível | Conflito não resolvido. Não use `#0018FF` sem confirmar |
| `Branco` | `#000000` | Círculo **branco** | Hex errado. Leia como `#FFFFFF` |

Há ainda um `#00ded7` (ciano/turquesa) registrado na estrutura do arquivo Figma que **não aparece na prancha renderizada** — não há swatch, rótulo nem hex visível para ele. Pode ser layer oculta, resíduo ou cor de anotação. Não trate como cor de marca. `[não consta na fonte]` qual o papel dele.

# Cores secundárias

| Nome na prancha | Hex declarado | O que a prancha realmente mostra | Consistente? |
|---|---|---|---|
| `Chumbo` | `#323232` | Círculo cinza-escuro, quase preto | Sim |
| `Cinza Claro` | `#DDDDDD` | Círculo cinza muito claro | Sim |

As secundárias são as duas únicas entradas da paleta em que rótulo, hex e renderização batem entre si.

# Tipografia

A prancha traz uma tabela de três colunas: `Nome`, `Sans`, `Uso`.

| Nome | "Sans" | Uso declarado |
|---|---|---|
| `NANUMMYEONGJO` | `Regular` | `"Títulos e informações de destaque"` |
| `MONTSERRAT` | `Regular` | `"Subtítulo e informações complementares"` |

Duas observações sobre a tabela, ambas do que se vê:

1. A coluna se chama `Sans`, mas os valores preenchidos nela são pesos (`Regular`, `Regular`), não classificações de família. O cabeçalho não descreve o conteúdo.
2. O espécime de `NANUMMYEONGJO` está renderizado **com serifas** — NanumMyeongjo é uma serifada, e é assim que ela aparece na prancha, sob a coluna chamada "Sans". A escolha em si é coerente com o resultado (serifada para título, sans para corpo); só o rótulo da coluna é que não fecha.

Só um peso está declarado para cada fonte. Não há escala tipográfica, tamanhos, entrelinha, nem definição para caixa alta — e as peças usam caixa alta o tempo todo. `[não consta na fonte]`

# Botões

A prancha mostra dois grupos, cada um com duas variantes, todas rotuladas `Comprar Agora`:

| Grupo | Variante | Aparência na prancha |
|---|---|---|
| `Botões primários` | 1 | Fundo **preto**, texto branco |
| `Botões primários` | 2 | Fundo **branco**, texto preto |
| `Botões Secundários` | 1 | Fundo **cinza-escuro** (lê como Chumbo), texto branco |
| `Botões Secundários` | 2 | Fundo **cinza-claro** (lê como Cinza Claro), texto escuro |

Os hexadecimais dos preenchimentos não estão escritos na prancha; a leitura acima é visual. `[não consta na fonte]` os valores exatos, o raio de canto, o padding e os estados (hover, disabled).

**Descrição idêntica nos dois grupos.** Primários e secundários carregam exatamente a mesma legenda: `"Usados para ações positivas, CTA's principais etc"`. Isso significa que **o manual não dá regra de quando usar um e quando usar o outro** — o único critério inferível é contraste sobre o fundo, e mesmo esse é inferência de quem lê, não instrução do documento. Na prática, quem for produzir peça nova tem que decidir sozinho, e vai decidir diferente do próximo.

# Selos — copy verbatim reutilizável

Três selos com ícone de linha (caminhão com check, roseta com check, escudo com check), título em caixa alta e subtítulo. Esta copy é o ativo mais diretamente reaproveitável da prancha:

| Selo | Título | Subtítulo |
|---|---|---|
| Envio | `"ENVIO GRATUITO"` | `"Frete Grátis Acima de R$89,90"` |
| Parcelamento | `"PROMO DE PARCELAMENTO"` | `"Parcelamos em até 12x no cartão de crédito. Ou até 4x no pix"` |
| Segurança | `"COMPRA SEGURA"` | `"Ambiente seguro para pagamentos."` |

O bloco na prancha se chama `Icones`, sem acento.

**Atenção ao conflito de promessa.** O selo do manual promete `"Frete Grátis Acima de R$89,90"`. A barra de confiança que roda em 12 e-mails da mesma implementação diz outra coisa: `"Frete calculado no checkout. Sem surpresa no final, como tem que ser."` — cálculo no checkout, sem menção a frete grátis. As duas promessas convivem no mesmo arquivo Figma e não são a mesma promessa. Resolver com o cliente antes de reusar qualquer uma das duas.

# A paleta declarada e o sistema real não batem

Este é o achado estrutural da prancha, e ele vale mais que os dois defeitos isolados:

- **Nenhum dos quatro botões usa o azul declarado.** O sistema de botões inteiro é preto, branco, cinza-escuro e cinza-claro. Se `#0018FF` fosse mesmo cor primária, seria estranho que a cor primária não aparecesse no componente mais importante do e-mail.
- **A paleta real de operação tem quatro valores neutros**, não uma cor de marca: preto, branco, `#323232` e `#DDDDDD`. É exatamente o que os botões usam.
- **A hipótese mais econômica** é que a marca opera em preto e branco e que a linha `Azul / #0018FF` é resíduo — o círculo preto seria o valor verdadeiro e o rótulo o errado. **Mas isso é hipótese, não é o que a fonte diz.** A fonte diz "Azul" e mostra preto, e a nota registra as duas coisas.
- **Consequência prática:** para qualquer peça nova nesta marca, o sistema seguro é o neutro de quatro valores. Introduzir azul é decisão nova, não aplicação de manual.

# Como usar esta nota

1. Para gerar peça: use preto, `#FFFFFF`, `#323232`, `#DDDDDD`. NanumMyeongjo em título, Montserrat em corpo, ambas Regular.
2. Para escolher botão: `[não consta na fonte]` — o manual não distingue primário de secundário. Decida por contraste e registre a decisão, porque o manual não vai arbitrar.
3. Para reusar a copy dos selos: transcreva verbatim, mas confira antes se a regra de frete grátis de R$89,90 ainda vale, por causa do conflito com a barra de confiança.
4. Para alimentar IA: nunca cole a paleta crua desta prancha. Cole a tabela corrigida desta nota.

# O que este material não prova

1. **É uma implementação, não uma amostra.** Este é o manual de **um** cliente, a Ride Nation, numa entrega da Convertfy. Nada aqui demonstra que o padrão de manual da casa seja este, nem que os mesmos defeitos apareçam em outros clientes.
2. **Não há um único número anexado.** Nem teste de contraste, nem acessibilidade medida, nem A/B de cor de botão, nem taxa de clique por variante. Não há evidência de que preto converta mais que azul nesta marca, nem o contrário.
3. **Esta nota é padrão de execução, não medição.** Ela serve para reproduzir e corrigir o artefato — não para sustentar afirmação de performance sobre cor, fonte ou botão.
