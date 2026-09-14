---
tipo: requisito
familia: ativo-visual
classe: gate
fonte_resolucao: brand_identity
default_quando_desconhecido: false
valor: wordmark-tipografico
status: aprovada
procedencia: inferida
---

# O que é

A marca tem um wordmark que funciona bem como texto puro, em caixa
alta com tracking largo — não depende de um logotipo em imagem para ser
reconhecível.

# Por que é eliminatório e não preferência

Nesta variante o nome da marca é o maior elemento tipográfico da peça,
maior até que o wordmark em outras variantes — ele é renderizado como
texto vivo, não como imagem. Sem um wordmark que funcione
tipograficamente nesse tratamento, não há substituto: colocar um logo
em imagem no lugar quebra a lógica de texto vivo que sustenta a
variante inteira.

Da prosa do inventário, verbatim (`hero 6`, condição de uso — a
ausência é o inverso direto): *"Quando a marca tem wordmark tipográfico
que funciona em caixa alta com tracking largo."*

# Como se resolve
Resolvedor (código): `store_brand_identity` → logo/wordmark tipográfico
cadastrado como ativo. `false` → elimina.

# Procedência

Este requisito foi inferido, não extraído de citação do inventário nem de
doutrina do vault. O inventário só registra a condição positiva ("Quando
a marca tem wordmark tipográfico...") — não há cláusula de "Quando NÃO
usar" declarando a ausência de wordmark tipográfico como motivo de
exclusão. Utilizável, mas ainda não validado por quem opera as lojas.

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
