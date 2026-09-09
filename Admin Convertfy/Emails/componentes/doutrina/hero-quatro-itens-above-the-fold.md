---
tipo: doutrina
secao: hero
fonte: "Conhecimento/Advisors/Max/design/secao-hero.md — §O que é (bruto L8234-8235, L7256-7258), §Above the fold, definido (L7266-7272, L8239), §A composição obrigatória — 4 itens (L8243-8246, L7274-7284), §A fórmula resumida (L7352-7354), §O botão do topo (L8248-8251, L7027-7029)"
registro: [transcricao, slide]
status: aprovada
---

Ponte para a regra do Max sobre a seção do topo — os quatro itens que um hero precisa ter acima da dobra — traduzida para o que uma variante de `hero` deste vault precisa ter para passar, e para o que `hero-9` e `hero-2` deixam de fora.

# A regra do Max

A hero é "the top part of the email. It is by far the most important. Most people will only read the top section so 75% of your efforts should go to this" (slide L8234-8235; fala L7256-7258). Above the fold é "the section that's viewed without scrolling" (L7266; slide L8239), e o objetivo é que a pessoa "could not scroll and still be fine and we can make sales" (L7268-7272).

A composição obrigatória, verbatim do slide (L8243-8246):

> Clear headline · Strong graphic · Clear value prop · Clear button

A fala dá a função de cada um (L7274-7280): headline de preferência com o benefício do produto ou o motivo de comprar agora; gráfico "a strong graphic of some sort", sem dizer o quê; value prop para o cliente saber que valor recebe; botão para poder clicar. O teste de suficiência é a leitura mental "oh, this is the benefit I get. And here's where I have to click to make it happen" (L7282-7284). Versão curta: "Headline, value, graphic, and button above the fold. That's all you need to know" (L7352-7354).

**Ressalva do número.** Há três "75%" no módulo de design e medem coisas diferentes (`armadilhas-ao-citar-numero`, no vault do Max): L8235/L7258 é esforço de produção a alocar na hero; L7027 ("Button above the fold for 75% of your email") é proporção de e-mails com botão acima da dobra, e o bruto escreve "your email" no singular, sem desambiguar; L7089 é marcas auditadas. Nunca citar "75%" sem dizer de quê. O botão do topo tem conflito próprio (`design-botao-above-the-fold-sempre`): a nota da hero não abre exceção (L8248-8251); a aula de princípios abre — "Don't need to include it in every single one" (L7027-7029).

# Como isso se lê neste vault

- **Seção e papel.** A hero do Max é a seção `hero` daqui na posição `papel_na_peca: [abre]` — sete das nove heroes declaram `abre`; [[hero-8-lineup-com-lembrete-de-oferta]] e [[hero-10-lineup-de-colecao]] declaram `meio` e, pelo Max, não são hero no sentido dele: são bridge de catálogo. O teste do eixo [[abre]] ("essa abertura, isolada, já entrega algum valor ou decisão?") é o teste do Max lido de trás para a frente.
- **Os quatro itens em campos do vault.** Headline = o slot de título (`HEADLINE`, `HERO_HEADLINE`, `HEADLINE_L1/L2`). Strong graphic = o ativo fotográfico em `exige` — `foto-estudio-fundo-claro`, `foto-monocromatica`, `macro-de-produto`, `foto-com-pessoas`, `foto-de-campanha-propria`; sem o ativo a variante não é pior, é impossível (passo 4). Value prop = o que responde à `objecao` declarada: em `preco-valor` é o cupom em slot próprio (`OFFER_VALUE`, `COUPON_CODE` em hero-3, 4, 5, 6); em `qualidade-eficacia` é o diferencial; em `suporte-duvida` é a ajuda. Button = `CTA_LABEL/CTA_URL`.
- **O que passa.** Uma hero passa pelo Max quando os quatro slots existem e o par "benefício + onde clicar" fecha sem rolar. `schema_campos: 0` (passo 3) já reprova: não há slot para escrever.
- **O que [[hero-9-atendimento-proativo]] deixa de fora.** A value prop de compra. A nota é explícita: "Não há oferta nem desconto"; "Nenhum slot de oferta. Sem cupom, sem percentual, sem urgência". O benefício que sobra é o atendimento — pelo teste do Max, "this is the benefit I get" vira "posso pedir ajuda", não "posso comprar". É escolha, não defeito: "a variante existe para o momento em que vender seria contraproducente". E tem dois botões, não um "clear button" — hierárquicos (sólido e contorno), que é a leitura daqui para "claro": um domina.
- **O que [[hero-2-pergunta-comparativa]] deixa de fora.** O slot de value prop. "A oferta vive no botão, não na headline. A headline é argumento; o desconto aparece só no label do CTA" — as tags são `HEADLINE`, `HEADLINE_HIGHLIGHT`, `CTA_LABEL`: benefício comprimido no trecho destacado (2-3 palavras), valor comprimido no botão ("SHOP 10% OFF"). Pelo Max a headline é, de preferência, o benefício ou o motivo de comprar agora (L7274); aqui é uma pergunta. Três dos quatro itens em slot próprio; o quarto, distribuído.

# Onde entra na decisão

Passo 1 do [[_protocolo-de-selecao]]: a intenção diz a `objecao`, e a `objecao` diz qual value prop a hero tem de carregar. Passo 4: o "strong graphic" é `exige`. Passo 7, quarto eixo: `papel_na_peca: abre` é onde este teste se aplica. O aprendizado [[saida-rapida-no-primeiro-terco]] diz o mesmo por observação própria — saída de compra no primeiro terço — e, pela precedência, vale antes desta doutrina de curso; quando concordam, o Max só confirma. Sem tradução: "75% do esforço" — o vault não tem campo de esforço de produção; só `peso`, que mede altura.
