---
tipo: teste-ab
marca: Treuquell
canal: popup
plataforma: Omnisend
status: draft-aguardando-start
criado: 2026-09-08
base: "[[list-growth/os-sete-testes-de-form]], [[list-growth/os-tipos-de-form]], [[list-growth/alia-e-a-alternativa]]"
---

# Teste 4 — QUIZ vs ROLETA

Alavanca **#2 de Max** (*Form Type*), a maior ainda não testada nesta conta.
Base doutrinária: [[os-tipos-de-form]] ("o quiz em 2026 é o melhor form que você
pode rodar") + o mecanismo central da Alia, que roda quiz em quase todos os
templates ("most of these are running quizzes because they perform the best",
[[alia-e-a-alternativa]]).

## Histórico — o que já sabemos desta conta

Taxa = submits / views. Números do endpoint `ab-setup/reports`.

| # | Período | Variante A | Variante B | Vencedor |
|---|---|---|---|---|
| 1 | 01–19/ago | Desconto misterioso — **0,39 %** (34/8830) | Oferta direta 10 % — **0,55 %** (50/9083) | **B** — oferta direta |
| 2 | 19–26/ago | Popup clássico 10 % — **0,60 %** (14/2338) | Roleta 10 % — **1,07 %** (25/2342) | **B** — roleta (+78 %) |
| 3 | 26/ago–08/set | Roleta 2 campos — **0,94 %** (14/1491) | Roleta 1 campo — **1,92 %** (26/1352) | **B** — 1 campo (+105 %) |

**Encerrado hoje:** teste 3, com B declarado vencedor. z = 2,23 · p = 0,026
(significativo a 95 %). Confirma o item 1 do [[checklist-do-form]]: *only asks
for one input per step*.

**Contradição registrada:** o teste 1 derruba o "mystery discount" que Max
recomenda como bônus em [[a-oferta-e-o-componente-principal]]. Nesta conta,
oferta explícita ganhou. O próprio corpus manda respeitar isso — "the results
based off a certain A-B test are going to be different based off your brand"
([[quando-vale-testar]]).

## O gap que importa

Melhor taxa atual: **1,92 %**. Benchmark de Max: **6–12 %**, mínimo 6 %
([[por-que-o-popup-decide]]). Ainda estamos a ~3x do piso. Há espaço para
várias rodadas — a curva dele é serrilhada, não escada.

## A hipótese

> Trocar a roleta por um quiz de 2 passos aumenta a taxa de submit, porque
> soma **commitment bias** (a pessoa já agiu antes de dar o e-mail) a
> **personalization bias** (a oferta parece feita para ela), enquanto a roleta
> entrega só novidade — e novidade satura.

Contra-hipótese honesta: a roleta ganhou de lavada no teste 2 justamente pelo
apelo de jogo, e o quiz adiciona um passo antes do e-mail. Pode perder.

## As duas variantes

**Terceira versão do design.** As duas primeiras foram reprovadas: caixa de
350 px sem imagem, e depois Montserrat + dourado + faixa branca quebrada.

O que estava errado, e a correção:

| Erro | Correção |
|---|---|
| Montserrat (geométrica, larga, ruim em corpo pequeno) | **Open Sans** — humanista, a mais próxima da **Assistant**, que é a fonte real de treuquell.de. Assistant não existe na lista do Omnisend. |
| Dourado `#E0A82E` como cor principal | Branco sobre `#121212` — o preto real do site. Dourado sobra só no link legal. |
| Bloco de imagem em seção própria → **faixa branca gigante** | O bloco de imagem do Omnisend falhou. Trocado por `generalSettings.backgroundImage` com `position: top`, `fit: cover`, `size: 168px` — mecanismo nativo, caminho diferente. |
| Sem hierarquia, tudo competindo | Foto (168 px) → wordmark → "Sie haben" 20 px → **10 % RABATT 40 px** → pergunta 14 px → botões → recusa 11 px. |

Casca compartilhada, idêntica nas duas:

| Elemento | Valor |
|---|---|
| Largura / raio | 400 px, raio 4 px |
| Fundo | `#121212` (preto do site) |
| Fonte | Open Sans, Helvetica Neue, Helvetica, Arial |
| Hero | banner da home no topo, 168 px, `fit: cover` |
| Escolhas do quiz | pill vazada, borda `#6E6E6E`, texto branco 15 px |
| CTA | pill branca sólida, texto `#121212` 15 px bold |
| Recusa | 11 px `#6E6E6E` sublinhado |
| Gatilho | 12 s + scroll 70 % + exit intent, 1×/dia, exclui /cart e /checkout |

Descartados: o logo do site (preto sobre branco — vira barra branca no escuro) e
as fotos de produto (trazem a marca **KLARWEN**, do fornecedor, impressa).

**Só o mecanismo muda entre A e B.**

### A — CONTROLE (roleta, 1 campo)
Foto · wordmark · "Sie haben" · **10 % RABATT** · roleta 58 % em branco/cinza
(sem dourado) · "E-Mail eingeben und drehen" · e-mail · **RAD DREHEN** · recusa
· legal. Sucesso: "10 % gewonnen". Tags: `form_subscriber`, `wheel_10`.

### B — QUIZ (2 passos)
**Passo 1** (nenhum campo): foto · wordmark · "Sie haben" · **10 % RABATT** ·
**Wofür shoppen Sie heute?** · três pills com as coleções reais da loja
(`Werkzeuge & Haushalt`, `Beleuchtung & Energie`, `Garten & Reinigung`) · recusa.
**Passo 2** (um input): "Fast geschafft" · **10 % RABATT** · "Wohin schicken wir
Ihren Code?" · e-mail · **RABATT SICHERN** · recusa · legal.
Sucesso: "Willkommen an Bord". Tags: `form_subscriber`, `quiz_10`.

Copy ancorada em [[copy-do-form]]: "Sie haben 10 % Rabatt" é o *"You've got 10%
off"* (posse + loss aversion); "Wofür shoppen Sie heute?" é o *"tell us what
you're shopping for"*; **RABATT SICHERN** é o *"Claim now"*, nunca *"Continue"*.

**Pendência:** confirmar no painel se a foto de fundo renderiza. A imagem subida
pela API (`6aa093bc97f14cdaac6b0953`) serve 1×1 px quando acessada direto; se
aparecer em branco, subir a foto pelo painel e trocar o id.

**O botão de recusa entrou nas duas** — alavanca #3 de Max ("Always performs
better", [[checklist-do-form]]); como está nas duas, não contamina. O X continua
visível nas duas.

> **Atenção na leitura dos números.** A casca mudou nas duas variantes, então a
> taxa absoluta deste teste **não é comparável** com os 1,92 % do teste 3. Só o
> delta A × B deste teste é leitura válida.

## Limitação conhecida — segmentação

Max e a Alia vendem o quiz também pelo dado: a resposta vira profile property e
segmenta os e-mails seguintes ([[segmentacao-vinda-do-form]]). **A API do
Omnisend não permite isso aqui:** `isMappedToCustomProperty` é aceito apenas em
botões `submit`, e os botões de resposta do passo 1 precisam ser `nextStep`.
Tentativa registrada — erro 400, `invalid_value`.

Consequência: neste teste o quiz roda **sem capturar a resposta**. Duas saídas,
se ele vencer:
1. trocar os três botões por um `radioField` com `customProfileField` + botão
   "WEITER" — captura o dado, custa um clique a mais (e o clique a mais é
   exatamente o que estamos otimizando);
2. medir esse custo como o teste seguinte: quiz-botões vs quiz-radio.

## Critério de decisão

**Métrica primária:** submits / views. Secundária: signups (opt-ins confirmados).

Amostra necessária por variante (α = 0,05 bicaudal, poder 80 %, base 1,92 %):

| Lift que se quer detectar | Views por variante | Dias no tráfego atual (~110 views/variante/dia) |
|---|---|---|
| +100 % (→ 3,84 %) | ~1.190 | **~11 dias** |
| +50 % (→ 2,88 %) | ~3.980 | ~36 dias |

**Mínimo: 14 dias.** Bate com a cadência que Max prescreve — "at least for like
bi-weekly" ([[os-sete-testes-de-form]]). Se a diferença ficar abaixo de +50 %,
o teste não conclui em tempo útil: registrar como empate e seguir para a próxima
alavanca, sem forçar leitura.

Regra de conclusividade dele é repetição, não tempo ([[quando-vale-testar]]):
se der um resultado apertado, rodar de novo antes de mudar o form principal.

## Fila dos próximos testes

Ordem de alavanca de [[os-sete-testes-de-form]], descontando o que já rodou:

1. **Esconder o X** (resto da alavanca #3). O botão de recusa já entrou nas
   duas variantes deste teste; falta testar **X visível contra X escondido**,
   forçando a decisão pelo botão. Max: *"Hide that X (…) Always performs
   better"*.
2. **Gatilho** (alavanca #4, nunca testada). Hoje: 12 s + scroll 70 % + exit
   intent. Testar contra **4 s**, que é o único valor comum às três faixas do
   corpus. Critério: **submits totais, não taxa**.
3. **Oferta** (alavanca #1). AOV da loja é ~€20–50, abaixo do corte de $100 →
   **% OFF é o formato certo** ([[a-oferta-e-o-componente-principal]]). O que
   falta testar não é o formato, é o valor (10 % vs 15 %) e o frete grátis.
4. **Foto** (alavanca #5). As duas variantes agora usam o mesmo banner da home.
   Testar contra foto de produto, ou foto como fundo em vez de faixa.

## IDs no Omnisend

| Objeto | ID |
|---|---|
| Form principal | `6a6d06374b0e7010597932f2` |
| A/B setup novo (**draft**) | `6aa08fd3b768dbb66a45e35a` |
| Variante A — controle roleta | `6aa08fd3b768dbb66a45e35b` |
| Variante B — quiz | `6aa08fd3b768dbb66a45e35c` |
| A/B setup encerrado (teste 3) | `6a8ef9a92040b45f06495db5` |
| Imagem hero no Omnisend | `6aa093bc97f14cdaac6b0953` |

Split 50/50. **Ainda não iniciado.** Para lançar:
`post_form_ab_setups_ab_setup_id_start` com o setup acima, ou o play no painel.
