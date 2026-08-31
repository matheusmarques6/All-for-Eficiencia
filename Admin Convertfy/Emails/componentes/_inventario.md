---
tipo: inventario
status: aprovada
fonte: componentesinventario.md
extraido_em: 2026-08-31
branch: componentes/estrutura
---

Números e procedência da biblioteca de 44 variantes. Sem prosa nova — os
julgamentos ficam nas notas de seção ([[_hero]], [[_body]], [[_products]],
[[_reviews]], [[_offer]], [[_footer]]) e nas notas de variante.

# Fonte e conferência

- Fonte: `C:\Users\Usuario\Downloads\componentesinventario.md`, extraído do
  Supabase (`email_component_variants`) em **2026-08-31**.
- Branch de referência: `componentes/estrutura`.
- O HTML das 44 variantes foi conferido por md5 contra o banco:
  **44 de 44** bateram. 35 vieram fiéis do próprio markdown do inventário;
  as outras 9 (base64 embutido truncado no markdown) foram puxadas
  diretamente do banco e conferidas linha a linha contra a tabela de
  md5/bytes extraída por SQL. Detalhe em
  `.superpowers/sdd/2026-08-31-vault-componentes-email/html-md5-do-banco.md`.

# Cobertura por seção

| Seção | Variantes | Ativas |
|---|---|---|
| header | 0 | — |
| hero | 9 | 9 |
| body | 9 | 7 |
| products | 9 | 9 |
| reviews | 7 | 7 |
| cta | 0 | — |
| offer | 6 | 6 |
| footer | 4 | 4 |
| **Total** | **44** | **42** |

`header` e `cta` têm zero variantes — a lacuna estrutural mais importante
do conjunto: quando o blueprint pede uma dessas seções, o pipeline cai
silenciosamente no template global. Ver [[header-sem-variante]] e
[[cta-sem-variante]].

# Julgamento e schema

- **Prosa:** 40 de 44 variantes têm ao menos um dos seis campos de
  julgamento (descrição, quando usar, quando NÃO usar, orientação de copy,
  design system, direção fotográfica) preenchido; 4 não têm nenhum —
  `body 6`, `body 7`, `body 8`, `body 9`, todas ativas. Ver
  [[body-quatro-variantes-sem-julgamento]].
- **Schema:** 39 de 44 têm campos de `output_schema` declarados; 5 estão
  zerados. Ver [[cinco-variantes-sem-schema]].

# Vocabulário controlado

| Camada | Contagem |
|---|---|
| `eixos/` (momento + objecao + paleta + papel-na-peca + registro) | 56 |
| `requisitos/` | 52 |
| `convivencia/` | 6 |

# Lacunas

15 notas em `lacunas/`: [[header-sem-variante]] ·
[[cta-sem-variante]] · [[body-quatro-variantes-sem-julgamento]] ·
[[cinco-variantes-sem-schema]] · [[reviews-3-duplicado]] ·
[[hero-8-duplicata-de-hero-10]] · [[offer-e-footer-sem-design-system]] ·
[[o-que-o-curador-ainda-nao-tem]] · [[migrations-atras-do-banco-vivo]] ·
[[welcome-5-sem-variante-ativa]] · [[dezesseis-variantes-sem-objecao]] ·
[[estruturas-de-welcome-sem-variantes]] ·
[[tags-do-banco-contradizem-a-prosa]] · [[conceitos-sem-requisito]] ·
[[aplica-a-nao-reflete-o-corpo]].

---

Protocolo que consome estes números: [[_protocolo-de-selecao]] · Ponte de
parâmetros: [[_parametros-da-loja]]
