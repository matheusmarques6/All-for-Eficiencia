---
tipo: indice
modulo: auditoria
assunto: correcoes-e-conflitos-novos-da-consolidacao
autor: max-sturtevant
conflitos: []
status: aprovado
---

Fechamento da auditoria da consolidação do registro de conflitos do corpus de Max Sturtevant: as correções aplicadas a entradas herdadas, os conflitos novos abertos nesta consolidação e a lista do que parece conflito e não é.

## Correções aplicadas a entradas herdadas

| Entrada | O que estava errado | O que passou a valer |
|---|---|---|
| `sms-frequencia` | resolvia por média ("7 mensagens em 31 dias dá menos de 2/semana"), violando a regra 2 do protocolo | dá as versões e os quatro critérios dele (evento · lacuna < 1 semana · dias consecutivos para evento grande · segmentar acima do teto, L9368); a leitura das datas registra que a semana do lançamento passa do teto |
| `flows-onde-testar` / `otimizacao-onde-testar` | as duas afirmavam que "o corpus nunca faz essa distinção" | o deck faz a distinção duas vezes — a palavra "**content**" em L4128 e o heading "**Flow Specific A/B Tests**" em L4139. O que falta é a frase que amarra, não a evidência |
| `campanhas-share-do-90-day-engaged` | apresentado no índice de campanhas como conflito | reclassificado como **armadilha de leitura**: L4838 e L4652 medem vendas, L5139 e L5597 medem envios, e **L4652 nem é percentual** — é rótulo de Pareto (confirmado por L5017-5021) |
| `doutrina-proporcao-basico-avancado` | classificava L8764 como slide GAMMA | L8764 é resumo da página do curso e aponta para o deck (L8769); ver veredicto arbitrado 1 |
| `doutrina-segundos-de-atencao` | afirmava que o "antes" não conflita | conflita; ver veredicto arbitrado 2 |


## Conflitos novos, abertos nesta consolidação

| Slug | Por que ninguém tinha aberto |
|---|---|
| `campanhas-cadencia-alta-vs-tier-1m` | a faixa danosa (L5264-5269) e o tier de topo (L5298) estão a 30 linhas de distância no mesmo deck, em seções com títulos diferentes; a reconciliação está só na fala (L4240, L4270-4276), num bloco `outro-provavel` |
| `copy-email-marketing-brain-tamanho` | "500 pages" (L6775, slide) e "500 docs" (L6387, fala) parecem o mesmo número; a divergência é de **unidade**. O "past 6 months" de L6387 não existe em nenhum outro lugar do corpus |
| `entre-modulos-tabela-de-metricas` | cada unidade comparou a sua tabela com o glossário; ninguém comparou a tabela de fundamentos (L372-380) com a de deliverability (L8713-8719). Divergem em click rate (0,5%/2% vs 0,75%) e unsubscribe (0,3% vs 0,4%) |


## O que parece conflito e não é

Registrado para que ninguém abra entrada nova por engano.

- **Prazo da janela de honeymoon.** A fala dá 30 dias (L22), o slide não dá prazo nenhum
  (L319). Omissão, não contradição.
- **Desconto.** A regra contra desconto vale para campanhas (L4197, bullets escritos;
  L4372-4378, fala **outro-narrador**); os descontos do welcome flow (L3495-3497) e o
  email de sale do Calvin Klein (L6364-6365, `max-provado`) estão em outro escopo. O
  corpus delimita, não se contradiz — e a versão com lastro de Max é a escrita (L4197)
  mais o walkthrough do Calvin Klein, não a formulação falada de L4372-4378.
- **S.C.E. grafado "SDE"** em L4715 — erro de ASR. O slide (L5504) dá a forma correta.
- **Email share de 40%.** Tabela (L374) e glossário (L388) concordam.
- **Slide reaproveitado não é segunda fonte.** A linha de tabela do 90 Day Engaged List
  é idêntica em L5587 e L8734; os quatro testes de topo são idênticos entre L4141-4176 e
  L9151-9180. Ver `otimizacao-deck-duplicado`.
- **Ordem do S.C.E.** O acrônimo está certo em três lugares; só a numeração erra.

