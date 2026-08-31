"""Validador da camada componentes/ do vault.

Uso:  python .tools/valida.py
Sai com 1 e imprime uma linha por erro. Silêncio e código 0 = tudo certo.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

VAULT = Path(__file__).resolve().parent.parent
RAIZ = VAULT / "Admin Convertfy" / "Emails" / "componentes"
FONTE = r"C:\Users\Usuario\Downloads\componentesinventario.md"

EIXOS = {
    "momento": "momento",
    "momento_vetado": "momento",
    "objecao": "objecao",
    "registro": "registro",
    "registro_vetado": "registro",
    "paleta": "paleta",
    "papel_na_peca": "papel-na-peca",
}

OBRIGATORIAS = [
    "tipo", "slug", "secao", "nome_no_banco", "variant_id", "ativa",
    "momento", "momento_vetado", "objecao", "registro", "registro_vetado",
    "paleta", "papel_na_peca", "exige", "product_slots", "itens", "peso",
    "convivencia", "aprendizados", "serve_estruturas", "fonte", "status",
]

CAMPO_PARA_TITULO = {
    "descricao_curta": "Descrição curta",
    "descricao_detalhada": "Descrição detalhada",
    "quando_usar": "Quando usar",
    "quando_nao_usar": "Quando NÃO usar",
    "copy_ia": "Orientações de copy para a IA",
    "design_system": "Design system",
    "direcao_fotografica": "Direção fotográfica",
}


def frontmatter(caminho: Path) -> dict:
    texto = caminho.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", texto, re.S)
    if not m:
        return {}
    return yaml.safe_load(m.group(1)) or {}


def _corpo(caminho: Path) -> str:
    texto = caminho.read_text(encoding="utf-8")
    return re.sub(r"^---\n.*?\n---\n", "", texto, flags=re.S)


def _secao_do_corpo(corpo: str, titulo: str) -> str | None:
    padrao = r"(?m)^## " + re.escape(titulo) + r"\n(.*?)(?=\n## |\n---\n|\Z)"
    m = re.search(padrao, corpo, re.S)
    if not m:
        return None
    valor = m.group(1).strip()
    return None if valor == "_(vazio)_" else valor


def rodar(raiz: Path, so_estrutura: bool = False) -> list[str]:
    erros: list[str] = []
    notas_variante = sorted(raiz.glob("variantes/*/*.md"))

    # índice de todas as notas do vault, por nome sem extensão (Obsidian resolve assim)
    indice = {p.stem for p in VAULT.rglob("*.md") if ".obsidian" not in p.parts}
    indice |= {p.stem for p in raiz.rglob("*.md")}

    for nota in notas_variante:
        fm = frontmatter(nota)
        rel = nota.relative_to(raiz)

        for chave in OBRIGATORIAS:
            if chave not in fm:
                erros.append(f"{rel}: falta a chave obrigatória `{chave}`")

        for chave, pasta in EIXOS.items():
            for valor in fm.get(chave) or []:
                if not (raiz / "eixos" / pasta / f"{valor}.md").exists():
                    erros.append(f"{rel}: `{chave}: {valor}` sem nota em eixos/{pasta}/")

        for valor in fm.get("exige") or []:
            if not (raiz / "requisitos" / f"{valor}.md").exists():
                erros.append(f"{rel}: `exige: {valor}` sem nota em requisitos/")

        for valor in fm.get("convivencia") or []:
            if not (raiz / "convivencia" / f"{valor}.md").exists():
                erros.append(f"{rel}: `convivencia: {valor}` sem nota em convivencia/")

        slug = fm.get("slug")
        if slug and not (raiz / "_html" / f"{slug}.html").exists():
            erros.append(f"{rel}: sem _html/{slug}.html")

    # wikilinks de toda a camada
    for nota in sorted(raiz.rglob("*.md")):
        for alvo in re.findall(r"\[\[([^\]|#]+)", nota.read_text(encoding="utf-8")):
            nome = alvo.strip().split("/")[-1]
            if nome.endswith(".html"):
                continue  # aponta para _html/; a regra 8 já cobre a existência
            nome = nome.removesuffix(".md")
            if nome and nome not in indice:
                erros.append(f"{nota.relative_to(raiz)}: wikilink quebrado [[{alvo}]]")

    if so_estrutura:
        return erros

    # prosa verbatim + coerência do status
    sys.path.insert(0, str(Path(__file__).parent))
    import inventario
    import slugs

    por_slug = {slugs.SLUG_POR_ID[v.variant_id]: v for v in inventario.parse(FONTE)}

    for slug, v in por_slug.items():
        nota = raiz / "variantes" / v.secao / f"{slug}.md"
        if not nota.exists():
            erros.append(f"variantes/{v.secao}/{slug}.md: nota ausente")
            continue
        corpo = _corpo(nota)
        for campo, titulo in CAMPO_PARA_TITULO.items():
            esperado = v.prosa[campo]
            veio = _secao_do_corpo(corpo, titulo)
            if esperado != veio:
                erros.append(f"variantes/{v.secao}/{slug}.md: `{campo}` diverge do inventário")

        fm = frontmatter(nota)
        vazia = all(x is None for x in v.prosa.values())
        if vazia and fm.get("status") != "sem-julgamento":
            erros.append(f"variantes/{v.secao}/{slug}.md: prosa vazia exige status sem-julgamento")
        if not vazia and fm.get("status") == "sem-julgamento":
            erros.append(f"variantes/{v.secao}/{slug}.md: tem prosa, não pode ser sem-julgamento")

    return erros


if __name__ == "__main__":
    problemas = rodar(RAIZ)
    for linha in problemas:
        print(linha)
    print(f"\n{len(problemas)} problema(s)")
    sys.exit(1 if problemas else 0)
