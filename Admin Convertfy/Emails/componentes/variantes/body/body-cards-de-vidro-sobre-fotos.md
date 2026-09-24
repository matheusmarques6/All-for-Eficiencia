---
tipo: componente
slug: body-cards-de-vidro-sobre-fotos
secao: body
nome_no_banco: null
variant_id: null
ativa: false
legado: true
dispositivo: catalogo_por_ocasiao

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: []
momento_vetado: []

# --- eixos de ranking, na ordem do protocolo ---
objecao: []
registro: []
registro_vetado: []
paleta: []
papel_na_peca: []

# --- requisitos duros (eliminam) ---
exige: []

# --- capacidade e composição ---
product_slots: 0
itens: null
peso: { altura_px: 953, classe: medio, fonte: medido }
convivencia: []

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: "Fichas arsenal/ficha-secao-cards-vidro-sobre-fotos.md (2026-09-10) — ficha do rebuild, sem PNG de referência"
densidade_no_banco: null
schema_campos: 0
status: legado
---

Bloco de meio de e-mail que leva o leitor a explorar o catálogo por ocasião, em peças de data comemorativa ou de descoberta sem um produto único em foco: headline, sublinha e uma composição fotográfica com cards de vidro e um CTA único sobreposto. **Não é candidata** — ver o aviso abaixo.

> **⚠ Não elegível.** Esta variante não tem linha no banco (`variant_id: null`,
> `nome_no_banco: null`), não está entre as 44 do [[_catalogo]] e sua ficha de
> origem se declara incompleta: as seções 6 (design system) e 7 (direção
> fotográfica) dependem de um PNG de referência que nunca chegou, e o fim da
> ficha lista sete decisões a confirmar, não divergências medidas. Os cinco
> eixos estão vazios porque **o julgamento por eixo não foi feito** — e aqui,
> como nas quatro body sem-julgamento, eixo vazio significa "nunca foi julgada",
> não "não discrimina" (passo 5 do [[_protocolo-de-selecao]]). `ativa: false`,
> `schema_campos: 0` e `status: rascunho` a mantêm fora do passo 3 por três
> caminhos independentes. Registro da lacuna:
> [[cards-de-vidro-sem-referencia-e-sem-banco]].

## Descrição curta

Leva o leitor a explorar o catálogo por ocasião, em e-mails de data comemorativa ou de descoberta sem um produto único em foco.

## Descrição detalhada

Seção de 600×953 em três faixas: headline em itálico bold, sublinha em itálico regular colada nela e uma composição fotográfica de 600×850 com um CTA único sobreposto na base.

Mecanismos:

- **Composição achatada.** Fotos e cards de vidro (painel translúcido com desfoque) chegam num único ativo, usado como fundo da célula. A navegação por ocasião é visual: o leitor vê as ocasiões na imagem, e a seção tem um CTA só, não um link por card.
- **CTA como fecho da imagem.** O botão fica dentro da composição, a 731px do topo dela e 62px da base, e não numa linha branca abaixo. A imagem precisa reservar essa faixa.
- **Par headline + sublinha sem respiro.** Não há padding entre as duas linhas, que funcionam como uma frase em dois pesos. A sublinha começa onde a entrelinha da headline termina.

## Quando usar

- E-mails de data comemorativa ou temporada de presentes (Dia das Mães, Natal, Dia dos Namorados), quando a loja tem produtos para mais de uma ocasião.
- Welcome ou reengajamento de lojas com catálogo amplo, para mostrar variedade antes de empurrar um produto.
- Como seção de descoberta depois de um hero de oferta.

## Quando NÃO usar

- Quando o e-mail tem um produto ou oferta única como foco. Aqui o CTA é genérico e dilui a conversão.
- Quando cada ocasião precisa de link próprio: a composição achatada só comporta um destino.
- Quando a copy precisa estar visível com imagens desligadas. Tudo abaixo da sublinha depende do fundo (ver decisão 2).
- Em lojas de catálogo curto (1 a 3 SKUs), onde "qualquer ocasião" soa vazio.

## Orientações de copy para a IA

