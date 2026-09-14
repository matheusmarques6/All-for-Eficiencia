---
tipo: padrao
assunto: como-escrever-nota
autor: convertfy
status: padrao
---

Este é o molde de toda nota que entra na base de conhecimento da ConvertIA. Ele não está com `status: aprovado` de propósito: é instrução para quem escreve, não conhecimento para a IA responder. O sincronizador ignora esta nota, e é isso que queremos.

# Por que existe um molde

A IA não lê o vault inteiro. Ela lê três coisas, com capacidades muito diferentes:

| Canal | Tamanho | Entra quando |
|---|---|---|
| Persona do advisor | 18.000 chars | sempre, em toda resposta |
| Catálogo de títulos | 400 notas, só os títulos | sempre |
| Corpo das notas | 12.000 chars por leitura | só se a IA buscar e abrir |

Numa conversa típica ela abre 2 a 4 notas. O que decide se a sua nota é uma delas não é a qualidade do texto — é o **nome do arquivo** e a **primeira frase**. Todo o resto do molde deriva disso.

# As seis regras que fazem uma nota existir

**1. `status: aprovado` ou a nota não existe.** Sem isso ela é pulada em silêncio, sem erro em lugar nenhum. Também valem `aprovada`, `approved`, `publicado`, `published`. Qualquer outro valor — ou nenhum — e a nota fica invisível. Use isso a seu favor: escreva com `status: rascunho` enquanto não estiver pronta.

**2. O título vem do NOME DO ARQUIVO, não do `# H1`.** `secao-hero.md` vira "Secao hero" no catálogo. O `# H1` lá dentro é decoração. Para forçar outro título, use `title:` no frontmatter — ele vence.

**3. O nome precisa se explicar fora da pasta.** O catálogo agrupa por pasta, mas a busca semântica compara o texto todo. `o-que-e.md` dentro de `deliverability/` faz sentido para você e nenhum para a busca. `o-que-e-deliverability.md` faz para os dois. Teste: leia só o nome do arquivo, sem a pasta. Ainda dá para saber do que trata?

**4. A primeira frase é a vitrine, e ela tem 320 caracteres.** O resumo de busca é gerado da primeira **prosa** do corpo, e ele descarta títulos, código, tabelas e imagens. Uma nota que abre com uma tabela ou um bloco de HTML produz resumo lixo — e a IA escolhe o que abrir pelo resumo. Então: **abra sempre com uma frase corrida que se explique sozinha**, antes de qualquer `#`. Ela deve dizer do que a nota trata para alguém que não sabe onde ela está.

**5. Máximo ~10.000 caracteres.** A leitura corta em 12.000 com um aviso "(truncado)" e a IA conclui a partir do pedaço que recebeu. Passou disso, quebre por **assunto** — nunca por tamanho. Metade de um argumento em cada nota é pior que a nota truncada, porque as duas metades passam a ser encontradas separadamente e nenhuma se sustenta.

**6. Mínimo ~1.500 caracteres.** Abaixo disso a nota ocupa uma linha do catálogo e não sustenta uma resposta. Vire seção de uma nota existente.

# Frontmatter

Obrigatório:

```
---
tipo: <principio|especificacao|procedimento|artefato|indice|registro|referencia|pesquisa|decisao|anti-exemplo>
assunto: <slug-do-assunto>
autor: <convertfy|max-sturtevant|nome-da-fonte>
status: aprovado
---
```

Opcionais, quando fizerem sentido:

- `fonte:` — de onde veio, com precisão de localizar de novo (URL, arquivo + linha, data da captura)
- `modulo:` — a pasta lógica, quando a nota pertence a um módulo
- `validade:` — para nota datada que envelhece (preço, print de interface, tutorial de ferramenta)
- `conflitos:` — slugs de conflito conhecidos que esta nota toca

# A estrutura do corpo

```
<frase de abertura em prosa, auto-explicativa, sem título antes>

# <primeiro assunto>
...

# <segundo assunto>
...
```

Wikilinks resolvem por **nome de arquivo**, como no Obsidian — nunca por caminho. Consequência prática que vale ouro: **mover uma nota de pasta é seguro, renomear quebra.**

# O que evitar

- **Nome genérico.** `frequencia.md`, `glossario.md`, `o-que-e.md` — perdem na busca e no catálogo.
- **`parte-1` / `parte-2`.** Não é nome de assunto. `conflitos-frequencia-de-envio` é.
- **`_index.md` e `readme.md`.** São descartados pelo sincronizador. Mapa de pasta chama-se `mapa-do-<assunto>.md`.
- **Abrir com título, tabela ou código.** Mata o resumo de busca.
- **Escrever mais doutrina.** Já há mais de 1 MB dela no corpus do Max. O que falta é execução: o que a casa decidiu, o que rejeitou, e com que número.
