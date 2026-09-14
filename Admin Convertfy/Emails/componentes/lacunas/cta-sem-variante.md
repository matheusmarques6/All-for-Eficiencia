---
tipo: lacuna
sobre: codigo
descoberta_em: 2026-08-31
status: aberta
---

# O que falta

O mesmo buraco de `header-sem-variante`, na seção `cta`: zero das 44
variantes pertencem a ela. `variantes/cta/` não existe; a categoria só
aparece como stub em [[_cta]].

# Por que importa

Duas estruturas de referência do welcome pedem `cta` explicitamente no
`secoes:` do frontmatter: `avelmore-inspecao-antecipada` (toque 1,
`secoes: [header, hero, body, body, products, cta, reviews, footer]`) e
`avelmore-prova-social-cirurgica` (toque 4,
`secoes: [header, hero, body, reviews, cta, footer]`). Isso não é uma
seção hipotética — é uma peça que duas estruturas aprovadas do vault
declaram como parte da montagem, e o catálogo não tem nenhuma candidata
para preenchê-la. É uma das causas verificadas do achado
[[estruturas-de-welcome-sem-variantes]]: a ausência de `cta` deixa as duas
estruturas **impossíveis de montar por completo** com o catálogo atual,
mesmo que todas as outras seções tivessem candidata perfeita.

# O que se perde hoje

Nas duas estruturas de welcome que pedem `cta`, essa seção específica não
tem como vir de uma variante julgada — cai no template global, do mesmo
jeito silencioso descrito em `header-sem-variante`. Como as duas estruturas
inteiras já falham por outras causas (ver [[estruturas-de-welcome-sem-variantes]]),
esta lacuna soma-se às demais em vez de ser a única barreira, mas é a mais
fácil de apontar: não existe candidata nenhuma, para nenhuma loja.

# Fora do escopo desta entrega

Desenhar variantes de `cta` — decidir se elas devem existir como blocos
próprios ou se `cta` deveria deixar de ser uma seção pedível pelas
estruturas. Qualquer uma das duas é decisão de conteúdo/produto, não desta
entrega.