- **GLASS_TITLE:** afirmação curta sobre variedade ou ocasião, em uma linha. É o bold da seção. Sem ponto final.
- **GLASS_SUBTITLE:** complementa a headline e fecha a frase. Deve ser gerada junto com o título, porque as duas linhas são lidas como uma unidade. Sem repetir palavras do título.
- **GLASS_CTA_LABEL:** verbo + escopo ("Shop for any occasion", "Find your gift"). Gerar já em CAIXA ALTA: o `text-transform` não vale na cópia VML do Outlook.
- O texto que aparece nos cards de vidro, se houver, **não é gerado por esta ficha**, porque hoje está congelado dentro do ativo (ver decisão 1).

## Design system

**Incompleto.** Os valores abaixo saem do código e do render (Chromium, fallback Arial), não de uma referência preenchida.

| Elemento | Valor (do HTML) |
|---|---|
| Container | 600px, fundo `#FFFFFF`, sem borda |
| Família | `'Helvetica Neue', Helvetica, Arial, sans-serif` (uma família só) |
| Headline | 33/40, 700, itálico, `#000000`, centralizada, padding 33 topo / 85 laterais (miolo de 430px) |
| Sublinha | 25/30, 400, itálico, `#000000`, padding 0 / 85 laterais |
| Composição | 600×850, começa em y=103 da seção |
| CTA | 355×57, `#000000`, raio 4 (VML `arcsize="7%"`), centralizado (x 123–478) |
| Label CTA | 18px, 700, caixa alta, `#FFFFFF` |
| Posição CTA | 731px do topo da composição, 62px da base |
| Acento | nenhum: peça em preto e branco, a cor vem da fotografia |

*Pendente da referência:* cor e opacidade do vidro, raio dos cards, tipografia dentro dos cards e se a headline é de fato itálica na peça original.

## Direção fotográfica

**Incompleto — pendente da referência.** O que dá para fixar pelo código:

- A faixa inferior da composição (y 731–850 em 1x) fica atrás de um botão preto. Ela precisa ser clara e sem detalhe na área x 123–478, senão o CTA perde contorno.
- O topo da composição encosta direto na sublinha, sem padding. O primeiro elemento da imagem deve ter margem própria, ou a sublinha parece sentada na foto.
- Número de fotos, enquadramento, luz e posição dos cards: aguardando o PNG.

---

# O que veio da ficha e ainda não virou campo

Material da ficha de origem que **não** foi traduzido para eixo nenhum. Está aqui como matéria-prima do julgamento que falta, não como decisão — traduzir "Aspiracional" para `registro` ou "Campanha sazonal" para `momento` é exatamente o julgamento que esta nota não tem.

- **Categoria declarada na ficha:** "Navegação por ocasião (a confirmar)".
- **Objetivos compatíveis:** Descoberta de catálogo · Campanha sazonal ou de presentes · Aquecimento antes da oferta · Reengajamento.
- **Tons compatíveis:** Aspiracional · Editorial · Celebratório · Sofisticado.

## Schema de output de texto (da ficha, não do banco)

| Nome do schema | Tipo | Limite | Exemplo |
|---|---|---|---|
| GLASS_TITLE | texto | 24 | não extraível (placeholder "TEXT HERE") |
| GLASS_SUBTITLE | texto | 38 | não extraível (placeholder "TEXT HERE") |
| GLASS_CTA_LABEL | texto | 24 | SHOP FOR ANY OCCASION |
| GLASS_CTA_URL | url | — | não extraível |
| GLASS_COMPOSITION_ALT | texto | 90 | não extraível |

Os limites foram calculados em Arial, o fallback no Windows e o pior caso: headline a 16,6px/char em 430px, sublinha a 10,8px/char em 430px e label a 11,3px/char em 355px com 30px de folga por lado. A margem é de cerca de 7% para Helvetica Neue.

`schema_campos: 0` no frontmatter **não** contradiz esta tabela: o campo conta o schema que o banco expõe ao passo de copy do pipeline, e não há linha no banco. Sem ela, o passo de copy não tem endereço para escrever — a mesma condição de [[cinco-variantes-sem-schema]].

## Schema de output de imagem

