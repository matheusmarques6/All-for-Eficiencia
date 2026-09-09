---
tipo: indice
modulo: sms
assunto: mapa-local
autor: max-sturtevant
fonte: "CONTEUDO BRUTO/max.md — L9213-9260 (transcrição), L9261-9544 (slide GAMMA)"
status: aprovado
---

# O que tem nesta pasta

O canal de SMS inteiro: por que ele defende o canal, as restrições de custo e
tamanho que governam tudo, frequência, escolha de plataforma, captação de
número, os cinco flows com os templates prontos, o que pode ser enviado e o
calendário com os horários.

Ordem de leitura para quem vai montar SMS do zero: [[por-que-sms]] →
[[custo-e-tamanho-da-mensagem]] → [[setup-e-plataforma]] → [[crescer-a-lista]] →
[[flows-sms]] → [[frequencia]] → [[o-que-enviar]] → [[calendario-e-horarios]].

**Neste módulo o slide vale mais que a fala.** São 284 linhas de deck contra 41
de transcrição, e os artefatos — os quatro templates de copy, os delays dos
flows, os passos do Shopify — só existem no slide. A fala guarda o julgamento
(as ressalvas, o "test it", as admissões) e a descrição do calendário, cuja
imagem não sobreviveu à extração.

# As notas

| Nota | tipo | O que responde |
|---|---|---|
| [[por-que-sms]] | principio | por que SMS: 98% de open rate, lista como ativo proprietário, e por que "simple" não é "easy" |
| [[custo-e-tamanho-da-mensagem]] | especificacao | 160 caracteres, a dobra de preço em 161, MMS 2-3x, emoji = 35-50 caracteres |
| [[frequencia]] | especificacao | 1-2 por semana, o que acontece acima disso, e a única escapatória (segmentar) |
| [[setup-e-plataforma]] | procedimento | Klaviyo, Attentive, Postscript — e por que ele diz que a escolha não decide nada |
| [[crescer-a-lista]] | procedimento | checkbox de checkout e pop-up; **a armadilha**: os passos do Shopify são de email |
| [[flows-sms]] | artefato | os cinco flows, os delays e os quatro templates de copy verbatim |
| [[o-que-enviar]] | principio | só transacional; nada de nurture nem prova social; o restock como coringa |
| [[calendario-e-horarios]] | especificacao | o mês de outubro reconstruído, a regra de lacuna e as janelas de envio |

# Os números que mais são perguntados

| Medida | Valor | Registro | Linha |
|---|---|---|---|
| Open rate de SMS | **98%** | ambos | L9223, L9291 |
| Frequência | **1-2 por semana** | ambos | L9227, L9367, L9491 |
| Limite por mensagem | **160 caracteres** (161 dobra o preço) | ambos | L9231, L9390-9392 |
| Custo de MMS | **2-3x** o SMS | ambos | L9229, L9383 |
| Custo de um emoji | **35-50 caracteres** | ambos | L9233, L9405 |
| Flows | **5** | transcrição | L9244 |
| Delay welcome 1 → 2 | **Wait 5 days** | slide | L9440 |
| Delay browse abandon | **Wait 60 minutes** | slide | L9453 |
| Delay cart / checkout abandon | **Wait 30 minutes** | slide | L9466 |
| Delay winback | **Wait 120 Days** | slide | L9479 |
| Cart abandon nos EUA | **1 mensagem só** — o resto é ilegal | slide | L9461 |
| Trigger do pop-up | **6-10s** após page load (ele usa 6) | transcrição | L9239-9240 |
| Janela base de envio | **11am-2pm** | ambos | L9256, L9509 |

Tabela completa em [[_numeros-completo#SMS]].

# Onde este módulo se contradiz

Treze entradas canônicas: onze em [[_conflitos-completo#sms]] e duas —
`sms-open-rate-de-email` e `sms-frequencia-de-email-comparada` — em
[[_conflitos#Conflitos entre módulos]]. As que mais mudam uma
resposta:

- **`sms-frequencia`** — 1-2/semana × "once per weekish" × o calendário-exemplo
  com 7 mensagens em 31 dias e dois envios em dias consecutivos.
- **`sms-instrucoes-de-optin-sao-de-email`** — o passo a passo prometido para
  capturar telefone captura email. Nunca entregue esses passos como solução de
  SMS.
- **`sms-mms-no-browse-abandon`** — text-only é regra absoluta, e o browse
  abandon manda testar imagem.
- **`sms-quinze-por-cento`** — "15%" é click rate num lugar e share de receita
  no outro; e ainda há um 20% de share.
- **`sms-open-rate-de-email`** — 30% aqui contra os 50%+ que ele exige no resto
  do corpus.
- **`sms-welcome-contagem`** — 2-3 mensagens na fala, 2 no template.
- **`sms-transacional-puro-ou-quase`** — "purely" no slide, "mostly" na fala.
- **`sms-benchmark-de-form`**, **`sms-delay-do-popup`**, **`sms-exit-intent`** —
  complementam conflitos já abertos em list growth, com uma versão a mais vinda
  daqui.

# O que este módulo não cobre

- **As 30 mensagens do swipe file.** Prometidas duas vezes (L9258, L9520-9523) e
  ausentes. Não existe **nenhum** exemplo de copy de campanha de SMS no corpus —
  só os quatro templates de flow. Nunca invente exemplos "no estilo dele".
- **Como capturar telefone no checkout do Shopify.** O procedimento que deveria
  cobrir isso é de email.
- **Compliance.** Zero linha sobre TCPA, consentimento expresso, texto de opt-in
  ou opt-out obrigatório — apesar de ele invocar a lei americana para limitar o
  cart abandon (L9461) e exigir checkbox pré-marcado (L9324).
- **Preços absolutos.** Nenhum custo por mensagem, por plataforma ou por volume:
  só múltiplos ("2-3x", "double").
- **Gatilhos nomeados.** Nenhum metric de plataforma para os cinco flows, nenhum
  filtro, nenhuma condição de saída.
- **Setup de plataforma.** Ele recusa explicitamente dar o passo a passo
  (L9236, L9316).
- **Segmentação de SMS.** Ele manda enviar só a "extremely engaged segments" se
  passar do teto (L9368) e nunca define o segmento.
- **Post-purchase, cross-sell, sunset ou back-in-stock em SMS** — não existem.

# Nota de tamanho

Três notas passam do teto de 4 KB do brief: [[flows-sms]] (5,7 KB),
[[crescer-a-lista]] (4,9 KB) e [[calendario-e-horarios]] (4,7 KB). As duas
primeiras carregam artefato verbatim que não pode ser resumido — os quatro
templates de copy e os quatro passos do Shopify. A terceira carrega o calendário
reconstruído linha a linha mais a tabela de horários, e é a única das três que
poderia ser quebrada em duas (calendário / send times) sem perder rastreabilidade.
