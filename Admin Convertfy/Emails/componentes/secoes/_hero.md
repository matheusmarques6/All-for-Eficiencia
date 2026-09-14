---
tipo: secao
secao: hero
variantes: 9
ativas: 9
com_julgamento: 9
status: aprovada
---

# Cobertura

9 variantes, todas ativas, todas com julgamento completo. É a seção mais
bem coberta da biblioteca — com uma ressalva: [[hero-8-lineup-com-lembrete-de-oferta]]
e [[hero-10-lineup-de-colecao]] têm todos os eixos e requisitos idênticos
no frontmatter (só `variant_id`, `schema_campos` e `peso.altura_px`
divergem). Nenhum eixo do
protocolo os separa; contam como 9 no inventário, mas como 8 perfis de
decisão distintos. Ver [[hero-8-duplicata-de-hero-10]].

# Chave de decisão

Ordem de leitura, na ordem real do protocolo: momento (filtro) → gates
(passo 4, resolvidos por código — ver os requisitos de cada variante) →
objeção (1º eixo de ranking) → registro (2º eixo). `paleta` não entra
como coluna: seus valores empatam exatamente onde os passos anteriores já
decidiram, então não teria poder de separação adicional. A foto que cada
uma pede não elimina — é diretiva de imagem, vira brief.

| Variante | Momento | Objeção | Registro |
|---|---|---|---|
| [[hero-3-cupom-de-captacao]] | welcome-1 | preço-valor | — |
| [[hero-4-editorial-de-pertencimento]] | welcome-1 | pertencimento | premium-editorial |
| [[hero-5-cupom-em-tres-lugares]] | welcome-1 | preço-valor | volume-impulso, popular-informal |
| [[hero-6-percentual-gigante]] | welcome-1 | preço-valor | — |
| [[hero-7-campanha-sem-cupom]] | campanha-promocional, sazonal | preço-valor | — |
| [[hero-2-pergunta-comparativa]] | consideração, reengajamento | qualidade-eficácia | — |
| [[hero-9-atendimento-proativo]] | browse-abandonment, reengajamento | suporte-dúvida | clínico-sóbrio |
| [[hero-10-lineup-de-colecao]] | welcome-meio, welcome-tardio, newsletter, sazonal, cross-sell, browse-abandonment | amplitude-de-catálogo | — |
| [[hero-8-lineup-com-lembrete-de-oferta]] | idêntico a hero-10 | idêntico a hero-10 | idêntico a hero-10 |

**Como ler:** os gates de cada variante moram no frontmatter dela e nas
notas de `requisitos/` — hero-3/4/5/6 dependem de cupom ativo; hero-7
depende de desconto automático sem código (as duas coisas não convivem
na mesma peça). Dentro do grupo `preço-valor` (hero-3, 5, 6, 7), quem
separa é a diretiva de imagem — os quatro pedem uma foto diferente — e o
momento, que isola hero-7 (campanha, sem welcome) dos outros três
(welcome-1).

# Onde a seção não cobre

- Nenhuma variante de hero para `carrinho-abandonado` ou
  `checkout-abandonado`: as nove vetam esses momentos explicitamente.
- Nenhuma para `pos-compra` ou `transacional`.
- Nenhuma de registro `comunidade-identitario`.
- Efetivamente 8 perfis de decisão, não 9 — hero-8 e hero-10 competem pela
  mesma vaga sem que nenhum eixo do protocolo escolha entre eles. A escolha
  em si é resolvida pelo "desempate final" de [[_protocolo-de-selecao]]
  (menos usada no histórico vence; fallback: menor número no slug).
