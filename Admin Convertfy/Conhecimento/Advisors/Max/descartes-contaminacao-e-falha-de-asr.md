---
tipo: indice
assunto: procedencia
autor: max-sturtevant
status: aprovado
---

Parte do arquivo bruto `CONTEUDO BRUTO/max.md` não é curso: são cerca de 50
linhas de outra gravação coladas por erro dentro da AULA 4 de List Growth
(L860–958), pangramas e testes de microfone nas emendas entre aulas, e um loop
de ASR em L4480–4488 que destruiu a enumeração falada dos pilares de conteúdo.
Esta nota lista essas faixas linha a linha, com o motivo do descarte e o que
dá para recuperar em outro lugar do corpus.

# Descartes por ruído de gravação e falha de ASR

O que não entra em nota nenhuma, com linha e motivo. Os descartes por venda e
por placeholder estão em [[descartes-cta-comercial-e-placeholders]].

## Contaminação — L860–958

Cerca de 50 linhas inseridas no meio da AULA 4 de List Growth (walkthrough de
pop-up no Klaviyo), entre o fim da explicação de compressão de imagem (L858) e
o título da AULA 5 (L960). Não têm relação com o curso. Composição verificada:

- 17 repetições de `The quick brown fox jumps over the lazy dog.` — pangrama
  de teste de microfone (L864, 870, 886, 888, 894, 898, 902, 908, 914, 916,
  922, 928, 932, 934, 938, 952, 956).
- Testes de gravação: "Hello, is this recording working?" (L860), "Is this
  working? Okay, great." (L868), "Is this a real microphone test?" (L872),
  "Is the microphone on?" (L882), "Is it okay if I start the recording now?"
  (L924).
- Conversa doméstica: jantar (L900), compras de mercado com ovos, leite e
  ração de cachorro (L926), "Hey what's going on?" (L936).
- Uma linha em mandarim sobre ata de reunião (L912).
- Timestamp órfão `00:00:15` (L910).
- Release note de produto sem relação nenhuma com email: "The new design is a
  major upgrade… sleeker interface, improved navigation, faster loading
  speeds." (L940). **Armadilha:** lida fora de contexto parece falar de design
  de email. Não fala.
- String de UI: "Are you sure you want to delete this photo?" (L942).
- Frase religiosa solta: "The first major key to the Kingdom is prayer."
  (L944).

Motivo: material de outra gravação, colado por erro. Zero conteúdo do curso.

## Ruído de teste fora do bloco principal

Mesmo tipo de contaminação, em doses menores, nas emendas entre aulas:

| Linhas | Onde | Conteúdo |
|---|---|---|
| L150–156 | fim da AULA 4 de fundamentos | preço/`[unintelligible]` + 2 pangramas + hesitação |
| L164 | logo após `Transcrição da Aula :` da AULA 5 | 1 pangrama antes do conteúdo real começar em L166 |
| L198–210 | fim da AULA 5 | 3 pangramas + espera de trem + testing, testing |
| L231–235 | fim da AULA 6, antes de `# GAMMA` | 2 pangramas + "hoje vamos falar de coding" |
| L559–561 | fim da AULA 1 de List Growth | hesitação sobre reunião + 1 pangrama |

Motivo: TTS/teste de microfone. Nenhuma delas contém afirmação sobre email
marketing. Total de pangramas no arquivo inteiro: 26.

## Falha de ASR — L4480–4488

**Correção de mapa: o loop está em L4480–4488, não em L4293–4301.** L4293–4301
é conteúdo íntegro (revolving door de novos subscribers, graphic vs text
based).

Cinco linhas de fala — L4480, 4482, 4484, 4486 e 4488, intercaladas por linhas
vazias — em que o ASR travou repetindo *"If you're going to include those
testimonials"*: 7, 10, 11, 10 e 12 vezes na mesma linha, com truncamento no
fim de cada uma. O trecho fica entre L4478 (fim da explicação do pilar de
social proof) e L4490, onde a fala retoma já nos percentuais ("20%
educational, 20% social proof, 20% product, 20% community branded, one sale,
two sale emails, so 20%"). O que se perdeu é a enumeração falada dos
pilares de conteúdo restantes e o critério de uso de testimonials.

Recuperação parcial: os bullets em **L4424–4430** listam os cinco pilares
(Educational, Social Proof, Community / Branded, Product or Collection
Highlights, Sales) com um exemplo cada. Use os bullets. O racional falado
sobre testimonials não existe no corpus — se a pergunta for essa, recusar.

