---
tipo: secao
secao: hero
variantes: 9
ativas: 9
com_julgamento: 9
status: aprovada
---

# Cobertura

9 variantes, todas ativas, todas com julgamento completo. É a seção mais
bem coberta da biblioteca — com uma ressalva: [[hero-8-lineup-com-lembrete-de-oferta]]
e [[hero-10-lineup-de-colecao]] têm `momento`, `objecao`, `registro`,
`paleta`, `exige` e `convivencia` idênticos no frontmatter (só
`variant_id`, `schema_campos` e `peso.altura_px` divergem). Nenhum eixo do
protocolo os separa; contam como 9 no inventário, mas como 8 perfis de
decisão distintos. Ver [[hero-8-duplicata-de-hero-10]].

# Chave de decisão

Ordem de leitura, na ordem real do protocolo: momento (filtro) → exige
(requisito duro, inclui o ativo fotográfico) → objeção (1º eixo de
ranking) → registro (2º eixo). `paleta` não entra como coluna: seus
valores empatam exatamente onde `exige` e `objeção` já decidiram, então
não teria poder de separação adicional.

| Variante | Momento | Exige (requisito duro) | Objeção | Registro |
|---|---|---|---|---|
| [[hero-3-cupom-de-captacao]] | welcome-1 | cupom ativo · foto estúdio fundo claro · terço superior liso | preço-valor | — |
| [[hero-4-editorial-de-pertencimento]] | welcome-1 | cupom ativo · foto de campanha própria · serif/script display · cor de acento definida | pertencimento | premium-editorial |
| [[hero-5-cupom-em-tres-lugares]] | welcome-1 | cupom ativo · foto com pessoas | preço-valor | volume-impulso, popular-informal |
| [[hero-6-percentual-gigante]] | welcome-1 | cupom ativo · foto monocromática | preço-valor | — |
| [[hero-7-campanha-sem-cupom]] | campanha-promocional, sazonal | desconto automático **sem** cupom · desconto escalonado · foto estúdio fundo claro | preço-valor | — |
| [[hero-2-pergunta-comparativa]] | consideração, reengajamento | cor de acento definida · desconto percentual · macro de produto | qualidade-eficácia | — |
| [[hero-9-atendimento-proativo]] | browse-abandonment, reengajamento | foto monocromática · terço superior liso · duas ações de suporte | suporte-dúvida | clínico-sóbrio |
| [[hero-10-lineup-de-colecao]] | welcome-meio, welcome-tardio, newsletter, sazonal, cross-sell, browse-abandonment | foto estúdio fundo claro · terço superior liso | amplitude-de-catálogo | — |
| [[hero-8-lineup-com-lembrete-de-oferta]] | idêntico a hero-10 | idêntico a hero-10 | idêntico a hero-10 | idêntico a hero-10 |

**Como ler:** nenhuma das nove exige nem veta cupom, exceto quando o
próprio requisito é sobre isso: hero-3/4/5/6 **exigem** cupom ativo no
sentido literal de `exige`; hero-7 tem `desconto-automatico-sem-cupom` em
`exige`, o que **veta** cupom de fato (as duas coisas não convivem na
mesma peça). Nenhuma outra variante — nem hero-2, nem hero-9, nem
hero-8/10 — menciona cupom em `exige`: elas não exigem nem vetam, o que a
prosa do banco descreve como "lembrete de oferta" no caso do hero-8 não é
um requisito duro, é só o nome da peça. Dentro do grupo `preço-valor`
(hero-3, 5, 6, 7), quem separa é o ativo fotográfico exigido — os quatro
pedem uma foto diferente — e o momento, que isola hero-7 (campanha, sem
welcome) dos outros três (welcome-1).

# Onde a seção não cobre

- Nenhuma variante de hero para `carrinho-abandonado` ou
  `checkout-abandonado`: as nove vetam esses momentos explicitamente.
- Nenhuma para `pos-compra` ou `transacional`.
- Nenhuma de registro `comunidade-identitario`.
- Efetivamente 8 perfis de decisão, não 9 — hero-8 e hero-10 competem pela
  mesma vaga sem que nenhum eixo do protocolo escolha entre eles.
