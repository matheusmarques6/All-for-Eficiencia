---
tipo: indice
modulo: flows
assunto: mapa-de-flows
autor: max-sturtevant
fonte: "CONTEUDO BRUTO/max.md — L1307-3403 (transcrição), L3404-4186 (slide GAMMA)"
status: rascunho
---

# O que tem aqui

O módulo de flows do curso: oito flows nomeados, sete com aula, um só com
título. Mais três notas auxiliares.

| Nota | O que tem dentro |
|---|---|
| [[welcome]] | gatilho, filtros, saída, as 7 non-negotiables, as **três** sequências que não coincidem, a janela de 5 dias |
| [[welcome-fillers]] | os 7 fillers que ele julga na aula + os 21 ângulos catalogados no slide |
| [[welcome-templates]] | os 3 templates de seção do slide, verbatim: welcome #1, last chance, text-based support |
| [[site-abandon]] | `Active on Site`, 1-2 emails, delay 4h (só na fala), saída ao ver produto |
| [[browse-abandon]] | `Viewed Product`, 4 emails, 1h + 1 dia, subject lines dos quatro |
| [[cart-checkout-abandon]] | **dois** flows, `Added to Cart` e `Started Checkout`; a acusação de que os templates base do Klaviyo estão rotulados errado |
| [[post-purchase]] | `Placed Order`, 2 emails base, split por número de compras, três escopos temporais em conflito |
| [[replenishment]] | 21 dias + 7 dias, exclusivo-ish de CPG, o desconto que contradiz a promessa do flow |
| [[winback]] | o único disparado por **segmento**, não por metric; 90/120/180 dias |
| [[sunset]] | **lacuna declarada** — o corpus tem só o título, um link gamma e uma imagem quebrada |
| [[conteudo-dinamico-klaviyo]] | as três fórmulas de bloco dinâmico, verbatim, e por que a de checkout é estruturalmente diferente |
| [[otimizacao-de-flows]] | só no slide: campanha como campo de teste, migrar vencedoras para flows, os 4 testes de flow |

# A tabela comparativa dos 8 flows

**Célula vazia = o corpus não informa.** Não preencher por analogia com outro
flow. A ausência é informação, não erro de extração.

| Flow | Gatilho | Nº de emails | Delay do 1º | Delays seguintes | Filtros | Condição de saída |
|---|---|---|---|---|---|---|
| **Welcome** | opt-in na lista *(metric nunca nomeada)* | 3 mín. · 4-5 · 6 · até 15 · 3-4 ou 6-8 | imediato (L1420, L3492) | 1-2 dias (L1458, L3494) — contra "every day" (L1468-1472) | `placed order zero times since starting this flow` (L1542) · `bounce less than two times since starting this flow` (L1544) | falhar qualquer filtro (L1546) |
| **Site abandon** | `Active on Site` (L2345, L3613) | 1-2 (L2363-2365, L3619) | 4h padrão · 1h agressivo (L2369-2371) | | | ver página de produto (L2347-2355) |
| **Browse abandon** | `Viewed Product` (L2452, L3671) | 4 (L2472, L3678) | 1 hora (L2476) | 1 dia entre os demais (L2476-2478); slide: "over 3-4 days" (L3678) | | |
| **Cart abandon** | `Added to Cart` (L2669, L3784) | 4 (L3798-3881) | | | | |
| **Checkout abandon** | `Started Checkout` (L3790) / "checkout started" (L2671) | 4 (L3798-3881) | | | | |
| **Post-purchase** | `Placed Order` — Shopify (L3032, L3920) | 2 base, "add more" (L3156, L3969) | imediato (L3064) | "a couple days" (L3066) | | |
| **Replenishment** | `placed order` (L3251) — só na fala | 2 (L3255, L4003) | 21 dias (L3251); janela citada 30-60 / 21-60 (L3233-3235) | 7 dias (L3257-3259, L4003); depois "set whatever time delay you want" (L3289) | | não ter recomprado — implícito (L4003), nunca especificado |
| **Winback** | **segmento**, não metric (L3314, L4053) | 3 (L3334, L4063-4065) | Day 0 (L3326, L4063) | Day 7 e Day 10 (L4065) — só no slide | | |
| **Sunset** | | | | | | |

Notas da tabela:

- **Sunset está inteiramente vazio** e isso não é falha de leitura: o corpus tem
  seis linhas sobre ele (L3398-3403). Ver [[sunset]].
- **Cart e checkout são a lacuna mais cara**: quatro emails especificados, com
  subject lines e quick tips, e nenhum delay, filtro ou condição de saída em
  nenhum dos dois registros (L2618-3019 e L3777-3914).
- **Welcome é o único flow com filtros declarados** no corpus inteiro.
- **Winback é o único disparado por segmento.** Ele explicita o contraste: "all
  the other flows, we're using an actual trigger of some sort where it's some
  sort of metric connected to Shopify" (L3314).
- O segmento do winback é prometido no slide (L4057) e não entregue ali; a
  definição existe fora da faixa de flows, em L5589 e L5057.

# Como rotear daqui

| A pergunta é sobre… | Vá para |
|---|---|
| montar um flow do zero | a nota do flow → [[_conflitos]] |
| um número (delay, contagem, prazo) | [[_numeros]] antes de tudo |
| bloco dinâmico, variável Klaviyo | [[conteudo-dinamico-klaviyo]] |
| o que testar num flow | [[otimizacao-de-flows]] |
| copy/subject line de flow | a nota do flow, bloco `# A sequência` ou `# Templates` |
| sunset flow | [[sunset]] — e recusar |

# Duas advertências de leitura

1. **Os exemplos de copy são ASR.** Quase todo exemplo de email neste módulo foi
   lido em voz alta em cima de uma imagem que não sobreviveu à extração. A
   transcrição erra nomes de marca e números ("Mints versus facts" por *Myths vs
   Facts*, "1x% off" por *10% off*). Onde a nota marca "(ASR)", a fidelidade é
   menor que a de um artefato de slide.
2. **Nenhuma imagem sobreviveu.** Há um único marcador de imagem em toda a faixa
   L1307-4186, e é o do Sunset Flow (L3402). Todos os slots
   "**Email Example:**" do deck vieram vazios.
