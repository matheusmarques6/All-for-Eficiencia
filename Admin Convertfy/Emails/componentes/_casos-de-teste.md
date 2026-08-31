---
tipo: casos-de-teste
status: aprovada
fonte: spec §11 (2026-08-31-vault-componentes-email-design.md)
---

Dois casos rodados à mão contra [[_protocolo-de-selecao]], seção por seção,
com o traço completo de eliminação. Depois, o resultado das checagens de
aceitação da §11.

O valor está no traço — quem foi eliminado, em que passo, contra qual
campo — não na conclusão final.

# Caso A — welcome #1, skincare premium com cupom

**Entrada.** Toque: [[1|welcome 1]]. Objeção dominante: `qualidade-eficacia`
(ticket médio-alto, "eficácia" no enunciado). Estrutura de referência:
[[avelmore-inspecao-antecipada]] — `secoes: [header, hero, body, body,
products, cta, reviews, footer]`.

**Perfil de ativos da loja** (traduzido para o vocabulário de
[[_parametros-da-loja]]): `cupom-ativo`, `foto-estudio-fundo-claro`,
`terco-superior-liso`, `serif-ou-script-display`, `produtos-com-pagina-propria`
(6), `depoimento-com-credencial`, `foto-do-depoente` (3 depoimentos).
Ausentes, por declaração explícita do caso: `foto-de-campanha-propria`,
`ugc-autorizado`, `estoque-integrado`. Não declarados (tratados como
ausentes por omissão): `cor-de-acento-definida`, `foto-com-pessoas`,
`foto-monocromatica`, `desconto-automatico-sem-cupom`, `motivo-sazonal`,
`gift-card-digital`, `acervo-por-angulo`, `colecao-ou-kit`,
`fragmentos-de-contorno`, `grade-de-tamanho-real`.

## hero

Passo 3 — universo de 9, lista em [[_hero]].

Passo 4 (`exige:`), contra o perfil acima:

| Variante | `exige` | Resultado |
|---|---|---|
| [[hero-3-cupom-de-captacao]] | cupom-ativo · foto-estudio-fundo-claro · terco-superior-liso | **sobrevive** — os três presentes |
| [[hero-4-editorial-de-pertencimento]] | serif-ou-script-display · **foto-de-campanha-propria** · cupom-ativo · **cor-de-acento-definida** | eliminada — falta `foto-de-campanha-propria` (negado explicitamente no caso) e `cor-de-acento-definida` (não declarada) |
| [[hero-5-cupom-em-tres-lugares]] | cupom-ativo · **foto-com-pessoas** | eliminada — falta `foto-com-pessoas` |
| [[hero-6-percentual-gigante]] | **foto-monocromatica** · cupom-ativo | eliminada — falta `foto-monocromatica` |
| [[hero-7-campanha-sem-cupom]] | **desconto-automatico-sem-cupom** · **duas-ou-tres-cores-de-identidade** · **desconto-escalonado** · foto-estudio-fundo-claro · terco-superior-liso | eliminada — três requisitos ausentes; além disso incompatível com `cupom-ativo` real da loja |
| [[hero-2-pergunta-comparativa]] | **cor-de-acento-definida** · **desconto-percentual** · **macro-de-produto** | eliminada — os três ausentes |
| [[hero-9-atendimento-proativo]] | **foto-monocromatica** · terco-superior-liso · **duas-acoes-de-suporte** | eliminada — dois de três ausentes |
| [[hero-10-lineup-de-colecao]] | foto-estudio-fundo-claro · terco-superior-liso | **sobrevive** |
| [[hero-8-lineup-com-lembrete-de-oferta]] | idêntico a hero-10 | **sobrevive** (duplicata de decisão, ver [[hero-8-duplicata-de-hero-10]]) |

Sobreviventes ao passo 4: hero-3, hero-8, hero-10.

**Nota de leitura do protocolo — achado 1.** A brief original desta task
esperava `hero-4` como candidata viável. O caso, como escrito aqui, nega
explicitamente `foto-de-campanha-propria` — um dos quatro requisitos de
hero-4 — então ela é eliminada no passo 4. Isso é o resultado real, não o
esperado; documentado, não forçado.

