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
3. **Por seção pedida, partir da lista** em `secoes/_<secao>.md`. Consulta
   o campo `secao` de cada variante.
4. **Eliminar por `exige:`** contra o perfil de ativos da loja. Consulta o
   campo `exige`. Sem o ativo, a variante não é pior — é impossível.
5. **Eliminar por veto** — consulta `momento_vetado` e `registro_vetado`,
   o "Quando NÃO usar" tornado legível por máquina.
6. **Eliminar por capacidade** — consulta `product_slots` e `itens` contra
   o catálogo real da loja.
7. **Rankear por ordenação lexicográfica com degradação** — consulta
   `objecao`, `registro`, `paleta`, `papel_na_peca`, nesta ordem. Ver
   "O ranking do passo 7" abaixo.
8. **Conferir `convivencia:`** e o orçamento de `peso` contra as variantes
   já escolhidas para as outras seções da mesma peça.
9. **Desempatar** pela chave de decisão em `secoes/_<secao>.md` — a tabela
   que cada nota de seção mantém para exatamente este caso.

# O ranking do passo 7

Ordem dos eixos: **`objecao` → `registro` → `paleta` → `papel_na_peca`.**

`momento` não entra nesta lista: já foi consumido como filtro nos passos
4-6. Quem chega ao passo 7 já cabe no momento pedido, e rankear por um
critério que já foi usado para eliminar não separa mais nada.

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

`registro` vem depois porque é forte como veto e fraco como ranking — três
das nove heroes servem "premium", então sozinho não separa. `paleta` é
cosmético: duas variantes com a mesma objeção e paletas diferentes estão
as duas certas, e o design system diz como adaptar a cor. `nicho` não
entra como eixo próprio: é proxy de objeção, não a coisa em si —
"skincare" não diz se o e-mail ataca eficácia ou preço. É o que o código
tenta hoje, com `niche_affinity` peso 3 sobre um campo vazio na quase
totalidade das variantes.

**A regra de degradação.** Objeção não discrimina em toda seção. Nos
quatro footers o que separa é número de destinos de navegação e paleta —
nenhum ataca objeção alguma (os quatro declaram `objecao: []`); o mesmo
vale para `header`. Portanto:

> Se **todos** os candidatos restantes declaram a mesma `objecao` ou
> nenhuma, o eixo é neutro naquela seção: desce para `registro`, e assim
> por diante até `papel_na_peca`. Se todos os eixos forem neutros, o
> desempate é o passo 9.

# Por que lexicográfico e não soma ponderada

Com ordenação lexicográfica você sempre consegue dizer qual critério
decidiu: "ganhou porque `objecao` bateu; se não fosse isso, teria sido
`registro`". Com pesos somados — o modelo que `component-deriver.ts:85-117`
usa hoje (`niche_affinity` peso 3, `positioning` peso 2, `mood` peso 1) —
o resultado não é auditável: um número final não diz qual campo pesou
mais, e pesos arbitrários aplicados sobre campos vazios na maior parte do
catálogo produzem empate universal, que é exatamente o estado atual do
pipeline.

# Quando nenhuma variante sobrevive

Declarar a lacuna, cair no template global, e registrar o caso em
`lacunas/`. Um zero-elegíveis recorrente é o sinal mais valioso que o
sistema produz — diz exatamente qual variante falta comprar ou construir.
Casos já registrados nesse padrão: [[header-sem-variante]] e
[[cta-sem-variante]] (zero variantes para a seção inteira, sempre) e
[[welcome-5-sem-variante-ativa]] (variantes existem, mas nenhuma ativa
serve a objeção pedida — o caso concreto abaixo).

# Teste de validação

O protocolo tem que reproduzir decisões já validadas na prática. Caso de
referência: `intencoes/welcome/5.md` declara a objeção do canal ("por que
comprar de vocês?") → `objecao: confianca-no-canal`. Na seção `body`,
[[body-5-comparacao-nos-vs-eles]] declara `objecao: [confianca-no-canal,
preco-valor]` (overlap 1) e `body 4 — tutorial de uso` declara
`objecao: [uso-aprendizado]` (overlap 0). O passo 7 escolhe a comparação —
que é exatamente o que [[medicube-comparacao-categoria]] faz no toque #5
real.

O mesmo caso entrega o primeiro achado do protocolo: **[[body-5-comparacao-nos-vs-eles]]
está `ativa: false`.** Não há hoje variante ativa que sirva a objeção do
welcome #5. Sem o eixo `objecao` isso é invisível — o pipeline simplesmente
não tem como saber que faltou; com o eixo, os passos 4-6 zeram o universo
de candidatas e o caso vira lacuna declarada, não silêncio. Registrado em
[[welcome-5-sem-variante-ativa]].

---

Ponte de parâmetros: [[_parametros-da-loja]] · Números da biblioteca:
[[_inventario]]
