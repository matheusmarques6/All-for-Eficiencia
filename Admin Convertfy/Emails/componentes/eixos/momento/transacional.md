---
tipo: eixo
eixo: momento
valor: transacional
procedencia: inferida
status: aprovada
---

> Derivado por código de `flow_type` + `email_number` (`momentoDoEmail` em curador-vault.ts). Filtro do passo 5, não eixo de ranking; não é lido pelo LLM. Mudou o vocabulário, muda o mapa no mesmo commit.

# Transacional

E-mail disparado por um evento do sistema — confirmação de pedido, envio,
entrega, redefinição de senha — não por estratégia de marketing. A função
primária é informativa e a pessoa espera recebê-lo; a persuasão, quando
existe, é secundária e cabe em espaço residual (rodapé, bloco de
recomendação), nunca no corpo principal.

# Como usar na seleção

Uma variante com `momento: [transacional]` prioriza clareza da informação
central (status, número do pedido, prazo) acima de qualquer argumento de
venda. Elementos de outras objeções — cross-sell, prova social — só entram
como bloco secundário, depois que a informação transacional já foi entregue
sem ambiguidade.

# Procedência

Esta distinção foi inferida, não extraída de doutrina existente do vault.
Utilizável, mas ainda não validada por quem opera as lojas.
