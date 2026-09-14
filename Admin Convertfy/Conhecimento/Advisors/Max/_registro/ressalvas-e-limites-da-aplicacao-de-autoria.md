---
tipo: registro-de-aplicacao
assunto: aplicacao-do-laudo-de-autoria
autor: max-sturtevant
status: aprovado
---

Os três casos em que o laudo [[mapa-da-autoria]] e a âncora real do corpo discordaram na aplicação, a confirmação por amostragem das pastas declaradas limpas, e o que a unidade de aplicação deliberadamente **não** fez. Em nenhum dos três casos a discordância inverte a conclusão do laudo. As tabelas nota a nota estão em [[mapa-da-aplicacao-de-autoria]].

# Onde o laudo e a âncora real discordaram

Três casos. Em nenhum deles a discordância inverte a conclusão do laudo — todas
são notas que o laudo classificou como **não afetadas** e que, pela âncora do
corpo, têm exposição pontual.

### 1. `copy/principio-engaging` — o laudo diz que escapa; a âncora diz que não

O laudo (§6.1) lista as notas de `copy/` afetadas e conclui: "Escapam
`o-que-evitar`, `principio-clear-e-conciso` e `principio-engaging`, que saem do
deck." A nota **de fato sai do deck** — mas cita, como reforço do argumento sobre
repetição, a frase **L6219** ("people are so accustomed to seeing the same thing
over and over and over and over"), que é fala dentro de L6101-6248,
`outro-provavel`.

**Resolvido a favor da âncora:** `registro: [slide, outro-narrador]`, aviso
mínimo, uma frase marcada. O corpo doutrinário da nota não muda.

### 2. `flows/sunset` — o laudo lista `winback`, não `sunset`

O laudo (§6.1) diz "`flows/` — 1 de 12 notas. Só `winback` (L5057, dentro de
Segmentation)". Mas `flows/sunset` traz **L5127 dentro do próprio `fonte:`** e
cita L5127 e L5129 no corpo, ambas dentro de L4846-5154 (`outro-provavel`), com
atribuição direta ("ele promete").

**Resolvido a favor da âncora**, com o mesmo tratamento pontual de `winback`.

### 3. Três notas em pastas declaradas limpas — **não tocadas, por instrução**

A varredura de âncoras encontrou citações de faixa não-Max em três notas de
pastas que o laudo declara limpas e que esta unidade foi instruída a não alterar.
**Nenhuma foi modificada.** Ficam registradas para quem for revisar o laudo:

| Nota | Linha citada | Faixa | Como a nota a usa |
|---|---|---|---|
| `design/emails-baseados-em-imagem` | L8500, L8504 | L8381-8646, `outro-provavel` | citação longa em blockquote sobre HTML e deliverability, dentro do conflito `design-html-vs-imagem` |
| `fundamentos/metricas-nucleo` | L6229 | L6101-6248, `outro-provavel` | "10%, maybe 15" usado como contraponto quantitativo a L180 |
| `sms/frequencia` | L4242 | L4202-4421, `outro-provavel` | "sweet spot de 2-4x" citado como referência cruzada ao módulo de campanhas |

O laudo está correto no que afirma — nenhuma dessas pastas **deriva** de faixa
não-Max. A divergência é de referência cruzada: as notas importam uma frase de
fora. Se o critério for "nenhuma frase de faixa não-Max sem marca", as três
precisam de uma linha; se for "nenhuma nota derivada de faixa não-Max", o laudo
está certo e não há o que fazer.

### Confirmação por amostragem das pastas limpas

`design/`, `fundamentos/`, `list-growth/` e `sms/` foram varridas por âncora
(todas as ocorrências `L####` de todas as notas, classificadas contra as faixas do
laudo). Resultado: **`list-growth/` está limpa; `design/`, `fundamentos/` e
`sms/` têm exatamente as três referências cruzadas da tabela acima e nada mais.**
Nenhuma dessas notas tem `fonte:` em faixa não-Max.

---

# O que esta unidade deliberadamente não fez

- **Não apagou conhecimento.** Nenhuma afirmação, número, verbatim ou racional
  saiu de nota nenhuma. Só mudou a atribuição.
- **Não mexeu em `_numeros`, `_conflitos` nem `_cobertura`.** A consequência de
  §6.2 (a frequência de campanhas muda de dono) está registrada no aviso de
  `campanhas/frequencia-de-envio` e no `_index` da pasta; propagá-la para as notas
  de controle é trabalho de outra unidade.
- **Não tocou em `design/`, `fundamentos/`, `list-growth/` e `sms/`**, por
  instrução — ver o caso 3 acima.
- **Não reescreveu a entrada de conflito de doutrina** (hoje em
  [[conflitos-de-doutrina]]), só marcou a parte superada.
