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

**Redesign aplicado nas duas** (1ª versão foi reprovada: caixa de 350 px, sem
imagem, botões finos, tipografia pequena). Referência: os popups da Alia
(Lemme, Nécessaire, Kopari) — foto de verdade, tipografia grande, botões pill de
alto contraste, link de recusa.

Casca compartilhada, idêntica nas duas:

| Elemento | Valor |
|---|---|
| Largura | **400 px** (era 350) |
| Fundo / raio | `#151515`, raio 16 px |
| Wordmark | TREUQUELL, 12 px, letter-spacing 4 px |
| Headline | "Sie haben" 24 px branco + **"10 % RABATT" 36 px em `#E0A82E`** |
| Botões / campos | pill (raio 50 px), branco sólido, texto `#151515` 16 px bold |
| Recusa | "Nein danke, ich zahle den vollen Preis", 11 px, sublinhado |
| Hero | banner da home (`BannerTreuquell_cleanup`) em faixa full-bleed no rodapé |
| Gatilho | 12 s + scroll 70 % + exit intent, 1×/dia, exclui /cart e /checkout |

O logo do site **não** foi usado: é preto sobre branco (2045×584) e vira uma
barra branca no fundo escuro. O wordmark em texto é o que o próprio header do
site mostra.

Imagens de produto também foram descartadas: são collages com a marca
**KLARWEN** impressa (fornecedor), não Treuquell.

**Só o mecanismo muda entre A e B.**

### A — CONTROLE (roleta, 1 campo)
Passo único: wordmark · "Sie haben" · **10 % RABATT** · roleta (62 % da largura)
· "E-Mail eingeben und drehen" · campo e-mail · botão **RAD DREHEN** · recusa ·
rodapé legal · faixa de foto.
Sucesso: "10 % gewonnen". Tags: `form_subscriber`, `wheel_10`.
Altura ≈ 800 px.

### B — QUIZ (2 passos)

**Passo 1** — nenhum campo, só decisão:
- wordmark · "Sie haben" · **10 % RABATT**
- **Wofür shoppen Sie heute?** ← *"To claim your discount, tell us what you're
  shopping for"* de [[copy-do-form]]
- três pills (`nextStep`) com as **coleções reais da loja**:
  `Werkzeuge & Haushalt` · `Beleuchtung & Energie` · `Garten & Reinigung`
- recusa · faixa de foto

**Passo 2** — um input só:
- wordmark · "Fast geschafft" · **10 % RABATT** · "Wohin schicken wir Ihren Code?"
- campo e-mail · botão **RABATT SICHERN** ← *"Claim now"*, nunca *"Continue"*
- recusa · rodapé legal · faixa de foto

Sucesso: "Willkommen an Bord" + instrução de checar a caixa de entrada.
Tags: `form_subscriber`, `quiz_10`. Altura ≈ 580 px.

**Headline "Sie haben 10 % RABATT"** é o *"You've got 10% off"* de
[[copy-do-form]]: personalização + *loss aversion* — fechar o popup passa a ser
abrir mão de algo que já é seu.

**O botão de recusa entrou nas duas.** É a alavanca #3 de Max ("Always performs
better", [[checklist-do-form]]) e, como está nas duas, não contamina o teste.
O X continua visível nas duas — esconder o X fica para o teste seguinte.

> **Atenção na leitura dos números.** Como a casca mudou nas duas variantes, a
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
