---
tipo: especificacao
modulo: flows
assunto: sunset-flow
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L92-94 e L5127 (transcrição), L411 (slide, glossário), L3398-3402 (seção sem aula); definição do segmento lida do PNG embutido na L9545, referenciado por `![][image1]` na L3402"
status: rascunho
---

# O que é

**Cobertura parcial, não lacuna total.** O corpus entrega a finalidade e a
definição do segmento. Não entrega sequência, delays, número de emails nem copy.

Finalidade, verbatim do glossário (L411):

> **Sunset Flow** – Triggered when a contact is no longer engaging. Removes or
> suppresses inactive users.

Ele também aparece na lista dos oito flows configurados na conta de exemplo do
Klaviyo — "Browse Abandon, Cart Abandon, Checkout Abandon, Post Purchase, Side
Abandon, Sunset, Welcome, Win Back" (L92) — que ele chama de "the recommended
flows when just starting out" (L94). Ou seja: ele recomenda e não ensina.

# A definição do segmento

> **Lido de print, não de texto.** A seção do Sunset Flow (L3398-3402) traz um
> `![][image1]` que **resolve**: a referência aponta para a L9545, última linha
> do arquivo, onde está `[image1]: <data:image/png;base64,…>` com um PNG de
> 624×169. É a única imagem do arquivo inteiro. Print de baixa resolução, lido
> por ampliação; onde a leitura é duvidosa, está marcado abaixo.

Print do Klaviyo. Segmento salvo com o nome `WC | Sunset`, tipo Segment,
**93726** perfis, `Nov 13, 2024, 9:49 AM`. Quatro condições, verbatim:

> * Person has Opened Email zero times in the last 180 days
> * **AND** Person has Clicked Email zero times in the last 180 days
> * **AND** Person has Received Email is at least 10 over all time
> * **AND** Person has Placed Order zero times over all time

Leitura confiável nas quatro condições e no nome do segmento. **Incerto:** o dia
da data (`13` pode ser `18`) e se `93726` traz separador de milhar — o glifo tem
7 px de altura e não decide. Perfis e data são de uma conta de cliente, não são
especificação.

**A quarta condição é a única surpresa útil.** `Placed Order zero times over all
time` exclui do sunset qualquer pessoa que já tenha comprado uma vez. Quem
comprou e sumiu vai para o [[winback]], não para o sunset. O corpus nunca diz
isso em texto; o segmento diz.

# Onde isso não fecha com o resto do corpus

Em L5127, dentro da aula de segmentação e falando da **suppression list**, ele
promete: "We'll talk about this more in the Sunset Flow, obviously, as well."
A promessa nunca é cumprida. E os três limiares de inatividade que o corpus dá
não coincidem:

| Onde | Limiar | reg | linha |
|---|---|---|---|
| Segmento do print | 0 opens **e** 0 clicks em 180 dias · ≥10 emails recebidos · 0 pedidos over all time | print | L9545 |
| Suppress list (fala) | "at least five to ten emails over all time, opened zero times in the last year" | transcrição | L5129 |
| Suppress list (slide) | ≥5 recebidos · 0 aberturas em 365 dias · **OU** ≥3 bounces · **OU** ≥1 spam | slide | L5592 |

Sunset e suppress list não são a mesma coisa, mas ele os apresenta juntos e dá
números diferentes para cada um sem reconciliar. Não fazer média nem transpor um
limiar para o outro.

# O que o corpus não diz

- **Nenhuma sequência.** Zero emails especificados: sem contagem, sem delay, sem
  subject line, sem template, sem exemplo.
- **Nenhum filtro e nenhuma condição de saída.**
- **Remove ou suprime?** O glossário diz "removes or suppresses" (L411) e nunca
  escolhe, nem diz o que decide entre os dois.
- **O deck não veio.** L3400 aponta para um gamma próprio
  (`Sunset-Flow-v13borkcrsurvpv`), diferente do `Email-Flows-nccnz3vebo4vyy1`
  dos outros sete flows. O conteúdo desse deck não está no corpus.
- **Não há aula.** Nenhuma transcrição de vídeo, e nenhuma seção correspondente
  na parte GAMMA (L3404-4186): depois do Winback (L4040-4114) o deck vai direto
  para Flow Optimization (L4115).

# Como responder

Recusa **parcial**, conforme [[_protocolo]]: entregar a finalidade (L411) e o
segmento (print da L9545, sempre marcando que é print), e nomear o que falta.
Quem perguntar "quantos emails tem o sunset flow" ou "o que escrever nele"
recebe a lacuna — nunca uma sequência montada por analogia com [[winback]] ou
com o material de deliverability.
