---
tipo: doutrina
secao: [hero, cta, offer]
fonte: "Conhecimento/Advisors/Max/design/principio-ease-of-click.md — §O que é (bruto L8147-8149, L7123-7127), §Os quatro itens (L8151-8171, L7041-7047, L7067-7081), §O resumo dele (L7139), §O contra-exemplo nominal (L7149-7153), §O que o corpus não diz (L8141, L8166); Conhecimento/Advisors/Max/numeros-de-design.md — §Os três 75% (L7027) e §Botão, CTA e estrutura (L8136-8137, L8160, L7033, L7051-7059)"
registro: [transcricao, slide]
status: aprovada
---

Ponte para o princípio "ease of click" do Max — botão acima da dobra, grande, contrastante e centralizado — traduzida para onde o botão mora neste vault (dentro de `hero` e `offer`, porque `cta` não tem variante) e para o que já existe aqui como requisito e aprendizado.

# A regra do Max

O modelo de leitor: "When customers are opening emails they are in zombie mode. Any friction in the ability for someone to click will automatically lead to churn. We need to hand the click to them on a silver platter" (slide L8147-8149; fala L7123-7127). Quatro itens:

1. **Button Above the Fold** (L8151-8156) — nem todo cliente rola; "Including a top button is an easy low-hanging fruit to automatically improve your click rates" (L8156).
2. **Large Buttons** — "at least 1.5–2 inches wide" (slide L8136; fala L7033) numa tela em que "An iPhone screen is 2.75 inches" (L8160). A prova: "I've never had a bigger button lose an A-B test in click rates" (L7041-7043).
3. **Clear Calls to Action** (L8163-8166) — "Your buttons should be the easiest to view part of your email"; "high-contrast colors and simple backgrounds" (L8141). O contra-exemplo de cor é qualitativo: "You don't want to use like a blue button here" (L7045-7047).
4. **Centered Main Buttons** — "Most people hold their phone in their right hand. If you put a button on the left side, the user has to stretch their thumb over to click" (L8170-8171). As exceções são da fala: imagem com o sujeito à direita e seções de produto em zigue-zague (L7071-7081).

Resumo dele: "Large, clear buttons above the fold that are ideally centered" (L7139). Contra-exemplo nominal: Nike — descentralizado, pequeno e abaixo da dobra (L7149-7153).

**Ressalvas de número.** "Button above the fold for 75% of your email" (L7027) é um dos três "75%" do módulo e não é o "75% dos esforços" da hero; o bruto escreve "your email" no singular e não desambigua entre "75% dos e-mails" e "75% da área". "Repeat your CTA 2–3 times throughout the email" existe só no slide (L8137); a fala não dá número e dá o limite — "a shit ton of buttons" é o erro (L7051-7059) → `design-repeticao-de-cta`. O corpus não dá hex, contraste medido, raio nem altura de botão.

# Como isso se lê neste vault

- **Onde o botão mora.** Não há seção `cta` com variante ([[_cta]], [[cta-sem-variante]]); o botão é slot das variantes de `hero` (`CTA_LABEL/CTA_URL`), de `offer` e, por item, de `products`. "Above the fold" é, portanto, o botão da variante com `papel_na_peca: [abre]` — a hero. O teste do eixo [[abre]] já pede que o topo entregue decisão sozinho; o botão é a decisão.
- **Tamanho.** A régua do Max é polegada de tela; as variantes daqui medem em pixels de container de 600px. Convertida por proporção (conta desta ponte, não do Max), 1.5–2 de 2.75 polegadas dá entre 55% e 73% da largura — 327 a 436px: [[hero-3-cupom-de-captacao]] (389px) e [[hero-9-atendimento-proativo]] (330px) passam; [[hero-2-pergunta-comparativa]] (306px, 51%) fica abaixo por pouco.
- **Contraste.** O ativo que responde "a marca tem cor de contraste?" é o requisito [[cor-de-acento-definida]] (hero-2 e hero-4 exigem). Variante monocromática ([[hero-9-atendimento-proativo]]) resolve por valor, preto sobre cinza — e proíbe "qualquer cor saturada, inclusive no CTA primário". O "blue button" do Max não tem tradução em eixo.
- **Centralizado.** Nenhuma variante declara alinhamento do botão em campo; está no HTML de `_html/`. A exceção do Max (zigue-zague de produto) tem correspondente: [[reviews-7-zigue-zague-com-cupom]].
- **Repetir 2–3 vezes.** Colide com [[um-cta-dominante-em-email-curto]]: "um CTA dominante; os demais são secundários por hierarquia visual". Pela precedência, o aprendizado com origem vence a doutrina de curso; e o próprio Max limita a repetição pelo contra-exemplo. A leitura compatível é a de hero-9: dois botões, um domina.

# Onde entra na decisão

Passo 3 do [[_protocolo-de-selecao]] (`schema_campos > 0`: sem slot, não há botão para escrever). Passo 4 (`exige: cor-de-acento-definida`). Passo 7, eixo `papel_na_peca`: [[abre]] carrega o botão do topo, [[fecha]] carrega o CTA dominante. Passo 8 é onde "2–3 repetições" se confere contra o aprendizado. Fase 2 (copy do botão): o Max não fala do label — "clear" nele é visibilidade (contraste, fundo simples, L8163-8166), não copy.
