---
tipo: ponte
status: aprovada
fonte: spec §7-7.1 e 1.1-BIS (2026-08-31-vault-componentes-email-design.md); reorganizacao 2026-09-13
---

Sem esta nota os eixos do vault são decorativos: o agente não sabe
traduzir o que tem em mãos para o vocabulário de [[_protocolo-de-selecao]].
Duas partes: o que o pipeline recebe da loja, e como cada requisito de
`requisitos/` se resolve — por código, contra a fonte que a própria nota
do requisito declara.

# Parte 1 — o que o agente tem

| O que o agente tem | Origem | Eixo que alimenta |
|---|---|---|
| identidade visual (cores com papel, fontes, logo/wordmark) | `store_brand_identity` | `paleta`, `registro`; gates de identidade (ver Parte 2) |
| produtos mais vendidos | `store_top_products` | `product_slots`, `itens`; [[produto-de-entrada-definido]] |
| catálogo público | `https://<loja>/products.json` e `collections.json` | gates de catálogo (ver Parte 2) |
| `nicho` | `store_briefings.marca.nicho` → `client_stores.niche` | ranking secundário — proxy dentro de `momento` e `objecao` |
| `posicionamento` | `marca.posicionamento` → `client_stores.posicionamento_preco` | `registro` |
| `tom_voz` / `mood` | `marca.tom_voz` → `tone_description` → `tom_de_voz` | `registro` |
| `persona` | `marca.persona` → `icp_persona` → `persona` | `objecao` |
| `pesquisa` (5 pilares) | `pesquisaToFullText(client_stores)` | `objecao`, `registro`, `paleta` — contexto de voz, **não** fonte de fatos operacionais |
| `outline_objective` / `guidance` / `tone_hint` / incentivo do toque | `email_outline_templates` | `momento`, `papel_na_peca`; gates comerciais (ver Parte 2) |
| `flow_type` + `email_number` | fila `email_dispatch_jobs` | `momento` (derivado por código) |

O Curador já recebe o julgamento em prosa das candidatas (`quando_usar`,
`quando_nao_usar`, `orientacao_copy`, `notas_implementacao`) e cruza
`product_slots` com os produtos cadastrados. O que a Parte 2 fecha é o
passo 4 (`exige:`) — eliminação verificável por código, não inferência.

# Parte 2 — como cada requisito se resolve

Todo requisito em `requisitos/` declara `classe` e `fonte_resolucao` no
frontmatter. O resolvedor é código; a resposta nunca é presumida.

| Classe | O que o código faz | Requisitos |
|---|---|---|
| `gate` · `outline` (6) | consulta `email_outline_templates` + cadência do flow; `false` elimina | [[cupom-ativo]], [[desconto-percentual]], [[prazo-real]], [[desconto-automatico-sem-cupom]], [[desconto-escalonado]], [[duas-ofertas-simultaneas]] |
| `gate` · `products_json` (8) | consulta `products.json` / `collections.json` / `store_top_products`; `false` elimina | [[gift-card-digital]], [[catalogo-de-variantes]], [[grade-de-tamanho-real]], [[produtos-com-pagina-propria]], [[colecao-ou-kit]], [[produto-com-composicao-relevante]], [[destinos-de-navegacao]], [[produto-de-entrada-definido]] |
| `gate` · `brand_identity` (4) | consulta `store_brand_identity` (não `client_stores.cores`); `false` elimina | [[cor-de-acento-definida]], [[duas-ou-tres-cores-de-identidade]], [[serif-ou-script-display]], [[wordmark-tipografico]] |
| `gate` · `pesquisa` (7) | exige citação literal do trecho da pesquisa; sem trecho, `false` elimina | [[manifesto-de-marca-escrito]], [[tres-diferenciais-concretos]], [[quatro-criterios-objetivos]], [[tres-provas-verificaveis]], [[motivo-sazonal]], [[duas-acoes-de-suporte]], [[valores-articulados]] |
| `diretiva_imagem` (16) | **não elimina**; entra em `diretivas_de_imagem` da variante e no brief da foto (`photo_direction`); `image_format` confere por pixel o que der | [[terco-superior-liso]], [[foto-estudio-fundo-claro]], [[canto-livre-para-selo]], [[corredores-livres-nas-laterais]], [[macro-de-produto]], [[packshot-vertical]], [[packshot-recortado]], [[foto-monocromatica]], [[foto-de-cena-ambiente]], [[ativo-composto-faixa-inteira]], [[fragmentos-de-contorno]], [[foto-com-pessoas]], [[foto-de-campanha-propria]], [[acervo-por-angulo]], [[embalagem-colorida]], [[ornamento-grafico-de-identidade]] |
| `reviews` (8) | fora do escopo até o banco de reviews expor metadados; **não elimina**; variantes que dependem declaram em `requisitos_de_reviews` | [[reviews-curtos]], [[reviews-longos]], [[foto-de-uso-real]], [[depoimento-com-credencial]], [[foto-do-depoente]], [[selo-compra-verificada]], [[tres-reviews-distintos]], [[ugc-autorizado]] |
| `plataforma` (3, superadas) | não é requisito — configuração de ESP/loja fora da geração; notas em `status: superada`, fora do sync | estoque-integrado, bloco-dinamico-de-carrinho, preference-center-na-esp |

`default_quando_desconhecido: false` em todos os gates: fonte indisponível
= loja não tem = elimina. A consulta exata de cada um está na própria nota
do requisito, seção `# Como se resolve`.

Números da biblioteca: [[_inventario]] · Precedência entre fontes:
[[_julgamento]]
