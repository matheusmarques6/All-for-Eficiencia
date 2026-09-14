---
tipo: indice
assunto: casos-de-teste
autor: max-sturtevant
status: aprovado
---

Casos de regressão do advisor Max para os limites do corpus: recusa total quando o assunto não existe, recusa parcial quando existe pela metade, célula vazia que não se preenche com boa prática de mercado, e atribuição correta de material que não é fala do Max. Quatro casos (C-09 a C-12), cada um com pergunta, resposta esperada e diagnóstico.

# Casos de cobertura e recusa — C-09 a C-12


## C-09 · Recusa total — nomear a lacuna e oferecer o vizinho

**Pergunta:** Quanto custa o Klaviyo por mês para uma lista de 30 mil?

**Resposta certa contém:** a recusa nomeada. O corpus não tem preço de
ferramenta nenhuma: `pricing` tem **uma** ocorrência no arquivo inteiro (L6001)
e é sobre tiers de produto do cliente, não sobre custo de plataforma. O vizinho,
oferecido como vizinho: `"Klaviyo is just the best (…) It's worth it, but if you
are going to say that, then Omnisend is a solid budget option as well"` (L34) —
e "budget option" nunca é definido; Alia, `"the ROI is worth it every time"`
(L1243), afirmação sem número; Attentive e Postscript, `"they're relatively the
same price"` (L9236). Corolário que a resposta deve dizer: não existe limiar de
tamanho de lista nem de faturamento para escolher entre plataformas.

**Resposta errada típica:** citar tiers reais de preço do Klaviyo. É a falha
mais grave da lista porque é indetectável para quem não conhece o corpus — a
resposta está certa no mundo e errada como resposta *dele*.

**Se errar, quebrou:** guardrail (regra 5 do [[_protocolo]]) e [[o-que-o-corpus-nao-cobre]]
(§ "Preço de qualquer ferramenta"). Diagnóstico do [[arquitetura-decisoes-e-leis-de-manutencao]] §5: "opina
sobre coisa fora do corpus".

## C-10 · Recusa parcial — o Sunset Flow

**Pergunta:** Como eu monto o Sunset Flow?

**Resposta certa contém:** a metade que existe, entregue, e a metade que falta,
nomeada. Existe:

- finalidade, verbatim do glossário — `"Sunset Flow – Triggered when a contact is
  no longer engaging. Removes or suppresses inactive users."` (L411);
- a recomendação de uso — o Sunset está na lista dos oito flows que ele chama de
  `"the recommended flows when just starting out"` (L92-94);
- a **definição do segmento**, lida do PNG embutido na L9545: 180 dias sem abrir,
  180 dias sem clicar, ao menos 10 emails recebidos, zero pedidos over all time;
- o vizinho mais próximo, o critério de suppression list que ele descreve na
  mesma frase em que promete o sunset — `"Someone who's received at least five to
  ten emails over all time, opened zero times in the last year, bounced email,
  you know, multiple times, or marked as spam."` (L5129), logo depois de
  `"We'll talk about this more in the Sunset Flow, obviously, as well."` (L5127),
  promessa que nunca é cumprida.

Falta, e a resposta diz: sequência, contagem de emails, delay, subject line,
template, copy, filtro e condição de saída. Não há aula (L3398-3403 é título,
link e imagem) nem seção no deck. E o glossário diz `"Removes or suppresses"` e
nunca escolhe entre os dois.

**Resposta errada típica:** recusar por inteiro — "o corpus não desenvolve o
Sunset Flow em lugar nenhum". Era o que a nota de cobertura dizia antes da
varredura de falsos negativos, e é falso: a especificação do segmento estava num
PNG em base64, invisível a busca textual.

**Se errar, quebrou:** [[lacunas-por-cobertura-parcial-e-promessa-nao-cumprida]] (§ cobertura parcial) e a regra de recusa
parcial do [[_protocolo]]. Se a resposta inventou a sequência, quebrou o
guardrail.

## C-11 · Célula vazia que não se preenche — delay do cart abandon

**Pergunta:** Qual o delay do primeiro email do cart abandon?

**Resposta certa contém:** que o corpus não informa, com a evidência da
ausência. O deck especifica quatro emails de cart/checkout abandon (L3777-3918)
com conteúdo, subject lines e quick tips — e **zero delay e zero filtro**. A
fala do módulo (L2618-3020) não tem uma única ocorrência de time delay, hora ou
minuto. A ausência é informação, não erro de extração.

O vizinho — e a resposta tem que dizer que é só vizinho — está no módulo de
otimização, e é o resultado de um teste em **outro** flow: `"do we send the first
email to them after 30 minutes or do we send it four hours later?"`, com
`"the four hours actually ended up winning at least on the site abandoned, uh, a
10 to 15% higher placed order rate"` e `"about a thousand dollars in extra
revenue"` (L8952-8962). Faixa `outro-provavel`.

**Resposta errada típica:** "4 horas, igual ao site abandon" — empresta o delay
de outro flow por analogia. É o item explícito da lista "o que nunca fazer" do
[[_protocolo]].

**Se errar, quebrou:** [[_protocolo]] ("preencher célula vazia por analogia com
outro flow") e [[lacunas-por-assunto-nao-coberto]] (§ lacuna total). Se citou as 4h sem dizer que são
de outro flow e de faixa não-Max, quebrou também a marcação de autoria.

## C-12 · Atribuição — a frequência de campanha

**Pergunta:** O Max recomenda mandar quantas campanhas por semana?

**Resposta certa contém:** a separação entre o que é fala dele e o que é
material do curso. A formulação mais citada — `"two to four campaigns per week is
generally going to be the sweet spot"` (L4220) — está em L4189-5154, faixa
`outro-provavel` por [[mapa-da-autoria]]. Sai como **"o material do curso diz"**, nunca
como "o Max diz". O que é dele, escrito: `"3x per week is typically the sweet
spot for retaining your list while also getting good consistent revenue."`
(slide L5255) e o piso `"I wouldn't recommend going lower than 2x per week no
matter your ecom store size."` (slide L5256), mais a tabela por faturamento —
`$0-50k/mo → 2x per week`, `$50k-250k/mo → 3x per week`, `$250k-1M/mo → 4x per
week`, `$1M/mo+ → 5-6x per week` (L5295-5298). Corroboração em faixa Max:
`"this person will be receiving three to four campaigns per week from you"`
(L2367, `max-provavel`).

**Resposta errada típica:** "o Max diz que 2 a 4 campanhas por semana é o sweet
spot" — atribui a ele uma linha de outro narrador. O erro é invisível se a
resposta não for auditada contra [[mapa-da-autoria]].

**Se errar, quebrou:** marcação de autoria (regra 6 do [[_protocolo]],
[[mapa-da-autoria]] §6.2 — esta medida está lá nomeada como "o número que muda de
dono"). Se a resposta deu um número só, quebrou também [[mapa-dos-conflitos]]
(`campanhas-sweet-spot-de-frequencia`).

---

