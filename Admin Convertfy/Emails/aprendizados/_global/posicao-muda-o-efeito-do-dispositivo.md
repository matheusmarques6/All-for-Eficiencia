---
tipo: aprendizado
escopo: cross-flow
aplica_a: [welcome, abandoned_cart, browse_abandonment, post_purchase]
origem_estrutura: medicube-comparacao-categoria
autor: coo
status: pendente
status_evidencia: convergente
---

# Observação

O bloco de comparação categoria-vs-loja funciona no 5º toque de
[[medicube-comparacao-categoria]] e não funcionaria no 1º.

No primeiro toque, comparar é defensivo: a pessoa ainda nem desconfiou e a marca
já está se justificando. No quinto, a dúvida já existe, madura — nomeá-la é
alívio, não alerta.

O mesmo padrão já havia sido observado em outro flow: abrir carrinho abandonado
com FAQ ficou defensivo demais, e a solução foi guardar o FAQ para o 3º toque.

Dois dispositivos diferentes, dois flows diferentes, mesmo mecanismo de falha.

# Regra derivada

Bloco defensivo cedo demais planta a dúvida que pretendia curar. A posição na
sequência muda o efeito do dispositivo — o mesmo bloco é alívio ou alerta
dependendo de a dúvida já existir na cabeça do leitor.

Antes de posicionar um dispositivo que responde a uma objeção, perguntar: **neste
toque, o leitor já tem essa dúvida?** Se não tem, o bloco a cria.

# Onde já se manifestou

- `welcome` #5 — comparação categoria-vs-loja (funciona no 5º, falharia no 1º)
- `abandoned_cart` — FAQ defensivo no 1º toque, movido para o 3º
