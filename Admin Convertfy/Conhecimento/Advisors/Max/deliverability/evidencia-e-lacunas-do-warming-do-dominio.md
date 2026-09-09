---
tipo: procedimento
modulo: deliverability
assunto: warming-do-dominio
autor: max-sturtevant
registro: [outro-narrador]
fonte: "CONTEUDO BRUTO/max.md — L8607-8645 (transcrição). O corpo do deck de warming NÃO foi exportado."
validade: "procedimento — o corpus não data a gravação. Extraído em 2026-09-06."
status: aprovado
---

Esta nota reúne a evidência e os limites do procedimento de warming do domínio:
os dois casos reais em que ele foi aplicado, a ferramenta de otimização de HTML
que o material recomenda mas **nunca nomeia**, e a lista do que o corpus não
responde. O procedimento em si está em [[preparacao-para-o-warming-do-dominio]]
e [[rampa-de-warming-do-dominio]].

# Aviso de autoria

**Faixa L8381-8646 (toda a fala do módulo de deliverability) — `outro-provavel`.**
Sem prova nominal. A classificação é **estilométrica**: o bloco pertence ao aglomerado
do único bloco `outro-provado` e não traz um só marcador do idioleto de Max.
`outro-provavel` não é `outro-provado` — não está provado que a voz não é dele, está
estabelecido que é muito improvável ([[mapa-da-autoria]] §7.3).

Critério: **idioleto** ([[mapa-da-autoria]] §2.1) — ausência de "I recommend", "my favorite"
e "I like to", presença de "at the end of the day" e "obviously", e o fecho coletivo
"thank you guys… see you in the next one". **A saudação de abertura não é critério e
não pode ser citada como evidência:** o laudo testou e ela caiu — o walkthrough de
Figma abre com "Hello, hello" e é comprovadamente Max, que em L7817 digita `@max` e
diz "tags me" ([[mapa-da-autoria]] §5).

Nesta nota a exposição é quase total. Os cinco bullets do deck (L8522-8526) e o
limiar de 60%+ do deck de deliverability (L8728) são **slide** — artefato de Max.
Todo o resto — fundação, segmentos-semente, rampa, passo de escalonamento,
cadência, batching, cronograma por semanas, regra de ouro e correção de rota —
está em L8532-8646, faixa não-Max, e **não é citável como fala dele**. Como o deck
de warming nunca foi exportado, este procedimento fica sem nenhum registro de Max
que o confirme: é a peça do corpus com menor lastro de autoria.

> **Lacuna estrutural desta nota.** O deck citado no vídeo — "Email Warming
> Deliverability Deep Dive", `https://gamma.app/docs/Email-Warming-Deliverability-Deep-Dive-ex6p9skikw53x06`
> (L8520) — **nunca foi exportado**. A seção GAMMA (L8647-8759) cobre só o deck
> de deliverability e vai direto de "Check Your Deliverability With Glockapps"
> (L8752) para `# OPTIMIZATION` (L8760). O único registro de slide sobreviveu
> como cinco bullets de resumo (L8522-8526). Todo o resto — rampa, cronograma,
> batching, casos — existe **apenas na transcrição falada**. É a única parte
> crítica do corpus sem segundo registro para conferir número.

# Os dois casos reais

Em [[warming-casos-reais]], com os volumes verbatim. Em uma linha cada:

- **Migração de MailChimp** (L8607-8622) — havia dado de email fora do Klaviyo,
  mas trataram como conta nova: **amostra aleatória** dentro do 30 dias
  engajados, começando com 1.000 pessoas e 46.22% de abertura. "Even if you have
  that data, it's still different platform (…) you always end up somewhat
  starting from scratch" (L8612-8613).
- **Zero dado, pré-lançamento** (L8623-8639) — só waitlist e lista de marca
  irmã. Emails de warming **todos text-based**, lotes pequenos, primeiro envio
  ~200 pessoas. Contém a autocrítica da equipe narrada: "we actually weren't
  even including any CTAs, which was a bad idea on our end" (L8635).

# A ferramenta que nunca é nomeada

No fim do vídeo o material recomenda uma ferramenta de terceiros para quem cai em
promotions — e **o nome dela não está no corpus**. O trecho (L8641-8643):

> If your emails are landing in spam, don't use this, but if your emails are
> landing in promotions very heavily, this is a great tool that runs in the
> backend and optimizes all that HTML and things to make sure that you are
> landing in the primary inbox (…) they are a very, very good tool to work with
> a lot of very well-known brands as well.

Escopo declarado: serve para **promotions**, não serve para spam nem para
warming (L8643).

A ausência do nome é comprovável, não suposta. Duas evidências:

1. **O salto de tempo.** A transcrição vai de 21:52 (L8641) para 22:33 (L8642):
   41 segundos. É o **maior salto do vídeo inteiro** — a mediana entre marcas de
   tempo consecutivas nessa transcrição é de 11 segundos e o percentil 90 é 18.
2. **A emenda dentro de L8641.** A linha costura duas frases de assuntos
   diferentes sem pontuação: "…I'll be happy to answer questions that I can help
   **If your emails are landing in spam, don't use this…**". O corte está dentro
   da própria linha, e é ali que a ferramenta seria apresentada.

Irrecuperável. Nunca preencher esse nome por dedução.

# O que o corpus não diz

- O corpo do deck de warming (ver o aviso no topo).
- Quantos emails por semana é "demais" — o teto de diminishing returns perdeu o
  número (L8560).
- Quais são os "few tweaks" que adaptam o método para conta com deliverability
  ruim (L8524).
- Que porcentagem de queda de open rate obriga a recuar. O exemplo é 50% → 25%
  (L8601), não é regra.
- O nome da ferramenta de otimização de HTML (L8641-8643).
- Quanto tempo o warming inteiro leva. Há "weeks 1 to 3" e "weeks 3 to 12"
  (L8578-8580) e uma "60 day window" num caso (L8611) — não são a mesma unidade.

# Onde está o procedimento

Preparação (quando se aplica, fundação, primeiro público) em
[[preparacao-para-o-warming-do-dominio]]. Execução (rampa, cronograma, conflito
do limiar, correção de rota) em [[rampa-de-warming-do-dominio]].
