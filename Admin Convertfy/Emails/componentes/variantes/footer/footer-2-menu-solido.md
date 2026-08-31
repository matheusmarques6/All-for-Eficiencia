---
tipo: componente
slug: footer-2-menu-solido
secao: footer
nome_no_banco: "footer 2"
variant_id: 85557ad0-dc20-48fa-8baf-b14c2e1a147b
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: []
momento_vetado: []

# --- eixos de ranking, na ordem do protocolo ---
objecao: []   # footer não ataca objeção; o ranking degrada para registro (§6.1)
registro: [bold-alto-contraste]
registro_vetado: [minimalista-leve]
paleta: [claro]
papel_na_peca: [fecha]

# --- requisitos duros (eliminam) ---
exige: []   # sem ativo específico; a quantidade de destinos de navegação é capturada em itens, não como requisito binário

# --- capacidade e composição ---
product_slots: 0
itens: { min: 5, max: 5 }
peso: { altura_px: 1113, classe: medio, fonte: medido }
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

Footer de alto contraste: menu em 5 botões sólidos (2×2 + 1 full-width de destaque), 3 ícones sociais sem label e bloco legal com unsubscribe em evidência.

## Descrição detalhada

Mesma base técnica do footer outline: table de botões bulletproof (aqui com background sólido — contraste máximo, melhor CTR de rodapé), ícones = PNGs pequenos, legal vivo com variável de unsubscribe da ESP. O quinto botão full-width = row própria com colspan. Ícones sem label: mais limpo, porém sem fallback quando imagens bloqueadas — mitigar com alt text em cada ícone. Mesmo gap de compliance da referência anterior: sem endereço físico — o template adiciona. Diferença de acessibilidade a favor: botões sólidos têm contraste AA garantido em qualquer paleta escura sobre clara.

## Quando usar

Clientes de identidade bold/alto contraste (streetwear, fitness, food casual) e quando existe um destino prioritário que merece o botão full-width. Footer alternativo ao outline — a escolha entre os dois é estética da marca, não funcional.

## Quando NÃO usar

Marcas de estética leve/minimalista clara (botões sólidos pesam visualmente — usar o outline). Clientes com 6+ links iguais em prioridade (a hierarquia 4+1 força uma escolha).

## Orientações de copy para a IA

Configuração por cliente, sem geração por campanha (mesma regra do outro footer). Labels curtos em caps (~12 caracteres). O link full-width recebe o destino de maior valor comercial ("SHOP ALL", "NOVIDADES"). Frase de unsubscribe direta e visível — a referência até a coloca acima do copyright, bom sinal de compliance.

## Design system

_(vazio)_

## Direção fotográfica

_(vazio)_

---

HTML: [[_html/footer-2-menu-solido.html]] · Seção: [[_footer]] · Protocolo: [[_protocolo-de-selecao]]
