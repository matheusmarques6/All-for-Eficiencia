---
tipo: indice
assunto: conflitos-no-mesmo-registro-deliverability
autor: max-sturtevant
status: aprovado
---

Os dois conflitos do deck de deliverability do corpus Max em que o slide contradiz a si mesmo: o unsubscribe rotulado como métrica que não afeta a entrega e ao mesmo tempo listado entre as que os provedores olham, com meta na mesma célula (`deliverability-unsubscribe-afeta-ou-nao`), e os registros de DNS — quatro na prosa com MX, três na lista de requisitos (`deliverability-registros-dns`).

# Conflitos dentro do mesmo registro — unsubscribe e registros de DNS

A precedência do [[mapa-do-corpus-do-max]] — slide vence em especificação, fala vence em julgamento —
só funciona quando os **dois registros discordam entre si**. Boa parte dos conflitos
deste corpus é slide contra slide, no mesmo deck, às vezes na mesma linha. Aqui a
precedência não resolve, e o desempate, quando existe, é por **evidência de autoria
dentro do próprio material**.

**Consequência geral: não presuma que o slide fala com uma voz só.**

## deliverability-unsubscribe-afeta-ou-nao

O defeito cabe numa célula: a mesma linha da tabela diz que a métrica não afeta
deliverability e lhe dá meta. Três linhas antes, o mesmo deck a lista entre as que os
provedores olham.

| Versão | Valor | Registro | Linha |
|---|---|---|---|
| Está na lista do que os provedores olham | "Engagement rates. / That is all that Google, Yahoo, etc look at. / Open rates, click rates, bounce rates, **unsubscribe rates**, and spam complaint rates." — sob o título "All That Matters For Deliverability" | slide (deliverability) | L8706-8710 |
| Não afeta — e tem meta, na mesma célula | "\| Unsubscribe Rate **(doesn't affect deliverability)** \| Less than 0.4% \|" | slide (deliverability) | L8719 |
| A fala também o lista entre o que importa | "But all that matters, open rates, click rates, bounce rates, spam, complete rate, and then unsubscribe rate." | **outro-narrador** (deliverability) | L8430 |
| E o desmente na linha seguinte | "The unsubscribe is actually a neutral metric. It doesn't really affect deliverability, but it's a good thing to keep an eye on." | **outro-narrador** (deliverability) | L8432 |
| Para que a aula usa a métrica | "that's a really good indicator if you're sending too many emails, honestly, or if your filters are messed up in your flows, because people will start unsubscribing in droves" | **outro-narrador** (deliverability) | L8434 |

**Como responder:** o atrito existe **dentro de cada registro**, não entre eles. No
slide, o rótulo "(doesn't affect deliverability)" convive com a meta `Less than 0.4%`
na mesma célula (L8719), enquanto três linhas acima o unsubscribe está entre as cinco
coisas que "Google, Yahoo, etc look at" (L8710). Na fala é ainda mais apertado: L8430
o inclui em "all that matters" e L8432, imediatamente depois, o chama de "neutral
metric".

A leitura que concilia sem inventar nada é a que os dois registros já dizem: **é
métrica de monitoramento com alvo, não de deliverability.** "A good thing to keep an
eye on" (L8432) é literal, e o uso que a aula lhe dá é diagnóstico — frequência alta
demais ou filtro de flow quebrado (L8434), não caixa de spam.

Se a pergunta for "unsubscribe alto me manda para spam?", entregue as duas coisas: o
material diz que não, e ainda assim exige `< 0.4%` e mantém a métrica na lista do que os
provedores olham. **Não use o 0,4% como se fosse o teto do corpus** — é o valor de um
deck só; o mais sustentado é 0,3%. Ver `entre-modulos-tabela-de-metricas` e
`fundamentos-unsubscribe-glossario`.

**Ressalva de atribuição:** as três linhas faladas desta entrada (L8430, L8432, L8434)
estão em L8381-8517, `outro-provavel` por [[mapa-da-autoria]] — **não são citáveis como fala de
Max**. O que sobra dele é o deck (L8706-8710, L8719), e é justamente o deck que se
contradiz na própria célula. A leitura conciliadora acima é do material do curso, não
julgamento declarado dele. O conflito de slide contra slide (L8710 vs L8719) fica de pé
sozinho, sem depender dessa fala.
## deliverability-registros-dns

| Versão | Valor | Registro | Linha |
|---|---|---|---|
| Quatro, na prosa | "Fancy records hosted by your domain provider in your DNS settings (**MX, SPF, DMARC, DKIM**)" — sob "What Affects Deliverability?" | slide (deliverability) | L8671 |
| Três, na lista de requisitos | "Records you need on your domain for inbox placement:" → "SPF / DMARC / DKIM" | slide (deliverability) | L8685-8689 |
| Quem instala | "As you setup Klaviyo they set these all up for you :)" | slide (deliverability) | L8684 |
| Como conferir | "Use https://glockapps.com/domain-checker to see if you are missing any, if you are follow their guide to getting installed." | slide (deliverability) | L8691 |
| A fala não nomeia registro nenhum | "the best way to do this is going to Klaviyo domain setup and then going through how to set up a branded sending domain" | **outro-narrador** (deliverability) | L8410 |

**Como responder:** **não há desempate.** As duas listas estão no mesmo deck, a poucas
linhas de distância (L8671 e L8687-8689), e a diferença é o **MX**: a prosa de "What
Affects Deliverability?" cita quatro registros; a lista rotulada "Records you need on
your domain for inbox placement" cita três.

Responda assim: **SPF, DMARC e DKIM são o requisito declarado**; o MX aparece uma única
vez e só na prosa. **Não afirme que o MX é dispensável nem que é obrigatório** — o
corpus não decide, e nenhuma das duas leituras está escrita lá.

Dois avisos que evitam errar por outro caminho:

- **A fala não sustenta nenhum dos lados**, porque não nomeia registro algum: delega ao
  artigo de setup de domínio do Klaviyo (L8410-8412) e ao `glockapps.com/domain-checker`
  (L8414, L8691). A precedência slide-vence-em-especificação não tem contra quem operar
  aqui.
- **O corpus não ensina a instalar nada disso.** O slide diz que o Klaviyo faz por você
  (L8684) e manda checar no glockapps. Pedido de passo a passo de DNS é recusa — ver
  [[_protocolo]].

Ressalva de atribuição: a fala citada (L8410-8414) está no bloco "What is
Deliverability?" (L8365-8517), `outro-provavel` por [[mapa-da-autoria]]. Não altera o
conflito, que é slide contra slide dentro do mesmo deck.
