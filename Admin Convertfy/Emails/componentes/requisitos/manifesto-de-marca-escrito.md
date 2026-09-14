---
tipo: requisito
familia: catalogo
valor: manifesto-de-marca-escrito
verificavel_hoje: false
status: aprovada
procedencia: inventario
---

# O que é

A marca tem um manifesto ou discurso institucional já escrito e
aprovado — não é algo que a IA pode inventar do zero na hora de gerar
o e-mail.

# Por que é eliminatório e não preferência

A peça inteira É o manifesto: três parágrafos com funções fixas
(missão, ganho do cliente, detalhe e pessoa), sem slot de imagem, sem
oferta em destaque. Sem manifesto real por trás, esses três parágrafos
viram texto de preenchimento gerado na hora — e como não há mais nada
na peça, ela fica vazia por inteiro, não só naquele trecho.

Da prosa do inventário, verbatim (`offer 4`): *"Marca sem discurso
próprio. Sem manifesto real, os três parágrafos viram texto de
preenchimento e a peça fica vazia."*

# Como o agente verifica

**Não verifica automaticamente hoje**, mas o campo existe:
`client_stores.brand_thesis` e `brand_about` (texto livre,
`20260516000000_pesquisa_diagnostico.sql:7-8`) guardam a tese/sobre da
marca produzidas pela Pesquisa & Diagnóstico — presença de texto não
vazio já responde "a marca tem discurso institucional escrito". O que
falta não é o dado, é o Curador cruzar `exige` contra ele: hoje `exige`
nem entra no prompt do Curador (ver
[[o-que-o-curador-ainda-nao-tem]]). Ver [[_parametros-da-loja]].
