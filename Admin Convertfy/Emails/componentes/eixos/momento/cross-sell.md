---
tipo: eixo
eixo: momento
valor: cross-sell
procedencia: inferida
status: aprovada
---

> Derivado por código de `flow_type` + `email_number` (`momentoDoEmail` em curador-vault.ts). Filtro do passo 5, não eixo de ranking; não é lido pelo LLM. Mudou o vocabulário, muda o mapa no mesmo commit.

# Cross-sell

Oferece produto complementar ao que a pessoa já comprou ou já demonstrou
interesse — não é a mesma coisa de novo, é o próximo item lógico. Pressupõe
contexto: só faz sentido depois que existe uma relação já estabelecida com um
produto específico.

# Como usar na seleção

Uma variante com `momento: [cross-sell]` deve nomear a relação entre o item
já adquirido e o sugerido — não apenas empilhar produtos. Cabe naturalmente
depois de `pos-compra`, uma vez que o trabalho de retenção e uso já foi feito;
puxar cross-sell antes disso compete com o objetivo do momento anterior.

# Procedência

Esta distinção foi inferida, não extraída de doutrina existente do vault.
Utilizável, mas ainda não validada por quem opera as lojas.
