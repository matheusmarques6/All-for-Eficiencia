---
tipo: indice
assunto: cobertura-e-lacunas
autor: max-sturtevant
status: aprovado
---

Os dois limites que qualificam toda resposta tirada do corpus Max sem serem
lacuna: **de quem é a fala** — cerca de 25% da transcrição não é dele e não pode
sair entre aspas atribuídas a ele — e **de quando é o material**, que o corpus
não declara em lugar nenhum. Nenhum dos dois gera recusa; os dois mudam a forma
da atribuição e obrigam ao carimbo de data. Índice em [[mapa-da-cobertura]].

# O limite de autoria

**~25% da fala do corpus não é do Max.** São **2.228 linhas**, 25.141 palavras,
distribuídas em cinco faixas ([[_autoria]]). *(Recontado com `wc` faixa a faixa:
250 + 966 + 382 + 282 + 348 = 2.228. As palavras conferem exatamente; [[_autoria]] §6
já traz 2.228 — a correção pedida por uma versão anterior desta linha foi aplicada lá.
25.141 sobre 100.638 palavras de fala = 24,98%; [[_autoria]] escreve 100.640 no mesmo
lugar, divergência de duas palavras que nenhum dos dois arquivos resolve.)*

| Faixa | Módulo | Classificação |
|---|---|---|
| L5617-5866 | Copywriting (ChatGPT) | **`outro-provado`** — L5753 fala de Max em terceira pessoa |
| L4189-5154 | Campaigns (fala inteira) | `outro-provavel` |
| L5867-6248 | Copywriting (infográficos, subject lines) | `outro-provavel` |
| L8365-8646 | Deliverability (fala inteira) | `outro-provavel` |
| L8762-9109 | Optimization (fala inteira) | `outro-provavel` |

**O que isso significa na prática, e o que não significa.**

Não significa que o material seja inválido. Significa exatamente uma coisa: **é
material do curso, não é fala dele.** O curso é dele — ele o compilou, o
entregou e o assina. A doutrina continua utilizável, os números continuam
válidos, as especificações continuam valendo. O que muda é a **forma da
atribuição**: nada dessas faixas pode sair como *"Max diz que…"*, *"na visão
dele…"* ou entre aspas atribuídas a ele. Sai como *"o material do curso diz"*.

Isto **não é uma lacuna** e não gera recusa. É a distinção entre responder e
citar. Se a pergunta é "o que fazer", responda. Se a pergunta é "o que **ele**
acha", entregue o conteúdo marcando que essa parte do curso não é fala dele.

**Onde bate mais forte:** [[mapa-de-deliverability]] (9 de 9 notas),
[[mapa-de-otimizacao]] (7 de 7), [[mapa-das-campanhas]] (8 de 9),
[[mapa-de-copy]] (6 de 9), [[mapa-da-doutrina]] (8 de 13). Somando: os dois
módulos de densidade baixa que mais concentram lacunas são também os dois em
que **nenhuma linha falada é citável como dele**.

**E onde bate de leve, mas bate:** [[mapa-dos-flows]] — **1 de 12**, só
[[flows/winback]], por causa da definição de segmento que vem de L5057, dentro
da faixa de Segmentation. Flows **não** é pasta limpa; não está na lista de
terreno seguro abaixo por isso.

**O que não está em causa:** os nove decks GAMMA. São artefato escrito de Max —
carregam a bio assinada (L3419, L9269) e reivindicações em primeira pessoa
(L358, L1208, L5475, L6774, L8311, L9522). Ressalva de [[_autoria]] §7.5: não
dá para distinguir "Max escreveu usando 'nós'" de "a equipe escreveu e Max
assinou", e por isso convém não citar um slide como *"ele disse"* — o deck é
artefato dele, não fala dele.

**E o inverso também vale.** Os quatro módulos sem contaminação nenhuma —
[[mapa-de-design]], [[mapa-dos-fundamentos]], [[mapa-de-list-growth]],
[[mapa-de-sms]] — têm cada um ao menos um bloco `max-provado` como âncora
(L7817/L8044 · L34 · L631/L1014 · L9258). Quando a pergunta pedir a voz dele,
estas quatro pastas são o terreno seguro.

---
# Datação

**O corpus não declara data de gravação em lugar nenhum.** Nenhum bloco, nenhum
deck, nenhum marcador. O que existe são âncoras internas.

**A data conhecida mais recente é `Nov 13, 2024, 9:49 AM`** — o carimbo do print
do segmento `WC | Sunset`, no PNG embutido na L9545, lido por ampliação em
[[flows/sunset]]. O dia é incerto entre 13 e 18: o glifo tem 7 px de altura. Não
há nada mais recente no material.

Outras âncoras temporais, todas verificadas:

| Âncora | Linha |
|---|---|
| "People had lots of money from the stimulus checks back in **2020**" | L9 |
| "we apply that to, like, **2025** where tariffs come into play" | L9 |
| "Increased Cost Per Acquisition x Lower LTV x **Tariffs** = Lower Profitability" | L268 (slide) |
| Título do vídeo de SMS: "Everything You Need to Know About SMS Marketing **in 2025**" | L9220 |
| Exemplo de copy: "if you got the new **iphone 16** you're at a 100 plus cases for it" | L2425 |
| "a lot has changed in the e-com world in the **past 5 years**" | L9 |

**O que apodrece, em ordem de velocidade:**

1. **Telas de ferramenta.** Todas as notas `tipo: procedimento` — os dois
   walkthroughs de form no Klaviyo, o dashboard, o Alia, o Figma, o upload
   (que é Omnisend), o Glockapps, o setup de checkout no Shopify. Interface
   muda sem aviso. Toda resposta que dependa de uma tela sai com o carimbo
   **antes** dos passos, nunca depois — regra 4 do [[_protocolo]].
2. **Os links de afiliado.** `omnisend.com/max`, o link Klaviyo com
   `utm_source=001Nu0000022YR4IAM`, `aliapops.com`, `alialearn.com`,
   `wellcopy.net/gpt`, o Skool. Todos descartados como CTA ([[_fontes]]), mas
   registrados aqui porque as **ofertas** que eles prometem ("30% OFF first 3
   months", L358/L8044; "Say Max sent you when you book a call and you'll get a
   gift ;)", L1245) são datadas e podem não existir mais.
3. **O diagnóstico de mercado.** Stimulus checks de 2020, tarifas de 2025, "70
   anúncios por dia" e "250 num estudo", CPM em alta. Nenhum tem fonte, e o
   argumento inteiro é conjuntural e americano. Ver
   [[fundamentos/estado-do-mercado]].
4. **Exemplos ancorados em lançamento.** O iPhone 16 (L2425) como gancho de
   campanha. A copy é boa; a âncora vence.
5. **Números de conta de exemplo.** Os 93.726 perfis e a data do print do
   Sunset são de uma conta de cliente num dia específico. Não são
   especificação e nunca devem ser citados como alvo.

**O que não apodrece:** princípio, framework, estrutura de flow, doutrina de
design, S.C.E., os pilares de conteúdo. Onde a resposta for de julgamento e não
de tela, a datação não muda nada.
