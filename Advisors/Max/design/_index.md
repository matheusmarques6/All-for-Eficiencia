---
tipo: indice
modulo: design
assunto: mapa-do-design
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L6859-8065 (transcrição), L8066-8362 (slide), L8740-8748 (slide de upload no módulo deliverability)"
status: rascunho
---

# O que tem aqui

O módulo de design do curso: por que design importa, três princípios, doutrina
por seção de email, transições, e os dois procedimentos de ferramenta (Figma e
upload). Treze notas.

O módulo é onde o corpus mais se contradiz por seção. Doze slugs `design-*` têm
entrada em [[_conflitos-completo#design]]; `design-cta-por-produto` e
`design-html-vs-imagem` ficam em [[_conflitos]], nas duas seções transversais.
Antes de responder qualquer pergunta com número aqui, abrir [[_numeros]] e
[[_conflitos]].

# As notas

| Nota | O que responde | Registro |
|---|---|---|
| [[por-que-design-importa]] | os seis argumentos do deck; o número 3x; a analogia do terno | transcrição + slide |
| [[o-email-tem-um-trabalho-so]] | "Get the click"; as 7 regras de botão e CTA | transcrição + slide |
| [[principio-ease-of-click]] | zombie mode, silver platter, botão grande/claro/centralizado/above the fold | transcrição + slide |
| [[principio-skimmability]] | 2-4 segundos; simplicidade, seções, destaques, infográficos | transcrição + slide |
| [[principio-branding]] | congruência entre canais; branded graphics / correct fonts / congruent styling | transcrição + slide |
| [[secao-hero]] | a seção obrigatória; 75% do esforço; os 4 itens above the fold | transcrição + slide |
| [[secao-bridge]] | o wild card; os 7 conteúdos possíveis; default = infográfico | transcrição + slide |
| [[secao-product]] | CTA por produto; CTA geral no fim; quantidade de produtos | transcrição + slide |
| [[secao-footer]] | universal; botões de categoria como último catch-all | transcrição + slide |
| [[transicoes]] | os 4 métodos (só na fala); a autocorreção sobre "blocky" | transcrição |
| [[emails-baseados-em-imagem]] | a posição contra o consenso de HTML nativo; a prova Ridge | transcrição |
| [[upload-do-design]] | procedimento datado: slice → comprimir → subir → links e alt text | transcrição + slide |
| [[figma-para-email]] | procedimento datado: frames, grupos, 600 de largura, slice tool | transcrição + slide |

Fora desta pasta, do mesmo módulo:
[[doutrina/roubar-e-o-metodo]] (o "#1 tip: STEAL", as fontes de swipe e as marcas
citadas — L7851-8007 e L8309-8348) e [[doutrina/o-processo-de-criacao]].

# As quatro seções do email

| Seção | Obrigatória? | Função | Regra dura | Onde conflita |
|---|---|---|---|---|
| **Hero** | **Sim** — "every email is going to have a hero section" (L7238) | vender sem exigir rolagem; 75% do esforço (L7258 / L8235) | 4 itens above the fold: clear headline · strong graphic · clear value prop · clear button (L8243-8246) | botão no topo: slide manda sempre (L8135, L8154), fala diz 75% dos emails (L7027-7029) |
| **Bridge** | Não — "Bridge is optional" (L7238) | apoiar a hero e fazer ponte para o produto (L8259-8260) | em geral, usar infográfico (L7404 / L8271) | quantidade: fala admite 0 ou 1 (L7368-7372), slide admite 2 (L8260); "most will" (L8229) vs "optional" (L7238) |
| **Product** | Não — "product section is optional" (L7238) | destacar produtos, que podem ser categorias (L8277) | (1) CTA individual por produto (L7458) · (2) sempre fechar com CTA geral, +25% de cliques (L7482 / L8287) | CTA por produto: slide aceita "or underlines product titles" (L8282); quantidade de produtos: 1 · "not that many" · 8 · "just test it" (L7488-7494) |
| **Footer** | **Universal** — igual em todos os emails (L7500 / L8293) | último catch-all: botões de categoria para quem rolou tudo e não achou nada (L8296) | botões no footer, e footer branded (L7506, L7526) | — (nenhuma contradição declarada) |

Transições ligam uma seção à seguinte e não são seção: ver [[transicoes]].

# Rota rápida

- pergunta de **botão** → [[o-email-tem-um-trabalho-so]] → [[principio-ease-of-click]]
- pergunta de **layout / o que vai em cada parte** → a tabela acima → a nota da seção
- pergunta de **"por que design"** → [[por-que-design-importa]]
- pergunta de **ferramenta** → [[figma-para-email]] ou [[upload-do-design]] —
  sempre avisando que é datado e que o upload é demonstrado no **Omnisend**, não
  no Klaviyo (L8009 vs L8044)
- pergunta de **imagem vs HTML** → [[emails-baseados-em-imagem]]

# O que este módulo não cobre

Nenhuma cor, nenhuma paleta, nenhuma tipografia com valor prescrito. Nenhum
tamanho de arquivo alvo além do teto de slice. Nada sobre dark mode, acessibilidade
além do alt text, ou clientes de email específicos. Nada sobre GIF ou vídeo em
email além da menção de plugin (L7797). Ver [[_cobertura]].
