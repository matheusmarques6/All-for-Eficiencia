---
tipo: especificacao
modulo: sms
assunto: custo-e-tamanho-da-mensagem
autor: max-sturtevant
registro: [transcricao, slide]
fonte: "CONTEUDO BRUTO/max.md — L9228-9233 (transcrição), L9379-9407 (slide)"
conflitos: [sms-mms-no-browse-abandon]
status: rascunho
---

# A especificação

| Item | Regra | Registro |
|---|---|---|
| Limite por mensagem | 160 caracteres (L9231, L9390) | fala + slide |
| Passar de 160 | 161 caracteres = 2 SMS = preço dobrado (L9231, L9392) | fala + slide |
| Acima disso | segue dobrando "for like 3 SMS to 4 SMS all split up by 160 characters" (L9231) | fala |
| MMS | 2-3x mais caro que SMS (L9229, L9383) | fala + slide |
| Emoji | equivale a 35-50 caracteres (L9233, L9405) | fala + slide |
| Recomendação de emoji | não usar (L9233, L9406) | fala + slide |

# O critério econômico, que é um só

Toda restrição aqui é derivada da mesma conta: o incremento tem de pagar o
próprio multiplicador de custo.

**MMS.** "if MMS messages are two to three times more expensive than SMS that
means that if you including an image or a gift or whatever in an MMS needs to
generate two to three times more revenue for it to be worth it in an Roi
perspective" — e então: "in my experience that is very very rare to have one
image generate so much more Revenue" (L9229-9230). O slide fecha igual:
"In my experience that's very rare. / I would highly recommend just **sticking
to SMS text only messages**" (L9385-9386).

**Comprimento.** Mesma conta aplicada ao texto: "it is very very rare for kind
of this extra messaging to generate you 2x more Revenue" (L9231); slide: "it's
very unlikely the increased text will result in 2x more revenue and ROI for
you" (L9394). Daí a regra de escrita: "our SMS messaging needs to be very
short clear and concise" (L9232), "waste no space" (L9232, L9395).

**Contexto de custo.** Ele ancora tudo comparando com email, "where it
literally costs like a fraction of a scent" (L9229, ASR de *cent*). É o motivo
declarado de o SMS ser gerido por custo e o email não.

# Emoji: a admissão

Ele não sustenta o mecanismo, só o efeito: "emojis use a different kind of code
which I don't really understand the science of it but what I do know is that
emojis take up the equivalent of 35 to 50 characters" (L9233). O slide não
admite a lacuna — afirma direto "They use a different kind of code and can have
the **equivalent of 35-50 characters in your message**" (L9405) e conclui "They
will just drive your price up and decrease your sms ROI" (L9407).

# A consequência de doutrina

"with all the character limits and limitations that we have in our SMS
marketing our messages need to be pretty Bare Bones and simple" (L9233-9234);
slide: "your sms messaging has to be pretty bare bones and simple" (L9411). Isso
não é concessão de qualidade: "That doesn't mean it can't be effective"
(L9412). Ver os templates em [[flows-sms]]: as cinco mensagens dos quatro
templates têm entre 72 e 132 caracteres como estão escritas — mas isso é
contagem nossa, com os placeholders ainda vazios. O corpus não faz essa conta
nem diz se os templates cabem em um SMS depois de preenchidos.

# Onde o corpus discorda

A proibição de MMS é absoluta na fala e no slide ("unless it's absolutely
necessary to include an image", L9230), mas o próprio slide sugere testar
imagem no browse abandon: "you can A/B test including a picture of the item the
person browsed" (L9449). Ver `sms-mms-no-browse-abandon`.

# O que o corpus não diz

- Nenhum preço absoluto: nem por SMS, nem por MMS, nem por plataforma. Só
  múltiplos ("2-3x", "double").
- Não diz quantos caracteres um emoji consome *especificamente* — a faixa de
  35-50 aparece sem discriminar tipo de emoji.
- Não trata de link encurtado, opt-out obrigatório no rodapé nem prefixo de
  marca, que consomem caracteres do mesmo limite de 160.
- Os slides "**1 SMS Long**" e "**3 SMS Long (triple the cost)**" (L9397-9399)
  são títulos de imagens que não sobreviveram à extração: os exemplos visuais
  não existem no arquivo.
