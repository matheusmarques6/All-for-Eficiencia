---
tipo: indice
assunto: como-ler-o-registro-de-conflitos
autor: max-sturtevant
status: aprovado
---

O registro de conflitos do corpus Max é onde ficam documentadas as contradições internas do material, e esta nota explica para que ele serve e como ler uma entrada dele: a regra de ouro de nunca resolver conflito por média, a anatomia de cada entrada (tabela de versões verbatim mais o "Como responder"), a precedência entre slide e fala, e os quatro marcadores de tipo usados no índice — conflito, armadilha, lacuna e proveniência.

# Para que serve

Registro único de onde o corpus Max se contradiz. É o que impede o advisor de
responder com confiança falsa: se o assunto tem entrada aqui, não existe
resposta limpa, e a resposta certa mostra as duas versões.

O [[_protocolo]] manda checar esta nota no passo 4, **antes** de ler a nota do
assunto. Toda nota que carrega contradição declara o slug no frontmatter
`conflitos:`; os slugs vivem no índice abaixo.

**O [[mapa-dos-conflitos]] é a porta.** O registro contém o índice completo dos 126
slugs canônicos (mais os 18 redundantes e para onde apontam), repartido em
[[indice-de-conflitos-fundamentos-doutrina-list-growth-flows-campanhas]] e
[[indice-de-conflitos-copy-design-deliverability-otimizacao-sms]], e, na íntegra, as
duas seções transversais — os **conflitos entre módulos**
([[conflitos-entre-modulos-metas-e-open-rate]],
[[conflitos-entre-modulos-html-imagem-e-janela-de-atencao]],
[[conflitos-entre-modulos-onde-testar-frequencia-e-pontas-soltas]]) e os **conflitos
dentro do mesmo registro** ([[conflitos-no-mesmo-registro-metas-e-open-rate]],
[[conflitos-no-mesmo-registro-resumo-slide-contra-slide]],
[[conflitos-no-mesmo-registro-deliverability-unsubscribe-e-dns]],
[[conflitos-no-mesmo-registro-copy-design-e-otimizacao]]) —, que são as que mais mudam
resposta e as que o roteamento por pasta do [[_INDEX]] nunca entrega sozinho. **As outras 108 entradas estão em [[_conflitos-completo]]**, agrupadas por
módulo, com o mesmo cabeçalho `## slug`.

**A regra de busca é uma só:** ache o slug num dos dois índices; se o `## slug` não
estiver nas notas transversais listadas acima, ele está em [[_conflitos-completo]]. Não
existe slug fora dessas notas, e nenhuma entrada existe em duas delas.

**A regra de ouro: nenhum conflito é resolvido por média.** Se o corpus dá 3, 6
e 15, a resposta é "o piso é 3 e o critério é este" — nunca "cerca de 8". Média
inventada é indistinguível de conhecimento real e impossível de auditar depois.
Vale também para arredondamento, conversão e interpolação. Onde o corpus não
permite desempate, o "Como responder" diz isso com todas as letras.
# Como ler cada entrada

Cada entrada tem duas partes:

1. **Tabela de versões** — `valor verbatim` · `registro` · `linha`. O valor é
   copiado do bruto em inglês, sem tradução e sem normalização. O registro é
   `transcricao`, `slide` (deck GAMMA), `resumo do módulo` (bloco de bullets da
   página do curso, que não é nem fala nem deck) ou `outro-narrador`. A linha é
   de `CONTEUDO BRUTO/max.md`.
2. **`Como responder:`** — a posição mais sustentada e por quê, a outra versão
   com a linha, e o critério dele para decidir quando existe. O critério real
   quase nunca é numérico: é tipo de produto, tamanho de lista, faturamento.

**Precedência** ([[_INDEX]]): slide vence em especificação, fala vence em
julgamento. Ela só funciona **entre** registros. Boa parte dos conflitos deste
corpus é slide contra slide no mesmo deck — esses estão reunidos em
[[conflitos-no-mesmo-registro-resumo-slide-contra-slide]] e nas notas que ele aponta, e
a precedência não os resolve.

**Atribuição:** o laudo [[_autoria]] classifica dez blocos de fala como
`outro-provavel` ou `outro-provado`. Onde um lado do conflito cai num desses
blocos, a entrada avisa — porque isso muda o peso da versão, e às vezes decide.

Marcadores de tipo usados no índice:

| Marcador | Significa |
|---|---|
| `conflito` | duas ou mais versões incompatíveis, ou não reconciliadas pelo corpus |
| `armadilha` | **não é conflito** — o mesmo número mede coisas diferentes, e a leitura ingênua cria contradição que não existe |
| `lacuna` | o corpus promete e não entrega; a ausência é informação |
| `proveniência` | mesmo conteúdo em dois lugares; importa a origem, não o valor |
| `→ slug` | slug redundante; a entrada canônica é a apontada |
