---
tipo: secao
secao: header
variantes: 0
ativas: 0
com_julgamento: 0
status: aprovada
---

# Cobertura

**Nenhuma variante cadastrada.** Das 44 variantes do catálogo, zero
pertencem à seção `header`. A pasta `variantes/header/` não existe.

# Consequência

Quando um blueprint pede um bloco de `header`, o Montador não tem
candidata nenhuma para rankear e o pipeline cai no template global
(`email_reference_templates`) — silenciosamente, sem registro de que a
seção pedida não tinha candidata. O e-mail sai sem a identidade visual que
o resto da peça carrega.

Ver [[header-sem-variante]].

# Chave de decisão

Não se aplica enquanto não houver variante.

# Onde a seção não cobre

Tudo. Nenhum momento, nenhuma objeção, nenhum registro tem candidata de
`header` — a lacuna é total, não parcial.
