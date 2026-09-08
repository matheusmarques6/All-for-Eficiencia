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

Tudo idêntico entre A e B — cores, fonte, largura 350 px, gatilho (12 s +
scroll 70 % + exit intent), frequência 1/dia, exclusão de /cart e /checkout,
X visível, sem double opt-in. **Só o tipo de form muda.**

### A — CONTROLE (roleta, 1 campo)
Passo único: `TREUQUELL` · **DREHEN & GEWINNEN** · "Bis zu 10 % Rabatt auf Ihre
erste Bestellung." · roleta · "E-Mail eingeben und auf RAD DREHEN tippen." ·
campo e-mail · botão **RAD DREHEN**.
Tags: `form_subscriber`, `wheel_10`.

### B — QUIZ (2 passos)

**Passo 1** — sem nenhum campo, só decisão:
- `TREUQUELL`
- **Sie haben 10 % Rabatt** ← tradução direta do *"You've got 10% off"* de
  [[copy-do-form]]: posse + *loss aversion* (fechar o popup = abrir mão de algo
  que já é seu).
- **Zum Einlösen: Wofür shoppen Sie heute?** ← *"To claim your discount, tell us
  what you're shopping for"*.
- Três botões (`nextStep`), montados a partir do catálogo real da loja:
  `Reparieren & Abdichten` · `Licht & Solar` · `Haus, Garten & Outdoor`

**Passo 2** — um input só:
- **Fast geschafft** · "Wohin dürfen wir Ihre 10 % schicken?"
- campo e-mail
- botão **RABATT SICHERN** ← *"Claim now"*, nunca *"Continue"* ([[copy-do-form]]:
  "continue implies that there's going to be more that the person has to do").
- rodapé legal + link de privacidade

**Sucesso:** "Willkommen bei TREUQUELL" + instrução de checar a caixa de entrada
(engajamento na primeira mensagem ajuda reputação — [[copy-do-form]]).
Tags: `form_subscriber`, `quiz_10`.

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

1. **Fechar o form** (alavanca #3, nunca testada). Hoje o X está visível e não
   existe botão de recusa. Testar X contra **"Nein danke, ich zahle den vollen
   Preis"** com o X escondido. Max: *"Always performs better"*.
2. **Gatilho** (alavanca #4, nunca testada). Hoje: 12 s + scroll 70 % + exit
   intent. Testar contra **4 s**, que é o único valor comum às três faixas do
   corpus. Critério: **submits totais, não taxa**.
3. **Oferta** (alavanca #1). AOV da loja é ~€20–50, abaixo do corte de $100 →
   **% OFF é o formato certo** ([[a-oferta-e-o-componente-principal]]). O que
   falta testar não é o formato, é o valor (10 % vs 15 %) e o frete grátis.
4. **Foto** (alavanca #5). Nenhuma das variantes usa imagem hoje.

## IDs no Omnisend

| Objeto | ID |
|---|---|
| Form principal | `6a6d06374b0e7010597932f2` |
| A/B setup novo (**draft**) | `6aa08fd3b768dbb66a45e35a` |
| Variante A — controle roleta | `6aa08fd3b768dbb66a45e35b` |
| Variante B — quiz | `6aa08fd3b768dbb66a45e35c` |
| A/B setup encerrado (teste 3) | `6a8ef9a92040b45f06495db5` |

Split 50/50. **Ainda não iniciado.** Para lançar:
`post_form_ab_setups_ab_setup_id_start` com o setup acima, ou o play no painel.
