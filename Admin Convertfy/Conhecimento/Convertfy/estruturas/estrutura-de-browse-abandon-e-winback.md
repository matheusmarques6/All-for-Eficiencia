---
tipo: especificacao
assunto: estrutura-browse-abandon-winback
autor: convertfy
status: aprovado
fonte: 'Figma "ESTRUTURA FIGMA — RIDE NATION" — implementação Convertfy, 5 peças de browse abandon + 2 de winback, extraído em 2026-09'
---

O padrão da casa para browse abandon é uma sequência de cinco e-mails que já abre com cupom: a Convertfy trata intenção fraca com desconto no primeiro contato e escala de 12% para 14% ao longo da série, sem nunca mandar uma peça sem oferta. O winback é o oposto — abre sem desconto nenhum, apostando em saudade e novidade. Esta nota especifica peça a peça o que cada e-mail faz, transcreve os componentes fixos reutilizáveis e confronta a prática com a doutrina de curso do Max Sturtevant, que diverge em contagem de e-mails e em quando o desconto entra. O material vem de uma implementação (Ride Nation, streetwear/ciclismo, ticket R$ 100–250) e não traz resultado medido.

# Browse abandon: desconto desde a peça 1

A decisão estrutural da casa é a mais discutível e a mais clara: **não existe e-mail de browse abandon sem cupom**. Já a peça #1, que só relembraria, carrega `cupom:` / `EXCLUSIVO12` — não há degrau "lembrete sem oferta". A escada é de valor, não de existência:

| Peça | Cupom | Desconto exibido | Papel |
|---|---|---|---|
| #1 (600x2146) | `EXCLUSIVO12` | [não consta na fonte] — só o cupom | reconhecimento da visita |
| #2 (600x3094) | `EXCLUSIVO12` | `12%OFF` | objeção + escassez |
| #3 (600x3721) | `EXCLUSIVo12` | `12` `%` `OFF` | prova social dura + prazo |
| #4 (600x1734) | `EXCLUSIVO14 ` | `14%` | reoferta como "SURPRESA" |
| #5 (600x1846) | `EXCLUSIVO14` | `14%OFF` | última chance |

O salto 12% → 14% acontece entre a #3 e a #4, junto com a troca do código. Na #1 o percentual não aparece no texto capturado — registrar como `[não consta na fonte]`, não como "12% implícito". Nenhum delay, janela ou gatilho consta: a fonte é copy de Figma, não configuração de Klaviyo.

## A função de cada uma das 5 peças

**#1 — Reconhecer a visita e reabrir a vitrine.** Headline `Viu Algo QUE` / ` te pegou?`. Corpo assume o comportamento observado: `"Você passou por aqui, olhou com atenção. A gente notou — e separou mais do que você vai querer ver."` Dois CTAs de navegação, `VER MINHAS PEÇAS` e `CONTINUAR GARIMPANDO` — empurra para catálogo, não para checkout.

**#2 — Quebrar objeção de identidade e justificar o desconto.** Abre com `"Cansou de vestir o que todo mundo no rolê já tem?"` e nomeia o cupom como ajuda para fechar: `"Não foi por acaso que você parou nessa peça. (…) Aproveitamos pra deixar um desconto exclusivo pra te ajudar a fechar."` Três argumentos numerados — `"Reconhecimento não tem preço, mas tem peça certa"`, `"Fast fashion cansa. Qualidade fica."`, `"Essa não vai ficar disponível pra sempre"` — e escassez do próprio cupom: `"O cupom EXCLUSIVO12 expira em 3 horas depois disso, some junto. Sem prorrogação. Sem segunda chance no mesmo cupom."`

**#3 — Escassez com números e prazo.** `A PEÇA QUE VOCÊ VIU TÁ ESPERANDO.` / `MAS O JOGO MUDOU.` Bloco `O QUE ACONTECEU DESDE A TUA ÚLTIMA VISITA?` com três claims de movimento: `"27 unidades vendidas nas últimas 24h. Sem exagero."`, `"O que sobrou não vai durar o fim de semana."`, `"Mais de 800 pessoas estão de olho nessa peça agora mesmo."` Prazo explícito `ESTA OFERTA SOME em` / `48 HORAS`, reforçado em `POR QUE FECHAR NaS` / `PRÓXIMAS 48 HORAS?`. Depoimento de `Rafael M.` e o benefício `+ FRETE CALCULADO NA HORA, SEM SURPRESA`.

