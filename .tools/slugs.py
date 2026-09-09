"""Tabela canônica variant_id → slug e variant_id → seção.

Regra do slug: <secao>-<n>-<descritor>, com <n> vindo do nome no banco.
Número repetido na mesma seção desambigua por letra na ordem do inventário
(products-8a / products-8b, reviews-3a / reviews-3b).
"""

# (variant_id, secao, slug) — 44 linhas, na ordem do inventário
_LINHAS = [
    ("dc6c363c-7d4f-4c70-a163-632bcadfdce6", "hero", "hero-10-lineup-de-colecao"),  # 2.1
    ("43f9b0ec-9ebc-4657-b1ef-9cfd5a521895", "hero", "hero-8-lineup-com-lembrete-de-oferta"),  # 2.2
    ("3e241d7f-5f84-4017-a553-880736a450dc", "hero", "hero-2-pergunta-comparativa"),  # 2.3
    ("d9e34a1f-7bc7-47e8-9081-53600b104dd2", "hero", "hero-3-cupom-de-captacao"),  # 2.4
    ("e447ef06-95e2-4c5d-9b6f-c3e0b895f8d2", "hero", "hero-4-editorial-de-pertencimento"),  # 2.5
    ("8858709f-ef36-45d8-98f4-7d8711628cba", "hero", "hero-5-cupom-em-tres-lugares"),  # 2.6
    ("72c32ec8-bbd2-4d2c-a938-3c24b65848cd", "hero", "hero-6-percentual-gigante"),  # 2.7
    ("c90713ff-9821-4d92-98c1-c22008fb9609", "hero", "hero-7-campanha-sem-cupom"),  # 2.8
    ("85006b06-b7db-498e-af9d-4db11be4fd5f", "hero", "hero-9-atendimento-proativo"),  # 2.9
    ("d5fb804f-8934-4c39-b011-950e20802498", "body", "body-2-colagem-de-data-comemorativa"),  # 3.1
    ("4e9726d1-40fe-40ce-aa81-c2a33b062603", "body", "body-3-pitch-de-gift-card"),  # 3.2
    ("63736c6c-7d1b-4c7c-83ea-bae15599f1d7", "body", "body-4-comparativo-em-duas-colunas"),  # 3.3
    ("7d1c214a-abb1-44b6-bb5e-95777fb0f306", "body", "body-5-comparacao-nos-vs-eles"),  # 3.4
    ("35a68bb0-7a74-40bc-a342-32ef68605aaf", "body", "body-6-skin-minimalism-101"),  # 3.5
    ("d699e212-57df-4b68-a80c-2b2aa81372c0", "body", "body-7-faq"),  # 3.6
    ("753d7e86-f909-4322-93d8-99f0f2381c01", "body", "body-8-cards-vidro"),  # 3.7
    ("2daabd5e-f366-4130-b6f8-636ad77781f4", "body", "body-9-key-features-pilulas"),  # 3.8
    ("42c883e5-6c4a-43df-b18f-e7ee866e4ae7", "body", "body-10-listicle-educativo"),  # 3.9
    ("640b0a34-8632-4041-8378-38fe804c1516", "products", "products-8a-quatro-recomendacoes"),  # 4.1
    ("8ef65206-2f01-408f-ab07-c17f57cc136c", "products", "products-2-tres-ingredientes"),  # 4.2
    ("a15a6331-8761-4025-8d70-574c18fcd40b", "products", "products-3-arco-de-novidades"),  # 4.3
    ("7bd9e98b-f016-4495-8245-88df69b8f4e1", "products", "products-4-produto-unico-com-prazo"),  # 4.4
    ("7ef1a9f4-5141-4732-b58c-15628ac8e4a8", "products", "products-5-tres-com-selo-de-percentual"),  # 4.5
    ("fc41efe6-a2dc-493a-ab92-75e30fd13198", "products", "products-6-vitrine-de-sale"),  # 4.6
    ("cee34b0a-030c-43df-93b6-c54de6f00569", "products", "products-7-dois-com-galeria-de-angulos"),  # 4.7
    ("9c00bf11-22e4-4675-98aa-499aee857d7d", "products", "products-8b-grade-3x3"),  # 4.8
    ("2f115df3-1ddd-4ca4-bb45-e3337cef5546", "products", "products-9-grade-de-tamanho"),  # 4.9
    ("d48deaa4-6d8b-4a09-95fb-e512b676c8d8", "reviews", "reviews-1-depoimento-com-credencial"),  # 5.1
    ("7dafa6ca-65de-4907-b52c-dad83ecd63a4", "reviews", "reviews-3a-depoimento-longo-monoespacado"),  # 5.2
    ("cff6c8d8-a0da-4c80-90fa-1875174a75a1", "reviews", "reviews-3b-depoimento-longo-monoespacado"),  # 5.3
    ("f8ed9f85-f0f3-47f3-879a-2dd65aba0f86", "reviews", "reviews-5-prova-por-volume"),  # 5.4
    ("956b9e76-2c97-448e-bbfd-4a97f082e1dd", "reviews", "reviews-6-review-por-variante"),  # 5.5
    ("a8468e9f-c8d8-4c71-b416-6a4f6f5ca0f9", "reviews", "reviews-7-zigue-zague-com-cupom"),  # 5.6
    ("d92f812f-d83e-4e82-99a6-11286eba0e07", "reviews", "reviews-8-ugc-de-comunidade"),  # 5.7
    ("3cee424b-5278-4503-9fa7-2afca3b5d13f", "offer", "offer-1-condicao-sem-imagem"),  # 7.1
    ("304bf7ce-6a23-4c68-b3a5-c37f551aaa5f", "offer", "offer-2-duas-ofertas-sazonais"),  # 7.2
    ("da0b6e11-c681-48af-ae88-316429e25c05", "offer", "offer-3-lembrete-de-cupom"),  # 7.3
    ("69ede46f-1534-431c-bdab-2d7be60ce236", "offer", "offer-4-manifesto-antes-do-cupom"),  # 7.4
    ("5a34dbaf-6710-4282-8b7b-3c03921bd6fc", "offer", "offer-5-tres-diferenciais-e-cupom"),  # 7.5
    ("1e45ed32-01c4-487c-bb60-f986623a3270", "offer", "offer-6-carrinho-preto-e-branco"),  # 7.6
    ("35b5d8fd-59b5-4e0f-92ab-a180745242e0", "footer", "footer-1-menu-outline"),  # 8.1
    ("85557ad0-dc20-48fa-8baf-b14c2e1a147b", "footer", "footer-2-menu-solido"),  # 8.2
    ("a2bb5abd-931e-4884-aae7-627b11c75f19", "footer", "footer-3-dark-editorial"),  # 8.3
    ("7ba06b7c-8a6a-423b-9478-262fb3c2ce1d", "footer", "footer-4-dark-mega-menu"),  # 8.4
]

SLUG_POR_ID = {vid: slug for vid, _, slug in _LINHAS}
SECAO_POR_ID = {vid: secao for vid, secao, _ in _LINHAS}
