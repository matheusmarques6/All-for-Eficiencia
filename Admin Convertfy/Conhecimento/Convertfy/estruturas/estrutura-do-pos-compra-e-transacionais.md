---
tipo: especificacao
assunto: estrutura-pos-compra-transacionais
autor: convertfy
status: aprovado
fonte: 'Figma "ESTRUTURA FIGMA — RIDE NATION" — implementação Convertfy, 4 peças de pós-compra + 5 transacionais, extraído em 2026-09'
---

O padrão da casa depois da compra tem duas camadas que não se misturam: um pós-compra de quatro peças que vende com cupom escalonado, e uma cadeia transacional de quatro estados de pedido — pago, em separação, em coleta, enviado — mais um caminho de exceção para atraso. O transacional é peça de marketing: leva grade de produtos com botão, navegação e suporte, mas nunca cupom, contador ou prova social. Esta nota especifica o que cada estado comunica, o que é componente fixo e o que a estrutura não faz.

Implementação de referência: Ride Nation (streetwear/ciclismo, ticket R$ 100–250, Brasil).

# A cadeia transacional: quatro estados e uma exceção

A casa não manda "um e-mail de confirmação". Manda quatro, um por estado, mais um quinto para quando o pedido fura o prazo. **Transacional é slot de mídia, não recibo.**

| Estado | Altura | Headline verbatim | O que só ele tem |
|---|---|---|---|
| Pedido pago | 600x2937 | `SEU PEDIDO` / `FOI APROVADO` | o mais curto; sem rastreio, sem botão duplo |
| Pedido em separação | 600x3299 | `SEU PEDIDO ESTÁ` / `em preparação!` | entra o par de botões (`✍️ Learn More`) |
| Pedido em coleta | 600x3299 | `ENVIADO PARA` / `TRANSPORTADORA` | ganha `Background Image` de topo |
| Pedido enviado | 600x3299 | `SEU PEDIDO` / `FOI ENVIADO` | dois parágrafos sob o hero |
| Atraso na entrega | texto puro 800x727 | *(sem hero)* | único de texto puro, único de exceção |

**O que muda entre eles:** só o hero e a moldura de rastreio. A progressão de headline é narrativa de posse — dinheiro, mãos, estrada, a caminho de você — e a altura vai de 2937 para 3299 quando entra o rastreio.

**O que se mantém nos quatro:** o mesmo esqueleto, na mesma ordem. Hero de marca → resumo do pedido (`Order details`, itens com miniatura e preço, `Sub-total` · `Delivery` · `Taxes` · `Total order amount:`) → datas (`Ordered on:` / `Arriving by:`) → **grade de cross-sell com botão por produto** → bloco de suporte → rodapé de navegação. A informação do pedido vem **depois** da tela de marca, nunca antes.

# Onde há venda dentro do transacional — e onde não há

**Há:** grade de quatro produtos, cada um com preço e botão próprio (`ButtonStyle03`), nos quatro estados, e o rodapé de categorias clicável. A casa monetiza o transacional com **catálogo e botão**, não com desconto.

**Não há, em nenhum dos quatro:** cupom, código, percentual, contador regressivo, escassez, depoimento, nota de avaliação, barra de confiança. Todos existem no arsenal — aparecem no pós-compra e no abandono da mesma implementação — e foram **mantidos fora**. A regra: *o transacional pode oferecer produto; não pode oferecer preço.*

# "Atraso na entrega": o único de exceção

A peça mais delicada da cadeia — e **o que está no Figma não é sobre atraso.** O frame chama-se `Atraso na entrega`, mas dentro dele está o template `Email 9: Everything All Good?`, o mesmo texto, palavra por palavra, do `Winback Email #3`:

> `Hey {{ first_name|default:'there' }}, I noticed it's been quite some time since your last purchase with us. I wanted to check in and make sure everything with your last purchase went okay. If it didn't, please let us know by replying to this email. (…) Use code MISSYA10 for 10% OFF when you order in the next 24 hours. Shop 10% OFF >> Thanks again for your support, [Founder Name] | [Brand Name]`

O que a estrutura decide, e o que ainda não decidiu:

