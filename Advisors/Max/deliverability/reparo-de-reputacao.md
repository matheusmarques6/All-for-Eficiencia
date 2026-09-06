---
tipo: procedimento
modulo: deliverability
assunto: reparo-de-reputacao
autor: max-sturtevant
registro: [outro-narrador]
fonte: "CONTEUDO BRUTO/max.md — L8589-8597 (transcrição). Sem contraparte de slide."
validade: "procedimento — o corpus não data a gravação. Extraído em 2026-09-06."
status: rascunho
---


# Aviso de autoria

**Faixa L8381-8646 (toda a fala do módulo de deliverability) — `outro-provavel`.**
Sem prova nominal. A classificação é **estilométrica**: o bloco pertence ao aglomerado
do único bloco `outro-provado` e não traz um só marcador do idioleto de Max.
`outro-provavel` não é `outro-provado` — não está provado que a voz não é dele, está
estabelecido que é muito improvável ([[_autoria]] §7.3).

Critério: **idioleto** ([[_autoria]] §2.1) — ausência de "I recommend", "my favorite"
e "I like to", presença de "at the end of the day" e "obviously", e o fecho coletivo
"thank you guys… see you in the next one". **A saudação de abertura não é critério e
não pode ser citada como evidência:** o laudo testou e ela caiu — o walkthrough de
Figma abre com "Hello, hello" e é comprovadamente Max, que em L7817 digita `@max` e
diz "tags me" ([[_autoria]] §5).

Nesta nota **não sobra nada de Max**: L8589-8597 é fala, dentro da faixa não-Max, e
não há contraparte de slide. Todo o procedimento de reparo — segmento curto, 2-3
semanas, alvo de 60-80%, prioridade a text-based — é **material do curso**, e
nenhuma frase daqui é citável como fala dele. O conhecimento continua valendo;
muda quem pode ser citado como autor.

> **Registro único.** Este trecho existe só na fala. O deck de warming não foi
> exportado (ver [[warming-do-dominio]]) e o deck de deliverability não trata de
> reparo. Nenhum número aqui tem segunda confirmação.

# Quando se aplica

Conta que já está caindo em spam, não conta nova. O quadro descrito na aula
(L8589):

> let's say you're consistently seeing yourself landing in spam, and you're
> sending to, you know, 90, 120 day engage list

Ou seja: a lista larga é o suspeito. O warming trata de construir reputação do
zero; isto trata de puxar reputação já danificada de volta. Ver o bullet do deck
que autoriza o uso do mesmo método com ajustes (L8524).

# O procedimento

**1. Achar o segmento mais engajado que existe** (L8590): "this is the
opportunity where you want to find your most engaged segment, and send to them."

**2. Enviar só para ele, por 2 a 3 semanas** (L8591): "You have to determine
what the right window is, but I'd say anywhere between 2 to 3 weeks to start."

Note que a janela é declarada como decisão local — "you have to determine what
the right window is" — e o "2 to 3 weeks" vem como sugestão de partida, não como
regra.

**3. Segmentos a usar**, verbatim (L8591):

> your 7 day engage, 14 day engage, 30 day engage, and then maybe you want to
> add additional parameters, and people that have opened 2 times, 3 times in the
> last 14 days

São janelas mais curtas que as do envio normal, mais uma condição extra de
frequência de abertura sobreposta. A estrutura do segmento base fica igual — só
muda o número de dias e entra o parâmetro adicional. Ver
[[so-envie-para-engajados]].

**4. O alvo** (L8592): "once you hit those 60% open rates, 60, 70, 80, that's
going to start to pull you and start repairing."

**60-80% de abertura** é o número que começa a puxar a conta de volta —
deliberadamente acima do alvo de operação normal (`Greater than 50%`, L8715 —
este, sim, slide de Max). O racional apresentado (L8593):

> you want to aggressively put that in the other direction where your engagement
> is so high that it's going to actually start to repair and send more favorable
> numbers over to the inbox provider.

# Priorizar email text-based durante o reparo

Regra separada, e vale tanto no warming quanto no reparo (L8594):

> Text-based emails, another quick tip is to text-based emails deliver much,
> much better. So prioritizing HTML, prioritizing like text-based email,
> especially either when you're warming or just when you're starting to see some
> deliverability issues is super, super helpful.

O motivo é o mesmo do alt text (ver [[upload-para-deliverability]]): o provedor
lê texto, não lê imagem (L8595-8597):

> Google is going to look more favorably on text-based because it can actually
> read all of that. When you're sending constant image-based emails, and not
> that that's a bad thing, that's something that we do very consistently, but
> Google doesn't see it as much of that. They just see an image file, opposed to
> actually seeing the text that we're sending out.

A ressalva é do material, e é importante: **email image-based não é erro** —
"that's something that we do very consistently" (L8596). A troca para text-based é
situacional, ligada a warming e a problema de deliverability, não é doutrina
permanente. No caso real de pré-lançamento sem dado nenhum, os emails de warming
foram "all text-based" (L8625).

# O caso vizinho: promotions, não spam

Se o problema é cair em **promotions** e não em spam, o material aponta outra
saída —
uma ferramenta de terceiros que reescreve o HTML no backend. **O nome dela não
está no corpus** (L8641-8643); a transcrição pula ~41 segundos exatamente onde a
apresentação estaria. Detalhes em [[warming-do-dominio]].

Escopo declarado na aula: essa ferramenta "will not help you in the warming,
will not help you if your primary issue is you're landing in spam, those you
have to take the different approaches that we talked about earlier" (L8643) — as
"different approaches" são justamente o procedimento desta nota.

# O que o corpus não diz

- Frequência de envio durante o reparo. O 3-4x/semana é declarado para warming
  (L8557); não é repetido aqui.
- Volume por envio durante o reparo. A rampa de warming não é reaplicada
  explicitamente.
- O que fazer se o segmento de 7 dias já estiver abaixo de 60%.
- Quando parar de reparar e voltar à operação normal — só "start to pull you"
  (L8592), sem critério de saída.
- Se durante o reparo os flows continuam rodando ou são pausados.
- A transcrição salta de 13:04 (L8593) para 13:33 (L8594). ~29 segundos do
  raciocínio de reparo estão ausentes.
