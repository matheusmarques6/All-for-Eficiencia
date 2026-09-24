---
dispositivo: carrinho_dinamico
secoes: [offer]
status: aprovada
---

# O que é

Devolve ao leitor o item ou conjunto que ele deixou para trás. Move a decisão reabrindo uma intenção concreta, com dados do carrinho em vez de uma oferta genérica.

# Quando usar

Use em recuperação de carrinho ou checkout, depois que existe estado transacional recuperável.

# Quando não usar

Não use em campanhas ou quando não existe carrinho; use `codigo_relembrado` se o papel for apenas lembrar o incentivo.

# O que ele exige

- [[bloco-dinamico-de-carrinho]]
- [[cupom-ativo]]

# Variantes que realizam

- [[offer-6-carrinho-preto-e-branco]] — peça inteira com bloco dinâmico e cupom.
