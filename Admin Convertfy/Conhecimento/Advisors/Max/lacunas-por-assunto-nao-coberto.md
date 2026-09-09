---
tipo: indice
assunto: cobertura-e-lacunas
autor: max-sturtevant
status: aprovado
---

Registro das lacunas de tipo **lacuna total** do corpus Max: os assuntos que nem
a fala, nem o slide, nem um exemplo tocam, e que por isso se recusam por
inteiro. Traz junto as dezesseis ausências que já foram declaradas lacuna aqui e
**não são** — falsos negativos derrubados contra o bruto, que nunca devem ser
recusados. Índice em [[mapa-da-cobertura]].

# Lacuna total — o corpus não toca o assunto

Nem fala, nem slide, nem exemplo. Recusa inteira.

| Lacuna | Evidência da ausência |
|---|---|
| **Delay de cart abandon e de checkout abandon.** | Varredura de `time delay`/`hour`/`minute`/`wait` na fala do módulo (L2618-3020): zero. No deck (L3777-3918): zero. Registrado em [[flows/otimizacao-de-flows]]. **Nunca preencher por analogia com o welcome, que tem.** O vizinho — e é só vizinho — está no módulo de otimização: o teste descrito ali opõe **30 minutos a 4 horas** em flows de abandono e reporta 4h vencendo "at least on the site abandoned" (L8952-8962, **`outro-narrador`** — é material do curso, não fala de Max). É o valor de um teste em outro flow, não o delay prescrito para estes dois. |
| **Critério de escolha dentro de catálogo.** Qual filler do welcome usar; qual dos 9 tipos de infográfico; qual dos 7 tipos de bridge; qual dos 4 métodos de list growth. | Existe catálogo, não existe ordem nem árvore de decisão. Confirmado nas quatro notas: [[flows/welcome-fillers]], [[copy/infograficos]], [[design/secao-bridge]], [[list-growth/os-quatro-metodos]]. |
| **Preço de qualquer ferramenta.** | `pricing` tem **uma** ocorrência no arquivo inteiro (L6001) e é sobre tiers de produto do cliente, não sobre custo de plataforma. Ver §4. |

## Cinco coisas que já foram declaradas lacuna total aqui e **não são**

Revisão contra o bruto. Cada uma destas foi listada como lacuna total numa
versão anterior desta nota; cada uma tem conteúdo no corpus. **Não recusar
nenhuma delas.** Ficam registradas para que a classificação errada não volte.
Uma sexta — filtro e condição de saída de flow — desceu para *cobertura
parcial*, porque lá existem três flows cobertos e cinco descobertos.

O padrão dos cinco erros é o mesmo e vale como aviso: **a promessa vazia estava
num registro e o conteúdo em outro.** O deck não lista os métodos de transição,
a fala lista; a aula de copy não tem transcrição, a de campanhas explica o mesmo
framework. Antes de declarar lacuna, procurar o assunto **no outro registro e no
outro módulo** — e considerar a grafia corrompida pelo ASR ([[_fontes]] §5),
que foi o que escondeu o S.C.E. atrás de "SDE".

| Já foi chamada de lacuna | O que existe, e onde |
|---|---|
| Métodos de transição entre seções | **Os quatro estão na fala, L7550-7588**: gradiente (L7552-7558), formas/quebras de linha (L7560-7568), fundo consistente com elementos em primeiro plano (L7570-7578) e o favorito dele, transição atrás de foto (L7580-7586). O deck é que não lista nenhum. Já estava certo em [[design/transicoes]] e no conflito `design-metodos-de-transicao-ausentes`. |
| Racional falado do S.C.E. | Existe, **em outra aula**: L4715-4767 percorre S, C e E com exemplo trabalhado para cada um. A busca literal falha porque o ASR escreve **"SDE framework"** em L4715. Mais o deck de campanhas, que explica letra por letra (L5504-5512). O que falta é só a transcrição da aula "The Principles of Good Copy" — ver *Perda por falha técnica*. Ressalva de voz: L4715-4767 cai na faixa `outro-provavel`. |
| Amostra mínima de teste A/B | L8800-8820 dá a régua inteira: lista de 1.000 partida 500/500 "is not enough data"; 100k-500k → um ou dois envios bastam; 5k-10k → repetir o teste três ou quatro vezes; e a regra explícita "Base it off the number of recipients that are receiving". Já estava em [[otimizacao/quando-vale-testar]]. |
| Cadência de teste de form | L663 declara "at least for like bi-weekly. Once every two weeks, run some sort of test". A versão anterior desta nota citava a mesma linha cortada antes dessa metade — **e [[list-growth/os-sete-testes-de-form]] ainda citava, até a varredura de falsos negativos. Corrigir aqui não corrige a nota; verificar as duas.** |
| Janela de medição — atribuição e painel | **Janela de atribuição de receita: 3 a 5 dias** após o clique (L54, verbatim: "they say somebody clicks an email and they purchase within three to five days, they count it as email revenue"). **Janela do painel: 30 dias, comparada com os 30 anteriores** (L64). Já estava em [[fundamentos/dashboard-do-klaviyo]]. |

