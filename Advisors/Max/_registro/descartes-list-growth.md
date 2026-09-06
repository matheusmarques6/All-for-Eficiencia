# Descartes — list-growth

O que existe na faixa L523-1306 e **não** entrou em nenhuma nota, com o motivo.

Total descartado: ~60 linhas de conteúdo (contando só linhas não vazias), das
quais ~50 estão num único bloco contíguo, L860-958.

---

## L860-958 — o maior bloco de contaminação do arquivo

Cinquenta linhas entre o fim da aula 4 (Klaviyo desktop, termina em L858) e o
início da aula 5 (Alia, começa em L960). **Nada nesse bloco tem relação com email
marketing, e-commerce ou com o curso.** É material de outra sessão de gravação
que vazou para dentro do arquivo.

### Composição

| Categoria | Linhas | Ocorrências |
|---|---|---|
| Pangrama de teste de ASR — "The quick brown fox jumps over the lazy dog." | 864, 870, 886, 888, 894, 898, 902, 908, 914, 916, 922, 928, 932, 934, 938, 952, 956 | 17 |
| Teste de microfone / de gravação | 860, 868, 872, 876, 882, 918, 924, 930 | 8 |
| Filler de ASR sem conteúdo (um/er/[unintelligible]/[laughter]) | 866, 874, 880, 890, 896, 920, 950, 958 | 8 |
| Conversa doméstica ou social | 878, 884, 900, 904, 906, 926, 936, 946, 948 | 9 |
| Fala corporativa genérica, sem assunto | 862, 892, 954 | 3 |
| Timestamp órfão — `00:00:15` | 910 | 1 |
| Linha em mandarim | 912 | 1 |
| Release note de produto sem relação | 940 | 1 |
| String de interface | 942 | 1 |
| Frase religiosa | 944 | 1 |

Soma: 50 — todas as linhas não vazias do bloco estão classificadas.

### As linhas que merecem registro individual

- **L862** — "you can have all the ideas in the world, but if you don't actually
  execute on them, then it's just a dream" — motivacional genérico. Tentador de
  citar como doutrina do Max; **não é**. Está no meio de testes de microfone, sem
  contexto de aula e sem relação com list growth. Não atribuir a ele.
- **L892** — "Hello. I am here to help you with your transcription needs. Um,
  please feel free to send me your files" — fala de um **serviço de
  transcrição**, não do Max. Evidência de que o bloco inteiro é de outra sessão.
- **L900** — "Hey, um, what did you want for dinner tonight?" — doméstico.
- **L910** — `00:00:15` — timestamp solto, sem transcrição associada.
- **L912** — "嗯, 我是想问一下, 就是关于那个, um, 之前的那个会议纪要, [laughter]
  是不是还需要再补充一下细节呀?" — mandarim, sobre ata de reunião. Nenhuma outra
  linha do arquivo nessa faixa está em mandarim.
- **L926** — "could you, uh, pick up some groceries? We're running low on, well,
  eggs and, uh, milk. Also, don't forget the dog food" — doméstico.
- **L940** — "The new design is a major upgrade. It features a sleeker interface,
  [pause] improved navigation, and faster loading speeds" — release note de
  software. **Risco alto de falso positivo**: fala de "design", "interface" e
  "faster loading" perto de uma aula sobre design de pop-up e velocidade de
  carregamento de form. Não é sobre isso.
- **L942** — "Are you sure you want to delete this photo?" — string de UI.
- **L944** — "The first major key to the Kingdom is prayer." — frase religiosa,
  sem qualquer relação com o restante.

---

## L559-561 — contaminação no fim da aula 1

Duas linhas, logo após "Next, we are getting into pop up forms" (L557) e antes do
cabeçalho da aula 2 (L563).

- **L559** — "um, I think, er, well, I need to [unintelligible] the, the
  [laughter] the meeting, okay? Yes, that's right." — filler de ASR, sem
  conteúdo. Mesma assinatura das linhas do bloco L860-958.
- **L561** — "The quick brown fox jumps over the lazy dog." — pangrama de teste.
  É a **primeira** das 18 ocorrências na faixa L523-1306; as outras 17 estão
  todas dentro do bloco L860-958. Ou seja: a contaminação já começa aqui, 300
  linhas antes do bloco grande.

---

## Outros descartes na faixa

### Meta de gravação (o autor falando da própria gravação)

