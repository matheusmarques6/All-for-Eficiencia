---
tipo: especificacao
modulo: campanhas
assunto: frequencia-de-envio
autor: max-sturtevant
registro: [slide, outro-narrador]
fonte: "CONTEUDO BRUTO/max.md — L4220, L4238-4296 e L4404-4406 (transcrição), L4191-4192 (bullets do módulo), L5247-5249 e L5252-5298 (slide)"
conflitos: [campanhas-sweet-spot-de-frequencia, campanhas-tier-250k-1m, campanhas-o-que-determina-a-frequencia]
status: rascunho
---


# Aviso de autoria

**Faixa L4202-4421 (Campaign Strategy) — `outro-provavel`.**
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

Nesta nota: **a tabela receita × tráfego (L5295-5298), o piso de 2x (L5256) e o
"3x per week is typically the sweet spot" (L5255) são slide** — artefato escrito
de Max, e prevalecem em especificação. Tudo o que vem da fala — o "two to four …
sweet spot" (L4220, L4242, L4404), o tier "three to four" (L4268), o gate por
tamanho de lista (L4276) e a carga da equipe (L4244) — está na faixa não-Max e
**não é citável como fala dele**. Os bullets do módulo (L4191-4192) são texto
escrito, não fala. Consequência registrada em [[_autoria]] §6.2 e em
[[_numeros]]: a corroboração falada do 3x/semana continua existindo, mas vem de
L2367 (Site Abandon Flow, faixa Max), não daqui.

# O que é

Campanha é o envio pontual, numa data e hora específicas, para a lista
(L4191, L5247). A pergunta de frequência é, segundo a aula, "one of the questions
we get the most" (L4238).

# A especificação

Tabela do slide — receita mensal **OU** visitantes mensais; se o brand cai em
uma das duas colunas, use a frequência da linha (L5290):

| Store Revenue | Monthly Site Visitors | Email Frequency |
|---|---|---|
| $0-50k/mo | 0-25k/mo | 2x per week |
| $50k-250k/mo | 25k-50k/mo | 3x per week |
| $250k-1M/mo | 50k-250k/mo | 4x per week |
| $1M/mo+ | 250k/mo+ | 5-6x per week |

(L5295-5298, verbatim)

**Piso absoluto:** "I wouldn't recommend going lower than 2x per week no matter
your ecom store size" (L5256).

**O tamanho da lista também limita.** Com 5.000, 10.000 ou 20.000 pessoas na
lista, o material manda não enviar 5-6x por semana, porque o envio real acaba
concentrado num segmento de "four or 5,000 people" que se cansa (L4276-4280).
Esse gate não existe na tabela do slide.

# Por que os extremos falham

**1-2x por semana** (L4238, L5258-5262): o cliente esquece a marca; não se
forma o hábito de abrir; dinheiro deixado na mesa.

**5-7x por semana** (L4240-4242, L5264-5269): mais unsubscribes; clientes
irritados; a mensagem se dilui; a receita atinge platô — "diminishing returns"
(L4242). Exceção declarada: em $1M+/mês dá para sustentar 5-6x *porque a lista
cresce e a segmentação permite não enviar sempre para as mesmas pessoas*
(L4270-4276).

**2-4x por semana** (L5271-5276): mais receita, unsubscribes baixos, top of
mind, "every email you send has equal weight and impact".

Fator extra que só aparece na fala: carga de trabalho criativa da equipe —
2-4x/semana é o que se sustenta operacionalmente (L4244).

# Onde o corpus discorda

- **Sweet spot.** A fala — não-Max — diz "two to four times per week is really
  hitting the sweet spot" (L4242, repetido em L4220 e L4404-4406). O slide diz "3x per week is
  typically the sweet spot" (L5255) e, na mesma página, mantém a cadência
  "2-4 email campaigns per week" (L5249). Ver `campanhas-sweet-spot-de-frequencia`.
- **Tier $250k-1M.** Fala: "probably in that three to four emails a week"
  (L4268). Slide: `4x per week` (L5297). Ver `campanhas-tier-250k-1m`.
- **O que determina a frequência.** O slide decide por receita OU tráfego
  (L5290). A fala acrescenta tamanho de lista (L4276) e carga da equipe
  (L4244). Ver `campanhas-o-que-determina-a-frequencia`.

# O que o corpus não diz

Não há critério para quando subir de tier além do próprio número de
receita/tráfego. Não há regra de rampa **de frequência**: o corpus não diz em
quanto tempo passar de 2x para 4x.

**Correção de escopo (varredura de falsos negativos).** Duas frases desta seção
diziam mais do que podiam.

- **Dia e horário existem, em outro módulo.** O que não os tem é *esta faixa*.
  Horário: "Typically, we've found around **11am-12pm** to perform the best.
  Main times to test would be 9am, 12pm, 2pm, and 4pm" (L9148, slide), com caso
  real de 11h contra 13h45 (L8846-8852). Dia da semana: não há dia prescrito,
  mas há **método** — "you can always export all the data from Klaviyo (…)
  placed order, average placed order and break things down by day"
  (L9034-9036). Ver [[otimizacao/send-time]] e [[otimizacao/outros-testes]].
- **Rampa existe, mas é de volume, não de frequência.** O módulo de
  deliverability prescreve uma: "start small, gradually increase from 25 to 50
  percent based on performance" (L8556) e a cadência de warming "3-4x por
  semana" (L8557), com o caso de 1.000 → 120.000 em 60 dias (L8607-8622). É o
  vizinho a oferecer, marcando que **é rampa de destinatários, não de número de
  campanhas por semana**. Ver [[deliverability/warming-do-dominio]].

# Ligações

[[ocupar-espaco-mental]] · [[mix-grafico-e-texto]] · [[segmentacao]]
