---
tipo: especificacao
modulo: otimizacao
assunto: pre-condicao-e-conclusividade
autor: max-sturtevant
registro: [slide, outro-narrador]
fonte: "CONTEUDO BRUTO/max.md — L8774-8828 e L9096-9108 (transcrição), L9116-9141 (slide)"
conflitos: [otimizacao-peso-do-basico, otimizacao-frequencia-precondicao, otimizacao-lista-pequena-quantas-repeticoes, otimizacao-onde-testar]
status: rascunho
---


# Aviso de autoria

**Faixa L8773-9109 (toda a fala do módulo de otimização) — `outro-provavel`.**
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

Nesta nota: o slide (L9116-9141) é artefato escrito de Max e continua valendo. Toda
a fala — a pré-condição de L8786-8790, a tabela de conclusividade por volume
(L8802-8812), o fecho de L9096-9102 — está na faixa não-Max e **não é citável como
fala dele**. A referência cruzada ao deck de flows (L4126-4132) é slide, sem
problema de voz.

# O que é

A porta de entrada do módulo: A/B test não é o que faz o resultado, é o que
sobra depois que o básico está de pé — "you're not going to CRO your way to 10x"
(L8778), e o slide dá o mesmo título, "You Can't Conversion Rate Optimize Your
Way To a 10x…" (L9118). O princípio está em
[[doutrina/o-basico-entrega-90-por-cento]]; aqui fica a mecânica.

# A pré-condição

Fala, verbatim (L8786-8790):

> Primary focus is getting the bases in place, getting all your base flows live,
> getting three to four campaigns a week up and running, doing that consistently,
> then start opening things up to more testing and optimizing.

O fecho da aula repete a lista com um item a mais — pop-up — e outro número
(L9096-9102): "80% of your results are going to come from setting up the basis
of sending consistent campaigns, setting up the base flows, getting your pop-up
running, getting deliverability good, yada, yada, yada. And then after you have
all that in place, then you really start optimizing." Slide (L9122-9123): "It's
important to not get too carried away with A/B testing if you don't have all the
cores in place. Focus on high levers first and spend your time there."

**Lista pequena não é impedimento, é despriorização.** Com "5,000, 10,000,
20,000 people": "You're still probably going to see some results. I wouldn't say
don't A-B test, but it shouldn't be the primary focus" (L8782-8786).

# Conclusividade se mede por volume, não por tempo

A pergunta que o material diz receber, e a resposta (L8814-8816):

> how long should I run an A-B test for? How many times should I run it before
> it's conclusive? Base it off the number of recipients that are receiving.

| Tamanho da lista | O que o corpus manda | Linha |
|---|---|---|
| 1.000, divididos em 500/500 | "I wouldn't say that is enough data to make a sound conclusion" | L8802-8804 |
| 100.000 / 200.000 / 500.000 | "sending one, maybe two at different times and get pretty conclusive results" | L8806-8810 |
| 5.000 a 10.000 | "you might want to test that three or four times" | L8810-8812 |

Slide (L9138-9139): "it's important to make sure you have the proper volume to
know your results are conclusive. If you need to send multiple emails to get
enough data to make a conclusion, that's fine."

O critério de parada é repetição do mesmo resultado — "especially if you're
constantly seeing the same results" (L8820). O material aplica isso ao próprio
caso: o teste de send time venceu por 5x e ainda assim "I probably run it one or
two more times just to confirm what we're seeing here" (L8854).

# Duas consequências

**O resultado é da conta, não do mercado**: "the results based off a certain A-B
test are going to be different based off your brand, based off the list, based
off the type of audience or customer that you're speaking to" (L8820-8824) — por
isso esta pasta guarda casos, não benchmarks. **A escolha do teste é por
alavanca**: "It is hard to choose, but you're going to want to start with the
highest leverage test" (L8826; slide L9140-9141), e o topo declarado é
[[flow-time-delays]] — "This is the biggest lever I'd say" (L9178).

# Onde o corpus discorda

- Peso do básico: 90/10, "80, 90%"/"10, 20%" e 80% — `otimizacao-peso-do-basico`.
- Pré-condição de campanha aqui é "three to four campaigns a week" (L8788), e o
  módulo de campanhas trabalha com 2-4: `otimizacao-frequencia-precondicao`.
- Lista de 5-10k: "shouldn't be the primary focus" (L8784) e, logo adiante,
  "test that three or four times" (L8810-8812):
  `otimizacao-lista-pequena-quantas-repeticoes`.
- O deck de flows diz que o campo de teste são as campanhas, não os flows
  (L4126-4132): `otimizacao-onde-testar`.

# O que o corpus não diz

Nenhum limiar estatístico — sem significância, p-valor ou amostra mínima além
dos números acima; nada sobre quantos testes rodar em paralelo. A frase
L8818-8820 sai emendada no ASR ("the larger the sample size, the more times you
run it, the more conclusive"): não separa amostra de repetição.
