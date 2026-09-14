---
tipo: secao
secao: body
variantes: 9
ativas: 7
com_julgamento: 5
status: aprovada
---

# Cobertura

9 variantes, 7 ativas, mas só **5 com julgamento** (`status: aprovada`) —
e dessas 5, duas ([[body-5-comparacao-nos-vs-eles]] e
[[body-10-listicle-educativo]]) estão `ativa: false`. Isso deixa apenas
**3 variantes** (body-2, body-3, body-4) simultaneamente ativas e
julgadas — o conjunto que o protocolo de fato rankeia por eixo.

As outras 4 ([[body-quatro-variantes-sem-julgamento]]: body-6, body-7,
body-8, body-9) estão `ativa: true` mas com `status: sem-julgamento` e
todos os eixos de ranking vazios — `momento`, `objecao`, `registro`
em branco nas quatro. Elas existem, o pipeline pode renderizá-las,
mas como nunca perdem por veto nem ganham por match de eixo, o ranking
nunca tem razão para colocá-las à frente de uma variante julgada — na
prática, **nunca são escolhidas** enquanto houver candidata julgada
disponível para o mesmo momento.

# Chave de decisão

Entre as 3 variantes ativas e julgadas, `momento` e `objeção` já separam:

| Variante | Momento | Objeção | Ativa |
|---|---|---|---|
| [[body-2-colagem-de-data-comemorativa]] | sazonal-data-comemorativa | — | sim |
| [[body-3-pitch-de-gift-card]] | gift-card, sazonal-data-comemorativa | escolha-variedade, pertencimento | sim |
| [[body-4-comparativo-em-duas-colunas]] | welcome-meio, welcome-tardio, consideração, browse-abandonment | qualidade-eficácia, preço-valor | sim |

Duas variantes julgadas ficam de fora já no passo 3 do
[[_protocolo-de-selecao]] (lista restrita a `ativa: true`) por estarem
inativas — registradas aqui porque descrevem o que a seção *deveria*
cobrir se fossem reativadas:

| Variante | Momento | Objeção | Ativa |
|---|---|---|---|
| [[body-5-comparacao-nos-vs-eles]] | welcome-meio, welcome-tardio, carrinho-abandonado, browse-abandonment | confiança-no-canal, preço-valor | **não** |
| [[body-10-listicle-educativo]] | nutrição-de-conteúdo, welcome-meio, reengajamento | uso-aprendizado | **não** |

As 4 sem-julgamento não entram em tabela de eixos porque não têm eixo
nenhum — são escolhidas às cegas quando sorteadas, nunca por critério.

# Onde a seção não cobre

- Entre as variantes que o protocolo de fato consegue rankear (as 3
  ativas+julgadas), só **duas objeções** têm cobertura:
  `qualidade-eficacia` e `preco-valor` (body-4, o comparativo). Todo o
  resto do vocabulário de objeções fica sem body julgado e ativo —
  inclusive `uso-aprendizado` (body-10 existe mas está inativa).
- **Dispositivos não cobertos** (por `objecao × papel`), pedidos pelo
  batch 6249aef2: tese com 3 itens sem cupom
  ([[body-tese-3-itens-sem-cupom]]) e faixa de garantias com 3 selos
  ([[body-garantias-3-selos]]) — ambos para `confianca-no-canal` /
  `qualidade-eficacia`.
- [[body-5-comparacao-nos-vs-eles]] é a **única** variante do catálogo
  inteiro (44) que serve a objeção `confianca-no-canal` — e está inativa.
  Ver [[welcome-5-sem-variante-ativa]].
- Nenhuma cobertura julgada e ativa para `campanha-promocional`,
  `carrinho-abandonado`, `checkout-abandonado`, `welcome-1`, `lançamento`
  ou `consideração`.
