---
tipo: lacuna
sobre: cadastro
descoberta_em: 2026-08-31
status: aberta
---

# O que falta

Quatro variantes de `body` — [[body-6-skin-minimalism-101]],
[[body-7-faq]], [[body-8-cards-vidro]] e [[body-9-key-features-pilulas]] —
estão `ativa: true` no banco com os sete campos de prosa do inventário
vazios: `descricao_curta`, `descricao_detalhada`, `quando_usar`,
`quando_nao_usar`, `copy_ia`, `design_system` e `direcao_fotografica`
retornam `_(vazio)_` nas quatro. São exatamente as 4 variantes que
`test_inventario.py` confirma como "sem nenhum julgamento" no inventário de
44. Nenhuma delas tem `momento`, `objecao`, `registro` ou `exige`
preenchido — todos os eixos de ranking estão vazios também.

# Por que importa

O [[_protocolo-de-selecao|protocolo de seleção]] rankeia candidatas por
`objecao`, `registro`/`registro_vetado`, `paleta` e `papel_na_peca`, nessa
ordem — e usa a prosa (`quando_usar`/`quando_nao_usar`) como o material que
justifica a escolha. Com todos os eixos vazios, `body-6`, `body-7`, `body-8`
e `body-9` nunca são filtradas por veto e nunca perdem pontos por
desalinhamento: elas competem em pé de igualdade com variantes plenamente
julgadas, sem nenhum critério que as distinga entre si ou das outras. Um
LLM (ou um humano seguindo o protocolo) escolhendo entre elas está,
literalmente, escolhendo às cegas — não há frase nenhuma dizendo quando usar
uma FAQ (`body-7`) em vez de um bloco de cards (`body-8`).

# O que se perde hoje

Quando o blueprint pede `body` e uma dessas quatro é sorteada, a loja recebe
um bloco sem nenhuma garantia de que ele serve o momento, a objeção ou o
registro daquele e-mail — o julgamento que orienta todas as outras 40
variantes simplesmente não existe para essas quatro. É pior que cair no
template global (que ao menos é sempre o mesmo, previsível): aqui a peça
muda a cada geração e ninguém pode prever qual.

# Fora do escopo desta entrega

Escrever a prosa e os eixos de `body-6`, `body-7`, `body-8` e `body-9`.
Exige julgamento de conteúdo (quando cada uma serve, que objeção ataca) que
não faz parte desta entrega — só o registro do vazio, para não sumir.
