---
tipo: especificacao
modulo: deliverability
assunto: segmento-engajado
autor: max-sturtevant
registro: [slide, outro-narrador]
fonte: "CONTEUDO BRUTO/max.md — L8456-8482 (transcrição), L8721-8734 (slide)"
conflitos: [deliverability-limiar-de-open-rate, deliverability-lista-base-padrao]
status: rascunho
---


# Aviso de autoria

**Faixa L8381-8646 (toda a fala do módulo de deliverability) — `outro-provavel`.**
Sem prova nominal. A classificação é **estilométrica**: o bloco pertence ao aglomerado
do único bloco `outro-provado` e não traz um só marcador do idioleto de Max.
`outro-provavel` não é `outro-provado` — não está provado que a voz não é dele, está
estabelecido que é muito improvável ([[_autoria]] §7.3).

Critério: **idioleto** ([[_autoria]] §2.1) — ausência de "I recommend", "my favorite"
e "I like to", presença de "at the end of the day" e "obviously", e o fecho coletivo
"thank you guys… see you in the next one". **A saudação de abertura não é critério e
não pode ser citada como evidência:** o laudo testou e ela caiu — o walkthrough de
Figma abre com "Hello, hello" e é comprovadamente Max, que em L7817 digita `@max` e
diz "tags me" ([[_autoria]] §5).

Nesta nota: a definição verbatim do 90 Day Engaged List (L8732-8734) e a regra de
ajuste (L8725-8729) são **slide** — artefato de Max, e prevalecem em especificação.
As formulações faladas (L8456-8482) estão na faixa não-Max: o endurecimento da
regra, o exemplo de aperto e a exceção das listas largas são do material do curso,
**não citáveis como fala dele**.

# A regra

"You only want to be sending to your engage list" (L8458). A versão com ressalva,
uma linha antes: "you want to be mainly and almost exclusively sending to your
engage list" (L8456) — o "keeping things simple" (L8458) é a razão declarada do
endurecimento imediato da regra.

O motivo, no slide (L8723): a lista inteira contém gente que nunca vai abrir —
"they changed emails, they stopped checking, lost interest in your brand, or
maybe even they gave you a fake email". Na fala (L8482): "If you send to
unengaged people, it'll hurt your engagement rate. Google notices. Then like I
said, you start landing in your spam folder."

E a promessa de suficiência, verbatim (L8730):

> This is all you need to maintain deliverability.

# O segmento base, verbatim

Slide, tabela completa (L8732-8734). Definição em inglês, nunca traduzir:

> | Segment Name | Segment Definition | Segment Use Case |
> | ----- | ----- | ----- |
> | **90 Day Engaged List** (You can use any time frame, 90 is recommended to start) | Someone can receive email marketing because person is subscribed**AND** Someone has Opened Email at least once in the last 90 days**OR** Someone has been Active on Site at least once in the last 90 days**OR** Someone has Placed An Order at least once in the last 90 days | This is your base segment for sending all your email campaigns to. We want to only send emails to our active subscribers so we keep high open rates and click rates. If we send to unengaged people they will hurt our engagement rates, Google will notice, and we will land more often in the spam folder. |

Estrutura: uma condição obrigatória (`can receive email marketing` /
`is subscribed`) **AND** três condições alternativas em **OR** — abriu email,
esteve ativo no site, ou fez pedido, cada uma na mesma janela.

> **Nota de transcrição do verbatim.** No bruto, L8734 é a **única linha da faixa
> inteira** que usa quebras de linha internas de célula (caractere `VT`, 0x0B) —
> três delas, exatamente antes de cada `**AND**` / `**OR**`. Em texto corrido
> elas somem e as palavras colam (`subscribed**AND**`). O conteúdo acima é
> idêntico ao bruto caractere a caractere **exceto** por esses três caracteres de
> controle: eles são quebra de linha do export do GAMMA, não parte da definição.
> A definição de fato tem quatro linhas, uma por condição.

A janela é um parâmetro, não uma constante: "Logic stays the same. You just
change the 90 to a 60" (L8480). Vale para 30, 60, 90, 120, 180 ou 365 dias
(L8460, L8726).

