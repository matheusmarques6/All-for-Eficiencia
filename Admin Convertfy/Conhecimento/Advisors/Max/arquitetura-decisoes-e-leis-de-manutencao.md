---
tipo: relatorio
status: aprovado
data: 2026-09-06
fonte: dossiê "Clones de IA de Pessoas Reais" + dossiê "Como organizar grandes corpora para agentes"
---

Segunda metade do relatório de internalização que decidiu a arquitetura do advisor Max: o que vai ser implementado e em que ordem, o que **não** vai ser implementado e o gatilho que mudaria isso, os limiares que dizem se está funcionando (§5), as duas leis de manutenção aprendidas construindo (§5.1) e o que é preciso do lado humano quando o conhecimento chegar. A numeração das seções é a do documento original. A razão medida de cada decisão está em [[arquitetura-diagnostico-e-o-que-aprendi]].

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
