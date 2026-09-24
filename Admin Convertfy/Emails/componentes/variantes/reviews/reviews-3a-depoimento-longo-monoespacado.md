---
tipo: componente
slug: reviews-3a-depoimento-longo-monoespacado
secao: reviews
nome_no_banco: "review 2"
variant_id: 7dafa6ca-65de-4907-b52c-dad83ecd63a4
ativa: false
dispositivo: prova_por_relato
legado: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [checkout-abandonado, carrinho-abandonado]
momento_vetado: []

# --- eixos de ranking, na ordem do protocolo ---
objecao: [qualidade-eficacia]
registro: []
registro_vetado: [premium-editorial]
paleta: [preto-e-branco]
papel_na_peca: [meio]

# --- requisitos duros (eliminam) ---
exige: []
diretivas_de_imagem: []
requisitos_de_reviews: [foto-de-uso-real, reviews-longos]

# --- capacidade e composição ---
product_slots: 0
itens: { min: 2, max: 2 }
peso: { altura_px: 1682, classe: pesado, fonte: medido }
convivencia: [prova-social-nao-duplica-na-peca, exige-hero-ou-contexto-acima, monoespacado-nao-convive-com-serif-display]

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: minimal
schema_campos: 12
status: legado
---

> **Correção (04/09/2026).** O `nome_no_banco` desta nota dizia `review 3`.
> O `variant_id` `7dafa6ca` é, no cadastro, a **`review 2`** — quem se chama
> `review 3` é a peça de `reviews-3b-depoimento-longo-monoespacado`. As duas
> descrevem o mesmo bloco e são a duplicata registrada em
> `[[reviews-3-duplicado]]`: enquanto o cadastro não resolver, o Curador vê
> duas fichas equivalentes e pode escolher qualquer uma.

## Descrição curta

Bloco de prova social para inserir depois do argumento principal, quando a objeção que falta vencer é confiança no produto e não preço. Usa dois depoimentos longos de clientes reais com foto do item comprado para fechar a decisão antes do CTA final.

## Descrição detalhada

Título centralizado em duas linhas seguido de duas linhas de review em disposição espelhada: na primeira, foto à esquerda sangrando na borda e texto à direita; na segunda, texto à esquerda e foto à direita sangrando. Cada review é uma pilha fixa — aspas decorativas alinhadas à direita da coluna de texto, título do depoimento em bold, corpo do depoimento, régua de 5 estrelas, nome e selo de credencial. Fecha com um CTA sólido centralizado.  

Tipografia monoespaçada em todos os blocos, sem nenhuma segunda família. O depoimento fica com aparência de texto digitado pelo próprio cliente, não de copy da marca.  
Sangria alternada das fotos. As duas fotos encostam nas bordas opostas do container e o texto respira para dentro. O zigue-zague dá ritmo sem precisar de card, borda ou fundo colorido.  
Alinhamento superior das colunas. A altura de cada linha é ditada pelo depoimento mais longo, e a foto acompanha. Depoimentos de tamanhos diferentes não quebram o layout.

## Quando usar

Recuperação de checkout ou carrinho, como segundo ou terceiro bloco, depois de recuperar o item.  
Loja com reviews escritos longos e específicos (menciona sensação, uso, encaixe), não "produto muito bom, recomendo".  
Categorias em que o cliente decide por confiança em ajuste ou qualidade: vestuário, performance, suplemento, skincare.  
Marca sem paleta ou com identidade preto e branco — a seção depende de contraste, não de cor.

## Quando NÃO usar

Sem foto do produto real usado ou vestido. Foto de estúdio genérica derruba o efeito de depoimento.  
Reviews curtos (menos de ~80 caracteres). A coluna fica vazia ao lado de uma foto alta e o bloco desmonta.  
Como primeira seção do e-mail. A seção não tem oferta, cupom nem contexto de campanha — só reforça.  
E-mail que já tem outra seção de prova social. Duplicar prova social na mesma peça cansa.  
Marca com tipografia serifada ou display de identidade forte — o monoespaçado é dominante demais para conviver.

## Orientações de copy para a IA

Depoimento é citação, não copy. Preservar as palavras do cliente, inclusive repetição e falta de vírgula. Não corrigir gramática nem encurtar para "ficar limpo".  
Título do depoimento é o benefício em duas ou três palavras, extraído do próprio texto do review — nunca um slogan da marca.  
Título da seção fala do cliente, não do produto: quantos já compram, quem já usa, quem já aprovou.  
Os dois reviews devem cobrir atributos diferentes (um sobre a peça, outro sobre outro item ou outro aspecto). Dois reviews sobre a mesma coisa desperdiçam o bloco.  
Selo de credencial é obrigatório e sempre o mesmo texto nos dois ("Verified Buyer", "Compra verificada"). É o que sustenta a alegação.  
CTA retoma a ação pendente, não repete "comprar agora" genérico.  
Se o review original mencionar cupom ou código de afiliado, manter — reforça que é texto de gente real.

