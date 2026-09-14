---
tipo: requisito
familia: dado-operacional
valor: bloco-dinamico-de-carrinho
verificavel_hoje: false
status: aprovada
procedencia: inventario
---

# O que é

Existe infraestrutura — feed dinâmico ou merge tag da ESP — que injeta o
item salvo no carrinho de cada destinatário dentro do bloco, um a um.

# Por que é eliminatório e não preferência

O bloco branco da variante existe unicamente para mostrar o item salvo
daquele contato. Com um placeholder estático no lugar do dado dinâmico,
o bloco perde a razão de existir — não é uma versão mais pobre da
variante, é a variante sem o motivo dela estar ali.

Da prosa do inventário, verbatim (`offer 6`): *"Sem bloco dinâmico
funcionando. O bloco branco existe para mostrar o item salvo; com
placeholder estático ele perde a razão de ser."*

# Como o agente verifica

**Não verifica automaticamente hoje.** Nenhum campo de `client_stores`
responde a esta pergunta. Ver [[_parametros-da-loja]].
