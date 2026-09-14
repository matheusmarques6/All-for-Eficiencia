---
tipo: lacuna
sobre: cadastro
descoberta_em: 2026-08-31
status: aberta
---

# O que falta

[[offer-1-condicao-sem-imagem]] e as quatro variantes de footer —
[[footer-1-menu-outline]], [[footer-2-menu-solido]],
[[footer-3-dark-editorial]] e [[footer-4-dark-mega-menu]] — têm as seções
"Design system" e "Direção fotográfica" vazias (`_(vazio)_` no inventário),
mesmo estando todas `ativa: true` e com as demais cinco seções de prosa
(`descricao_curta`, `descricao_detalhada`, `quando_usar`, `quando_nao_usar`,
`copy_ia`) preenchidas.

# Por que importa

"Design system" é onde o vault registra dimensão, paleta hexadecimal,
tipografia e regras de implementação HTML/CSS — o material que o agente de
HTML (#7 do pipeline) usa para repintar a arquitetura sem inventar medida.
"Direção fotográfica" faz o mesmo para o agente de Imagem (#6). Sem essas
duas seções, as cinco variantes têm julgamento de **quando usar** mas não
de **como construir**: o "porquê" existe, o "como" não. Para `offer-1` e
`footer-1`/`footer-2`/`footer-3`, a ausência de direção fotográfica é
esperada — nenhuma das quatro usa imagem (footers são menu + legal;
`offer-1` é "condição sem imagem", no próprio nome). Mas a ausência de
Design System nas cinco é diferente: mesmo peças sem foto têm cor, borda,
tipografia e grid a especificar, e nenhuma das cinco tem isso registrado.

# O que se perde hoje

O agente de HTML monta essas cinco variantes sem a mesma base de
especificação visual que orienta as outras 39 — ele improvisa medida,
paleta e regra de implementação a partir só da prosa narrativa (`quando_usar`,
`copy_ia`), que não substitui uma tabela de dimensões. O risco concreto é
inconsistência visual entre gerações da mesma variante: o footer 1 de uma
loja pode sair com proporções diferentes do footer 1 de outra, porque não
há um design system fixo ancorando o agente.

# Fora do escopo desta entrega

Escrever o Design System das cinco variantes — exige acesso ao HTML de
referência de cada uma e decisão de padrão visual, trabalho de conteúdo que
não cabe aqui. Registrado para não sumir.
