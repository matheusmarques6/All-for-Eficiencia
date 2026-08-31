---
tipo: ponte
status: aprovada
fonte: spec §7-7.1 e 1.1-BIS (2026-08-31-vault-componentes-email-design.md)
---

Sem esta nota os eixos do vault são decorativos: o agente não sabe
traduzir o que tem em mãos para o vocabulário de [[_protocolo-de-selecao]].
Duas partes: o que o Montador já recebe hoje, e o que ele não tem — o
contrato de um perfil de ativos da loja que ainda não existe.

# Parte 1 — o que o agente tem hoje

Mapeamento campo a campo do que o Montador recebe, verificado em
`generate.service.ts:90-169`:

| O que o agente tem | Origem | Eixo que alimenta |
|---|---|---|
| `nicho` | `store_briefings.marca.nicho` → `client_stores.niche` | ranking secundário — não é eixo próprio; nicho aparece dentro de `momento` e `objecao` como proxy, não como a coisa em si |
| `posicionamento` | `marca.posicionamento` → `client_stores.posicionamento_preco` | `registro` |
| `tom_voz` / `mood` | `marca.tom_voz` → `tone_description` → `tom_de_voz` | `registro` |
| `persona` | `marca.persona` → `icp_persona` → `persona` | `objecao` |
| `pesquisa` (5 pilares) | `pesquisaToFullText(client_stores)` | `objecao`, `registro`, `paleta` |
| `outline_objective` / `guidance` / `tone_hint` | `email_outline_templates` | `momento`, `papel_na_peca` |
| `flow_type` + `email_number` | fila `email_dispatch_jobs` | `momento` |

Isso é o insumo hoje disponível para os passos 1, 2 e 7 do protocolo — dá
para preencher `momento` (via `flow_type`/`email_number`) e para inferir
`objecao`/`registro`/`paleta` a partir de marca e pesquisa. Não dá,
sozinho, para responder ao passo 4 (`exige:`) — é essa a lacuna da Parte 2.

# Parte 2 — o buraco

**Correção necessária antes de listar o buraco.** A versão anterior desta
seção do projeto afirmava que o Curador do Montador recebia só cinco
campos categóricos por candidata e que o julgamento em prosa nunca chegava
ao LLM que escolhe. **É falso** — registrado como erro em
`docs/superpowers/specs/2026-08-31-vault-componentes-email-design.md §1.1-BIS`.
Verificado no HEAD atual de `admin-convertfy`,
`src/lib/agents/architect/component-assembler.service.ts`: o pré-filtro
determinístico por `niche_affinity`/`positioning`/`mood` foi removido
(commit `f0fcd72d`), e o catálogo enviado ao Curador (linhas 664-671)
inclui `quando_usar` (`when_use`), `quando_nao_usar` (`when_not_use`),
`product_slots`, `orientacao_copy` (`copy_guidance`) e `notas_implementacao`
(`long_description`). O prompt trata `quando_nao_usar` como **veto**, não
como desempate, e recebe `<perfil_marca>`, `<objecoes>`, `<vocabulario>`,
`<intencao>` e `<memoria>`.

Portanto o buraco real é mais estreito do que "o julgamento não chega ao
LLM":

- o pipeline **já lê** o julgamento em prosa (`when_use`, `when_not_use`,
  `copy_guidance`) e **já cruza** `product_slots` com os produtos
  cadastrados da loja;
- o que **não existe** é `exige` como lista estruturada de pré-requisitos
  de ativo (o catálogo enviado ao Curador não inclui esse campo);
  `peso` como orçamento de composição (nada impede montar uma peça de
  6.000px); `convivencia` entre blocos da mesma peça (o campo não entra no
  prompt); e, na raiz dos três, o **perfil de ativos da loja** — não existe
  em `client_stores` nenhuma coluna ou tabela que responda "esta loja tem
  cupom ativo? UGC autorizado? estoque integrado?".

Sem esse perfil, checar `exige:` contra a loja real não tem como rodar
fora de inferência implícita do LLM a partir do contexto de texto que o
prompt já carrega — não é um filtro verificável, testável e auditável fora
do modelo. É esse contrato — pergunta por pergunta, um por requisito do
vocabulário — que a tabela abaixo registra. Os **52 requisitos** de
`requisitos/` são exatamente esse contrato: cada um é uma pergunta que a
loja precisa responder para que uma eliminação por `exige:` deixe de ser
julgamento implícito.

## Comercial (8)

