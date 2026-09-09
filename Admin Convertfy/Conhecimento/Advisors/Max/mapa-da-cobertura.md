---
tipo: indice
assunto: cobertura-e-lacunas
autor: max-sturtevant
status: aprovado
---

Este é o registro do que o corpus Max **não** cobre, repartido em seis notas, e
existe para que o advisor recuse **nomeando a lacuna** em vez de dizer "não
sei". Consultar antes de recusar, nunca depois: o tipo do buraco é o que decide
a forma da resposta — recusa inteira, resposta pela metade, citação da promessa
ou aviso ativo.

# Para que serve

O [[_protocolo]] manda recusar tudo que estiver fora do corpus, e manda que a
recusa **nomeie a lacuna e ofereça o vizinho**. Estas notas são o que torna isso
possível: o mapa do que o corpus cobre, com que densidade, e — principalmente —
de que **tipo** é cada buraco.

O tipo é o que decide a forma da resposta. Um assunto que o corpus nunca tocou
se recusa por inteiro. Um assunto em que ele deu a finalidade e engoliu a
execução se responde pela metade, entregando a metade que existe. Uma promessa
que ele fez e não cumpriu se responde citando a promessa — porque o usuário vai
perguntar exatamente por ela. E um assunto que ele **entregou errado** exige o
oposto de uma recusa: exige o aviso.

Regra de leitura: consultar antes de recusar, nunca depois. "Não sei" não é
resposta aceitável deste advisor.

**Lacuna não é descarte.** Descarte é ruído que tiramos de propósito — pangrama
de teste de microfone, CTA de afiliado, contaminação de outra gravação. Está
todo listado em [[descartes-contaminacao-e-falha-de-asr]] e [[descartes-cta-comercial-e-placeholders]] e nos `_registro/descartes-*`. Lacuna é conteúdo do
curso que **falta**. Nunca confundir os dois: nenhuma linha descartada vira
lacuna, e nenhuma lacuna se explica dizendo "isso a gente tirou".

---

# As partes

| Nota | Que lacuna registra |
|---|---|
| [[densidade-do-corpus-por-assunto]] | Nenhuma — registra o **contrário**: quanta matéria existe por assunto, em notas e em palavras de fala e de slide, e onde a densidade baixa avisa que a lacuna é provável. É a primeira parada. |
| [[lacunas-por-assunto-nao-coberto]] | **Lacuna total** — o que nem a fala, nem o slide, nem um exemplo tocam: delay de cart/checkout abandon, critério de escolha dentro de catálogo, preço de ferramenta. Mais as dezesseis ausências **falsas**, já derrubadas contra o bruto, que nunca devem ser recusadas. |
| [[lacunas-por-cobertura-parcial-e-promessa-nao-cumprida]] | **Cobertura parcial** — o Sunset Flow como caso-escola, filtro e saída de flow, limiar de teste A/B, janela de métrica, setup técnico, Email Architect, Alia, warming. E **promessa não cumprida** — os swipe files de 30 SMS e 84 emails, o doc de A/B tests, as seções de walkthrough anunciadas e vazias. |
| [[lacunas-por-falha-tecnica-e-entrega-errada]] | **Perda por falha técnica** — os dois cortes de áudio em deliverability, o loop de ASR sobre testimonials, a transcrição vazia de "The Principles of Good Copy", os ~79 rótulos de exemplo sem imagem, as frases truncadas que levaram número. E **entregue errado** — o opt-in de telefone que é o de email colado, o upload "para Klaviyo" demonstrado no Omnisend, o deck de Optimization que repete o de Flows. |
| [[o-que-o-corpus-nao-cobre]] | Os assuntos que vão ser perguntados assim mesmo, com a varredura que prova a ausência: **consentimento e compliance de SMS — a lacuna mais grave do corpus** —, preço de ferramenta, B2B e assinatura, mercados fora dos EUA, plataformas concorrentes, canais adjacentes. |
| [[limites-de-autoria-e-datacao]] | Nenhuma — são os dois limites que **não** são lacuna e não geram recusa: os ~25% da fala que não são de Max e não podem sair entre aspas atribuídas a ele, e a ausência de data de gravação, com as âncoras temporais e o que apodrece primeiro. |
