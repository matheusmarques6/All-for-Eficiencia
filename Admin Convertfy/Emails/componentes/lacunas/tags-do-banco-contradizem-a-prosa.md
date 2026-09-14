---
tipo: lacuna
sobre: cadastro
descoberta_em: 2026-08-31
status: aberta
---

# O que falta

As tags gravadas no banco para [[hero-8-lineup-com-lembrete-de-oferta]] —
`dark_bg`, `coupon_code`, `discount_offer`, `offer_reminder`,
`urgency_copy` — descrevem um bloco de lembrete de oferta com cupom, fundo
escuro e urgência. A prosa colada da própria variante, no campo
"Orientações de copy para a IA", diz o oposto:
*"Proibições: desconto ou cupom em qualquer slot, contagem regressiva
[...]"* — e no "Design system", a paleta é `#FFFFFF`/`#000000` sobre fundo
claro, não escuro. [[hero-10-lineup-de-colecao]] — a variante de conteúdo
idêntico (ver [[hero-8-duplicata-de-hero-10]]) — não tem tag nenhuma
gravada.

# Por que importa

O vault tem uma regra explícita, seguida em toda a execução deste projeto:
nunca deduzir um valor de eixo (`objecao`, `registro`, `momento` etc.) a
partir de tag crua do banco — só a partir da prosa julgada, porque tag é
metadado de cadastro e prosa é o julgamento real da variante. Este achado é
a evidência concreta que sustenta essa regra: se alguém tivesse inferido
`objecao`/`registro` de `hero-8` a partir das tags (`coupon_code`,
`urgency_copy`, `dark_bg`), o resultado contradiria a variante inteira —
paleta clara, zero cupom, zero urgência, exatamente o oposto do que as
tags sugerem.

# O que se perde hoje

Nada se perde no vault hoje — a regra de nunca deduzir de tag já estava em
vigor antes deste achado e foi respeitada nas 44 variantes. O que esta nota
registra é a prova de que a regra era necessária, não decorativa: as tags
de `hero-8` são resíduo de um estado anterior da variante (ou de um
cadastro errado) que a prosa atual já não reflete, e ficaram no banco sem
serem limpas quando o conteúdo mudou.

# Fora do escopo desta entrega

Corrigir ou remover as tags erradas de `hero-8` no banco — dado vivo de
produção, fora do escopo deste vault. Registrado como evidência da regra,
não como pendência de correção nossa.
