---
tipo: indice
assunto: procedencia
autor: max-sturtevant
status: aprovado
---

Todo o corpus de email e SMS marketing atribuído a Max Sturtevant sai de um
único arquivo bruto, `CONTEUDO BRUTO/max.md`, com 9.544 linhas repartidas em
nove módulos e três camadas de registro que às vezes discordam entre si. Esta
nota é o mapa dessa fonte: o que ela é, onde cada módulo começa e termina, que
camada responde o quê, e como verificar qualquer afirmação contra a linha que
a sustenta.

# A fonte

`CONTEUDO BRUTO/max.md`. Arquivo único, **9.544 linhas, 121.344 palavras,
689.468 bytes** (medido com `wc`, não estimado).

Ressalva de contagem: `wc -l` conta quebras de linha e o arquivo não termina
com uma. Existe uma **linha 9.545**, fora do mapa de módulos abaixo — a
definição de referência `[image1]: <data:image/png;base64,…>`, 14.686
caracteres, um PNG de 624×169 embutido. É a imagem que `![][image1]` (L3402)
aponta.

É a transcrição e os decks de um curso de email e SMS marketing para
e-commerce atribuído a Max Sturtevant, fundador da agência Well Copy. Nove
módulos: fundamentos, list growth, flows, campanhas, copywriting, design,
deliverability, otimização, SMS. O material é misto: aulas gravadas
transcritas por ASR, vídeos de YouTube com timestamps, e o texto exportado de
apresentações GAMMA.

**Material de terceiro.** Não foi produzido aqui, não foi licenciado aqui, e
não é para republicação. O corpus em `Advisors/Max/` existe para uso interno
e por isso preserva a procedência linha a linha: toda afirmação sai de uma
linha identificável deste arquivo, e todo descarte está listado em
[[descartes-contaminacao-e-falha-de-asr]] e
[[descartes-cta-comercial-e-placeholders]], com o motivo. Sem esse rastro o
corpus vira opinião anônima e deixa de ser auditável.

# Mapa de módulos

Cada módulo aparece duas vezes: primeiro o bloco de transcrição, depois o
bloco do slide GAMMA. As fronteiras abaixo foram confirmadas uma a uma com
`grep -n "^# "`: 18 marcadores, faixas contíguas de L1 a L9544, sem buraco nem
sobreposição, somando 9.544 linhas. A L9545 (definição base64 acima) não
pertence a módulo nenhum.

| Módulo | Transcrição | Slide GAMMA | Marcador de abertura |
|---|---|---|---|
| Intro / fundamentos | L1–236 | L237–522 | `# INTRO` / `# GAMMA` |
| List Growth | L523–1084 | L1085–1306 | `# LIST GROWTH` / `# GAMMA LIST` |
| Flows | L1307–3403 | L3404–4186 | `# FLOWS` / `# GAMMA FLOWS` |
| Campaigns | L4187–5236 | L5237–5599 | `# CAMPAIGNS` / `# GAMMA CAMPAIGNS` |
| Copywriting | L5600–6500 | L6501–6858 | `# COPYWRITING` / `# GAMMA COPY` |
| Design | L6859–8065 | L8066–8362 | `# DESIGN` / `# GAMMA DESIGN` |
| Deliverability | L8363–8646 | L8647–8759 | `# DELIVERABILITY` / `# GAMMA DELIVERABILITY` |
| Optimization | L8760–9109 | L9110–9212 | `# OPTIMIZATION` / `# GAMMA OPTIMIZATION` |
| SMS | L9213–9260 | L9261–9544 | `# SMS Marketing` / `# GAMMA SMS` |

A distribuição é desigual e isso importa para a cobertura. Flows tem 2.097
linhas de fala; SMS tem 48. Deliverability e Optimization têm decks de 113 e
103 linhas. Onde o bloco é curto, o corpus é raso — não é falha de extração.

# As três camadas

Dentro de cada módulo o material chega em três registros distintos, e os dois
últimos se completam e às vezes discordam.

