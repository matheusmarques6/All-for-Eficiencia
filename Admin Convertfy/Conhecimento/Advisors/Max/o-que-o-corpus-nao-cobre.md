---
tipo: indice
assunto: cobertura-e-lacunas
autor: max-sturtevant
status: aprovado
---

Lista dos assuntos que o corpus Max não cobre e que vão ser perguntados assim
mesmo, cada um com a varredura de termos que prova a ausência. Abre pela lacuna
mais grave do corpus — consentimento e compliance de SMS — e segue por preço de
ferramenta, B2B e assinatura, mercados fora dos EUA, plataformas concorrentes e
canais adjacentes. É a nota de consulta antes de recusar. Índice em
[[mapa-da-cobertura]].

# Assuntos que o corpus NÃO cobre e vão ser perguntados

Derivados do próprio material, não do senso comum. Cada um com a varredura que
prova a ausência.

## Consentimento e compliance de SMS — a lacuna mais grave do corpus

**A varredura.** No arquivo inteiro, 9.544 linhas:

| Termo | Ocorrências |
|---|---|
| `TCPA` | **0** |
| `CTIA` | **0** |
| `10DLC` / `10 DLC` | **0** |
| `short code` / `shortcode` | **0** |
| `toll-free` | **0** |
| `carrier` | 2 — e **as duas são "baby carriers"** (L2076, L2080), copy de exemplo de uma marca. Zero como operadora. |
| `consent` | 5 — e **nenhuma sobre SMS**: L219 e L229 são o narrador citando o índice do glossário, L499 é o cabeçalho `### 🔐 **Compliance & Consent**`, L503 é a definição de GDPR, L1414 é navegação de UI do Klaviyo ("go to settings, list settings, consent"). |

> **Correção de brief.** `consent` e `carrier` **não** têm zero ocorrências, ao
> contrário do que a especificação desta nota supunha. Têm 5 e 2. O que é
> verdade — e é o que importa — é que **nenhuma delas trata de consentimento de
> SMS**. A lacuna se sustenta; a formulação "zero ocorrências" não. Registrado
> aqui para que ninguém a repita como fato.

**O que existe, e é só isto.** Uma seção do glossário, `### 🔐 **Compliance &
Consent**` (L499-507), com sete definições de uma linha — Opt-In, Double Opt-In,
GDPR, CAN-SPAM, CASL, Unsubscribe Link, Preference Center. **Todas de email.**
E a fala que acompanha o glossário descarta a seção explicitamente:

> **L229** — "compliance and consent. **which you really don't, don't need to
> know these**, but if you ever mention it, you can check back to this"

**E mesmo assim o corpus prescreve nos dois sentidos, sem conciliar:**

- **L9324** (slide de SMS): "We want it to be **auto-checked** so someone will
  be added to the list." Checkbox pré-marcado, sobre a captação de telefone.
- **L9461** (slide de SMS, três seções depois): "In an ideal world I would love
  to send multiple cart abandon sms messages, but it's actually **illegal to do
  in the US** lol… so we're only limited to one message."

Ou seja: ele invoca a lei americana para **limitar** a frequência de envio e
ignora a mesma jurisdição ao prescrever consentimento pré-marcado — e não cita
uma única norma em nenhum dos dois casos. Conflito registrado:
`sms-auto-check-e-a-lei`.

**Como responder.** Esta é a única lacuna do corpus em que a recusa deve vir
acompanhada de aviso ativo, e não só do vizinho: o material recomenda uma
prática de consentimento e não cobre o regime que a governa. Entregar o que ele
diz, marcar que ele não fundamenta, e nomear que o corpus não tem TCPA, CTIA,
10DLC, short code nem texto de consentimento. Ver [[sms/setup-e-plataforma]] e
[[sms/crescer-a-lista]].

## Preço de qualquer ferramenta

`pricing` tem **uma** ocorrência (L6001) e é sobre tiers de produto do cliente.
Não há preço de Klaviyo, Omnisend, Alia, Glockapps, Attentive nem Postscript, em
nenhum registro. O mais específico que o corpus chega:

- Klaviyo vs Omnisend: "Omnisend is a solid budget option" (L34, L357-358) —
  "budget option" nunca é definido.