| Requisito | Pergunta que faz à loja | Veredito |
|---|---|---|
| [[cupom-ativo]] | Existe um cupom de desconto ativo e válido para publicar no e-mail? | nenhum campo de `client_stores` responde |
| [[desconto-automatico-sem-cupom]] | O desconto se aplica sozinho no checkout, sem código? | nenhum campo de `client_stores` responde |
| [[desconto-escalonado]] | O desconto varia por faixa de quantidade ou valor do carrinho? | nenhum campo de `client_stores` responde |
| [[desconto-percentual]] | A campanha atual é um desconto percentual puro, exibível como número? | nenhum campo de `client_stores` responde |
| [[duas-ofertas-simultaneas]] | Há duas ofertas de natureza diferente rodando ao mesmo tempo? | nenhum campo de `client_stores` responde |
| [[gift-card-digital]] | A loja vende gift card digital como produto? | nenhum campo de `client_stores` responde |
| [[prazo-real]] | A oferta tem data de expiração real e verificável? | nenhum campo de `client_stores` responde |
| [[preference-center-na-esp]] | A ESP da loja tem central de preferências publicada e linkável? | nenhum campo de `client_stores` responde |

## Dado operacional (5)

| Requisito | Pergunta que faz à loja | Veredito |
|---|---|---|
| [[bloco-dinamico-de-carrinho]] | Existe feed dinâmico ou merge tag que injete o item salvo no carrinho, por destinatário? | nenhum campo de `client_stores` responde |
| [[destinos-de-navegacao]] | A loja tem destinos de navegação distintos o bastante para preencher os links que a variante reserva? | nenhum campo de `client_stores` responde |
| [[estoque-integrado]] | A loja expõe, via API, o estoque real por SKU ou variante? | nenhum campo de `client_stores` responde |
| [[grade-de-tamanho-real]] | O produto tem variação real de tamanho, com estoque individual por tamanho? | nenhum campo de `client_stores` responde |
| [[produtos-com-pagina-propria]] | Cada produto do catálogo tem página própria (URL individual) para o CTA apontar? | nenhum campo de `client_stores` responde |

## Catálogo e argumento (11)

| Requisito | Pergunta que faz à loja | Veredito |
|---|---|---|
| [[catalogo-de-variantes]] | O catálogo tem variantes reais do mesmo produto para citar separadamente, uma por linha? | nenhum campo de `client_stores` responde |
| [[colecao-ou-kit]] | Os produtos mostrados na peça pertencem à mesma coleção ou kit? | nenhum campo de `client_stores` responde |
| [[duas-acoes-de-suporte]] | Existem duas ações de suporte com pesos diferentes que a loja pode oferecer no mesmo e-mail? | nenhum campo de `client_stores` responde |
| [[manifesto-de-marca-escrito]] | A marca tem um manifesto ou discurso institucional já escrito e aprovado? | nenhum campo de `client_stores` responde |
| [[motivo-sazonal]] | Existe um motivo sazonal real ancorando a campanha? | nenhum campo de `client_stores` responde |
| [[produto-com-composicao-relevante]] | O produto tem composição, ingredientes ou materiais que valem a pena listar? | nenhum campo de `client_stores` responde |
| [[produto-de-entrada-definido]] | A loja tem um produto de entrada claro para quem nunca comprou? | nenhum campo de `client_stores` responde |
| [[quatro-criterios-objetivos]] | Existem ao menos quatro critérios objetivos de comparação de categoria em que a marca vence de forma defensável? | nenhum campo de `client_stores` responde |
| [[tres-diferenciais-concretos]] | A marca tem três diferenciais concretos e nomeáveis, cobrindo eixos distintos? | nenhum campo de `client_stores` responde |
| [[tres-provas-verificaveis]] | Existem três atributos objetivos e verificáveis do produto? | nenhum campo de `client_stores` responde |
| [[valores-articulados]] | A marca tem valores institucionais já articulados, prontos para virar selo? | nenhum campo de `client_stores` responde |

## Prova social (8)

