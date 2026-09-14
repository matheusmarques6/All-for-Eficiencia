---
tipo: eixo
eixo: momento
valor: sale-recorrente
procedencia: inferida
status: aprovada
---

> Derivado por código de `flow_type` + `email_number` (`momentoDoEmail` em curador-vault.ts). Filtro do passo 5, não eixo de ranking; não é lido pelo LLM. Mudou o vocabulário, muda o mapa no mesmo commit.

# Sale recorrente

Evento de desconto que se repete em cadência conhecida — sale mensal,
promoção de toda sexta, aniversário de assinatura. Diferente de
`campanha-promocional` (evento único) e de `sazonal-data-comemorativa`
(amarrada a uma data do calendário geral), aqui a recorrência é própria da
marca e o assinante frequente já espera o padrão.

# Como usar na seleção

Uma variante com `momento: [sale-recorrente]` pode assumir que parte da
audiência já reconhece o formato — permite menos explicação do mecanismo da
promoção e mais foco direto na oferta atual. Cuidado com a mesma armadilha de
prazo decorativo: se a "sale" é sempre igual e sempre volta, a urgência
declarada perde força a cada repetição — ver
[[deadline-falso-queima-o-proximo]].

# Procedência

Esta distinção foi inferida, não extraída de doutrina existente do vault.
Utilizável, mas ainda não validada por quem opera as lojas.
