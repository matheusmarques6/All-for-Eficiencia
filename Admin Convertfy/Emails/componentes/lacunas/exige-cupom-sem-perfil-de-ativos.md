---
tipo: lacuna
sobre: codigo
secao: hero
descoberta_em: 2026-09-09
status: aberta
---

As quatro heroes que servem `welcome-1` (hero-3, hero-4, hero-5, hero-6)
exigem `cupom-ativo`, nenhum campo da loja responde se existe cupom, e o
alvo do Seletor proíbe inventar código, valor ou expiração de incentivo —
em 4 de 4 runs a hero escolhida exigiu o que o alvo proíbe.

# O que falta

Um perfil de ativos da loja que responda "tem cupom ativo?" antes do
passo 4 do [[_protocolo-de-selecao]] — e, enquanto ele não existe, uma
hero de `welcome-1` que não dependa da resposta.

O que o catálogo declara, conferido nas notas (linha `exige:`) e em
[[_catalogo]]: [[hero-3-cupom-de-captacao]] (`exige: [cupom-ativo,
foto-estudio-fundo-claro, terco-superior-liso]`),
[[hero-5-cupom-em-tres-lugares]] (`[cupom-ativo, foto-com-pessoas]`) e
[[hero-6-percentual-gigante]] (`[foto-monocromatica, cupom-ativo]`)
exigem cupom. Além dessas três, [[hero-4-editorial-de-pertencimento]]
(`[serif-ou-script-display, foto-de-campanha-propria, cupom-ativo,
cor-de-acento-definida]`) também — [[_hero]] já lê as quatro juntas:
"hero-3/4/5/6 exigem cupom ativo no sentido literal de `exige`". As
quatro são exatamente as que declaram `momento: [welcome-1]`. As outras
cinco não chegam ao toque 1: hero-7 e hero-9 listam `welcome-1` em
`momento_vetado`; hero-2, hero-8 e hero-10 declaram `momento` não vazio
sem `welcome-1` e caem no passo 5. Para uma loja sem cupom confirmado, o
universo de hero do welcome-1 é **zero** — e o único offer que declara
`momento: [welcome-1]`, [[offer-4-manifesto-antes-do-cupom]], também exige
`cupom-ativo` e está `ativa: false`: o toque 1 não tem offer ativo, com ou
sem cupom.

O que a loja tem para responder: nada. [[cupom-ativo]] é
`verificavel_hoje: false` ("Não verifica automaticamente hoje. Nenhum
campo de `client_stores` responde a esta pergunta"). A Parte 2 de
[[_parametros-da-loja]] diz por quê: "não existe em `client_stores`
nenhuma coluna ou tabela que responda 'esta loja tem cupom ativo? UGC
autorizado? estoque integrado?'", e na
tabela "Comercial (8)" a linha de `cupom-ativo` tem veredito "nenhum campo
de `client_stores` responde". [[o-que-o-curador-ainda-nao-tem]] fecha o
circuito nos itens 1 e 4: o catálogo enviado ao Curador **não inclui
`exige`** (item 1) e não há perfil de ativos para cruzar mesmo que
incluísse (item 4) — o que sobra é o prompt pedir "bloco que exige dado
que a loja não tem (campo de cupom sem oferta no contexto) fica fora",
inferência do LLM sobre texto.

O que a telemetria mediu (briefing de 2026-09-09, T3): o alvo do Seletor
proíbe "inventar código, valor ou expiração de incentivo" quando a loja
não confirmou promoção ativa; em 4 de 4 runs a hero escolhida exige o que
o alvo proíbe. É o `protocol_violations` do tipo `proibicao_violada ×
exige` da §4.3 do briefing.

# Por que importa

`exige` é eliminatório, não preferência: "Sem o ativo, a variante não é
pior — é impossível" (passo 4 do protocolo). Para cupom, [[cupom-ativo]] é
explícito: as variantes "são construídas em volta do código: pílula, barra
do topo, label do botão. Sem cupom os slots ficam vazios e a peça não
degrada — desmonta". E as quatro heroes carregam
[[incentivo-precisa-existir-em-texto]] — código, valor e prazo em texto
real, nunca só na imagem — então um código inventado não fica escondido:
é o texto mais visível do e-mail.

As quatro heroes não estão erradas. O toque 1 existe para entregar o
incentivo — regra 1 de [[_flow]] ("entregue no toque 1, inteiro e sem
fricção"), `trabalhos_fixos: [entrega_de_incentivo, ...]` e a proibição
"condição nova no incentivo" em `intencoes/welcome/welcome-1.md`. Para a
loja que prometeu cupom no opt-in, elas são a escolha certa. O buraco é a
montante: nada diz ao pipeline em qual caso ele está. Sem a resposta, o
passo 4 "roda com o que o humano souber responder"
([[_parametros-da-loja]]) — no Caso A de [[_casos-de-teste]] o perfil da
loja foi declarado à mão no enunciado, e só por isso hero-3 sobreviveu —
e em produção o Curador infere do texto, o Seletor proíbe inventar e a
hero tem um slot obrigatório de código: as três coisas colidem na mesma
run, e a copy é quem paga.

Há dois problemas com dois donos. Do lado do código, os itens 1 e 4 de
[[o-que-o-curador-ainda-nao-tem]]. Do lado da biblioteca, esta lacuna:
mesmo com o perfil pronto, uma loja que responda "não" fica com zero
heroes para o welcome-1 — [[avelmore-inspecao-antecipada]] já avisa que
sem incentivo ativo "o hero e o bloco 3 perdem o fechamento; a estrutura
desmonta", e não há estrutura nem variante para o toque 1 sem cupom.

# O que se perde hoje

Toda run de welcome-1 para loja sem promoção confirmada termina de um de
dois jeitos, ambos invisíveis ao pipeline: um incentivo inventado (viola
o alvo do Seletor e o "prometido" da regra 1 — promete o que a loja não
deu) ou uma hero com o slot de código vazio (a peça "desmonta"). Não há
campo para checar antes, não há lacuna servida ao Curador para declarar, e
a violação só aparece depois, na contagem de `protocol_violations`. E o
passo 4 não distingue "loja com cupom mas sem foto monocromática" de
"loja sem cupom" — a eliminação é tudo-ou-nada sobre um dado que ninguém
tem.

# Fora do escopo desta entrega

Criar a coluna ou tabela de perfil de ativos em `client_stores` e incluir
`exige` no catálogo enviado ao Curador (código — itens 1 e 4 de
[[o-que-o-curador-ainda-nao-tem]]); a pergunta "a loja tem cupom ativo?"
como parte do julgamento servido antes do protocolo (T4); e construir uma
hero de welcome-1 sem cupom (variante nova, `variant_id` no banco).
Registrado para a decisão não se perder.
