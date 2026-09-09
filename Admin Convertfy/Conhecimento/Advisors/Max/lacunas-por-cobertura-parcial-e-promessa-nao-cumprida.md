---
tipo: indice
assunto: cobertura-e-lacunas
autor: max-sturtevant
status: aprovado
---

Registro das lacunas em que o corpus Max entrega uma parte e engole a outra:
**cobertura parcial** (existe a finalidade e falta a execução, ou o inverso) e
**promessa não cumprida** (o material anuncia um objeto e não entrega). Nos dois
tipos a resposta não é recusa inteira — é entregar o que existe, ou citar a
promessa, e nomear o que falta. Índice em [[mapa-da-cobertura]].

# Cobertura parcial — existe finalidade e falta execução, ou vice-versa

Aqui a recusa é **parcial**: entrega-se o que existe e nomeia-se o que falta.
Recusar por inteiro o que o corpus cobre pela metade é erro tão grave quanto
inventar.

**Sunset Flow — o caso-escola.** O corpus dá a finalidade e o segmento, e não dá
nada da execução.

| O que existe | Onde |
|---|---|
| Finalidade, verbatim: "**Sunset Flow** – Triggered when a contact is no longer engaging. Removes or suppresses inactive users." | L411, slide (glossário) |
| Recomendação de uso — está na lista dos oito "recommended flows when just starting out" | L92, L94, transcrição |
| **Definição do segmento**, lida do PNG embutido na L9545 (referenciado por `![][image1]` na L3402): 180 dias sem abrir · 180 dias sem clicar · ao menos 10 emails recebidos · zero pedidos over all time | L9545, print |
| O vizinho mais próximo: o critério de suppression list descrito na aula de segmentação ao prometer o sunset | L5129, **outro-narrador** |

O que **não** existe: sequência, contagem de emails, delay, subject line,
template, copy, filtro, condição de saída. Nem aula (L3398-3403 é título + link
+ imagem) nem seção no deck (o `# GAMMA FLOWS` começa em L3404 e vai do Winback
direto para Flow Optimization). O deck próprio do Sunset
(`Sunset-Flow-v13borkcrsurvpv`, L3400) não está no corpus. E o glossário diz
"removes **or** suppresses" e nunca escolhe entre os dois. Ver [[flows/sunset]].

Outros casos de cobertura parcial:

| Assunto | Tem | Falta |
|---|---|---|
| **Filtro e condição de saída de flow** | **três dos oito.** Welcome: dois filtros — `placed order zero times since starting this flow` (L1542) e `bounce less than two times since starting this flow` (L1544) — mais a saída, verbatim: "if anybody fails to meet any of these, they'll be kicked out of the flow" (L1546). Site abandon: a saída, falada — "what's going to kick me out of this flow is if I actually view a product page" (L2349). Winback e Sunset são disparados por **segmento**, e o segmento está publicado (L5589 e o print da L9545) — o critério de entrada existe | **browse abandon, cart/checkout abandon, post-purchase e replenishment: nada.** Nem filtro nem saída, em nenhum dos dois registros. E em site abandon o filtro não existe. Ver a tabela "Gatilho, filtros e saída" de cada nota em [[mapa-dos-flows]] |
| **Limiar de teste A/B** | amostra mínima e número de repetições por tamanho de lista (L8800-8820); cadência de teste de form, "at least bi-weekly" (L663); a regra de onde testar — campanha e não flow, "we mostly use campaigns as our testing ground" (L4128-4131) | **nenhum nível de significância, nenhum intervalo de confiança, nenhuma duração em dias e nenhum teto de testes simultâneos.** A conclusividade é medida por volume, nunca por estatística. Ver [[otimizacao/quando-vale-testar]] |
| **Janela de medição de métrica** | a janela de atribuição de receita (3 a 5 dias após o clique, L54) e a janela de leitura do painel (30 dias contra os 30 anteriores, L64) | **a janela das métricas de meta.** Nem a tabela de metas (L372-380), nem o glossário (L384-519), nem [[fundamentos/metricas-nucleo]], nem [[deliverability/metricas-alvo]] dizem se open rate é por envio, por 30 dias ou vitalício. Nunca transpor a janela do painel para o alvo |
| **Setup técnico de deliverability** | as siglas listadas (SPF, DKIM, DMARC, MX) e a instrução de onde ler | o que cada uma faz — nunca explicadas; nenhum valor de registro, nenhuma tela, nenhum tempo de propagação. O procedimento inteiro é "leia o artigo do Klaviyo, cheque no Glockapps". Ver [[deliverability/setup-tecnico]] |
| **Segmentos de exclusão** | "Exclusion segments should include (**but not be limited to**): Bounced 3+ times" (L4839-4840). O vizinho forte é a **Suppress List** do mesmo deck, essa sim completa: recebeu ≥5 emails over all time **AND** abriu zero vezes em 365 dias **OR** bounce ≥3 over all time **OR** marcou spam ≥1 (L5592), com a versão falada em L5129 | a lista de exclusão em si nunca é completada. A própria frase declara que está incompleta. Ver [[campanhas/segmentacao]] |
| **Email Architect** | o conceito, o racional, a regra dos 80% e o **esqueleto campo a campo**, falado: headline + subheadline + CTA como hero "most generic and most commonly used" (L5823-5825), bridge section = infográfico, com o exemplo de layout de tabela "reviews, average rating, five star reviews" (L5827-5831) | **nenhum exemplo do formato em imagem** — a fala descreve uma tela que não está no texto — e nenhuma definição do artefato (documento? Figma? wireframe?). Os dois slots "Example \#1/\#2" (L6794-6796) vieram vazios. Ver [[copy/email-architect]] |
| **Alia como alternativa ao Klaviyo** | julgamento forte ("the ROI is worth it every time", L1243) e um walkthrough falado | preço, limiar de lista ou faturamento em que passa a valer, e o material do deck — que é o placeholder `[need]` (L1304). Ver [[list-growth/alia-e-a-alternativa]] |
| **Warming do domínio** | a rampa em duas fases e dois casos reais | o teto de frequência (a frase que o carregava foi truncada, L8560), o nome da ferramenta de HTML (corte de 41s), a duração total do warming — "weeks 1 to 3", "weeks 3 to 12" e uma "60 day window" não são a mesma unidade |
| **Captura de telefone no checkout** | a intenção declarada e o argumento | o procedimento — o que está lá é o de email, colado. Ver *Entregue errado*, abaixo |

