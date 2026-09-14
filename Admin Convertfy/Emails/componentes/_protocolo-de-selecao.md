---
tipo: protocolo
status: aprovada
fonte: spec §6-6.2 (2026-08-31-vault-componentes-email-design.md)
---

Como escolher uma variante para uma seção de um e-mail, dado o toque, a
estrutura de referência (se houver) e a loja. Nove passos, na ordem. A
ordem é a regra: **eliminar antes de rankear, sempre**.

# Os nove passos

1. **Ler a intenção do toque** — `intencoes/<flow>/<n>.md`. Não consulta
   frontmatter de variante ainda: define qual objeção este e-mail ataca e
   qual papel é pedido de cada bloco — os alvos contra os quais os passos
   seguintes vão filtrar e rankear.
2. **Ler a estrutura de referência**, se houver — `estruturas/<flow>/<slug>.md`.
   Quais seções, em que ordem, com que papel. Também externo ao
   frontmatter da variante; quando existe, resolve o passo 9 antes mesmo de
   chegar nele.
3. **Por seção pedida, partir da lista** em `secoes/_<secao>.md`, restrita
   a `ativa: true` **e `schema_campos > 0`**. Consulta os campos `secao`,
   `ativa` e `schema_campos` de cada variante — inativa não é candidata, e
   variante sem schema não é preenchível: mesmo escolhida, o passo de copy
   do pipeline não tem endereço para escrever. É o caso de
   `footer-4-dark-mega-menu` — ativa e com julgamento completo, ainda assim
   fora ([[cinco-variantes-sem-schema]]). Atalho: [[_catalogo]] tem todos
   esses campos das 44 variantes em uma única tabela, servindo os passos
   3–8 sem abrir nota por nota.
4. **Eliminar por `exige:`** contra o resolvedor de requisitos (código):
   cada requisito de `classe: gate` é respondido contra a
   `fonte_resolucao` que a própria nota declara (outline do flow,
   `products.json`, `store_brand_identity`, pesquisa com citação — ver
   [[_parametros-da-loja]], Parte 2). Sem o ativo, a variante não é pior —
   é impossível. Requisito de `classe: diretiva_imagem` **não elimina**:
   sai de `exige`, mora em `diretivas_de_imagem` e vira brief da foto.
5. **Eliminar por `momento`** — dois mecanismos. O veto: consulta
   `momento_vetado` e `registro_vetado`, o "Quando NÃO usar" tornado
   legível por máquina. A declaração positiva: se `momento` da variante é
   uma lista **não vazia** que não inclui o momento do e-mail, elimina.
   Lista vazia (`momento: []`) **não elimina** — significa que a variante
   não discrimina por momento, não que ela não serve a nenhum (é o caso
   dos 4 footers e das 4 body sem-julgamento — ver o aviso na seção do
   ranking abaixo).
6. **Eliminar por capacidade** — consulta `product_slots` e `itens` contra
   o catálogo real da loja.
7. **Rankear por ordenação lexicográfica com degradação** — consulta
   `objecao`, `registro`, `paleta`, `papel_na_peca`, nesta ordem. Ver
   "O ranking do passo 7" abaixo.
8. **Conferir `convivencia:`** e o orçamento de `peso` contra as variantes
   já escolhidas para as outras seções da mesma peça. Ver "O orçamento de
   `peso`" abaixo.
9. **Desempatar** pela chave de decisão em `secoes/_<secao>.md` — a tabela
   que cada nota de seção mantém para exatamente este caso. Se nem ela
   separa — empate total — aplicar "O desempate final" abaixo. O resultado
   nunca é sorteio.

# O ranking do passo 7

Ordem dos eixos: **`objecao` → `registro` → `paleta` → `papel_na_peca`.**

`momento` não entra nesta lista: já foi consumido como filtro no passo 5
(veto e declaração positiva). Quem chega ao passo 7 já cabe no momento
pedido, e rankear por um critério que já foi usado para eliminar não
separa mais nada.

**Por que `objecao` primeiro.** É o eixo em que o vault já pensa.
`intencoes/welcome/_flow.md` declara que o flow é uma varredura de
objeções, não uma repetição de oferta — cada toque assume que o anterior
falhou e ataca uma objeção de natureza diferente. O inventário fala a
mesma língua sem ter sido desenhado para isso: `review 1` se define por
"objeção de eficácia ou segurança", `offer 5` por "objeção de preço em
marca premium", `products 2` por "quando a objeção é 'o que exatamente tem
nisso'". O "quando NÃO usar" do `review 5` já desempata por objeção
explicitamente: "Objeção técnica ou de segurança — use a variante de
cards com credencial."

