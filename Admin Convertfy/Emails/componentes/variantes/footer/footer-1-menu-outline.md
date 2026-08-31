---
tipo: componente
slug: footer-1-menu-outline
secao: footer
nome_no_banco: "footer 1"
variant_id: 35b5d8fd-59b5-4e0f-92ab-a180745242e0
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: []
momento_vetado: [transacional]

# --- eixos de ranking, na ordem do protocolo ---
objecao: []   # footer não ataca objeção; o ranking degrada para registro (§6.1)
registro: [minimalista-leve]
registro_vetado: []
paleta: [claro]
papel_na_peca: [fecha]

# --- requisitos duros (eliminam) ---
exige: []   # sem ativo específico; a quantidade de destinos de navegação é capturada em itens, não como requisito binário

# --- capacidade e composição ---
product_slots: 0
itens: { min: 4, max: 6 }
peso: null
convivencia: []

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: null
schema_campos: 3
status: aprovada
---

## Descrição curta

Footer padrão de e-commerce: logo, menu de navegação em grid 2×3 de botões outline, 4 ícones sociais com label e bloco legal de copyright + unsubscribe.

## Descrição detalhada

100% vivo exceto logo e ícones sociais: grid de links = table 2 col × 3 rows, cada célula um botão bulletproof outline (border 1px + padding, link no <a> cobrindo o texto). Ícones sociais = 4 PNGs pequenos (~34px) hospedados, com label em texto vivo abaixo — labels vivas garantem navegação mesmo com imagens bloqueadas. Bloco legal em texto vivo com o link de unsubscribe usando a variável nativa da ESP ({{unsubscribe}} do Omnisend) — nunca URL fixa. Gap de compliance da referência: falta o endereço físico do remetente, exigido por CAN-SPAM (e boa prática LGPD) — o template do arsenal deve adicionar uma linha de endereço acima do copyright, mesmo que a referência não tenha. Módulo opcional de UGC (visto nas camadas ocultas) pode virar variante da seção. Footer é o bloco mais reaproveitado do sistema: 1 configuração por cliente, repetida em todo e-mail.

## Quando usar

Todo e-mail — footer é obrigatório. Esta variação (menu em botões grandes) favorece mobile (alvo de toque generoso) e clientes com 4–6 destinos de navegação relevantes (coleções, FAQ, rastreio, conta).

## Quando NÃO usar

Não se aplica "não usar footer" — mas esta variação específica não serve para clientes com menos de 4 links úteis (grid fica capenga; usar variante de lista horizontal simples) ou e-mails transacionais ultra-minimalistas.

## Orientações de copy para a IA

A IA não gera copy aqui — footer é configuração por cliente, não geração por campanha: labels de link vêm do onboarding do cliente (máx ~15 caracteres por label, caps), sociais são URLs fixas, legal é template com ano dinâmico e nome da empresa. Único texto sensível: a frase de unsubscribe deve ser clara e sem dark pattern ("Para cancelar a inscrição, clique aqui"), traduzida pro idioma do público.

## Design system

_(vazio)_

## Direção fotográfica

_(vazio)_

---

HTML: [[_html/footer-1-menu-outline.html]] · Seção: [[_footer]] · Protocolo: [[_protocolo-de-selecao]]
