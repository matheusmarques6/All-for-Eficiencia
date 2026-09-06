---
tipo: principio
modulo: deliverability
assunto: o-que-e-deliverability
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L8382-8396 (transcrição), L8655-8679 (slide)"
status: rascunho
---

# O que é

Deliverability é **onde** o email cai, não se ele foi enviado. Três destinos
possíveis, e só três (L8386-8388, L8659-8661):

| Destino | Quando |
|---|---|
| **primary tab** | credit score bom — "what everybody checks where you obviously want to be" (L8386) |
| **promotions tab** | "if you're somewhere in the middle" (L8388, L8661) |
| **spam** | credit score ruim — "where nobody's going to read you" (L8388) |

A justificativa do lado do provedor, no slide (L8657): "Inbox providers want to
improve the experience of their customers by only showing them emails they want
to see."

# A analogia central: credit score

É a imagem que sustenta a pasta inteira. "When you think or hear
deliverability, think of it like a credit score, essentially" (L8382). A
inversão está na linha seguinte: **os inbox providers ocupam o lugar dos
bancos**.

> But instead of with Visa or Amex or Discover, Chase, it's actually with the
> inbox providers. So Google, Yahoo, iCloud, Hotmail, if anyone still uses
> that. But deliverability is essentially a credit score, but it tracks your
> sender reputation. (L8384)

O slide fecha a mesma imagem em uma linha: "Deliverability essentially refers to
your domain and IP's sending 'credit score'" (L8658) — note que o slide inclui
**IP**, que a fala não menciona.

A analogia volta do outro lado, com a construção do score: se a Chase vê que
você paga em dia, ela te trata como responsável; se o Google vê que abrem,
clicam e respondem seus emails **consistentemente ao longo do tempo**, você
constrói o que ele chama de infraestrutura (L8418-8422).

# Só duas coisas afetam

"There's two things essentially that affect deliverability" (L8396). O slide
nomeia as duas com o que cada uma soma (L8667-8679):

| | O que é | O que soma |
|---|---|---|
| **Technical Setup** | "Fancy records hosted by your domain provider in your DNS settings (MX, SPF, DMARC, DKIM)" | "+ Dedicated Klaviyo sending domain" |
| **Sender Reputation** | "A combination of your email engagement metrics (open rates, click rates, bounce rates, spam complaints)" | "+ Proper domain warm-up" |

Setup técnico em [[setup-tecnico]]; warm-up em [[warming-do-dominio]].

# O Google só vê métrica

O ponto de doutrina mais importante da nota: **o provedor não julga o conteúdo,
julga o número**. "They only see the metrics, and they're saying these people
have engaging content, people are interacting with it" (L8392).

O exemplo dele é aritmético (L8390): 20% abrindo → "this isn't someone with good
content. This might be spam (…) Why would I put this in someone's primary
inbox?". 50% abrindo e 1% clicando → o oposto. O slide comprime isso numa
pergunta retórica (L8665): "If 2/10 people are opening your emails… you think
they'll keep putting you in their main inbox?"

A demonstração aparece de novo no caso real de warming (L8621-8622), onde ele
literalmente narra a leitura do Google como uma conta: quantos receberam,
quantos abriram, quantos clicaram — "It doesn't look like it's spam."

# A analogia do algoritmo do Instagram

Ele usa uma segunda analogia para dizer que não há nada de especial em email
(L8392-8394): "at the end of the day, Google's just like any other app. It
rewards positive engagement. It really just rewards engagement."

> The same way that if you're on Instagram and a video starts to blow up,
> starts to get 1,000 likes, 10,000 likes, 50,000 likes, 100,000 likes,
> Instagram's going to put that in front of more people because it sees people
> are engaging with it. Same sort of deal over email, same thing with your
> inbox provider. (L8394)

# O que o corpus não diz

- Como o provedor pondera cada métrica entre si.
- O que é "IP" nesse contexto, ou como ele difere de domínio — o termo aparece
  uma vez só, no slide (L8658), e nunca é explicado.
- Se o comportamento descrito vale igual para Google, Yahoo, iCloud e Hotmail.
  Ele lista os quatro juntos (L8384, L8394) e nunca os separa.
