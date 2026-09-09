---
tipo: procedimento
modulo: deliverability
assunto: auditoria-glockapps
autor: max-sturtevant
registro: [slide, outro-narrador]
fonte: "CONTEUDO BRUTO/max.md — L8508-8514 (transcrição), L8750-8757 (slide)"
validade: "procedimento — o corpus não data a gravação. Extraído em 2026-09-06. Preço, plano gratuito e telas do Glockapps podem ter mudado."
status: aprovado
---

Como usar o Glockapps para medir em qual caixa os emails estão caindo — primary, promotions ou spam: o que a ferramenta faz, os três passos do teste de placement, com que cadência rodar e por que não confundir com o domain-checker.


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

Nesta nota: o que o Glockapps faz, os 3 passos e a cadência (L8754-8757) são
**slide** — artefato de Max. As passagens faladas (L8508-8514, L8414, L8641-8643)
estão na faixa não-Max e **não são citáveis como fala dele**, inclusive a
afirmação sobre o plano gratuito.

> **Procedimento datado.** Serviço de terceiro. A fala afirma que é "at least
> free to start" e que "eventually, you will have to get onto a plan" (L8508) —
> isso era verdade quando o vídeo foi gravado, e o corpus não diz quando foi.

# O que faz

Mede **onde o email cai**, não se ele chegou. Slide, verbatim (L8754-8756):

> Glockapps is a platform that allows you to see where you are landing in
> inboxes.
> Main inbox, promotions, or spam.
> It will give you a list of 100+ email addresses, you will send a campaign to
> this list, then they will send back to you how often you landed in the
> different inboxes.

Na fala, o mesmo mecanismo, com o detalhe de que os endereços são de teste
(L8510):

> it essentially tells you exactly where your emails are landing. So whether
> it's landing in the primary inbox, promotion, spam, it'll give you a bunch of
> different email addresses, kind of dummy email addresses. You send campaigns
> to that list, and they'll tell you how often you land in different inboxes.

# Os 3 passos

1. Pegar a lista de **100+ endereços** que a plataforma fornece (L8756).
2. Disparar uma campanha para essa lista (L8756, L8510).
3. Receber de volta o relatório de placement por caixa: main inbox / promotions
   / spam (L8754-8756).

A fala acrescenta que a própria plataforma entrega as instruções (L8512): "It'll
give you the step-by-step instructions on what to do to get the most out of it.
Make sure you can test everything accurately."

# Cadência

Slide, verbatim (L8757):

> If you struggle with deliverability, consider using one of their tests once
> per month.

Condicional em duas camadas: **só se houver problema**, e mesmo assim
"consider". Não é rotina. A fala vai na mesma direção pelo lado do custo:
"Eventually, you will have to get onto a plan. But for the purposes here, you
guys probably shouldn't" (L8508) — a frase morre antes de completar o que não se
deve fazer, mas o sentido é que o plano pago não é necessário para o uso
descrito.

# O que fazer com o resultado

O corpus só diz que o resultado orienta a decisão (L8514): "after that, you can
determine where your deliverability is and what steps have to be taken based off
the metrics." Quais passos, o material não lista aqui. Os vizinhos são
[[reparo-de-reputacao]] (para spam) e a ferramenta não nomeada de otimização de
HTML (para promotions, L8641-8643, ver [[evidencia-e-lacunas-do-warming-do-dominio]]).

# Não confundir com o domain-checker

Mesma empresa, duas ferramentas diferentes, usadas em momentos diferentes:

| Ferramenta | O que mede | Quando | Linha |
|---|---|---|---|
| `glockapps.com/domain-checker` | se faltam registros DNS | antes de enviar qualquer email | L8691, ver [[setup-tecnico]] |
| teste de placement (esta nota) | onde os emails estão caindo | quando há problema, ~1x/mês | L8754-8757 |

A fala mistura as duas: em L8414 chama o Glockapps de "a domain checker" e diz
que ele "will let you know if your deliverability is in a good spot and if
the technical setup is looking right" — as duas funções numa frase só. O slide
separa (L8691 vs L8752-8757).

# O que o corpus não diz

- Que percentual de primary inbox é aceitável no relatório. Nenhum alvo.
- Se a campanha de teste deve ser uma campanha real ou uma feita para o teste.
- O que "struggle with deliverability" significa em número — não há gatilho
  medido para começar a testar.
- Quanto custa o plano pago, ou o que o gratuito limita.
