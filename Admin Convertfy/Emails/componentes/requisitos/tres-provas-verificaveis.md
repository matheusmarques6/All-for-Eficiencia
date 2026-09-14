---
tipo: requisito
familia: catalogo
classe: gate
fonte_resolucao: pesquisa
default_quando_desconhecido: false
valor: tres-provas-verificaveis
status: aprovada
procedencia: inventario
---

# O que é

Existem três atributos objetivos e verificáveis do produto — "0%
parabenos", "testado dermatologicamente", "3x mais concentrado" — não
adjetivos.

# Por que é eliminatório e não preferência

Os três marcadores da peça são o argumento inteiro do bloco, não um
complemento dele. Trocar prova verificável por adjetivo genérico não
enfraquece a peça — esvazia, porque o bloco não tem outro conteúdo além
desses três marcadores.

Da prosa do inventário, verbatim (`produtos 2`): *"Sem provas
verificáveis — três marcadores com adjetivo genérico (\"suave\",
\"poderoso\") esvaziam o bloco."*

# Como se resolve
Resolvedor (código, com citação): pesquisa da marca → três provas
verificáveis (números, certificações, testes) com trecho. Senão `false` → elimina.