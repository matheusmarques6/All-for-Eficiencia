---
tipo: especificacao
assunto: estrutura-welcome-flow
autor: convertfy
status: aprovado
fonte: 'Figma "ESTRUTURA FIGMA — RIDE NATION" — implementação Convertfy, 8 e-mails de welcome, extraído em 2026-09'
---

O welcome flow que a Convertfy monta tem oito e-mails: sete peças desenhadas e uma de texto puro no fim. Todos carregam o mesmo cupom de 10% (`BEMVINDO10`), e cada peça ataca um ângulo diferente para justificar a mesma oferta — boas-vindas e missão, por que a marca, a origem, lembrete, comparação com o concorrente, escassez, última chance e um check-in de suporte. A urgência entra cedo, no segundo e-mail, e escala até o sétimo. O caso documentado é a Ride Nation (streetwear/ciclismo, ticket R$ 100-250, Brasil). Esta nota transcreve os componentes fixos verbatim, porque eles são biblioteca reutilizável, e registra o que a estrutura deliberadamente não faz.

# A sequência: o que cada e-mail faz que o anterior não fez

| # | Função | Figma | Movimento novo |
|---|---|---|---|
| 1 | Boas-vindas + cupom + missão | 600x3775 | dá o código e diz o que a marca é |
| 2 | "Por que Ride Nation?" | 600x3887 | vira a barra de confiança em argumento; **1ª urgência** |
| 3 | A origem | 600x3013 | narrativa de fundação, 2018, sem vender |
| 4 | Lembrete + prova social nominal | 600x2722 | pergunta se ainda quer; nome e nota de cliente |
| 5 | Us vs. them | 600x2709 | ataca a alternativa, não a marca própria |
| 6 | Escassez + janela de 12 horas | 600x3075 | nº de pessoas e de códigos restantes |
| 7 | Última chance | 600x1549 | peça despida: urgência, cupom, botão |
| 8 | Check-in de texto puro | TEXTO PURO 800x727 | sai do template, fala como pessoa, estende a oferta |

**#1** — `"Bem-vindo À"` / `"Ride Nation"`, CTA `"COMPRAR COM 10% OFF"` a 638px do topo de 3775: botão antes de qualquer scroll. Só depois a missão: `"Nossa missão: vestir quem vive a cena através de peças que funcionam como código de tribo. Com a Ride Nation, você garimpa sem firula — e sai do checkout com algo que a crew reconhece de longe."`

**#2** — abre com o cupom (y=630) antes de qualquer argumento e desenvolve quatro razões numeradas: `"Qualidade que aguentam o rolê de verdade"`, `"Preço Justo"`, `"CONVENIÊNCIA"`, `"Troca sem burocracia"`. É a barra de confiança de #1 expandida em parágrafo. Único e-mail que cita o ticket: `"Ticket entre R$ 100 e R$ 250 com qualidade que justifica cada real."`

**#3** — bloco único e longo: `"De um problema real ao uniforme da crew Em 2018, a galera que vivia na pista, no asfalto e na cena não tinha opção real de vestuário."` (…) `"A decisão foi simples: criar do jeito que a gente queria encontrar."` Único sem barra de confiança e com CTA que não vende: `"DESCOBRIR NOSSA JORNADA"`, `"EXPLORAR COLEÇÃO"`.

**#4** — headline em pergunta, `"Ainda Quer Seus"` / `"10%OFF?"`, e três depoimentos com nome e nota 5.0: `"Comprei a primeira peça sem saber muito e hoje já tenho cinco."` (Lucas M.), `"Tinha receio com o tamanho comprando online, mas a tabela bate certinho."` (Marina L.), mais Gabriel R. Um quarto nome, `"Beatriz P."`, aparece sem depoimento.

**#5** — `"A Ride Nation não é loja de roupa."` / `" É loja pra quem tem cena."` Duas colunas, `ride nation` contra `Outras lojas`: `Envio Nacional`/`Qualidade Garantida`/`Modelos para todos os gostos`/`Durabilidade e Autenticidade` contra `Tempo longo de entrega`, `Baixa qualidade`, `Produtos falsificados`, `Modelos limitados`, `Site questionável`, `Pagamento suspeito`, `Sem transparência`.

**#6** — `"Últimas 12 horas do seu"` / `"desconto exclusivo"`, mais dois números: `"387 pessoas"` `"já usaram o BEMVINDO10 essa semana."` e `"Restam apenas 13 códigos"`. Três depoimentos novos (Diego M., Thiago R., Juliana R.) — prova social renovada, não reciclada de #4.

