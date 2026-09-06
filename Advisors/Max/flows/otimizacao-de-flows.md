---
tipo: principio
modulo: flows
assunto: otimizacao-de-flows
autor: max-sturtevant
registro: [slide]
fonte: "CONTEUDO BRUTO/max.md — L4115-4177 (slide de flows); trechos duplicados em L9151-9180 (deck de otimização)"
conflitos: [flows-onde-testar]
status: rascunho
---

# O que é

A última seção do deck de flows, e **existe só no slide**. Não há transcrição
falada correspondente: a aula de Winback termina em L3396 e o corpus emenda
direto no Sunset Flow (L3398) e depois na parte GAMMA.

**Metade desta seção é duplicada.** Quatro dos cinco testes que o deck de flows
lista aparecem palavra por palavra no deck de otimização (L9151-9180). Eles
estão detalhados em [[otimizacao/_index]] e **não** são repetidos aqui — repetir
faria dois decks parecerem duas fontes independentes da mesma regra, e não são.
O mapa de âncoras está em `_staging/descartes-flows.md`.

O que segue é o que existe **só** neste deck.

# A tese: campanha é o campo de teste, flow é o arquivo

O argumento começa pelo problema de escala (L4117-4124), verbatim:

> **The Cons of Flow Optimization & A/B Testing**
>
> Considering you can have 30-50+ automated emails…
>
> * It's overwhelming
> * Hard to monitor at scale
> * Difficult to track and report at scale
> * Documenting is difficult

E a saída é não testar dentro do flow (L4126-4137), verbatim:

> **Long-Term Optimization Strategy**
>
> Rather than have a ton of active tests in flows of all sorts of different
> triggers, trying out different content, etc
> We mostly use campaigns as our testing ground.
> Try new angles and A/B test frequently in your email blasts.
> Rather than waiting for results like you have to do in flows, you can get near
> instant data with campaigns.
> We literally put full campaigns that perform well into our flows.
> Go back and edit your flow emails across all triggers to include the angle you
> saw work.
> If it's an an educational email on the product creation process, we'll add it
> to the Welcome Flow.
> If it's an email about how to get the most out of your product, add it to your
> Post Purchase Flow.
> If it's an email that goes over your return policy, add it to your cart
> abandon flow to reverse risk.
> Don't reinvent the wheel!

Esta é a única parte da seção sem cópia em nenhum outro lugar do corpus, e é a
tese central: o teste roda onde o sinal chega rápido (campanha) e o vencedor é
transplantado para onde o sinal chega devagar (flow).

O roteamento é por ângulo, não por métrica: campanha educacional sobre produção
vai para o welcome; campanha sobre uso do produto vai para o post-purchase;
campanha sobre política de devolução vai para o cart abandon, "to reverse risk"
(L4136).

# Long form vs short form — o único teste exclusivo daqui

Dos cinco testes listados, este é o único **sem** duplicata no deck de
otimização. Verbatim (L4147-4151):

> **Long Form vs Short Form**
>
> Especially for flows, we want to test longer form content vs shorter form.
> This will also apply to campaigns but especially in flows like abandonments
> when people have objections.
> Sometimes it makes sense to be quick and get an impulse purchase, other times
> it makes sense to spend time working through objections.

O racional do meio — "especially in flows like abandonments when people have
objections" (L4150) — é o único lugar do corpus onde ele liga tamanho de copy a
estágio de funil. Verificado: a frase não aparece em nenhuma outra linha do
bruto.

# Os quatro testes duplicados

Não repetidos aqui. Ficam nomeados só para roteamento:

| Teste | Neste deck | No deck de otimização |
|---|---|---|
| Flow Time Delays — "the biggest lever I'd say" | L4141-4145 | L9176-9180 |
| SLs and PTs | L4153-4162 | L9165-9174 |
| Graphic vs Text Based | L4164-4170 | L9151-9157 |
| Promoting Categories vs Products | L4172-4176 | L9159-9163 |

Ver [[otimizacao/_index]].

# O racional dele

O deck inteiro de flows monta especificações; esta seção desmonta a ideia de que
elas se otimizam sozinhas. A lógica é de velocidade de sinal: flow precisa
esperar volume acumular por gatilho, campanha entrega dado quase imediato
(L4131).

Isso também explica a insistência, em quase todas as notas de flow, de que o
cliente "will still be receiving campaign emails" ([[site-abandon]] L2367,
[[replenishment]] L4005, [[winback]] L3384-3386). Campanha não é o resto do
trabalho — é o laboratório.

# Onde o corpus discorda

**Onde testar.** Este deck diz que o teste sai do flow: "we mostly use campaigns
as our testing ground (…) rather than waiting for results like you have to do in
flows" (L4128-4131). E na mesma página, doze linhas depois, o teste de time
delay — que só existe dentro do flow — é "the biggest lever I'd say" (L4143),
frase que o deck de otimização repete idêntica (L9178). Ver `flows-onde-testar`
em [[_conflitos]].

**Uma tensão de cobertura.** O deck manda testar time delay como maior alavanca
e o corpus não declara delay nenhum para cart abandon nem para checkout abandon
— justamente os dois flows de maior intenção. Não há o que testar a partir do
corpus. Site abandon só tem o delay do primeiro email (L2369-2375), nada entre o
1 e o 2.

# O que o corpus não diz

- Nenhum tamanho de amostra, duração de teste ou limiar de significância.
- Nenhum critério para decidir quando um vencedor de campanha "merece" entrar no
  flow.
- Nenhuma métrica de decisão — nem open rate, nem clique, nem receita.
- Nada sobre a ferramenta de A/B do Klaviyo, apesar de o deck inteiro assumir
  Klaviyo.
- Os dois slots de exemplo do slide vieram vazios: "Example of Text Based sale
  email winner:" (L4170) e "Example of categories performing better:" (L4176).
