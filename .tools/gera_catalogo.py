"""Gera componentes/_catalogo.md — frontmatter das variantes em uma tabela.

Uso:  python .tools/gera_catalogo.py
Reescreve o arquivo inteiro. Rodar sempre que um frontmatter de variante mudar.
"""
from __future__ import annotations

import datetime
from pathlib import Path

import yaml

VAULT = Path(__file__).resolve().parent.parent
VARIANTES = VAULT / "Admin Convertfy" / "Emails" / "componentes" / "variantes"
SAIDA = VAULT / "Admin Convertfy" / "Emails" / "componentes" / "_catalogo.md"

ORDEM_SECOES = ["hero", "body", "products", "reviews", "offer", "footer"]


def frontmatter(md: Path) -> dict:
    texto = md.read_text(encoding="utf-8")
    assert texto.startswith("---"), f"{md} sem frontmatter"
    # split("---") truncaria nos comentários "# --- ..." dentro do bloco;
    # o delimitador de fechamento é uma linha que COMEÇA com ---.
    bloco = texto[4:].split("\n---", 1)[0]
    return yaml.safe_load(bloco)


def lista(v) -> str:
    return ", ".join(v) if v else "—"


def celula_itens(v) -> str:
    if not v:
        return "—"
    lo, hi = v.get("min"), v.get("max")
    return f"{'?' if lo is None else lo}–{'?' if hi is None else hi}"


def celula_peso(v) -> str:
    if not v:
        return "—"
    return f"{v.get('classe', '?')} · {v.get('altura_px', '?')}px"


def linha(fm: dict) -> str:
    cols = [
        f"[[{fm['slug']}]]",
        fm["secao"],
        "✓" if fm.get("ativa") else "✗",
        str(fm.get("schema_campos", "?")),
        lista(fm.get("momento")),
        lista(fm.get("momento_vetado")),
        lista(fm.get("objecao")),
        lista(fm.get("registro")),
        lista(fm.get("registro_vetado")),
        lista(fm.get("paleta")),
        lista(fm.get("papel_na_peca")),
        lista(fm.get("exige")),
        str(fm.get("product_slots", 0)),
        celula_itens(fm.get("itens")),
        celula_peso(fm.get("peso")),
        lista(fm.get("convivencia")),
    ]
    return "| " + " | ".join(cols) + " |"


def main() -> None:
    fms = [frontmatter(p) for p in sorted(VARIANTES.rglob("*.md"))]
    assert fms, "nenhuma variante encontrada"
    fms.sort(key=lambda f: (ORDEM_SECOES.index(f["secao"]), f["slug"]))

    hoje = datetime.date.today().isoformat()
    cab = (
        "variante | secao | ativa | schema | momento | momento_vetado | objecao"
        " | registro | registro_vetado | paleta | papel_na_peca | exige"
        " | slots | itens | peso | convivencia"
    )
    linhas = [
        "---",
        "tipo: catalogo",
        f"gerado_em: {hoje}",
        f"variantes: {len(fms)}",
        "status: gerado",
        "---",
        "",
        "**Gerado por `.tools/gera_catalogo.py` — não editar à mão.**",
        "Uma linha por variante, todos os campos de decisão do frontmatter.",
        "Serve os passos 3–8 de [[_protocolo-de-selecao]] em uma única leitura;",
        "a prosa de julgamento continua nas notas de variante.",
        "Legenda: — = lista vazia (não discrimina) · ✓/✗ = `ativa`.",
        "",
        "| " + cab + " |",
        "|" + "---|" * 16,
        *[linha(fm) for fm in fms],
        "",
    ]
    SAIDA.write_text("\n".join(linhas), encoding="utf-8")
    print(f"{SAIDA.name}: {len(fms)} variantes")


if __name__ == "__main__":
    main()
