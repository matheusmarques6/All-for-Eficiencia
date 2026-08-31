"""Sanity check falseavel de mede_peso.py, contra 3 calibradores reais.

reviews-8 sozinho nao discrimina (tanto o medidor quebrado quanto o correto
davam peca-inteira, por estar 2,6x-4,6x acima do corte de 2000). hero-2 e
offer-3 sao os que importam: tem altura real declarada no proprio
background-size do HTML, perto de fronteira de classe, e o medidor da
rodada anterior perdia essa altura ao remover o bloco MSO — caia em leve.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from mede_peso import HTML, altura, classe

CALIBRADORES = [
    # (arquivo, altura minima esperada, classe proibida)
    ("reviews-8-ugc-de-comunidade", 2000, "leve"),      # declarado ~2500px na prosa
    ("hero-2-pergunta-comparativa", 567, "leve"),        # background-size: 600px 567px
    ("offer-3-lembrete-de-cupom", 639, "leve"),          # background-size do HTML
]


def main() -> None:
    for nome, altura_min, classe_proibida in CALIBRADORES:
        px = altura((HTML / f"{nome}.html").read_text(encoding="utf-8"))
        assert px >= altura_min, f"{nome}: mediu {px}px, esperava >= {altura_min}px"
        assert classe(px) != classe_proibida, f"{nome}: caiu em {classe_proibida}, nao devia"
        print(f"ok: {nome} -> {px}px, {classe(px)}")
    print(f"ok: {len(CALIBRADORES)} calibradores passaram")


if __name__ == "__main__":
    main()
