---
tipo: lacuna
sobre: codigo
secao: geral
descoberta_em: 2026-09-09
status: aberta
---

Três aprendizados de `escopo: cross-flow` carregam `serve_a:` só com toques
do welcome, e o filtro que vai ler `serve_a` ainda não tem regra para o caso
em que o flow corrente não aparece na lista — quando os seis flows novos
forem promovidos, esses aprendizados deixam de servir a toque nenhum deles
sem que ninguém tenha decidido isso.

# O que falta

Uma convenção, no código do Estruturador (briefing de reorganização, seção
4.2), para `serve_a` em aprendizado cross-flow: o que fazer quando a lista
tem slugs de um flow e o e-mail em geração é de outro. Duas saídas
possíveis, e a escolha muda o que os agentes recebem:

- **Tratar como `todos` para flows sem slug na lista.** A nota serve a todo
  toque de qualquer flow em `aplica_a` que não tenha toque nomeado — perde a
  precisão do welcome, mantém a cobertura.
- **Exigir slug por flow.** A nota só serve aos toques nomeados; para os
  flows novos, alguém precisa acrescentar `abandoned_cart-3`,
  `browse_abandonment-1`… à lista, com a mesma leitura toque a toque que
  T5 fez para o welcome.

Os três afetados hoje, com `aplica_a` que cobre mais de um flow:
[[remocao-de-risco-escala-com-o-ticket]] (`serve_a` só welcome-1/2/3/6),
[[quebra-de-formato-atravessa-a-cegueira]] (só welcome-8),
[[posicao-muda-o-efeito-do-dispositivo]] (só welcome-1 a 5 — e a evidência da
própria nota inclui `abandoned_cart`: "FAQ defensivo no 1º toque, movido
para o 3º").

# Por que importa

`serve_a` foi criado (T5) para cortar os 17,6k tokens de aprendizados que
entram inteiros em toda chamada do Estruturador. A regra de bolso que o
preencheu foi "os toques em que a nota muda a decisão" — lida contra a
`_progressao` do welcome, porque só o welcome tem progressão. Para os
outros seis flows não há progressão observada (T8 não cria
`_progressao.md` sem referência), então a mesma leitura não tem contra o que
ser feita. Sem convenção, o comportamento na promoção é o que o código
fizer por acaso: ou serve tudo, ou serve nada.

# O que se perde hoje

Nada: só o welcome roda no pipeline, e para ele `serve_a` está completo e
revisado. A perda começa na primeira promoção de intenção fora do welcome —
e é silenciosa, porque um aprendizado que deixa de entrar não gera erro,
só uma peça pior. Decidir antes de promover, e registrar a decisão no
briefing (`.tools/BRIEFING-emails-reorganizacao.md`, seção 4.2).
