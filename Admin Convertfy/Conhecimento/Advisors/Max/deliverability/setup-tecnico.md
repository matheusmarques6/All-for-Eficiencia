---
tipo: procedimento
modulo: deliverability
assunto: setup-tecnico-dns
autor: max-sturtevant
registro: [slide, outro-narrador]
fonte: "CONTEUDO BRUTO/max.md — L8396-8412 (transcrição), L8667-8692 (slide)"
validade: "procedimento — o corpus não data a gravação. Extraído em 2026-09-06. Telas do Klaviyo, do provedor de domínio e do Glockapps podem ter mudado."
status: aprovado
---

O setup técnico de DNS que precisa estar pronto antes de enviar qualquer email: quais registros o material exige (SPF, DMARC, DKIM), o papel do branded sending domain no Klaviyo e como verificar se falta algum.


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

Nesta nota: o bloqueio ("do this before sending ANY emails", L8526), a lista de
registros (L8685-8689) e a linha sobre o Klaviyo configurar tudo (L8683-8684) vêm
do **deck** — artefato escrito de Max, e continuam valendo. As passagens faladas
(L8396-8398, L8408-8414) estão na faixa não-Max: a desdramatização do setup e a
delegação ao artigo do Klaviyo são do material do curso, não citáveis como fala
dele.

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
[[mapa-dos-conflitos]].

Além dos registros, o **branded sending domain** no Klaviyo — o slide chama de
"Dedicated Klaviyo sending domain" (L8673). Na fala (L8396-8398):

> It's basically where you hook up your Klaviyo settings with your domain
> settings and make sure that those match, make sure that those record match so
> that they recognize you as a real account and not spam and not something
> shady.

# A posição do material: provavelmente já está pronto

O setup é desdramatizado nos dois registros — no deck, que é de Max, e na fala,
que não é.

Fala (L8408): "it seemed very complex, but most domains already have the right
records in place."

Slide, verbatim (L8683-8684):

> Seems complex, but most domains already have the correct records in place on
> your domain, maybe one missing.
> **As you setup Klaviyo they set these all up for you :)**

Note a diferença de força: a fala diz que os registros costumam já existir; o
slide vai além e diz que o **Klaviyo configura tudo para você**. A fala não faz
essa afirmação.

# A fonte oficial indicada

Não é material próprio. O curso delega para o artigo do Klaviyo, citado duas vezes —
uma no resumo de deliverability (L8371) e outra como pré-requisito do warming
(L8525):

> **Technical Setup: [Setting up branded sending domain >>>](https://help.klaviyo.com/hc/en-us/articles/115000357752)**

O grau de confiança que a fala dá ao artigo (L8410-8414): é "the most forward
step-by-step", tem muita informação, e "if you follow the instructions
one-to-one, you're going to set yourself up for success". A fala diz que o próprio
Klaviyo aponta a direção dentro do produto, mas o artigo é mais profundo — e é o
que a agência manda para os clientes. Faixa não-Max: a rotina é da casa, não uma
preferência declarada por ele.

# Verificação

Glockapps, na variante domain-checker. Slide, verbatim (L8691):

> Use [https://glockapps.com/domain-checker](https://glockapps.com/domain-checker)
> to see if you are missing any, if you are follow their guide to getting
> installed.

Na fala o mesmo endereço sai degradado por ASR ("Glock apps. It's a domain
checker", L8414), descrito como o recurso para quando "we don't have the domain
information".

Isso é uma ferramenta diferente do teste de placement descrito em
[[auditoria-glockapps]], embora seja a mesma empresa: aqui o alvo é o registro
DNS, lá é onde o email cai.

# O que o corpus não diz

- O que SPF, DMARC ou DKIM fazem **individualmente**. Correção de escopo
  (varredura de falsos negativos): a versão anterior dizia "as siglas são
  listadas, nunca explicadas", e isso é falso fora deste módulo. O glossário de
  fundamentos as define em uma linha — "**DKIM / SPF / DMARC** – Email
  authentication protocols" (L452) — e o próprio deck daqui diz o que elas são
  fisicamente: "Fancy records hosted by your domain provider in your DNS
  settings (MX, SPF, DMARC, DKIM)" (L8671). Ou seja: o corpus diz que são
  protocolos de autenticação hospedados como registro de DNS no provedor de
  domínio; o que ele nunca diz é o que **cada uma** verifica nem em que ordem.
  Ver [[fundamentos/glossario-deliverability-e-plataforma]].
- Se o MX é requisito ou não (o slide se contradiz).
- Nenhum passo de tela, nenhum valor de registro, nenhum print. O procedimento
  inteiro é: leia o artigo do Klaviyo, cheque no Glockapps.
- Quanto tempo o setup leva ou quanto tempo o DNS demora a propagar.
