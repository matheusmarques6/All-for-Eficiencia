---
tipo: indice
assunto: casos-de-teste
autor: max-sturtevant
status: aprovado
---

Como rodar a bateria de regressão do advisor Max e o que fazer com cada tipo de falha: uma pergunta por conversa limpa, registro de passou/falhou por campo ausente, e a tabela que liga o sintoma observado à peça do corpus que precisa ser consertada — mais o mapa de cobertura da bateria e o que ela explicitamente não mede.

# Como usar

## Rodar

Uma pergunta por conversa limpa, na ordem em que estão. Contexto acumulado
mascara falha de roteamento: se a nota certa já foi lida num caso anterior, o
caso seguinte não testa mais o índice, testa a memória da sessão.

Registrar, para cada caso: **passou / falhou**, e — quando falhou — qual campo
da "Resposta certa contém" não apareceu. O campo ausente é o diagnóstico; a
sensação de que "ficou fraco" não é.

Um caso só passa se **todos** os elementos obrigatórios aparecerem. Meia resposta
certa em caso de conflito é falha, não passe parcial: o valor da resposta está
justamente em mostrar as duas versões.

## O que fazer com cada tipo de falha

Mapeado aos limiares do [[arquitetura-decisoes-e-leis-de-manutencao]] §5, que foram definidos **antes** de
medir exatamente para que a decisão não seja racionalizada depois.

| Sintoma | Casos que o pegam | Peça a consertar | O que **não** mexer |
|---|---|---|---|
| **Erro de fato** — número errado, linha errada, conteúdo que existe declarado ausente | C-01 a C-08, C-21, C-22, C-23, C-25 | **Recuperação**: caminho de leitura, nomes de nota, frontmatter, tabelas de [[numeros-de-email-marketing-mais-pedidos]] e o índice de slugs de [[mapa-dos-conflitos]] | prompt e modelo |
| **Soa genérico** — o fato está certo, a resposta poderia ser de qualquer consultor | C-19, C-20 | **[[persona]]**: aprofundar o expert reflection, principalmente §7 "o que Max nunca diria" e §2 "como ele decide" | recuperação |
| **Opina fora do corpus** — completa lacuna com boa prática de mercado | C-09, C-24 | **Guardrail** (regra 5 do [[_protocolo]] + [[mapa-da-cobertura]]). É a falha mais grave da lista: indetectável para quem não conhece o assunto | nada mais, antes de fechar esta |
| **Perde coerência em conversa longa** — contradiz o que ele mesmo disse três turnos atrás | nenhum caso isolado pega; aparece rodando a bateria inteira numa sessão só | **Arquitetura de memória** — e só aqui | prompt, corpus, persona |

Três leituras que mudam o conserto e não estão na tabela:

**Recusa indevida conta como erro de fato, não como excesso de cautela.** C-07,
C-10, C-21 e C-22 existem para pegar isso. Quando o advisor recusa uma pergunta
que o corpus responde, o defeito é de recuperação, e é o mais caro de todos
porque é silencioso: ninguém audita uma resposta que nunca foi dada.

**Erro de atribuição é peça própria.** C-12, e o lado de atribuição de C-05,
C-08, C-11, C-15, C-18, C-21 e C-23. O fato pode estar certo e a resposta ainda
assim errada, se material de faixa `outro-provavel` sair como *"o Max diz"*. O
conserto é em [[mapa-da-autoria]] e no frontmatter `registro:` das notas afetadas —
nunca em [[persona]].

**Corrigir a nota de controle não corrige a nota do assunto.** Primeira lei de
manutenção do [[arquitetura-decisoes-e-leis-de-manutencao]] §5.1. Índice e nota são cópias independentes da
mesma afirmação: toda correção derivada de uma falha aqui precisa de varredura
por texto no corpus inteiro, nunca de uma edição no lugar onde o erro apareceu.
Depois de corrigir, **rodar o caso de novo** — e rodar também os casos vizinhos
da mesma pasta, que é onde a cópia não corrigida costuma estar.

## Cobertura desta bateria

| Categoria | Casos |
|---|---|
| Roteamento simples | C-01 |
| Número com conflito | C-02 |
| Número sem conflito | C-03 |
| Armadilha de referente | C-04 |
| Número corrompido não citável | C-05, C-06 |
| Corrompido **com** versão limpa | C-07 |
| Rótulo que não é percentual | C-08 |
| Recusa total | C-09 |
| Recusa parcial | C-10 |
| Célula vazia | C-11 |
| Atribuição | C-12 |
| Procedimento datado | C-13 |
| Artefato verbatim | C-14 |
| Conflito entre módulos | C-15, C-16 |
| Conflito dentro do mesmo registro | C-17, C-18 |
| Voz | C-19, C-20 |
| Falso negativo | C-21, C-22, C-23 |
| Recusa com aviso ativo | C-24 |
| Ruído de ASR preservado | C-25 |

**O que esta bateria não mede.** Coerência em conversa de vários turnos, ordem
de leitura efetivamente percorrida (só o resultado é observável), e qualquer
coisa dos quatro módulos de fala não-Max apresentada como *voz* — porque ali não
há voz dele para comparar. Também não mede densidade: um caso por pasta não
prova que a pasta inteira está sã, prova que o caminho até aquela nota está.
