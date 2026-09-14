---
tipo: eixo
eixo: momento
valor: browse-abandonment
procedencia: doutrina
status: aprovada
---

> Derivado por código de `flow_type` + `email_number` (`momentoDoEmail` em curador-vault.ts). Filtro do passo 5, não eixo de ranking; não é lido pelo LLM. Mudou o vocabulário, muda o mapa no mesmo commit.

# Browse abandonment

A pessoa visitou produto ou categoria e saiu sem adicionar ao carrinho. É o
gatilho mais fraco dos três de recuperação comportamental (o outro é
`carrinho-abandonado`, mais adiante `checkout-abandonado`): existe interesse
demonstrado, mas nenhuma intenção de compra declarada — a variante não pode
assumir que a pessoa já decidiu o item.

# Onde aparece na doutrina

Escopo explícito das restrições cross-flow em
[[cada-alegacao-e-uma-promessa-operacional]] e
[[posicao-muda-o-efeito-do-dispositivo]] — ambas se aplicam também a este
flow, não só ao welcome onde foram observadas.

# Como usar na seleção

Uma variante com `momento: [browse-abandonment]` reapresenta o produto visto
(ou a categoria) com contexto — por que esse item, o que outros compradores
acharam — em vez de pedir fechamento direto como faria um carrinho
abandonado. O tom é convite a voltar a olhar, não resgate de compra
interrompida.
