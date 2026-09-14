---
tipo: eixo
eixo: momento
valor: abertura
procedencia: inferida
status: aprovada
---

> Derivado por código de `flow_type` + `email_number` (`momentoDoEmail` em curador-vault.ts). Filtro do passo 5, não eixo de ranking; não é lido pelo LLM. Mudou o vocabulário, muda o mapa no mesmo commit.

# Abertura

Primeiro toque de qualquer flow que não seja o welcome — o equivalente
genérico de `welcome-1` para carrinho abandonado, browse abandonment, pós-compra
e outros: o momento em que a peça assume que é a primeira vez que a pessoa vê
aquele gatilho específico, sem histórico de e-mails anteriores do mesmo flow
para se apoiar.

# Como usar na seleção

Uma variante com `momento: [abertura]` não pode pressupor que a pessoa já viu
argumento anterior do mesmo flow — precisa se sustentar sozinha, com contexto
completo do que disparou o e-mail. Não confundir com `welcome-1`: aquele
valor é específico do flow de boas-vindas e carrega a doutrina própria dele
(entrega de incentivo, troca de motivo); `abertura` é o mesmo papel estrutural
em qualquer outro flow.

# Procedência

Esta distinção foi inferida, não extraída de doutrina existente do vault.
Utilizável, mas ainda não validada por quem opera as lojas.
