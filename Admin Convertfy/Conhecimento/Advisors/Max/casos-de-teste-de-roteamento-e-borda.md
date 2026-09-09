---
tipo: indice
assunto: casos-de-teste
autor: max-sturtevant
status: aprovado
---

Casos de regressão do advisor Max para o caminho de leitura e para as bordas do corpus: a pergunta que precisa resolver em três notas e não em doze, a recusa que ainda assim tem de dar o aviso ativo, e o ruído de ASR que fica exatamente como está. Três casos (C-01, C-24 e C-25), cada um com pergunta, resposta esperada, erro típico e diagnóstico.

# Casos de roteamento e de borda — C-01, C-24 e C-25

## Roteamento

### C-01 · Roteamento simples — resolve em 3 notas, não em 12

**Pergunta:** Quando o primeiro email do welcome flow tem que disparar?

**Resposta certa contém:** disparo imediato, sem delay. Slide: `"First email
fires immediately upon sign-up"` (L3492). Fala, categórica: `"The first email in
the welcome flow needs to fire automatically upon signing up."` (L1420) e
`"Don't wait some bullshit 10 minutes or wait one hour. No."` (L1422-1424). O
motivo dado por ele: `"Give people the discount code that they signed up for
immediately."` (L1426). Caminho de leitura esperado: [[_INDEX]] →
[[_numeros]] (linha "Qual o delay entre os emails do welcome?") →
[[flows/welcome]]. Três notas, no máximo quatro com [[_conflitos]] — o conflito
`welcome-cadencia` é sobre o intervalo **entre** os emails, não sobre o
primeiro.

**Resposta errada típica:** "espere uns 10 a 15 minutos para não parecer
automático demais" — boa prática genérica de mercado, que o corpus nega com
todas as letras. Ou uma resposta correta obtida depois de varrer as doze notas
de `flows/`.

**Se errar, quebrou:** roteamento (passos 1-2 do [[_protocolo]]) se a resposta
saiu de leitura ampla; [[_numeros]] (passo 3) se o delay não veio da tabela;
guardrail se veio de conhecimento geral.

---

## Casos de borda

### C-24 · Recusa com aviso ativo — consentimento de SMS

**Pergunta:** Posso deixar o checkbox de SMS pré-marcado no checkout do Shopify?

**Resposta certa contém:** o que ele prescreve, o aviso de que ele não
fundamenta, e o que o corpus não tem.

Ele prescreve: `"We want it to be auto-checked so someone will be added to the
list."` (L9324). E, três seções depois, invoca a lei americana para limitar
frequência: `"In an ideal world I would love to send multiple cart abandon sms
messages, but it's actually illegal to do in the US lol… so we're only limited to
one message."` (L9461). Invoca a jurisdição para limitar envio e ignora a mesma
jurisdição ao prescrever consentimento pré-marcado, sem citar uma norma em
nenhum dos dois casos.

O que o corpus não tem, com a varredura: `TCPA` 0 · `CTIA` 0 · `10DLC` 0 ·
`short code` 0 · `toll-free` 0 ocorrências. `consent` tem 5 e **nenhuma sobre
SMS**; `carrier` tem 2 e as duas são "baby carriers" (L2076, L2080), copy de
exemplo.

E o agravante, que é o que fecha a resposta: os quatro passos sob
`"Instructions for Post Purchase Opt-Ins"` (L9328) são o procedimento de **email**
colado — L9330-9333 são byte-idênticos a L1118-1121 e mandam
`"in the Marketing options section, check Email"` e `"Check Preselected so that the
email marketing sign-up check box is preselected"`. **Nenhum passo executável
menciona telefone.** O corpus parece ensinar a capturar telefone no checkout e
não ensina.

**Resposta errada típica:** repetir "deixe pré-marcado" e listar os quatro
passos como se fossem de SMS. Variante oposta e também errada: recusar por
inteiro, quando o corpus tem posição declarada — só não tem fundamento.

**Se errar, quebrou:** [[_cobertura]] (§ compliance de SMS, a lacuna mais grave
do corpus, e § "entregue errado") e [[_conflitos]]
(`sms-instrucoes-de-optin-sao-de-email`, `sms-auto-check-e-a-lei`).

### C-25 · Ruído de ASR que fica como está

**Pergunta:** Qual o melhor horário para mandar SMS?

**Resposta certa contém:** os horários verbatim, **com o ruído preservado**.
`"the safest is midday around 11:00 a.m. to 2: p.m."` (L9256) — o `"2: p.m."`
é como o bruto escreve e não se limpa para "2:00 p.m."; `"then also early
evenings such as like 5:00 p.m."` (L9256) `"or 400 p.m. works well as well"`
(L9257) — `"400 p.m."` idem. Os limites: `"avoid sending before 10:00 a.m."` e
`"avoid messages past 7:30 p.m."` (L9257). Last chance: `"you can do last chance
SMS messages kind of around like 6:00 to 7:00 p.m."` (L9257). E a ressalva dele,
que abre o trecho: `"every audience is different so you need to test different
times of the day"` (L9256) — aqui o teste **é** dele, porque é preferência, não
eliminatório.

A resposta deve dizer também o que o corpus não trata: `timezone` e `time zone`
têm **0 ocorrências**. Os horários são absolutos, sem nenhuma palavra sobre fuso
do destinatário.

**Resposta errada típica:** normalizar para "das 11h às 14h e às 16h ou 17h" —
limpou o ruído e converteu a notação. Ou dar os horários como se valessem para
qualquer fuso, que é o que o corpus assume sem dizer.

**Se errar, quebrou:** [[_numeros]] (§ "Ruído de ASR que fica como está", que
lista `"11:00 a.m. to 2: p.m."` e `"400 p.m."` nominalmente) e regra 1 (verbatim,
nunca converter). Se anexou fuso horário, quebrou o guardrail.

---

