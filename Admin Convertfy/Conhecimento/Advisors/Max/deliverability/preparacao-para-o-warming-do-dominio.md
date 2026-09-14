---
tipo: procedimento
modulo: deliverability
assunto: warming-do-dominio
autor: max-sturtevant
registro: [slide, outro-narrador]
fonte: "CONTEUDO BRUTO/max.md — L8518-8576 (transcrição); L8522-8526 (bullets do deck). O corpo do deck de warming NÃO foi exportado."
validade: "procedimento — o corpus não data a gravação. Extraído em 2026-09-06."
status: aprovado
---

Warming do domínio é aquecer um domínio de envio novo (ou machucado) com volume
crescente antes de qualquer campanha. Esta nota cobre a **preparação**: em quais
casos o método se aplica, a fundação de flows e pop-up que precisa estar rodando
antes, e de onde tirar o primeiro público. A execução da rampa está em
[[rampa-de-warming-do-dominio]]; os casos reais e as lacunas, em
[[evidencia-e-lacunas-do-warming-do-dominio]].

# Aviso de autoria

**Faixa L8381-8646 (toda a fala do módulo de deliverability) — `outro-provavel`.**
Sem prova nominal. A classificação é **estilométrica**: o bloco pertence ao aglomerado
do único bloco `outro-provado` e não traz um só marcador do idioleto de Max.
`outro-provavel` não é `outro-provado` — não está provado que a voz não é dele, está
estabelecido que é muito improvável ([[mapa-da-autoria]] §7.3).

Critério: **idioleto** ([[mapa-da-autoria]] §2.1) — ausência de "I recommend", "my favorite"
e "I like to", presença de "at the end of the day" e "obviously", e o fecho coletivo
"thank you guys… see you in the next one". **A saudação de abertura não é critério e
não pode ser citada como evidência:** o laudo testou e ela caiu — o walkthrough de
Figma abre com "Hello, hello" e é comprovadamente Max, que em L7817 digita `@max` e
diz "tags me" ([[mapa-da-autoria]] §5).

Nesta nota a exposição é quase total. Os cinco bullets do deck (L8522-8526) e o
limiar de 60%+ do deck de deliverability (L8728) são **slide** — artefato de Max.
Todo o resto — fundação, segmentos-semente, rampa, passo de escalonamento,
cadência, batching, cronograma por semanas, regra de ouro e correção de rota —
está em L8532-8646, faixa não-Max, e **não é citável como fala dele**. Como o deck
de warming nunca foi exportado, este procedimento fica sem nenhum registro de Max
que o confirme: é a peça do corpus com menor lastro de autoria.

> **Lacuna estrutural desta nota.** O deck citado no vídeo — "Email Warming
> Deliverability Deep Dive", `https://gamma.app/docs/Email-Warming-Deliverability-Deep-Dive-ex6p9skikw53x06`
> (L8520) — **nunca foi exportado**. A seção GAMMA (L8647-8759) cobre só o deck
> de deliverability e vai direto de "Check Your Deliverability With Glockapps"
> (L8752) para `# OPTIMIZATION` (L8760). O único registro de slide sobreviveu
> como cinco bullets de resumo (L8522-8526). Todo o resto — rampa, cronograma,
> batching, casos — existe **apenas na transcrição falada**. É a única parte
> crítica do corpus sem segundo registro para conferir número.

# Quando se aplica

Bullets do deck, verbatim (L8522-8526):

> * **This if for you if:**
>   * You have sent no emails before from your Klaviyo account AND Your
>     technical setup / branded sending domain is set up
>   * OR, your deliverability is poor. This same method can be used to improve
>     it (with a few tweaks)
> * **Technical Setup: [Setting up branded sending domain >>>](https://help.klaviyo.com/hc/en-us/articles/115000357752)**
>   * If this isn't done, do this before sending ANY emails

Dois casos, portanto: conta nova **ou** deliverability ruim — "This same method
can be used to improve it (with a few tweaks)" (L8524). Os *tweaks* nunca são
enumerados como lista; o que existe é [[reparo-de-reputacao]]. O setup técnico é
pré-condição, não etapa: ver [[setup-tecnico]].

O que se está prevenindo (L8533-8534): abrir conta no Klaviyo, importar a lista
de clientes e leads e disparar para todo mundo — "nobody opens them, no one
engages, you get super low rates, and then basically everything going forward
ends up going to spam". O custo do erro (L8555, L8606): "it's much easier to
build your sender reputation and deliverability warming up than it is to fix it
when it's already in a poor position."

A imagem usada na aula (L8541): "it's like building a house. You have to establish
the infrastructure through warming before you get really creative."

# A fundação, antes de qualquer campanha

Duas coisas ligadas antes de começar a rampa.

**1. Flows de alta intenção rodando** (L8545): "Welcome Flow, Post-Purchase,
Abandoned Card [*Cart*], Abandoned Checkout, Browse, Site Abandonment, I'll list
the other ones" — as outras nunca são listadas. Racional (L8549-8551): são pessoas em
estágios diferentes da jornada, "these are points where we obviously want to
target people", e ficam rodando evergreen.

**2. Pop-up convertendo** (L8546): "no matter what, if it's a new account or
whenever, you want to make sure your pop-up form is converting."

E dentro do pop-up, uma regra explícita de onde **não** colocar o código
(L8548-8549):

> it's important to not put that discount code or whatever, if there is a code.
> In the form itself, you want to strategically place that in welcome email 1,
> 2, 3, 4, so that people are prompted and conditioned from the beginning to
> expect value coming from their emails and they're forced to open and click
> that link.

O objetivo é warming, não conversão: o desconto vira o isco que garante open e
click nos primeiros quatro emails.

# De onde tirar o primeiro público

Depende do dado que existe. "It's not always going to be the same solution or
the same exact segment" (L8553).

**Com dado de email** — migração de MailChimp ou OmniSend, ou conta antiga com
deliverability ruim (L8563). "You always want to stick with your email data"
(L8563-8564). Os quatro segmentos-semente citados (L8564-8565), verbatim:

> people who have opened three times in the last thirty days, people who have
> opened five times in the last sixty days, people that have opened an email
> once or twice in the last week, people that have clicked an email in the last
> week

Ressalva do material (L8565-8567): não existe solução única — o segmento sugerido
pode estar vazio, ou ter "seventy-eight people in there, which isn't really going
to move the needle".

**Sem dado de email** — dado comportamental do Shopify, que integra com o
Klaviyo (L8571). "It's also one that you have to be a little bit careful about"
(L8572). Os três sinais citados (L8574), verbatim:

> people that have viewed a product in the last three days, placed an order in
> the last week, and started checkout in the last week

E a migração de volta assim que houver dado de email (L8576): "the best
indicator of future behavior is past performance."

# Continua em

Feita a preparação, a execução — primeiro envio, passo de escalonamento,
cadência, batching, cronograma por semanas e correção de rota — está em
[[rampa-de-warming-do-dominio]]. Os dois casos reais aplicados, a ferramenta
nunca nomeada e o que o corpus não diz estão em
[[evidencia-e-lacunas-do-warming-do-dominio]].