**#7** — a peça mais curta (1549px contra ~3000 de média) e a única sem navegação e sem `Unsub Info`. Só `"SEU ACESSO EXCLUSIVO ESTÁ EXPIRANDO"`, o `10 % OFF` em display, `"ÚLTIMA CHANCE"`, dois `Body Copy` vazios, cupom e `"GARANTIR 10%"`.

# A biblioteca fixa — copy verbatim, reutilizável

**Barra de navegação** (#1 a #6, y=16; ausente em #7 e #8):
`MAIS VENDIDOS` · `MASCULINO` · `MOLETOM` · `FEMININO`

**Barra de confiança** (#1, #4, #6 — três colunas com título e subtítulo):
- `ENTREGA PRA TODO O BRASIL` — `"Frete calculado no checkout. Sem surpresa no final, como tem que ser."`
- `TROCA SEM BUROCRACIA` — `"7 dias. Sem formulário de 3 páginas. Sem drama. Só avisa a gente."`
- `PAGAMENTO SEGURO` — `"Checkout protegido. Cartão, Pix ou boleto do jeito que você preferir."`

A mesma copy aparece em outras peças do mesmo arquivo (Site Abandon) — é componente de biblioteca, não texto de welcome.

**Bloco de cupom** (#1 a #7): rótulo `CUPOM:` (em #5 minúsculo, `cupom:`) + `BEMVINDO10` + botão. Em #1 vem acompanhado da linha `"por tempo limitado"`.

**Prova social agregada** (#1): `"+25,000"` / `"clientes satisfeitOs"` · `"Cliente verificado"` · `"4.8/5 de 2,847 reviews verificados"` · depoimento `"Pedi esperando mais do mesmo. Chegou diferente. A estampa segurou depois de um monte de lavagens e a crew perguntou onde comprei."`

**Slot de descadastro**: linha `Unsub Info` em posição fixa (y=415) nas peças #1 a #6.

Erros de digitação preservados porque estão no arquivo: `"SOMENTE ATé hoje"`, `"GARRAR COM 10% OFF"`, `"clientes satisfeitOs"`.

# A urgência: onde nasce e como escala

A urgência aparece **já no e-mail #2**, com prazo duro: `"SOMENTE ATé hoje, 11:59 p.m."` Depois: #4 em forma branda de pergunta (`"Ainda Quer Seus 10%OFF?"`), #6 com janela e estoque (`"Últimas 12 horas"`, `"Restam apenas 13 códigos"`), #7 em terminalidade (`"EXPIRANDO"`, `"ÚLTIMA CHANCE"`) e #8 revogando tudo com extensão (`"we wanted to extend your discount for one more day"`).

Duas incoerências internas: o prazo de #2 encerra "hoje" e o flow segue por mais seis e-mails com o mesmo cupom; e `"Restam apenas 13 códigos"` é dito sobre um código estático, igual para toda a lista — a escassez é retórica, não mecânica.

# O e-mail de texto puro

É o **#8, último da sequência**, e é o único fora do template desenhado. Não tem navegação, barra de confiança, bloco de cupom estilizado nem rodapé: é parágrafo corrido numa captura 800x727. Funciona como check-in de suporte, não como venda — reconhece que a pessoa não usou o desconto, estende o prazo e abre canal de resposta: `"We noticed that you haven't used your welcome discount - but we don't want you to miss it... Since you're new to the club, we wanted to extend your discount for one more day!"` e `"Feel free to reply to his email if you have any questions!"` (o typo `his` está na fonte).

**Ressalva de rigor:** esta peça está em inglês, com marca genérica `[Brand]` e código `WELCOME10` — não `BEMVINDO10`. No arquivo, ela é template não-localizado, não copy final da Ride Nation. A versão em português não consta na fonte.

# Um cupom, sete formas de pedir

`BEMVINDO10` aparece nos sete e-mails desenhados, sempre com o mesmo valor de 10%. **A oferta nunca muda; o verbo do pedido muda em toda peça** — e é essa rotação que impede a repetição de soar repetição. A escada dos CTAs, verbatim e na ordem do flow:

`COMPRAR COM 10% OFF` · `APROVEITAR AGORA` (#1) → `GARANTA JÁ` · `RESGATAR DESCONTO` (#2) → `DESCOBRIR NOSSA JORNADA` · `EXPLORAR COLEÇÃO` (#3) → `GARANTIR MEUS 10%OFF` (#4) → `GARIMPAR AGORA` (#5) → `USAR DESCONTO` · `GARRAR COM 10% OFF` · `USAR MEU DESCONTO` (#6) → `GARANTIR 10%` (#7) → `SHOP NOW >>` (#8).

O movimento é de descoberta (`DESCOBRIR`, `EXPLORAR`, `GARIMPAR`) para posse (`GARANTIR`, `RESGATAR`) e finalmente para uso (`USAR MEU DESCONTO`) — como se o cupom já fosse da pessoa e só faltasse gastá-lo.

# O que a estrutura NÃO faz

- **Não personaliza.** Nenhum token de nome em nenhum dos oito. Outras peças do mesmo Figma usam `{{ first_name|default:'there' }}`; o welcome, não.
- **Não usa código único por pessoa.** `BEMVINDO10` é estático para toda a lista.
- **Não tem bloco dinâmico de produto.** O marcador `[in-klaviyo Dynamic Product section]` existe no Browse Abandon do mesmo arquivo e em nenhum welcome.
- **Não assina com pessoa.** O texto puro fecha em `"The [Brand] Team"`; não há remetente nomeado em peça alguma.
- **Não segmenta.** Uma trilha só, sem variante por pop-up, gênero ou categoria — apesar de a navegação separar `MASCULINO` e `FEMININO`.
- **Não pede nada além da compra.** Sem SMS, sem redes, sem quiz, sem centro de preferências, sem expectativa de frequência.
- **Não traz subject lines.** O artefato é só corpo de e-mail. `[não consta na fonte]`
- **Não traz delays.** O Figma não informa o intervalo entre os e-mails, nem se o #1 dispara imediatamente. `[não consta na fonte]`
- **Peças inacabadas:** `Body Copy` e `Headline` permanecem como placeholder em #2, #3, #6 e #7.

# Onde a prática da casa bate e onde diverge

Comparação com a doutrina de [[welcome-flow]], [[welcome-templates]] e [[welcome-fillers]] (Max Sturtevant) e com a coleção [[padroes-do-welcome-flow]] (Well Copy).

**Bate — desconto em todos os e-mails.** Non-negotiable do Max: "Remind of welcome discount in every email". A casa cumpre 8/8.

**Bate — desconto e botão acima da dobra**, como no hero prescrito por [[welcome-templates]] e no Medicamentum da Well Copy.

**Bate — existe last chance e existe texto puro.** Duas das sete non-negotiables; e o #7 executa o "no need to go crazy right here": a peça mais curta, sem nav.

**Bate — os fillers são do catálogo.** #3 é `Our story`, #4 é `Social proof`, #5 é `Us vs Them`, #2 é "how we're different". Quatro fillers, dentro da faixa 1-5 de [[welcome-fillers]].

**Bate — o texto puro tem a mesma linhagem.** O #8 é quase o Pedal Commander de [[padroes-do-welcome-flow]]: "I hope our previous emails have been a warm welcome…" contra "I hope my previous emails have given you a taste of…" — mesma matriz.

**Diverge — contagem no teto.** Oito e-mails. O Max dá piso 3, "sweet spot" 4-5 e 6-8 só para produto que pede educação; streetwear de R$ 100-250 é compra de impulso pelo critério dele, e a casa usa a faixa alta mesmo assim.

**Diverge — remetente sem nome.** [[welcome-templates]] exige "it's coming from an actual person, from Sarah" e P.S. de suporte; o #8 assina como time.

**Diverge — urgência antecipada.** No desenho do Max, o e-mail #2 apenas "lembra que a oferta não fica disponível para sempre"; a casa já dá prazo duro (`"SOMENTE ATé hoje, 11:59 p.m."`) e depois o contradiz por seis e-mails.

**Diverge da Well Copy — código estático e sem split.** A Well Copy defende código que pareça calculado (`HI-4XY7G`); a casa fica com `BEMVINDO10`, do lado do Max — e a peça da própria Well Copy usa `WELCOME10` no fecho, então a divergência é com o racional dela, não com a prática. Também não há nada equivalente ao Salt Lab (quatro versões por resposta de pop-up) nem ao quiz de recaptura.

**Não comparável — cadência.** O Max prescreve #1 imediato e 1-2 dias de intervalo; o Figma não registra tempo. `[não consta na fonte]`

# O que este material não prova

1. **É uma implementação, não uma amostra.** A Convertfy declara que replica esta estrutura em vários clientes; o artefato mostra um caso, a Ride Nation. A generalização é da casa, não do documento.
2. **Não há um único número de performance.** Nem abertura, nem clique, nem receita, nem teste A/B, nem período. `"+25,000 clientes satisfeitOs"` e `"4.8/5 de 2,847 reviews verificados"` são copy de venda, não medição de flow. **Esta nota é padrão de execução, não evidência de conversão** — não a use para afirmar que esta estrutura converte mais que outra.
