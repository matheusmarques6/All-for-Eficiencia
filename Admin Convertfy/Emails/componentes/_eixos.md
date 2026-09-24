---
tipo: indice
status: aprovada
---

O vocabulário controlado do sistema, inteiro, em uma leitura. Cinco eixos, 56
valores: `momento` 21 · `objecao` 11 · `paleta` 8 · `registro` 10 ·
`papel-na-peca` 6. Uma linha por valor, com o link para a nota que o define.

Serve para achar a nota certa a partir do slug que aparece no frontmatter de uma
variante ou no [[_catalogo]], sem abrir 56 arquivos. **Não substitui a nota**:
cada uma traz "onde aparece na doutrina" e "como usar na seleção", que é o que
os passos 5 e 7 do [[_protocolo-de-selecao]] de fato consomem.

Lembretes do contrato: valores são **slugs simples, não wikilinks**, no
frontmatter — `momento: [consideracao]`, nunca `[[consideracao]]`. Lista vazia
(`momento: []`) significa "não discrimina", nunca "não serve a nenhum". Todo
valor usado tem que ter nota aqui; valor sem nota é bug.

# `momento` — quando a peça é disparada (21)

Filtro, não ranking: consumido nos passos 4-6 do protocolo, via `momento` e
`momento_vetado`.

| Valor | O que é |
|---|---|
| [[abertura]] | Primeiro toque de qualquer flow que não seja o welcome — a peça assume que é a primeira vez que a pessoa vê aquele gatilho, sem histórico do mesmo flow. |
| [[browse-abandonment]] | Visitou produto ou categoria e saiu sem adicionar ao carrinho — o mais fraco dos três gatilhos comportamentais: interesse demonstrado, intenção não declarada. |
| [[campanha-promocional]] | Disparo comercial pontual, para vender agora em torno de uma oferta com prazo; sem cadência esperada, ao contrário de `sale-recorrente`. |
| [[carrinho-abandonado]] | Adicionou ao carrinho e saiu — já há intenção declarada sobre um item; o e-mail não reapresenta catálogo, resolve o que travou. |
| [[catalogo-mais-vendidos]] | Peça organizada por curadoria de popularidade, não por oferta nem por evento: serve quem decide o que comprar e quem quer prova indireta de demanda. |
| [[checkout-abandonado]] | Mais fundo que `carrinho-abandonado`: iniciou o checkout e saiu. A objeção provável não é valor, é fricção — pagamento, frete revelado tarde. |
| [[consideracao]] | Meio de funil: assinante ou lead qualificado, sem gatilho comportamental e sem decisão — cultivado até um gatilho aparecer. |
| [[cross-sell]] | Produto complementar ao que já foi comprado ou desejado; pressupõe relação estabelecida com um item específico. |
| [[gift-card]] | Peça centrada em cartão-presente — promoção autônoma (comprar para dar) ou lembrete de saldo (usar o que já se tem), com objeções opostas. |
| [[lancamento]] | Produto ou coleção nova: o trabalho é apresentação, não recuperação — ainda não há dúvida acumulada porque ninguém experimentou. |
| [[newsletter]] | Envio editorial de cadência regular; o contrato com o assinante é "recebo isso periodicamente", não "isso responde a algo que eu fiz". |
| [[nutricao-de-conteudo]] | Sem pedido comercial direto: mantém a lista quente entre momentos comerciais; pode não ter CTA de compra dominante. |
| [[pos-compra]] | Já comprou. O trabalho muda de convencer para reter, ensinar ou expandir, sem parecer que a marca só queria a venda. |
| [[queima-de-estoque]] | Liquidação por motivo operacional (fim de coleção, excesso, descontinuação); desconto mais agressivo e escassez genuína. |
| [[reengajamento]] | Está na lista mas parou de abrir — a objeção implícita não é sobre o produto, é "por que voltar a prestar atenção nesta marca?". |
| [[sale-recorrente]] | Desconto em cadência conhecida e própria da marca (sale mensal, sexta de promoção), que o assinante frequente já espera. |
| [[sazonal-data-comemorativa]] | Amarrado a uma data do calendário; o gancho temático é parte do argumento, não só pretexto para o desconto. |
| [[transacional]] | Disparado por evento de sistema (pedido, envio, entrega, senha): função informativa; persuasão só em espaço residual. |
| [[componentes/eixos/momento/welcome-1\|welcome-1]] | Primeiro toque do welcome: pico de atenção, veio pelo incentivo, não conhece a marca. Cumpre o contrato do opt-in e troca o motivo da compra. |
| [[welcome-meio]] | Faixa central do welcome — já recebeu a tese e não agiu: varredura de objeções, mecanismo para o cético, troca de voz para prova social (toques 2-4). |
| [[welcome-tardio]] | Reta final do welcome, quando o argumento se esgota e o trabalho vira sobre tempo (toques 5-8). |

