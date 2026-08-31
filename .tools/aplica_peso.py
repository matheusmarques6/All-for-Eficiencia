"""Aplica o peso medido (mede_peso.py) no campo `peso:` das 44 notas de variante.

Uso: python .tools/aplica_peso.py
Só troca a linha `peso: null` por `peso: { altura_px: N, classe: C, fonte: F }`.
reviews-8-ugc-de-comunidade é o calibrador (Task 12): usa a altura declarada
na prosa (2500px) e fonte: declarado. As outras 43 usam o medido, fonte: medido.
"""
from __future__ import annotations

from pathlib import Path

from mede_peso import HTML, altura, classe

VAULT = Path(__file__).resolve().parent.parent
VARIANTES = VAULT / "Admin Convertfy" / "Emails" / "componentes" / "variantes"

CALIBRADOR = "reviews-8-ugc-de-comunidade"
CALIBRADOR_ALTURA = 2500


def main() -> None:
    notas = {p.stem: p for p in VARIANTES.glob("*/*.md")}
    htmls = {p.stem for p in HTML.glob("*.html")}
    faltando = htmls - notas.keys()
    if faltando:
        raise SystemExit(f"nota sem HTML correspondente: {faltando}")

    aplicadas = 0
    for stem, nota in sorted(notas.items()):
        html_path = HTML / f"{stem}.html"
        if not html_path.exists():
            raise SystemExit(f"HTML ausente para nota {stem}")

        if stem == CALIBRADOR:
            px, fonte = CALIBRADOR_ALTURA, "declarado"
        else:
            px, fonte = altura(html_path.read_text(encoding="utf-8")), "medido"

        linha_nova = f"peso: {{ altura_px: {px}, classe: {classe(px)}, fonte: {fonte} }}"
        texto = nota.read_text(encoding="utf-8")
        linhas = texto.split("\n")
        alvo = [i for i, l in enumerate(linhas) if l == "peso: null"]
        if len(alvo) != 1:
            raise SystemExit(f"{nota}: esperava 1 linha 'peso: null', achou {len(alvo)}")
        linhas[alvo[0]] = linha_nova
        nota.write_text("\n".join(linhas), encoding="utf-8")
        aplicadas += 1

    print(f"{aplicadas} notas atualizadas.")


if __name__ == "__main__":
    main()
