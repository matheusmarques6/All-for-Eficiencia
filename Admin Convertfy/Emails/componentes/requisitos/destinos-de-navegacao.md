---
tipo: requisito
familia: dado-operacional
valor: destinos-de-navegacao
verificavel_hoje: false
status: aprovada
procedencia: inventario
---

# O que é

A loja tem pelo menos tantos destinos distintos e navegáveis — páginas,
coleções, categorias — quantos espaços de link a variante reserva.

# Por que é eliminatório e não preferência

Um rodapé de grid com quatro espaços de link pressupõe quatro destinos
reais e diferentes entre si. Com menos destinos que espaços, o grid não
fica só "menos completo" — fica capenga, porque a estrutura existe para
ser preenchida com destinos distintos, não para repetir o mesmo link em
várias posições.

Da prosa do inventário, verbatim (`footer 1`): *"esta variação
específica não serve para clientes com menos de 4 links úteis (grid
fica capenga; usar variante de lista horizontal simples) ou e-mails
transacionais ultra-minimalistas."*

# Como o agente verifica

**Não verifica automaticamente hoje.** Nenhum campo de `client_stores`
responde a esta pergunta. Ver [[_parametros-da-loja]].


# Como está codificado nas variantes

Este requisito não aparece em nenhum `exige:`. Nas variantes de footer ele é
codificado como `itens: { min, max }` — a quantidade de destinos é restrição
de **capacidade**, que o protocolo elimina num passo próprio, e não um ativo
que a loja tem ou não tem.

A nota permanece porque a lista de requisitos é o contrato do perfil de
ativos da loja, não apenas o índice do que as variantes referenciam.
