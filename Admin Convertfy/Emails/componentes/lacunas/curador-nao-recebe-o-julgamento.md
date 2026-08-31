---
tipo: lacuna
sobre: codigo
descoberta_em: 2026-08-31
status: aberta
---

# O que falta

O passo A do Montador — o Curador, que escolhe uma variante por bloco —
recebe apenas cinco campos de cada candidata: `variant_id`, `name`,
`description`, `mood`, `density`
(`src/lib/agents/architect/component-assembler.service.ts:383-397`).

Todo o julgamento que esta camada organiza — `when_use`, `when_not_use`,
`copy_guidance`, `design_system`, `photo_direction` — existe no banco e
**nunca chega ao LLM que escolhe**.

# Por que importa

O pré-filtro determinístico
(`src/lib/agents/architect/component-deriver.ts:85-117`) pontua por
`niche_affinity` (peso 3), `positioning` (peso 2) e `mood` (peso 1).
`niche_affinity` e `positioning` estão vazios na quase totalidade das 44
variantes, então viram wildcard e o score não discrimina. O critério de
densidade é código morto: `ctx.density` nunca é setado pelo caller real.

Resultado: entre as nove heroes, a escolha é praticamente arbitrária.

# O que se perde hoje

Tudo que o [[_protocolo-de-selecao]] descreve. Enquanto esta lacuna
existir, o protocolo é executado por humano ou por agente que lê o vault —
não pelo pipeline.

# Fora do escopo desta entrega

Alterar o prompt do Curador. Registrado aqui para não sumir.