Passo 5 (veto) — `momento_vetado` de nenhum dos três sobreviventes lista
`welcome-1` (hero-3: veta carrinho/checkout/browse-abandonment/
transacional/sazonal/lançamento; hero-8/10: vetam carrinho/checkout/
transacional). `registro_vetado`: hero-3 veta `luxo` — a loja não declara
registro `luxo`, sem conflito. Nenhuma eliminação neste passo.

**Nota de leitura do protocolo — achado 2 (ambiguidade genuína).** Os nove
passos, lidos literalmente, só usam `momento` como **veto** (passo 5); não
existe passo que elimine por `momento` **não** declarado. hero-8/hero-10
declaram `momento: [welcome-meio, welcome-tardio, ...]` — não incluem
`welcome-1` — mas como nada os veta explicitamente, sobrevivem ao passo 5
por leitura literal. Isso é consistente com o próprio teste de validação
do protocolo (seção "Teste de validação"), que deixa `body-4` sobreviver
ao ranking do welcome #5 mesmo com `momento: [pos-compra, reengajamento]`
— sem `welcome-5`. Assumi essa leitura literal (só veto elimina por
momento) nos dois casos deste documento.

Passo 6 (capacidade) — `product_slots: 0` nos três, sem produto a encaixar
no hero. Nenhuma eliminação.

Passo 7 (ranking, `objecao → registro → paleta → papel_na_peca`):

- `objecao`: hero-3 declara `preco-valor`; hero-8/10 declaram
  `amplitude-de-catalogo`. Nenhum dos três bate com o alvo
  `qualidade-eficacia` do e-mail — overlap zero nos três. Tratado como
  empate (zero contra zero) → eixo neutro → degrada para `registro`.
- `registro`: hero-3 declara `[]`; hero-8/10 declaram `[]`. Empate → degrada
  para `paleta`.
- `paleta`: hero-3 declara `[claro]`; hero-8/10 declaram `[claro]`.
  Empate → degrada para `papel_na_peca`.
- `papel_na_peca`: hero-3 declara `[abre]`; hero-8/10 declaram `[meio]`. O
  hero da estrutura pedida abre o e-mail (primeiro bloco de
  [[avelmore-inspecao-antecipada]]) — `abre` bate com o papel pedido,
  `meio` não. **hero-3 vence aqui.**

**Escolha final, hero: [[hero-3-cupom-de-captacao]].** Eliminação
decidida pelo passo 7 no eixo `papel_na_peca` — o único dos quatro eixos
de ranking que discriminou, depois de três empates seguidos.

## body (dois blocos — tese+incentivo e garantias em 3 ícones)

Universo ativo (7 de 9 — body-5 e body-10 são `ativa: false`): body-2,
body-3, body-4, body-6, body-7, body-8, body-9.

Passo 4 (`exige:`):

| Variante | `exige` | Resultado |
|---|---|---|
| [[body-2-colagem-de-data-comemorativa]] | foto-com-pessoas · **motivo-sazonal** | eliminada — sem motivo sazonal (welcome, não campanha de data) |
| [[body-3-pitch-de-gift-card]] | **gift-card-digital** | eliminada — loja não vende gift card |
| [[body-4-tutorial-de-uso]] | `[]` | sobrevive (vazio, nada a exigir) |
| body-6, body-7, body-8, body-9 | todos os eixos em branco (`status: sem-julgamento`) | sobrevivem por vacuidade — nenhum requisito para falhar |

Passo 5/6 — sem veto nem estouro de capacidade nos sobreviventes.

Passo 7 (ranking) — `objecao`: body-4 declara `uso-aprendizado` (overlap
zero com `qualidade-eficacia`); body-6/7/8/9 não declaram `objecao`
nenhuma (campo vazio). Zero contra zero → eixo neutro nos cinco.
`registro`/`paleta`/`papel_na_peca`: body-4 declara `[]` nos três (única
com julgamento completo, mas sem valor em nenhum eixo de ranking);
body-6/7/8/9 idem. Todos os cinco eixos empatam vazios em todos os cinco
candidatos.

