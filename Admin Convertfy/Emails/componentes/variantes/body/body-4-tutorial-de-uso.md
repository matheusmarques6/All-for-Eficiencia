---
tipo: componente
slug: body-4-tutorial-de-uso
secao: body
nome_no_banco: "body 4 - bridge fundo cards"
variant_id: 63736c6c-7d1b-4c7c-83ea-bae15599f1d7
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: [pos-compra, reengajamento]
momento_vetado: [campanha-promocional]

# --- eixos de ranking, na ordem do protocolo ---
objecao: [uso-aprendizado]
registro: []
registro_vetado: []
paleta: []
papel_na_peca: []

# --- requisitos duros (eliminam) ---
exige: []  # "Quando NÃO usar" veta tipo de campanha, tipo de produto e limite de passos por coluna -- nenhuma frase cita ativo ausente ("sem X")

# --- capacidade e composição ---
product_slots: 0
itens: { min: null, max: 6 }
peso: null
convivencia: []

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: null
schema_campos: 9
status: aprovada
---

## Descrição curta

Tutorial de uso em 2 colunas paralelas: foto circular do produto, título do modo e passos numerados em badges, com Pro Tip compartilhado e CTA de aprofundamento.

## Descrição detalhada

2 cards = table 2 col com TDs bege + border-radius (degrada quadrado). Foto circular cavalgando o topo = overlap inexistente em e-mail — degradar para foto circular DENTRO do card (primeira linha, centralizada); círculo via PNG já recortado circular (border-radius 50% em <img> falha no Outlook — o PNG pronto resolve em todo client). Badges numeradas = TD mínima com background branco + radius contendo o número (degrada quadradinho, ok) ou fallback "1." em texto. Passos 100% vivos. Colunas assimétricas (5 vs 6 passos) são naturais — vertical-align top e cada card com sua altura; o stagger decorativo da referência se perde, sem prejuízo. Fundo texturizado → cor sólida. Pro Tip = bloco de texto vivo com label bold. Mobile: colunas empilham (card 1 sobre card 2) — a comparação lado a lado vira sequência, aceitável.

## Quando usar

E-mails pós-compra (o uso certo do produto recém-chegado — reduz devolução e review ruim), welcome de produtos com curva de aprendizado, e reengajamento educativo. O formato de 2 colunas pede 2 produtos/modos complementares (shampoo+condicionador, dia+noite, preparo+finalização); para produto único, existe variante de coluna só. Nichos: beauty, skincare, food com preparo, qualquer produto em que "usar errado" gera frustração.

## Quando NÃO usar

Campanhas de venda (zero slot de oferta). Produtos autoexplicativos (tutorial de camiseta é ruído). Rotinas com mais de ~6 passos por coluna (vira manual — quebrar em 2 e-mails).

## Orientações de copy para a IA

Headline em mantra de 2–4 palavras staccato com pontos ("LATHER. RINSE. REPEAT." / "MOLHA. PASSA. PRONTO.") — o ritmo é a assinatura. Título de coluna = verbo/modo em 1 palavra caps. Passos: imperativos curtíssimos de 3–10 palavras, 1 ação por passo, com detalhe sensorial ou de tempo entre parênteses quando agregar ("3–5 minutos", "você vai sentir o 'slip'") — os parênteses humanizam. Pro Tip: 1 dica de conservação/armazenamento que estende a vida do produto (~110 caracteres). CTA de aprofundamento ("LEARN MORE" / "VER TUTORIAL COMPLETO"), nunca de compra.

## Design system

_(vazio)_

## Direção fotográfica

_(vazio)_

---

HTML: [[_html/body-4-tutorial-de-uso.html]] · Seção: [[_body]] · Protocolo: [[_protocolo-de-selecao]]