> **Colisão de nome.** `componentes/eixos/momento/welcome-1.md` (o valor de eixo)
> e `intencoes/welcome/welcome-1.md` (a intenção do toque 1) têm o mesmo nome de
> arquivo, e nenhum dos dois pode ser renomeado — o caminho é o tipo da nota.
> Desde 16/09 os links dos dois lados são qualificados por caminho:
> `[[componentes/eixos/momento/welcome-1|welcome-1]]` para o eixo,
> `[[intencoes/welcome/welcome-1|welcome-1]]` para a intenção. Ver
> [[wikilink-flow-ambiguo-com-seis-flows]].

# `objecao` — o que a peça precisa derrubar (11)

Primeiro eixo do ranking (passo 7), porque é o eixo em que o vault já pensa.
Overlap zero não é segunda opção — é lacuna.

| Valor | O que é |
|---|---|
| [[adesao-social]] | "Sou só eu que estou considerando isso?" O antídoto não é a marca falar de novo: é ver que outras pessoas já decidiram. |
| [[amplitude-de-catalogo]] | "Só tem isso, ou tem mais coisa pra eu ver?" Dúvida sobre a profundidade da loja, não sobre o produto em mãos. |
| [[composicao-formulacao]] | "Como isso é feito? Como isso se sustenta?" A objeção do cético: não basta alegar qualidade, é preciso mostrar mecanismo. |
| [[confianca-no-canal]] | "Por que comprar de VOCÊS?" Não é sobre produto nem preço — é sobre a loja contra a experiência genérica da categoria. |
| [[disponibilidade-urgencia]] | "Por que agora? Ainda dá tempo? Eu perdi?" A única objeção que muda de forma conforme a posição no flow, e não some — se transforma. |
| [[escolha-variedade]] | "Tem a opção certa pra mim, entre tantas?" A indecisão entre cor, tamanho, formulação ou kit paralisa antes da objeção de preço. |
| [[pertencimento]] | "Essa marca é para gente como eu?" Identidade, não quantidade — diferente de `adesao-social`. |
| [[preco-valor]] | "Vale o que custa?" Objeção econômica, não de qualidade: pede comparação, decomposição de custo ou razão para o preço fazer sentido. |
| [[qualidade-eficacia]] | "Isso presta? Faz o que promete?" A objeção dominante de quem não conhece a marca, e por isso a primeira a ser atacada. |
| [[suporte-duvida]] | "Se der problema, tem alguém do outro lado?" É sobre o que acontece depois da compra. |
| [[uso-aprendizado]] | "Eu vou saber usar isso direito?" Objeção de execução, não de decisão — típica de quem já converteu ou está no limite. |

# `paleta` — a decisão de cor (8)

Terceiro eixo do ranking, e o mais fraco: duas variantes com a mesma objeção e
paletas diferentes estão as duas certas; o design system diz como adaptar a cor.

O eixo resolve a cor **dentro** de uma variante. A cor **entre** as variantes já
escolhidas — ritmo de faixas claro/escuro, onde o acento entra, qual CTA em qual
fundo — não tem eixo e é o que o plano de cor propõe cobrir, rodando depois do
protocolo: [[plano-de-cor-entradas-e-paleta-da-loja]] (entradas e validação),
[[plano-de-cor-tokens-e-eixo-paleta]] (a árvore que classifica a loja nos oito
valores abaixo), [[plano-de-cor-faixas-e-cta]] e
[[plano-de-cor-checagens-e-saida]]. São doutrina em `status: rascunho`, com
parte das regras marcada `[PROPOSTA]` — não mandam em nada enquanto não forem
revisadas, e não alteram a definição de nenhum valor desta tabela.

