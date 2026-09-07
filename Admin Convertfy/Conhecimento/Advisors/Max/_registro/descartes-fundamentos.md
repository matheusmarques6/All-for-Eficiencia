---
status: aprovado
---

# Descartes — fundamentos

O que existe em L1-522 e **não** entrou em nenhuma nota, com o motivo.

Total: **17 linhas** de conteúdo não vazio descartadas integralmente, das quais 15 são
ruído de gravação em quatro blocos. Consistente com o registrado em `_fontes.md`
(L117-120).

---

## Ruído de gravação — testes de microfone e TTS

Quinze linhas em quatro blocos, todos em fronteira de aula. Nenhuma tem relação
com email marketing. O padrão é o mesmo do bloco maior do arquivo (L860-958,
documentado em `descartes-list-growth.md`): pangramas alternados com frases
soltas de teste de voz.

### L150-156 — fim da AULA 4 (Klaviyo walkthrough)

| Linha | Conteúdo | Categoria |
|---|---|---|
| L150 | "The price has gone up significantly since last month, um, do we really need to proceed with this \[unintelligible\]?" | frase de teste — soa comercial, mas não tem referente no curso; nenhum preço é discutido em nenhum ponto do módulo |
| L152 | "The quick brown fox jumps over the lazy dog." | pangrama |
| L154 | "The quick brown fox jumps over the lazy dog." | pangrama |
| L156 | "um well I think we should \[unintelligible\] just like get started right now." | frase de teste, sem tópico |

**Atenção a L150.** É a linha mais perigosa da faixa: fala de preço subindo, e o
módulo imediatamente anterior recomenda duas ferramentas pagas. Tentador de ler
como comentário sobre o custo do Klaviyo. **Não é.** Está no bloco de teste de
voz, não tem sujeito, e o corpus inteiro não traz um único preço. Não atribuir.

### L164 — dentro da AULA 5, antes do conteúdo

| Linha | Conteúdo | Categoria |
|---|---|---|
| L164 | "The quick brown fox jumps over the lazy dog." | pangrama, imediatamente após `Transcrição da Aula :` e antes do conteúdo real, que começa em L166 |

### L198-210 — fim da AULA 5 (métricas)

| Linha | Conteúdo | Categoria |
|---|---|---|
| L198 | "um, I think, well, I'm not really sure \[unintelligible\] whether I should be here today." | frase de teste |
| L200, L202, L208 | "The quick brown fox jumps over the lazy dog." | pangrama (3×) |
| L204 | "Is it okay if I sit here? Um, I'm just waiting for the, er, the train." | frase de teste, fora de tópico |
| L206 | "um well I think that the project should um be reconsidered because er it might lead to some \[unintelligible\] issues later on." | frase de teste corporativa genérica, sem referente |
| L210 | "Is this working? Um, er, well, testing, testing. \[laughter\]" | teste de microfone explícito |

### L231-235 — fim da AULA 6, antes do bloco `# GAMMA`

| Linha | Conteúdo | Categoria |
|---|---|---|
| L231, L235 | "The quick brown fox jumps over the lazy dog." | pangrama (2×) |
| L233 | "Hey what is up guys, um today we are going to be talking about, er, some coding stuff. Well, anyway, let us, \[unintelligible\] begin." | abertura de vídeo de **outro assunto** (programação). Prova de que o bloco é de outra sessão de gravação |

---

## Ruído de ASR dentro do conteúdo

Não descartadas — as linhas entraram nas notas — mas o trecho ruidoso não foi
citado, ou foi citado com a marca do ruído.

| Linha | Ruído | Leitura correta |
|---|---|---|
| L9 | "seamless checks" | *stimmy checks*, como o slide grafa em L248 |
| L12 | "Ads are just way too expansive" | *expensive* |
| L78 | "typically you want to send that off" | *turn that off* |
| L92 | "Side Abandon" na lista de flows da conta | *Site Abandon*, cf. glossário L405 |
| L94 | "you'll be able to see the revenue, oops, revenue, revenue per recipient" | repetição de fala |
| L174 | "or 60% campaigns, 40% follows" | *flows* |
| L196 | "that we are going to be teaching you to do for via." | frase truncada; o fim da aula 5 não fecha |
| L9, L22 | "Newtonic" (L9) / "new tonic" (L22) | mesma marca, duas grafias em aulas diferentes |

