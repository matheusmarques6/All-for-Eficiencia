---
tipo: especificacao
assunto: estrutura-cart-abandon
autor: convertfy
status: aprovado
fonte: 'Figma "ESTRUTURA FIGMA — RIDE NATION" — implementação Convertfy, 9 peças de cart abandon + 1 de site abandon, extraído em 2026-09'
---

O cart abandon da casa tem nove e-mails, não quatro. Seis são peças desenhadas em português, na voz da marca; três são de texto puro, ainda no template original em inglês. O desconto entra já na primeira peça, a 10%, e sobe uma única vez — para 12%, no sexto e-mail. Não existe escada de concessão: há um platô de preço com um degrau simbólico, e a escalada real acontece em urgência, escassez e prova. O site abandon usa uma peça só, com desconto de largada maior (12%, 48h) que o do carrinho.

# Como montar a sequência

Alterne desenhada e texto puro: o segundo é descanso visual e pretexto de suporte.

**#1 — o presente dourado (oferta em curiosidade).** 600x3092. `"CLIQUE NO"` / `"PRESENTE DOURADO"` / `"E GANHE UMA SURPRESA NO CARRINHO"`, CTA `"QUERO VER MINHA SURPRESA"`. A revelação só vem depois do bloco dinâmico: `10%OFF`, `DESCONTO10`, `"GARANTIR DESCONTO"`. Fecha com três depoimentos 5.0 e `"FECHAR MEU PEDIDO AGORA"`. Sem prazo.

**#2 — lembrete pessoal em texto puro.** `"It looks like you added an item to your cart but didn't purchase. [Insert brand info and unique selling propositions] I saved your item for you just in case."` Sem oferta e sem prazo.

**#3 — o pedido tratado como já existente.** A maior peça, 600x4073. `"ESTAMOS EMBALANDO"` / `"SEU PEDIDO"`, e a copy assume posse: `"[Nome], a gente foi lá e separou tudo. Os itens que você colocou no carrinho estão aqui, na fila, prontos pra ir embora com a etiqueta do teu nome."` Depois `"Reservamos pra você:"`, `"10% OFF POR TEMPO LIMITADO"`, `"Envio ainda hoje se confirmar agora"`. Aqui entra o prazo — `"Reserva válida por:"` com contador — e `"CONFIRMAR PEDIDO E FINALIZAR"`.

**#4 — preço explícito + confiança.** `"TUA PEÇA TÁ AQUI."` / `"E AGORA COM 10% OFF."` Depois do bloco dinâmico o eixo vira prova: `"A GALERA JÁ FALOU"`, `"Quem já comprou, voltou. E não foi à toa."`, `RATING GERAL` `"4.9/5 (12.847 avaliações)"`, `"COMPRAR COM SEGURANÇA"`, e `"DEPOIMENTO EM DESTAQUE"` com uma `"NOSSA RESPOSTA"` da marca.

**#5 — urgência máxima e falso encerramento.** `"ÚLTIMA CHANCE"` + `10%OFF`, contador `"HORAS QUE FALTAM:"`, CTA `"SALVAR MEU CARRINHO AGORA"`, e o bloco `AVISO FINAL:` — `"Esse é nosso ÚLTIMO email sobre seu carrinho. Depois que o timer zerar, não conseguimos mais garantir esse preço nem a disponibilidade dos produtos. A decisão é tua. O tempo não espera."` Única aparição de escassez.

**#6 — reabertura com o degrau de desconto.** `12%OFF`, `"Teu carrinho ainda tá aqui."` / `"O desconto, por enquanto, também."`, `DESCONTO12`, `"FINALIZAR MINHA COMPRA"`. Fecha abrindo o leque: `"OUTROS QUE A CREW TÁ VESTINDO"` — recomendação lateral, não o carrinho.

**#6a — suporte com prazo, texto puro.** `"I noticed you almost made a purchase (…) Need help? (…) I saved your item for you just in case [expires in 24 hours]."`

**#7 — última chance com prova em volume.** `"ÚLTIMA CHANCE"` + `12%OFF`, `"GARANTA A PEÇA AGORA"`, `DESCONTO12`, e o fecho `"+50.000"` / `"PESSOAS JÁ VESTEM A CENA"` com seis depoimentos em grade.

**#8 — desconto sem valor declarado, texto puro.** Igual ao #6a, com uma troca: `"I saved your item and your discount for you just in case. Use code "DISCOUNT" at checkout to claim."` Sem prazo.

# A escada de concessão não existe

**10% no #1, #3, #4 e #5; 12% no #6 e no #7.** O #2 e o #6a não têm oferta; o #8 traz código `"DISCOUNT"` sem valor.

