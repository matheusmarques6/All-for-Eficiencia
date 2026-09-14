---
tipo: estrutura
slug: avelmore-inspecao-antecipada
flow_type: welcome
emails: [1]
objecao_alvo: qualidade percebida do produto — parece bom na foto e decepciona na mão
mecanismo: nomear a objeção dominante e convertê-la em alegação da marca; garantia verificável antes da vitrine; confirmação de terceiro fechando o arco
escopo: geral
loja: avelmore
amostra: montagem sobre marca de calçado de couro, ticket médio (US$ 50-70)
procedencia: nossa
revisado_por: Convertfy
status: aprovada
secoes: [header, hero, body, body, products, cta, reviews, footer]
performance:
---

Serve a intenção [[welcome-1|welcome 1]].

# A estrutura

1. **header** — logo sobreposto à imagem do hero, sem navegação. Por quê:
   assinar sem oferecer saída; menu completo aqui levaria a pessoa embora
   antes do argumento. (O sobreposto é característica da variante de hero,
   não bloco próprio.)

2. **hero** — dispositivo: entrega imediata da promessa. Foto de USO real
   (produto em contexto de vida, close, não estúdio) + boas-vindas + o
   incentivo prometido no opt-in + CTA. Por quê: cumprir o contrato nos
   primeiros segundos — quem abriu para pegar o código acha sem procurar. A
   foto de uso já é o primeiro argumento antes de qualquer texto: o produto
   em condição real, não idealizada.

3. **body** — dispositivo: tese que nomeia a objeção + incentivo como
   fechamento. Um bloco só: headline de tese + 2 parágrafos + o mesmo
   incentivo do hero + prazo vago ("por tempo limitado") + CTA. Por quê: é o
   pivô do e-mail — troca o motivo da compra. A headline pega a dúvida
   dominante da categoria e a transforma em alegação da própria marca
   (convida a inspeção em vez de fugir dela). O incentivo aqui tem papel
   DIFERENTE do hero: lá era entrega da promessa; aqui fecha o argumento —
   primeiro a razão, depois o gatilho. Não é redundância, são dois papéis.

4. **body** — dispositivo: faixa de garantias em 3 ícones (fundo
   contrastante). Remoção de risco: entrega, devolução e um compromisso
   específico da marca que responde à MESMA objeção da tese (não um selo
   genérico). Por quê: converte a alegação do bloco 3 em compromisso
   verificável, ANTES da vitrine — remoção de risco visível antes do ponto
   de decisão, não no rodapé. O fundo contrastante isola: sinaliza que isto
   é de outra natureza (compromisso, não argumento).

5. **products** — grade 2×2, cada card com avaliação + preço + botão
   próprio. Por quê: aterrissar a tese em objetos compráveis. A faixa de
   preço visível revela posicionamento sem declarar. A avaliação em cada
   card é prova DISTRIBUÍDA — pequena, no ponto exato da micro-decisão, em
   vez de concentrada num bloco distante.

6. **cta** — botão isolado. Por quê: saída para quem decidiu na grade mas
   não quer escolher o item agora.

7. **reviews** — depoimento único com nota e nome, que fecha exatamente o
   arco aberto pela tese: um terceiro dizendo a frase que a marca não pode
   dizer sobre si mesma. Por quê: a objeção nomeada no bloco 3 e garantida
   no bloco 4 é confirmada por quem pagou.

8. **footer** — logo + navegação por categorias + credencial discreta
   (tempo de mercado) + suporte. Por quê: rota para quem não clicou em
   nada; a credencial fica onde não vira discurso.

# Dispositivos (objecao × papel)

Vocabulário para o Estruturador emitir `requisitos.dispositivo` em vez de prosa.

