---
tipo: lacuna
sobre: conteudo
descoberta_em: 2026-08-31
status: aberta
---

# O que falta

[[reviews-3a-depoimento-longo-monoespacado]] e
[[reviews-3b-depoimento-longo-monoespacado]] são a mesma variante gravada
duas vezes no banco: os sete campos de prosa, todos os eixos (`momento`,
`objecao`, `registro`, `paleta`, `papel_na_peca`), `exige`, `product_slots`
e `peso` são idênticos byte a byte entre as duas notas — só `variant_id`
(`7dafa6ca-...` vs. `cff6c8d8-...`) e o `slug` distinguem uma da outra. As
duas estão `ativa: true`.

# Por que importa

O protocolo de seleção sorteia/rankeia entre candidatas de uma seção; uma
peça duplicada no banco entra na lista duas vezes com `variant_id`
diferentes, então **dobra a chance estatística de ser a escolhida** frente
a qualquer outra variante `reviews` que só existe uma vez. Isso não é um
efeito desejado de nenhum critério de ranking — é um artefato de cadastro
que distorce a distribuição de escolhas sem que ninguém tenha decidido
"essa variante deve pesar o dobro".

# O que se perde hoje

Nas seis outras variantes de `reviews` (`reviews-1` a `reviews-8`, exceto a
dupla), a chance relativa de aparecer cai porque a dupla ocupa duas vagas
com um conteúdo só. Se um dia a variante for revisada ou corrigida, há risco
concreto de só uma das duas cópias ser atualizada — e a divergência que
nasceria daí seria silenciosa, porque nada no vault ou no validador aponta
hoje que as duas são a mesma peça.

# Fora do escopo desta entrega

Decidir qual `variant_id` sobrevive e desativar/remover o outro no banco —
mexe em dado vivo de produção, fora do que esta camada de vault se propõe a
fazer. Registrado aqui para a decisão não se perder.