**Achado 3 — zero elegíveis, também no Caso A.** Nenhum candidato
sobrevivente do body tem QUALQUER eixo de ranking que bata com o alvo do
e-mail. body-4 é a única variante *julgada* (`status: aprovada`) do grupo,
mas sua `objecao` (`uso-aprendizado`) não é a do e-mail
(`qualidade-eficacia`), e seu `momento` (`pos-compra`, `reengajamento`)
não inclui `welcome-1`. Aplicando ao Caso A o mesmo padrão que o próprio
protocolo usa no teste de validação do Caso B — "zero overlap de
`objecao`" não é preenchido por proximidade, é lacuna — nenhum dos dois
blocos de body pedidos pela estrutura (tese+incentivo; garantias em 3
ícones) tem candidata real na biblioteca. As quatro variantes
`sem-julgamento` (body-6/7/8/9) sobrevivem tecnicamente por não terem
requisito para falhar, mas [[_body]] já registra que "nunca
são escolhidas [...] enquanto houver candidata julgada" — e aqui não há
candidata julgada que sirva. O caso cai no template global para os dois
blocos de body; seria candidata a uma nota nova em `lacunas/` (não criada
aqui — está fora do escopo desta task, que só cria `_casos-de-teste.md`).

## header

Passo 3 — [[_header]] lista **zero variantes** na seção
inteira (`variantes/header/` não existe no catálogo). Lacuna estrutural,
já registrada em [[header-sem-variante]]. Cai direto no template global
sem passar pelos passos 4-9 — não há o que eliminar.

## products

Passo 3 — universo de 9 em [[_products]]. A estrutura
pede grade 2×2 (`product_slots: 4`), loja com 6 produtos com página
própria.

Passo 4/5, nas três candidatas de `slots=4` (ou próximas) inspecionadas:

| Variante | Slots | `exige` | `momento_vetado` inclui `welcome-1`? | Resultado |
|---|---|---|---|---|
| [[products-7-dois-com-galeria-de-angulos]] | 2 | acervo-por-angulo · colecao-ou-kit | não | eliminada passo 4 (nenhum dos dois declarado) |
| [[products-8a-quatro-recomendacoes]] | 4 | fragmentos-de-contorno | **sim** | eliminada passo 4 (requisito ausente) — e seria vetada no passo 5 de qualquer forma |
| [[products-9-grade-de-tamanho]] | 4 | estoque-integrado · grade-de-tamanho-real | não veta `welcome-1` diretamente | eliminada passo 4 — `estoque-integrado` é negado explicitamente no caso |

As outras seis variantes de products não foram abertas individualmente
nesta rodada (limite de orçamento da task) — mas
[[_products]] já declara em "Onde a seção não cobre":
*"nenhuma products para `welcome-1`, `welcome-meio`, `welcome-tardio`
[...]"*. Combinado com as três eliminações confirmadas acima, o resultado
é o mesmo padrão do body: **zero candidata products com evidência real de
servir `welcome-1`** dentro do orçamento desta rodada. Registrado como
achado, não como prova exaustiva das 9 variantes.

## cta

Passo 3 — [[_cta]]: **zero variantes**, mesma lacuna
estrutural do header, já nomeada como o caso concreto de
[[avelmore-inspecao-antecipada]] em [[cta-sem-variante]] (a própria nota
cita esta estrutura por nome). Cai no template global.

## reviews

Passo 3 — universo de 7 em [[_reviews]] (6 perfis reais,
reviews-3a/3b duplicadas).

Passo 4 (`exige:`), entre as três que declaram `objecao: qualidade-eficacia`:

