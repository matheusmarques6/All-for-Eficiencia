---
tipo: eixo
eixo: momento
valor: campanha-promocional
procedencia: inferida
status: aprovada
---

> Derivado por código de `flow_type` + `email_number` (`momentoDoEmail` em curador-vault.ts). Filtro do passo 5, não eixo de ranking; não é lido pelo LLM. Mudou o vocabulário, muda o mapa no mesmo commit.

# Campanha promocional

Disparo comercial pontual — não ligado a um evento comportamental do
assinante nem a calendário fixo. Existe para vender agora, geralmente em
torno de uma oferta com prazo. Difere de `sale-recorrente` por não ter
cadência esperada: é um evento único, não um ritmo que o assinante já
conhece.

# Como usar na seleção

Uma variante com `momento: [campanha-promocional]` deve deixar a oferta e o
prazo evidentes cedo — este não é o lugar para argumento longo de mecanismo
ou origem de marca, que cabe em nutrição ou no meio do welcome. A objeção
mais provável de resolver aqui é `disponibilidade-urgencia` ou `preco-valor`.

# Procedência

Esta distinção foi inferida, não extraída de doutrina existente do vault.
Utilizável, mas ainda não validada por quem opera as lojas.
