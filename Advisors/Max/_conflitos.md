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

**Esta nota é a porta.** Ela contém o índice completo dos 126 slugs canônicos (mais os
16 redundantes e para onde apontam) e, na íntegra, as duas seções transversais —
[[#Conflitos entre módulos]] e [[#Conflitos dentro do mesmo registro]] —, que são as
que mais mudam resposta e as que o roteamento por pasta do [[_INDEX]] nunca entrega
sozinho. **As outras 108 entradas estão em [[_conflitos-completo]]**, agrupadas por
módulo, com o mesmo cabeçalho `## slug`.

**A regra de busca é uma só:** ache o slug no índice; se o `## slug` não estiver nesta
nota, ele está em [[_conflitos-completo]]. Não existe slug em lugar nenhum além destes
dois arquivos, e nenhuma entrada existe nos dois.

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
| `list-growth-time-delay` | oito formulações do delay do pop-up | conflito |
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
| `deliverability-limiar-de-open-rate` | doze formulações; o slide discorda de si | conflito (§ mesmo registro) |
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

**Onde cada uma vive:** as **18** entradas das duas seções transversais estão nesta
nota, logo abaixo do índice — sete em [[#Conflitos entre módulos]]
(`design-html-vs-imagem`, `sms-open-rate-de-email`, `entre-modulos-tabela-de-metricas`,
`doutrina-segundos-de-atencao`, `flows-onde-testar`, `fundamentos-o-que-move-o-open-rate`,
`sms-frequencia-de-email-comparada`) e onze em [[#Conflitos dentro do mesmo registro]]
(as quatro `fundamentos-*-glossario`, `deliverability-limiar-de-open-rate`,
`deliverability-unsubscribe-afeta-ou-nao`, `deliverability-registros-dns`,
`copy-numeracao-dos-principios`, `copy-takeaways-por-email`, `design-cta-por-produto`,
`otimizacao-sl-julgar-por-abertura-ou-receita`). **As outras 108 estão em
[[_conflitos-completo]]**, na seção do módulo indicada pelo título da tabela acima.

O marcador `(§ mesmo registro)` na coluna Tipo significa que o conflito é slide contra
slide e que a seção [[#Conflitos dentro do mesmo registro]] tem algo a dizer sobre ele
— **não** significa necessariamente que a entrada inteira more lá. Cinco entradas
marcadas assim (`welcome-contagem-de-fillers`, `list-growth-checkbox-preselecionado`,
`list-growth-friccao-na-signup-page`, `replenishment-desconto`,
`campanhas-cadencia-alta-vs-tier-1m`) têm a entrada completa em
[[_conflitos-completo]] e apenas uma linha de diagnóstico aqui.

---
# Conflitos entre módulos

Os que atravessam pastas. São os mais perigosos porque o roteamento do [[_INDEX]]
manda ler **uma** pasta: quem entra por `design/` nunca vê a versão de
`deliverability/`. Toda entrada aqui tem que ser lida antes de responder na pasta de
origem.

## design-html-vs-imagem

design (L8026) contra deliverability (L8500-8504). **As duas falas não têm o mesmo
dono:** L8026-8028 está no walkthrough de upload (L8009-8065), `max-provado`; já
L8500-8504 está em L8381-8646, `outro-provavel` por [[_autoria]] — **não é fala de
Max**. O conflito continua de pé como conflito do *corpus*, mas um dos lados não é
citável como fala dele.

| Versão | Valor | Registro | Linha |
|---|---|---|---|
| Não precisa de HTML nativo | "There's some rumor in the space, someone started it like 8 years ago, and maybe it had some truth then that you need to have like HTML sections in your email. You need to have native text sections and whatnot. But that couldn't be farther from the truth." | transcricao (design) | L8026 |
| Prova oferecida (fala de Max) | "Look at how little HTML there is in this email (…) don't think that you need to have native text native text sections" | transcricao (design) | L8027-8028 |
| Google não lê imagem | "Google can't properly scan the image-based emails, but it can scan any of the alternate text or the text kind of behind it that is in the email. And that's what we would call HTML. Google read HTML. Image-based emails have a lot less HTML." | **outro-narrador** (deliverability) | L8500 |
| Um mínimo de HTML é necessário | "However, if you at least have a base amount of HTML for people that can't open the images or for Google to read, that's where your alt text comes into play." | **outro-narrador** (deliverability) | L8502 |
| Algum HTML melhora a entrega | "making sure you're including different bits of HTML in your email **will include deliverability** because it'll show different things that Google wouldn't pick up on if it was an image-only email" | **outro-narrador** (deliverability) | L8504 |

**Como responder:** as duas afirmações **não se anulam se lidas com cuidado**, mas
se anulam se citadas isoladamente — que é exatamente o que o roteamento por pasta
provoca. A distinção que reconcilia: em L8026 **Max** nega que **seções de texto
nativo** sejam necessárias **para vender**; em L8500-8504 **o outro narrador** afirma
que **algum** HTML ajuda o Google a ler o email, ou seja, é argumento de
**deliverability**, não de conversão. São duas perguntas diferentes com a mesma
palavra.

A ponte oferecida é o **alt text**: é HTML, é passo obrigatório do
upload (L8052-8053, este narrado por Max; L8496 e L8502 são do outro narrador), e é o que preenche o "base amount". Nunca responda
"não precisa de HTML" sem o alt text junto, nem "precisa de HTML" sem dizer que Max
rejeita explicitamente seções de texto nativo. **O corpus não diz quanto é "a base
amount"** (L8502) — se perguntarem quanto HTML basta, a resposta é que o corpus não
quantifica em lugar nenhum. Nota de verbatim: "will include deliverability" (L8504) é o texto do
bruto; a leitura óbvia é *improve*, mas a correção não está no corpus e não deve ser
citada como se estivesse.

## sms-open-rate-de-email

O módulo de SMS benchmarka o open rate de email em 30%. Todo o resto do corpus exige
mais de 50%.

| Valor | Papel | Registro | Linha |
|---|---|---|---|
| "**SMS marketing messages have an average open rate of 98%** (email has an average open rate of **30%**)" | comparativo retórico | slide (SMS) | L9291 |
| "\| Open Rates \| **Greater than 50%** \|" | meta operacional | slide (deliverability) | L8715 |
| "Open Rates — 50%+" | tabela de metas | slide (fundamentos) | L376 |
| "we need to be above 50%. This is the only one where it's like, okay, if you're below 50%, you're fucking something up" | linha de corte | transcricao (fundamentos) | L178 |
| "you ideally want to be in that 50 to 60% range, but anything over 40% is okay" | tolerância | transcricao (campanhas) | L4236 |
| "Target: 45%+ for engaged segments" | glossário | slide (fundamentos) | L430 |

**Como responder:** são **coisas diferentes usadas como se fossem a mesma**. Os 30%
são média de mercado, citados uma única vez e com função retórica: fazer o 98% do SMS
parecer maior. Os 50%+ são a meta dele para as contas que gere, e ele a trata como
linha de corte, com a ênfase mais forte do módulo de fundamentos (L178). **Nunca cite
30% como benchmark de email do Max** — é o número contra o qual ele mede o mercado,
não a régua dele. Se a pergunta for sobre qual open rate perseguir, a entrada que vale
é `deliverability-limiar-de-open-rate`, e o piso de 40% aparece lá com contexto. Nota:
nenhuma das duas médias de mercado (30% de email, 98% de SMS) tem fonte citada no
corpus.

## entre-modulos-tabela-de-metricas

**Conflito novo, registrado nesta consolidação.** O corpus tem **duas tabelas de metas
de métricas**, em dois decks diferentes, e elas não batem. Nenhuma das duas unidades
de origem comparou uma com a outra.

| Métrica | fundamentos (L372-380) | deliverability (L8713-8719) | glossário (L428-438) |
|---|---|---|---|
| Open rate | "50%+" (L376) | "Greater than 50%" (L8715) | "Target: 45%+ for engaged segments" (L430) |
| Click rate | "0.5%+ on campaigns 2%+ on flows" (L377) | "Greater than 0.75%" (L8716) | "Target: 2–4%+" (L431) |
| Bounce rate | *ausente* | "Less than 1%" (L8717) | "Target: \<2%" (L437) |
| Spam complaint | "\<0.01%" (L379) | "Less than 0.01%" (L8718) | "Target: \<0.1%" (L438) |
| Unsubscribe | "\<0.3%" (L378) | "Less than 0.4%" (L8719) | "Target: \<0.2%" (L436) |

**Como responder:** as duas tabelas **concordam em dois pontos e divergem em três**.

- **Concordam:** open rate (>50%) e spam complaint (<0,01%). Esses dois números são os
  mais sólidos do corpus inteiro — dois decks e a fala (L178, L192).
- **Divergem em click rate:** fundamentos separa por tipo de envio (0,5% campanha, 2%
  flow) e dá o motivo — "flows are higher converting, and they're more intent based"
  (L184); deliverability dá um número único e achatado (0,75%), que não é nem um nem
  outro; o glossário dá 2-4%+ sem distinguir; e a fala de campanhas dá ainda "somewhere
  between one and 3%" (L4236). **Quatro versões.** Responda com a separação de
  fundamentos, porque é a única que traz racional, e nomeie as outras.
- **Divergem em unsubscribe:** 0,3% (fundamentos, L378, e a fala três vezes em
  L186-190) contra 0,4% (deliverability, L8719) contra 0,2% (glossário, L436). **Vale
  0,3%** — é o valor mais repetido do corpus e o único com fala sustentando. O 0,4%
  aparece uma vez, na tabela do deck de deliverability, e vem colado ao rótulo
  "(doesn't affect deliverability)" — ver `deliverability-unsubscribe-afeta-ou-nao`.
- **Bounce rate só existe fora da tabela de fundamentos**, e as duas fontes que o dão
  divergem por 2x: 1% (L8717) contra 2% (L437). Vale 1%, pela mesma regra que desqualifica
  o glossário (ver [[#Conflitos dentro do mesmo registro]]).

**Nunca componha uma tabela única a partir das três.** Se a pergunta for "quais são as
metas", a resposta diz qual tabela está sendo citada e por quê. A tabela de fundamentos
é a que ele defendeu linha por linha na fala (L168-194); a de deliverability é a que
vale dentro do contexto de entrega.

## doutrina-segundos-de-atencao

Absorve `copy-janela-de-atencao` e `design-segundos-de-atencao`. A janela de atenção
tem **três valores diferentes**, divididos por módulo.

**Hoje:**

| Valor | Registro | Linha |
|---|---|---|
| "In 2025/2026, you *maybe* have 3 seconds" | slide (campanhas) | L5501 |
| "Todat, you *maybe* have 3 seconds" | slide (copy) | L6517 |
| "~3 seconds to hook your reader. Eliminate fluff." | resumo do módulo (copy) | L5605 |
| "if they can't skim it in 3 seconds, it won't get read" | slide (campanhas) | L5508 |
| "now you have about three" | transcricao (campanhas) | L4705 |
| "the first two to three seconds" | transcricao (campanhas) | L4707 |
| "attention spans that are really three seconds" | transcricao (copy) | L5891 |
| "you literally have two to four seconds to get your point across" | transcricao (design) | L7161 |
| "On average you have **2-4 seconds** to get your point across." | slide (design) | L8185 |
| "If we only get **3 seconds** of our viewers attention" | slide (design) | L8201 |

**Antes:**

| Valor | Registro | Linha |
|---|---|---|
| "Before, you could have had an average of **5-10 seconds** of attention per email." | slide (campanhas) | L5500 |
| "Before, you could have had an average of **5-10 seconds** of attention per email." | slide (copy) | L6516 |
| "before five, 10 seconds per email" | transcricao (campanhas) | L4703 |
| "used to be **three to five**, five to 10 maybe" | transcricao (copy) | L5891 |

**Como responder:** três valores para a mesma janela — 3 segundos, 2-3 segundos e 2-4
segundos. A divisão é quase limpa por módulo: **copy diz 3; design diz 2-4; campanhas
diz 3 no slide (L5501, L5508) e na fala (L4705), mas a mesma fala emenda "two to three"
duas linhas depois (L4707)** — o 2-3 tem uma única ocorrência e ela está em campanhas.
Fora dessa emenda, a fala e o slide de cada módulo concordam entre si. Não é contradição
de registro, é contradição entre aulas. Nenhuma versão traz fonte, e duas trazem o
hedge "maybe" escrito por ele (L5501, L6517). A resposta honesta é dar a faixa completa
**2-4** e dizer de qual aula veio cada ponta. O "3 seconds" de L8201 é paráfrase interna
do próprio deck de design 16 linhas depois de L8185, dentro da faixa — não é quarto
valor independente.

**O "antes" também diverge, e isso é uma correção feita nesta consolidação.** Três
registros dizem 5-10 segundos (L4703, L5500, L6516), mas L5891 oferece "three to five"
como alternativa na mesma frase. Dê os dois valores do "antes" e não converta em faixa
única. Ressalva de atribuição: L5891 está no bloco L5867-6082 ("Utilizing
Infographics"), classificado `outro-provavel` por [[_autoria]] — **a única versão que
quebra o consenso de 5-10 é a de atribuição mais fraca**. O número que importa
operacionalmente é o de hoje, e é ele que está em disputa entre módulos.

## flows-onde-testar

Absorve `otimizacao-onde-testar`. As duas posições estão na **mesma página do mesmo
deck**, doze linhas de distância — e a segunda tem cópia idêntica no deck de
otimização.

| Posição | Verbatim | Registro | Linha |
|---|---|---|---|
| tirar o teste do flow | "Rather than have a ton of active tests in flows of all sorts of different triggers, trying out different **content**, etc / We mostly use campaigns as our testing ground. / Try new angles and A/B test frequently in your email blasts. / Rather than waiting for results like you have to do in flows, you can get near instant data with campaigns." | slide (deck de flows) | L4128-4131 |
| o motivo | "Considering you can have 30-50+ automated emails… It's overwhelming / Hard to monitor at scale / Difficult to track and report at scale / Documenting is difficult" | slide (deck de flows) | L4119-4124 |
| o que fazer com o vencedor | "We literally put full campaigns that perform well into our flows. / Go back and edit your flow emails across all triggers to include the angle you saw work." | slide (deck de flows) | L4132-4133 |
| testar dentro do flow | heading "**Flow Specific A/B Tests**" | slide (deck de flows) | L4139 |
| testar dentro do flow | "**Flow Time Delays** — This is the biggest lever I'd say. Testing the amount of time from the action of the customer and the first email they receive. Then also, the time delay between your flow messages." | slide (deck de flows) | L4141-4145 |
| testar dentro do flow | mesma frase, palavra por palavra | slide (deck de otimização) | L9176-9180 |

**Como responder:** não é contradição de valor, é **divisão de escopo — e o deck a
sinaliza duas vezes, ainda que nunca a formule numa frase só.** As duas âncoras que as
notas de origem tinham subestimado:

1. **L4128 nomeia o que sai do flow: "trying out different *content*".** A frase não
   diz "tirem os testes dos flows"; diz que não se deve manter muito teste de
   **conteúdo** ativo dentro deles, e o motivo dado logo acima é de escala e
   monitoramento (L4119-4124), não de mérito.
2. **L4139 é um heading que diz "Flow Specific A/B Tests"**, e é sob ele que o teste de
   delay aparece (L4141-4145). O deck classifica explicitamente esse teste como
   específico de flow.

Ou seja: **conteúdo se testa em campanha e migra pronto para o flow** (é literalmente o
que L4132-4133 mandam fazer); **timing só pode ser testado no flow**, porque não existe
delay em campanha. Ofereça essa leitura como leitura — o corpus **não a enuncia em uma
frase** —, mas **não diga que "o corpus nunca faz essa distinção"**: ele a faz duas
vezes, na palavra "content" (L4128) e no heading "Flow Specific" (L4139). O que falta é
a frase que amarra, não a evidência.

Registre também que "the biggest lever" (L4143) tem cópia idêntica no deck de
otimização (L9178), o que **não** o torna duas fontes: é o mesmo slide reaproveitado.
Ver `otimizacao-deck-duplicado`.

## Os que atravessam pastas e estão registrados no módulo dono

Pontas soltas que exigem leitura cruzada, mas cuja entrada canônica vive na pasta que
possui o assunto:

| Assunto | Módulos que discordam | Slug canônico |
|---|---|---|
| Cadência de campanha | campanhas (2-4x, 3x) · otimização (3-4x como pré-condição) · deliverability (3-4x, L8557) · SMS (4-5x, 4x — comparativos) · flows (3-4x, 3x) | `campanhas-sweet-spot-de-frequencia` + `otimizacao-frequencia-precondicao` + `sms-frequencia-de-email-comparada` |
| Benchmark do pop-up | fundamentos (6-12%) · list-growth (a escada) · SMS (2-3% / 8-10%) | `list-growth-benchmark-de-form` (+ `fundamentos-benchmark-do-form` para o denominador) |
| Delay do pop-up | fundamentos (4-6s) · list-growth (4-12s, 4-8s, 5s) · SMS (6-10s) | `list-growth-time-delay` |
| Exit intent | list-growth (rejeição geral, rejeição no mobile) · SMS (rejeição sem qualificar) | `list-growth-exit-intent` |
| Subject line move ou não o open rate | fundamentos (L180: não move) · copy (5-15%) · otimização (5-10%) | `fundamentos-o-que-move-o-open-rate` + `copy-open-rate-limite` |
| Stack de ferramentas | fundamentos (Klaviyo é o melhor) · list-growth (Klaviyo não performa em form; Alia é superior) · design (título Klaviyo, demo Omnisend) | `fundamentos-klaviyo-melhor-ou-pior` + `list-growth-alia-vs-klaviyo` + `design-klaviyo-vs-omnisend` |
| Denominador da receita de flows | fundamentos (loja vs email, mesma linha) · flows (20% loja vs 50% email) | `fundamentos-denominador-dos-80` + `flows-participacao-na-receita` |
| Definição do winback | flows (sem o teto de 150 dias) · campanhas (150/90 completo) | `winback-definicao-do-segmento` + `campanhas-winback-janela` |
| Janela da lista base | campanhas (90) · deliverability (90 no slide, 60 na fala) | `campanhas-janela-de-engajamento` + `deliverability-lista-base-padrao` |
| Checkbox pré-marcado do Shopify | list-growth (texto que se anula) · SMS (procedimento de email sob título de SMS) | `list-growth-checkbox-preselecionado` + `sms-instrucoes-de-optin-sao-de-email` |
| Grafia de nomes de marca | doutrina · design · copy | `doutrina-lista-de-marcas` |
| Credencial de receita | doutrina ($40M, $100M) · flows ($100M, $200M) · campanhas ($200M) | `doutrina-receita-da-agencia` |

## fundamentos-o-que-move-o-open-rate

| Posição | Registro | Linha |
|---|---|---|
| "It's not your subject line or preview text. It is your segmentation (…) they're going to open your email, **no matter what your subject line says**" | transcricao (fundamentos) | L180 |
| "at most you can get ~ 10% jump in opens" | slide (copy) | L6805 |
| "The biggest open rate difference we've had on an A-B test is… 10%, maybe 15" | transcricao (copy) | L6227-6229 |
| "our best, our best subject line and preview text, you maybe see a five, 10% bump in open rates" | transcricao (otimização) | L8934-8936 |
| "people should open your emails based off your sender name, NOT your Subject line" | resumo do módulo (copy) | L6093 |

**Como responder:** não é contradição frontal — 10 a 15 pontos não tiram uma conta de
30% para 50%, então "o conserto é segmentação" continua de pé **como prioridade**. Mas
a negação de L180 é **absoluta** e o resto do corpus não é: em três lugares ele
quantifica o efeito de subject line sobre abertura. Responda na ordem: primeiro
segmentação, que é o que ele manda consertar; depois o teto de 5-15% que copy adiciona.
**Nunca cite L180 sozinho para afirmar que subject line não importa** — ele dedica um
módulo inteiro a subject lines. Ver `copy-open-rate-limite` e
`otimizacao-sl-julgar-por-abertura-ou-receita`.

## sms-frequencia-de-email-comparada

| Valor | Registro | Linha |
|---|---|---|
| Email: "four to five messages a week" sem backlash | transcricao (SMS) | L9226 |
| Email: "With email you can easily send 4-5 email campaigns per week without getting much backlash" | slide (SMS) | L9364 |
| Email: "like four times a week" | transcricao (SMS) | L9248 |
| Email: "we see the best results and engagement sending 4x per week (every other day)" | slide (SMS) | L9490 |
| Email: tabela por faturamento, 2x a 5-6x/semana | slide (campanhas) | L5295-5298 |
| Email: "two to four times per week is really hitting the sweet spot" | transcricao (campanhas) | L4242 |

**Como responder:** os números de email citados **dentro do módulo de SMS** são
comparativos de argumento, não a especificação de email — existem para dizer que SMS é
menos. A especificação está no módulo de campanhas, que decide por tier de faturamento
ou tráfego (L5295-5298) e cujo sweet spot declarado é 2-4x (L4242) ou 3x (L5255).
**Nunca responda "4-5 por semana" citando L9226/L9364.** Note que 4-5x e "4x every
other day" também estouram a faixa 2-4 do módulo dono — é o mesmo tipo de atrito
registrado em `campanhas-cadencia-alta-vs-tier-1m`, e o corpus não o comenta.

---

# Conflitos dentro do mesmo registro

A precedência do [[_INDEX]] — slide vence em especificação, fala vence em julgamento —
só funciona quando os **dois registros discordam entre si**. Boa parte dos conflitos
deste corpus é slide contra slide, no mesmo deck, às vezes na mesma linha. Aqui a
precedência não resolve, e o desempate, quando existe, é por **evidência de autoria
dentro do próprio material**.

**Consequência geral: não presuma que o slide fala com uma voz só.**

## A tabela de metas contra o glossário — quatro divergências, uma de dez vezes

Mesmo deck de fundamentos. A tabela está em L372-380; o glossário, em L384-519. Quatro
métricas divergem.

| Métrica | Tabela de metas (L372-380) | Glossário (L384-519) | Diferença |
|---|---|---|---|
| Open rate | "50%+" (L376) | "Target: 45%+ **for engaged segments**" (L430) | 5 pontos, e o glossário qualifica |
| Click rate | "In general: 0.5%+ on campaigns 2%+ on flows" (L377) | "Target: 2–4%+" — sem distinguir (L431) | 4x a 8x o alvo de campanha |
| Unsubscribe | "\<0.3%" (L378) | "Target: \<0.2%" (L436) | glossário é mais estrito |
| Spam complaint | "\<0.01%" (L379) | "Target: \<0.1%" (L438) | **dez vezes** |

**O desempate, e por que ele existe aqui:** em **L217** ele declara que vai pular o
glossário — "So I am going to gloss over this glossary, I'm going to be gloss over-ing
this email marketing glossary in key terms. You can use these if you want" — enquanto a
tabela de metas ele defendeu linha por linha na fala, com racional, em L168-194. **A
tabela é material que ele sustentou; o glossário é material que ele entregou.** Onde os
dois divergem, vale a tabela.

**Como responder, por slug:**

- **`fundamentos-open-rate-glossario`** — **50%** é a posição sustentada: está na fala
  com a ênfase mais forte do módulo inteiro ("if you're below 50%, you're fucking
  something up", L178) e na tabela. Os 45% aparecem uma vez, sem fala. Mas há um detalhe
  que não é ruído: o glossário **qualifica** o alvo ("for engaged segments") e a tabela
  não qualifica nada. Se a pergunta for sobre segmento engajado, diga que existem dois
  números e que o mais exigente é o que ele defendeu. **Nunca responda "47,5%".** Se a
  pergunta for sobre warming ou alargamento de lista, a entrada que vale é
  `deliverability-limiar-de-open-rate`, não esta.
- **`fundamentos-unsubscribe-glossario`** — **0,3%**. É o valor mais repetido do módulo:
  ele o diz três vezes seguidas (L186, L188, L190) e no meio disso corrige o próprio
  slide ao vivo porque a tela mostrava o inverso do que ele queria dizer, sem detalhar o
  quê ("that should be the other way around (…) let me actually fix that right now",
  L188). O 0,2% do glossário não tem defesa falada. O diagnóstico associado vale para os
  dois: muitos unsubscribes = problema de conteúdo (L190). Há ainda uma terceira versão,
  0,4%, no outro deck — ver `entre-modulos-tabela-de-metricas`.
- **`fundamentos-spam-glossario`** — **o conflito mais grave da pasta em consequência
  prática.** 0,1% é **dez vezes** mais permissivo que 0,01%, e é a diferença entre uma
  conta saudável e uma conta em risco de bloqueio. **0,01%** é a posição sustentada —
  fala (L192), tabela (L379) e a tabela de deliverability (L8718) concordam. Dê o 0,1%
  do glossário apenas como registro divergente, **nunca como faixa** ("entre 0,01 e
  0,1%" seria a média inventada mais perigosa deste corpus). Diagnóstico associado: "you
  have a content problem, potentially a segmentation problem" (L192) — note a hesitação
  dele no segundo termo.
- **`fundamentos-click-rate-glossario`** — o conflito não é só de número, é de
  **estrutura**. Fala e tabela separam por tipo de envio e dão o motivo — "flows are
  higher converting, and they're more intent based" (L184). O glossário dá um número
  único, quatro a oito vezes maior que o alvo de campanha. Responda com a separação:
  0,5% em campanhas, 2% em flows, e cite que o glossário registra 2-4%+ achatado.
  Acrescente a tolerância declarada dele: 1% em campanha ele já considera doente ("I
  don't feel like that's healthy", L186), e ele mesmo diz que o número é frouxo ("it's
  really hard to say", L186). Há uma quinta e uma sexta versão fora do deck — ver
  `entre-modulos-tabela-de-metricas`.

Uma métrica **não** diverge e não deve ser apresentada como se divergisse: email share,
"40% (Goal)" na tabela (L374) e "Target is ~40%" no glossário (L388).

## O deck de deliverability dá três números de open rate em quatro linhas

`deliverability-limiar-de-open-rate` — **doze formulações**, sete na fala e cinco no
slide. É o número que decide qual lista usar e quando alargá-la.

| Valor | Contexto | Registro | Linha |
|---|---|---|---|
| "above 50%. 50% to 70% is ideal. If you're above 40%, you're probably okay" | meta geral | transcricao | L8436 |
| "consistently receiving 50 to 60% opens" | saber se a lista está certa | transcricao | L8468 |
| "ideally 50 plus open rates and then you know you're good to jump to a wider segment" | **a "golden rule"** do warming | transcricao | L8579 |
| "anywhere between 40 to 50 percent. If it starts dipping below 40, I definitely wouldn't be expanding it" | tolerância, **linha seguinte** | transcricao | L8580 |
| "you're hitting, again, 45 to 50% plus (…) that's a good indicator that we can expand" | expandir de 14 para 30 dias | transcricao | L8582 |
| "as long as you're hitting those, those 40 to 50% open rates" | cadência de rampa | transcricao | L8588 |
| "And that keeps us at a 40 to 50% mark" | após recuar de 30→60 para 30→45 | transcricao | L8604 |
| "This is how we can get consistent **50%** open rates" | o que enviar só para engajados entrega | **slide** | L8725 |
| "Whatever list gets you **50-60%** opens" | escolha da lista, **duas linhas depois** | **slide** | L8727 |
| "If you start to get **60%+** opens, widen your list to a larger timeframe" | **alargar**, **três linhas depois** | **slide** | L8728 |
| "If you start to get 40% opens, tighten your list to a smaller timeframe" | apertar | **slide** | L8729 |
| "\| Open Rates \| Greater than 50% \|" | tabela de metas do mesmo deck | **slide** | L8715 |

Duas adjacências agravam o conflito e são a prova de que ele não é artefato de recorte:

- **L8579 e L8580 são linhas consecutivas** e já discordam entre si: "50 plus" vira "40
  a 50" na frase imediatamente seguinte, dentro da mesma respiração.
- **L8725, L8727 e L8728 estão no mesmo slide**, a uma e duas linhas de distância: o
  slide promete "consistent 50%", manda escolher a lista por "50-60%" e depois exige
  "60%+" para alargar. **O registro que vence em especificação pelo protocolo tem três
  números em quatro linhas.**

**Como responder:** dê os valores todos, na ordem em que aparecem, e nomeie os dois
pontos em que **nenhuma das formulações contradiz as outras**: (a) **abaixo de 40%
nunca se alarga** (L8580; L8729 e L8470 mandam apertar em 40%); (b) o alvo de operação
é `Greater than 50%` (L8715). O slide é o mais exigente na hora de alargar — 60%+
(L8728) — **mas não é um bloco coerente**. Aqui não existe material sustentado contra
material entregue, como no caso do glossário: é a mesma tela. **Não há desempate.**

Se a pergunta for "posso alargar com 45%?", a resposta honesta é: pelo gatilho do slide
não (60%+), pela fala talvez (L8582 diz 45-50+), e ele nunca reconcilia. O critério de
segurança que ele próprio dá não é numérico — "I always err on the side of caution"
(L8569) e "it's much easier to build your sender reputation (…) than it is to fix it
when it's already in a poor position" (L8555). **Na dúvida, o número mais alto.**

## Os demais conflitos slide-contra-slide

Vivem no bloco do módulo dono; listados aqui porque a precedência do [[_INDEX]] não os
resolve e o diagnóstico é o mesmo.

| Slug | O defeito | Linhas | Desempate disponível |
|---|---|---|---|
| `deliverability-unsubscribe-afeta-ou-nao` | o rótulo da linha diz "(doesn't affect deliverability)" e a mesma tabela lhe dá meta; três linhas antes ele está na lista do que "Google, Yahoo, etc look at" | L8706-8710, L8719 | fala (L8432) confirma "neutral metric" → é métrica de **monitoramento com alvo**, não de deliverability |
| `campanhas-cadencia-alta-vs-tier-1m` | 5-7x/semana listado como faixa danosa, 5-6x/semana prescrito para $1M+/mês | L5264-5269 vs L5298 | **nenhum dentro do deck**; a reconciliação existe só na fala (L4240, L4270-4276), e essa fala é `outro-provavel` |
| `copy-numeracao-dos-principios` | dois "Principle #2" e nenhum "#3" | L6578, L6604, L6625 | o acrônimo, dado certo três vezes (L6558-6576, L5504-5512, L4715-4717) → Engaging é o terceiro; o "#2" de L6625 é erro do slide |
| `copy-takeaways-por-email` | heading "Limit to 1-3 Key Points Per Email" contrariado pelo corpo duas linhas abaixo | L6615 vs L6617-6618 | corpo vence: "1" aparece três vezes (L5611, L6547, L6617); a única concessão é "When you can", que não define quando |
| `welcome-contagem-de-fillers` | heading "Insert 1-4 Filler Emails" contra o corpo "the 1–5 educational emails" | L3544 vs L3547 | corpo vence: 1-5 em três lugares (L1612, L2178, L3517) |
| `design-cta-por-produto` | a lista de regras exige botão, a página da seção aceita alternativa | L8139 vs L8282 | fala (L7458) é categórica e traz teste: "Every single time I test this if you let people know shop now… then it gets higher clicks" (L7462) → **botão** |
| `design-segundos-de-atencao` (parte) | "2-4 seconds" e "3 seconds" no mesmo deck, 16 linhas de distância | L8185 vs L8201 | L8201 é paráfrase dentro da faixa, não valor independente |
| `list-growth-tipos-de-form` | slide promete "one of the 5 form types", corpus nomeia quatro | L1200 vs L1292-1298 | fala (L998) conta quatro; o próprio slide de exemplos repete um card e omite spin-to-win |
| `list-growth-checkbox-preselecionado` | a segunda metade da linha anula a primeira | L1120 | intenção declarada (L537, L1115) → auto-marcado; o texto é colado do Shopify e não foi revisado |
| `list-growth-friccao-na-signup-page` | "Remove as much friction as possible!" e, sete linhas depois, "enter a short description" | L1127 vs L1134 | fala vence (é julgamento): headline é o desconto (L547-549) |
| `replenishment-desconto` | "without heavy discounts" e "15% Off Your Next Refill!" **dentro de cada registro** | L3992/L3247 vs L4035-4037/L3299 | nenhum; a conciliação possível é que o desconto entra só no email 2, marcado opcional (L3269) |
| `otimizacao-sl-julgar-por-abertura-ou-receita` | "Not about your open rates" e, seis linhas depois, "track open rates" | L6085 vs L6091 | receita: sustentada no deck (L6810), na fala (L6229-6233, L8926-8944) e nos dados (L6127-6139). L6091 é resumo mal feito da página do curso |
| `deliverability-registros-dns` | quatro registros na prosa, três na lista de requisitos | L8671 vs L8687-8689 | nenhum; **SPF, DMARC, DKIM** são requisito declarado, o MX aparece uma vez na prosa. Não afirme que o MX é dispensável nem obrigatório |
| `welcome-estrutura-da-sequencia` | o slide promete "**Base Strategy:**" e não entrega nada | L3509 | nenhum; o diagrama não sobreviveu à extração |
| `winback-definicao-do-segmento` | o slide promete a definição do segmento e entrega slot vazio | L4057 | a definição completa está no deck de campanhas (L5589) |
| `design-metodos-de-transicao-ausentes` | "Here are a few methods to do this:" seguido de nada | L8307 | os quatro métodos existem só na fala (L7552-7586) |
| `flows-receita-da-agencia` (→ `doutrina-receita-da-agencia`) | $100M e $200M no mesmo deck, nove linhas de distância | L3419 vs L3428 | nenhum; o segundo está num bloco de recomendação paga do Klaviyo |

---

---

# As outras 108 entradas

Estão em [[_conflitos-completo]], agrupadas por módulo na mesma ordem do índice acima:
fundamentos · doutrina · list-growth · flows · campanhas · copy · design ·
deliverability · otimização · sms. O registro de auditoria da consolidação — as 15
colisões de slug, os dois veredictos arbitrados e o que parece conflito e não é —
também está lá, no fim.
