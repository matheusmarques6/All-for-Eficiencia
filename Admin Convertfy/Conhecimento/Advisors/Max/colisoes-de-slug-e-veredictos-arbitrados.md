---
tipo: indice
modulo: auditoria
assunto: colisoes-de-slug-e-veredictos-arbitrados
autor: max-sturtevant
conflitos: [otimizacao-peso-do-basico, doutrina-proporcao-basico-avancado, doutrina-segundos-de-atencao, copy-janela-de-atencao, design-segundos-de-atencao]
status: aprovado
---

Auditoria das colisões de slug da consolidação do registro de conflitos do corpus de Max Sturtevant: a regra de canonicidade aplicada, a tabela das 15 colisões resolvidas entre os arquivos de staging e os dois veredictos arbitrados — o peso do básico e a janela de atenção "antes".


Registro de auditoria da consolidação. Onze arquivos de staging registraram parte dos
mesmos conflitos com slugs diferentes. Regra aplicada: **canônico é o slug do módulo
que possui o registro onde a contradição vive** — quando os dois lados estão no mesmo
deck, é o dono do deck; quando o conflito é transversal por natureza, é `doutrina`.

| Conflito | Slugs concorrentes | Canônico | Situação |
|---|---|---|---|
| Onde testar | `otimizacao-onde-testar` · `flows-onde-testar` | `flows-onde-testar` | veredictos iguais; **os dois lados estão no deck de flows** (L4128 e L4141), o de otimização só carrega a cópia (L9176-9180) |
| Peso do básico | `otimizacao-peso-do-basico` · `doutrina-proporcao-basico-avancado` | `otimizacao-peso-do-basico` | **veredictos divergentes — arbitrado, ver abaixo** |
| Numeração S.C.E. | `copy-numeracao-dos-principios` · `doutrina-sce-numeracao-dos-principios` | `copy-numeracao-dos-principios` | duplicata declarada pela própria unidade de doutrina |
| Benchmark de form | `sms-benchmark-de-form` · `list-growth-benchmark-de-form` | `list-growth-benchmark-de-form` | complementares: as versões de SMS (2-3%, 8-10%) entraram na escada |
| Delay do pop-up | `sms-delay-do-popup` · `list-growth-time-delay` · `fundamentos-time-delay-do-form` | `list-growth-time-delay` | **três slugs para um conflito**; fundamentos era ponteiro puro |
| Exit intent | `sms-exit-intent` · `list-growth-exit-intent` | `list-growth-exit-intent` | complementar: L9240 entrou como terceira versão |
| Checkbox pré-marcado | `sms-instrucoes-de-optin-sao-de-email` · `list-growth-checkbox-preselecionado` | **os dois mantidos** | achados distintos (canal errado × texto que se anula); o defeito compartilhado é descrito uma vez só, em list-growth |
| Narrador da aula de IA | `copy-narrador-nao-e-max` · `doutrina-narrador-da-aula-de-ia` | `doutrina-narrador-da-aula-de-ia` | **colisão nova**; doutrina tem o superconjunto (assinaturas de 9 vídeos) |
| IA como primeiro rascunho | `copy-papel-da-ia` · `doutrina-ia-primeiro-rascunho` | `doutrina-ia-primeiro-rascunho` | **colisão nova**; mesmas linhas, doutrina acrescenta o Gymshark |
| Julgar SL por abertura ou receita | `copy-medir-por-abertura` · `otimizacao-sl-julgar-por-abertura-ou-receita` | `otimizacao-sl-julgar-por-abertura-ou-receita` | **colisão nova**; a versão de otimização acrescenta L8926-8944 |
| Teto do ganho de abertura | `copy-open-rate-limite` · `otimizacao-teto-de-abertura` | `copy-open-rate-limite` | **colisão nova**; o número está no deck de copy (L6805) |
| Credencial de receita | `doutrina-receita-da-agencia` · `flows-receita-da-agencia` | `doutrina-receita-da-agencia` | **colisão nova**; quatro valores num registro só |
| Grafia de nomes de marca | `doutrina-lista-de-marcas` · `design-nomes-de-marca` | `doutrina-lista-de-marcas` | **colisão nova**; a própria unidade de design já apontava para doutrina |
| Cadência de campanha | `campanhas-sweet-spot-de-frequencia` · `flows-frequencia-de-campanha` | `campanhas-sweet-spot-de-frequencia` | **colisão nova**; a entrada de flows era ponteiro |
| Janela de atenção | `doutrina-segundos-de-atencao` · `copy-janela-de-atencao` · `design-segundos-de-atencao` | `doutrina-segundos-de-atencao` | **colisão nova, três vias**; o "antes" de copy e o L8201 de design entraram na tabela única — **veredictos divergentes, ver abaixo** |

