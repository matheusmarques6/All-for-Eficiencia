---
tipo: requisito
familia: catalogo
classe: gate
fonte_resolucao: pesquisa
default_quando_desconhecido: false
valor: manifesto-de-marca-escrito
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

# Como se resolve
Resolvedor (código, com citação): pesquisa da marca → trecho literal de
manifesto/missão citável. Sem trecho citado, `false` → elimina.