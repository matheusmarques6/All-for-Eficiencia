---
tipo: lacuna
sobre: biblioteca
descoberta_em: 2026-08-31
status: aberta
---

# O que falta

Das 8 estruturas de referência em `estruturas/welcome/` (uma por toque,
`emails: [1]` a `[8]`), só uma — [[medicube-comparacao-categoria]] (toque
5) — tem uma variante do catálogo que a serve por completo:
[[body-5-comparacao-nos-vs-eles]]. As outras 7 —
`avelmore-inspecao-antecipada` (1), `avelmore-deadline-objecao` (2),
`avelmore-mecanismo-e-origem` (3), `avelmore-prova-social-cirurgica` (4),
`medicube-escassez-com-prova-de-demanda` (6), `medicube-ultima-batida` (7)
e `carta-plain-text-extensao` (8) — não têm nenhuma variante que as sirva.

Quatro causas verificadas, na investigação da Task 13:

(a) o eixo `momento` só distingue `welcome-1` como toque isolado; os
toques 2 a 8 caem todos nos baldes genéricos `welcome-meio`/`welcome-tardio`,
sem separar qual toque específico da régua — enquanto as 8 estruturas são
amarradas cada uma a **um** toque exato;

(b) duas estruturas (toques 1 e 4) pedem seção `cta`, que tem zero
variantes — ver [[cta-sem-variante]];

(c) as estruturas codificam dispositivos idiossincráticos da loja de
referência (fita de papel rasgado, cupom com label partido, carta
plain-text) que o catálogo geral, desenhado para ser reutilizável entre
lojas, não reproduz;

(d) a granularidade de `objecao` também trava: cada estrutura ataca a
objeção **daquele toque específico** (tabela em `intencoes/welcome/_flow.md`
— toque 2 = "vale o que custa?", toque 5 = "por que comprar de vocês?"
etc.), enquanto as variantes carregam `objecao` genérico, sem se amarrar a
qual toque da régua ele responde.

# Por que importa

As causas (a) e (d) não são limitação do catálogo de 44 variantes — são
limitação do **vocabulário que este projeto desenhou** para descrever as
variantes. `momento` e `objecao`, como eixos, foram criados por nós neste
vault; não existiam antes. Ao desenhá-los na granularidade de "família de
momento" (welcome-meio, welcome-tardio) e "objeção geral" (preco-valor,
qualidade-eficacia), perdemos a capacidade de expressar "toque 3 do
welcome" ou "a objeção específica que o toque 3 responde" — mesmo quando a
informação existe, gravada nas próprias estruturas de referência
(`emails: [N]`, e a tabela de objeção por toque em `intencoes/welcome/_flow.md`).
Não é que a variante certa não exista; é que o vocabulário não tem onde
gravar o vínculo fino que provaria que ela serve.

# O que se perde hoje

Como (a) e (d) atuam juntas — uma variante precisaria acertar `momento` E
`objecao` no nível do toque específico — elas se compõem
multiplicativamente: mesmo nos casos em que existe uma variante com o
dispositivo certo, a chance de o vínculo `serve_estruturas` ser
estabelecido com segurança é baixa. O resultado prático é que 7 das 8
estruturas do welcome — a régua mais estruturada e mais bem documentada do
vault — não têm nenhum registro formal de qual variante as monta, mesmo
quando uma correspondência real pode existir. Isso não é uma falha de
busca (a Task 13 verificou seção a seção, estrutura a estrutura); é o teto
que o vocabulário atual impõe.

# Fora do escopo desta entrega

Redesenhar os eixos `momento` e `objecao` para carregar granularidade de
toque — mudaria o schema de 44 variantes já aprovadas e o frontmatter de
todas as notas de eixo. Assumimos a autoria deste teto aqui; corrigi-lo é
trabalho de desenho de vocabulário, não desta entrega.