## Mais onze, derrubadas na varredura de falsos negativos

Segunda passada, agora sobre as seções "O que o corpus não diz" das 101 notas de
conteúdo — não sobre esta tabela. **O padrão se repetiu inteiro**: a afirmação de
ausência estava numa nota e o conteúdo em outra, quase sempre em outro módulo.
Em quatro casos a negação contradizia o **corpo da própria nota**. Todas
corrigidas na origem; ficam aqui para a classificação errada não voltar.

| Nota | Dizia que não existia | O que existe, e onde |
|---|---|---|
| [[campanhas/segmentacao]] | "O Sunset Flow (…) não é desenvolvido em lugar nenhum do corpus" | finalidade (L411), recomendação (L92-94) e a **definição do segmento** no print da L9545. É o caso-escola de cobertura parcial desta nota. Vizinha que já tinha: [[flows/sunset]] |
| [[fundamentos/glossario]] | "não há definição de `Sunset Flow` além da linha do glossário (L411)" | idem — o print da L9545 dá as quatro condições. Vizinha: [[flows/sunset]] |
| [[copy/subject-lines]] | "Personalization (…) não reaparece em lugar nenhum (…) Nenhuma SL do corpus é personalizada" | fala L9068-9082 (first name na SL, no preview text ou na 1ª linha, com exemplos), slide L9206-9207 (teste "Personalization Depth"), glossário L426 (`{{ first_name }}`) e a SL "Your Favorites Are on Sale – Personalized collection" (L5469). Vizinha: [[otimizacao/outros-testes]] |
| [[fundamentos/escolha-do-esp]] | "Mailchimp aparece uma única vez no corpus" | três vezes: L459, L8563, L8607 |
| [[fundamentos/escolha-do-esp]] | "Nenhuma instrução de migração entre plataformas" | procedimento completo em L8607-8622: exportar as listas de 30/60/90 dias engajados, importar no Klaviyo, re-aquecer do zero por amostra (1.000 → ~120.000 em 60 dias). Vizinha: [[deliverability/warming-casos-reais]] |
| [[list-growth/os-sete-testes-de-form]] | "O único gate declarado é qualitativo: 'depending on your site traffic' (L663)" | **a citação estava cortada na metade**: a mesma L663 segue com "at least for like bi-weekly. Once every two weeks, run some sort of test". Mais a régua de amostra de L8800-8820. Contradizia o próprio corpo da nota |
| [[flows/otimizacao-de-flows]] | "Nenhuma métrica de decisão — nem open rate, nem clique, nem receita" | L8932-8944: "placed order rates, revenue, number of recipients, over open rates"; slide L9185 "Measure both CTR and conversion rate". Vizinha: [[otimizacao/testar-subject-line-por-receita]] |
| [[otimizacao/outros-testes]] | "Nenhum destes 13 tem número, vencedor ou caso" | dois dos 13 são re-listagens de testes com vencedor declarado no mesmo módulo: send time (L8846-8852, "five X the amount of placed orders"; L9148) e gráfico vs texto (L8866, "text base sale winner"). Vizinhas: [[otimizacao/send-time]], [[otimizacao/grafico-vs-texto]] |
| [[sms/flows-sms]] | "Nada sobre (…) back-in-stock em SMS" | L9249 (fala), L9498 e L9504-9505 (slide: "Restocks are a great way to get traction when you aren't sure what to send"). Existe como **campanha**, não como flow. Vizinha: [[sms/o-que-enviar]], que tinha uma seção inteira sobre isso |
| [[flows/conteudo-dinamico-klaviyo]] | "Nenhuma versão para SMS" | L9457: a imagem do item navegado no browse abandon de SMS, com aviso de custo 2x-3x. Conceito sim, sintaxe não. Vizinha: [[sms/flows-sms]] |
| [[design/principio-ease-of-click]] | "não há: cor" | L8142 e L8166 ("high-contrast colors", "contrasting colors") e L7045-7047 ("You don't want to use like a blue button here") — **os três já citados no corpo da própria nota** |
| [[copy/infograficos]] | "não existe regra de qual usar em qual email" | mapeamento parcial já no corpo da nota: comparison chart → us-vs-them do welcome (L5979-5981), timeline → post-purchase de item lento (L5939-5961), feature diagram → produto técnico (L5915-5939), graph → estatística (L6047-6051); mais o default do bridge (L7404, L8271) |

**Cinco escopos corrigidos de "o corpus" para "esta nota / este módulo":**
[[deliverability/setup-tecnico]] (SPF/DKIM/DMARC **são** definidos numa linha em
L452 e como registro de DNS em L8671 — o que falta é o que cada um faz),
[[flows/welcome]] (não há metric porque **o gatilho é lista**, L4881-4883),
[[sms/setup-e-plataforma]] (compliance de **email** existe no glossário,
L499-507), [[design/secao-footer]] (unsubscribe, preference center e CAN-SPAM
estão em L504-507) e [[campanhas/frequencia-de-envio]] (dia e horário existem em
[[otimizacao/send-time]]; rampa existe, mas é de volume, em
[[deliverability/warming-do-dominio]]).

