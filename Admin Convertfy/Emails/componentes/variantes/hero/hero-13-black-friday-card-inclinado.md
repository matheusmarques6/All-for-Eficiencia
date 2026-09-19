---
tipo: componente
slug: hero-13-black-friday-card-inclinado
variant_id: bd4965fe-9606-49ca-bdbf-f260571acb3a
nome_no_banco: "hero section 13"
secao: hero
status: aprovada
fonte: catalogacao-2026-09-19
schema_campos: 8
product_slots: 0
objecao: [preco-valor]
aliviador: [dado_de_adequacao]
profundidade: afirmacao
registro: [festivo, bold-alto-contraste]
registro_vetado: [luxo, clinico-sobrio]
paleta: [escuro-saturado]
papel_na_peca: [abre]
peso: { altura_px: 1048, classe: medio, fonte: medido }
convivencia: []
exige: [cupom-ativo, motivo-sazonal]
aprendizados: [[[incentivo-precisa-existir-em-texto]], [[deadline-falso-queima-o-proximo]]]
---

## Descrição curta
Abre a peça gritando a data: o leitor reconhece a campanha (Black Friday) pelo card inclinado e pelas faixas diagonais antes de ler a oferta — e sai com o código na mão. Obriga oferta em três linhas, rótulo e código de cupom, CTA, nome da campanha e uma imagem de fundo. Card, faixas diagonais e logo são desenhados pelo próprio HTML.

## Descrição detalhada
Bloco de arte de 548px dentro do container de 600: logo fixo no topo (célula do layout, sem campo), um card escuro INCLINADO carregando a oferta em três linhas de texto real (`bf_offer_line_1`, `bf_offer_value`, `bf_offer_line_3`), faixa de cupom (`bf_coupon_label`, `bf_coupon_code`), CTA (`bf_cta_label`) e o nome da campanha (`bf_campaign_name`), sobre UMA imagem gerada, o fundo (`bf_background_image`); card e faixas diagonais são CSS do próprio bloco. Apontada em 15/09 como quase-duplicata da hero 15 POR DESCRIÇÃO; pela anatomia são distintas: esta tem card inclinado + faixas diagonais (8 campos); a [[hero-15-cyber-com-selo]] tem selo circular nomeando a data (8 campos) — a diferença é o ornamento que carrega a campanha.

## Quando usar
Campanha nomeada com cupom — Black Friday e datas da mesma família visual — quando existem as três coisas: o motivo sazonal real, o cupom ativo e a licença de registro para gritar. A oferta e o código são texto real fora da imagem: sobrevivem com imagens bloqueadas. Momento: campanha promocional/sazonal; não pertence à régua de welcome nem aos flows de abandono.

## Quando não usar
Fora da janela da data: faixas diagonais de Black Friday em fevereiro leem como erro de produção, não como estilo — o motivo sazonal é gate, não decoração. E não usar com sublinha ou copy de prazo sem prazo real: campanha nomeada carrega urgência implícita, e a data que passa sem a oferta acabar queima a próxima campanha.

## Convivência
Não empilhar com outra seção temática de campanha (segunda arte de BF, hero 15): uma moldura de campanha por peça. Abaixo dela, blocos neutros — a arte inclinada já gastou o orçamento de ruído visual da peça.

## Notas de cadastro
O 548px do cadastro é o bloco de arte, não necessariamente a seção completa — sem HTML para medir, `peso` omitido; ver relatório. Suspeita de duplicata com hero 15 verificada e descartada pela anatomia (campos diferentes, ornamento diferente). Descrição do banco bate com a anatomia.

**Conserto de 19/09 (admin, auditor de âncoras)**: saíram `bf_offer_card_image`, `bf_diagonal_stripes_image` e `bf_logo_image` (nenhum tem slot no HTML — card e faixas são CSS); example de `bf_coupon_label` = "USE CODE:". 11 → 8 campos.
