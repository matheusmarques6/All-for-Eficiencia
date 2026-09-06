---
tipo: procedimento
modulo: sms
assunto: crescer-a-lista-de-sms
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L9237-9242 (transcrição), L9320-9350 (slide)"
conflitos: [sms-instrucoes-de-optin-sao-de-email, sms-delay-do-popup, sms-benchmark-de-form, sms-exit-intent, sms-vias-de-crescimento, sms-auto-check-e-a-lei, list-growth-checkbox-preselecionado]
status: rascunho
---

> **Procedimento datado.** Tela do Shopify; ele mesmo avisa em outro ponto do
> corpus: "Shopify changes this a lot" (L537).

# As duas vias

"there are two main ways to grow your SMS list we have post purchase optins and
then we also have popup forms" (L9237) — duas, contra os quatro métodos que o
corpus dá para email (L531, L1093; ver `sms-vias-de-crescimento` e
[[list-growth/os-quatro-metodos]]). O checkbox é coleta passiva, "easy way to
just grow your list in the background"; o pop-up é "the most effective way to
grow your SMS list" (L9237-9238).

# Via 1 — checkbox no checkout

"a simple checkbox at checkout which will sign up someone's number for receiving
marketing" (L9322), "takes 5 minutes to set up on Shopify" (L9323). Regra dura:
"We want it to be auto-checked so someone will be added to the list" (L9324).
Quem entra por aqui "will be your highest value members" (L9326).

## ARMADILHA: os passos são de email, não de SMS

O slide "**Instructions for Post Purchase Opt-Ins**" (L9328) está dentro da
seção "How To Grow Your SMS List" (L9318). Os passos, verbatim (L9330-9333):

> * From your Shopify admin, go to **Settings** > **Checkout**.
> * To add a sign-up checkbox to your checkout, in the **Marketing options**
>   section, check **Email**.
> * Check **Preselected** so that the email marketing sign-up check box is
>   preselected at the checkout by default for customers without an account or
>   customers who are on your email subscription list. The email marketing
>   sign-up check box isn't preselected for customers who have opted out of
>   email marketing or who aren't on your email subscription list.
> * Click **Save**.

**Nenhum dos quatro passos cobre o checkbox de telefone.** O passo 2 manda marcar
`Email`; o passo 3 fala três vezes em "email marketing sign-up check box" e em
"email subscription list". A prosa promete inscrever "someone's number" (L9322) e
a instrução entrega opt-in de email — são os mesmos passos do módulo de list
growth (L1118-1121), onde eram corretos, reaproveitados sem adaptação. Ver
`sms-instrucoes-de-optin-sao-de-email`. O passo 3 ainda se contradiz sozinho
(L9332), mesmo defeito de L1120: `list-growth-checkbox-preselecionado`.

# Via 2 — pop-up

Benchmark: "most brands I audit only have a form that converts like around 2 to
3% of website visitors"; alcançável, "8% to 10% essentially like tripling the
amount of people entering your list" (L9238-9239). O módulo de list growth usa
outros números (6-12%, 10%+, 20-30%) — ver `sms-benchmark-de-form`. Sobre ser
intrusivo, o slide responde por ROI: "(+ a good form won't be intrusive)"
(L9338).

Quatro regras, todas da fala:

1. **Trigger 6-10 segundos após o page load**; nada de scroll nem exit intent,
   "because sometimes it can misfire" (L9239-9240). Ele usa 6 segundos, "and no
   that's not too soon trust me I've tested this"; contra o delay longo, "if we
   wait 30 seconds then how many people are actually going on your site for 30
   seconds not a lot" (L9240). O corpus dá 4-12s, 4-8s e 5s em outros pontos —
   ver `sms-delay-do-popup`; sobre exit intent, `sms-exit-intent`.
2. **Oferta real, obrigatória.** "it's not a charity people aren't just going to
   hand you their phone number you need to give them something such as a
   discount" (L9240-9241), aceitando perder margem na primeira compra porque o
   backend devolve. Alternativas: "giveaways or free guides" (L9241).
3. **Mínimo de palavras** — "just tell the customer this is what you get give us
   your email" (L9241).
4. **Nada de aniversário nem preferências** (L9242).

## Email no passo 1, telefone no passo 2

> "For our pop-ups **we don't want to add both email and sms in the same
> step.**" (L9342)

Motivo: "It's perceived to be **much more work** for the customer and it will
hurt conversions" (L9344). O desenho: email primeiro, para o cliente "**thinks
all they have to do it enter their email**", depois o número, com algo como
"finish claiming your discount by entering your phone number" (L9345). Na fala:
"that works 10 times better" (L9242).

# O que o corpus não diz

- Como capturar telefone no checkout do Shopify — a instrução prometida não existe.
- Se auto-marcar o checkbox vale para telefone: ele exige auto-check (L9324) e
  duas seções depois lembra que a lei americana limita SMS (L9461), sem
  conciliar. Ver `sms-auto-check-e-a-lei`. O corpus não tem nada sobre TCPA nem
  sobre texto de consentimento.
- Os prints "**Step 1**" / "**Step 2**" (L9348-9350) e os tutoriais de form
  (L9352-9357) são títulos sem conteúdo.
