---
tipo: indice
assunto: convertfy
autor: convertfy
status: aprovado
---

Porta de entrada do que a Convertfy faz, e não do que os outros ensinam. Reúne as estruturas de flow que a casa monta para cliente — welcome, abandono de carrinho e de navegação, winback, pós-compra e a cadeia transacional — extraídas de uma implementação real. É o corpus de maior autoridade da base quando houver medição nossa, e o único que descreve execução em vez de doutrina.

# O que tem aqui

| Nota | O que documenta |
|---|---|
| [[estrutura-do-welcome-flow]] | 8 e-mails, do cupom de boas-vindas à última chance |
| [[estrutura-do-cart-abandon]] | 9 e-mails de carrinho + 1 de site abandon |
| [[estrutura-de-browse-abandon-e-winback]] | 5 de navegação + 2 de reativação |
| [[estrutura-do-pos-compra-e-transacionais]] | 4 de pós-compra + a cadeia de 4 estados de pedido e o caminho de exceção |
| [[componentes-recorrentes-do-email]] | a biblioteca de blocos que se repete entre as peças |
| [[manual-da-marca-ride-nation]] | paleta, tipografia, botões e selos do cliente documentado |

# O que este corpus prova, e o que não prova

**Prova:** que existe um padrão de execução da casa, repetido e reconhecível. A evidência mais dura disso é mecânica — o marcador `Unsub Info` cai no mesmo pixel (`y=415`) em 22 layouts cujas alturas variam de 1.549 a 4.837px. Isso é biblioteca de componentes, não coincidência.

**Não prova:** que o padrão converte. **Não há um único número anexado** ao material — nem taxa, nem receita, nem teste, nem comparação. A IA pode dizer "é assim que a Convertfy monta"; **não pode dizer que essa estrutura performa melhor**, nem citar magnitude.

**E documenta uma implementação só.** A afirmação de que estas estruturas se replicam entre vários clientes é da casa. O artefato mostra um caso — Ride Nation, streetwear, ticket R$100-250, Brasil.

# Onde a casa tem doutrina própria

Um ponto em que a Convertfy vai além das duas fontes externas da base: **a cadeia transacional de quatro estados** — pedido pago, em separação, em coleta, enviado — mais um caminho de exceção para atraso. O corpus do Max tem só um "Order On The Way" opcional, sem template e fora do flow. A coleção da Well Copy tem uma única confirmação customizada, que a própria base já marcava como território novo.

Daí sai também uma regra editorial que a casa segue sem ter escrito: **o transacional pode oferecer produto, não pode oferecer preço.** Os quatro estados trazem grade de produtos com botão de compra, e nenhum deles usa cupom, percentual, contador, escassez, depoimento ou barra de confiança — recursos que existem no arsenal da mesma implementação e foram deliberadamente deixados de fora.

# A escada de desconto, e a inversão que ela contém

| Flow | Desconto |
|---|---|
| Welcome | 10% |
| Cart abandon | 10% → 12% |
| Site abandon | 12% |
| **Browse abandon** | **12% → 14%** |
| Pós-compra | 17% |

**Browse abandon dá mais desconto que cart abandon** — quem só olhou recebe 14%, quem chegou a colocar no carrinho recebe 12%. É uma inversão em relação à intenção de compra, e contraria [[browse-abandon]], onde o desconto entra no e-mail 3 de 4 e ainda é marcado como opcional. Pode ser deliberado; a fonte não diz. Apresente sempre como divergência, nunca como consenso.

# Cuidado ao ler: o arquivo é projeto em andamento

Parte do material são **templates comprados que nunca foram preenchidos nem traduzidos**, e não podem ser citados como copy da casa:

- As peças de "texto puro" (formato 800x727) estão **em inglês**, com `[Brand]`, `[Insert brand info and unique selling propositions]` e `"DISCOUNT"` como código literal.
- Os quatro estados transacionais **só diferem no hero** — o corpo é o mesmo nos quatro, assinado `Sabel, equipe {{ organisation.name }}`, com miolo em inglês, dólar e um produto chamado `Gather Phone Stand $39.00`.
- A peça chamada **"Atraso na entrega" não trata de atraso**: dentro dela está o template `Email 9: Everything All Good?`, idêntico palavra por palavra ao Winback #3.
- Há resíduo de **pelo menos três templates de origem diferentes** no mesmo arquivo: `[Brand]`, `MISSYA10` e `Sabel` / `Gather Phone Stand`.
- Doze das 23 peças desenhadas ainda têm placeholders `Headline`, `Body Copy` ou `Subheadline` vazios.

**A arquitetura dos flows é o ativo. A copy das peças não preenchidas não é.**

# Defeitos de produção a corrigir antes do próximo cliente

Encontrados na leitura, todos verificáveis no material bruto:

- **Prova social contraditória na mesma conta:** `+25,000` (Welcome #1) contra `+50.000` (Cart #7); `4.8/5 de 2,847 reviews` contra `4.9/5 (12.847)` contra `4.9/5.0`.
- **Duas promessas de frete incompatíveis:** o selo do manual diz `"Frete Grátis Acima de R$89,90"`, a barra de confiança que roda em 12 e-mails diz `"Frete calculado no checkout"`.
- **`EXCLUSIVo12`** — o cupom `EXCLUSIVO12` aparece com "O" minúsculo no Browse #3. Falha funcional se o checkout for case-sensitive.
- **Escassez sem mecânica:** `"Restam apenas 13 códigos"` dito sobre um código estático e idêntico para toda a lista.
- **Prazos contraditos pela própria sequência:** `"SOMENTE ATé hoje, 11:59 p.m."` no Welcome #2, seguido de seis e-mails com o mesmo cupom; e o Cart #5 declara ser o último com quatro peças por vir.
- **Depoimento cruzado:** assinado `"Lucas M."` com resposta dirigida a `"Rafael"` (Cart #4).
- **No manual da marca:** o swatch `"Azul · #0018FF"` está renderizado preto, e o swatch `"Branco"` traz o hex `#000000`. O círculo do branco está correto — só o hex está errado, o que torna o defeito invisível para um humano e fatal para leitura literal.

# Como crescer este corpus

O material bruto fica em `Admin Convertfy/CONTEUDO BRUTO/ride-nation/`, com a copy das 34 peças reconstruída e o manual capturado.

O que mais aumentaria o valor desta pasta, em ordem: **número de performance** de qualquer um destes flows (transforma o corpus inteiro de padrão em medição), **anti-exemplo** — o que a casa recusou e por quê —, e uma **segunda implementação** de cliente, que é o que permitiria separar o que é padrão do que é específico da Ride Nation.

Molde e regras em `Padrao Convertfy/como-escrever-uma-nota.md`.
