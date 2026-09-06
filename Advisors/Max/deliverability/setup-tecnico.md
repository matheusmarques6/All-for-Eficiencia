---
tipo: procedimento
modulo: deliverability
assunto: setup-tecnico-dns
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L8396-8412 (transcrição), L8667-8692 (slide)"
validade: "procedimento — o corpus não data a gravação. Extraído em 2026-09-06. Telas do Klaviyo, do provedor de domínio e do Glockapps podem ter mudado."
status: rascunho
---

> **Procedimento datado.** O corpus não diz quando foi gravado. Os passos abaixo
> dependem de telas de terceiros (Klaviyo, provedor de domínio, Glockapps) que
> podem ter mudado. Avise antes de executar.

# O bloqueio

É a única regra dura da pasta, e ela vem antes de tudo (L8526):

> **If this isn't done, do this before sending ANY emails**

O contexto no slide de warming (L8522-8523) trata o setup técnico como
pré-condição do warming, não como etapa dele: o método de warming é para quem
"has sent no emails before from your Klaviyo account **AND** Your technical
setup / branded sending domain is set up".

# Os registros

Ficam hospedados no DNS do provedor de **domínio**, não do Klaviyo. Slide,
verbatim (L8671):

> Fancy records hosted by your domain provider in your DNS settings
> (MX, SPF, DMARC, DKIM)

A lista formal de registros, no slide seguinte, tem **três** e omite o MX
(L8685-8689):

> Records you need on your domain for inbox placement:
> * SPF
> * DMARC
> * DKIM

Isso é uma divergência interna do próprio slide: o MX é citado na prosa (L8671)
e não aparece na lista de requisitos (L8687-8689). Nenhum dos dois registros
explica o que cada sigla faz. Ver `deliverability-registros-dns` em
[[_conflitos]].

Além dos registros, o **branded sending domain** no Klaviyo — o slide chama de
"Dedicated Klaviyo sending domain" (L8673). Na fala (L8396-8398):

> It's basically where you hook up your Klaviyo settings with your domain
> settings and make sure that those match, make sure that those record match so
> that they recognize you as a real account and not spam and not something
> shady.

# A posição dele: provavelmente já está pronto

Ele desdramatiza o setup nos dois registros.

Fala (L8408): "it seemed very complex, but most domains already have the right
records in place."

Slide, verbatim (L8683-8684):

> Seems complex, but most domains already have the correct records in place on
> your domain, maybe one missing.
> **As you setup Klaviyo they set these all up for you :)**

Note a diferença de força: a fala diz que os registros costumam já existir; o
slide vai além e diz que o **Klaviyo configura tudo para você**. A fala não faz
essa afirmação.

# A fonte oficial que ele indica

Não é o material dele. Ele delega para o artigo do Klaviyo, citado duas vezes —
uma no resumo de deliverability (L8371) e outra como pré-requisito do warming
(L8525):

> **Technical Setup: [Setting up branded sending domain >>>](https://help.klaviyo.com/hc/en-us/articles/115000357752)**

O grau de confiança que ele dá ao artigo (L8410-8414): é "the most forward
step-by-step", tem muita informação, e "if you follow the instructions
one-to-one, you're going to set yourself up for success". Ele diz que o próprio
Klaviyo aponta a direção dentro do produto, mas o artigo é mais profundo — e é
o que a agência dele manda para os clientes.

# Verificação

Glockapps, na variante domain-checker. Slide, verbatim (L8691):

> Use [https://glockapps.com/domain-checker](https://glockapps.com/domain-checker)
> to see if you are missing any, if you are follow their guide to getting
> installed.

Na fala ele dá o mesmo endereço de forma degradada por ASR ("Glock apps. It's a
domain checker", L8414) e o descreve como o recurso para quando "we don't have
the domain information".

Isso é uma ferramenta diferente do teste de placement descrito em
[[auditoria-glockapps]], embora seja a mesma empresa: aqui o alvo é o registro
DNS, lá é onde o email cai.

# O que o corpus não diz

- O que SPF, DMARC ou DKIM fazem. As siglas são listadas, nunca explicadas.
- Se o MX é requisito ou não (o slide se contradiz).
- Nenhum passo de tela, nenhum valor de registro, nenhum print. O procedimento
  inteiro é: leia o artigo do Klaviyo, cheque no Glockapps.
- Quanto tempo o setup leva ou quanto tempo o DNS demora a propagar.
