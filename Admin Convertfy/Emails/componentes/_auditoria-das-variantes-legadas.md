---
tipo: auditoria
escopo: variantes-legadas
verificado_em: 2026-09-24
status: aprovada
---

Auditoria das quatro notas preservadas fora do conjunto de 72 variantes canônicas. Todas permanecem inelegíveis: `legado: true`, `ativa: false` e `status: legado`.

# Resultado

| Nota | Dispositivo histórico | Verificação | Substituição atual |
|---|---|---|---|
| [[body-cards-de-vidro-sobre-fotos]] | `catalogo_por_ocasiao` | Não possui `variant_id`. O conteúdo e a descrição coincidem com [[body-8-cards-de-vidro-por-ocasiao]], que está ativa no banco como `body 8 - cards vidro`. | [[body-8-cards-de-vidro-por-ocasiao]] |
| [[reviews-3a-depoimento-longo-monoespacado]] | `prova_por_relato` | O `variant_id` antigo não existe mais no banco. A estrutura é igual à de [[reviews-3b-depoimento-longo-monoespacado]] e usa dois relatos longos com fotografia do item. | Nenhuma direta |
| [[reviews-3b-depoimento-longo-monoespacado]] | `prova_por_relato` | O `variant_id` antigo não existe mais no banco. A estrutura é igual à de [[reviews-3a-depoimento-longo-monoespacado]]; a diferença histórica era apenas o cadastro `review 2`/`review 3`. | Nenhuma direta |
| [[reviews-8-ugc-de-comunidade]] | `prova_com_vitrine` | O `variant_id` antigo não existe mais. O nome `review 8` foi reutilizado no banco por [[reviews-8-tres-cards-com-nota]], que é outra peça e realiza `prova_por_volume`. | Nenhuma direta; `review 8` atual é outra peça |

# Decisões

- [[body-cards-de-vidro-sobre-fotos]] é um rascunho incompleto do mesmo mecanismo de [[body-8-cards-de-vidro-por-ocasiao]].
- [[reviews-3a-depoimento-longo-monoespacado]] e [[reviews-3b-depoimento-longo-monoespacado]] são duplicatas aposentadas. Ambas realizavam `prova_por_relato`.
- [[reviews-8-ugc-de-comunidade]] realizava `prova_com_vitrine`; o `review 8` atual é [[reviews-8-tres-cards-com-nota]] e realiza `prova_por_volume`.
- Nenhuma das quatro deve voltar à seleção apenas por continuar fisicamente em `variantes/`.

Vocabulário completo: [[_glossario-de-tags-das-variantes]] · Biblioteca atual: [[_catalogo]]
