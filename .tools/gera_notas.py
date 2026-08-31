"""Gera as 44 notas de variante com a prosa verbatim e frontmatter esqueleto.

One-shot. Recusa sobrescrever nota existente — o julgamento das tasks 6-11
não pode ser perdido por rodar isto duas vezes.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import inventario
import slugs

VAULT = Path(__file__).resolve().parent.parent
RAIZ = VAULT / "Admin Convertfy" / "Emails" / "componentes"
FONTE = r"C:\Users\Usuario\Downloads\componentesinventario.md"

TITULOS = [
    ("descricao_curta", "Descrição curta"),
    ("descricao_detalhada", "Descrição detalhada"),
    ("quando_usar", "Quando usar"),
    ("quando_nao_usar", "Quando NÃO usar"),
    ("copy_ia", "Orientações de copy para a IA"),
    ("design_system", "Design system"),
    ("direcao_fotografica", "Direção fotográfica"),
]

MOLDE = """---
tipo: componente
slug: {slug}
secao: {secao}
nome_no_banco: "{nome}"
variant_id: {vid}
ativa: {ativa}

# --- momento: FILTRO (passos 4-6), não ranking ---
momento: []
momento_vetado: []

# --- eixos de ranking, na ordem do protocolo ---
objecao: []
registro: []
registro_vetado: []
paleta: []
papel_na_peca: []

# --- requisitos duros (eliminam) ---
exige: []

# --- capacidade e composição ---
product_slots: {slots}
itens: null
peso: null
convivencia: []

# --- fios para o resto do vault ---
aprendizados: []
serve_estruturas: []

# --- proveniência ---
fonte: inventario-2026-08-31
densidade_no_banco: {densidade}
schema_campos: {schema}
status: {status}
---

{corpo}

---

HTML: [[_html/{slug}.html]] · Seção: [[_{secao}]] · Protocolo: [[_protocolo-de-selecao]]
"""


def main() -> None:
    variantes = inventario.parse(FONTE)
    criadas = 0
    for v in variantes:
        slug = slugs.SLUG_POR_ID[v.variant_id]
        destino = RAIZ / "variantes" / v.secao / f"{slug}.md"
        if destino.exists():
            print(f"pula (já existe): {destino.name}")
            continue
        destino.parent.mkdir(parents=True, exist_ok=True)

        partes = []
        for campo, titulo in TITULOS:
            valor = v.prosa[campo]
            partes.append(f"## {titulo}\n\n{valor if valor is not None else '_(vazio)_'}")

        vazia = all(x is None for x in v.prosa.values())
        destino.write_text(
            MOLDE.format(
                slug=slug,
                secao=v.secao,
                nome=v.nome_no_banco,
                vid=v.variant_id,
                ativa="true" if v.ativa else "false",
                slots=v.product_slots,
                densidade=v.densidade if v.densidade else "null",
                schema=v.schema_campos,
                status="sem-julgamento" if vazia else "aprovada",
                corpo="\n\n".join(partes),
            ),
            encoding="utf-8",
        )
        criadas += 1
    print(f"{criadas} nota(s) criada(s)")


if __name__ == "__main__":
    main()