1. **O desconto abre a sequência, não a fecha.** Não há lembrete neutro — a primeira peça já é oferta, disfarçada de curiosidade.
2. **Dois pontos percentuais em nove e-mails.** Quem esperou até o fim ganhou 2% a mais que quem comprou no primeiro: não treina o cliente a esperar.
3. **A escalada é em outros eixos.** Prazo entra no #3 e volta no #5; escassez só no #5. A prova cresce: três depoimentos no #1 → rating agregado no #4 → `"+50.000"` e seis depoimentos no #7.

A trilha de texto puro tem escada própria e invertida: #2 sem oferta e sem prazo → #6a sem oferta e com prazo → #8 com oferta e sem prazo. E o eixo gira a cada peça, nunca dois seguidos no mesmo: curiosidade (#1) → pessoal (#2) → posse e urgência (#3) → preço e confiança (#4) → escassez (#5) → preço maior e descoberta (#6) → suporte (#6a) → prova em volume (#7).

# O que distingue #6 de #6a

**Nó, formato, idioma, oferta e função são todos diferentes.** `#6` é `node 2989:116`, desenhada 600x3088, em português, com `12%OFF` e `DESCONTO12`. `#6a` é `node 1032:1108`, texto puro 800x727, em inglês com `[Brand]`, sem desconto, com prazo de 24h e apelo de suporte. Não são versões da mesma peça, e sim peças distintas no mesmo passo.

