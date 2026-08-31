---
tipo: requisito
familia: ativo-visual
valor: corredores-livres-nas-laterais
verificavel_hoje: false
status: aprovada
procedencia: inventario
---

# O que é

A foto do produto tem espaço vazio — corredor — nas laterais, sem
elemento nem textura ocupando essa área.

# Por que é eliminatório e não preferência

A variante sobrepõe rótulos de texto exatamente nesses corredores. Sem
eles, os rótulos caem sobre o produto em vez de ao lado dele, e como o
produto tem textura e detalhe, o texto sobreposto fica ilegível — não é
um problema de acabamento, é o slot de texto não ter onde existir.

Da prosa do inventário, verbatim (`produtos 2`): *"Foto sem corredores
livres nas laterais — os rótulos caem sobre o produto e nada fica
legível."*

# Como o agente verifica

**Não verifica automaticamente hoje.** Nenhum campo de `client_stores`
responde a esta pergunta. Ver [[_parametros-da-loja]].
