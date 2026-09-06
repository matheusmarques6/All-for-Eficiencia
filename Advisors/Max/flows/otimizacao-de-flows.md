---
tipo: principio
modulo: flows
assunto: otimizacao-de-flows
autor: max-sturtevant
registro: [slide]
fonte: "CONTEUDO BRUTO/max.md — L4115-4177 (slide)"
status: rascunho
---

# O que é

A última seção do deck de flows, e **existe só no slide**. Não há transcrição
falada correspondente: a aula de Winback termina em L3396 e o corpus emenda
direto no Sunset Flow (L3398) e depois na parte GAMMA. Tudo abaixo é `registro:
slide`, sem julgamento falado por trás — exceto onde marcado.

# A tese: campanha é o campo de teste, flow é o arquivo

O argumento começa pelo problema de escala (L4119-4124), verbatim:

> Considering you can have 30-50+ automated emails…
>
> * It's overwhelming
> * Hard to monitor at scale
> * Difficult to track and report at scale
> * Documenting is difficult

E a saída é não testar dentro do flow (L4128-4137), verbatim:

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

O critério de roteamento é por ângulo, não por métrica: o que venceu numa
campanha educacional vai para o welcome; o que venceu sobre uso do produto vai
para o post-purchase; o que venceu sobre política de devolução vai para o cart
abandon, "to reverse risk" (L4136).

# Os testes que ele diz valer a pena dentro do flow

Quatro, nesta ordem no deck.

**1. Time delays (L4141-4145).** Ele mesmo marca como o mais importante: "This
is the biggest lever I'd say." Duas variáveis: o tempo entre a ação do cliente e
o primeiro email, e o tempo entre os emails do flow.

**2. Long form vs short form (L4147-4151).** "Especially for flows, we want to
test longer form content vs shorter form. (…) especially in flows like
abandonments when people have objections. Sometimes it makes sense to be quick
and get an impulse purchase, other times it makes sense to spend time working
through objections."

**3. Subject lines e preview texts (L4153-4162).** Ele registra o custo desse
teste: "this is the obvious one, but hard to take the learnings and apply to
future emails since there will be a lot of variation" (L4155). Os testes que dá,
verbatim:

> * Including discount vs not including (for sales)
> * Including or excluding emojis
> * Ilusing "…" or exlcuding
> * Adding time delays
> * Using all caps vs not

*(Os erros de digitação são do original, incluindo "Ilusing" por "Including" e
"Adding time delays" numa lista de testes de subject line.)*

**4. Graphic vs text based (L4165-4169).** "Heavy text based emails vs graphic
based emails can really vary across accounts. Test out different styles to see
what your list responds to better. Especially for big drops and sales… We find
that you want to mix them up but use text based for key emails."

**Bônus — promoting categories vs products (L4173-4175).** "We've noticed that
some brand customers prefer to shop in their emails by category and some by
individual products. Important to mix it up but you can bias one option more,
especially for important emails, if it performs better."

# O racional dele

O deck inteiro de flows monta especificações; esta seção desmonta a ideia de que
elas se otimizam sozinhas. A lógica é de velocidade de sinal: flow precisa
esperar volume acumular por gatilho, campanha entrega dado quase imediato
(L4131). Então o teste roda onde o sinal chega rápido e o vencedor é
transplantado para onde o sinal chega devagar.

Isso também explica a insistência, em quase todas as notas de flow, de que o
cliente "will still be receiving campaign emails" ([[site-abandon]] L2366-2369,
[[replenishment]] L4005, [[winback]] L3384-3387). Campanha não é o resto do
trabalho — é o laboratório.

# Onde o corpus discorda

Nada contradiz esta seção diretamente, porque nada mais fala dela. Mas há uma
tensão de registro: o deck manda testar time delay como maior alavanca (L4143) e
o corpus não declara delay nenhum para cart abandon nem para checkout abandon —
justamente os dois flows de maior intenção. Não há o que testar a partir do
corpus. Site abandon só tem o delay do primeiro email (L2369-2373), nada entre o
1 e o 2.

# O que o corpus não diz

- Nenhum tamanho de amostra, duração de teste ou limiar de significância.
- Nenhum critério para decidir quando um vencedor de campanha "merece" entrar no
  flow.
- Nenhuma métrica de decisão — nem open rate, nem clique, nem receita.
- Os dois slots de exemplo do slide vieram vazios: "Example of Text Based sale
  email winner:" (L4170) e "Example of categories performing better:" (L4176).
- Nada sobre ferramenta de A/B do Klaviyo, apesar de o deck inteiro assumir
  Klaviyo.