## Design system

Container: 600px travado, fundo branco, sem borda.  

Tipografia principal: Space Mono (fallback 'Courier New', Courier, monospace) em todos os blocos de texto. Não há tipografia secundária — as estrelas usam Arial só porque o glifo ★ do monoespaçado não é confiável.  

| Bloco | Tamanho / entrelinha | Peso | Tracking | Caixa |  
|---|---|---|---|---|  
| Título da seção | 30 / 39 | 700 | 0.06em | ALTA |  
| Aspas decorativas | 120 / 58 | 700 | 0.04em | glifo &rdquo; |  
| Título do depoimento | 22 / 29 | 700 | 0.04em | Sentença |  
| Corpo do depoimento | 20 / 26 | 400 | 0.04em | Sentença |  
| Estrelas (Arial) | 32 / 32 | — | — | ★ ×5 (154px) |  
| Nome | 18 / 24 | 700 | 0.04em | Sentença |  
| Selo de credencial | 16 / 21 | 400 | 0.04em | Sentença |  
| Label do CTA | 22 | 700 | 0.10em | ALTA |  

Cores. Cor primária   
#000000 (todo o texto e o fundo do CTA). Cor secundária   
#FFFFFF (fundo da peça e label do CTA). Cor de acento   
#FA6B05 — usada exclusivamente em aspas e estrelas, os dois únicos elementos coloridos da seção.  

Grade e ritmo vertical (medido no PNG de referência):  

título da seção          padding lateral 79px, centralizado  
   ↓ 47px  
REVIEW 1   linha de 598px — coluna foto 275px | coluna texto 323px  
           aspas (alinhadas à direita do bloco de texto)  
              ↓ 6px   título do depoimento  
              ↓ 8px   corpo  
              ↓ 20px  estrelas  
              ↓ 11px  nome  
              ↓ 1px   selo  
   ↓ 66px  
REVIEW 2   espelhado — coluna texto 360px | coluna foto 238px  
   ↓ 39px  
CTA        325 × 60, fundo #000000, centralizado  
   ↓ 100px  

Regras que não podem ser quebradas:  

Zero border-radius, zero sombra, zero gradiente, zero borda em qualquer elemento.  
As fotos encostam na borda do container (x=0 e x=599). Adicionar respiro lateral mata a sangria.  
As aspas são alinhadas à direita do bloco de texto nos dois reviews, inclusive no espelhado.  
Acento só em aspas e estrelas. Título, corpo, nome, selo e CTA são pretos.  
Colunas com valign="top", nunca middle.  
display:block em toda <img> e célula da foto com font-size:0;line-height:0 — sem isso o Outlook abre um gap na sangria.  
Nenhuma segunda família tipográfica além do fallback do monoespaçado.

## Direção fotográfica

Produto recortado em fundo branco puro (cor de fundo do e-mail), sem sombra projetada, sem superfície, sem cenário. O fundo do ativo é o fundo do e-mail — a ausência de emenda é o efeito.  

Peça vestível: fotografada plana ou em suporte invisível, levemente girada, com a estampa ou detalhe que o review menciona totalmente visível.  
Par de itens: os dois em diagonal, sobrepostos parcialmente, um claro e um escuro para gerar contraste no branco.  
Escala: o produto ocupa 85–95% da altura do slot. Sobra de branco só no eixo em que o recorte sangra para fora do container.  
Luz: difusa e frontal, alto-chave, sem vinheta e sem realce especular forte. O branco do produto tem que se separar do branco do fundo apenas por sombra própria suave.  
Proibições: modelo com rosto, fundo colorido, sombra dura no chão, prop de cena, moldura, reflexo de estúdio, recorte com halo cinza na borda.

---

HTML: [[_html/reviews-3a-depoimento-longo-monoespacado.html]] · Seção: [[_reviews]] · Protocolo: [[_protocolo-de-selecao]]

# Auditoria de legado

- **Verificado em:** 2026-09-24.
- **Dispositivo histórico:** `dispositivo: prova_por_relato`.
- **Situação no banco:** O `variant_id` antigo não existe mais no banco. A estrutura é igual à de [[reviews-3b-depoimento-longo-monoespacado]] e usa dois relatos longos com fotografia do item.
- **Decisão:** Manter como registro aposentado e duplicado. Não há substituição direta no banco atual.
- **Elegibilidade:** continua `legado: true`, `ativa: false` e `status: legado`.