| Seção | Papel | Dispositivo | Objeção |
|---|---|---|---|
| header | apoio | logo-sobreposto-ao-hero — **não realizável hoje** ([[header-sem-variante]]) | — |
| hero | abre | entrega-imediata-da-promessa | preco-valor |
| body | meio | tese-que-nomeia-a-objecao | qualidade-eficacia |
| body | apoio | faixa-de-garantias-3-icones | confianca-no-canal |
| products | apoio | grade-2x2-com-avaliacao-e-preco | amplitude-de-catalogo |
| cta | ponte | botao-isolado — **não realizável hoje** ([[cta-sem-variante]]) | — |
| reviews | fecha | depoimento-unico-que-fecha-a-tese | adesao-social |
| footer | fecha | menu-de-saida | — |

**Fio narrativo:** promessa entregue → dúvida nomeada e transformada em
alegação → compromisso verificável → produto com prova distribuída →
confirmação de terceiro.

# Por que essa estrutura funciona

O e-mail inteiro é UM argumento: a objeção dominante da categoria (na loja
de origem, "parece bom na foto e decepciona na mão") atravessa três blocos
em papéis diferentes — nomeada na tese (3), garantida no compromisso (4),
confirmada pelo terceiro (7). As partes conversam porque atacam a mesma
dúvida de ângulos distintos. É o oposto do welcome genérico em que cada
bloco elogia uma coisa diferente e nada soma.

A entrega imediata do incentivo no hero respeita o contrato do opt-in — a
pessoa assinou por isso, e front-loading do que ela veio buscar é a regra
de atenção mais bem sustentada que existe (a leitura de e-mail é
escaneada e afunila rápido; o essencial precisa estar no primeiro
terço). A repetição do incentivo no bloco 3 não é desperdício porque muda
de papel: entrega → fechamento de argumento.

Garantia antes da vitrine segue o consenso de CRO: remoção de risco
funciona no ponto da decisão, visível, e sua importância ESCALA com o
ticket — em ticket médio-alto de categoria com medo de qualidade, subir a
garantia para antes do preço é a escolha certa; em impulso barato ela pode
descer.

Fraquezas conhecidas (adaptar ao usar): (a) o depoimento — a peça que
fecha o argumento central — está DEPOIS de todos os CTAs; quem clica na
grade nunca o vê. Prova social não é universalmente aditiva: ela vale onde
a objeção está ativa. Se a objeção da loja é desconfiança, considerar
subir o reviews para antes ou junto da grade. (b) Três CTAs genéricos +
botões por produto disputam com peso igual; e-mail curto pede UM CTA
dominante. (c) O incentivo do hero não pode viver só dentro da imagem —
com imagens bloqueadas o código some; precisa existir em texto real.

# Quando usar / quando não usar

**Usar quando:** primeiro toque do welcome; a loja tem UMA objeção
dominante clara de PRODUTO (qualidade percebida, eficácia, durabilidade) —
a estrutura é monotemática por desenho; existe incentivo ativo prometido
no opt-in; ticket médio para cima (a garantia antecipada se paga).

**Não usar quando:** a objeção dominante é da LOJA/canal (legitimidade,
entrega, falsificação) — aí a comparação contra a categoria serve melhor
(ver [[medicube-comparacao-categoria]]); a loja não tem incentivo ativo (o
hero e o bloco 3 perdem o fechamento; a estrutura desmonta); não há
depoimento real com nome — sem o bloco 7 o arco fica sem confirmação e é
melhor escolher estrutura que não dependa de prova.

**Exige da loja:** incentivo ativo · ≥4 produtos com foto, preço e
avaliação · ≥1 depoimento com nome que toque a objeção central · garantias
reais de entrega/devolução · categorias de navegação para o rodapé.

# Aprendizados aplicáveis

- Fraqueza (a) → [[prova-de-terceiro-antes-do-cta]]
- Fraqueza (b) → [[um-cta-dominante-em-email-curto]]
- Fraqueza (c) → [[incentivo-precisa-existir-em-texto]]
- Ordenação da garantia → [[remocao-de-risco-escala-com-o-ticket]]
- Repetição do incentivo em dois papéis → [[cupom-repetido-precisa-de-papel]]
