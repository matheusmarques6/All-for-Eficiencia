# Brief de construção — leia antes de escrever qualquer nota

Arquivo temporário. Será apagado ao fim da construção.

## Contexto

Estamos convertendo `CONTEUDO BRUTO/max.md` (9.544 linhas, curso de email
marketing de Max Sturtevant / Well Copy) num corpus de notas atômicas em
`Advisors/Max/`.

Leia primeiro, obrigatoriamente:
- `Advisors/Max/_INDEX.md` — convenções, tipos, precedência de registro
- `Advisors/Max/_protocolo.md` — as regras invioláveis
- `Advisors/Max/_arquitetura.md` — por que o corpus é assim

## O corpus tem dois registros e eles discordam

Cada módulo do curso aparece duas vezes:
- **transcrição falada** — julgamento, exceção, o porquê, a voz, os exemplos
- **slide (GAMMA)** — número de tabela, template, código, checklist

Precedência: slide vence em **especificação**; fala vence em **julgamento**.
Quando discordam sobre especificação, NÃO escolha — registre nos dois lugares
(a nota e o staging de conflitos).

## Regras de escrita

1. **Prosa em português. Artefato verbatim em inglês.** Subject lines,
   templates de copy, sintaxe Klaviyo, definições de segmento, nomes de
   trigger: nunca traduzir. Termos técnicos (welcome flow, browse abandon,
   deliverability, hero section) ficam em inglês dentro da prosa portuguesa.
2. **Nunca invente.** Nenhum número, prazo, passo ou opinião que não esteja no
   bruto. Se falta, escreva que falta.
3. **Nunca faça média.** Se o corpus dá 3, 4-5, 6 e 15, os quatro aparecem.
4. **Toda afirmação rastreável.** Cite a linha: `(L1436)` ou `(L3492-3498)`.
5. **Célula vazia é informação.** Se um flow não tem delay declarado, a tabela
   fica vazia com nota dizendo que o corpus não informa. Nunca preencher por
   analogia com outro flow.
6. **Descarte é declarado.** Ruído de transcrição, CTA comercial, placeholder
   morto: não entram nas notas, mas você lista no staging o que descartou.
7. **Isolamento.** Nunca referencie `Admin Convertfy/Emails/`. É outra
   doutrina, de outro autor. Zero wikilink para lá.
8. **Voz.** As notas descrevem o que Max diz — não imitam o Max. A imitação
   fica só em `persona.md`, que outra unidade vai escrever.

## Frontmatter obrigatório

```yaml
---
tipo: principio | especificacao | artefato | procedimento
modulo: <nome da pasta>
assunto: <slug curto>
autor: max-sturtevant
registro: [transcricao, slide]      # ou [transcricao] / [slide] / [outro-narrador]
fonte: "CONTEUDO BRUTO/max.md — L1309-2324 (transcrição), L3467-3606 (slide)"
conflitos: [slug-do-conflito]        # só quando houver; senão omitir
status: rascunho
---
```

`registro: outro-narrador` existe porque há pelo menos dois narradores no
material (L5753 fala de Max em terceira pessoa). Use quando a voz não for a
dele.

## Tamanho e forma das notas

- Alvo: **2 a 3,5 KB por nota** (~700 tokens). Se passar de 4 KB, quebre.
- Nome do arquivo: kebab-case descritivo, sem numeração
  (`welcome.md`, `warming-do-dominio.md`, `principio-skimmable.md`).
- Estrutura de corpo livre, mas quase toda nota se beneficia de:
  `# O que é` · `# A regra` / `# A especificação` · `# O racional dele` ·
  `# Onde o corpus discorda` · `# O que o corpus não diz`
- Artefatos vão em blockquote, em inglês, marcados como verbatim.

## O que cada unidade entrega

1. As notas da pasta.
2. `<pasta>/_index.md` — mapa local. Uma linha por nota, mais a tabela
   comparativa do domínio quando fizer sentido (ex.: em `flows/`, a tabela
   gatilho × nº de emails × delays × filtros dos 8 flows, com célula vazia
   onde o corpus é omisso).
3. `_staging/numeros-<modulo>.md` — todo número do módulo, formato:
   `| Medida | Valor verbatim | registro | linha | slug-do-conflito ou — |`
4. `_staging/conflitos-<modulo>.md` — toda contradição, formato:
   `## <modulo>-<assunto-curto>` + tabela de versões (valor, registro, linha)
   + parágrafo `**Como responder:**`
5. `_staging/descartes-<modulo>.md` — linhas ignoradas e o motivo
   (ruído de ASR, CTA comercial, placeholder sem imagem, título que mente).

Os slugs de conflito seguem `<modulo>-<assunto-curto>`, ex.:
`welcome-contagem-de-emails`, `deliverability-limiar-de-open-rate`.

## Como trabalhar

Leia a faixa de linhas INTEIRA com `sed -n 'X,Yp'` em blocos de ~350 linhas
antes de escrever qualquer nota. Não escreva a partir de memória ou de
resumo — escreva a partir do texto.
