---
tipo: inventario
status: aprovada
fonte: supabase
extraido_em: 2026-09-24
registros_no_banco: 75
variantes_canonicas: 72
ativas_no_banco: 67
---

Snapshot atual de `public.email_component_variants`: **75 registros**, sendo **72 variantes canônicas** e **3 espelhos ativos de offer na seção body**. Há **67 registros ativos** e nenhum registro sem `dispositivo`.

# Cobertura por seção

| Seção | Registros | Ativos |
|---|---:|---:|
| body | 21 | 13 |
| footer | 4 | 4 |
| hero | 18 | 18 |
| offer | 9 | 9 |
| products | 15 | 15 |
| reviews | 8 | 8 |
| **Total** | **75** | **67** |

`header` e `cta` continuam sem variantes. Os três espelhos de `body` são `offer 1 (body)`, `offer 4 (body)` e `offer 11 (body)`; eles reutilizam notas canônicas de offer.

# Cobertura por dispositivo

| Dispositivo | Registros | Ativos |
|---|---:|---:|
| abertura_editorial | 3 | 3 |
| antes_e_depois | 1 | 1 |
| assinatura_minima | 1 | 1 |
| campanha_nomeada | 2 | 2 |
| carrinho_dinamico | 1 | 1 |
| catalogo_por_ocasiao | 1 | 1 |
| cena_de_uso | 2 | 2 |
| codigo_entregue | 4 | 4 |
| codigo_relembrado | 2 | 2 |
| comparacao_pareada | 3 | 2 |
| duvida_antecipada | 1 | 0 |
| escassez_por_estoque | 1 | 1 |
| galeria_de_angulos | 1 | 1 |
| lineup_de_colecao | 3 | 3 |
| lista_enumerada | 4 | 2 |
| mecanismo_apontado | 2 | 2 |
| menu_de_saida | 3 | 3 |
| moldura_de_genero | 1 | 1 |
| nao_classificado | 2 | 0 |
| oferta_adiada | 2 | 2 |
| oferta_condicionada | 3 | 3 |
| oferta_de_ajuda | 1 | 1 |
| oferta_em_manchete | 4 | 4 |
| pergunta_ao_leitor | 1 | 1 |
| prazo_declarado | 1 | 1 |
| produto_unico_aprofundado | 2 | 2 |
| prova_com_vitrine | 2 | 2 |
| prova_por_autoridade | 1 | 1 |
| prova_por_relato | 3 | 3 |
| prova_por_volume | 2 | 2 |
| remocao_de_risco | 1 | 1 |
| tese_declarada | 5 | 3 |
| vitrine_narrada | 4 | 4 |
| vitrine_paralela | 5 | 5 |

Existem **33 dispositivos utilizáveis** e o valor de controle `nao_classificado`. As definições operacionais estão em `componentes/dispositivos/`.

# Proveniência

- Fonte de verdade: projeto Supabase `ppygkfeffknypfncsnlv`, tabela `public.email_component_variants`.
- Data de conferência: 2026-09-24.
- Notas canônicas: 72; notas locais marcadas `legado: true` não entram na biblioteca ativa.

Legadas: [[_auditoria-das-variantes-legadas]] · Tags: [[_glossario-de-tags-das-variantes]]
