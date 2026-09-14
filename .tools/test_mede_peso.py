"""Sanity check falseavel de mede_peso.py: 3 calibradores reais + 2 sinteticos.

reviews-8 sozinho nao discrimina (tanto o medidor quebrado quanto o correto
davam peca-inteira, por estar 2,6x-4,6x acima do corte de 2000). hero-2 e
offer-3 sao os que importam: tem altura real declarada no proprio
background-size do HTML, perto de fronteira de classe, e o medidor da
rodada 1 perdia essa altura ao remover o bloco MSO — caia em leve.

Mas os 3 calibradores so tem piso (>= altura minima), entao passam tanto com
a implementacao correta (max por <td>) quanto com uma que soma o
background-size por cima do conteudo aninhado (rodada 2, bug). Os 2 testes
sinteticos abaixo miram a regra max() diretamente, nas duas direcoes.
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

# fundo (1000) maior que o conteudo aninhado (400) -> vence o fundo
HTML_FUNDO_MAIOR = """
<table><tr><td style="background-image:url(x);background-size:600px 1000px;">
  <table><tr><td style="height:400px;">conteudo</td></tr></table>
</td></tr></table>
"""

# conteudo aninhado (900) maior que o fundo (300) -> vence o conteudo
HTML_CONTEUDO_MAIOR = """
<table><tr><td style="background-image:url(x);background-size:600px 300px;">
  <table><tr><td style="height:900px;">conteudo</td></tr></table>
</td></tr></table>
"""


def main() -> None:
    for nome, altura_min, classe_proibida in CALIBRADORES:
        px = altura((HTML / f"{nome}.html").read_text(encoding="utf-8"))
        assert px >= altura_min, f"{nome}: mediu {px}px, esperava >= {altura_min}px"
        assert classe(px) != classe_proibida, f"{nome}: caiu em {classe_proibida}, nao devia"
        print(f"ok: {nome} -> {px}px, {classe(px)}")

    px = altura(HTML_FUNDO_MAIOR)
    assert px == 1000, f"regra max() quebrada: fundo 1000 + aninhado 400 deu {px}, esperava 1000 (nao 1400)"
    print(f"ok: fundo maior que aninhado -> {px}px (max, nao soma)")

    px = altura(HTML_CONTEUDO_MAIOR)
    assert px == 900, f"regra max() quebrada: aninhado 900 + fundo 300 deu {px}, esperava 900"
    print(f"ok: aninhado maior que fundo -> {px}px (max, nao soma)")

    print("ok: 3 calibradores + 2 sinteticos passaram")


if __name__ == "__main__":
    main()
