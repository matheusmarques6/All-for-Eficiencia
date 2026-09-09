---
tipo: indice
assunto: aplicacao-do-laudo-de-autoria
autor: max-sturtevant
status: aprovado
---

Registro de execução da aplicação do laudo de autoria [[_autoria]] às notas do corpus: o que a unidade mudou, como a exposição a faixa não-Max foi apurada âncora por âncora, e onde está a tabela nota a nota de cada pasta afetada. Nenhum conhecimento foi apagado — só mudou quem pode ser citado como autor.

# O que esta unidade fez

Aplicou [[_autoria]] às notas. O laudo estabelece **quem fala**; esta unidade
mudou `registro:`, a prosa de atribuição e os `_index.md` para que a saída do
advisor nunca cite como fala de Max o que não é.

**Nenhum conhecimento foi apagado.** Só mudou quem pode ser citado como autor.

## Como a exposição foi apurada

Não pelo laudo direto. Para cada nota: `fonte:` do frontmatter + **toda** âncora
`L####` do corpo, conferidas contra a estrutura do bruto com
`grep -n -E "^(# |Transcrição do Vídeo|\# File-)"`.

Isso revelou uma distinção que as faixas do laudo não separam e que decidiu vários
casos: **dentro de cada faixa de vídeo há um cabeçalho de bullets escritos** (do
mesmo doc GAMMA), antes do marcador `Transcrição do Vídeo :`. Esses bullets são
artefato escrito, não fala. As faixas de fala reais:

| Bloco | Bullets escritos | Fala |
|---|---|---|
| Campaign Strategy | L4189-4200 | **L4202-4421** |
| Campaign Calendar Creation | L4422-4440 | **L4444-4675** |
| Creating Great Campaigns | L4676-4683 | **L4686-4828** |
| Segmentation | L4829-4843 | **L4846-5154** |
| ChatGPT Copywriting | L5617-5664 (inclui o prompt L5627-5661) | **L5667-5866** |
| Utilizing Infographics | L5867-5885 | **L5888-6082** |
| Subject Lines & Preview Texts | L6083-6098 | **L6101-6248** |
| What is Deliverability? | L8365-8378 | **L8381-8517** |
| Warming Your Domain | L8518-8529 | **L8532-8646** |
| High Leverage A/B Tests | L8762-8770 | **L8773-9109** |

Consequência prática: `copy/principio-clear-e-conciso` (L5631, L5649) **não** tem
exposição — essas linhas caem dentro do prompt escrito, não na fala. Confere com
o laudo, que a lista como não afetada.

## Padrão do bloco `# Aviso de autoria`

Todo bloco traz, nesta ordem: **faixa** → **classificação com a certeza explícita**
→ **critério** → **o que na nota vem de onde**.

- `outro-provado` — "prova nominal, a única do corpus" (L5753), com a ressalva de
  ASR do §4.1.
- `outro-provavel` — "sem prova nominal, a classificação é estilométrica…
  `outro-provavel` não é `outro-provado`" (§7.3).

O critério citado é sempre **idioleto** (§2.1). Todo bloco diz explicitamente que
**a saudação de abertura não é critério e não pode ser citada como evidência**,
nomeando a contraprova (§5, L7603 + L7817).

---

# Onde está cada parte

A tabela nota a nota foi dividida por pasta afetada. Cada uma traz, por nota, a
exposição encontrada, o `registro:` antes → depois e o que mudou na prosa.

| Nota | O que traz |
|---|---|
| [[aplicacao-autoria-em-deliverability-e-otimizacao]] | `deliverability/` — 9 de 9 + índice; `otimizacao/` — 7 de 7 + índice |
| [[aplicacao-autoria-em-campanhas-e-copy]] | `campanhas/` — 8 de 9 + índice; `copy/` — 6 de 9 (o laudo dizia 5 + 1) + índice |
| [[aplicacao-autoria-em-doutrina-e-flows]] | `doutrina/` — 8 de 13 (+ 1 aviso anulado) + índice; `flows/` — 2 notas (fora das cinco pastas do escopo); a entrada de conflito de doutrina |
| [[ressalvas-e-limites-da-aplicacao-de-autoria]] | os três casos em que o laudo e a âncora real discordaram, a confirmação por amostragem das pastas limpas, e o que esta unidade deliberadamente **não** fez |
