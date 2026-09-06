---
tipo: procedimento
modulo: list-growth
assunto: hidden-fields-e-profile-property
autor: max-sturtevant
registro: [transcricao]
fonte: "CONTEUDO BRUTO/max.md — L1062-1065 (transcrição YouTube), contexto em L1012 e L976"
status: rascunho
---

> **Procedimento datado.** Passo a passo de uma tela do Klaviyo, demonstrada na
> aula 6 (L986-1083), que é a transcrição de um vídeo público. A interface pode
> ter mudado. Ver [[criar-form-no-klaviyo]] para o aviso completo de
> volatilidade.

# O que é

Como transformar a resposta do quiz em segmento. É o que dá ao quiz a vantagem
que os outros tipos de form não têm: "based on somebody's answers, we can tag
them with a profile property saying, 'Hey, this profile is interested in male
clothing, or this profile is interested in women'... And then we can customize
the emails that we send them based on their answers" (L1012). Ver
[[os-tipos-de-form]].

# Os passos

1. No botão de resposta do quiz, abrir **submit hidden fields** (L1062).
2. **Add a property** e criar a propriedade — no exemplo dele, `gender interest`
   — e clicar em **create** (L1062-1063).
3. Preencher o **value** correspondente àquele botão. No botão "men's", o valor é
   `men's` (L1063).
4. Repetir em **todos** os outros botões da mesma pergunta (L1064).
5. Depois, criar segmento no Klaviyo ou dar split no flow com base na resposta:
   "you can create a segment in Claio in split based on whatever the answer was"
   (L1065).

# A pegadinha

> "technically this property isn't created until somebody submits it. So all you
> want to do is you need to make sure that the wording that you put for the
> profile property is the same for all of them." (L1064)

A propriedade **não existe** no Klaviyo antes do primeiro submit. A regra que ele
tira disso é uma só, e é a que está na linha: o texto do nome da propriedade tem
que ser idêntico em todos os botões. Ele não descreve o que acontece se não for,
nem por que a tela não protege contra isso — o corpus só dá a regra e a garantia
de que "it's going to populate okay once people are submitting this" (L1065).

# Quando não é você quem faz isso

Se o form estiver no Alia em vez do Klaviyo, o tagueamento é automático: "whatever
somebody answers, it's going to tag that person's profile inside of Clavia"
(L976). Ver [[alia-e-a-alternativa]].

# O que o corpus não diz

- Não diz quantas propriedades por form são demais.
- Não dá convenção de nomenclatura (snake_case, Title Case, prefixo) — só a
  regra de que tem que ser idêntica entre botões (L1064).
- Não mostra a definição do segmento em si, só que ela é possível (L1065).
- Não diz o que acontece com quem opta pelo botão de recusa: se recebe
  propriedade vazia ou nenhuma.
