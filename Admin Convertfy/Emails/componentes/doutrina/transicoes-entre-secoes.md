---
tipo: doutrina
secao: geral
fonte: "Conhecimento/Advisors/Max/design/transicoes-entre-secoes-do-email.md — §O que é (bruto L8304-8306), §A autocorreção em cena (L7538-7548), §Os quatro métodos (L7552-7586; slide L8307 promete e não lista), §O favorito dele (L7580-7588), §Como isso conversa com skimmability (L8196, L7177), §O que o corpus não diz"
registro: [transcricao]
status: aprovada
---

Ponte para a regra do Max sobre o que acontece entre as seções de um e-mail — a transição que impede a pessoa de achar que o e-mail acabou — traduzida para o que este vault tem para juntar dois blocos: `convivencia`, `paleta` e o passo 8 do protocolo.

# A regra do Max

> Transitions are what help make your different sections in your email flow. Having separate sections that are blocky and unrelated will lead to churn. By making it congruent, customers will keep scrolling without realizing. (slide L8304-8306)

Na fala ele começa errado e se corrige (L7538-7542): o problema de seções "blocky" não é facilitar a rolagem — é criar um ponto de parada em que "people might reach the end of a section and not want to move on to the next section". Vale a correção (`design-blocky`). O objetivo: "the customer keeps scrolling without realizing like okay here's a hard stopping point" (L7548).

Os quatro métodos existem só na fala — o slide anuncia "Here are a few methods to do this:" (L8307) e não lista nenhum (`design-metodos-de-transicao-ausentes`):

1. Gradiente da hero para dentro da seção seguinte (L7552-7558).
2. Formas ou quebras de linha em vez da linha reta chapada (L7560-7568).
3. Fundo consistente no e-mail inteiro — "That's not just like white" — com os elementos por cima (L7570-7578).
4. Transição atrás de foto — gradientes ou formas por trás das fotos; "it just flows like butter" (L7580-7586). É o favorito dele e é composição dos métodos 1 e 2.

Fecho: "make sure that you do transitions behind elements and make sure that your emails aren't too blocky" (L7588). A tensão com skimmability é declarada: suave demais vira "one big blob" (L7177), duro demais vira blocky; "clearly see 2-3 sections" (L8196) é o outro lado. O corpus não dá altura de transição, pixels de gradiente nem critério por tipo de e-mail.

# Como isso se lê neste vault

- **O que o vault tem é o veto, não o fluxo.** As seis regras de `convivencia` são incompatibilidades. [[raio-alto-nao-convive-com-canto-vivo]] é o "blocky and unrelated" do Max lido como veto: "leem como dois e-mails colados, não como um". [[monoespacado-nao-convive-com-serif-display]] é o mesmo critério em tipografia. O Max acrescenta o lado positivo — o que faz fluir — e para isso não há campo.
- **Método 3 tem vizinho.** `paleta` é o eixo que diz o fundo de cada variante; duas seções adjacentes com a mesma `paleta` são o "fundo consistente" dele. Com paletas diferentes e nada entre elas, é a emenda que ele chama de blocky.
- **Método 4 já existe dentro de variante.** [[hero-9-atendimento-proativo]]: "O cinza de fundo é o fundo de estúdio da foto. Não existe bloco de cor separado nem emenda. A ausência total de costura é o efeito". O requisito [[terco-superior-liso]] é o que torna isso possível. A transição atrás da foto acontece aí — dentro de um bloco, não entre dois.
- **`ponte` não é transição.** O papel [[ponte]] é um bloco curto de conteúdo entre dois de natureza diferente; a transição do Max é tratamento visual sem conteúdo. São respostas diferentes ao mesmo problema; não tomar uma pela outra.
- **O limite estrutural.** As variantes são HTML fixo, conferido por md5 contra o banco (`_html/`). O agente não desenha um gradiente entre duas variantes; a única alavanca é a escolha da vizinha. Os métodos 1, 2 e 4 entre blocos ficam sem tradução — é achado, não regra.

# Onde entra na decisão

Passo 8 do [[_protocolo-de-selecao]]: ao conferir `convivencia` e `peso` contra as seções já escolhidas, a leitura do Max entra na mesma ordem — primeiro os vetos declarados (raio, tipografia, [[exige-hero-ou-contexto-acima]]); depois, entre candidatas que sobrevivem, a que compartilha `paleta` com a seção de cima é a que "flui". Não é regra nova do vault; é o que o Max diz, lido pela chave que o passo 8 já usa. Quando duas seções `pesado` se seguem sem `leve`/`medio` entre elas, o orçamento de `peso` e o "blocky" apontam para o mesmo lugar.