- **Decidido — o formato.** Exceção sai em **texto puro, assinado por pessoa** (`[Founder Name] | [Brand Name]`). Frustração não se responde com banner.
- **Decidido — o canal de escape.** `please let us know by replying to this email`. Pede resposta, não clique: único ponto da cadeia que convida ao reply.
- **Decidido — há compensação.** Um cupom (`10% OFF`). É a única peça pós-venda em que desconto é reparação, não oferta.
- **Não decidido — a desculpa.** O texto **não pede desculpa, não explica o atraso e não dá previsão nova**. Pergunta se está tudo bem com a compra anterior — pergunta de winback, não de crise logística.
- Gatilho, janela de atraso e prazo de disparo: `[não consta na fonte]`.

**Prescrição:** o slot existe e o formato está certo (texto puro + pedido de resposta + compensação). A copy é placeholder herdado e **tem que ser reescrita por cliente** com três movimentos que faltam: reconhecer o atraso, explicar a causa em uma linha, dar prazo novo. Só depois o cupom.

# Os quatro de pós-compra

Distinguem-se do transacional por não terem estado de pedido: sem resumo, sem datas, sem rastreio. São venda pura sobre a janela quente, e os três desenhados formam **uma escada de um único cupom** — `ESPECIAL`, `17% OFF` — reenquadrado três vezes.

1. **#1 — a revelação** (600x4107). Apresenta o cupom e o justifica com prova: `70%` / `dos clientes da Ride Nation` / `voltam pra uma segunda peça em menos de 30 dias e não é por acaso. (…) Você fez a escolha certa. Agora a gente facilita a próxima.` Regras explícitas: `Válido por 7 dias | Aplicável em qualquer peça do site`. Fecha com escassez: `Toda vez que liberamos cupom pra quem já comprou, o estoque das peças mais pedidas some antes do prazo acabar.`
2. **#2 — a urgência** (600x4837). Mesmo cupom com `EXPIRA hoje`, contador (`23` `:` `59` `:` `47`) e inventário de perda: `Você tá deixando isso na mesa:` + quatro linhas (`17% de economia em qualquer peça da loja`, `Chegar antes da galera na peça que vai sumir`).
3. **#3 — a última chance** (600x3009). Encurta e fecha: `VÁLIDO POR APENAS` `24h`, `Última chance de economizar` `17%OFF`, `Depois de hoje às 23:59h`. É o único dos três com barra de confiança.
4. **#4 — o fundador** (texto puro 800x727). Agradecimento, missão, e-mail de suporte, `Not done? Keep shopping here >>` e `PS - This is my favorite of ours right now >>`. **Também está no template original em inglês, com colchetes por preencher** — mesma pendência do "Atraso na entrega".

# Componentes fixos — biblioteca reutilizável

**Navegação** (topo das peças de marketing e rodapé dos quatro transacionais):

> `MAIS VENDIDOS` · `MASCULINO` · `MOLETOM` · `FEMININO`

