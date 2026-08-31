---
tipo: requisito
familia: comercial
valor: preference-center-na-esp
verificavel_hoje: false
status: aprovada
procedencia: inferida
---

# O que é

A ESP da loja tem uma central de preferências de e-mail publicada e
linkável — não apenas um link de unsubscribe genérico.

# Por que é eliminatório e não preferência

Rodapés que trazem "Gerenciar preferências" pressupõem uma página real
por trás desse clique. Sem central de preferências configurada na ESP,
o link do rodapé não tem destino — o footer promete uma opção que a
loja não tem como cumprir. Isso não degrada a peça: o link fica quebrado
ou tem que ser removido, o que muda a variante disponível.

O inventário não traz uma citação de "Quando NÃO usar" ligada
diretamente à ausência de central de preferências — os footers só
citam o label do link ("Gerenciar preferências") como orientação de
copy, presumindo que ele existe. A eliminação aqui vem da mecânica do
link, não de uma frase do inventário.

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
