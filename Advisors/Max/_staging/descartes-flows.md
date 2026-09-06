# Descartes do módulo `flows`

Linhas da faixa L1307-4186 que **não** entraram nas notas, e o motivo. O
critério é o do `_brief`: ruído de ASR, CTA comercial, placeholder morto,
título que mente.

## 1. CTA comercial e autopromoção

| Linhas | O que é | Motivo |
|---|---|---|
| L3417-3424 | Bio do Max + quatro links de rede social | Não é doutrina. O `$100M` de L3419 foi para `numeros-flows.md` como credencial disputada, não como fato. |
| L3426-3429 | "Sign Up For Klaviyo For Email Marketing" — link de afiliado com "free to start and takes 2 minutes to setup" | CTA comercial. O `$200M` de L3428 está registrado em `numeros-flows.md` e em `conflitos-flows.md` justamente porque a origem é promocional. |
| L3458-3465 | "Join My Email Course / Community" — 30+ módulos, 250+ templates, calls semanais, link Skool | CTA comercial puro. Os números não são especificação de nada. |
| L4178-4185 | "That's It For This One!", "Want More Help?", consultoria para marcas de $50k/mo | Fechamento comercial. O piso de $50k/mo entrou em `numeros-flows.md` por ser número declarado, mas não sustenta nenhuma nota. |
| L2614-2616 | "feel free to message me or the group as well and we'll get you get a fix for you" | Oferta de suporte, não instrução. |

## 2. Placeholders mortos — o slide promete e não entrega

| Linha | O que promete | O que tem |
|---|---|---|
| L3509 | "**Base Strategy:**" — o diagrama que reconciliaria as duas sequências do welcome | nada; a linha seguinte é o próximo heading |
| L4057 | "**Segment Definition for 90 Day Winback Flow:**" | nada; a definição real está em L5589, fora da faixa |
| L3642, L3663 | "**Email Example:**" do site abandon | vazio |
| L3700, L3721, L3742, L3763 | "**Email Example:**" do browse abandon | vazio |
| L3817, L3838, L3859, L3881 | "**Email Example:**" do cart/checkout | vazio |
| L3948, L3966 | "**Email Example:**" do post-purchase | vazio |
| L4170, L4176 | "Example of Text Based sale email winner:" e "Example of categories performing better:" | vazio |
| L3402 | `![][image1]` no Sunset Flow | **não é placeholder morto**: a referência resolve para a L9545, onde está `[image1]: <data:image/png;base64,…>` — PNG 624×169 com o print do segmento `WC \| Sunset`. Único marcador de imagem em toda a faixa L1307-4186. Lido e transcrito em [[sunset]] |

Todos os 14 slots vazios estão declarados nas notas correspondentes, na seção
`# O que o corpus não diz`. O fato de o welcome ser o único flow do deck **sem**
slots "Email Example:" está registrado em [[welcome-templates]].

## 3. Links repetidos de gamma

L1311, L2328, L2435, L2620, L3224, L3307 — a mesma URL
(`gamma.app/docs/Email-Flows-nccnz3vebo4vyy1`) repetida no cabeçalho de cada
seção de flow. Descartada como boilerplate. **Exceção:** L3400 aponta para um
deck diferente (`Sunset-Flow-v13borkcrsurvpv`) e por isso está citada em
[[sunset]] — é a única evidência de que o Sunset Flow tinha material.

Mesma coisa para os marcadores `\# File-<nome do flow>` (L1314, L2331, L2438,
L2623, L3026, L3227, L3310): metadado de arquivo de transcrição, não conteúdo.

## 4. Ruído de ASR

Descartado como texto, mas registrado onde afeta a leitura de um artefato.

| Linha | ASR | Provável original | Onde afeta |
|---|---|---|---|
| L1448 | "you've done, Dan, that if you're sending campaigns regularly" | frase truncada, sentido perdido | argumento sobre campanhas no welcome |
| L1818 | "an R story email" | *our story email* | nome do filler — corrigido em [[welcome-fillers]] com o nome do slide |
| L2152 | "Mints versus facts" | *Myths vs Facts* (confirmado em L3565) | catálogo de fillers |
| L2363 | "like a card abandoned" | *cart abandoned* | comparação de intenção em [[site-abandon]] |
| L2401, L2403, L2429, L2496 | "side abandoned", "side of band", "side of band and flow", "side of Bain and Flow" | *site abandon* | nome do flow |
| L2417 | "velvet cowder yard" | *Velvet Caviar* — o mesmo exemplo reaparece identificado em L5198 | exemplo do site abandon E2 |
| L2911 | "Still 1x% off" | provavelmente *10% off* | valor de desconto — mantido verbatim em `numeros-flows.md` com marca de corrupção |
| L2987 | "For Bannon checkout" | *for abandoned checkout* | bloco dinâmico |
| L2995-2997 | "With this row collection and row alias. Alias." | repetição de ASR | fórmula do checkout — a versão boa está no slide L3903-3904 |
| L3160-3162 | "You know your brand / post-purchase flow as within 14 days" | frase truncada entre dois parágrafos | escopo temporal do post-purchase — confirmado pelo slide L3971 |
| L2080-2082 | "Baby carriers. Oopsies." | ele se corrigindo em voz alta | exemplo de filler |
| L2817 | "Sorry, I got really excited there." | comentário fora de conteúdo | exemplo do cart E2 |
| L3120 | "You can get more aggressive." repetido três vezes na mesma linha | gagueira de ASR | post-purchase |