| Variante | `exige` | Resultado |
|---|---|---|
| [[reviews-1-depoimento-com-credencial]] | depoimento-com-credencial · foto-do-depoente | **sobrevive** — os dois presentes (3 depoimentos com credencial e foto do depoente) |
| [[reviews-3a-depoimento-longo-monoespacado]] | foto-de-uso-real · reviews-longos | eliminada — nenhum dos dois declarado no caso |
| [[reviews-7-zigue-zague-com-cupom]] | selo-compra-verificada · cupom-ativo · reviews-curtos | eliminada — falta selo de compra verificada e reviews curtos (só cupom presente) |

Passo 5 — `momento_vetado` de reviews-1: carrinho-abandonado ·
checkout-abandonado · transacional. Não veta `welcome-1`. Sobrevive.

Passo 6 — `itens: {min:2, max:2}`; a loja tem 3 depoimentos disponíveis,
o slot pede 2 — capacidade satisfeita (usa 2 dos 3 disponíveis).

**Escolha final, reviews: [[reviews-1-depoimento-com-credencial]].**
Única sobrevivente ao passo 4 dentro do grupo cujo `objecao` já bate
exatamente com o alvo do e-mail (`qualidade-eficacia`) — o passo 7 nem
precisa decidir, o passo 4 já resolveu.

## footer

Passo 3 — universo de 4 em [[_footer]]. `objecao: []` nas
quatro (por desenho) → eixo neutro por construção, degrada direto para
`registro`.

**Achado 4 — subdeterminado pelos dados do caso.** O enunciado do Caso A
não declara `registro` nem `paleta` da loja, nem quantidade de destinos de
navegação — só "identidade com serif display". Sem esses dados, `registro`
(minimalista-leve / premium-editorial / bold-alto-contraste ×2) e `paleta`
(claro / full-dark) não têm como ser decididos com evidência do caso, e o
passo 9 (desempate por `secoes/_footer`) também não resolve — a estrutura
[[avelmore-inspecao-antecipada]] não declara contagem de links de
navegação. **Não forço uma escolha aqui** — os quatro footers seguem
empatados até que o caso declare `registro` ou `paleta` da loja. Isto é
diferente dos outros achados: não é lacuna do catálogo, é lacuna do
enunciado do caso.

---

# Caso B — welcome #5, ferramentas sem cupom

