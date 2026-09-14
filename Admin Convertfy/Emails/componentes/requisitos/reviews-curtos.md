---
tipo: requisito
familia: prova-social
classe: reviews
fonte_resolucao: reviews_bank
default_quando_desconhecido: false
valor: reviews-curtos
status: aprovada
procedencia: inventario
---

# O que é

Existem reviews de clientes curtos — depoimentos de uma frase, não
parágrafo — que caibam numa faixa de largura ou altura estreita sem
transbordar.

É o oposto de [[reviews-longos]], e as duas nunca convivem na mesma
peça: um acervo de review que só tem depoimento de uma linha não serve
`review 6`/`review 8`, e um acervo que só tem depoimento de parágrafo
não serve `review 5`/`review 7`. É por isso que a restrição elimina em
vez de degradar — não há meio-termo de review que sirva as duas
variantes ao mesmo tempo.

# Por que é eliminatório e não preferência

Nas duas variantes o texto ocupa um espaço fixo e estreito ao lado ou
sobre a foto. Com review longo, o texto não fica só mais denso — ele
estoura o espaço que a variante reservou para ele, cortando frase ou
invadindo a foto.

Da prosa do inventário, verbatim (`review 5`): *"Depoimentos longos
demais — a altura fixa de 346px corta o texto."*

Da prosa do inventário, verbatim (`review 7`): *"Depoimento longo — o
padding assimétrico deixa só 245px de largura útil."*

# Como se resolve
Depende do banco de reviews expor metadados (tamanho, foto, credencial).
Fora do escopo até lá: **não elimina**. Quando o banco expuser, o resolvedor
consulta `reviews_bank` da loja.