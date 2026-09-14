---
tipo: requisito
familia: prova-social
valor: selo-compra-verificada
verificavel_hoje: false
status: aprovada
procedencia: inventario
---

# O que é

A loja ou a plataforma de reviews tem selo real de "compra verificada"
associado aos depoimentos — não é decoração aplicada pela IA.

# Por que é eliminatório e não preferência

O selo é o mecanismo central da variante, não um detalhe visual a mais.
Sem ele o mecanismo inteiro — a promessa de que aquele review vem de
uma compra real — fica vazio, porque não existe outro elemento na
variante que carregue essa promessa.

Da prosa do inventário, verbatim (`review 7`): *"Sem selo de compra
verificada — o mecanismo central fica vazio."*

# Como o agente verifica

**Não verifica automaticamente hoje.** Nenhum campo de `client_stores`
responde a esta pergunta. Ver [[_parametros-da-loja]].