`registro` vem depois porque é forte como veto e fraco como ranking —
três das nove heroes servem "premium", então sozinho não separa. `paleta`
é cosmético: duas variantes com a mesma objeção e paletas diferentes
estão as duas certas, e o design system diz como adaptar a cor. `nicho`
não entra como eixo próprio: é proxy de objeção, não a coisa em si —
"skincare" não diz se o e-mail ataca eficácia ou preço. É o que o código
já tentou — pontuar `niche_affinity`/`positioning`/`mood` num pré-filtro
determinístico, removido junto com o resto do pré-filtro (commit
`f0fcd72d`) — não o que ele tenta hoje: `niche_affinity` não existe em
nenhum código de score atual.

**A regra de degradação.** Objeção não discrimina em toda seção. Nos
quatro footers o que separa é número de destinos de navegação e paleta —
nenhum ataca objeção alguma (os quatro declaram `objecao: []`); o mesmo
vale para `header`. Portanto:

> Se nenhum candidato restante declara a `objecao`-alvo do e-mail — seja
> porque **todos** declaram a mesma `objecao` ou nenhuma, seja porque
> **cada um declara uma `objecao` diferente entre si**, sem que nenhuma
> bata com o alvo — o eixo é neutro naquela seção: todos empatam em
> overlap zero e o ranking desce para `registro`, e assim por diante até
> `papel_na_peca`. Se todos os eixos forem neutros, o desempate é o
> passo 9.

O segundo caso é o do hero no Caso A de [[_casos-de-teste]]: hero-3
declara `preco-valor`, hero-8/hero-10 declaram `amplitude-de-catalogo` —
três candidatos, três leituras de `objecao`, nenhuma delas
`qualidade-eficacia` (o alvo do e-mail). Nenhum dos três repete a
`objecao` de outro, mas o eixo ainda é neutro: overlap zero nos três é o
que importa, não se as objeções declaradas coincidem entre si.

# Por que lexicográfico e não soma ponderada

Com ordenação lexicográfica você sempre consegue dizer qual critério
decidiu: "ganhou porque `objecao` bateu; se não fosse isso, teria sido
`registro`". Com pesos somados, o resultado não é auditável: um número
final não diz qual campo pesou mais, e pesos arbitrários aplicados sobre
campos vazios na maior parte do catálogo produzem empate universal.

O histórico do próprio pipeline corrobora esse argumento em vez de ser o
alvo dele. O Montador já teve um pré-filtro determinístico que pontuava
candidatas por soma ponderada de campos categóricos, antes de qualquer
leitura de marca — removido no commit `f0fcd72d`. O comentário deixado no
código explica o motivo: *"ele decidia quem o LLM podia ver a partir de
três campos categóricos, antes de qualquer leitura de marca. Agora o
Curador recebe o catálogo INTEIRO — no system prompt, para ser cacheável
— e é ele quem corta."* Ou seja: o
pipeline tentou soma ponderada, produziu o tipo de empate que o argumento
acima prevê, e foi removido por causa disso — não apesar disso.

# O orçamento de `peso`

Os limiares de `classe` de `peso` não estão declarados em nenhuma outra
nota deste vault — vêm da spec, fora dele
(`docs/superpowers/specs/2026-08-31-vault-componentes-email-design.md:227`):
`leve` <600px · `medio` 600-1200px · `pesado` 1200-2000px ·
`peca-inteira` >2000px (`altura_px`, `fonte: declarado` quando a prosa da
variante afirma, `fonte: medido` quando somado das alturas e paddings
explícitos no HTML — nunca estimado no olho).

O que a spec **não** declara é um número de orçamento por peça — um teto
de `altura_px` somada para o e-mail inteiro, ou uma contagem máxima de
blocos `pesado`/`peca-inteira` por peça. Isso não existe, aqui nem na
spec. O passo 8 é, nessa parte, **qualitativo**: soma as classes das
seções já escolhidas e evita repetir `pesado`/`peca-inteira` em sequência
sem uma seção `leve`/`medio` entre elas — não há limiar numérico para
aplicar automaticamente.

