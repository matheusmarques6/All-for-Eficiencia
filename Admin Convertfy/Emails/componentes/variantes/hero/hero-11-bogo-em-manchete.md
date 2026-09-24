---
tipo: componente
slug: hero-11-bogo-em-manchete
variant_id: 2ce07010-4b17-4f44-931a-f5f0b014b444
nome_no_banco: "hero section 11"
secao: hero
status: aprovada
fonte: catalogacao-2026-09-19
schema_campos: 6
product_slots: 0
objecao: [preco-valor]
aliviador: [dado_de_adequacao]
profundidade: afirmacao
registro: [comercial, volume-impulso]
registro_vetado: [luxo, clinico-sobrio, premium-editorial]
paleta: [com-acento-definido]
papel_na_peca: [peca-inteira]
peso: { altura_px: 1022, classe: medio, fonte: medido }
convivencia: [peca-inteira-nao-e-bloco]
exige: [oferta-bogo-real]
aprendizados: [[[cupom-repetido-precisa-de-papel]], [[deadline-falso-queima-o-proximo]]]
ativa: true
dispositivo: oferta_em_manchete
---

## Descrição curta
Abre o e-mail já com a oferta de compre-e-leve em manchete: o leitor não precisa rolar para saber o que ganha — o resgate (código ou desconto automático) fica para outra posição. Obriga headline em duas linhas, sublinha de urgência, corpo curto, CTA e imagem de fundo. Não há faixa de cupom nem campo de código: o logo é célula fixa do layout.

## Descrição detalhada
Caixa de logo fixa no topo (célula `LOGO HERE` do layout, sem campo). Headline em duas linhas de corpos diferentes (`bogo_headline_1` grande, `bogo_headline_2` menor). Sublinha de urgência (`bogo_subline`). Corpo de uma frase (`bogo_body`) e CTA sólido (`bogo_cta_label`). Tudo sobre `bogo_background_image`, gerada. Como a hero 14 (mesmo dispositivo), DECLARA a oferta e não entrega código: nenhuma das duas tem cupom no HTML nem no schema — quem entrega o código é um offer abaixo. Difere das heroes 13 e 15 por não nomear data de campanha.

## Quando usar
Toque cuja intenção é declarar uma oferta de compre-e-leve, quando a mecânica é real na plataforma e cabe em uma frase; se houver código, ele entra num offer abaixo. Funciona como peça inteira: o e-mail pode terminar aqui ou seguir só com rodapé.

## Quando não usar
Welcome-1 com incentivo simples de percentual: o dispositivo é BOGO, e forçar "10% off" na manchete de compre-e-leve entrega uma promessa que a loja não faz. Também não use quando outra posição já entrega o mesmo código sem papel novo, e nunca com sublinha de prazo sem prazo real na plataforma.

## Convivência
Não empilhar com body de oferta (repetiria a manchete). Um offer de código abaixo é o par natural quando há cupom. Depois, só products leve ou footer.

## Notas de cadastro
Na run de 17/09 o Curador a descreveu como "peça inteira promocional sem eixos": esta nota é a resposta. A descrição do banco bate com a anatomia. Atenção a uma leitura fácil de errar: `papel_na_peca: [peca-inteira]` é PAPEL (ela é o e-mail, não um bloco entre outros), `peso.classe: medio` é ALTURA — a ficha da catalogação declarava `peca-inteira` também na classe, a 1180px, mas nem esse número chegaria ao limiar da classe (≥2000) e a medição de 19/09 dá 1022px. Papel e classe não precisam coincidir.

**Conserto de 19/09 (admin, auditor de âncoras)**: saíram `bogo_coupon_label` e `bogo_coupon_code` (o HTML não tem faixa de cupom — os campos não tinham onde ancorar) e `bogo_logo_image` (sem slot). 9 → 6 campos.
