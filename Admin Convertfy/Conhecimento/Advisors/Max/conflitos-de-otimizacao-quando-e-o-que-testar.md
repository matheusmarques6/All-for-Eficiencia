---
tipo: indice
modulo: otimizacao
assunto: conflitos-otimizacao-quando-e-o-que-testar
autor: max-sturtevant
conflitos: [otimizacao-peso-do-basico, otimizacao-frequencia-precondicao, otimizacao-lista-pequena-quantas-repeticoes, otimizacao-horarios-a-testar]
status: aprovado
---

Registro dos conflitos do módulo `otimizacao` do corpus de Max Sturtevant sobre quando e o que testar: o peso do básico contra o avançado, frequência como pré-condição do teste, quantas repetições numa lista pequena e quais horários testar. Cada entrada lista os valores divergentes por registro e fecha com um "Como responder".


Faixa: L8760-9109 (transcrição) e L9110-9211 (slide GAMMA). O registro `resumo do
módulo` é o bloco de bullets da página do curso (L8760-8769) que antecede a
transcrição e termina no link para o deck (L8769) — **não é slide GAMMA**. Essa
distinção decide o primeiro conflito abaixo. `otimizacao-onde-testar` resolve para
`flows-onde-testar` ([[_conflitos#Conflitos entre módulos]]);
`otimizacao-sl-julgar-por-abertura-ou-receita` está em [[#Conflitos dentro do mesmo
registro]]; `otimizacao-teto-de-abertura` resolve para `copy-open-rate-limite`.


## otimizacao-peso-do-basico

Absorve `doutrina-proporcao-basico-avancado`. **Veredicto arbitrado nesta
consolidação** — as duas unidades divergiam; ver a seção
[[#Colisões de slug e veredictos arbitrados]].

| Valor | Registro | Linha |
|---|---|---|
| "90% of results are driven by basics, 10% come from the advanced 'stuff.'" | resumo do módulo | L8764 |
| "80, 90% of the results are driven by the basics. The 10, 20% come from that advanced stuff." | **outro-narrador** (`outro-provavel`) | L8778-8780 |
| "90% of the results are driven by the basics. / 10% come from the advanced stuff." | slide | L9120-9121 |
| "that 80% of your results are going to come from setting up the basis" | **outro-narrador** (`outro-provavel`) | L9098 |

**Como responder:** **90/10** é o número de registro. Três motivos, nesta ordem:

1. É a versão do deck GAMMA (L9120-9121), que é artefato escrito dele, e do bloco de
   resumo da página do curso que aponta para esse mesmo deck (L8764 → L8769). Não são
   duas fontes independentes: são o deck e o resumo do deck.
2. O conflito é sobre **número**, e a precedência do [[_INDEX]] dá o slide.
3. As duas versões que dizem 80% (L8778-8780 e L9098) estão dentro do bloco de fala
   L8762-9109, classificado **`outro-provavel`** por [[_autoria]] — por **idioleto**:
   zero "I recommend" / "my favorite" / "I like to", "obviously" 9×, fecho coletivo
   "hit us up" em L9108. Não são citáveis como fala do Max.

Dê 90/10 e registre que a fala do módulo abre a faixa para "80, 90%" na abertura e
fecha em 80% no encerramento — marcando que essa fala é de atribuição duvidosa.
**Nunca dar "85%" nem "cerca de 90%".** O ponto que não muda em versão nenhuma é a
consequência prática, e é ela que importa mais que o número: A/B test é etapa 2, e a
etapa 1 é a lista de básicos de L8786-8790 e L9098-9100.


## otimizacao-frequencia-precondicao

Ver também [[_conflitos#Conflitos entre módulos]], onde a frequência de campanha aparece com
todas as versões dos cinco módulos.

| Valor | Registro | Linha |
|---|---|---|
| "getting three to four campaigns a week up and running" (pré-condição para testar) | **outro-narrador** | L8788 |
| "We need a consistent cadence of 2-4 email campaigns per week" | slide (campanhas) | L5249 |
| "two to four campaigns per week is generally going to be the sweet spot" | **outro-narrador** (campanhas) | L4220 |
| "3x per week is typically the sweet spot" | slide (campanhas) | L5255 |
| tabela por faturamento: 2x / 3x / 4x / 5-6x por semana | slide (campanhas) | L5295-5298 |
| "ideally 3 to 4 times per week" | **outro-narrador** (deliverability) | L8557 |

**Como responder:** a faixa oficial do corpus é **2-4/semana** e pertence ao módulo
de campanhas (`campanhas-sweet-spot-de-frequencia`). O módulo de otimização usa
**3-4** como o patamar que precisa estar rodando **antes** de abrir testes — é uma
pergunta diferente (pré-condição de teste, não cadência recomendada), mas os números
não batem, e responder "2-4" a quem pergunta "quando posso começar a testar" perde a
informação. Dê as duas com o papel de cada uma. O critério real dele não é número
único: é faturamento e tamanho de lista (tabela L5295-5298).


## otimizacao-lista-pequena-quantas-repeticoes

| Valor | Registro | Linha |
|---|---|---|
| com "5,000, 10,000, 20,000 people", testar "shouldn't be the primary focus" | **outro-narrador** | L8782-8786 |
| com lista de "5,000 to 10,000", testar "three or four times" para concluir | **outro-narrador** | L8810-8812 |

**Como responder:** não é conflito de número, é de prioridade — a mesma faixa de lista
aparece como "não é onde você deve gastar tempo" e, um minuto depois, com receita de
repetição. Leitura consistente: com lista pequena o custo de concluir é repetir 3-4
vezes, e é por isso que a aula diz que não deve ser o foco. Registre as duas frases; não
escolha. **As duas são `outro-narrador`** (L8773-9109) — nenhuma é citável como fala de
Max.


## otimizacao-horarios-a-testar

| Valor | Registro | Linha |
|---|---|---|
| "Typically, we've found around 11am-12pm to perform the best" | slide | L9148 |
| "Main times to test would be 9am, 12pm, 2pm, and 4pm" | slide | L9149 |
| caso real: 1:45pm bate 11am com ~5x placed orders | **outro-narrador** | L8848-8852 |
| público blue collar: "eight or 9 a.m." ou "between four and six" | **outro-narrador** | L8844-8846 |
| SMS: "midday from 11am-2pm or evening around 5pm"; evitar antes de 10am e depois de 7:30pm | slide (SMS) | L9509-9516 |

**Como responder:** horário é **output de teste, não input** — a própria aula mostra o
caso em que o horário "que costuma performar melhor" perde por ~5x em placed orders. A
lista do slide (9am, 12pm, 2pm, 4pm) é ponto de partida; a fala amplia para 8am e
4-6pm conforme a rotina do público; e o canal SMS tem grade própria. Nunca apresente
11am-12pm como recomendação fechada.


