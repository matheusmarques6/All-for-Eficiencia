---
tipo: procedimento
modulo: list-growth
assunto: montar-popup-no-klaviyo-desktop
autor: max-sturtevant
registro: [transcricao]
fonte: "CONTEUDO BRUTO/max.md — L826-858 (transcrição)"
conflitos: [list-growth-imagem-lateral, list-growth-popup-vs-full-page, list-growth-teaser]
status: aprovado
---

Como montar a versão desktop do pop-up de captura no Klaviyo clonando o form mobile já pronto: dimensão 1000x600, pop-up em vez de full page, X transparente, imagem à direita e compressão do arquivo.

> **PROCEDIMENTO DATADO.** Mesma ressalva de [[criar-form-no-klaviyo]]: é
> gravação de tela do Klaviyo, a interface muda. Os valores são a doutrina; os
> cliques, aproximação.

# O ponto de partida

Ele não monta do zero: clona o form mobile já pronto e converte (L828). Depois
troca targeting para **display on desktop only** (L830-832) e insere uma imagem
(L832). Pré-requisito, portanto, é ter feito [[criar-form-no-klaviyo]].

# A especificação

**Dimensão: 1000x600.** Ele passa por 800 e depois 600 antes de fechar em "The
perfect, 1000 x 600 looks to be a good amount" (L836-840). O corpus não diz qual
dos dois valores intermediários é largura e qual é altura.

**Tipo: pop-up, não full page.** O trade-off que ele declara: "usually the bigger
your form is the better converting, but you have to sacrifice some customer
experience because this is a little bit more bombarding. So I typically will do a
popup like this, but maybe make it a little bit bigger" (L834). Sobre a terceira
opção: flyouts "aren't as effective" (L836).

**X transparente também no desktop.** O template traz um X com borda; ele zera a
cor de fundo — "we like to make our X clear so that people don't know that they
can that there's an X here and instead they're forced to make a decision. Um,
highly recommend doing that. It's going to improve conversions" (L840).

**Imagem à direita.** Uma das poucas afirmações do módulo em que ele nomeia um
teste como origem: "We have actually tested this and right image typically works
best. You could also do left" — ou nenhuma imagem (L852-854). Contrasta com o
mobile, onde a imagem lateral quebra o layout (L712). As outras afirmações com
teste declarado são a da oferta ("I've tested this across multiple different
brands", L615), a do micro-commit contra o classic (L1007) e a da copy
(L1041) — em nenhuma delas ele dá número de amostra.

**Comprimir a imagem.** "you want to use a site like iloveimg.com... Or make it
smaller file so it doesn't load so slow when you load the form" (L856). É o que
sustenta o item *form loads instantly after delay with no lag* do
[[checklist-do-form]].

# O resto é igual ao mobile

Micro-commit, passo de email, passo de SMS e tela de sucesso seguem o mesmo
roteiro: "is the same exact thing as mobile, so we don't really need to change
too much. Um, maybe some formatting stuff, maybe some spacing" (L844); "very
similar to mobile. Um you just want to play around with your spacing, with your
words" (L858). O micro-commit se adiciona da mesma forma (L846-850).

**Bug que ele mesmo registra:** mexer no tamanho zerou a formatação — "for some
reason, that reset my formatting, so let's turn this back to 1,000" (L856).

# Onde o corpus discorda

- **Imagem lateral:** atrapalha no mobile (L712) × testada e melhor à direita no
  desktop (L852). Ver `list-growth-imagem-lateral`.
- **Tamanho:** o checklist pede ≥75% da tela (L1253) e aqui ele recusa full page
  em nome da experiência (L834). Ver `list-growth-popup-vs-full-page`.
- **Teaser:** ele não usa no mobile (L700) mas usa no desktop (L1073) — a
  distinção por dispositivo só aparece na aula 6, não aqui.

# O que o corpus não diz

Não dá delay, frequência de reexibição nem regra de disparo específicos para
desktop — a seção de targeting só é demonstrada no mobile (L818-822). Não diz que
imagem usar além de "I just put a main one from their site in" (L834). Não dá
peso máximo de arquivo depois da compressão.