**Erros de digitação do slide, mantidos verbatim nas notas:** "Ilusing '…' or
exlcuding" (L4160), "If it's an an educational email" (L4134), "Include relevant
shipping information (should as free shipping threshold)" (L3814), "Make sure to
include individual buttons for each product you should" (L3639), "Some welcome
flows can we 3-4 emails" (L3502), "which will take the customer top the product
page" (L3775). São artefato: não corrigidos, marcados como do original onde a
leitura fica ambígua.

## 5. Conteúdo que pertence a outro módulo

Aparece na faixa de flows mas é assunto de outra pasta. Não escrito aqui, só
sinalizado.

| Linhas | Assunto | Vai para |
|---|---|---|
| L1318-1368, L3469-3484 | O argumento de CAC do pop-up | `list-growth/` — usado em [[welcome]] só como racional do flow |
| L3435-3444 | Definição geral de "o que são flows" e a divisão 50/50 flow vs campanha | `doutrina/` — o número está em `numeros-flows.md` |
| L3446-3452 | "Already Have Flows?" — diagnóstico de flows desatualizados | `doutrina/` |
| L2367, L3384-3386 | Frequência de campanha (3-4/semana, 3x/semana) | `campanhas/` — números registrados, conflito aberto |
| L5057, L5589 | Definição completa do segmento de winback | `campanhas/` (segmentação) — citada em [[winback]] por necessidade |
| L2512-2522, L2743-2745 | Doutrina de above the fold e hierarquia de seção | `design/` — o recorte de abandono ficou em [[browse-abandon]] |
| L3148 | Bloco "recommended Klaviyo products" | `design/` ou procedimento — sem instrução no corpus |

## 6. O que foi mantido apesar de parecer descartável

- **A hesitação "days 30 through 60-ish, 21 through 60-ish"** (L3233-3235). Não
  é ruído: é ele se corrigindo sobre uma especificação. Registrada em
  [[replenishment]] e em `conflitos-flows.md`.
- **"Because I'm impatient"** (L3322). Parece piada, mas é o racional inteiro de
  por que o winback usa segmento em vez de metric. Mantido em [[winback]].
- **"For whatever reason, Klaviyo, their base templates, they labeled them
  wrong"** (L2683). Acusação à ferramenta que ele recomenda e vende por link de
  afiliado. Mantida em [[cart-checkout-abandon]] exatamente por isso.
- **"Trust me. We've tested this."** (L2901-2905). É a única justificativa que
  ele dá para dois text-based em quatro emails. Mantida com a fraqueza à vista.
- **"This is what we've always done"** (L2991). Admissão de que a diferença
  entre os blocos dinâmicos é histórica, não técnica. Mantida em
  [[conteudo-dinamico-klaviyo]].

## 7. Conteúdo duplicado entre o deck de flows e o deck de otimização

Verificado linha a linha com `grep -n` e `sed -n`. Quatro dos cinco testes de
A/B da seção "Flow Optimization" (L4115-4177) aparecem **palavra por palavra**
no deck de otimização, no bloco L9151-9180.

| Bloco | Deck de flows | Deck de otimização | Diferença |
|---|---|---|---|
| Flow Time Delays | L4141-4145 | L9176-9180 | nenhuma |
| SLs and PTs | L4153-4162 | L9165-9174 | uma: L4160 "**Ilusing** '…' or exlcuding" vs L9172 "**Using** '…' or exlcuding" — o deck de flows tem um typo a mais |
| Graphic vs Text Based | L4164-4170 | L9151-9157 | nenhuma |
| Promoting Categories vs Products | L4172-4176 | L9159-9163 | espaçamento apenas (L9162 tem espaço duplo) |

**Por que isso importa.** Sem este registro, alguém que encontre a mesma regra
em `flows/` e em `otimizacao/` pode tratar as duas ocorrências como confirmação
independente. Não são: é o mesmo slide reaproveitado em dois decks. Uma regra
duplicada não é uma regra mais sustentada.

O catálogo dos quatro testes **não foi escrito** em [[otimizacao-de-flows]] — a
nota aponta para `otimizacao/` e guarda só as âncoras.

**O que NÃO é duplicado** e por isso permaneceu na nota de flows:

| Bloco | Linhas | Verificação |
|---|---|---|
| "The Cons of Flow Optimization & A/B Testing" + "30-50+ automated emails" | L4117-4124 | `grep -n "30-50+ automated emails"` → só L4119 |
| "Long-Term Optimization Strategy" — campanha como campo de teste, migrar vencedoras, "Don't reinvent the wheel!" | L4126-4137 | `grep -n "testing ground"` → só L4129; `"put full campaigns that perform well"` → só L4132; `"reverse risk"` → só L4136 |
| "Long Form vs Short Form" | L4147-4151 | `grep -n "Long Form vs Short Form"` → só L4147 |
| "especially in flows like abandonments when people have objections" | L4150 | ocorrência única no bruto inteiro |

Nota lateral: "Don't reinvent the wheel\!" (L4137) tem dois quase-homônimos
fora da faixa — "really no need to reinvent the wheel" (L7865) e "Don't reinvent
the wheel, stick with what is proven to work" (L8315) — em outros módulos e
outros contextos. Frases diferentes, não são duplicatas.
