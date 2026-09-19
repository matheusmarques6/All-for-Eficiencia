---
tipo: componente
slug: body-21-tres-selos-e-garantia
variant_id: a2b509a4-2b74-42de-851d-01fe91735847
nome_no_banco: "body 21"
secao: body
status: aprovada
fonte: catalogacao-2026-09-19
schema_campos: 7
product_slots: 0
objecao: [confianca-no-canal]
aliviador: [transparencia_de_politica]
profundidade: garantia
registro: [bold-alto-contraste]
registro_vetado: [festivo]
paleta: [preto-e-branco]
papel_na_peca: [meio]
itens: { min: 3, max: 3 }
peso: { altura_px: 959, classe: medio, fonte: medido }
convivencia: []
exige: [politica-real]
aprendizados: [[[remocao-de-risco-escala-com-o-ticket]], [[cada-alegacao-e-uma-promessa-operacional]]]
---

## Descrição curta
Remove o risco da transação no ponto da decisão: o leitor vê três compromissos em selos, lê a política por extenso e sai sabendo o que acontece se der errado. Obriga três rótulos de selo (os ícones são fixos no HTML), headline, corpo de política, CTA e foto.

## Descrição detalhada
Três blocos empilhados de fundos alternados. O primeiro é preto, com três círculos fixos em linha (células do layout, sem campo de imagem), cada um com rótulo (`trust_icon_N_label`). Seguem headline (`trust_headline`), corpo (`trust_body`) — o slot onde a política é escrita por extenso, com prazo —, CTA (`trust_cta_label`) e foto (`trust_photo`, gerada). A profundidade `garantia` é o que a anatomia comporta: selos nomeiam, o corpo escreve a política. Se os selos forem de pagamento em vez de troca/frete, o aliviador realizado desliza para `seguranca_de_pagamento` — a anatomia serve os dois; o declarado aqui é o caso dominante.

## Quando usar
No toque de remoção de risco: [[abandoned_cart-4]] é o encaixe exato (profundidade mínima `garantia`, aliviadores admitidos incluem `transparencia_de_politica`) e [[welcome-5]] o segundo habitat — os medos do canal riscados um a um. Exige política real: prazo de troca, condição de devolução, canal de suporte que a operação sustenta. Quanto maior o ticket, mais alto este bloco sobe na peça.

## Quando não usar
No [[abandoned_cart-1]] ou no primeiro toque de qualquer flow: garantia antes da dúvida existir é bloco defensivo cedo demais — cria a dúvida que pretendia curar. E nunca com política inventada ou arredondada ("troca grátis" quando a troca tem custo): cada selo é uma promessa operacional; sem lastro, o bloco é removido, não suavizado.

## Convivência
Não duplicar remoção de risco na mesma peça (com offer-21, que carrega selos próprios): duas faixas de selos leem como seguro demais — protestando demais. Fundos alternados preto/claro pedem vizinhos de emenda limpa; entre duas seções escuras ele perde o contraste que o organiza.

## Notas de cadastro
Há OUTRA "body 21" no banco, na seção offer (f8fd38f6-04d0-4337-a130-31e207510b59) — homônimas, variantes diferentes; endereçar sempre pelo `variant_id`. Descrição do banco bate com a anatomia. Relação com a lacuna [[body-garantias-3-selos]]: mesma família de dispositivo, mas a lacuna pede faixa compacta de APOIO e esta é bloco de meio com headline, corpo e foto — não a fecha; registrado no relatório. Sem HTML para medir altura — `peso` omitido.

**Conserto de 19/09 (admin, auditor de âncoras)**: saíram `trust_icon_1..3` (fixos no HTML). 10 → 7 campos.
