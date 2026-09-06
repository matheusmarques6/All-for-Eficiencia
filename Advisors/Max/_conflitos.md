---
tipo: indice
assunto: conflitos-do-corpus
autor: max-sturtevant
status: rascunho
---

# Para que serve

Registro único de onde o corpus Max se contradiz. É o que impede o advisor de
responder com confiança falsa: se o assunto tem entrada aqui, não existe
resposta limpa, e a resposta certa mostra as duas versões.

O [[_protocolo]] manda checar esta nota no passo 4, **antes** de ler a nota do
assunto. Toda nota que carrega contradição declara o slug no frontmatter
`conflitos:`; os slugs vivem no índice abaixo.

**A regra de ouro: nenhum conflito é resolvido por média.** Se o corpus dá 3, 6
e 15, a resposta é "o piso é 3 e o critério é este" — nunca "cerca de 8". Média
inventada é indistinguível de conhecimento real e impossível de auditar depois.
Vale também para arredondamento, conversão e interpolação. Onde o corpus não
permite desempate, o "Como responder" diz isso com todas as letras.

# Como ler cada entrada

Cada entrada tem duas partes:

1. **Tabela de versões** — `valor verbatim` · `registro` · `linha`. O valor é
   copiado do bruto em inglês, sem tradução e sem normalização. O registro é
   `transcricao`, `slide` (deck GAMMA), `resumo do módulo` (bloco de bullets da
   página do curso, que não é nem fala nem deck) ou `outro-narrador`. A linha é
   de `CONTEUDO BRUTO/max.md`.
2. **`Como responder:`** — a posição mais sustentada e por quê, a outra versão
   com a linha, e o critério dele para decidir quando existe. O critério real
   quase nunca é numérico: é tipo de produto, tamanho de lista, faturamento.

