---
tipo: indice
assunto: conflitos-no-mesmo-registro-resumo-slide-contra-slide
autor: max-sturtevant
status: aprovado
---

A tabela-resumo de todos os conflitos slide-contra-slide do corpus Max: os casos em que a precedência do protocolo não resolve porque as duas versões estão no mesmo registro, com o defeito de cada um, as linhas do bruto e o desempate disponível quando existe. É resumo, não entrada — nomeia o defeito e aponta onde está a entrada completa de cada slug.

# Conflitos dentro do mesmo registro — resumo dos casos slide-contra-slide

A precedência do [[mapa-do-corpus-do-max]] — slide vence em especificação, fala vence em julgamento —
só funciona quando os **dois registros discordam entre si**. Boa parte dos conflitos
deste corpus é slide contra slide, no mesmo deck, às vezes na mesma linha. Aqui a
precedência não resolve, e o desempate, quando existe, é por **evidência de autoria
dentro do próprio material**.

**Consequência geral: não presuma que o slide fala com uma voz só.**

## Os demais conflitos slide-contra-slide

Listados juntos porque a precedência do [[mapa-do-corpus-do-max]] não resolve nenhum deles e o
diagnóstico é o mesmo. **A tabela é resumo, não entrada** — ela nomeia o defeito e não
dá as versões. A maioria tem a entrada completa no bloco do módulo dono, em
[[mapa-dos-conflitos-por-modulo]]; as **seis marcadas com ↓** são canônicas deste registro
transversal e têm a entrada completa nas notas irmãs —
`deliverability-unsubscribe-afeta-ou-nao` e `deliverability-registros-dns` em
[[conflitos-no-mesmo-registro-deliverability-unsubscribe-e-dns]];
`copy-numeracao-dos-principios`, `copy-takeaways-por-email`, `design-cta-por-produto` e
`otimizacao-sl-julgar-por-abertura-ou-receita` em
[[conflitos-no-mesmo-registro-copy-design-e-otimizacao]]. As quatro
`fundamentos-*-glossario` e `deliverability-limiar-de-open-rate` estão em
[[conflitos-no-mesmo-registro-metas-e-open-rate]].

| Slug | O defeito | Linhas | Desempate disponível |
|---|---|---|---|
| ↓ `deliverability-unsubscribe-afeta-ou-nao` | o rótulo da linha diz "(doesn't affect deliverability)" e a mesma tabela lhe dá meta; três linhas antes ele está na lista do que "Google, Yahoo, etc look at" | L8706-8710, L8719 | fala (L8432, **outro-narrador**) confirma "neutral metric" → é métrica de **monitoramento com alvo**, não de deliverability |
| `campanhas-cadencia-alta-vs-tier-1m` | 5-7x/semana listado como faixa danosa, 5-6x/semana prescrito para $1M+/mês | L5264-5269 vs L5298 | **nenhum dentro do deck**; a reconciliação existe só na fala (L4240, L4270-4276), e essa fala é `outro-provavel` |
| ↓ `copy-numeracao-dos-principios` | dois "Principle #2" e nenhum "#3" | L6578, L6604, L6625 | o acrônimo, dado certo três vezes (L6558-6576, L5504-5512, L4715-4717) → Engaging é o terceiro; o "#2" de L6625 é erro do slide |
| ↓ `copy-takeaways-por-email` | heading "Limit to 1-3 Key Points Per Email" contrariado pelo corpo duas linhas abaixo | L6615 vs L6617-6618 | corpo vence: "1" aparece três vezes (L5611, L6547, L6617); a única concessão é "When you can", que não define quando |
| `welcome-contagem-de-fillers` | heading "Insert 1-4 Filler Emails" contra o corpo "the 1–5 educational emails" | L3544 vs L3547 | corpo vence: 1-5 em três lugares (L1612, L2178, L3517) |
| ↓ `design-cta-por-produto` | a lista de regras exige botão, a página da seção aceita alternativa | L8139 vs L8282 | fala (L7458) é categórica e traz teste: "Every single time I test this if you let people know shop now… then it gets higher clicks" (L7462) → **botão** |
| `design-segundos-de-atencao` (parte) | "2-4 seconds" e "3 seconds" no mesmo deck, 16 linhas de distância | L8185 vs L8201 | L8201 é paráfrase dentro da faixa, não valor independente |
| `list-growth-tipos-de-form` | slide promete "one of the 5 form types", corpus nomeia quatro | L1200 vs L1292-1298 | fala (L998) conta quatro; o próprio slide de exemplos repete um card e omite spin-to-win |
| `list-growth-checkbox-preselecionado` | a segunda metade da linha anula a primeira | L1120 | intenção declarada (L537, L1115) → auto-marcado; o texto é colado do Shopify e não foi revisado |
| `list-growth-friccao-na-signup-page` | "Remove as much friction as possible!" e, sete linhas depois, "enter a short description" | L1127 vs L1134 | fala vence (é julgamento): headline é o desconto (L547-549) |
| `replenishment-desconto` | "without heavy discounts" e "15% Off Your Next Refill!" **dentro de cada registro** | L3992/L3247 vs L4035-4037/L3299 | nenhum; a conciliação possível é que o desconto entra só no email 2, marcado opcional (L3269) |
| ↓ `otimizacao-sl-julgar-por-abertura-ou-receita` | "Not about your open rates" e, seis linhas depois, "track open rates" | L6085 vs L6091 | receita: sustentada no deck (L6810, Max), na fala (L6229-6233, L8926-8944 — as duas **outro-narrador**) e nos dados (L6127-6139, **outro-narrador**). L6091 é resumo mal feito da página do curso |
| ↓ `deliverability-registros-dns` | quatro registros na prosa, três na lista de requisitos | L8671 vs L8687-8689 | nenhum; **SPF, DMARC, DKIM** são requisito declarado, o MX aparece uma vez na prosa. Não afirme que o MX é dispensável nem obrigatório |
| `welcome-estrutura-da-sequencia` | o slide promete "**Base Strategy:**" e não entrega nada | L3509 | nenhum; o diagrama não sobreviveu à extração |
| `winback-definicao-do-segmento` | o slide promete a definição do segmento e entrega slot vazio | L4057 | a definição completa está no deck de campanhas (L5589) |
| `design-metodos-de-transicao-ausentes` | "Here are a few methods to do this:" seguido de nada | L8307 | os quatro métodos existem só na fala (L7552-7586) |
| `flows-receita-da-agencia` (→ `doutrina-receita-da-agencia`) | $100M e $200M no mesmo deck, nove linhas de distância | L3419 vs L3428 | nenhum; o segundo está num bloco de recomendação paga do Klaviyo |
