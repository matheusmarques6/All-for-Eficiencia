---
tipo: componente
slug: hero-14-lockup-tipografico
variant_id: fea49994-d150-40fa-a8e9-513686563686
nome_no_banco: "hero section 14"
secao: hero
status: aprovada
fonte: catalogacao-2026-09-19
schema_campos: 7
product_slots: 0
objecao: [preco-valor]
aliviador: [dado_de_adequacao]
profundidade: afirmacao
registro: [bold-alto-contraste]
registro_vetado: [clinico-sobrio]
paleta: [com-acento-definido]
papel_na_peca: [abre]
convivencia: []
exige: [desconto-percentual]
aprendizados: [[[cupom-repetido-precisa-de-papel]]]
---

## Descrição curta
Transforma a oferta em tipografia monumental: o leitor lê o valor antes de qualquer frase, num lockup que ocupa um terço da peça — e NÃO recebe código, porque esta hero declara a oferta sem entregá-la. Obriga sobrescrito, palavra de reforço repetida, valor, sufixo, título de coleção, corpo e CTA — sem nenhuma imagem gerada: o lockup é tipografia HTML, o fundo é cor chapada e o logo é célula fixa.

## Descrição detalhada
Logo fixo no topo (célula do layout, sem campo), sobrescrito curto (`lockup_eyebrow`), lockup tipográfico que ocupa um terço da altura — a palavra de reforço repetida (`lockup_repeat_word`) emoldurando o valor (`lockup_value`) e o sufixo (`lockup_suffix`) — tudo em texto HTML, sem arte gerada —, seguido de título de coleção (`lockup_collection_title`), corpo (`lockup_body`) e CTA (`lockup_cta_label`), sobre fundo cinza chapado (sem slot de imagem). NÃO há campo de cupom: é a diferença estrutural para a [[hero-11-bogo-em-manchete]] (mesmo dispositivo, código em campo próprio). Das campanhas nomeadas (13, 15) difere por não citar data: a manchete é o valor, não a ocasião.

## Quando usar
Oferta declarada sem código: desconto automático aplicado no checkout, ou peça em que o código é entregue em outra posição (um offer de código abaixo — aí cada aparição da oferta tem papel próprio: manchete aqui, resgate lá). O valor precisa existir como desconto real e declarável em número; o lockup não funciona com "ofertas selecionadas".

## Quando não usar
Toque cujo trabalho fixo é ENTREGAR o incentivo ([[welcome-1]]) sem outro bloco de código na peça: esta hero não tem onde escrever o código, e o leitor que abriu para pegá-lo encontraria só a manchete — a promessa do opt-in ficaria sem resgate. Ali, ou entra a hero 11, ou esta vem acompanhada de um offer de entrega.

## Convivência
Se houver bloco de código abaixo, a manchete não repete o código (não tem slot) — a dupla funciona; dois lockups de valor na mesma peça, não. Tipografia display gigante não convive com segunda tipografia display na seção vizinha.

## Notas de cadastro
Descrição do banco bate com a anatomia (sem campo de cupom, confirmado nos 7 campos). Sem HTML para medir altura — `peso` omitido; ver relatório.

**Conserto de 19/09 (admin, auditor de âncoras)**: saíram `lockup_type_image`, `lockup_background_image` e `lockup_logo_image` (a variante não tem nenhum slot de imagem). 10 → 7 campos.
