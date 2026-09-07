---
tipo: relatorio
status: aprovado
data: 2026-09-06
fonte: dossiê "Clones de IA de Pessoas Reais" + dossiê "Como organizar grandes corpora para agentes"
---

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

# 3. O que vou implementar

Na ordem. Cada item existe por causa de um achado da seção 1.

**3.1 `Advisors/Max/persona.md` — o expert reflection.** Quando o
conhecimento chegar, rodo sobre ele uma passagem de síntese no método
Stanford: leio o material do ponto de vista de quem estuda o Max e
escrevo traços, valores, critérios de julgamento recorrentes, o que ele
sempre pergunta antes de responder, o que ele despreza, e — o campo mais
importante — **o que Max nunca diria**. Esse arquivo é o system prompt.
É o item 1.1 e 1.2 cobrados juntos.

**3.2 `Advisors/Max/_INDEX.md` — porta de entrada.** Mesma função do
`_INDEX.md` de Emails: mapa de uma tela, com o caminho de leitura na
ordem. É o que o agente carrega sempre; todo o resto é sob demanda.
Item 1.6.

**3.3 `Advisors/Max/_protocolo.md` — como Max decide.** O equivalente ao
`_protocolo-de-selecao`: os passos que Max percorre para responder,
na ordem, com eliminação antes de ranqueamento. Sem isso, "personalidade"
vira estilo de escrita e o julgamento não se reproduz. É a separação
doutrina (como pensa) × fato (o que sabe), que é o mesmo eixo do
"estilo vs conhecimento" do item 1.3, resolvido em arquivos em vez de
pesos.

**3.4 `Advisors/Max/conhecimento/` — notas atômicas.** Uma ideia por nota,
~700 tokens, slug kebab-case, frontmatter com vocabulário controlado
espelhando o padrão de `eixos/`. Fatiar o material que você mandar por
fronteira de julgamento, não por contagem de caracteres. Item 1.4.

**3.5 Guardrails, escritos dentro do protocolo, não como aviso solto.**
Três regras: (a) responder só com material recuperado suficiente;
(b) quando a pergunta cai fora do corpus, dizer que está fora e o que
falta, nunca preencher — o modo de falha declarado do Stanford foi
justamente "embellishment"; (c) lista explícita de território proibido,
derivada do "o que Max nunca diria" de 3.1. Item 1.7, lado Jill Watson.

**3.6 `Advisors/Max/_casos-de-teste.md` — o eval.** 10 a 20 perguntas
reais com a resposta que Max daria, ou pelo menos o formato e o
julgamento que a resposta precisa conter. Sem isso não há como saber se
qualquer mudança futura melhorou ou piorou. O padrão já existe no vault e
eu reuso.

**3.7 Reaproveitar as ferramentas que já existem.** `valida.py` e
`gera_catalogo.py` já fazem validação de vocabulário e geração de
manifesto para Emails. Se o Max precisar disso, estendo o que existe em
vez de escrever script novo.

# 4. O que NÃO vou implementar, e o gatilho que muda isso

Isto é a parte que economiza mais trabalho, então está explícito:

| Não faço | Por quê | O gatilho que me faria fazer |
|---|---|---|
| Vector DB / pgvector / Pinecone | Corpus navegável no filesystem; 94,5% da fidelidade sem índice; índice fica stale a cada edição de nota | O corpus passar de alguns milhares de notas, ou a busca por nome/estrutura passar a falhar de forma medida |
| Chunking automático + embeddings | As notas já SÃO os chunks, com fronteira melhor que qualquer splitter | Só se entrar material que não dá para curar à mão (transcrição bruta em volume) |
| Fine-tuning / LoRA | Ovadia: pior que RAG para fato. E estilo cabe em prompt | Teste cego mostrar que ainda "não soa como ele" **depois** de persona.md maduro |
| Knowledge graph / GraphRAG | Vence em pergunta global, perde em fato local, custa caro para indexar e reindexar | Perguntas passarem a ser majoritariamente "quais os temas gerais de todo o corpus" |
| Memória entre sessões (Mem0/Zep) | Complexidade antes de existir a dor; benchmarks da área têm disputa metodológica pública | Conversas longas perderem coerência de forma repetida e observável |
| Voz (ElevenLabs) / avatar | Camada de apresentação, não de cérebro | O caso de uso pedir áudio ou vídeo, e o cérebro já estar aprovado |
| Contextual Retrieval (Anthropic) | Serve para chunk isolado que perdeu contexto; nota atômica bem escrita já carrega o seu | Notas passarem a depender de contexto que só existe fora delas |

# 5. Como vou saber se está funcionando

Os limiares que mudam a decisão, definidos antes de medir para não
racionalizar depois:

- **Max erra um FATO** → problema é recuperação. Conserto o caminho de
  leitura (índice, nomes, frontmatter). Não mexo em prompt e não mexo em
  modelo.
- **Max acerta o fato mas soa genérico** → problema é `persona.md`.
  Aprofundo o expert reflection, principalmente o "o que nunca diria".
- **Max opina sobre coisa fora do corpus** → falha de guardrail 3.5(b),
  e é a falha mais grave da lista, porque é indetectável para quem não
  conhece o assunto. É a falha da CarynAI.
- **Max perde coerência em conversa longa** → aí sim é arquitetura de
  memória, e só aí.

# 5.1 Duas leis de manutenção, aprendidas construindo

Não são teoria — cada uma custou uma rodada de correção.

**Corrigir a nota de controle não corrige a nota do assunto.** O limiar
estatístico de teste foi declarado lacuna inexistente, derrubado na revisão de
`_cobertura.md`, e **sobreviveu intacto** em `_numeros-completo.md` e em
`flows/otimizacao-de-flows.md`. Índice e nota são cópias independentes da mesma
afirmação. Toda correção de fato precisa de uma varredura por texto, nunca de
uma edição no lugar onde o erro foi encontrado.

**Não achar não é o mesmo que não existir.** Três vezes o corpus foi declarado
omisso sobre algo que ele cobre: o Sunset Flow (a especificação estava num PNG
em base64 na última linha, invisível a qualquer busca textual), o racional do
S.C.E. (existe, mas o ASR grafa "SDE framework"), e as ocorrências de `consent`
e `carrier` (existem, só não sobre SMS). Antes de escrever "o corpus não diz",
procure em outro registro, em outro módulo, na grafia corrompida e em imagem
embutida. A varredura de falsos negativos derrubou 16 de 275 afirmações de
ausência — e em 12 delas o conteúdo estava em outro módulo.

Corolário de escopo: quase nunca é verdade que "o corpus não diz". Quase sempre
o certo é "**este deck** não diz" ou "**esta aula** não diz". A diferença decide
se o advisor recusa ou responde.

# 6. O que preciso de você quando mandar o conhecimento

1. **Origem do material**: escrito por Max, transcrito dele, ou escrito
   sobre ele? Muda o peso de cada frase na hora de extrair persona.
2. **Para quem Max responde** e em que superfície (chat aqui, agente em
   produção, uso interno). Muda o formato de resposta e o rigor de
   guardrail.
3. **Onde Max discorda do consenso do mercado.** É o que mais separa clone
   de assistente genérico, e quase nunca está no material — costuma
   precisar ser perguntado.
4. **Exemplos reais de resposta dele**, se existirem, mesmo poucos. Viram
   os `_casos-de-teste.md` e são o único jeito honesto de medir estilo.
