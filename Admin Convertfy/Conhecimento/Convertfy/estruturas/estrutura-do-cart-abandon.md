---
tipo: especificacao
assunto: estrutura-cart-abandon
autor: convertfy
status: aprovado
fonte: 'Figma "ESTRUTURA FIGMA — RIDE NATION" — implementação Convertfy, 9 peças de cart abandon + 1 de site abandon, extraído em 2026-09'
---

O cart abandon da casa tem nove e-mails, não quatro. Seis são peças desenhadas em português, na voz da marca; três são e-mails de texto puro ainda no template original em inglês. O desconto entra já na primeira peça, a 10%, e sobe uma única vez — para 12%, no sexto e-mail. Não existe escada de concessão: existe um platô de preço com um degrau simbólico, e a escalada real acontece em urgência, escassez e prova social. O site abandon usa uma peça só, e nela o desconto de largada é maior (12%, 48h) que o do carrinho.

# Como montar a sequência

Nove peças no flow de carrinho. Alterne peça desenhada e texto puro — o texto puro é o descanso visual e o pretexto de suporte entre blocos de oferta.

**#1 — o presente dourado (oferta embrulhada em curiosidade).** Desenhada, 600x3092. Abre em `"CLIQUE NO"` / `"PRESENTE DOURADO"` / `"E GANHE UMA SURPRESA NO CARRINHO"`, CTA `"QUERO VER MINHA SURPRESA"`. O bloco dinâmico vem antes da revelação: `10%OFF`, `CUPOM:` `DESCONTO10`, `"GARANTIR DESCONTO"`. Fecha com três depoimentos 5.0, um bloco de identidade — `"Essa peça no seu carrinho não tá lá à toa. Você já sentiu que era a certa. Faltou só apertar o botão."` — e `"FECHAR MEU PEDIDO AGORA"`. Sem prazo.

**#2 — lembrete pessoal em texto puro.** `"Hey there. It looks like you added an item to your cart but didn't purchase. [Insert brand info and unique selling propositions] I saved your item for you just in case. Complete My Order >>"` Sem desconto, sem prazo, não localizado.

**#3 — o pedido tratado como já existente.** A maior peça, 600x4073. `"ESTAMOS EMBALANDO"` / `"SEU PEDIDO"`, e a copy assume posse: `"[Nome], a gente foi lá e separou tudo. Os itens que você colocou no carrinho estão aqui, na fila, prontos pra ir embora com a etiqueta do teu nome."` Depois `"Reservamos pra você:"`, `"10% OFF POR TEMPO LIMITADO"`, `"Envio ainda hoje se confirmar agora"`, `"Precisamos apenas da sua"` / `"confirmação final."` É aqui que entra o prazo: `"Reserva válida por:"` com contador (`01 : 59 : 47`). Cupom `DESCONTO10` três vezes. Fecha em `"CONFIRMAR PEDIDO E FINALIZAR"`.

**#4 — preço explícito + confiança.** `"TUA PEÇA TÁ AQUI."` / `"E AGORA COM 10% OFF."` Depois do bloco dinâmico o eixo vira prova: `"A GALERA"` / `"JÁ FALOU"`, `"Quem já comprou, voltou. E não foi à toa."`, `RATING GERAL` `"4.9/5 (12.847 avaliações)"`, CTA `"COMPRAR COM SEGURANÇA"`, e `"DEPOIMENTO EM DESTAQUE"` com review longo e uma `"NOSSA RESPOSTA"` da marca.

**#5 — urgência máxima e falso encerramento.** `"ÚLTIMA CHANCE"` + `10%OFF`, contador `"HORAS QUE FALTAM:"`, CTAs `"SALVAR MEU CARRINHO AGORA"` e `"RESGATAR AGORA"`, e o bloco `AVISO FINAL:` — `"Esse é nosso ÚLTIMO email sobre seu carrinho. Depois que o timer zerar, não conseguimos mais garantir esse preço nem a disponibilidade dos produtos. A decisão é tua. O tempo não espera."` Única aparição de escassez de estoque.

