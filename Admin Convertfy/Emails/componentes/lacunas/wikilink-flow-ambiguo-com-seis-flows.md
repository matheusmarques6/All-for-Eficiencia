---
tipo: lacuna
sobre: codigo
secao: geral
descoberta_em: 2026-09-09
status: aberta
---

Quando as intenções dos seis flows fora do welcome forem promovidas a
`aprovada`, o vault passa a ter sete arquivos chamados `_flow.md` e sete
`_progressao.md`, e os 40 wikilinks `[[_flow]]` e `[[_progressao]]` que hoje
apontam sem ambiguidade para o welcome deixam de ter um alvo único — e o
sincronizador resolve wikilink por nome de arquivo.

# O que falta

Uma regra de resolução para wikilink cujo nome de arquivo existe em mais de
uma pasta. Hoje o vault tem um caso só, `welcome-1.md` (eixo de momento e
intenção do toque 1), e convive com ele sem que se saiba para qual dos dois o
sincronizador aponta. A tarefa T8 do briefing de reorganização cria seis
pastas `intencoes/<flow_type>/` com `_flow.md` cada — o caminho é fixado pela
regra 2 do próprio briefing, então renomear não é opção.

Medido em 2026-09-09 (recontado na revisão de T4): 40 ocorrências — 26 de
`[[_flow]]` e 14 de `[[_progressao]]` — em **25 notas**: seis eixos de
objeção (`adesao-social`, `composicao-formulacao`, `confianca-no-canal`,
`disponibilidade-urgencia`, `preco-valor`, `qualidade-eficacia`), os eixos de
momento `welcome-1`, `welcome-meio` e `welcome-tardio`, o eixo `fecha` de
papel-na-peça, a estrutura `avelmore-deadline-objecao`, os aprendizados
`deadline-falso-queima-o-proximo` e `extensao-declarada-quatro-condicoes`, a
lacuna `exige-cupom-sem-perfil-de-ativos`, as oito intenções do welcome, o
`_flow` e a `_progressao` entre si, e o `_julgamento` — que sozinho tem seis,
a nota com mais links do vault. Todas hoje significam "o flow do welcome".

# Por que importa

Duas saídas possíveis, e as duas são código, não vault:

- O sincronizador resolve pelo caminho quando o link é qualificado —
  `[[intencoes/welcome/_flow|_flow]]`. Aí as 40 ocorrências precisam ser
  reescritas nessa forma, de uma vez, antes da promoção. O Obsidian aceita.
- O sincronizador resolve pelo contexto — link dentro de
  `intencoes/welcome/` aponta para o `_flow.md` da mesma pasta; link fora
  dela precisa ser qualificado. Aí só as ~12 ocorrências fora de
  `intencoes/welcome/` precisam de reescrita.

Sem decidir, promover qualquer um dos seis flows faz os 40 links
resolverem para um `_flow.md` aleatório — e um eixo de objeção passa a citar
"a regra transversal 3" de um flow que não a tem.

# O que se perde hoje

Nada, enquanto os seis flows estiverem em `rascunho`: rascunho não entra no
pipeline e a colisão só existe no Obsidian. A perda aparece na promoção. A
decisão precisa ser tomada antes dela, e por quem tem o código do
sincronizador — a seção 4.1 do briefing (`.tools/BRIEFING-emails-reorganizacao.md`).