**1. Bullets de resumo.** Ficam no bloco de transcrição, entre o título da
aula e o marcador de transcrição. São o índice da aula: frases curtas, sem
racional, frequentemente redundantes com a fala que vem logo abaixo.
Exemplos verificados: L5604–5611 (princípios de copy), L5619–5623
(ChatGPT), L4424–4437 (pilares de conteúdo), L8369–8377 (deliverability),
L8522–8526 (warming), L8764–8767 (A/B tests). Redundantes na maioria dos
casos — mas não sempre: L4424–4430 preserva os cinco pilares de conteúdo que
o loop de ASR destruiu na fala
(ver [[descartes-contaminacao-e-falha-de-asr]]).

Ao buscar o marcador, cuidado: ele tem **oito grafias** no arquivo —
`Transcrição do Vídeo :` (29×), `Transcrição da Aula :` (5×), e uma ocorrência
cada de `Transcrição da Aula:`, `Transcrição do Audio :`, `Transcrição do
Áudio :`, `Transcrição de Audio:`, `Transcrição da Loja :` e `Transcrição dos
Texto :` — mais `Transcripts:` (6×) nos blocos vindos do YouTube.

**2. Transcrição falada.** Onde estão o julgamento, a exceção, o porquê, os
exemplos de marca e a voz. **Mas não é sempre a mesma voz:** cerca de 25% da fala do
arquivo é de um segundo narrador e recebe o registro `outro-narrador` — as cinco faixas
estão em [[armadilhas-da-fonte-bruta]] §2. É também onde está todo o ruído: hesitação,
correção no meio da frase, grafia corrompida de nome próprio, e os blocos de
contaminação listados em [[descartes-contaminacao-e-falha-de-asr]]. Vem em dois formatos — texto corrido quebrado em
linhas curtas (aulas próprias) e linhas com timestamp `(00:00)` ou `00:00`
(vídeos de YouTube reaproveitados).

**3. Slide GAMMA.** Onde estão número de tabela, template verbatim, sintaxe
Klaviyo, checklist e listas fechadas. É o registro que fecha especificação. É
também onde estão quase todos os placeholders mortos, porque o export do GAMMA
trouxe as legendas das imagens sem as imagens.

Um caso de camada ausente: **"The Principles of Good Copy" (L5602) não tem
transcrição.** O marcador `Transcrição do Vídeo :` em L5615 está vazio — é o
único marcador vazio do arquivo inteiro — e L5617 já é a próxima seção. Só
existem os bullets L5604–5611 e o link gamma (L5613). Qualquer nota sobre
S.C.E. que precise do racional falado tem de dizer que ele não está no corpus.

# Como usar este mapa

Ao verificar uma afirmação de qualquer nota: pegue a linha citada no
`fonte:` do frontmatter e abra-a no bruto — `sed -n 'X,Yp' "CONTEUDO
BRUTO/max.md"`. Se a linha sustenta a afirmação, a nota está certa. Se a linha
não sustenta, **o erro é da nota**, não do corpus, e a nota se corrige contra a
linha.

Se a linha citada cair dentro de uma faixa de descarte listada nas duas
notas de descarte, a nota não deveria existir: apague-a.

Se a afirmação não tiver linha nenhuma, ela foi inventada. Mesmo destino.

# O resto do mapa

Esta nota cobre o que a fonte **é**. Duas outras cobrem o que ela **não
entrega**:

- [[descartes-contaminacao-e-falha-de-asr]] — contaminação de outra gravação
  (L860–958), ruído de teste nas emendas entre aulas e o loop de ASR de
  L4480–4488.
- [[descartes-cta-comercial-e-placeholders]] — os CTAs comerciais que são venda
  e não doutrina, e os 79 rótulos órfãos e demais placeholders que anunciam
  conteúdo inexistente.
- [[armadilhas-da-fonte-bruta]] — as sete armadilhas de leitura: título que
  mente sobre a ferramenta, os dois narradores, credenciais divergentes, Sunset
  Flow sem aula, grafias corrompidas pelo ASR, deck duplicado e os dois cortes
  de transcrição.
