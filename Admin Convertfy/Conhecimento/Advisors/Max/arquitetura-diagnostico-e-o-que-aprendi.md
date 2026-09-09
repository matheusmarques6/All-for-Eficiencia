---
tipo: relatorio
status: aprovado
data: 2026-09-06
fonte: dossiê "Clones de IA de Pessoas Reais" + dossiê "Como organizar grandes corpora para agentes"
---

Primeira metade do relatório de internalização que decidiu a arquitetura do advisor Max: o que foi extraído dos dois dossiês (só o que muda decisão) e o diagnóstico medido do vault. É onde está a razão medida de cada decisão — persona por prompt como maior multiplicador de fidelidade, RAG para fato e fine-tune para estilo, busca agêntica sobre índice vetorial, degradação de contexto longo. As decisões que saíram daqui estão em [[arquitetura-decisoes-e-leis-de-manutencao]].

# O que este documento é

Relatório de internalização. Registra o que extraí dos dois dossiês, o
diagnóstico do vault como ele está hoje, e a arquitetura que vou aplicar
ao advisor **Max** quando o conhecimento real chegar. Escrito antes do
conhecimento para que a decisão de arquitetura não seja contaminada pelo
formato em que o material vier.

# 1. O que aprendi (só o que muda decisão)

Ignorei tudo que era história ou marketing. Sobrou isto:

**1.1 — Persona por prompt é o maior multiplicador de fidelidade, e é
grátis.** No teste de Turing de UC San Diego, GPT-4.5 foi julgado humano
73% das vezes **com** prompt de persona e 36% **sem**. Nenhuma outra
alavanca da lista tem esse retorno por esse custo. Consequência prática:
o system prompt do Max é o artefato mais importante do projeto, não o
corpus e não o modelo.

**1.2 — O método Stanford: entrevista → "expert reflection" → role-play.**
Park et al. (arXiv:2411.10109) clonaram 1.052 pessoas com acurácia
normalizada de 0,83 (0,86 somando survey). O passo que fez a diferença não
foi guardar a transcrição — foi pedir a um LLM que **revisasse a
transcrição do ponto de vista de um especialista** (psicólogo, economista)
e sintetizasse traços. A síntese entra na memória junto com o material
bruto. Vou usar exatamente isso sobre o conhecimento que você mandar.

**1.3 — "Fine-tune para estilo, RAG para fato" está estabelecido, não é
opinião.** Ovadia et al. (EMNLP 2024): RAG 0,875 vs fine-tuning 0,504 em
conhecimento novo. Fine-tuning não ensina fatos; ensina forma. Como o
estilo do Max cabe em prompt (ver 1.1), fine-tuning sai da mesa inteira
por ora.

**1.4 — Busca agêntica sobre arquivos derruba RAG vetorial quando o corpus
é navegável.** A Anthropic removeu RAG do Claude Code em favor de
grep/glob ("superou tudo, por muito"). Paper da Amazon Science (AAAI 2026)
mediu busca por keyword agêntica em 94,5% da fidelidade do RAG **sem
vector store nenhum**. Chunking quebra estrutura, embedding aproxima
quando o campo exige exato, índice fica stale. Esse é precisamente o caso
deste vault.

**1.5 — Contexto longo degrada muito antes do limite anunciado.** Chroma
"context rot" (jul/2025): 18 modelos, todos pioram com input maior, mesmo
em tarefa trivial. Databricks (NeurIPS 2024): poucos modelos sustentam
acurácia acima de 64k. Então "joga o vault inteiro no contexto" está
errado por medição, não por preço.

**1.6 — Progressive disclosure é a resposta a 1.5.** O padrão SKILL.md da
Anthropic: no boot carrega só nome + descrição (mediana ~80 tokens); o
corpo entra quando a tarefa casa; referências só se as instruções pedirem.
O `_INDEX.md` + `_catalogo.md` de Emails já é isso, só não estava nomeado
assim.

**1.7 — Guardrail é arquitetura, não disclaimer.** Os dois pólos estão
documentados: a Jill Watson (Georgia Tech) só responde quando há material
verificado suficiente, com validação por implicação textual — 75% a 97% de
acurácia contra ~30% do assistente da OpenAI no mesmo A/B. A CarynAI não
tinha guardrail de persona sobre o GPT-4 e o modelo seguiu o incentivo
conversacional do usuário até sair do personagem. Max nasce do lado da
Jill.

**1.8 — Erro de fato e erro de estilo têm causas diferentes e conserto
diferente.** Se o clone erra FATO, o problema é recuperação (o que foi
lido), nunca o modelo. Se a audiência distingue o clone em teste cego por
ESTILO, aí sim é camada de voz. Diagnosticar antes de mexer.

**1.9 — Números de vendor são teto otimista.** Delphi, mem0, Zep,
Intercom, Klarna: praticamente tudo autorreportado, e onde houve auditoria
independente os números encolheram (LightRAG 66,7% → 39,06% depois de
corrigir viés do LLM-juiz; Intercom Fin 76% headline vs 38–53% medido por
terceiros). Não vou calibrar nenhuma expectativa do Max por esses números.

# 2. Diagnóstico do vault (medido, não estimado)

| Medida | Valor |
|---|---|
| Notas markdown | 224 |
| Peso total do markdown | 631.795 bytes (~160k tokens) |
| Média por nota | 2.820 bytes (~700 tokens) |
| Maior nota | `_casos-de-teste.md`, 20.259 bytes |
| HTML de componentes | 526.451 bytes em 44 arquivos, fora do caminho de raciocínio |
| `Advisors/Max/` | vazio — este arquivo é o primeiro |

Três leituras disso:

**O corpus não cabe em contexto e não precisa caber.** 160k tokens está
acima da faixa onde a degradação já é medida (64k). Mas o caminho de
resposta típico do protocolo de Emails toca 5 a 8 notas — algo entre 5k e
20k tokens. O vault já resolve por seleção o que o contexto longo
resolveria por força bruta, e resolve melhor.

**A biblioteca de Emails já implementa, sem nomear, quase toda a
recomendação do dossiê 2.** Notas atômicas de ~700 tokens (a faixa de
chunk que a pesquisa recomenda, só que com fronteira semântica escrita por
humano em vez de cortada por script); vocabulário controlado em
`eixos/`; frontmatter legível por máquina que permite filtrar antes de
ler; `_catalogo.md` gerado como manifesto; `_INDEX.md` como progressive
disclosure; `valida.py` como teste de integridade referencial;
`_casos-de-teste.md` como eval. Isso é o alvo do dossiê 2, já construído.
Max herda a convenção — não invento outra.

**Portanto a decisão de arquitetura já está tomada pelos fatos.** Corpus
markdown, atômico, navegável, com metadados, num filesystem que o agente
lê direto: a árvore de decisão do dossiê 2 cai em "agentic search, pule o
índice vetorial". Zero infra nova.


---

O que foi decidido a partir disto — as seções 3 a 6, incluindo os limiares de
diagnóstico (§5) e as duas leis de manutenção (§5.1) — está em
[[arquitetura-decisoes-e-leis-de-manutencao]].