**Precedência** ([[_INDEX]]): slide vence em especificação, fala vence em
julgamento. Ela só funciona **entre** registros. Boa parte dos conflitos deste
corpus é slide contra slide no mesmo deck — esses estão reunidos na seção
[[#Conflitos dentro do mesmo registro]] e a precedência não os resolve.

**Atribuição:** o laudo [[_autoria]] classifica dez blocos de fala como
`outro-provavel` ou `outro-provado`. Onde um lado do conflito cai num desses
blocos, a entrada avisa — porque isso muda o peso da versão, e às vezes decide.

Marcadores de tipo usados no índice:

| Marcador | Significa |
|---|---|
| `conflito` | duas ou mais versões incompatíveis, ou não reconciliadas pelo corpus |
| `armadilha` | **não é conflito** — o mesmo número mede coisas diferentes, e a leitura ingênua cria contradição que não existe |
| `lacuna` | o corpus promete e não entrega; a ausência é informação |
| `proveniência` | mesmo conteúdo em dois lugares; importa a origem, não o valor |
| `→ slug` | slug redundante; a entrada canônica é a apontada |

# Índice de slugs

## fundamentos

| Slug | Assunto | Tipo |
|---|---|---|
| `fundamentos-open-rate-glossario` | piso de open rate: 50% vs 45% | conflito (§ mesmo registro) |
| `fundamentos-unsubscribe-glossario` | teto de unsubscribe: 0,3% vs 0,2% | conflito (§ mesmo registro) |
| `fundamentos-spam-glossario` | teto de spam: 0,01% vs 0,1% — **10×** | conflito (§ mesmo registro) |
| `fundamentos-click-rate-glossario` | click rate separado por tipo de envio ou único | conflito (§ mesmo registro) |
| `fundamentos-roi-do-email` | $36+ por $1 vs ~40x ROI | conflito |
| `fundamentos-split-campanhas-flows` | 50/50, 40-60 ou 60/40 | conflito |
| `fundamentos-denominador-dos-80` | 80% de qual receita | conflito |
| `fundamentos-limiar-de-escalar-aquisicao` | 55% ou 60% para voltar a anúncio | conflito |
| `fundamentos-piso-de-email-share` | piso de 30% (e o 40% que é meta) | conflito |
| `fundamentos-anuncios-por-dia` | 70+ vs 250 anúncios/dia | conflito |
| `fundamentos-formula-da-lucratividade` | produto no slide, soma na fala | conflito |
| `fundamentos-smart-sending` | desligar em campanha ou em flow | conflito |
| `fundamentos-benchmark-do-form` | 6-12% de qual denominador | conflito |
| `fundamentos-klaviyo-melhor-ou-pior` | melhor ESP e pior plataforma de pop-up | conflito |
| `fundamentos-deliverability-e-facil` | meio pilar porque é fácil, e "complicated" | conflito |
| `fundamentos-o-que-move-o-open-rate` | segmentação, não subject line — vs 5-15% | conflito (§ entre módulos) |
| `fundamentos-time-delay-do-form` | → `list-growth-time-delay` | → slug |

## doutrina

| Slug | Assunto | Tipo |
|---|---|---|
| `doutrina-narrador-da-aula-de-ia` | parte do material não é fala do Max | conflito |
| `doutrina-segundos-de-atencao` | 3s vs 2-3s vs 2-4s, e o "antes" | conflito (§ entre módulos) |
| `doutrina-ia-primeiro-rascunho` | a regra proíbe, a prática faz | conflito |
| `doutrina-formato-do-slice` | JPEG, PNG ou tanto faz | conflito |
| `doutrina-receita-da-agencia` | $40M, $100M, $200M | conflito |
| `doutrina-lista-de-marcas` | grafia dos nomes próprios | conflito |
| `doutrina-sce-numeracao-dos-principios` | → `copy-numeracao-dos-principios` | → slug |
| `doutrina-proporcao-basico-avancado` | → `otimizacao-peso-do-basico` | → slug |

## list-growth

| Slug | Assunto | Tipo |
|---|---|---|
| `list-growth-tipos-de-form` | slide promete cinco, corpus nomeia quatro | conflito + lacuna |
| `list-growth-time-delay` | sete formulações do delay do pop-up | conflito |
| `list-growth-benchmark-de-form` | a escada 3-5 · 6 · 6-12 · 10+ · 20+ · 20-30% | conflito |
| `list-growth-botao-x` | rótulo OPTIONAL, comportamento obrigatório | conflito |
| `list-growth-exit-intent` | rejeição geral vs rejeição só no mobile | conflito |
| `list-growth-teaser` | rejeição geral vs liberado no desktop | conflito |
| `list-growth-imagem-lateral` | quebra no mobile, testada no desktop | conflito |
| `list-growth-alia-url-e-oferta` | três URLs, duas ofertas, oito grafias | conflito |
| `list-growth-alia-vs-klaviyo` | stack de duas camadas pagas | conflito |
| `list-growth-popup-vs-full-page` | template "full page" executado como pop-up | conflito |
| `list-growth-checkbox-preselecionado` | L1120 anula a si mesma | conflito (§ mesmo registro) |
| `list-growth-friccao-na-signup-page` | remova fricção vs escreva subheading | conflito (§ mesmo registro) |
| `list-growth-lista-de-ofertas` | sete opções vs resumo de quatro | conflito |

## flows

| Slug | Assunto | Tipo |
|---|---|---|
| `welcome-contagem-de-emails` | 3, 4-5, 6, 3-4/6-8, 15 | conflito |
| `welcome-cadencia` | 1-2 dias vs todo dia | conflito |
| `welcome-estrutura-da-sequencia` | base strategy vs template vs recap | conflito + lacuna |
| `welcome-contagem-de-fillers` | 1-5 contra um heading 1-4 | conflito (§ mesmo registro) |
| `welcome-catalogo-de-fillers` | 21 ângulos no slide, 14 na fala | conflito |
| `welcome-prazo-da-oferta` | 40h, "tonight", +24h | conflito |
| `welcome-valor-do-desconto` | nenhuma regra em nenhum registro | lacuna |
| `site-abandon-delay-so-na-fala` | 4h (fala) e nada no slide | conflito |
| `browse-abandon-janela-de-delays` | 1h+1d+1d+1d vs "3-4 days" | conflito |
| `browse-abandon-definicao-do-gatilho` | "no further" vs "doesn't add to cart" | conflito |
| `cart-checkout-conteudo-igual-ou-diferente` | três posições em minutos | conflito |
| `cart-checkout-ausencia-total-de-delays` | zero delay/filtro nos dois registros | lacuna |
| `cart-checkout-bloco-dinamico` | Table vs Split sem explicação | conflito |
| `post-purchase-escopo-temporal` | 7d, 14d, ~3 semanas | conflito |
| `replenishment-janela` | 30→21 dias, e "set whatever you want" | conflito |
| `replenishment-desconto` | "without heavy discounts" + 15% off | conflito (§ mesmo registro) |
| `winback-cadencia` | fala só dá Day 0; slide dá 0/7/10 | conflito |
| `winback-definicao-do-segmento` | versão sem o teto de 150 dias | conflito |
| `flows-participacao-na-receita` | 20% da loja vs 50% do email | conflito |
| `flows-onde-testar` | campanha é o campo de teste vs delay é no flow | conflito (§ entre módulos) |
| `flows-frequencia-de-campanha` | → `campanhas-sweet-spot-de-frequencia` | → slug |
| `flows-receita-da-agencia` | → `doutrina-receita-da-agencia` | → slug |

## campanhas

| Slug | Assunto | Tipo |
|---|---|---|
| `campanhas-sweet-spot-de-frequencia` | 2-4x vs 3x | conflito |
| `campanhas-tier-250k-1m` | 4x (tabela) vs 3-4x (fala) | conflito |
| `campanhas-o-que-determina-a-frequencia` | tabela tem 2 entradas, fala tem 4 | conflito |
| `campanhas-cadencia-alta-vs-tier-1m` | 5-7x é danoso e 5-6x é prescrito | conflito (§ mesmo registro) |
| `campanhas-ratio-grafico-texto` | 80-20, 75-25, 4:1, 5:1 | conflito |
| `campanhas-frequencia-de-texto-puro` | ratio vs piso de 2/mês | conflito |
| `campanhas-distribuicao-dos-pilares` | divisão par vs "no exact formula" | conflito |
| `campanhas-limiar-vip` | 4 pedidos (slide) vs 5 (fala) | conflito |
| `campanhas-suppress-list` | sintaxe exata vs fala aproximada | conflito |
| `campanhas-share-do-90-day-engaged` | **não é conflito de quatro valores** | armadilha |
| `campanhas-janela-de-engajamento` | 90 dias e o critério para 30/60 | conflito |
| `campanhas-winback-janela` | 150/90 vs 100/180 | conflito |
| `campanhas-janela-do-segmento-de-interesse` | over all time vs last 30 days | conflito |
| `campanhas-limiar-de-hipersegmentacao` | $1M/mês e a segunda porta indefinida | conflito |
| `campanhas-encanador-ou-eletricista` | mesma analogia, dois ofícios | conflito |

## copy

| Slug | Assunto | Tipo |
|---|---|---|
| `copy-numeracao-dos-principios` | dois "#2" e nenhum "#3" | conflito (§ mesmo registro) |
| `copy-takeaways-por-email` | heading diz 1-3, corpo diz 1 | conflito (§ mesmo registro) |
| `copy-subject-line-comprimento` | regra 2-5 palavras, prática 5 e 8 | conflito |
| `copy-subject-line-reticencias` | "…" é de preview text ou de SL | conflito |
| `copy-open-rate-limite` | ~10% vs "10, maybe 15" vs "five, 10%" | conflito |
| `copy-multiplicador-de-vendas` | 3x vs 3-5x, métricas diferentes | conflito |
| `copy-preview-text-obrigatorio` | framework exige, disrupção omite | conflito |
| `copy-nao-complique-vs-framework` | "don't overthink" + dois frameworks | conflito |
| `copy-nomes-dos-infograficos` | Icons vs Icon Graphics | conflito |
| `copy-email-marketing-brain-tamanho` | "500 pages" vs "500 docs" | conflito |
| `copy-janela-de-atencao` | → `doutrina-segundos-de-atencao` | → slug |
| `copy-medir-por-abertura` | → `otimizacao-sl-julgar-por-abertura-ou-receita` | → slug |
| `copy-open-rate-limite` ← `otimizacao-teto-de-abertura` | (canônico acima) | → slug |
| `copy-papel-da-ia` | → `doutrina-ia-primeiro-rascunho` | → slug |
| `copy-narrador-nao-e-max` | → `doutrina-narrador-da-aula-de-ia` | → slug |

## design

| Slug | Assunto | Tipo |
|---|---|---|
| `design-botao-above-the-fold-sempre` | sempre vs 75% dos emails | conflito |
| `design-repeticao-de-cta` | 2-3x vs "não encha de botões" | conflito |
| `design-cta-por-produto` | botão obrigatório vs botão ou sublinhado | conflito (§ mesmo registro) |
| `design-quantidade-de-produtos` | cinco respostas em oito linhas | conflito |
| `design-quantidade-de-bridges` | 0-1 (fala) vs 0-2 (slide) | conflito |
| `design-bridge-e-product-opcionais` | opcional com e sem frequência | conflito |
| `design-altura-do-slice` | 800, 720, mil | conflito |
| `design-blocky` | frase errada corrigida em cena | conflito |
| `design-metodos-de-transicao-ausentes` | deck promete métodos e lista zero | lacuna |
| `design-klaviyo-vs-omnisend` | título Klaviyo, demonstração Omnisend | conflito |
| `design-passos-do-upload` | mesmo procedimento, duas redações | conflito |
| `design-plugins-do-figma` | plug-ins como razão vs "não uso" | conflito |
| `design-tres-usos-de-75-por-cento` | o mesmo 75% mede três coisas | armadilha |
| `design-html-vs-imagem` | HTML desnecessário vs HTML ajuda | conflito (§ entre módulos) |
| `design-segundos-de-atencao` | → `doutrina-segundos-de-atencao` | → slug |
| `design-nomes-de-marca` | → `doutrina-lista-de-marcas` | → slug |

## deliverability

| Slug | Assunto | Tipo |
|---|---|---|
| `deliverability-limiar-de-open-rate` | dez formulações; o slide discorda de si | conflito (§ mesmo registro) |
| `deliverability-passo-de-escalonamento` | 25-50% vs ~50% por envio | conflito |
| `deliverability-primeiro-degrau-da-rampa` | "200,000" corrompido vs 100-300 | conflito |
| `deliverability-unsubscribe-afeta-ou-nao` | neutro, mas com meta e na lista | conflito (§ mesmo registro) |
| `deliverability-lista-base-padrao` | 90 dias (slide) vs 60 (fala) | conflito |
| `deliverability-registros-dns` | quatro na prosa, três na lista | conflito (§ mesmo registro) |
| `deliverability-caso-mailchimp-escala-final` | números narrados que não fecham | conflito |
| `deliverability-salto-de-45` | unidade ausente | lacuna |

## otimizacao

| Slug | Assunto | Tipo |
|---|---|---|
| `otimizacao-peso-do-basico` | 90/10 vs 80/20 — **veredicto arbitrado** | conflito |
| `otimizacao-frequencia-precondicao` | 3-4/semana como pré-condição de teste | conflito (§ entre módulos) |
| `otimizacao-lista-pequena-quantas-repeticoes` | não é foco, mas repita 3-4 vezes | conflito |
| `otimizacao-horarios-a-testar` | 11h-12h vs a lista vs o caso real | conflito |
| `otimizacao-lista-redundante` | deck repete long/short e send time | proveniência |
| `otimizacao-grafico-numero-de-variantes` | duas vias vs três vias | conflito |
| `otimizacao-metricas-do-print` | métrica do print não é definida | lacuna |
| `otimizacao-sl-julgar-por-abertura-ou-receita` | receita vs "track open rates" | conflito (§ mesmo registro) |
| `otimizacao-from-name-testar-ou-prescrever` | teste no deck, prescrição no resto | conflito |
| `otimizacao-deck-duplicado` | quatro testes vindos do deck de flows | proveniência |
| `otimizacao-onde-testar` | → `flows-onde-testar` | → slug |
| `otimizacao-teto-de-abertura` | → `copy-open-rate-limite` | → slug |

## sms

| Slug | Assunto | Tipo |
|---|---|---|
| `sms-frequencia` | 1-2/semana, "once per weekish", e o calendário | conflito |
| `sms-frequencia-de-email-comparada` | 4-5x de email citado dentro do SMS | conflito (§ entre módulos) |
| `sms-mms-no-browse-abandon` | proibição e a exceção nomeada | conflito |
| `sms-open-rate-de-email` | 30% de mercado vs 50%+ de meta | conflito (§ entre módulos) |
| `sms-quinze-por-cento` | o mesmo 15% mede duas coisas | armadilha |
| `sms-instrucoes-de-optin-sao-de-email` | procedimento de email sob título de SMS | conflito |
| `sms-vias-de-crescimento` | duas vias (SMS) vs quatro (email) | conflito |
| `sms-welcome-contagem` | 2-3 (fala) vs template de 2 (slide) | conflito |
| `sms-janela-do-winback` | 120 dias (SMS) vs 90 (email) | conflito |
| `sms-transacional-puro-ou-quase` | "purely" vs "mostly" | conflito |
| `sms-horario-de-last-chance` | 18h-19h vs 18h30-19h | conflito |
| `sms-horario-do-fim-da-tarde` | 17h nos dois; "400 p.m." só uma vez | conflito |
| `sms-auto-check-e-a-lei` | pré-marcar telefone e invocar a lei | conflito |
| `sms-benchmark-de-form` | → `list-growth-benchmark-de-form` | → slug |
| `sms-delay-do-popup` | → `list-growth-time-delay` | → slug |
| `sms-exit-intent` | → `list-growth-exit-intent` | → slug |

## entre módulos (slug próprio)

| Slug | Assunto | Tipo |
|---|---|---|
| `entre-modulos-tabela-de-metricas` | duas tabelas de metas em dois decks | conflito |

**Total após deduplicação: 126 entradas canônicas**, mais 16 slugs redundantes
que resolvem para elas.

---

# fundamentos

As quatro entradas `*-glossario` estão na seção
[[#Conflitos dentro do mesmo registro]], porque são slide contra slide no mesmo
deck. `fundamentos-o-que-move-o-open-rate` está em [[#Conflitos entre módulos]].

## fundamentos-roi-do-email

| Valor | Registro | Linha |
|---|---|---|
| "Email average is $36 plus in return for every $1 spent" | transcricao | L13 |
| "Email averages **$36+ return for every $1 spent**" | slide | L285 |
| "Email typically delivers ~40x ROI when done right" | slide (glossário) | L393 |

**Como responder:** **$36+ por $1** — duas ocorrências, dois registros, redação
quase idêntica. O 40x do glossário é uma terceira formulação sem fonte e com uma
condicional que as outras não têm ("when done right"). Nenhum dos três vem com
estudo citado. Se o número for usado, vá junto do contraste que ele faz na mesma
frase: anúncio devolve "2 to 3 dollar" e há marcas satisfeitas com 0.8 ROAS (L13).

## fundamentos-split-campanhas-flows

| Valor | Registro | Linha |
|---|---|---|
| "roughly 50% (…) 60/40, 40/60, depends on the brand a little bit. In general, you want to be around 50/50" | transcricao | L22 |
| "around 50/50 or 40/60, 60/40 anywhere in that range" | transcricao | L60 |
| "We want it to be 40 to 60% each so 40% campaigns, 60% flows. or 60% campaigns, 40% follows" | transcricao | L172-174 |
| "around 50% of your total email revenue with the other 50% coming from campaigns" | slide | L326 |
| "**Campaigns:** 40–60% of email revenue **Flows:** 40–60% of email revenue" | slide | L375 |

**Como responder:** o **centro é 50/50** e isso é unânime — está nos dois
registros e nas três falas. A divergência é na tolerância: "40/60 ou 60/40" (L22,
L60) descreve dois pontos discretos; "40 a 60% cada" (L172, L375) descreve um
intervalo contínuo. Não é a mesma afirmação, mas as duas produzem a mesma faixa
operacional. Dê o centro e a faixa, e diga que ele nunca formula isso duas vezes
do mesmo jeito. O critério de decisão **não é numérico**: "So it's going to take a
little bit of context" (L22). O uso prático é diagnóstico, não meta: 14% em flows
significa "the flows could use a lot of improvement" (L62).

## fundamentos-denominador-dos-80

| Valor | Denominador | Registro | Linha |
|---|---|---|---|
| "flows generating 80% of the total store revenue" | receita da **loja** | transcricao | L22 |
| "roughly 50% of your total email revenue" | receita de **email** | transcricao | L22 |
| "They should make up around 50% of your total email revenue" | receita de **email** | slide | L326 |

**Como responder:** as duas primeiras frases estão **na mesma linha do bruto** e
trocam de denominador no meio. O pilar #2 define flows como percentual da receita
de email; o caso extremo citado na frase seguinte é percentual da receita da loja.
80% da receita total da loja vindos de flows é um número extraordinário; 80% da
receita de email é apenas um desequilíbrio dentro do próprio modelo dele. **Não
escolher.** Cite a frase com o denominador que está escrito e sinalize que ela
contradiz a definição do pilar duas frases antes. Conflito irmão:
`flows-participacao-na-receita`.

## fundamentos-limiar-de-escalar-aquisicao

| Valor | Registro | Linha |
|---|---|---|
| "If you're over that, say you're at like 60 percent, that tells you, okay, let's funnel some of our profits back into paid ads" | transcricao | L56 |
| "If you get over 55%, you're kind of like at 60%, then it's like, okay, we need to scale our acquisition" | transcricao | L170 |
| "\>55% \= time to scale acquisition" | slide | L374 |

**Como responder:** **55%** — está no slide, que vence em especificação, e na fala
da aula de métricas. Os 60% do walkthrough não são erro: L170 mostra que na cabeça
dele os dois números são vizinhos. Dê 55% como gatilho e 60% como o exemplo que ele
usa. O racional é o mesmo nas duas versões e é o que importa: acima da faixa o
problema **não é o email**, é aquisição (L172).

## fundamentos-piso-de-email-share

| Valor | Registro | Linha |
|---|---|---|
| "If you're anywhere under 30%, um 40%, then that tells you, okay, our email systems can be improved" | transcricao | L56-58 |
| "if we have less than like 30% then we need to be doing better with our email marketing" | transcricao | L172 |
| "30–50% is healthy" | slide, transcricao | L374, L170 |

**Como responder:** **30%** é o piso, sustentado pela aula de métricas e pela faixa
saudável dos dois registros. O "under 30%, um 40%" de L56-58 é hesitação de fala:
ele começa em 30 e emenda 40 sem completar a frase. Não trate 40% como piso
alternativo — 40% é a **meta** (L168, L374, L388), não o piso.

## fundamentos-anuncios-por-dia

| Valor | Registro | Linha |
|---|---|---|
| "over 70 different e-commerce brand ads every single day" | transcricao | L9 |
| "70+ ecom ads per day" | slide | L252 |
| "this is, like, really low balling. I have some studies that say people see, like, 250" | transcricao | L9 |

**Como responder:** ele desmonta o próprio número na frase seguinte a dizê-lo. Dê
os dois: 70+ é o que vai no slide, 250 é o que ele diz acreditar, com a condição
"if you're on, like, a lower—lower demographic". Nenhum dos dois tem fonte citada
("I have some studies" não nomeia estudo nenhum). Se a pergunta depender do número
para uma decisão, diga que o corpus não sustenta nem um nem outro — a função do
dado no argumento dele é retórica, não analítica.

## fundamentos-formula-da-lucratividade

| Valor | Registro | Linha |
|---|---|---|
| "Increased Cost Per Acquisition x Lower LTV x Tariffs \= Lower Profitability" | slide | L268 |
| "increased cost per acquisition plus dec decrereased LTV plus tariffs, you got lower profitability" | transcricao | L9 |

**Como responder:** conflito de formulação, não de conclusão — mas registrado
porque produto e soma não são a mesma coisa e alguém pode citar a fórmula do slide
como se fosse modelo. Não é: nenhum dos três termos é quantificado em lugar nenhum
do corpus. Cite a versão do slide se o pedido for o artefato, a da fala se o pedido
for o raciocínio.

## fundamentos-smart-sending

| Valor | Registro | Linha |
|---|---|---|
| "skip recently emailed profiles, typically you want to send that off" — dito montando uma **campanha** | transcricao | L78 |
| "Smart Sending – Klaviyo feature that skips sending to people recently emailed. **Turn off for flows**\!" | slide (glossário) | L447 |

**Como responder:** os dois dizem para desligar; discordam sobre **onde**. A fala
está no meio do fluxo de criação de campanha e não menciona flows; o glossário
manda desligar em flows e não menciona campanhas — com exclamação, único item do
glossário inteiro com instrução imperativa. "send that off" em L78 é ruído de ASR
para *turn that off*. Responda: ele manda desligar nos dois contextos, cada um
registrado uma vez, e o corpus nunca trata os dois na mesma frase. Não infira uma
regra geral a partir das duas.

## fundamentos-benchmark-do-form

| Valor | Registro | Linha |
|---|---|---|
| "you want to shoot for six to 12% of your total **email revenue**" | transcricao | L104 |
| "or 6 to 12% of your total **site traffic**" — autocorreção na linha seguinte | transcricao | L106 |
| "6-12%" | slide | L380 |

**Como responder:** o denominador correto é **tráfego do site**, não receita de
email — ele se corrige sozinho em L106 e a aritmética que faz em seguida confirma
("if you have 1000 people viewing your site, you want to have at least 60 to, um,
120 people", L108). Trate L104 como lapso de fala, não como posição. A faixa 6-12%
em si tem escada própria e conflito próprio: ver `list-growth-benchmark-de-form`.
Nunca responda o 6-12% isolado.

## fundamentos-klaviyo-melhor-ou-pior

| Posição | Registro | Linha |
|---|---|---|
| "I highly recommend using Klaviyo. It is the best option (…) Klaviyo is just the best" — como **ESP** | transcricao | L32-34 |
| "I highly recommend Klaviyo, it is the best option" | slide | L357 |
| "but Clavio (…) It's just not going to perform as well" — como plataforma de **pop-up** | transcricao | L617 |
| "Oly is my recommended pop-up platform" | transcricao | L615 |
| "it's the superior option. It will always perform better" — sobre Alia | transcricao | L647 |
| "The most used eCommerce email platform, especially for Shopify" | slide (glossário) | L458 |

**Como responder:** não é contradição lógica — é stack de duas camadas, Klaviyo
como ESP e Alia como camada de pop-up — mas produz duas assinaturas pagas, e a
recomendação de fundamentos não avisa disso. Cite sempre as duas camadas juntas. O
único suporte factual que o corpus dá ao "it is the best option" é a linha do
glossário, e ela afirma **market share**, não qualidade. Conflitos irmãos:
`list-growth-alia-vs-klaviyo` e `design-klaviyo-vs-omnisend`. Os links de ESP são
de afiliado (L34, L358, L360) — declarar sempre.

## fundamentos-deliverability-e-facil

| Posição | Registro | Linha |
|---|---|---|
| "Deliverability is like a half. Just because it's so easy" | transcricao | L21 |
| "Why only a 3.5 pillar? Because it's easy\!" | slide | L348 |
| "with health and deliverability. This is where things get a little bit comm- complicated" | transcricao | L225 |
| "if you do struggle with it, that's what we will walk you through here in this program" | transcricao | L22 |

**Como responder:** as quatro linhas estão na mesma faixa, a 200 linhas de
distância. A tese do meio pilar é dele e é sustentada nos dois registros — mas a
condição que ele anexa ("as long as you only send to engaged profiles and send
good content", L349) é justamente o que o módulo de deliverability leva centenas de
linhas para ensinar, com rampa de warming, registros DNS e reparo. Responda: para
ele deliverability é meio pilar porque a **condição de sucesso é subproduto** dos
outros três, não porque o assunto seja simples — e ele próprio chama a terminologia
de complicada (L225) e abre exceção para quem já está em apuros (L22).