> **A versão falada dessa definição está corrompida.** Em L8478 o ASR colapsa a
> condição de inscrição em "someone has placed order at least once" e a repete no
> fim. Use só a do slide. Registrado em [[_registro/descartes-deliverability]].

# A regra de ajuste

Slide, verbatim (L8725-8729) — as quatro linhas seguidas, porque o número muda
dentro delas:

> This is how we can get consistent 50% open rates.
> Use either a 30, 60, 90, 120, 180, or 365 day engaged list.
> Whatever list gets you 50-60% opens.
> If you start to get 60%+ opens, widen your list to a larger timeframe to get
> more opportunities for revenue.
> If you start to get 40% opens, tighten your list to a smaller timeframe.

Um limiar para cada lado: **60%+ alarga, 40% aperta**. E um objetivo declarado
para alargar que não é deliverability — é receita: "to get more opportunities for
revenue" (L8728).

Mas note a escada dentro do próprio slide: ele promete **50%** (L8725), manda
escolher a lista por **50-60%** (L8727) e só alarga em **60%+** (L8728). Três
números em quatro linhas, no registro que o protocolo faz vencer em
especificação. Não é possível responder "qual é o limiar" com um número só.

A fala dá a mesma mecânica com números diferentes (L8468-8470): "the way that
you'll know if you're sending to the right one is if you're consistently
receiving 50 to 60% opens. If you start to get 40% opens or things start to drop
in a significant way, tighten the list up."

O exemplo de aperto (L8472-8474): estava em 30 dias com ~65% de abertura,
expandiu para 120 e caiu para 30% — "We need to tighten this up. Maybe 90 is a
good place to go, but probably want to go back to your 60 day." A ordem final
("probably 60") contradiz a sugestão imediatamente anterior ("maybe 90"), e a fala
não escolhe.

O motivo de voltar e não insistir (L8476): "if you start sending to the wrong
list too many times, you start, your deliverability starts to" — a frase morre
aí na transcrição.

# Listas largas são para grandes datas

A exceção à regra, e a única declarada (L8462-8466):

- envio normal → "you might only want to send to your 60 day engage list" (L8462)
- venda grande, "It's Black Friday, especially, but let's say I have a 4th of
  July sale running and you want to reach more people" → "That's where you start
  tapping into the 180, 365 day engage list" (L8464-8466)

# Onde o corpus discorda

- **Limiar de open rate.** Não há um número, e **o slide não desempata porque
  discorda de si mesmo em quatro linhas**: "consistent 50% open rates" (L8725),
  "Whatever list gets you 50-60% opens" (L8727), "60%+ opens, widen your list"
  (L8728). A fala dá 50-60% como zona de acerto (L8468) e, na aula de warming,
  50+ (L8579), 40-50 (L8580), 45-50+ (L8582), 40-50 (L8588) e 40-50 de novo na
  correção de rota (L8604). São **dez formulações**, todas em
  `deliverability-limiar-de-open-rate` em [[_conflitos]].
- **Lista base padrão.** O slide recomenda 90 dias como ponto de partida
  (L8734); a fala usa 60 dias como envio normal (L8462).

# O que o corpus não diz

- Como construir o segmento no Klaviyo. A definição é lógica, não é tela.
- Se `Active on Site` e `Placed An Order` dependem da integração Shopify.
- Quanto tempo esperar entre um ajuste de lista e o próximo — só "if you start
  to get" (L8728-8729), sem número de envios.
- O que fazer com quem fica de fora do segmento. **Não há sunset flow nesta
  pasta** — mas há fora dela, e é o vizinho a oferecer em vez de recusar:
  finalidade no glossário (L411) e a definição do segmento no print da L9545
  (180 dias sem abrir · 180 sem clicar · ≥10 emails recebidos · 0 pedidos),
  em [[flows/sunset]]; e a **Suppress List** completa do deck de campanhas
  (L5592), em [[campanhas/segmentacao]]. O que continua faltando é a sequência
  do sunset e a decisão entre "remove **or** suppress".
