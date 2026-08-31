---
tipo: lacuna
sobre: codigo
descoberta_em: 2026-08-31
status: aberta
---

# O que falta

15 colunas existem hoje na tabela `email_component_variants` do banco
Supabase vivo (projeto `ppygkfeffknypfncsnlv`, extraídas do
`information_schema`) e **não têm migration correspondente** em
`supabase/migrations/` no repo `admin-convertfy`:

`rendered_html` · `objectives` · `tones` · `when_use` · `when_not_use` ·
`copy_guidance` · `long_description` · `product_slots` · `output_schema` ·
`html_tagged` · `tagging_status` · `tagging_meta` ·
`rendered_html_source_sha` · `design_system` · `photo_direction`

Boa parte destas são, precisamente, o julgamento que
[[o-que-o-curador-ainda-nao-tem]] descreve o Curador lendo hoje
(`when_use`, `when_not_use`, `copy_guidance`, `product_slots`,
`long_description`) — a lacuna aqui não é sobre esses campos existirem ou
não; é sobre eles existirem só no banco vivo, sem migration que os
reconstrua.

# Por que importa

Migration é o mecanismo normal pelo qual o time reconstrói o schema em um
ambiente novo (staging, branch de teste, restauração de desastre) e pelo
qual outro desenvolvedor entende *por que* uma coluna existe. Colunas
adicionadas fora desse fluxo — via Supabase Studio, script ad-hoc ou
migration aplicada e depois descartada do controle de versão — não deixam
rastro de intenção: ninguém consegue saber, olhando só o repo, se
`tagging_meta` ou `output_schema` são decisão de produto ativa ou resíduo
de um experimento abandonado. É exatamente essa incerteza que motivou os
agentes fazerem o inventário deste vault a partir do banco em vez de a
partir das migrations.

# O que se perde hoje

Reprodutibilidade. Se alguém precisar recriar o ambiente de banco do zero
(um branch de teste do Supabase, por exemplo), rodar todas as migrations em
sequência **não** produz a mesma tabela que está em produção — faltam 15
colunas, entre elas `when_use`/`when_not_use`/`copy_guidance`/`product_slots`,
que o Curador já usa como critério de corte em produção. Esta camada do
vault (`componentes/`) existe em parte para compensar esse hiato: é o
registro legível do que o banco realmente tem, enquanto o código-fonte das
migrations não conta a história completa.

# Fora do escopo desta entrega

Escrever as 15 migrations retroativas que faltam, ou decidir quais das 15
colunas são intencionais versus resíduo. Isso é trabalho de
`supabase-architect` sobre o repo `admin-convertfy`, não deste vault.