**Entrada.** Toque: [[5|welcome 5]]. Objeção: do canal ("por que comprar
de vocês?"), traduzida no vocabulário do vault para `confianca-no-canal`
(a mesma tradução que [[_protocolo-de-selecao]] já faz na sua seção "Teste
de validação"). Estrutura de referência:
[[medicube-comparacao-categoria]] — `secoes: [header, body, products,
footer]`. Sem cupom ativo, sem UGC, catálogo funcional, 4 produtos com
página própria.

## body

Passo 3 — mesmo universo de 7 ativas do Caso A.

Passo 4 (`exige:`) — nenhuma das candidatas com `objecao` real (body-4:
`[]`) exige nada que a loja não tenha; body-2/body-3 seguem eliminadas
pelos mesmos motivos do Caso A (sem motivo sazonal, sem gift card).

Passo 7 (ranking por `objecao`) — o candidato que de fato serve
`confianca-no-canal` no catálogo inteiro é
[[body-5-comparacao-nos-vs-eles]] (`objecao: [confianca-no-canal,
preco-valor]`, overlap 1 contra o alvo). [[body-4-tutorial-de-uso]]
declara `objecao: [uso-aprendizado]`, overlap 0. Por ranking puro, body-5
venceria.

**Mas body-5 está `ativa: false`.** Uma variante inativa não é candidata
— cai fora antes mesmo de chegar ao passo 7 (tratado aqui, junto com o
resto do catálogo, como filtro de "não é candidata" que precede o passo 3
efetivo: a lista de [[_body]] já separa "9 variantes, 7
ativas"). Sem body-5, o único candidato com QUALQUER overlap de `objecao`
com o alvo do e-mail desaparece. body-4 (overlap 0) e as quatro
sem-julgamento (sem `objecao` declarada) não substituem — pelo mesmo
argumento do achado 3 do Caso A, zero overlap não é "segunda opção", é
lacuna.

**Escolha final, body: nenhuma. Zero variantes elegíveis.** Confirma o
resultado esperado do brief e reproduz exatamente o "Teste de validação"
que a própria [[_protocolo-de-selecao]] já documenta, com a mesma
variante nomeada como causa: [[welcome-5-sem-variante-ativa]]. O template
global assume o bloco de body inteiro.

## header

Mesma lacuna estrutural do Caso A — [[_header]]: zero
variantes. [[header-sem-variante]].

## products

Passo 3 — universo de 9. A estrutura pede grade 2×2 (`product_slots: 4`),
loja com 4 produtos com página própria — bate exatamente com `itens:
{min:4, max:4}`.

Passo 4/5, nas duas candidatas de `slots=4`:

| Variante | `exige` | `momento_vetado` inclui `welcome-tardio`? | Resultado |
|---|---|---|---|
| [[products-8a-quatro-recomendacoes]] | fragmentos-de-contorno | não (veta welcome-**1**, não welcome-tardio) | eliminada passo 4 — requisito não declarado para a loja de ferramentas |
| [[products-9-grade-de-tamanho]] | estoque-integrado · grade-de-tamanho-real | **sim, explicitamente** | eliminada em ambos — passo 4 (a loja não tem estoque integrado nem grade de tamanho — é loja de ferramentas, não vestuário) e passo 5 (veta `welcome-tardio` no frontmatter) |

Mesmo padrão dos outros achados: as duas candidatas de capacidade certa
caem, e — como no Caso A — [[_products]] já documenta
zero cobertura de `welcome-meio`/`welcome-tardio` na seção inteira. Sem
abrir as 7 variantes restantes (fora do orçamento desta rodada), o
resultado observado é **zero products com evidência de servir este
toque**, reportado como achado e não como varredura completa.

## footer

Passo 3 — universo de 4. `objecao: []` nas quatro, degrada para
`registro`. A estrutura [[medicube-comparacao-categoria]] declara "4
categorias" no rodapé — isso bate com `itens: {min:4, max:6}` de
[[footer-1-menu-outline]] (único que inclui 4 na sua faixa; footer-2 é
fixo em 5, footer-3 fixo em 3, footer-4 pede 6-7). **Escolha final,
footer: [[footer-1-menu-outline]]**, decidida no passo 9 (desempate por
contagem de itens, já que `registro`/`paleta` não têm dado do caso para
decidir e a estrutura de referência declara a contagem que falta no
enunciado do Caso A).

---

# Checagens de aceitação (§11)

## Scripts

```
python .tools/test_inventario.py   → PASS (0)
python .tools/test_valida.py       → PASS (0)
python .tools/test_mede_peso.py    → PASS (0)
python .tools/valida.py            → PASS (0 problemas)
```

## Contagens

| Item | Esperado (brief original) | Esperado (real, vocabulário cresceu) | Obtido |
|---|---|---|---|
| variantes | 44 | 44 | 44 |
| html | 44 | 44 | 44 |
| eixos | 56 | 56 | 56 |
| requisitos | 49 | **52** | 52 |
| convivencia | — | 6 | 6 |
| lacunas | 9 | **15** | 15 |
| secoes | — | 8 | 8 |
| sem `exige:` | 0 | 0 | 0 |
| propostas | 0 | 0 | 0 |
| notas em rascunho | 0 | 0 | 0 |

`requisitos` e `lacunas` batem com o número **real** (52 e 15), não com o
do brief original (49 e 9) — exatamente a divergência que a task avisou
que aconteceria.

## Checagem de procedência inferida em `exige:`

Script que parseia o YAML de cada variante (não grep) e cruza contra os
requisitos com `procedencia: inferida`:

```
achados: []
```

Vazio — nenhuma variante elimina por um requisito cuja própria nota admite
não ter lastro no inventário.

---

Todas as checagens de aceitação passaram. Ver relatório da task para os
achados de protocolo (ambiguidades e lacunas descobertas ao rodar os dois
casos).

Protocolo: [[_protocolo-de-selecao]] · Ponte de parâmetros:
[[_parametros-da-loja]]