**#4 — Reoferta com desconto maior, enquadrada como surpresa.** `SURPRESA` / `Aproveite um DESCONTO de 14% em seu pedido por tempo limitado`, cupom `EXCLUSIVO14 `, CTA `rESGATAR AGORA`. Curta, sem prova social e sem argumento: oferta + vitrine + barra de confiança. É aqui que o desconto sobe.

**#5 — Última chance, mesma oferta.** `ÚLTIMA CHANCE` / `14%OFF`, corpo curto de lisonja: `"Você tem bom gosto. Não se esqueça de aproveitar seu desconto exclusivo antes que expire!"` Mesmo cupom, mesmo CTA, duas seções dinâmicas. Sem aviso de encerramento — o cart abandon da mesma implementação tem `AVISO FINAL:`, este não.

Arco: reconhecimento → argumento → escassez → reoferta maior → encerramento. A casa alonga onde convence (#2, #3) e encurta onde só reoferta (#4, #5).

# Winback: gatilho e oferta

**O gatilho não consta na fonte.** Sem janela de lapso, segmento ou delay. O material prova só a copy.

**Winback #1** (600x2880, desenhada) é **sem desconto**. Headline `Que saudade!`, corpo `"Faz um tempo que você sumiu da pista e muita coisa boa chegou por aqui."` O eixo é novidade e escassez de drop, não preço: `"Enquanto você estava fora, a Ride Nation não parou."` e `"Chegaram drops novos (…) Sem firula: quando acaba, acaba. Não tem reposição, não tem segunda chance."` CTAs de navegação: `Ver as Novidades`, `Ver Lançamentos`, `APROVEITE AGORA`. Prova social sob `Quem voltou, não se arrependeu`. Fecho `Não deixe para` / `depois`.

**Winback #3** é `TEXTO PURO (captura 800x727)` e está **em inglês, não localizado**: template com `{{ first_name|default:'there' }}`, checagem de satisfação e a oferta `"Use code MISSYA10 for 10% OFF when you order in the next 24 hours."` É placeholder de biblioteca, não peça pronta — texto idêntico ao da peça `## Atraso na entrega` do mesmo arquivo.

## Correção obrigatória sobre a oferta de winback

`VOLTEI15`, `15% OFF`, `"Sua volta tá com"`, `"Válido por tempo limitado"` e `"Aproveite Enquanto Há Tempo"` **não existem na fonte** — busca literal no arquivo inteiro: `[não consta na fonte]`. Os parecidos são de outros flows: `VOLTEI12` e `48h` em **Site Abandon Email #1**; `48 HORAS` em **Browse Abandon Email #3**.

**Logo, não há escada de desconto welcome → winback.** O único desconto de winback no material é 10% (`MISSYA10`), em template inglês — o mesmo percentual do welcome (`BEMVINDO10`). A escada real: welcome 10% → cart abandon 10% e 12% (`DESCONTO10`, `DESCONTO12`) → site abandon 12% (`VOLTEI12`) → browse abandon 12% e 14% (`EXCLUSIVO12`, `EXCLUSIVO14`) → post purchase 17% (`ESPECIAL`). O achado incômodo: **browse abandon (intenção fraca) recebe desconto maior que cart abandon (intenção forte)**.

## A lacuna do Winback #2

Existem `## Winback Email #1` e `## Winback Email #3`; **não existe `#2`**. O que a numeração sugere: o flow foi projetado com pelo menos três peças e a do meio — a que introduziria o desconto entre a saudade da #1 e o fecho da #3 — não chegou ao Figma ou não foi capturada.

O que **não** dá para afirmar: que a #2 exista em outro lugar, que tenha sido descartada, que use cupom, que a numeração seja a ordem de envio, ou que a #3 encerre o flow. É lacuna de material, não decisão.

# Componentes fixos (biblioteca reutilizável)

**Navegação de topo** (`y=16`, nas 5 de browse abandon e na Winback #1): `MAIS VENDIDOS` · `MASCULINO` · `MOLETOM` · `FEMININO`.

**Unsubscribe**: `Unsub Info`, sempre em `y=415`.

**Barra de confiança** (browse #4 e #5, Winback #1; ausente em browse #1–#3):

- `ENTREGA PRA TODO O BRASIL` — `"Frete calculado no checkout. Sem surpresa no final, como tem que ser."`
- `TROCA SEM BUROCRACIA` — `"7 dias. Sem formulário de 3 páginas. Sem drama. Só avisa a gente."`
- `PAGAMENTO SEGURO` — `"Checkout protegido. Cartão, Pix ou boleto do jeito que você preferir."`

**Bloco de cupom**: rótulo + código, com o rótulo variando entre `cupom:` (browse #1, #3) e `CUPOM:` (browse #2, #4, #5) — inconsistência real do arquivo, não erro de transcrição.

**Vitrine dinâmica**: `[in-klaviyo Dynamic Product section]` nas 5 peças de browse abandon (duas vezes na #5) e **ausente na Winback #1** — o winback manda para lançamentos, não para o produto visto.

**Prova social**: depoimento com nome e inicial (`Rafael M.`, `Thiago M.`, `Rafael S.`).

# O que a estrutura NÃO faz

- **Não manda e-mail sem desconto no browse abandon.** Nenhuma das 5 é lembrete puro.
- **Não segmenta comprador de não-comprador** — nada indica versão alternativa.
- **Não declara delay, janela ou gatilho** em nenhum dos dois flows.
- **Não fecha o browse abandon com aviso de encerramento**, o que o cart abandon faz.
- **Não localiza o Winback #3** — segue em inglês, com `[Founder Name] | [Brand Name]`.
- **Não usa contagem regressiva no browse abandon**, só prazo em texto.
- **Não anexa resultado.**

# Honestidade sobre o alcance desta nota

1. **É uma implementação.** Tudo vem de um cliente só. Que este seja o padrão replicado entre clientes é afirmação da casa; o artefato não prova replicação.
2. **Não há nenhum número de performance.** Os únicos números da fonte são claims dentro do e-mail (`27 unidades`, `4.9/5`), não medição. Esta nota é **padrão de execução, não evidência de eficácia**. "Isso funciona?" e "quanto rende?" respondem-se com `[não consta na fonte]`.

# Onde a prática da casa bate e onde diverge

Contra [[browse-abandon]], [[winback]], [[conflitos-de-flows-abandono-de-navegacao-e-carrinho]] e [[conflitos-de-flows-pos-compra-e-winback]].

**Concorda:**

- **Bloco dinâmico alto.** Ele manda "Put the dynamic content block as high up in the email as possible". Nas peças #1, #2, #4 e #5 a vitrine está no primeiro terço; na #3 desce para `y=2100` — divergência pontual.
- **Mostrar outros produtos.** O CTA `CONTINUAR GARIMPANDO` executa o racional de que "it might not be the product that they want".
- **Winback #1 é o "we miss you" dele.** `Que saudade!` cumpre o "Email 1 (Day 0): A warm 'We miss you' message… The goal here is emotional" — degrau emocional sem desconto.
- **Último e-mail text-based.** O Winback #3, texto puro assinado por fundador, é o formato que ele prescreve para o fecho.

**Diverge:**

- **Contagem no browse abandon: 5 contra 4.** Ele fixa 4 nos dois registros. A casa faz 5.
- **Quando o desconto entra — divergência central.** Ele coloca o desconto no **email 3 de 4** e ainda o marca como opcional ("you could send this to just people who haven't bought from you before"). A casa põe cupom **já no #1** e depois escala. Pela doutrina do curso isso queima margem em intenção fraca; pela prática da casa é o padrão. Divergência assumida, sem árbitro — não há número dos dois lados.
- **Percentual.** O exemplo dele é 10% ("10% OFF your viewed item!"), nunca virou regra. A casa usa 12% e 14%.
- **Winback: contagem e cadência.** Ele especifica 3 e-mails, Day 0 / Day 7 / Day 10 (só no slide; a fala dá só o Day 0 — `winback-cadencia`). A casa tem **duas** peças, #1 e #3, sem cadência declarada. A lacuna do #2 é compatível com o desenho de 3 dele, mas é leitura, não prova.
- **Janela de lapso do winback.** O corpus dele diverge — "90, 120, 180 days are the most common ones that I do", com a definição completa do segmento fora da faixa de flows ("at least once in the past 150 days AND zero times in the last 90 days") e um slot de slide vazio onde ela deveria estar. A casa **não declara janela nenhuma**: `[não consta na fonte]`. Não dá para dizer de que lado do conflito 90/120/180 a prática cai.
- **Definição do gatilho de browse abandon.** O conflito registrado é entre "didn't go any further" (fala) e "doesn't add anything to their cart" (slide). A casa não declara gatilho, então **não resolve o conflito** — mas a copy da #1 e da #2 (`"Não foi por acaso que você parou nessa peça"`) fala de uma peça específica vista, consistente com `Viewed Product` nas duas leituras.
- **Desconto de winback maior que o de welcome.** Não se sustenta aqui: ambos 10%. Para afirmar essa escada, a casa precisa de peça que a mostre — esta não mostra.
