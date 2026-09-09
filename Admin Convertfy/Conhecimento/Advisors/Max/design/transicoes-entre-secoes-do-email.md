---
tipo: principio
modulo: design
assunto: transicoes
autor: max-sturtevant
registro: [transcricao]
fonte: "CONTEUDO BRUTO/max.md — L7532-7588 (transcrição); slide L8302-8307 (sem os métodos)"
conflitos: [design-blocky, design-metodos-de-transicao-ausentes]
status: aprovado
---

# O que é

O que acontece **entre** as seções — hero → bridge, bridge → product. Não é
decoração: é o mecanismo que impede a pessoa de parar de rolar.

> Transitions are what help make your different sections in your email flow.
> Having separate sections that are blocky and unrelated will lead to churn.
> By making it congruent, customers will keep scrolling without realizing.
> (L8304-8306, verbatim)

# A autocorreção em cena

Na fala ele começa errado e se corrige no ar:

> So we want to have separate sections that we don't want things to be too
> blocky because it'll be too easy for someone to scroll.
> Or excuse me.
> We if you have sections that are super blocky people might reach the end of a
> section and not want to move on to the next section. (L7538-7542, verbatim)

**Vale a correção.** O problema de seções muito "blocky" não é facilitar a
rolagem — é criar um ponto de parada em que a pessoa acha que o email acabou.
O slide confirma a segunda versão ("blocky and unrelated will lead to churn",
L8305). → `design-blocky`

O objetivo declarado: "So the customer keeps scrolling without realizing like
okay here's a hard stopping point" (L7548).

# Os quatro métodos

Só existem na fala. O slide anuncia "Here are a few methods to do this:"
(L8307) e **não lista nenhum** — a página seguinte já é outro assunto. →
`design-metodos-de-transicao-ausentes`

| # | Método | Como ele descreve | Linha |
|---|---|---|---|
| 1 | Gradiente | pegar a hero e degradê-la para dentro da próxima seção, "so it kind of flows together" | L7552-7558 |
| 2 | Formas ou quebras de linha | evitar a linha reta chapada; "some cool shape like this" para dar fluidez | L7560-7568 |
| 3 | Fundo consistente com elementos em primeiro plano | o email inteiro com o mesmo fundo — "That's not just like white" — e os elementos (galeria de fotos, texto) por cima, com efeito 3D | L7570-7578 |
| 4 | Transição atrás de foto | gradientes ou formas/quebras **por trás** das fotos | L7580-7586 |

# O favorito dele

> And my favorite is to add transitions behind photos.
> So you want to use gradients or use shapes and line breaks behind photos.
> Because a customer will like go through, look at the photo, and scroll through
> the photo without even realizing it. They're moving on to the next section
> because it just flows like butter. (L7580-7586, verbatim)

O método 4 é composição, não alternativa: usa os métodos 1 e 2 como material,
posicionados atrás de uma foto. A foto é o que segura o olho enquanto a
transição acontece.

O fecho é a única frase do módulo que junta as duas metades:

> So it's very, very important to make sure that you do transitions behind
> elements and make sure that your emails aren't too blocky. (L7588)

# Como isso conversa com skimmability

[[principio-skimmability]] pede "Smooth, Clear Sections" e 2-3 seções
identificáveis (L8196). Transição é o lado "smooth" dessa exigência; a separação
visível é o lado "clear". Suave demais vira "one big blob" (L7177); duro demais
vira blocky e churn. O corpus não dá régua para achar o meio.

# O que o corpus não diz

Altura da transição, quantos pixels de gradiente, se o método varia por tipo de
email, ou como fazer isso sobreviver ao fatiamento em imagens do upload — o
corte entre slices cai justamente entre seções. Ver [[upload-do-design]].