**#6 — reabertura com o degrau de desconto.** `12%OFF`, `"Teu carrinho ainda tá aqui."` / `"O desconto, por enquanto, também."`, `DESCONTO12` duas vezes, `"COMPRAR AGORA"` e `"FINALIZAR MINHA COMPRA"`. Fecha abrindo o leque: `"OUTROS QUE A CREW"` / `"TÁ VESTINDO"` — recomendação lateral, não o carrinho.

**#6a — suporte com prazo, texto puro.** `"Hey there. I noticed you almost made a purchase (…) Need help? If you have any questions, reply to this email and our support team will get back to you as soon as possible. I saved your item for you just in case [expires in 24 hours]. Complete My Order >>"`

**#7 — última chance com prova em volume.** `"ÚLTIMA CHANCE"` + `12%OFF`, `"GARANTA A PEÇA AGORA"`, `DESCONTO12`, `"FECHAR MEU PEDIDO"`, e o fecho social: `"+50.000"` / `"PESSOAS JÁ VESTEM A CENA"` com seis depoimentos curtos em grade.

**#8 — desconto sem valor declarado, texto puro.** Igual ao #6a com uma troca: `"I saved your item and your discount for you just in case. Use code "DISCOUNT" at checkout to claim."` Sem prazo.

**Site Abandon #1 — convite, não recuperação.** Peça única, 600x3057. `"Chega mais, Preparamos isso pra você:"`, `12` `%` `OFF`, `"48h"` `"valido"` `"Por"`, cupom `VOLTEI12`, CTAs `"VOLTAR PRA LOJA"` / `"VER PRODUTOS"`.

# A escada de concessão não existe

Peça a peça: **10% no #1, 10% no #3, 10% no #4, 10% no #5, 12% no #6, 12% no #7.** O #2 e o #6a não têm oferta; o #8 tem código `"DISCOUNT"` sem valor.

1. **O desconto abre a sequência, não a fecha.** Não há lembrete neutro — a primeira peça já é oferta, disfarçada de curiosidade.
2. **Dois pontos percentuais em nove e-mails.** Quem esperou até o fim ganhou 2% a mais que quem comprou no primeiro. A sequência não treina o cliente a esperar.
3. **A escalada é em outros eixos.** Prazo entra no #3 (contador) e volta no #5; escassez só no #5. A prova cresce: três depoimentos no #1 → rating agregado + depoimento longo no #4 → `"+50.000"` e seis depoimentos no #7.

A trilha de texto puro tem escada própria e invertida: #2 sem oferta e sem prazo → #6a sem oferta e com prazo → #8 com oferta e sem prazo.

# O que distingue #6 de #6a

**Nó, formato, idioma, oferta e função são todos diferentes.** `#6` é `node 2989:116`, desenhada 600x3088, em português, com `12%OFF` e `DESCONTO12`. `#6a` é `node 1032:1108`, texto puro 800x727, em inglês com `[Brand]`, sem desconto, com prazo de 24h e apelo de suporte. Não é a mesma peça em duas versões: são duas peças distintas no mesmo número de passo.