| Valor | O que é |
|---|---|
| [[cinza-neutro]] | Escala de cinzas como base, sem acento forte nem contraste extremo — a paleta mais discreta do eixo; não compete com a fotografia. |
| [[claro]] | Fundo branco ou quase branco com acento pontual; a mais segura em legibilidade e compatibilidade — o default quando nada mais é exigido. |
| [[com-acento-definido]] | Base neutra com uma cor de acento única, reservada ao que pede atenção (CTA, título, selo) — a mais fácil de garantir CTA dominante. |
| [[creme]] | Base quente e suave (bege, off-white, marfim): calor e naturalidade onde `claro` comunicaria neutralidade técnica. |
| [[escuro-saturado]] | Fundo escuro com acento vibrante em protagonismo — intensidade e energia; casa com `bold-alto-contraste` e `volume-impulso`. |
| [[full-dark]] | Fundo escuro dominante com pouquíssimo acento: sofisticação pela ausência de cor. A paleta natural de `registro: luxo`. |
| [[monocromatico]] | Uma única cor de base em variações de tom e saturação — tudo deriva da mesma cor, inclusive o que seria acento em outra paleta. |
| [[preto-e-branco]] | Ausência total de cor; mais radical que `full-dark` — o contraste em si é o elemento visual. |

# `registro` — o tom (10)

Segundo eixo do ranking. Forte como veto (`registro_vetado`), fraco como
ranking — três das nove heroes servem "premium", então sozinho não separa.

| Valor | O que é |
|---|---|
| [[bold-alto-contraste]] | Visualmente agressivo: cor saturada, tipografia grande e pesada, hierarquia que grita. Existe para parar o scroll, não para leitura longa. |
| [[clinico-sobrio]] | Precisão técnica: factual, dado em vez de adjetivo, sem apelo emocional. O registro natural de `composicao-formulacao`. |
| [[comercial]] | Venda direta: preço visível, CTA repetido, pouca narrativa. Não disfarça que é peça de venda. |
| [[comunidade-identitario]] | Fala para um grupo: linguagem de pertencimento, referência cultural do público, prova social de identidade e não de volume. |
| [[festivo]] | Celebração temática amarrada a uma data — sinaliza "isto é sobre a data", não "isto é uma oferta com enfeite". |
| [[luxo]] | Exclusividade e raridade antes de tudo: espaço negativo generoso, poucos elementos, quase nenhum desconto explícito. |
| [[minimalista-leve]] | Baixa densidade visual e textual — deliberadamente vazio; o vazio é a mensagem, não o pano de fundo. |
| [[popular-informal]] | Conversacional: linguagem próxima, tom de quem escreve para um amigo. Reduz a distância marca-leitor de propósito. |
| [[premium-editorial]] | Revista de alto padrão: tipografia espaçosa, fotografia grande, pouco texto por área; o argumento é sugerido pela composição. |
| [[volume-impulso]] | Compra rápida e barata: preço em destaque, muitos produtos por tela, urgência explícita — o oposto de `clinico-sobrio`. |

# `papel-na-peca` — a função do bloco dentro do e-mail (6)

Último eixo do ranking. É papel, não seção: qualquer seção pode assumir
qualquer papel dependendo de onde está na peça.

| Valor | O que é |
|---|---|
| [[abre]] | Primeira posição visível — decide se a pessoa continua rolando. Carrega o gancho: alegação central, pergunta ou contexto. |
| [[apoio]] | Secundário: reforça argumento que outro bloco já carregou. Removível sem quebrar o argumento central. |
| [[fecha]] | Última coisa lida antes da decisão: carrega o CTA dominante e, quando existe, a urgência. O papel mais sensível a exagero. |
| [[meio]] | Desenvolvimento — aprofunda o que a abertura levantou: mecanismo, prova, catálogo, comparação. Pode ser mais denso. |
| [[peca-inteira]] | O dispositivo é o e-mail inteiro, não um bloco: quebra deliberadamente o padrão abre/meio/fecha porque só funciona como unidade. |
| [[ponte]] | Transição entre dois blocos de natureza diferente, sem carregar argumento próprio. Costuma ser curto. |

# O que este índice não cobre

Os oito vocabulários do contrato tipado das intenções — 44 valores fechados sem
pasta em `eixos/` nem nota por valor; a decisão está em
[[vocabulario-do-contrato-sem-nota-de-eixo]]. Nem `requisitos/` (52 valores de
`exige`) e `convivencia/` (6 regras), que têm nota por valor nas próprias pastas.

---

Catálogo que usa estes valores: [[_catalogo]] · Como eles decidem:
[[_protocolo-de-selecao]] · Mapa do sistema: [[_INDEX]]
