---
tipo: procedimento
modulo: fundamentos
assunto: dashboard-do-klaviyo
autor: max-sturtevant
registro: [transcricao]
fonte: "CONTEUDO BRUTO/max.md — L46-148 (transcrição); L364-366 (slide, vazio)"
conflitos: [fundamentos-limiar-de-escalar-aquisicao, fundamentos-piso-de-email-share, fundamentos-smart-sending, fundamentos-benchmark-do-form]
status: aprovado
---

> **Procedimento datado.** Passo a passo de interface do Klaviyo, gravado em
> tela. O print do dashboard mostra o período **27/jan/2024 a 26/fev/2024**
> (L64), o que data a gravação. Nomes de menu, posição de botão e telas mudam
> sem aviso. O que envelhece devagar é o **diagnóstico** — como ler os números.
> Os cliques, não.

> **O slide correspondente é vazio.** L364-366 tem só o título "Klaviyo
> Walkthrough" e a linha "Watch the video below for a Klaviyo walkthrough."
> Zero especificação em registro de slide. Tudo nesta nota é `transcricao`, sem
> segundo registro para conferir. O cabeçalho da aula também vem quebrado no
> bruto: o campo do link do gamma está vazio (L42) e a fonte está rotulada
> "Transcrição da Loja" em vez de "da Aula" (L44).

# O que o dashboard mostra, e o que ele desconta

**Receita total da loja** (vinda do Shopify) ao lado da **receita atribuída ao
Klaviyo** — "how much money actually came from email and SMS marketing" (L48-50).

O aviso é imediato: "can't take the attributed revenue like straight to heart"
(L50). O motivo é a janela de atribuição:

> Klaviyo typically, they say somebody clicks an email and they purchase, um,
> within three to five days, they count it as email revenue. So usually, it's a
> little bit inflated, but there's no perfect way to track it. (L54)

O exemplo do diagrama é $28.000 atribuídos (L52). O caso que ele usa para
explicar a imprecisão é o do clique sem compra imediata, com a compra caindo um
dia depois (L52).

# Os três números que ele lê como diagnóstico

**1. % da receita total vinda de email e SMS — 30 a 50%.**

> typically, you want to be anywhere from 30 to 50 percent. If you're over that,
> say you're at like 60 percent, that tells you, okay, let's funnel some of our
> profits back into paid ads. If you're anywhere under 30%, um 40%, then that
> tells you, okay, our email systems can be improved. (L56-58)

Acima da faixa o problema não é o email — é aquisição. Abaixo, é o email. Os dois
limiares desta frase divergem da aula de métricas (">55%" e "less than like 30%",
L170-172) — ver [[metricas-nucleo]].

**2. Split campanhas vs flows — "around 50/50 or 40/60, 60/40 anywhere in that
range" (L60).** O uso é diagnóstico direto: "if you look at a brand like this,
and you see 14% from flows, that tells you like, okay, the flows could use a lot
of improvement" (L62).

**3. Sign-up form, lido como percentual do tráfego — não em absoluto.** Ele
começa errado e se corrige na frase seguinte: "six to 12% of your total email
revenue" (L104) vira "or 6 to 12% of your total site traffic" (L106). A conta
que ele faz na tela deixa claro qual é a certa:

> this mobile form, it's converting 0.7% of people who view the site. So, if
> 1,000 people view the site (…) seven people are signing up, that's not what you
> want. You want to be at least 6 to 12% (…) if you have 1000 people viewing your
> site, you want to have at least 60 to, um, 120 people. (L106-108)

E o alvo não muda por dispositivo: "It's for mobile, same as desktop" (L110).

O período de comparação do painel é sempre o anterior de mesmo tamanho: "the
comparison period is just the prior 30-day period" (L64). Abaixo, "top performing
flows" com receita e variação percentual (L66).

# O que ele declara não usar

Duas áreas, nomeadas:

> Growth Tools, if you just want to have like an overview of like what Growth
> Tools to use, I really like I'm inside a lot of Klaviyo accounts and **I never
> visit this page. I never really view profiles either.** (L112)

E uma terceira, sobre o catálogo de produtos em Content: "if you want to go to
products, again, I don't really use this, but that's there" (L132).

O que sobra como uso real, na lista dele (L134-136): homepage para visão geral,
**campaigns e flows** — "you spend most of your time here" —, audience restrita a
lists e segments ("all that really matters is you want the lists in segments",
L112), sign-up forms e dashboards de analytics.

# Criar um segmento, passo a passo (L118-128)

Ele demonstra criando um segmento de abandono de checkout.

1. Audience → Segments → **Create segment**, dar nome ("test" / "abandoners").
2. Ir para **Definition** e escolher a condição por comportamento: "what somebody
   has done" → `checkout started` → **at least once in the last 30 days**.
3. Adicionar a segunda condição com **and**: `placed order` → **zero times in the
   last 30 days**.
4. Criar e esperar carregar. "what this is going to tell us is people who have
   abandoned checkout in the last 30 days" (L122).

Ele erra a definição ao vivo e usa o erro como demonstração: com a condição
trocada carregam **8 membros** (L126); corrigida para `place order zero times`,
carregam **2** (L128). O caminho de conserto é o mesmo botão: "you just go to
update definition if you want to change it" (L126).

O segundo segmento que ele lê na tela — "engage 60 days", 258 membros — mostra a
forma canônica de um segmento de engajamento: estar na newsletter **e** (ter
aberto email ao menos uma vez nos últimos 60 dias **ou** clicado nos últimos 60
dias **ou** ter entrado na newsletter nos últimos 30 dias) (L114-116).

Para que servem, na frase dele: "get different levels of engagement of your list,
and just get a better understanding of where they're at in the customer journey"
(L128).

# Um detalhe operacional que conflita com o glossário

Ao montar a campanha, sobre a opção de pular perfis emailados recentemente (Smart
Sending): "skip recently emailed profiles, typically you want to send that off"
(L78 — "send" é ruído de ASR para *turn*). O glossário restringe o mesmo conselho
a flows: "Smart Sending – Klaviyo feature that skips sending to people recently
emailed. **Turn off for flows**\!" (L447). Ver
[[conflitos-de-fundamentos-plataforma-e-operacao#fundamentos-smart-sending]].

# O que o corpus não diz

Não há passo a passo de conexão do Shopify com o Klaviyo, de configuração de
domínio de envio nem de importação de lista — o único passo prescrito é "follow
their onboarding steps" ([[escolha-do-esp]], L36). Os oito flows aparecem só como
lista de gatilhos numa conta já montada (L92) e nomeados "recommended flows when
just starting out" (L94); a montagem deles é do módulo [[mapa-dos-flows]].