- Alia: "the ROI is worth it every time" (L1243) — afirmação sem número.
- Attentive vs Postscript: "relatively same price" (L9236, L9315).
- Glockapps: existe plano gratuito e plano pago; o corpus não diz o preço nem o
  que o gratuito limita.

Corolário: **não há limiar de tamanho de lista nem de faturamento para escolher
entre plataformas**, e não há instrução de migração. Ver
[[fundamentos/escolha-do-esp]].

## B2B, assinatura e qualquer coisa que não seja DTC de Shopify

`B2B` = **0 ocorrências**. `wholesale` = **0**. Todo o corpus pressupõe
e-commerce direto ao consumidor em Shopify — a integração Shopify é assumida
como dada em segmentação, em flows e no dashboard, e nunca é discutida como
escolha. O público declarado é ainda mais estreito: marcas acima de **$50k/mês**
(L4184, L9259, L9542).

## Mercados fora dos EUA

`Europe`, `European`, `Australia`, `Germany`, `Brazil`, `international` = **0
ocorrências cada**. `UK` como palavra = **0** (as 14 ocorrências de `uk` são 13
dentro do base64 da L9545 e uma dentro de outra palavra). `timezone` /
`time zone` = **0** — e isso importa, porque [[sms/calendario-e-horarios]] e
[[otimizacao/send-time]] dão horários em absoluto, sem nenhuma palavra sobre
fuso do destinatário. `currency` aparece uma vez e é a variável Klaviyo
`currency_format` (L3910).

**Duas exceções, e são as duas na mesma seção do glossário.** `Canada` tem **1**
ocorrência: "**CASL** – Canada's anti-spam law" (L505). E a definição de GDPR
nomeia a União Europeia: "EU law regulating data and email marketing consent"
(L503). As duas estão dentro de `### 🔐 **Compliance & Consent**` (L499-507) —
a mesma seção que a fala manda ignorar (L229). São definições de uma linha, sem
nenhuma prescrição; não sustentam resposta sobre operar fora dos EUA. Mas
**a varredura não pode ser declarada como zero**: se a pergunta for "ele fala de
GDPR/CASL?", a resposta é "define numa linha cada, e descarta a seção", não
"não menciona".

O diagnóstico de mercado é frontalmente americano — "stimulus checks back in
2020", "we apply that to, like, 2025 where tariffs come into play" (L9);
"Increased Cost Per Acquisition x Lower LTV x **Tariffs** = Lower Profitability"
(L268) — e é apresentado como universal, sem recorte geográfico. Ver
[[fundamentos/estado-do-mercado]].

## Plataformas que não Klaviyo, Omnisend e Shopify

Varredura, ocorrências no arquivo inteiro: `ActiveCampaign` 0 · `Sendlane` 0 ·
`Braze` 0 · `HubSpot` 0 · `Salesforce` 0 · `Drip` 0 · `ConvertKit` 0 ·
`Beehiiv` 0 · `WooCommerce` 0 · `BigCommerce` 0 · `Magento` 0 · `Yotpo` 0 ·
`Recharge` 0 · `Gorgias` 0 · `Triple Whale` 0 · `Northbeam` 0.

As três exceções, todas incidentais:

- **Mailchimp** — 3 menções, nenhuma avaliativa: exemplo dentro da definição de
  ESP no glossário (L459) e origem de migração em dois trechos de warming
  (L8563, L8607). Nunca comparado, nunca julgado.
- **Attentive e Postscript** — nomeados como "the two other main options" para
  SMS e "both are great" (L9236, L9314). Zero walkthrough, zero critério de
  escolha, zero preço.
- **Alia** — tem walkthrough falado e julgamento, mas o material de deck é o
  placeholder `[need]` (L1304).

## Outros canais e disciplinas adjacentes

`WhatsApp` 0 · `push notification` 0 · `direct mail` 0 · `sms deliverability` 0.
`landing page` 3 ocorrências em 2 linhas (L545 duas vezes, L549) e `retargeting`
1 (L5081), todas de passagem. A analogia com CRO de
site é feita uma vez (L6896) e nunca desenvolvida — ver
[[design/por-que-design-importa]]. **Deliverability de SMS não existe no corpus**,
apesar de o módulo inteiro de deliverability de email existir.

---
