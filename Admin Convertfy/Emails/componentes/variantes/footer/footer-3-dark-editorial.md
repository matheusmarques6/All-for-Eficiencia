---
tipo: componente
slug: footer-3-dark-editorial
secao: footer
nome_no_banco: "footer 3 - dark"
variant_id: a2bb5abd-931e-4884-aae7-627b11c75f19
ativa: true

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: []
momento_vetado: []

# --- eixos de ranking, na ordem do protocolo ---
objecao: []   # footer não ataca objeção; o ranking degrada para registro (§6.1)
registro: [premium-editorial]
registro_vetado: [minimalista-leve]
paleta: [full-dark]
papel_na_peca: [fecha]

# --- requisitos duros (eliminam) ---
exige: []  # requisito de central de preferencias removido (fix lote B item B) -- procedencia inferida, sem clausula de "Quando NAO usar" no inventario

# --- capacidade e composição ---
product_slots: 0
itens: { min: 3, max: 3 }
peso: { altura_px: 755, classe: medio, fonte: medido }
convivencia: []

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: null
schema_campos: 4
status: aprovada
---

## Descrição curta

Footer dark editorial: logo tipográfico oversized, 3 links de texto entre hairlines, sociais em círculos e bloco legal completo (endereço + unsubscribe + preferências).

## Descrição detalhada

Fundo preto sólido, tudo vivo exceto ícones. Logo: se o cliente tem wordmark simples, renderizar como texto gigante vivo (como na referência — sobrevive a imagens bloqueadas); logos complexos viram imagem. Links = rows de texto centralizadas com border-top/bottom 1px na TD (hairlines full-width, zero botão). Ícones em círculo = PNGs prontos com o círculo embutido (border-radius em imagem não rola no Outlook). É a referência de compliance do arsenal: endereço físico presente, unsubscribe destacado em cor, e link de preference center — o "Manage my preferences" reduz unsubscribes totais oferecendo redução de frequência como alternativa; usar a URL de preference center da ESP. Os outros dois footers devem herdar essas três linhas legais deste.

## Quando usar

Marcas fashion/lifestyle de identidade forte e estética escura, com poucos destinos de navegação (3 links máx) e presença visual em redes (IG/TikTok/Pinterest). Quando o cliente tem preference center configurado na ESP.

## Quando NÃO usar

Clientes que precisam de 4+ links de rodapé (estrutura comporta 3 — mais que isso, usar os footers de grid). Marcas claras/leves (inverter a paleta descaracteriza; usar o outline).

## Orientações de copy para a IA

Configuração por cliente (mesma regra dos outros footers). Labels de link minúsculos e editoriais (~10 caracteres). Endereço físico completo obrigatório. Frase de unsubscribe + "Gerenciar preferências" na linha seguinte, ambos linkados.

## Design system

_(vazio)_

## Direção fotográfica

_(vazio)_

---

HTML: [[_html/footer-3-dark-editorial.html]] · Seção: [[_footer]] · Protocolo: [[_protocolo-de-selecao]]
