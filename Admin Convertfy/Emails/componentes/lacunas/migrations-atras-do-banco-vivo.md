---
tipo: lacuna
sobre: codigo
descoberta_em: 2026-08-31
status: aberta
---

# O que falta

12 colunas existem hoje na tabela viva de variantes de componente no banco
Supabase e **não têm migration correspondente** em `supabase/migrations/`
no repo `admin-convertfy`. O schema que produz `_inventario.md` (a fonte
`C:\Users\Usuario\Downloads\componentesinventario.md` que `.tools/inventario.py`
parseia) reflete o banco vivo — inclui campos como `niche_affinity`,
`positioning`, `schema_campos` e as sete colunas de prosa (`descricao_curta`
até `direcao_fotografica`) que este vault trata como fonte de verdade. O
histórico de migrations do projeto não reconstrói essa mesma estrutura de
ponta a ponta.

# Por que importa

Migration é o mecanismo normal pelo qual o time reconstrói o schema em um
ambiente novo (staging, branch de teste, restauração de desastre) e pelo
qual outro desenvolvedor entende *por que* uma coluna existe. Colunas
adicionadas fora desse fluxo — via Supabase Studio, script ad-hoc ou
migration aplicada e depois descartada do controle de versão — não deixam
rastro de intenção: ninguém consegue saber, olhando só o repo, se
`niche_affinity` foi uma decisão de produto abandonada ou um campo em uso
real. É exatamente essa incerteza que motivou os agentes fazerem o
inventário deste vault a partir do banco em vez de a partir das migrations.

# O que se perde hoje

Reprodutibilidade. Se alguém precisar recriar o ambiente de banco do zero
(um branch de teste do Supabase, por exemplo), rodar todas as migrations em
sequência **não** produz a mesma tabela que está em produção — faltam 12
colunas. Esta camada do vault (`componentes/`) existe em parte para
compensar esse hiato: é o registro legível do que o banco realmente tem,
enquanto o código-fonte das migrations não conta a história completa.

# Fora do escopo desta entrega

Escrever as 12 migrations retroativas que faltam, ou decidir quais das 12
colunas são intencionais versus resíduo. Isso é trabalho de
`supabase-architect` sobre o repo `admin-convertfy`, não deste vault.
