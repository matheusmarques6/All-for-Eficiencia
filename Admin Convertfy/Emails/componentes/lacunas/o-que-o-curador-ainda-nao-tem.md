---
tipo: lacuna
sobre: codigo
descoberta_em: 2026-08-31
status: aberta
---

> **Nota de correção (rodada de correção 1).** Esta nota substitui
> `curador-nao-recebe-o-julgamento`, que afirmava que o Curador recebia
> apenas cinco campos por candidata (`variant_id`, `name`, `description`,
> `mood`, `density`) e que todo o julgamento — `when_use`, `when_not_use`,
> `copy_guidance`, `design_system`, `photo_direction` — nunca chegava ao
> LLM que escolhe. **Isso estava errado.** A leitura vinha de um estado do
> código anterior ao commit `f0fcd72d feat(curador): rankeia ate 3 por
> posicao sobre o catalogo inteiro`, que removeu o pré-filtro
> determinístico, e não foi reverificada contra o HEAD atual antes da
> publicação da nota original. Era o achado central do projeto — a
> justificativa por trás de esta camada de julgamento existir fora do
> banco — e estava apontando para um mecanismo que já não existe. Uma
> camada que existe para registrar o que é verdade não pode apagar o
> próprio erro; o registro fica aqui.

# O que falta

O Curador de hoje **já lê o julgamento**. Em
`src/lib/agents/architect/component-assembler.service.ts:664-671` o
catálogo enviado ao LLM é montado com `when_use`, `when_not_use`,
`product_slots`, `copy_guidance` (orientação de copy) e `long_description`
(notas de implementação) — não os cinco campos categóricos que a nota
anterior descrevia. O prompt trata esses campos como critério explícito,
não decorativo:

- *"Respeite quando_nao_usar: se o contexto do email casa com um 'quando
  NÃO usar', a variante está fora, não em último lugar."* — `when_not_use`
  funciona como veto, não como desempate.
- *"Use orientacao_copy como sinal de viabilidade: bloco que exige dado que
  a loja não tem (campo de cupom sem oferta no contexto) fica fora."*
- *"Produtos: cruze product_slots com `<top_products>`. NUNCA indique
  variante que exige mais produtos do que a loja tem cadastrado. Produto
  sem LINK não sustenta slot que precisa levar a uma página de
  produto."*

O prompt também recebe `<perfil_marca>`, `<objecoes>`, `<vocabulario>`,
`<intencao>`, `<decisao_do_estruturador>`, `<memoria>` e `<top_products>` —
o pré-filtro determinístico por `niche_affinity`/`positioning`/`mood` que a
nota anterior descrevia saiu no mesmo commit (comentário em
`component-assembler.service.ts:95-98`: *"ele decidia quem o LLM podia ver
a partir de três campos categóricos, antes de qualquer leitura de marca.
Agora o Curador recebe o catálogo INTEIRO — no system prompt, para ser
cacheável — e é ele quem corta"*).

O que o Curador **não** tem, verificado contra o mesmo trecho do código:

1. **Pré-requisitos de ativo da loja contra os quais eliminar.** O
   catálogo enviado ao Curador não inclui `exige` — os 52 requisitos desta
   camada (`requisitos/*.md`, ex.: `cupom-ativo`, `ugc-autorizado`,
   `estoque-integrado`) não são cruzados automaticamente contra o que a
   loja de fato tem.
2. **Orçamento de composição** (`peso`) — nada no catálogo enviado impede
   o Curador de montar uma peça de 6.000px somando `altura_px` de cada
   bloco escolhido.
3. **Restrições de convivência** entre blocos da mesma peça — o campo
   `convivencia:` das variantes não entra no prompt.
4. **Perfil de ativos da loja** — o que tornaria (1) verificável de forma
   automatizada não existe em `client_stores`: não há coluna ou tabela que
   diga "esta loja tem cupom ativo / UGC autorizado / estoque integrado".
   Sem esse perfil, checar `exige` contra a loja real não tem como rodar
   fora de inferência do LLM a partir do contexto de texto.

# Por que importa

Os itens 1 e 4 se sustentam um no outro: mesmo que o catálogo passasse a
incluir `exige` no prompt, não há hoje uma fonte estruturada do lado da
loja para cruzar contra — "esta loja tem cupom ativo?" continua sendo
julgamento implícito dentro do LLM, extraído do contexto de texto que o
prompt já carrega (`<perfil_marca>`, briefing), em vez de um filtro
verificável, testável e auditável fora do modelo. Os itens 2 e 3
(orçamento e convivência) são diferentes: são regras de composição sobre o
conjunto de blocos escolhidos, não sobre uma variante isolada, e hoje não
têm representação nenhuma no prompt do Curador nem em nenhum outro passo
do Montador.

# O que se perde hoje

Vale registrar com honestidade: o Curador atual é bem mais capaz do que a
versão que este projeto assumiu no início. Ele já lê `when_use`,
`when_not_use` e `copy_guidance` como critério de corte, já cruza marca,
objeção, vocabulário e intenção do flow, e já verifica `product_slots`
contra o catálogo real da loja. O que falta é mais estreito do que a nota
original descrevia: não é "o julgamento não chega ao LLM" — é que quatro
sinais específicos (requisitos de ativo, orçamento de peso, convivência,
perfil de ativos da loja) não fazem parte do que ele recebe ou pode
verificar hoje. O risco concreto que sobra é montagem sem checagem de
ativo real (a loja pode não ter cupom e o Curador escolher uma variante
que o exige, confiando só no que o contexto de texto sugere) e composição
sem orçamento de altura ou de convivência entre blocos.

# Fora do escopo desta entrega

Nada dos quatro itens foi implementado no pipeline por este projeto:
cruzar `exige` contra perfil de loja, adicionar orçamento de `peso` ao
prompt do Curador, expor `convivencia` no catálogo enviado, ou desenhar a
tabela/coluna de perfil de ativos em `client_stores`. Ficam registrados
aqui para não sumir.
