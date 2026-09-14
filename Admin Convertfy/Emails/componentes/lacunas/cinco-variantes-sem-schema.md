---
tipo: lacuna
sobre: cadastro
descoberta_em: 2026-08-31
status: aberta
---

# O que falta

Cinco variantes têm `schema_campos: 0` no inventário: [[body-6-skin-minimalism-101]],
[[body-7-faq]], [[body-8-cards-vidro]], [[body-9-key-features-pilulas]] e
[[footer-4-dark-mega-menu]]. `schema_campos` é a contagem de campos que o
banco declara para a copy do n8n endereçar dentro do bloco (título,
subtítulo, CTA, etc.) — zero significa que não existe endereço nenhum para
a copy escrever.

# Por que importa

O agente de Copy (#5 do pipeline, via n8n) recebe blocos com slots vazios e
precisa saber *onde* escrever — é o schema que dá esse endereço. Sem
`schema_campos`, não há target: mesmo que o Curador escolhesse uma dessas
cinco variantes, o passo seguinte do pipeline não tem para onde mandar a
copy gerada. `body-6`, `body-7`, `body-8` e `body-9` já são o mesmo grupo
descrito em [[body-quatro-variantes-sem-julgamento]] — nelas, ausência de
schema é só mais um sintoma da mesma falta total de julgamento (todos os
sete campos de prosa também vazios). `footer-4-dark-mega-menu` é o caso
grave e distinto: está `ativa: true`, e as cinco seções de prosa relevantes
(`descricao_curta`, `descricao_detalhada`, `quando_usar`, `quando_nao_usar`,
`copy_ia`) estão **todas preenchidas** com julgamento completo — a nota
explica quando usar um footer de 6-7 destinos com mega-menu escuro, que
labels usar, tudo. E mesmo assim `schema_campos: 0` a deixa não-preenchível
pelo pipeline: o julgamento existe, o endereço para a copy não.

# O que se perde hoje

Para as quatro `body`, a lacuna de schema é redundante com a de julgamento —
tratada em `body-quatro-variantes-sem-julgamento`. Para `footer-4`, é uma
lacuna isolada e mais cara: é a única das quatro variantes de footer com
mega-menu (6-7 destinos), a única opção do catálogo para lojas com
catálogo ramificado — e está tecnicamente inutilizável pelo pipeline apesar
de aprovada e julgada.

# Fora do escopo desta entrega

Definir e gravar o schema de campos de `footer-4-dark-mega-menu` (e das
quatro `body`) no banco — trabalho de schema/backend sobre `admin-convertfy`,
fora do que este vault resolve.
