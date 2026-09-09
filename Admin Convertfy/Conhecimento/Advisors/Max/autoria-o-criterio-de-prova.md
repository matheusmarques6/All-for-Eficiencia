---
tipo: indice
assunto: autoria
autor: max-sturtevant
status: aprovado
---

Este é o método usado para decidir quem fala em cada bloco do corpus de Max: os cinco níveis de classificação de autoria (`max-provado`, `max-provavel`, `outro-provado`, `outro-provavel`, `indeterminado`), o que cada um exige como prova, e o critério estilométrico que sobreviveu ao teste — idioleto medido, não saudação de abertura. Aplicado bloco a bloco em [[autoria-tabela-mestra-de-quem-narra]].

# 1. O problema e por que importa

O corpus inteiro existe para clonar o julgamento de **uma** pessoa. O material
bruto, porém, é uma compilação de curso: 41 blocos de fala de origens diferentes
— aulas gravadas, vídeos de YouTube reaproveitados, walkthroughs de tela — mais
nove decks GAMMA. Nada no arquivo declara quem fala em cada bloco.

Uma linha prova que não é sempre a mesma pessoa. **L5753** diz:

> "So we have a email marketing brain, something that **Max had put together
> himself**. And it's awesome."

Terceira pessoa. Se essa faixa entrar no corpus como fala do Max, o advisor
passa a devolver, na voz dele e com a autoridade dele, o julgamento de outra
pessoa — e não há como um leitor da nota perceber. É o único tipo de erro deste
corpus que é **invisível na saída**: um número errado alguém confere, uma voz
errada ninguém confere.

Este laudo determina, bloco a bloco, quem fala.

---

# 2. O padrão de prova

Cinco níveis. Cada classificação exige evidência **nomeada por linha**.

| Nível | O que exige |
|---|---|
| `max-provado` | O narrador se identifica: é chamado de "Max" na própria fala, ou reivindica em primeira pessoa um ativo que só Max possui — o link de afiliado `omnisend.com/max`, a agência Well Copy, a comunidade Skool, o custom GPT, os designers da agência, o canal de YouTube. |
| `outro-provado` | O narrador fala de Max em terceira pessoa. |
| `max-provavel` | Sem auto-identificação nominal, mas com o **idioleto** de Max (ver §2.1) e/ou continuidade anunciada em primeira pessoa a partir de um bloco `max-provado`. |
| `outro-provavel` | Pertence ao aglomerado estilométrico do único bloco `outro-provado`, com **ausência total** dos marcadores de idioleto de Max e presença dos marcadores complementares. |
| `indeterminado` | Não há fala, ou não há sinal. |

**Assinatura de abertura não é prova de nada.** Isto foi testado e falhou — ver
§5. Um bloco classificado só pela abertura não recebe classificação nenhuma.

## 2.1 O critério que sobreviveu: idioleto, não assinatura

Cinco marcadores, medidos por ocorrência sobre o total de palavras faladas. As
duas colunas são o aglomerado A (75.381 palavras) e o aglomerado B (25.141
palavras), definidos ao fim desta medição, não antes dela.

| Marcador | A (/1.000 pal.) | B (/1.000 pal.) | Razão |
|---|---|---|---|
| "I recommend" / "I'd recommend" / "I highly recommend" | 0,42 (32×) | **0,00 (0×)** | ∞ |
| "my favorite" | 0,19 (14×) | **0,00 (0×)** | ∞ |
| "I like to" | 0,62 (47×) | 0,04 (1×) | 16× |
| "at the end of the day" | 0,027 (2×) | **1,03 (26×)** | 39× |
| "obviously" | 0,19 (14×) | **1,75 (44×)** | 9,4× |

Os três primeiros são **enunciados de preferência pessoal** — a marca de quem
tem autoridade própria sobre o assunto. Os dois últimos são **muletas de
discurso**. Se o aglomerado B fosse a mesma pessoa, a taxa de "I recommend" do
aglomerado A projetaria 10,6 ocorrências esperadas em B; observaram-se **zero**
(Poisson, λ=10,6 → p ≈ 2,5·10⁻⁵). Na direção inversa, a taxa de "at the end of
the day" de B projetaria 78 ocorrências em A; observaram-se **duas**.

Reforço independente, o **fecho de vídeo**. Os dez blocos do aglomerado B fecham
com pedido coletivo — "hit us up" (L4420, L9108), "reach out to us" (L4674),
"shoot us over emails, ask us questions. We're here for you" (L4827), "thank you
guys ... see you in the next one" (L5153, L5865, L6081, L6247, L8516, L8645).
Essa fórmula **não ocorre nenhuma vez** fora do aglomerado B. Os blocos
`max-provado` fecham no singular: "let me know if you have any questions" (L677,
L8063), "message me or the group" (L2616), "book a call with me" (L9259).

## 2.2 O teste que decidiu

Em **25.141 palavras** do aglomerado B não existe **um único possessivo de
primeira pessoa sobre ativo de negócio**. Varredura exaustiva de `my \w+`
naquelas faixas devolve, ao todo: `my inbox`, `my dad`, `my head` (2×), `my
camera`, `my list` (hipotético), `my brand` (hipotético). Nada mais.

Nas faixas `max-provado` o mesmo padrão devolve: `my link` (L34), `my checklist`
(L617), `my resources` (L686), `my agency` (L6350), `my community my school`
(L6279), `my designers` (L6458), `my channel` (L6499), `my company's name`
(L8046), `my clients` (L9237), `my newsletter` (L6350), além de `my favorite`
14×.

É essa assimetria — não a saudação — que sustenta o laudo.


---

O resultado da aplicação deste critério está em
[[autoria-tabela-mestra-de-quem-narra]]. As provas nomeadas (§4) e a refutação
da hipótese da assinatura (§5) estão em [[autoria-evidencias-e-o-que-caiu]]. A
consequência por pasta (§6) e o que ficou em aberto (§7) estão em
[[autoria-consequencia-por-pasta]]. Visão geral: [[mapa-da-autoria]].
