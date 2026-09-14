---
tipo: lacuna
sobre: doutrina
descoberta_em: 2026-08-31
status: observacao
---

# O que falta

`aprendizados/_global/titulos-precisam-carregar-o-argumento.md` declara, na
sua seção "Regra derivada": *"Vale para qualquer bloco de lista, em
qualquer flow."* — uma afirmação explícita de escopo cross-flow, sem
restrição. Mas o frontmatter da nota não tem o campo `aplica_a` nenhum. As
outras notas de `aprendizados/_global/` (por exemplo
`cada-alegacao-e-uma-promessa-operacional.md`,
`posicao-muda-o-efeito-do-dispositivo.md`) têm `aplica_a: [welcome,
abandoned_cart, browse_abandonment, post_purchase]` listando os flows
cobertos — esta é a única do grupo sem o campo, apesar de o corpo afirmar
um escopo mais amplo que qualquer lista que as outras quatro declaram.

# Por que importa

`aplica_a` é o campo que um consumidor automatizado (ou um agente lendo só
frontmatter, sem abrir o corpo inteiro) usaria para saber se um
aprendizado se aplica ao flow que está montando. Quando o campo falta, a
única forma de saber o escopo real é ler a prosa inteira — o que quebra a
premissa de que o frontmatter é suficiente para filtrar. Aqui o corpo diz
*mais* que qualquer `aplica_a` das notas irmãs diria (não é um subconjunto
de flows, é "qualquer flow") — então a ausência do campo não é
neutra: ela esconde a afirmação mais ampla de escopo do grupo inteiro.

# O que se perde hoje

Um consumidor que filtre `aprendizados/_global/` por `aplica_a` contendo o
flow que está montando simplesmente não encontra
`titulos-precisam-carregar-o-argumento` — porque ela não tem o campo — mesmo
sendo, pelo próprio corpo, a doutrina mais universalmente aplicável do
grupo. É o oposto do efeito normal de um campo faltando: aqui a nota mais
genérica é a que fica invisível a um filtro por frontmatter.

# Fora do escopo desta entrega

Esta é doutrina existente em `aprendizados/`, anterior a este projeto —
não nasceu da execução das 17 tasks e não deve ser corrigida por nós.
Nenhuma alteração foi feita em `aprendizados/`, `intencoes/` ou
`estruturas/`; esta nota registra a divergência como observação de
manutenção do vault, para quem for revisar `aprendizados/_global/` decidir
se adiciona `aplica_a: [cross-flow]` (ou equivalente) à nota original.