A numeração de nó reforça: os três textos puros — `1032:1102` (#2), `1032:1105` (#8), `1032:1108` (#6a) — são consecutivos no mesmo bloco. Foram criados juntos, como conjunto de templates, e depois encaixados em slots. O sufixo `a` marca encaixe posterior, não variante desenhada em paralelo.

**O que não dá para saber:** se é ramificação condicional (quem não abriu/clicou o #6), split A/B ou inserção intermediária. Nenhuma condição, regra de split ou percentual de tráfego consta. `[não consta na fonte]`.

# Componentes fixos — a biblioteca reutilizável

**Barra de navegação** (`y=16`, toda peça desenhada): `MAIS VENDIDOS` · `MASCULINO` · `MOLETOM` · `FEMININO`.

**Barra de confiança de três selos**, sempre abaixo de um CTA. Em #3, #4, #5, #6 e no Site Abandon. Verbatim:

> `ENTREGA PRA TODO O BRASIL` — `"Frete calculado no checkout. Sem surpresa no final, como tem que ser."`
> `TROCA SEM BUROCRACIA` — `"7 dias. Sem formulário de 3 páginas. Sem drama. Só avisa a gente."`
> `PAGAMENTO SEGURO` — `"Checkout protegido. Cartão, Pix ou boleto do jeito que você preferir."`

**Bloco de cupom**: rótulo `CUPOM:` colado ao código em display, seguido de botão. Códigos semânticos por flow — `DESCONTO10`, `DESCONTO12`, `VOLTEI12` (site), `EXCLUSIVO12` (browse).

**Bloco dinâmico**: `[in-klaviyo Dynamic Product section]` em todas as desenhadas, às vezes duplicado na mesma peça (#1, #3) — sugere split ou fallback.

**`Unsub Info`** sempre em `y=415`, mesma coordenada em peças de altura diferente.

**CTAs em escada, texto diferente a cada aparição**, nunca repetindo dentro da peça. #1: `QUERO VER MINHA SURPRESA` → `GARANTIR DESCONTO` → `FECHAR MEU PEDIDO AGORA`. #3: `ADQUIRIR AGORA` → `GARANTIR DESCONTO` → `CONFIRMAR PEDIDO E FINALIZAR`.

**Contador regressivo** `01 : 59 : 47` com `HORAS` / `minutOs` / `SEGUNDOS` — mesmo valor nas duas peças que o usam. Se é dinâmico ou imagem, `[não consta na fonte]`.

# Site abandon: o que muda quando a intenção é mais fraca

- **Uma peça, não nove.**
- **Desconto maior de largada**: 12%/48h contra 10% sem prazo do carrinho. Quem tem carrinho montado recebe a oferta menor — inversão de margem que vale checar por cliente.
- **Prazo declarado em texto**, não em contador.
- **Sem bloco dinâmico** — coerente, a pessoa não viu produto.
- **CTA de exploração, não de conclusão**: `VOLTAR PRA LOJA`, `VER PRODUTOS`. Nada de finalizar, confirmar ou fechar pedido.
- **Sem prova social, sem contador, sem escassez.**
- **Mantém** nav bar, `Unsub Info` e a barra de três selos.

# O que a estrutura NÃO faz

- **Não separa cart abandon de checkout abandon.** Não há uma única peça de checkout na coleção.
- **Não declara delay, filtro, supressão ou saída.** `[não consta na fonte]`.
- **Não oferece frete grátis nem brinde.** O incentivo é só percentual — e o frete pago vira argumento de transparência.
- **Não usa valor absoluto (R$)**, só percentual.
- **Não usa voz de fundador assinada.** Os textos puros assinam `"The [Brand] Team"`; as desenhadas não assinam. Contrasta com [[a-voz-do-fundador-como-formato]].
- **Não traz subject lines.** `[não consta na fonte]`.
- **Não localiza os textos puros** — três das nove peças em inglês com placeholders.
- **Não termina as headlines.** Placeholder `Headline` cru em #4, #5 e #6 (duas vezes); `Headline` e `Body Copy` no Site Abandon, a peça menos escrita da coleção.

**Inconsistências a corrigir na replicação:** o #4 assina o depoimento como `"Lucas M."` e a resposta da marca começa `"Rafael, é exatamente isso."`; o #4 anuncia `"E AGORA COM 10% OFF."` sendo que 10% roda desde o #1; e o #5 declara `"Esse é nosso ÚLTIMO email sobre seu carrinho"` com quatro peças ainda por vir.

# Onde a prática da casa bate e onde diverge

Cruzado com [[cart-checkout-abandon]] e [[site-abandon]] (Max Sturtevant) e [[padroes-de-abandono-e-transacional]] (Well Copy).

**Divergência principal — volume. 9 contra 4.** O Max é explícito: quatro e-mails para cart e quatro para checkout, como dois flows separados. A casa usa nove num flow só e não tem flow de checkout. Não é divergência de detalhe: dobra a sequência e elimina o corte por intenção que é a tese central da aula dele.

**Divergência — onde entra o desconto.** Max põe no e-mail 3, atrás de um lembrete neutro e de um text-based. A casa abre com desconto no #1. O "lembrete simples" do Max não existe no padrão da casa.

**Divergência — densidade.** Max: `"Keep it as simple as possible… the discount should be the main aspect of the email"` e `"Avoid too many CTAs that will cause overwhelm"`. As peças da casa têm 3.088 a 4.073 px, dois a três CTAs, prova social, barra de confiança e educação.

**Divergência — frete grátis e remetente.** Max manda incluir threshold de frete grátis e prefere remetente pessoa física. A casa não tem threshold e não nomeia remetente.

**Divergência — desconto em site abandon.** O corpus do Max não traz desconto algum nesse flow. A casa dá 12%/48h na primeira peça. Concordância no volume: ele prescreve 1 a 2, a casa usa 1.

**Concordância — text-based na sequência.** Max prescreve dois dos quatro em texto puro. A casa usa três, e o #2 é praticamente o "personal reminder" dele — os três parecem derivados diretos desse template ou da base Klaviyo.

**Concordância — bloco dinâmico e CTA acima da dobra.** `[in-klaviyo Dynamic Product section]` em todas as desenhadas, primeiro botão em `y≈578-674`, acima do bloco dinâmico. Bate com `"Have the button and dynamic content at the very top of the email"`.

**A headline que a Well Copy declara vencedora** é `"Your Order Is Ready To Ship!"` — e o Max registra a mesma frase como subject do e-mail 1. A casa executa o mesmo mecanismo em português: `"ESTAMOS EMBALANDO"` / `"SEU PEDIDO"`, `"Reservamos pra você:"`, `"Itens separados pra você:"`. **Mas no terceiro e-mail, não no primeiro.** Duas fontes independentes apontam essa frase como abertura; a casa a usa como reforço.

**Desconto misterioso — a casa flerta e não executa.** A Well Copy documenta a neutonic: código `MYSTERY`, valor nunca dito, `"Access expires in 24 hours"`. A casa promete `"PRESENTE DOURADO"` no #1 e revela `10%OFF` / `DESCONTO10` na mesma peça — curiosidade como embalagem, não oferta oculta. O único código sem valor é `"DISCOUNT"` no #8, e é template em inglês. A mesma referência chama `MYSTERY` de tão estático quanto `WELCOME10`: `DESCONTO10` e `DESCONTO12` são exatamente essa classe. Ver [[curiosidade-e-oferta-oculta]].

**Concordâncias de execução com a Well Copy**, todas fortes: barra de três selos logo abaixo do botão principal; três CTAs por peça com texto diferente em escada; educação e prova social depois do primeiro CTA; carrinho como bloco dinâmico e não copy; prova social com nome próprio. A adaptação brasileira troca `"Free Shipping On Orders Over $140"` e `"90 Day Money Back Guarantee"` por `ENTREGA PRA TODO O BRASIL` e `TROCA SEM BUROCRACIA`, com Pix e boleto.

**O que a casa acrescenta às duas fontes:** contador regressivo em display, bloco `AVISO FINAL:` com escassez de estoque, rating agregado com contagem de avaliações e resposta da marca ao depoimento. Nada disso aparece em Max nem em Well Copy. Ver [[urgencia-fabricada-por-formato]] e [[formato-da-prova-social]].

**Convergência por omissão:** nem o Max declara delays para cart/checkout, nem esta fonte. Não há o que comparar.

# O que esta nota não prova

**Uma implementação, não um padrão medido.** O material documenta a Ride Nation e mais nada. Que a estrutura se replique entre clientes é afirmação da casa — o artefato não a demonstra, porque é um Figma de um cliente só.

**Nenhum número.** Não há taxa de abertura, clique, conversão, receita, amostra, período ou teste em lugar algum da fonte. `"4.9/5 (12.847 avaliações)"` e `"+50.000"` são claims de marca dentro da copy, não medição do flow. Nada compara 9 e-mails contra 4, 10% contra 12%, ou peça desenhada contra texto puro. Não há A/B declarado, nem para o par `#6` / `#6a`.

Isto é padrão de execução — o que a casa monta e como monta. Não é evidência de que funciona melhor que a alternativa. Mesma limitação da coleção Well Copy, e vale a mesma ressalva.
