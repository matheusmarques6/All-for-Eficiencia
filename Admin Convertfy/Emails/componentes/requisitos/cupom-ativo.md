---
tipo: requisito
familia: comercial
valor: cupom-ativo
verificavel_hoje: false
status: aprovada
procedencia: inventario
---

# O que é

Existe um código de desconto válido, entregue ao contato, que a loja pode
publicar no e-mail.

# Por que é eliminatório e não preferência

As variantes que declaram este requisito são construídas em volta do
código: pílula, barra do topo, label do botão. Sem cupom os slots ficam
vazios e a peça não degrada — desmonta. Não existe versão "sem desconto"
dessas variantes.

Da prosa do inventário, verbatim (`offer 3`): *"Sem cupom. A pílula do
código é o centro da variante e não tem substituto."*

# Como o agente verifica

**Não verifica automaticamente hoje.** Nenhum campo de `client_stores`
responde a esta pergunta. Ver [[_parametros-da-loja]].