| Campo | Valor |
|---|---|
| Nome | GLASS_COMPOSITION_IMAGE |
| Slot exibido | 600×850 |
| Entrega | 1200×1700 (2x) |
| Proporção de geração | 2:3, em 1200×1800 |
| Corte | 100px **do topo**, vertical. A exceção à regra de corte lateral está explicada na decisão 3 |
| Zona reservada | base de 238px (2x), área x 246–956 livre para o CTA |
| Fallback | `background-color:#FFFFFF` (hoje) |

*Provisório até a decisão 1:* se a composição for montada a partir de N fotos, este slot vira N slots, cada um com proporção própria.

# Decisões a confirmar (da ficha de origem)

**1. Quem monta a composição achatada?** Esta é a decisão que define a variante. Um gerador de imagem não entrega cards de vidro consistentes, e muito menos texto legível dentro deles. Sobram dois caminhos: **(a)** o pipeline gera as fotos separadas e um passo programático compõe os cards por cima; **(b)** a composição é um ativo fixo por loja, feito à mão. Nos dois casos, qualquer rótulo dentro dos cards (o nome da ocasião, por exemplo) fica congelado: a IA não edita, não traduz, e o leitor não vê com imagens desligadas.

**2. Com imagens desligadas, sobram 731px de branco.** O CTA está em cima de um `background-image`. Com imagens desligadas (Outlook corporativo, por padrão) ou no app do Gmail com conta não-Google, o leitor vê o título, 731px vazios e o botão solto. E fundo não tem `alt`. Sugestão: fatiar a composição em `<img>` 600×731 com alt e deixar só a faixa de 600×119 como fundo da linha do CTA. O visual fica igual e o vazio cai de 731 para 119px. É o mesmo risco que [[incentivo-precisa-existir-em-texto]] registra para o incentivo.

**3. A proporção 12:17 não está na lista.** Nenhuma razão retrato da lista (2:3, 9:16) é mais larga que 600:850, então o corte lateral é impossível. Propus 2:3 com corte vertical no topo, porque a zona de descanso fica na base. Confirmar se vale a exceção, ou se a composição muda para 600×900 (2:3 exato, sem corte).

**4. O label do CTA está fixo e duplicado.** A cópia VML tem `SHOP FOR ANY OCCASION` escrito à mão, e a cópia HTML tem `Shop for any occasion` com `text-transform`. As duas precisam receber a mesma tag `{{GLASS_CTA_LABEL}}`. A fonte do VML também está em Arial, contra Helvetica Neue no resto.

**5. Há placeholders fora do vocabulário canônico.** São `URL_DA_COMPOSICAO`, `URL_DO_CTA_AQUI`, `TEXTO_DE_PREHEADER_AQUI`, além dos dois `TEXT HERE`, que nem são tags.

**6. O preheader está dentro da seção.** O preheader é do e-mail, não do bloco. Um e-mail montado com cinco seções assim sai com cinco `div`s de preheader, e só o primeiro aparece. Ele deve ficar no template base.

**7. O prefixo `GLASS_` é provisório.** Precisa ser conferido contra o `email-reference-tags.md`.

**O que está certo:** a soma 731 + 57 + 62 bate exata com os 850 do fundo, o VML `v:rect` usa as mesmas dimensões, `arcsize="7%"` corresponde aos 4px de raio e o CTA está centralizado. E, pela primeira vez, sem o `border:1px solid #000000` no container.

---

HTML: **não existe no vault** — [[html-das-44-variantes-nunca-gerado]] · Seção: [[_body]] · Protocolo: [[_protocolo-de-selecao]] · Lacuna: [[cards-de-vidro-sem-referencia-e-sem-banco]]



# Auditoria de legado

- **Verificado em:** 2026-09-24.
- **Dispositivo histórico:** `dispositivo: catalogo_por_ocasiao`.
- **Situação no banco:** Não possui `variant_id`. O conteúdo e a descrição coincidem com [[body-8-cards-vidro]], que está ativa no banco como `body 8 - cards vidro`.
- **Decisão:** Manter apenas como fonte histórica incompleta. Não reativar nem cadastrar separadamente sem uma referência visual nova que prove diferença real.
- **Elegibilidade:** continua `legado: true`, `ativa: false` e `status: legado`.
