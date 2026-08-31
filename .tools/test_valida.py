"""Checagem do validador, contra um vault de mentira montado em tmp."""
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import valida

NOTA_BOA = """---
tipo: componente
slug: hero-teste
secao: hero
nome_no_banco: "hero teste"
variant_id: 00000000-0000-0000-0000-000000000000
ativa: true
momento: [welcome-1]
objecao: [qualidade-eficacia]
registro: []
paleta: [claro]
papel_na_peca: [abre]
momento_vetado: []
registro_vetado: []
exige: [cupom-ativo]
product_slots: 0
itens: null
peso: { altura_px: 100, classe: leve, fonte: medido }
convivencia: []
aprendizados: []
serve_estruturas: []
fonte: inventario-2026-08-31
status: aprovada
---

## Descrição curta

Texto.
"""


def monta(raiz: Path) -> None:
    for sub in ("variantes/hero", "eixos/momento", "eixos/objecao", "eixos/registro",
                "eixos/paleta", "eixos/papel-na-peca", "requisitos", "convivencia", "_html"):
        (raiz / sub).mkdir(parents=True, exist_ok=True)
    (raiz / "variantes/hero/hero-teste.md").write_text(NOTA_BOA, encoding="utf-8")
    (raiz / "_html/hero-teste.html").write_text("<html></html>", encoding="utf-8")
    for caminho in ("eixos/momento/welcome-1.md", "eixos/objecao/qualidade-eficacia.md",
                    "eixos/paleta/claro.md", "eixos/papel-na-peca/abre.md",
                    "requisitos/cupom-ativo.md"):
        (raiz / caminho).write_text("---\ntipo: eixo\n---\n\nx\n", encoding="utf-8")


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        raiz = Path(tmp) / "componentes"
        monta(raiz)

        erros = valida.rodar(raiz, so_estrutura=True)
        assert erros == [], f"vault limpo devia passar, veio: {erros}"

        # 3: valor de eixo sem nota
        (raiz / "eixos/paleta/claro.md").unlink()
        erros = valida.rodar(raiz, so_estrutura=True)
        assert any("claro" in e and "paleta" in e for e in erros), erros
        (raiz / "eixos/paleta/claro.md").write_text("---\ntipo: eixo\n---\n\nx\n", encoding="utf-8")

        # 4: requisito sem nota
        (raiz / "requisitos/cupom-ativo.md").unlink()
        erros = valida.rodar(raiz, so_estrutura=True)
        assert any("cupom-ativo" in e for e in erros), erros
        (raiz / "requisitos/cupom-ativo.md").write_text("---\ntipo: requisito\n---\n\nx\n", encoding="utf-8")

        # 8: HTML faltando
        (raiz / "_html/hero-teste.html").unlink()
        erros = valida.rodar(raiz, so_estrutura=True)
        assert any("_html" in e for e in erros), erros
        (raiz / "_html/hero-teste.html").write_text("<html></html>", encoding="utf-8")

        # 7: wikilink quebrado
        nota = raiz / "variantes/hero/hero-teste.md"
        nota.write_text(NOTA_BOA + "\nVer [[nota-que-nao-existe]].\n", encoding="utf-8")
        erros = valida.rodar(raiz, so_estrutura=True)
        assert any("nota-que-nao-existe" in e for e in erros), erros
        nota.write_text(NOTA_BOA, encoding="utf-8")

        # 2: chave obrigatória ausente
        nota.write_text(NOTA_BOA.replace("exige: [cupom-ativo]\n", ""), encoding="utf-8")
        erros = valida.rodar(raiz, so_estrutura=True)
        assert any("exige" in e for e in erros), erros

    print("ok: validador pega as 5 quebras testadas")


if __name__ == "__main__":
    main()
