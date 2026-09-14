---
tipo: estrutura
slug: avelmore-deadline-objecao
flow_type: welcome
emails: [2]
objecao_alvo: trava desconhecida — a pessoa não agiu e não se sabe qual objeção travou
mecanismo: varredura numerada de objeções de naturezas diferentes, escaneável pelos títulos, seguida de custo de adiar isolado em bloco de interrupção
escopo: geral
loja: avelmore
amostra: montagem sobre marca de calçado de couro, ticket médio (US$ 50-70)
procedencia: nossa
revisado_por: Convertfy
status: aprovada
secoes: [header, hero, body, offer, products, footer]
performance:
---

Serve a intenção [[welcome-2|welcome 2]].

# A estrutura

1. **header** — barra própria com logo, isolada do hero. Por quê: o
   segundo toque não reapresenta; o logo só ancora. A mudança de tratamento
   em relação ao primeiro toque (lá, sobreposto ao hero) sinaliza
   visualmente que este é outro tipo de e-mail.

2. **hero** — dispositivo: oferta na frente. Foto de CATÁLOGO (vários
   produtos num plano aberto, opções visíveis) + a oferta dominando o
   quadro + incentivo + CTA de reivindicar. Por quê: a pergunta de quem já
   recebeu o primeiro toque mudou de "por quê" para "qual". Abrir com a
   marca de novo desperdiçaria o toque; abrir com opções prepara a escolha.

3. **body** — dispositivo: varredura numerada de objeções. De 3 a 6
   razões, cada uma com headline forte + 2-3 linhas, cada uma atacando uma
   trava de natureza DIFERENTE (qualidade do material, justificativa do
   preço, custo/velocidade de entrega, risco de errar a compra,
   diferenciação). Por quê: neste ponto a trava é desconhecida — este é o
   único toque de varredura do flow. A numeração serve à escaneabilidade:
   os títulos carregam o argumento sozinhos para quem só passa o olho. Ao
   menos duas razões devem ser remoção de risco descrita OPERACIONALMENTE
   (como funciona a entrega, como funciona a troca) — custo de entrega e
   medo de errar estão consistentemente entre as maiores causas reais de
   não-compra, e descrever o processo convence mais que o selo.

4. **offer** — dispositivo: custo de adiar, isolado em faixa de fundo
   contrastante. Incentivo + prazo + CTA. Por quê: é o bloco que carrega o
   e-mail — pela primeira vez no flow, decidir depois fica pior que decidir
   agora. O isolamento visual o transforma em interrupção, não em
   parágrafo. REGRA DURA DE POSIÇÃO NO FLOW: usado no segundo toque, o
   prazo é VAGO ("por tempo limitado"); hora fechada ("hoje, 23:59") só é
   permitida quando esta estrutura for aplicada no e-mail que ENCERRA o
   ciclo da oferta. Hora anunciada e não honrada no toque seguinte mata
   retroativamente todos os prazos do flow.

5. **products** — grade com a oferta repetida no título da seção
   ("escolha o seu com o desconto"). Por quê: fechar com a escolha,
   mantendo a oferta viva no ponto exato do clique.

6. **footer** — logo + navegação por categorias + suporte.

# Dispositivos (objecao × papel)

Vocabulário para o Estruturador emitir `requisitos.dispositivo` em vez de prosa.

| Seção | Papel | Dispositivo | Objeção |
|---|---|---|---|
| header | apoio | barra-de-logo — **não realizável hoje** ([[header-sem-variante]]) | — |
| hero | abre | oferta-na-frente | preco-valor |
| body | meio | varredura-de-objecoes | varredura (todas) |
| offer | apoio | custo-de-adiar-em-faixa | disponibilidade-urgencia |
| products | apoio | grade-com-oferta-no-titulo | amplitude-de-catalogo |
| footer | fecha | menu-de-saida | — |

**Fio narrativo:** oferta na cara → todas as travas derrubadas em títulos
escaneáveis → custo de adiar → escolha.

# Por que essa estrutura funciona

O diagnóstico do segundo toque é diferente do primeiro: quem recebeu o
toque 1 e não agiu não sofre de falta de informação — sofre de falta de
decisão, e não se sabe qual objeção travou. A resposta estrutural é dupla:
varrer as objeções (porque a trava é desconhecida) e introduzir custo de
tempo (porque sem custo a inação continua racional).

A varredura funciona porque respeita como e-mail é lido: uma fração
pequena das palavras, em saltos. Cada razão precisa sobreviver à leitura
só dos títulos — se os títulos sozinhos não contam a história, o bloco
falhou. E as razões devem ter naturezas distintas: cinco variações de
"qualidade" não são varredura, são repetição.

O bloco de prazo isolado é o motor. A separação visual (fundo
contrastante, quebra do ritmo claro/escuro) faz o leitor tratá-lo como
aviso, não como argumento. Mas o dispositivo só funciona se o prazo for
VERDADE — prazo decorativo ensina o contato a ignorar todos os seguintes,
e essa perda é permanente e por contato, não por campanha.

Fraquezas conhecidas (adaptar ao usar): (a) a varredura vem ANTES do
bloco de prazo — quem cansa no meio da lista nunca chega ao motor do
e-mail; com mais de 4 razões, ou corta-se a lista, ou o bloco de prazo
sobe. (b) Na origem, o incentivo aparece quatro vezes com a MESMA função
— diferente do primeiro toque, onde as repetições têm papéis distintos
(entrega vs. fechamento); aqui duas ocorrências bastam: hero e bloco de
prazo. (c) Não há nenhuma voz externa: quem não abriu o toque 1 recebe
só alegações da marca. Se a taxa de abertura do primeiro toque for baixa,
incluir prova mínima distribuída (avaliação nos cards da grade) sem
adicionar bloco.

# Quando usar / quando não usar

**Usar quando:** segundo toque, após um primeiro toque monotemático (a
varredura complementa a aposta única do 1); a loja tem 3-6 razões REAIS e
de naturezas diferentes, cada uma sustentável operacionalmente; existe
incentivo ativo com fim previsto (mesmo que a hora exata fique para o
fechamento).

**Não usar quando:** a objeção da loja é UMA, conhecida e profunda — aí
varredura dilui; o registro certo é aprofundar (ver
[[avelmore-mecanismo-e-origem]]). Não usar com hora fechada fora do e-mail de
fechamento do ciclo (para fechamento com hora e escassez, ver
[[medicube-escassez-com-prova-de-demanda]]). Não usar se as razões não se
sustentam na operação — cada razão listada é uma promessa; frete "rápido" que
demora vira munição de reclamação.

**Exige da loja:** incentivo ativo · 3-6 diferenciais reais de naturezas
distintas · política de entrega e troca descritível em uma linha cada ·
grade de produtos com foto e preço.

# Aprendizados aplicáveis

- Fraqueza (a) → [[deadline-antes-do-argumento]]
- Fraqueza (b) → [[cupom-repetido-precisa-de-papel]]
- Fraqueza (c) → [[ausencia-de-prova-social-assume-abertura]]
- Regra dura de posição do prazo → [[deadline-falso-queima-o-proximo]] e
  [[_flow]] (regra transversal 3)
- Teste de escaneabilidade → [[titulos-precisam-carregar-o-argumento]]
- Cada razão é promessa → [[cada-alegacao-e-uma-promessa-operacional]]