- **L671-673** — "There are 29 solid pop up form examples which I provided for
  you, which I need to actually update that link. Let me do that real quick.
  Okay, so I just updated this, so it's provided for you." O número (29) e a
  existência do swipe file entraram nas notas; a narração de estar arrumando o
  link, não.
- **L692** — "So this is kind of how the dashboard looks. [laughter]" — sem
  conteúdo.
- **L716** — "plenty different ways to skin the cat, um, for, if you've never
  heard that phrase" — digressão sobre a expressão.
- **L798-800** — "Why didn't you change? 35. Okay. Can you change size? Do you
  want to change size? There we go." — ele falando com a interface.
- **L828** — "I'm just going to clone this for ease of this video, making it a
  little bit faster" — logística da gravação.
- **L1078** — "To save time, I'm not going to go through desktop one by one" —
  idem.

### CTA comercial

- **L1028-1029** — "you can book a call with us using the link below. We've
  worked with over 279 figure e-commerce brands... you can book a call below or
  go to our website at wellcopy.net" — pitch de agência. Os números foram para
  [[_numeros-completo#Métodos de captação e o case da agência]] marcados como registro comercial; o CTA não entrou em
  nota.
- **L1082-1083** — "watch this next video and I will see you there. Thank you for
  watching this video. Catch you in the next one." — encerramento de YouTube.
- **L34** (fora da faixa, citado só para contexto do conflito Alia/Klaviyo) —
  link de afiliado do Omnisend com 30% off. Não pertence a este módulo.

### Placeholders e seções vazias do slide

- **L1300** — `# Klaviyo Pop-Up Form Creation` — cabeçalho sem nenhum conteúdo
  abaixo.
- **L1302-1304** — `# Alia Pop-Up Form Creation` seguido de `[need]` —
  **placeholder morto declarado**. O deck admite que o material não existe.
  Registrado em `alia-e-a-alternativa` e no `_index` como lacuna, não como
  descarte silencioso.
- **L1288-1298** — "Great Examples": quatro legendas de imagem (Quiz,
  Micro-Commit, Micro-Commit, The Classic) sem as imagens. As legendas entraram
  em `os-tipos-de-form` porque são evidência do conflito 4 vs 5; as imagens não
  existem no arquivo.
- **L1305** — "List Growth" solto, rodapé do deck.
- **L1085-1089** — "GAMMA LIST" seguido de "List Growth" duas vezes (L1087,
  L1089), cabeçalho do deck.

### Links repetidos

- **L527, L565, L607, L681, L962** — o mesmo link do gamma
  (`gamma.app/docs/List-Growth-2vvjfonhsa7j83j`) no topo de cada aula. Registrado
  uma vez na `fonte:` das notas, não cinco.
- **L567** — link do Figma do "Pop-Up Swipe File", no cabeçalho da aula 2. É um
  **segundo** swipe file, distinto das "29 solid pop-up form examples" do Drive
  (L671, L1290) que entraram nas notas. Nenhuma nota o menciona; ele não é citado
  em lugar nenhum da transcrição, só existe como link de cabeçalho. Fica aqui
  registrado como lacuna, não como conteúdo descartado.
- **L988-990** — "Link do gamma :" vazio, seguido do título do vídeo do YouTube.
  É a evidência de que a aula 6 não tem slide correspondente.

### Trechos de execução puramente estética

Descartados por serem ajuste fino de tela sem regra generalizável — ele mesmo diz
"you can play around with the spacing as you want" (L814):

- **L718-722** — radius, padding, margins, fontes do input field.
- **L744, L766-770, L796, L802-804** — ajustes de cor, centralização e
  alinhamento durante a montagem.
- **L842-850** — trocas de imagem e espaçamento na versão desktop.
- **L1045, L1059-1061** — ajustes de tamanho e padding no vídeo do YouTube.
  Atenção: **L1044 e L1058 não são descarte** — L1044 traz a datação da
  recomendação de copy ("at least right now this is what's working") e L1058 traz
  a frase do quiz; ambas estão em `copy-do-form`. Os valores de fonte 18 e altura
  54 (L1060) estão em [[_numeros-completo#Especificação do form]].

Os **valores** que saíram desses trechos (tamanhos de fonte, padding, altura de
botão) estão em [[_numeros-completo#Especificação do form]]; a narração dos cliques, não.