| Requisito | Pergunta que faz à loja | Veredito |
|---|---|---|
| [[depoimento-com-credencial]] | Existe depoimento de cliente com credencial nomeável (cargo, título, autoridade)? | nenhum campo de `client_stores` responde |
| [[foto-de-uso-real]] | Existe foto do produto sendo usado de verdade, não packshot de catálogo? | nenhum campo de `client_stores` responde |
| [[foto-do-depoente]] | Existe foto real da pessoa que deu o depoimento? | nenhum campo de `client_stores` responde |
| [[reviews-curtos]] | Existem reviews de uma frase, curtos o bastante para caber numa faixa estreita? | nenhum campo de `client_stores` responde |
| [[reviews-longos]] | Existem reviews com pelo menos ~80 caracteres, não notas de uma linha? | nenhum campo de `client_stores` responde |
| [[selo-compra-verificada]] | A loja ou a plataforma de reviews tem selo real de "compra verificada"? | nenhum campo de `client_stores` responde |
| [[tres-reviews-distintos]] | Existem ao menos três reviews que citam produtos diferentes entre si? | nenhum campo de `client_stores` responde |
| [[ugc-autorizado]] | Existe UGC — foto de cliente real — com autorização de uso concedida? | nenhum campo de `client_stores` responde |

## Ativo visual e identidade (20)

| Requisito | Pergunta que faz à loja | Veredito |
|---|---|---|
| [[acervo-por-angulo]] | Existe acervo de fotos do mesmo produto em ângulos realmente diferentes? | nenhum campo de `client_stores` responde |
| [[ativo-composto-faixa-inteira]] | Existe um ativo já montado como faixa inteira (composição horizontal única)? | nenhum campo de `client_stores` responde |
| [[canto-livre-para-selo]] | A foto do produto tem um canto vazio onde um selo circular pode ser sobreposto? | nenhum campo de `client_stores` responde |
| [[cor-de-acento-definida]] | A marca tem uma cor de acento definida na identidade, além de preto/branco/cinza? | nenhum campo de `client_stores` responde |
| [[corredores-livres-nas-laterais]] | A foto do produto tem espaço vazio nas laterais, sem elemento ocupando essa área? | nenhum campo de `client_stores` responde |
| [[duas-ou-tres-cores-de-identidade]] | A marca tem pelo menos duas ou três cores definidas na identidade? | nenhum campo de `client_stores` responde |
| [[embalagem-colorida]] | O produto tem embalagem colorida que funcione como elemento visual da peça? | nenhum campo de `client_stores` responde |
| [[foto-com-pessoas]] | Existe foto de pessoa real usando ou perto do produto? | nenhum campo de `client_stores` responde |
| [[foto-de-campanha-propria]] | Existe foto de campanha produzida pela própria marca, não banco de imagem? | nenhum campo de `client_stores` responde |
| [[foto-de-cena-ambiente]] | Existe foto de cena/ambiente do produto em contexto de uso? | nenhum campo de `client_stores` responde |
| [[foto-estudio-fundo-claro]] | Existe foto de produto em estúdio, com fundo claro e uniforme? | nenhum campo de `client_stores` responde |
| [[foto-monocromatica]] | Existe foto de produto ou campanha tratada em monocromia? | nenhum campo de `client_stores` responde |
| [[fragmentos-de-contorno]] | Existem ativos com fragmentos de contorno — molduras parciais que emolduram o recorte? | nenhum campo de `client_stores` responde |
| [[macro-de-produto]] | Existe foto em macro/close-up capaz de provar um diferencial de material ou acabamento? | nenhum campo de `client_stores` responde |
| [[ornamento-grafico-de-identidade]] | A marca tem um elemento gráfico ornamental próprio já incorporado à identidade? | nenhum campo de `client_stores` responde |
| [[packshot-recortado]] | Existe imagem do produto já recortada, com fundo removido? | nenhum campo de `client_stores` responde |
| [[packshot-vertical]] | Existe packshot do produto em orientação vertical (garrafa, tubo, frasco)? | nenhum campo de `client_stores` responde |
| [[serif-ou-script-display]] | A marca tem uma fonte display serifada ou script definida na identidade? | nenhum campo de `client_stores` responde |
| [[terco-superior-liso]] | A foto disponível tem uma faixa lisa e uniforme no terço superior? | nenhum campo de `client_stores` responde |
| [[wordmark-tipografico]] | A marca tem um wordmark que funciona como texto puro, sem depender de logotipo em imagem? | nenhum campo de `client_stores` responde |

---

Enquanto este perfil não existir, o passo 4 do [[_protocolo-de-selecao]]
roda com o que o humano souber responder. Esta nota diz isso em vez de
fingir que o filtro está automatizado.

Números da biblioteca: [[_inventario]] · O que o Curador recebe hoje, com
file:line: [[o-que-o-curador-ainda-nao-tem]]
