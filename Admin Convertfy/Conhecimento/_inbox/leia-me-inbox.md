---
tipo: padrao
assunto: inbox
autor: convertfy
status: padrao
---

Área de rascunho: nota começada e ainda não pronta. Fica visível para você no Obsidian e invisível para a IA, porque nada aqui tem `status: aprovado`.

# O fluxo

```
CONTEUDO BRUTO/          material cru chega aqui
      ↓
Conhecimento/_inbox/     vira rascunho (status: rascunho)
      ↓
Conhecimento/<corpus>/   promovido (status: aprovado) — só agora a IA enxerga
```

Os quatro corpora de destino, e o peso de cada um, estão em [[mapa-do-conhecimento]].

# A trava

Uma nota sem `status: aprovado` é **ignorada em silêncio** pelo sincronizador. Isso não é obstáculo — é o portão de qualidade. Escreva à vontade aqui; nada meio pronto contamina a base.

Quando promover: mova o arquivo para a pasta do corpus certo e troque `status: rascunho` por `status: aprovado`. Mover é seguro — wikilinks resolvem por nome de arquivo, não por caminho. **Renomear** é o que quebra.

# Antes de promover, confira

1. O nome do arquivo se explica **fora da pasta**?
2. A nota **abre com uma frase em prosa** — antes de qualquer título, tabela ou imagem?
3. Está entre **1.500 e 10.000 caracteres**?
4. Tem `status: aprovado`, `tipo:`, `assunto:`, `autor:`?

Modelos por tipo em `Padrao Convertfy/_templates/`.
