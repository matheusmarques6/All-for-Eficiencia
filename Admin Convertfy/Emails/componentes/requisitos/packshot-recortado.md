---
tipo: requisito
familia: ativo-visual
valor: packshot-recortado
verificavel_hoje: false
status: aprovada
procedencia: inferida
---

# O que é

Existe imagem do produto já recortada — fundo removido — pronta para
compor sobre fundo branco ou colorido definido pelo layout.

# Por que é eliminatório e não preferência

Variantes de grade e de card montam a composição inteira em torno do
recorte: sombra projetada própria, ângulo, sobreposição de elementos ao
redor. Sem o recorte pronto, não há o que compor — colar uma foto com o
fundo original faz o produto carregar um segundo fundo por baixo do
fundo do layout, o que quebra a montagem visualmente.

O inventário não traz uma frase de "Quando NÃO usar" declarando
diretamente a ausência de packshot recortado como motivo de exclusão —
as menções a "packshot recortado" aparecem como especificação de
composição (design system), não como cláusula de eliminação. A regra
aqui vem da mecânica das variantes que dependem dele.

# Como o agente verifica

**Não verifica automaticamente hoje.** Nenhum campo de `client_stores`
responde a esta pergunta. Ver [[_parametros-da-loja]].

# Procedência

Este requisito foi inferido, não extraído de citação do inventário nem de
doutrina do vault. Utilizável, mas ainda não validado por quem opera as
lojas.

# Por que não aparece em nenhum `exige`

Este requisito tem `procedencia: inferida` — o inventário traz apenas a
condição positiva de uso, sem nenhuma cláusula de "Quando NÃO usar" ligando a
ausência do ativo a uma falha estrutural da peça.

Chegou a ser aplicado como `exige` numa variante e foi retirado na revisão:
sem citação de impossibilidade, o requisito filtra por preferência, e um
filtro por preferência descarta variante boa.

Permanece na lista porque a lista é o contrato do perfil de ativos da loja,
não o índice do que as variantes referenciam. Se aparecer citação de
impossibilidade no inventário, ele volta a ser candidato a `exige`.
