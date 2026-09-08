---
tipo: peca
modulo: padrao-convertfy
assunto: popup-captura
autor: convertfy
status: aprovado
---

# O que é

Popup de captura em duas etapas — e-mail primeiro, telefone depois —
para loja que quer construir lista sem derrubar a taxa de entrada. É a
peça de referência: o HTML abaixo é o padrão, e cada decisão está
explicada ao lado. Use como base e troque a oferta, a paleta e a
tipografia; a estrutura fica.

# A peça

```html
<div style="max-width:440px;background:#ffffff;border-radius:4px;
            padding:40px 36px;font-family:Inter,Helvetica,Arial,sans-serif;
            position:relative;box-shadow:0 8px 40px rgba(0,0,0,.14)">

  <button aria-label="Fechar"
          style="position:absolute;top:14px;right:14px;width:28px;height:28px;
                 border:0;background:transparent;font-size:18px;line-height:1;
                 color:#8a8a8a;cursor:pointer">×</button>

  <p style="margin:0 0 10px;font-size:12px;letter-spacing:.08em;
            text-transform:uppercase;color:#8a8a8a">Primeira compra</p>

  <h2 style="margin:0 0 12px;font-size:30px;line-height:1.15;
             font-weight:600;color:#1f1f1f;letter-spacing:-.02em">
    10% de desconto no seu primeiro pedido
  </h2>

  <p style="margin:0 0 24px;font-size:15px;line-height:1.5;color:#5c5c5c">
    O cupom chega no seu e-mail em um minuto.
  </p>

  <input type="email" placeholder="seu@email.com"
         style="width:100%;box-sizing:border-box;height:48px;padding:0 14px;
                border:1px solid #d4d4d4;border-radius:4px;font-size:16px;
                color:#1f1f1f;margin-bottom:10px">

  <button style="width:100%;height:48px;border:0;border-radius:4px;
                 background:#1f1f1f;color:#ffffff;font-size:15px;
                 font-weight:600;cursor:pointer">
    Quero meu cupom
  </button>

  <p style="margin:14px 0 0;font-size:11.5px;line-height:1.45;color:#9a9a9a">
    Ao continuar você aceita receber nossos e-mails. Dá para sair quando
    quiser, em um clique.
  </p>
</div>
```

# As decisões, uma a uma

**Largura 440px, padding 40/36.** Abaixo de 400 o campo de e-mail fica
apertado e a headline quebra em três linhas; acima de 480 o popup começa
a parecer página. O padding generoso é metade da percepção de peça
profissional — popup amador é reconhecível pela borda colada no texto.

**A headline é a OFERTA, não o convite.** "10% de desconto no seu
primeiro pedido" contra "Assine nossa newsletter": a segunda pede um
favor, a primeira entrega um. Ninguém assina newsletter; todo mundo
aceita desconto.

**Eyebrow curto acima da headline.** Duas ou três palavras em caixa alta,
12px, cinza. Dá contexto sem competir e cria o degrau de hierarquia que
separa peça desenhada de texto empilhado.

**Um campo só na etapa 1.** Cada campo a mais derruba a conversão. Nome
não é necessário para mandar um cupom — e se for necessário depois, a
plataforma pergunta na etapa 2 ou no checkout.

**O botão tem verbo de ganho.** "Quero meu cupom" descreve o que a pessoa
recebe. "Enviar" e "Cadastrar" descrevem o trabalho que ela faz. A
diferença é de conversão, não de estilo.

**Campo e botão com 48px de altura.** É o alvo de toque confortável no
celular, onde a maioria dos popups é vista. Abaixo de 44px erra o dedo.

**Fonte do input em 16px, obrigatório.** Abaixo disso o Safari do iPhone
dá zoom automático ao focar o campo e desloca a página inteira. É o
defeito mais comum em popup de loja e não tem nada a ver com design.

**O X é visível e tem 28px.** Esconder o fechamento sobe a captura na
semana e derruba a marca no mês. Além disso o Google penaliza intersticial
que atrapalha, e um X escondido é exatamente isso.

**Contraste real no CTA.** Preto sobre branco, ou a cor de marca em cima
de fundo neutro. Botão claro sobre fundo claro é onde a peça perde a
hierarquia que o resto tentou construir.

**A linha legal fica.** 11,5px, cinza, e diz como sair. Custa quase nada
em conversão e é o que separa lista construída de lista comprada.

# A segunda etapa

Ela abre DEPOIS do e-mail já capturado — a etapa 1 grava. Assim, quem
desiste do telefone continua sendo lead de e-mail. Mesma estrutura, com
três mudanças: a headline vira confirmação ("Cupom a caminho" ou o
próprio código), o campo é telefone, e o botão de recusa aparece como
texto discreto abaixo ("Prefiro só por e-mail"), nunca como segundo botão
de igual peso.

# Quando não usar

- **Entrada imediata na primeira visita.** Popup antes de a pessoa ver o
  produto captura e-mail descartável. Gatilho por intenção de saída, por
  scroll ou por tempo.
- **Loja sem cupom.** Sem oferta concreta, a captura de duas etapas não
  se sustenta e vira newsletter — aí a peça é outra, com a promessa de
  conteúdo no lugar do desconto.
- **Mobile em tela pequena.** Abaixo de 380px de largura, o mesmo desenho
  precisa virar bottom sheet, não card centralizado.

Doutrina relacionada: [[por-que-o-popup-decide]].