**L148** — `"here if you want custom reports to be sent to your email, and then"`.
Duplicata parcial de L144, cortada no mesmo ponto. Fragmento de ASR, sem
conteúdo novo. **Descartada.**

**L38** — `"and everything there"`. Fragmento órfão que fecha a aula 3 sem sujeito
nem verbo. **Descartada.**

---

## Filler de gravação — não citados

| Linha | Conteúdo |
|---|---|
| L68 | "\[cough\]" |
| L82 | "da da da da da" |
| L108 | "\[cough\] excuse me" |
| L112 | "\[laughter\]" |
| L124 | "\[sigh\] Quick water break" |
| L142 | "Let's take there was an error there" — a página de benchmarks do Klaviyo deu erro na tela. **Não descartado**: registrado em [[dashboard-do-klaviyo]] como limite da demonstração |

---

## CTA comercial — registrado, não citado como doutrina

Não entram como conselho técnico. Onde a informação é relevante (conflito de
interesse), a nota declara o incentivo em vez de repetir a chamada.

| Linha | Conteúdo | Tratamento |
|---|---|---|
| L22 | "that's what us in this program, Reviewing Your Account, are here to help you with. Le, what do we deem as healthy for you?" | citado em [[os-tres-e-meio-pilares]] como evidência de que o critério dele não é numérico; não como serviço |
| L166-168 | "make sure that you consult with experts. Uh, like us to confirm if like this is what makes sense for your store" | a ressalva de contexto entrou em [[metricas-nucleo]]; o "like us" não |
| L34, L358, L360, L361 | links de afiliado de Klaviyo e Omnisend | **não descartados** — são o conflito de interesse declarado em [[escolha-do-esp]] |
| L13 | "this is why we have brands that are able to scale so fast with us us" | prova social da agência; não é afirmação técnica |

---

## Estrutura do arquivo — marcadores sem conteúdo

| Linha | Conteúdo | Motivo |
|---|---|---|
| L1 | `# INTRO` | marcador estrutural |
| L5, L17, L26, L160, L214 | `link do gamma :` + o **mesmo doc gamma** cinco vezes (L5 com `?mode=doc` no fim; as outras quatro sem) | metadado de origem, não conteúdo |
| L7, L19, L28, L162 | `Transcrição da Aula :` | rótulo de seção |
| L42 | `link do gamma app :` — **campo vazio**, sem URL | registrado em [[dashboard-do-klaviyo]] como defeito do bruto |
| L44 | `Transcrição da Loja :` — rótulo errado, deveria ser "da Aula" | idem |
| L216 | `Transcrição do Audio :` — terceira variante de rótulo no mesmo arquivo | inconsistência de rotulagem |
| L237 | `# GAMMA` | marcador estrutural |
| L239, L241 | "Email Marketing Foundations" duas vezes seguidas | capa do deck, duplicada |
| L243, L291, L293, L351, L368, L370, L382, L384 | títulos de seção do deck | estrutura, sem conteúdo próprio (L364 tratado abaixo) |
| L521 | "Email Marketing Foundations" | rodapé do deck |

---

## Slide sem conteúdo — declarado, não descartado

**L364-366** — a seção "Klaviyo Walkthrough" do deck tem uma frase: *"Watch the
video below for a Klaviyo walkthrough."* Nenhuma especificação, nenhum print,
nenhum passo. O módulo inteiro existe só em `registro: transcricao`.

Isso está declarado no topo de [[dashboard-do-klaviyo]] porque muda como a nota
pode ser usada: não há segundo registro para conferir nenhum passo, e o protocolo
de precedência slide-vence-em-especificação não tem o que aplicar aqui.

---

## O que foi tentado e rejeitado

**"Reviewing Your Account" como produto nomeado (L22).** Aparece uma vez, sem
descrição, sem preço, sem escopo. Não dá para escrever nota sobre o serviço a
partir de uma menção. Fica só como CTA registrado acima.

**A lista de 8 flows em L92.** Ela existe e é verbatim de uma conta real, mas é
inventário de tela, não prescrição de arquitetura — a versão com propósito
declarado está no glossário (L404-411) e a montagem está em `flows/`. Citada em
[[dashboard-do-klaviyo]] apenas como o que a tela mostra, com a nota de que ele a
chama de "recommended flows when just starting out" (L94).
