---
tipo: lacuna
sobre: biblioteca
secao: geral
descoberta_em: 2026-09-09
status: aberta
---

Os oito vocabulários novos do contrato tipado das intenções (`modo`,
`riscos_*`, `profundidade_minima`, `aliviadores_*`, `veiculos_exigidos`,
`trabalhos_fixos`, `fonte_das_objecoes`, `dimensao_alvo`) somam 44 valores
fechados que nenhuma nota de `componentes/eixos/` define — o agente lê o
valor no frontmatter e não tem onde ler o que ele significa.

# O que falta

A regra 5 do vault diz que todo valor de eixo precisa ter nota:
`objecao: [confianca-no-canal]` exige [[confianca-no-canal]] em
`eixos/objecao/`, com definição, onde aparece na doutrina e como usar na
seleção. O contrato que entrou nas oito intenções do welcome ([[welcome-1]]
a [[welcome-8]]) trouxe oito vocabulários novos — dez chaves de frontmatter,
porque `riscos_*` e `aliviadores_*` têm variante elegível/admissível e
vetada — e nenhum tem pasta em `eixos/` nem nota por valor. Os valores, por
campo (marcados os que o welcome já usa; os demais só existem no
vocabulário):

- `modo` (6): `quebra_de_objecao` ✓ · `varredura_de_objecoes` ✓ ·
  `confirmacao_por_terceiros` ✓ · `varredura_de_canal` ✓ ·
  `fechamento_de_ciclo` ✓ · `manutencao_de_confianca` (reservado ao upsell e
  ao shipping_stages, T8)
- `riscos_elegiveis` / `riscos_vetados` (7): `financeiro` ✓ · `desempenho` ✓
  · `tempo` ✓ · `psicologico` ✓ · `seguranca` ✓ · `adequacao` ✓ · `social`
- `profundidade_minima` (4, ordenados): `afirmacao` ✓ < `mecanismo` ✓ <
  `prova_de_terceiro` ✓ < `garantia`
- `aliviadores_admissiveis` / `aliviadores_vetados` (10 + curinga `todos`):
  `garantia_de_devolucao` ✓ · `prova_de_terceiro` ✓ · `prova_por_volume` ✓ ·
  `demonstracao_de_mecanismo` ✓ · `transparencia_de_politica` ✓ ·
  `comparacao_de_categoria` ✓ · `seguranca_de_pagamento` ✓ ·
  `reputacao_da_loja` ✓ · `amostra_ou_teste` · `dado_de_adequacao`
- `veiculos_exigidos` (4): `origem_da_marca` ✓ · `economia_do_preco` ✓ ·
  `operacao_por_pedido` ✓ · `mecanismo_unico`
- `trabalhos_fixos` (7): `entrega_de_incentivo` ✓ ·
  `lembrete_de_incentivo_vivo` ✓ · `prazo_com_hora` ✓ ·
  `custo_de_adiar_sem_hora` ✓ · `prova_secundaria` ✓ · `remocao_de_risco` ✓
  · `espelho_do_cetico` ✓
- `fonte_das_objecoes` (3): `nao_atacadas` ✓ · `ja_atacadas` ✓ ·
  `medos_de_categoria` ✓
- `dimensao_alvo` (3): `competencia` ✓ · `integridade` ✓ · `benevolencia` ✓

As outras chaves do contrato (`n_objecoes`, `exige_dominante_da_categoria`,
`permite_reataque`, `promessa_a_pagar`, `proibicoes`) são número, booleano
ou texto livre — não são eixo e não precisam de nota.

# Por que importa

O Seletor lê `dimensao_alvo: benevolencia` em [[welcome-8]] e não tem onde
abrir "benevolência": o valor só está enumerado no briefing em `.tools/`, que
o sincronizador não lê — e nem lá há definição. O mesmo vale para
`espelho_do_cetico`, descrito só de passagem na prosa de [[welcome-4]] e de
[[adesao-social]], sem nota com esse nome que o índice possa oferecer. Seis
valores (`manutencao_de_confianca`,
`social`, `garantia`, `mecanismo_unico`, `amostra_ou_teste`,
`dado_de_adequacao`) não aparecem em nenhuma intenção e portanto não
existem em lugar nenhum que o pipeline sirva — e o primeiro deles é o modo
que T8 vai declarar nos cinco toques do shipping_stages e na abertura
do upsell. Para `objecao`, `momento` e `registro` a
nota de eixo é o que diz ao agente "quando este valor se aplica e quando
não"; aqui ele recebe a palavra e infere o resto, que é exatamente o
comportamento (`modo_origem: deduzido`) que T1 veio corrigir — declarado o
valor, o significado continua deduzido.

# O que se perde hoje

Definição legível por valor: o agente não consegue abrir uma nota para
conferir se a prova que tem em mãos é `prova_de_terceiro` ou só
`afirmacao`, nem o que separa `varredura_de_canal` de
`varredura_de_objecoes`. Consistência entre flows: quando T8 usar os mesmos
valores em seis flows, cada intenção vai reexplicar o vocabulário na sua
prosa, e as explicações vão divergir. Validação: `python .tools/valida.py`
só cobre `variantes/` e o mapa `EIXOS` fixo (`momento`, `objecao`,
`registro`, `paleta`, `papel_na_peca`) — um valor errado nessas chaves
(`benevolência` com acento, `prova_terceiro` sem o `de`) não é pego aqui e
só aparece no sync, como nota pulada.

# Decisão pendente

Criar ou não as ~44 notas. A favor: é a regra 5 aplicada, o índice passa a
ter uma nota por valor e o `valida.py` pode cobrir `intencoes/` com o mesmo
mecanismo (novas pastas em `eixos/` e entradas no mapa `EIXOS`). Contra:
são oito pastas e 44 notas que hoje ninguém consome além do Seletor, o
código já reprova valor fora do vocabulário, e as pastas novas exigem
mudança no sincronizador (a regra 2 reconhece `eixos/<eixo>/<valor>.md`,
mas o conjunto de eixos é fixo em código). Alternativa mais barata a
avaliar antes: um único glossário em `componentes/` com uma seção por
vocabulário. Decidido por E1 do briefing: nada é criado agora; esta nota
guarda a decisão.
