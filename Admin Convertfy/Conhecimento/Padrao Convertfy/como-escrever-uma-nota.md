---
tipo: procedimento
modulo: padrao-convertfy
assunto: formato-de-nota
autor: convertfy
status: aprovado
---

# O que é

Como escrever uma nota que a ConvertIA realmente encontra e usa. Quatro
restrições do sincronizador decidem isso, e nenhuma é óbvia olhando para
o Obsidian: uma nota pode estar perfeita na tela e ser invisível na
base. As quatro foram medidas no código, não supostas.

# 1. A primeira frase é o que a busca mostra

A busca não devolve a nota. Devolve `path`, `titulo`, `pasta`, `tags` e
um **resumo de 320 caracteres** gerado a partir do corpo — e esse resumo
**descarta blocos de código, títulos (`#`) e imagens** antes de cortar.

O efeito, medido: uma nota que abre com o HTML da peça produz o resumo
"O primeiro passo pede só o e-mail." A mesma nota com uma frase de
abertura descritiva produz "Popup de duas etapas para captura de e-mail
em loja de moda: a primeira pede só o endereço…".

O modelo escolhe o que ler por esse resumo. Nota que abre com código
existe na base e nunca é aberta.

**Regra**: a primeira frase de prosa diz o que a nota é, para quem e em
que situação — sozinha, sem depender do título. Ela é o resumo.

# 2. O corpo é lido até 12.000 caracteres

`conhecimento_ler` corta em 12k e avisa "(truncado)". Doze notas do
corpus do Max já passam disso e chegam cortadas ao modelo.

**Regra**: uma nota, um assunto. Passou de 12k, quebre em duas e ligue
com wikilink — o grafo existe para isso.

# 3. O título é o nome do arquivo

`secao-hero.md` vira "Secao hero". O `# H1` do corpo é conteúdo, não
título — preferir o H1 já produziu um catálogo com vinte notas chamadas
"Aviso de autoria". Acento se perde no slug; quem quer nome exato põe
`title:` no frontmatter, que vence.

**Regra**: o nome do arquivo é a frase de busca. `popup-captura-duas-etapas`
encontra; `nota-3` não.

# 4. Sem `status: aprovado`, a nota não existe

O sincronizador só traz nota aprovada (aceita `aprovada`/`approved`/
`publicado`). Sem a linha, ela é ignorada em silêncio — nenhum erro, e o
painel de saúde conta uma nota a menos sem dizer qual.

**Regra**: frontmatter mínimo é `tipo`, `modulo`, `assunto`, `autor`,
`status: aprovado`.

# Esqueleto

```
---
tipo: peca | direcao | procedimento | especificacao
modulo: padrao-convertfy
assunto: slug-do-assunto
autor: convertfy
status: aprovado
---

# O que é

(Uma frase que diz assunto, público e situação. É o resumo da busca.)

# (o conteúdo)

# Quando não usar

(O limite. Nota sem limite vira regra universal na cabeça do modelo.)
```

# Uma nota que ninguém lê é pior que nota nenhuma

Ela ocupa espaço na busca por palavras e empurra para baixo a que
responderia. Antes de escrever mais, vale medir se a que existe é
encontrada — o card *ConvertIA · Saúde* mostra as lacunas: as buscas que
voltaram vazias, ordenadas por frequência. É a pauta do que escrever,
vinda de quem perguntou.
