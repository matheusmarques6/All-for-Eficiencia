---
tipo: requisito
familia: comercial
classe: gate
fonte_resolucao: outline
default_quando_desconhecido: false
valor: duas-ofertas-simultaneas
status: aprovada
procedencia: inventario
---

# O que é

A campanha tem duas ofertas de natureza diferente rodando ao mesmo
tempo — por exemplo um desconto percentual e um combo de preço fechado —
não uma oferta com um reforço secundário do mesmo tipo.

# Por que é eliminatório e não preferência

A estrutura reserva duas caixas de peso visual igual, cada uma com sua
própria mecânica. Com uma oferta só, a segunda caixa não tem o que
carregar e vira enchimento — a peça fica visivelmente desequilibrada,
não apenas menos rica.

Da prosa do inventário, verbatim (`offer 2`): *"Uma oferta só. Com uma
caixa a estrutura fica desequilibrada e a segunda vira enchimento."* E
ainda: *"São duas ofertas simultâneas, não uma oferta e um reforço."*

# Como se resolve
Resolvedor (código): `email_outline_templates` → dois incentivos distintos
ativos no mesmo toque. `false` → elimina.