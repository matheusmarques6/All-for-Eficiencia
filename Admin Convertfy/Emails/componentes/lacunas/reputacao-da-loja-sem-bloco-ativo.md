---
tipo: lacuna
sobre: biblioteca
secao: body
descoberta_em: 2026-09-09
status: aberta
---

Não existe no catálogo nenhum bloco ativo que realize o aliviador
`reputacao_da_loja` — garantias, selos ou política de troca com `objecao:
[confianca-no-canal]` no meio da peça — e a telemetria do welcome-1 já
pediu esse bloco em 4 de 4 runs sem que nenhuma posição o entregasse.

# O que falta

Um bloco de `body` que responda "nunca ouvi falar dessa marca, o site
parece pequeno" — o risco `seguranca` — com compromisso, não com
argumento: faixa de garantias (entrega, devolução, um compromisso
específico da marca), selos (pagamento seguro, tempo de mercado) ou a
política publicada, declarando `objecao: [confianca-no-canal]`,
`papel_na_peca: [meio]` e `momento` que inclua `welcome-1`. Hoje não há.

O que a telemetria mediu (briefing de 2026-09-09, T3): em 4 de 4 runs
recentes do welcome-1, o alvo do Seletor pediu o aliviador
`reputacao_da_loja` para o risco `seguranca`, e nenhuma posição da peça
montada o realiza. O contrato tipado de `intencoes/welcome/welcome-1.md`
permite exatamente esse pedido: `riscos_elegiveis` inclui `seguranca`,
`aliviadores_admissiveis: [todos]` inclui `reputacao_da_loja`, e
`remocao_de_risco` é um dos `trabalhos_fixos` — a prosa da intenção exige
que, ao terminar de ler, a pessoa "sabe que errar a compra não custa (o
risco foi removido)".

O que o catálogo tem, conferido em [[_catalogo]] e nas notas: entre as 44
variantes, **uma** declara `confianca-no-canal` —
[[body-5-comparacao-nos-vs-eles]] (`objecao: [confianca-no-canal,
preco-valor]`, `papel_na_peca: [meio, fecha]`) — e está `ativa: false`.
[[_body]] registra o mesmo ("única variante do catálogo inteiro (44) que
serve a objeção `confianca-no-canal` — e está inativa"). E mesmo reativada
ela não serviria o toque 1: é uma tabela de comparação, `exige:
[quatro-criterios-objetivos]`, com `momento: [welcome-meio,
welcome-tardio, carrinho-abandonado, browse-abandonment]` — lista não
vazia sem `welcome-1`, eliminada no passo 5 do [[_protocolo-de-selecao]].
O dispositivo que falta é outro: reasseguro, não comparação.

Os vizinhos mais próximos não são o bloco: [[body-3-pitch-de-gift-card]]
fecha com "faixa de 3 selos circulares com valores da marca", mas é pitch
de vale-presente (`exige: [gift-card-digital]`, `objecao: []`, momento
`gift-card`/`sazonal-data-comemorativa`) e os selos são valores, não
garantias; [[offer-5-tres-diferenciais-e-cupom]] cobre "o risco
(garantia, devolução)" como um de três diferenciais, mas é `momento:
[welcome-meio]`, `objecao: [preco-valor]` e `exige: [cupom-ativo,
tres-diferenciais-concretos]`. Os requisitos que o bloco novo pediria
também não existem: dos 52 em `requisitos/` (tabela de
[[_parametros-da-loja]]), nenhum cobre garantia de devolução, política de
troca publicada ou selo de segurança — só `selo-compra-verificada` e
`canto-livre-para-selo` falam de selo.

# Por que importa

A estrutura de referência do toque 1, [[avelmore-inspecao-antecipada]],
pede este bloco por nome — posição 4: "faixa de garantias em 3 ícones
(fundo contrastante). Remoção de risco: entrega, devolução e um
compromisso específico da marca que responde à MESMA objeção da tese" — e
o lista em "Exige da loja: garantias reais de entrega/devolução". O mesmo
dispositivo volta em [[avelmore-prova-social-cirurgica]] (toque 4: "os
mesmos 3 ícones do #1") e em [[medicube-escassez-com-prova-de-demanda]]
(toque 6: "os 3 ícones de garantia" como última reassurance antes do
clique). Três das oito estruturas do welcome usam a faixa; o catálogo não
tem uma. [[_casos-de-teste]] já rodou o Caso A com "body (dois blocos —
tese+incentivo e garantias em 3 ícones)" e terminou em zero elegíveis
(achado 3), anotando que "seria candidata a uma nota nova em `lacunas/`".
Esta é a nota.

O buraco não é só do toque 1. [[welcome-5-sem-variante-ativa]] registra o
mesmo zero para a objeção do canal no toque 5 — e o contrato de
[[welcome-5]] lista `reputacao_da_loja` explicitamente em
`aliviadores_admissiveis`, com `seguranca` em `riscos_elegiveis`. Onde a
objeção dominante é a loja e não o produto, os dois caminhos que o vault
conhece — comparar contra a categoria (body-5) ou garantir (a faixa que
não existe) — terminam no template global. A própria
`avelmore-inspecao-antecipada` diz "não usar quando a objeção dominante é
da LOJA/canal — a comparação serve melhor" e aponta para
[[medicube-comparacao-categoria]], cuja única variante está inativa.

# O que se perde hoje

Em toda run do welcome-1 em que o Seletor escolhe `seguranca` como risco
— loja desconhecida, site pequeno — o Curador não tem candidata: ou o
slot cai no template global sem que a lacuna seja nomeada, ou a posição
é preenchida por um bloco que não realiza o aliviador pedido; a telemetria
diz que o segundo aconteceu 4 de 4 vezes. O e-mail entrega o incentivo e
a tese, mas o "risco foi removido" da intenção não acontece em lugar
nenhum, e [[remocao-de-risco-escala-com-o-ticket]] deixa de ter onde
aplicar — em ticket médio-alto a garantia deveria subir para antes do
preço, e não há bloco para subir. Enquanto esta nota não existia, o
contador `aliviador_ausente` rodava sem lacuna registrada (briefing,
§4.3); a partir dela o Curador tem o que declarar.

# Fora do escopo desta entrega

Construir ou comprar a variante (HTML novo, `variant_id` e
`schema_campos` no banco), criar os requisitos que ela exigiria
(garantias reais de entrega/devolução, política publicada, selo de
segurança) e decidir a reativação de `body-5` — esta última já em aberto
em [[welcome-5-sem-variante-ativa]]. Registrado para a decisão não se
perder.