A numeração de nó reforça: os três textos puros — `1032:1102` (#2), `1032:1105` (#8), `1032:1108` (#6a) — são consecutivos e fora da ordem do flow. Foram criados juntos, como conjunto de templates, e encaixados em slots depois; o sufixo `a` marca encaixe posterior, não variante paralela.

**O que não dá para saber:** se é ramificação condicional (quem não abriu/clicou o #6), split A/B ou simples inserção. Nenhuma condição ou regra consta. `[não consta na fonte]`.

# Componentes fixos — a biblioteca reutilizável

**Barra de navegação** (`y=16`, toda peça desenhada): `MAIS VENDIDOS` · `MASCULINO` · `MOLETOM` · `FEMININO`.

**Barra de confiança de três selos**, sempre abaixo de um CTA — em #3, #4, #5, #6 e no Site Abandon; ausente em #1 e #7:

> `ENTREGA PRA TODO O BRASIL` — `"Frete calculado no checkout. Sem surpresa no final, como tem que ser."`
> `TROCA SEM BUROCRACIA` — `"7 dias. Sem formulário de 3 páginas. Sem drama. Só avisa a gente."`
> `PAGAMENTO SEGURO` — `"Checkout protegido. Cartão, Pix ou boleto do jeito que você preferir."`

**Bloco de cupom**: rótulo `CUPOM:` colado ao código em display, seguido de botão. Códigos semânticos por flow — `DESCONTO10`, `DESCONTO12`, `VOLTEI12` (site), `EXCLUSIVO12` (browse). **Bloco dinâmico** `[in-klaviyo Dynamic Product section]` em todas as desenhadas, por vezes duplicado na peça. **`Unsub Info`** sempre em `y=415`.

**CTAs em escada**, texto diferente a cada aparição, nunca repetindo dentro da peça. No #1: `QUERO VER MINHA SURPRESA` → `GARANTIR DESCONTO` → `FECHAR MEU PEDIDO AGORA`.

**Contador regressivo** `01 : 59 : 47` (`HORAS`/`minutOs`/`SEGUNDOS`), mesmo valor em #3 e #5. Se é dinâmico ou imagem, `[não consta na fonte]`.

# Site abandon: o que muda quando a intenção é mais fraca

Peça única, 600x3057: `"Chega mais, Preparamos isso pra você:"`, `12` `%` `OFF`, `"48h"` `"valido"` `"Por"`, cupom `VOLTEI12`. Convite, não recuperação. Desconto maior de largada — 12%/48h contra os 10% sem prazo do carrinho: quem tem carrinho montado recebe a oferta menor, inversão de margem que vale checar por cliente. Prazo em texto, não em contador. Sem bloco dinâmico, sem prova social, sem escassez. CTA de exploração (`VOLTAR PRA LOJA`, `VER PRODUTOS`), não de conclusão. Mantém nav bar e os três selos.

# O que a estrutura NÃO faz

**Não separa cart abandon de checkout abandon** — não há peça de checkout na coleção. **Não declara delay, filtro, supressão, saída nem subject line** `[não consta na fonte]` — convergência por omissão com o Max, que também não dá delay para cart/checkout. **Não oferece frete grátis, brinde nem desconto em R$**: só percentual, e o frete pago vira argumento de transparência. **Não usa voz de fundador assinada**: os textos puros assinam `"The [Brand] Team"`, as desenhadas não assinam. Ver [[a-voz-do-fundador-como-formato]]. **Não localiza os textos puros** e **não termina as headlines**: `Headline` cru em #4, #5 e #6, `Headline` e `Body Copy` no Site Abandon, a peça menos escrita da coleção.

**Inconsistências a corrigir na replicação:** o #4 assina o depoimento como `"Lucas M."` e a resposta da marca começa `"Rafael, é exatamente isso."`; anuncia `"E AGORA COM 10% OFF."` sendo que 10% roda desde o #1; e o #5 diz `"Esse é nosso ÚLTIMO email sobre seu carrinho"` com quatro peças por vir.

# Onde a prática da casa bate e onde diverge

Cruzado com [[cart-checkout-abandon]] e [[site-abandon]] (Max Sturtevant) e [[padroes-de-abandono-e-transacional]] (Well Copy).

**Divergência principal — volume. 9 contra 4.** O Max é explícito: quatro e-mails para cart e quatro para checkout, como dois flows separados. A casa usa nove num flow só e não tem checkout abandon. Dobra a sequência e elimina o corte por intenção que é a tese central da aula dele.

**Divergência — onde entra o desconto.** Max põe no e-mail 3, atrás de um lembrete neutro e de um text-based. A casa abre com desconto no #1; o "lembrete simples" dele não existe.

**Divergência — densidade.** Max: `"Avoid too many CTAs that will cause overwhelm"` e `"Keep it as simple as possible"`. As peças da casa têm 3.088 a 4.073 px e dois a três CTAs.

**Divergência — frete grátis, remetente e desconto em site abandon.** Max manda incluir threshold de frete grátis e prefere remetente pessoa física; a casa não tem nem um nem outro. E o corpus dele não traz desconto algum em site abandon — a casa dá 12%/48h de largada. Concordam só no volume: ele prescreve 1 a 2, a casa usa 1.

**Concordância — text-based, bloco dinâmico e CTA acima da dobra.** Max prescreve dois dos quatro em texto puro; a casa usa três, e o #2 é praticamente o "personal reminder" dele. `[in-klaviyo Dynamic Product section]` está em todas as desenhadas, com o primeiro botão em `y≈578-674`, acima do bloco dinâmico.

**A headline que a Well Copy declara vencedora** é `"Your Order Is Ready To Ship!"`, e o Max registra a mesma frase como subject do e-mail 1. A casa executa o mecanismo em português (`"ESTAMOS EMBALANDO"` / `"SEU PEDIDO"`) **mas no terceiro e-mail, não no primeiro**: duas fontes independentes a apontam como abertura, a casa a usa como reforço.

**Desconto misterioso — a casa flerta e não executa.** A Well Copy documenta a neutonic: código `MYSTERY`, valor nunca dito, `"Access expires in 24 hours"`. A casa promete `"PRESENTE DOURADO"` no #1 e revela `10%OFF` / `DESCONTO10` na mesma peça — curiosidade como embalagem, não oferta oculta. O único código sem valor é `"DISCOUNT"` no #8, template em inglês. E a mesma referência chama `MYSTERY` de tão estático quanto `WELCOME10`: `DESCONTO10` e `DESCONTO12` são essa classe. Ver [[curiosidade-e-oferta-oculta]].

**Concordâncias com a Well Copy:** três selos abaixo do botão principal, CTAs em escada, prova social depois do primeiro CTA, carrinho dinâmico, depoimento com nome próprio.

**O que a casa acrescenta às duas fontes:** contador regressivo em display, `AVISO FINAL:` com escassez de estoque, rating agregado e resposta da marca ao depoimento. Ver [[urgencia-fabricada-por-formato]] e [[formato-da-prova-social]].


# O que esta nota não prova

**Uma implementação, não um padrão medido.** O material documenta a Ride Nation e mais nada. Que a estrutura se replique entre clientes é afirmação da casa — o artefato não demonstra isso, porque é o Figma de um cliente só.

**Nenhum número.** Não há taxa, receita, amostra, período ou teste em lugar algum da fonte. `"4.9/5 (12.847 avaliações)"` e `"+50.000"` são claims de marca dentro da copy, não medição do flow. Nada compara 9 e-mails contra 4, 10% contra 12%, ou desenhada contra texto puro; nenhum A/B declarado, nem no par `#6` / `#6a`. É padrão de execução, não prova de que funciona melhor.