# Promessa não cumprida — o material anuncia e não entrega

O usuário vai perguntar por estes itens **porque o material os prometeu**. A
resposta cita a promessa e diz que o objeto não veio.

| Promessa | Onde é feita | Estado |
|---|---|---|
| **Swipe file de 30 SMS** — "in the description in the doc I have a swipe file of 30 SMS messages which I handpicked with the help of attentive" | L9258 (fala) e L9520-9523 (slide: "I went through Attentive's SMS database and picked 30 of my favorite SMS messages") | O deck tem o título `# **30 SMS Campaigns Swipe File**` e duas frases de racional. **As 30 mensagens não estão no corpus.** |
| **Swipe file de 84 emails** — "84 different emails in here. Very useful. We'll of course attach these" | L4506 (fala, **outro-narrador**) e L5351 (slide de Max: "Use this swipe file of 84 high-converting email campaigns handpicked by me a $100M email marketer") | O slide traz um link de Google Drive. **Os 84 emails são externos ao corpus.** |
| **Documento externo de A/B tests** — "there's another document we have that outlines some of the higher leverage AB tests with a little bit more info on it as well" | L9094-9096 (fala, **outro-narrador**) | Não está em `CONTEUDO BRUTO/max.md`. É a lacuna declarada pelo próprio material no módulo mais raso do corpus — a promessa é do narrador da aula de A/B, não de Max. |
| **"We'll talk about this more in the Sunset Flow, obviously, as well."** | L5127 (fala, dentro da aula de segmentação — **outro-narrador**) | Nunca cumprida. Não há aula nem deck de Sunset. É a promessa que fecha o caso-escola acima, e quem a faz não é Max. |
| "We'll have examples for you" — sobre como o split por número de compras muda a copy do post-purchase | L3084 (fala) | Não entrega na faixa. Ver [[flows/post-purchase]] |
| "I'll list the other ones" — os demais flows de alta intenção durante o warming | L8545 (fala, **outro-narrador**) | **Nunca lista.** |
| "maybe I'll attach a resource down below on this one" (bounce rate) · "we can maybe get more into the weeds on that in another video" (hard vs soft bounce) · "maybe we'll have a more in-depth video just talking about the importance there" (alt text / HTML) | L8438 · L8446 · L8504 | Três recursos ausentes, todos em deliverability. |
| Seções de walkthrough anunciadas e vazias: `# **Design Walkthroughs**` · `# **Copywriting Walkthroughs**` · `# **2 Copywriting ONLY Live Examples**` · `# **Copy + Design Creation Videos**` | L8357 · L6851 · L6853 · L6855, L8359 | Títulos sem uma linha de conteúdo abaixo. |
| Tutoriais de pop-up do deck: "Klaviyo Pop-Up Form Creation" e "Alia Pop-Up Form Creation" | L1300 e L1302-1304 | O primeiro vazio; o segundo com o marcador de produção `[need]` deixado no export. |
| Ponteiros de SMS para vídeo e doc externos ("I break this all down in the video", "I'll have a link to the document below it has like all the copy for you") | L9238, L9242-9243, L9246-9247, L9250 | O material apontado não está no corpus. Não confundir com lacuna nova — é a mesma lacuna, apontada cinco vezes. |

