---
tipo: lacuna
sobre: codigo
descoberta_em: 2026-08-31
status: retratada
---

# O que foi afirmado

Esta nota afirmava que 15 colunas da tabela `email_component_variants` —
`rendered_html`, `objectives`, `tones`, `when_use`, `when_not_use`,
`copy_guidance`, `long_description`, `product_slots`, `output_schema`,
`html_tagged`, `tagging_status`, `tagging_meta`,
`rendered_html_source_sha`, `design_system`, `photo_direction` — existiam
no banco vivo e **não tinham migration correspondente** em
`supabase/migrations/` no repo `admin-convertfy`.

# Por que é falso

**É falso.** As 15 colunas têm migration real e datada, todas com
`ADD COLUMN IF NOT EXISTS` e nenhum `DROP COLUMN` depois:
`20261003_component_variant_dimensions.sql` (`objectives`, `tones`,
`when_use`, `when_not_use`, `copy_guidance`, `long_description`,
`product_slots`, `output_schema`),
`20261022_component_variant_rendered_html.sql` (`rendered_html`),
`20261040_component_tagger.sql` (`html_tagged`, `tagging_status`,
`tagging_meta`), `20261056_rendered_html_source_sha.sql`
(`rendered_html_source_sha`), `20261059_variant_design_system.sql`
(`design_system`), `20261060_variant_photo_direction.sql`
(`photo_direction`). Verificado por leitura direta dos seis arquivos: cada
uma das 15 colunas aparece em exatamente um `ALTER TABLE ... ADD COLUMN IF
NOT EXISTS`, e nenhum arquivo do diretório de migrations remove qualquer
uma delas depois.

# A causa do erro

A busca original que gerou este achado procurou `when_to_use` em
`supabase/migrations/` — um nome de coluna que não existe. A coluna real
chama-se `when_use`. O nome foi inventado por analogia ao padrão de
nomenclatura, não conferido contra o schema real; a busca deu zero
resultados e isso foi lido como "a coluna não tem migration", quando na
verdade a busca é que estava malformada. As outras 14 colunas herdaram a
mesma conclusão sem checagem individual. O erro foi do orquestrador, na
etapa de levantamento do achado — não reverificado antes de ser repassado
para esta nota.

# O que não foi verificado

Esta retratação confirma que as 15 colunas nomeadas têm migration. Ela
**não** é uma comparação coluna a coluna entre o `information_schema` do
banco vivo e `supabase/migrations/` — só verificou as 15 colunas
específicas que a versão anterior citava, erradamente, como exemplo de
drift. Se existe drift real entre banco vivo e migrations nesta tabela (ou
em qualquer outra), ele não foi medido aqui. Afirmar que não há drift
nenhum repetiria o mesmo erro na direção oposta — por isso esta nota não
propõe uma lacuna substituta. Se alguém quiser essa resposta, precisa
rodar a comparação de verdade, coluna a coluna, contra o schema vivo.
