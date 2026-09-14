---
tipo: requisito
familia: ativo-visual
classe: diretiva_imagem
fonte_resolucao: nenhuma
default_quando_desconhecido: false
valor: ornamento-grafico-de-identidade
status: aprovada
procedencia: inventario
---

# O que é

A marca tem um elemento gráfico ornamental próprio — padrão, textura,
motivo repetido — que já faz parte da identidade visual, não uma
decoração genérica escolhida na hora.

# Por que é eliminatório e não preferência

A faixa ornamental (xadrez, na referência) precisa ser reconhecível
como parte da identidade da marca para funcionar como assinatura visual.
Sem essa origem na identidade, a mesma faixa não vira "menos autêntica"
— vira enfeite solto, sem relação nenhuma com a marca que a está usando.

Da prosa do inventário, verbatim (`produtos 6`): *"Marca sem ornamento
gráfico — a faixa xadrez precisa fazer parte da identidade, senão vira
enfeite solto."*

# Como se resolve
Não se resolve contra a loja: o pipeline **gera** a imagem com esta
propriedade. Entra em `diretivas_de_imagem` da variante e no brief da foto
(`photo_direction`); `image_format` confere por pixel o que der conferir.
**Nunca elimina variante.**