**Barra de confiança de três selos** (pós-compra #3, abandono, welcome, winback — **ausente no transacional**):

> `ENTREGA PRA TODO O BRASIL` — `Frete calculado no checkout. Sem surpresa no final, como tem que ser.`
> `TROCA SEM BUROCRACIA` — `7 dias. Sem formulário de 3 páginas. Sem drama. Só avisa a gente.`
> `PAGAMENTO SEGURO` — `Checkout protegido. Cartão, Pix ou boleto do jeito que você preferir.`

**Bloco de cupom.** Dois textos empilhados: rótulo `CUPOM:` (ou `cupom:`) + código em caixa alta. Repetido 2 a 3 vezes por peça, com CTA diferente a cada aparição — em #1: `USAR MEU DESCONTO` → `USAR MEU DESCONTO DE 17%` → `USAR MEU DESCONTO AGORA`.

**Prova social.** Aspas + primeiro nome e inicial (`Rafael M.`), às vezes cidade (`Caio T. - Curitiba/PR`) e nota (`5.0`, `4.9/5.0` / `avaliação média dos nossos clientes`). Nunca no transacional.

**Suporte, só no transacional:** `Devoluções de produtos` + `Você tem alguma  pergunta?` (dois espaços, verbatim). **`Unsub Info`** aparece em toda peça desenhada, em `y=415`.

# O que a estrutura NÃO faz

- **Não ensina a usar o produto.** Nenhuma peça de onboarding, cuidado, tabela de medidas ou lavagem entre os nove.
- **Não pede review nem UGC.** Nenhum CTA de avaliação depois da entrega.
- **Não ramifica** por número de compras nem por produto comprado.
- **Não pede resposta** — exceto na peça de exceção.
- **Não fecha o ciclo.** Depois de "Pedido enviado" não há "chegou?", nem confirmação de entrega.
- **Não diferencia o corpo por estado.** Nos quatro transacionais o parágrafo do corpo é literalmente o mesmo, o de separação: `Olá {{ first_name }}, Boas notícias! Seu pedido já está sendo preparado em nosso armazém. (…) Atenciosamente, Sabel, equipe {{ organisation.name }}`. `Sabel` é resíduo do template de origem. **Corpo por estado é obrigação de reescrita antes de subir.**
- **Não localizou o miolo transacional.** Resumo, datas e cross-sell seguem em inglês e dólar do template-mãe: `Sub-total` `$60.00`, `Arriving by: October 12-17, 2024 Via UPS`, itens `Gather Phone Stand $39.00`, cross-sell com lorem (`Morbi sed at a in velit mattis diam.`) e botões `✍️ Learn More`.

# Onde a prática da casa bate e onde diverge

**Doutrina própria — a cadeia de estados.** [[padroes-de-abandono-e-transacional]] registra que tratar a confirmação como peça de marketing ("Custom Order Confirmation", Instant Hydration) é **território novo, sem contraparte no corpus do Max** — [[post-purchase]] dispara em `Placed Order` e só cita um opcional "Order On The Way", que ele nem põe neste flow. A casa vai além das duas: **quatro estados desenhados mais um de exceção**, contra uma peça na Well Copy e um opcional sem template no Max. E monetiza mais fundo — a Instant Hydration só transforma o item em link, sem botão de compra. **É onde a prática da casa é a mais desenvolvida das três.**

**Concordância — inversão da ordem e escada de CTA.** A Well Copy observa que a confirmação "inverte a ordem esperada": hero de marca antes do resumo — os quatro transacionais da casa fazem o mesmo. E [[cart-checkout-abandon]] pede CTA com texto diferente a cada repetição; o pós-compra #1 executa isso.

**Concordância — fundador em texto puro.** [[o-fundador-nos-flows]] documenta o agradecimento pós-compra do fundador em texto puro com PS de upsell; o Max mede esse PS em "2% to 3% placed order rates". O pós-compra #4 é essa peça, com o mesmo PS — só que ainda no template, sem adaptação.

**Divergência — o e-mail 2 do Max não existe aqui.** [[post-purchase]] especifica o segundo pós-compra como instrução de uso, para reduzir devolução ("Reduce returns by ensuring customers know how to use their product"). A casa troca isso por urgência de cupom — **é a lacuna mais testável desta estrutura.**

**Divergência — sem split.** O Max chama de pro tip o split por número de compras, "so that it's not the same thing every time". A casa manda o mesmo `ESPECIAL` para todo mundo.

**Divergência — desconto onde as fontes usam conteúdo.** As três peças desenhadas de pós-compra são a mesma oferta reenquadrada; nas duas fontes externas o pós-compra é marca, história e uso. A casa aplica aqui a mecânica do abandono.

# O que esta nota NÃO prova

**Uma implementação, não um padrão medido.** O material documenta **um** cliente, um Figma, um momento. Que a estrutura se replique entre clientes é afirmação da casa — o artefato não prova isso, porque não há segundo cliente no material.

**Nenhum número anexado.** Não há aberto, clique, receita, conversão, teste A/B, controle, amostra ou período — nem para a cadeia transacional, nem para a escada de cupom. Os únicos números na fonte são **copy** (`70%`, `4.9/5.0`), não medição. É **padrão de execução, não evidência de performance.**

**Gatilhos e delays não constam.** Nenhuma peça declara metric, delay, filtro ou saída: `[não consta na fonte]`. Mapear contra [[mapa-dos-flows]] antes de montar no ESP.