**15 colisões resolvidas · 18 slugs redundantes · 126 entradas canônicas.**


## Veredicto arbitrado 1 — peso do básico

**A divergência:** a unidade de `otimizacao` classificou L8764 como `resumo do módulo` e
**recusou-se a resolver** ("as quatro versões são dele, e o ponto é o mesmo em qualquer
número"). A unidade de `doutrina` classificou L8764 como `slide (lista do módulo)` e
**resolveu por precedência** ("está nos dois slides (…) como o conflito é sobre número,
vale o slide").

**A arbitragem, com o bruto aberto:**

1. **L8764 não é slide GAMMA.** O deck de otimização começa em L9110 (`# GAMMA
   OPTIMIZATION`). L8760-8769 é o bloco de bullets da página do curso, e termina em
   L8769 com "Link to document in video: [gamma.app/docs/AB-Testing-Optimization…]" —
   ele **aponta para** o deck. A classificação de `otimizacao` está certa; a de
   `doutrina` está errada. Não são "dois slides": é o deck e o resumo do deck, uma
   fonte contada duas vezes.
2. **Mas isso não sustenta o "não resolver".** Sobra um slide (L9120-9121, 90/10) contra
   duas falas (L8778-8780 "80, 90%" e L9098 "80%"). Conflito de número entre registros
   → a precedência do [[mapa-do-corpus-do-max]] se aplica → **vale o slide**.
3. **E há um desempate mais forte que a precedência.** O bloco de fala L8762-9109 é
   classificado **`outro-provavel`** por [[mapa-da-autoria]] (bloco 40): "obviously" 9×, "at
   the end of the day" 3× e **zero** "I recommend" / "my favorite" / "I like to" em
   3.121 palavras, mais o fecho coletivo "feel free to hit us up" em L9108. A saudação
   "Yo, yo" de L8774 **não conta** — o critério caiu (§5). **As duas
   versões que dizem 80% não são citáveis como fala do Max.**

**Veredicto: 90/10.** Registrado em `otimizacao-peso-do-basico`, com as versões de 80%
preservadas e marcadas como atribuição duvidosa. Nenhuma das duas unidades tinha os
três elementos — uma acertou o registro e errou a conclusão, a outra errou o registro e
acertou a conclusão pelo motivo errado.


## Veredicto arbitrado 2 — a janela de atenção "antes"

**A divergência:** a unidade de `doutrina` afirmou que o valor "antes" **não conflita**
("Os três registros dizem 5-10 segundos (L4703, L5500, L6516). Quem responder não deve
inventar divergência aí"). A unidade de `copy` registrou que **conflita** (slide fixa
5-10; a fala hesita entre 3-5 e 5-10).

**A arbitragem:** `copy` está certa e `doutrina` trabalhou com um conjunto incompleto.
L5891 diz, verbatim: "used to be **three to five**, five to 10 maybe". É uma quarta
linha, e ela oferece 3-5. A afirmação de que os três registros concordam é verdadeira
para as três linhas que doutrina listou e falsa para o corpus.

**Veredicto: o "antes" conflita**, com a ressalva de que a única versão discordante
(L5891) está no bloco L5867-6082, classificado `outro-provavel` — ou seja, é a de
atribuição mais fraca. Registrado assim em `doutrina-segundos-de-atencao`. A instrução
"não inventar divergência aí" foi removida; a instrução "não converter em faixa única"
permanece.


