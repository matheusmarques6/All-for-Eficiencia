---
tipo: aprendizado
flow_type: welcome
origem_estrutura: avelmore-deadline-objecao
confirmado_em: [avelmore-mecanismo-e-origem, avelmore-prova-social-cirurgica]
status_evidencia: confirmada_e_refinada
autor: Convertfy
status: aprovada
---

# Observação

O deadline com hora explícita é a peça mais valiosa do welcome #2 e a mais
frágil. Se o cupom não expirar mesmo, o #3 nasce sem credibilidade — e essa perda
é permanente para aquele contato.

# Regra derivada

Prazo declarado no e-mail tem que ser prazo cumprido no ESP. Urgência não
honrada não custa um e-mail: custa o resto do flow.

# Confirmação observada

Previsto a partir do #2, confirmado no #3. O
[[avelmore-deadline-objecao|#2]] disse *"today, 11:59 p.m."*; o
[[avelmore-mecanismo-e-origem|#3]] chega com o mesmo WELCOME10 funcionando, sem
uma palavra sobre o prazo. O contato aprende que o deadline da marca é
decorativo.

Duas saídas coerentes: o #3 reconhece ("reativamos seu código") ou o #2 não fixa
hora. Do jeito que está, o #2 sabota o flow inteiro.

Terceira ocorrência no #4: [[avelmore-prova-social-cirurgica]] chega com o cupom
vivo e sem prazo pela terceira vez seguida. O padrão está consolidado — a hora do
#2 era decorativa, e o flow inteiro ensina isso ao contato.

# O flow aposta de novo no #6

[[medicube-escassez-com-prova-de-demanda|#6]] fixa um segundo prazo — *"expires at 11:59
PM today"* — depois de o primeiro (do #2) ter morrido em silêncio no #3.

A regra ganha direção temporal: **a credibilidade de um prazo não se decide no
e-mail que o anuncia, e sim no seguinte.** Se o #7 chegar com o código
funcionando, o #6 vira teatro retroativamente e o flow queima o segundo deadline.

Se o código expirou de verdade, #7 e #8 são obrigados a mudar de registro —
vender sem a alavanca que morreu. Ao fazer isso, provam que o prazo era real.

# Resolução da verificação (#7)

O #7 chegou e **não queimou o prazo — condicionalmente.** Ele repete a mesma
hora do #6 em vez de renovar prazo novo. Se a cadência for de horas, os dois são
a mesma batida do dia D e o prazo se sustenta; se for de dias, é o terceiro
deadline queimado.

A regra original vale, mas ganhou uma condição que não estava nela: **o que
queima um prazo não é o e-mail seguinte citá-lo de novo — é o tempo entre eles.**
Ver [[cadencia-decide-fechamento-ou-farsa]].

# Resolução final (#8)

**O prazo era real.** O [[carta-plain-text-extensao|#8]] prova isso pelo caminho
mais forte possível: em vez de fingir que o código nunca expirou, ele **admite
que expirou** e declara uma exceção nomeada e única.

A regra fecha em três camadas:

1. Prazo declarado tem que ser prazo cumprido. (lote 2, do #2)
2. O que queima um prazo não é citá-lo de novo — é o tempo entre os e-mails.
   (lote 7, do #7)
3. Um prazo cumprido **pode** ser estendido sem se destruir, desde que a exceção
   seja declarada. Ver [[extensao-declarada-quatro-condicoes]]. (lote 8, do #8)

O flow queimou o deadline do #2 (morto em silêncio no #3) e honrou o do #6/#7.
A diferença entre os dois casos é exatamente a declaração.

# Promoção

Esta regra foi promovida a doutrina do flow: [[_flow]], **regra transversal 4**.
A nota permanece como o registro da evidência que a produziu.