# O desempate final (empate total)

Empate total é quando dois candidatos chegam ao fim do passo 9 idênticos
em todos os eixos e a própria chave de decisão da seção declara que nada
os separa. Hoje são dois pares, ambos duplicatas de cadastro:
[[hero-8-lineup-com-lembrete-de-oferta]] ≡ [[hero-10-lineup-de-colecao]]
(ver [[hero-8-duplicata-de-hero-10]]) e
[[reviews-3a-depoimento-longo-monoespacado]] ≡
[[reviews-3b-depoimento-longo-monoespacado]] (ver [[reviews-3-duplicado]]).

A regra: **vence a menos usada no histórico de envios** — a contagem de
peças já montadas com cada `variant_id`, consultada no banco do pipeline
(o mesmo de onde vem a fila de disparos; ver [[_parametros-da-loja]]).
Empate total significa que as duas servem igualmente bem; escolher a menos
gasta rotaciona o criativo em vez de viciar na mesma peça — e de quebra
corrige a distorção estatística que as lacunas de duplicata descrevem, em
que a peça dobrada pesava o dobro no sorteio.

**Fallback determinístico:** a consulta de uso ainda não tem campo
mapeado em [[_parametros-da-loja]] ("quantas vezes cada variante já foi
usada"). Se o histórico não estiver disponível na hora da seleção, ou se
as contagens empatarem, **o menor número no slug vence** — hero-8 antes de
hero-10, reviews-3a antes de reviews-3b.

Isso resolve a escolha, não a duplicata: os pares continuam registrados em
`lacunas/` até o banco reconciliar `variant_id` e `schema_campos`.

# Quando nenhuma variante sobrevive

Declarar a lacuna e parar o batch no Curador com a lacuna nomeada —
nunca cair em silêncio no fallback de `email_reference_templates` — e
registrar o caso em `lacunas/`. Um zero-elegíveis recorrente é o sinal mais valioso que o
sistema produz — diz exatamente qual variante falta comprar ou construir.
Casos já registrados nesse padrão: [[header-sem-variante]] e
[[cta-sem-variante]] (zero variantes para a seção inteira, sempre) e
[[welcome-5-sem-variante-ativa]] (variantes existem, mas nenhuma ativa
serve a objeção pedida — o caso concreto abaixo).

# Teste de validação

O protocolo tem que reproduzir decisões já validadas na prática. Caso de
referência: `intencoes/welcome/welcome-5.md` não tem campo `objecao` no
frontmatter — a objeção do canal ("por que comprar de vocês?") só existe
em prosa nessa nota. Traduzida para o vocabulário do vault, ela mapeia
para `objecao: confianca-no-canal`. Na seção `body`,
[[body-5-comparacao-nos-vs-eles]] declara `objecao: [confianca-no-canal,
preco-valor]` (overlap 1) e `body-4-comparativo-em-duas-colunas` declara
`objecao: [qualidade-eficacia, preco-valor]` (overlap 1; em versão
anterior a nota descrevia um tutorial com `uso-aprendizado`, overlap 0 —
histórico no Git). Por ranking puro de `objecao`, body-5 venceria.

**Mas o mesmo caso entrega o primeiro achado do protocolo:
[[body-5-comparacao-nos-vs-eles]] está `ativa: false`.** O passo 3 já a
elimina — restrito a `ativa: true` — antes mesmo de o ranking do passo 7
entrar em jogo. Sem o eixo `objecao` essa perda é invisível: o pipeline
simplesmente não tem como saber que faltou candidata para essa objeção.
Com o eixo, o passo 3 já zera a única variante do catálogo que serve
`confianca-no-canal`, e o que sobra — `body-4` (overlap 0) e as quatro
`body` sem-julgamento (`objecao` vazia) — não substitui: pelo mesmo
argumento da regra de degradação acima, overlap zero não é "segunda
opção", é lacuna. **Não há hoje variante ativa que sirva a objeção do
welcome #5; o resultado é zero variantes elegíveis, não a escolha de
body-5.** O caso vira lacuna declarada, não silêncio — registrado em
[[welcome-5-sem-variante-ativa]] e reproduzido passo a passo no Caso B de
[[_casos-de-teste]].

---

Ponte de parâmetros: [[_parametros-da-loja]] · Números da biblioteca:
[[_inventario]] · Mapa do vault: [[_INDEX]]
