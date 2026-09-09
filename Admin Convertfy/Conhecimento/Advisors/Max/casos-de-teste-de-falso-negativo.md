---
tipo: indice
assunto: casos-de-teste
autor: max-sturtevant
status: aprovado
---

Casos de regressão do advisor Max para a falha silenciosa: recusar uma pergunta que o corpus responde. Limiar já declarado lacuna e depois preenchido, deck que promete e fala que entrega, e conteúdo escondido atrás de grafia corrompida. Três casos (C-21 a C-23), cada um com pergunta, resposta esperada, erro típico e a peça do corpus que a falha acusa.

# Casos de falso negativo — C-21 a C-23


## C-21 · Falso negativo — o limiar de teste que já foi declarado lacuna

**Pergunta:** Quantas vezes eu preciso rodar um A/B test para o resultado valer?

**Resposta certa contém:** a régua, que existe. L8800-8816, verbatim nas partes
que importam: lista de 1.000 dividida 500/500 — `"I wouldn't say that is enough
data to make a sound conclusion"`; lista de `"100,000, 200,000, 500,000"` —
`"you can probably get away with sending one, maybe two at different times and get
pretty conclusive results"`; lista de `"5,000 to 10,000"` — `"you might want to
test that three or four times"`; e a regra explícita: `"Base it off the number of
recipients that are receiving."` (L8816). Cadência de teste de form, em outro
módulo: `"at least for like bi-weekly. Once every two weeks, run some sort of
test"` (L663).

E o que de fato falta, que a resposta nomeia: **nenhum nível de significância,
nenhum intervalo de confiança, nenhuma duração em dias e nenhum teto de testes
simultâneos.** A conclusividade é medida por volume, nunca por estatística.
Faixa `outro-provavel` (L8762-9109).

**Resposta errada típica:** "o corpus não define limiar estatístico de teste" —
recusa por lacuna que não existe. Este item já foi declarado lacuna inexistente
e sobreviveu em duas notas depois de corrigido no índice.

**Se errar, quebrou:** recuperação ([[_arquitetura]] §5, "erra um fato → conserto
o caminho de leitura") e [[_cobertura]] (§ "Cinco coisas que já foram declaradas
lacuna total e não são"). Diagnóstico agravado: se a resposta recusou, o corpus
está produzindo recusa onde tem conteúdo — a falha mais cara de todas, porque é
silenciosa.

## C-22 · Falso negativo — o deck promete e a fala entrega

**Pergunta:** Que métodos ele dá para fazer transição entre as seções do email?

**Resposta certa contém:** os quatro, todos da fala (L7550-7588):

1. **gradiente** — `"You can do things like a gradient. Take this hero section and
   use a gradient into the next section so it kind of flows together."`
   (L7552-7556);
2. **formas ou quebras de linha** — `"You can use shapes or line breaks. So it's
   not like a super clear flat line."` (L7560-7562);
3. **fundo consistente com elementos em primeiro plano** — `"You could have
   consistent background with foreground elements."` (L7570);
4. **transição atrás de foto**, o favorito dele — `"And my favorite is to add
   transitions behind photos (…) Because a customer will like go through, look at
   the photo, and scroll through the photo without even realizing it."`
   (L7580-7584).

A resposta deve dizer que o **deck** é que não lista nenhum: a seção "Email
Transitions" termina em `"Here are a few methods to do this:"` (L8307) e a linha
seguinte já é outro heading. É lacuna do slide, não do corpus.

**Resposta errada típica:** "o deck promete os métodos e não entrega; o corpus
não tem" — o escopo errado. O certo quase nunca é "o corpus não diz"; é "**este
deck** não diz".

**Se errar, quebrou:** [[_cobertura]] (falsos negativos) e a segunda lei de
manutenção do [[_arquitetura]] §5.1 — "não achar não é o mesmo que não existir".

## C-23 · Falso negativo — o conteúdo escondido atrás da grafia corrompida

**Pergunta:** Ele explica por que o framework S.C.E. é esses três princípios e
não outros?

**Resposta certa contém:** que sim, e onde. O racional falado está em
L4715-4767, **em outra aula**, e a busca literal por "S.C.E." falha porque o ASR
grafa **"SDE framework"**: `"So the SDE framework is going to be skimmable, clear
and concise and engaging."` (L4715-4717), seguido de exemplo trabalhado para
cada letra — skimmable com `"use of sections, quick copy, bolded points, just
making this super clear"` (L4717-4719) e a sequência até L4767, que fecha com o
papel dos infográficos. Reforço no deck de
campanhas (L5504-5512) e no deck de copy (L6558-6650).

O que de fato se perdeu, e a resposta nomeia: a transcrição da aula "The
Principles of Good Copy" — o marcador `Transcrição do Vídeo :` da L5615 é o
**único marcador de transcrição vazio do arquivo**. É perda de camada, não
ausência de assunto. Marcação de autoria: L4715-4767 cai em L4189-5154,
`outro-provavel`.

**Resposta errada típica:** "não há racional falado do S.C.E., só a lista dos
três princípios" — a busca textual não achou e a conclusão virou ausência.

**Se errar, quebrou:** recuperação e [[_cobertura]]. A causa raiz específica está
em [[_fontes]] §5 (grafia corrompida pelo ASR): antes de declarar lacuna,
procurar no outro registro, no outro módulo, na grafia corrompida e em imagem
embutida.

---

