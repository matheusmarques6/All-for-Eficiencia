"""Checagem do validador, contra um vault de mentira montado em tmp."""
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import valida
import slugs

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

# Inventário de mentira com UMA variante, usando um variant_id real da
# tabela de slugs (2.1 · hero section 10 → hero-10-lineup-de-colecao).
# rodar() no modo completo faz slugs.SLUG_POR_ID[variant_id], então o id
# precisa existir de verdade lá.
VID_REAL = "dc6c363c-7d4f-4c70-a163-632bcadfdce6"

INVENTARIO_FAKE = """# Inventário de mentira

### 2.1 · hero section 10 — `Ativa`

| | |
|---|---|
| **Tipo de seção** | Hero (`hero`) |
| **Status** | Ativa (disponível para a IA) |
| **Densidade** | — |
| **Slots de produto** | 0 |
| **Tags** | — |
| **ID** | `""" + VID_REAL + """` |

#### Descrição curta

Curta de teste.

#### Descrição detalhada

Detalhada de teste.

#### Contexto para a IA

##### Quando usar

Quando usar de teste.

##### Quando NÃO usar

Quando não usar de teste.

##### Orientações de copy para a IA

Copy de teste.

##### Design system

Design de teste.

##### Direção fotográfica

Foto de teste.

#### Schema de output (4 campos)

nada aqui.
"""

CORPO_CERTO = """## Descrição curta

Curta de teste.

## Descrição detalhada

Detalhada de teste.

## Quando usar

Quando usar de teste.

## Quando NÃO usar

Quando não usar de teste.

## Orientações de copy para a IA

Copy de teste.

## Design system

Design de teste.

## Direção fotográfica

Foto de teste.
"""


def nota_completa(corpo: str, status: str = "aprovada") -> str:
    return (
        NOTA_BOA.split("\n\n## Descrição curta")[0]
        .replace("slug: hero-teste", "slug: hero-10-lineup-de-colecao")
        .replace(
            "variant_id: 00000000-0000-0000-0000-000000000000",
            f"variant_id: {VID_REAL}",
        )
        .replace("status: aprovada", f"status: {status}")
        + "\n\n"
        + corpo
        + "\n---\n\nHTML: [[_html/hero-10-lineup-de-colecao.html]]\n"
    )


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


def testa_modo_completo() -> None:
    """Exercita as regras 1, 5 e 6, que só rodam com so_estrutura=False."""
    with tempfile.TemporaryDirectory() as tmp:
        raiz = Path(tmp) / "componentes"
        monta(raiz)
        (raiz / "variantes/hero/hero-teste.md").unlink()
        (raiz / "_html/hero-teste.html").unlink()

        fixture = Path(tmp) / "inventario_fake.md"
        fixture.write_text(INVENTARIO_FAKE, encoding="utf-8")
        fonte_original = valida.FONTE
        valida.FONTE = str(fixture)
        try:
            nota = raiz / "variantes/hero/hero-10-lineup-de-colecao.md"
            html = raiz / "_html/hero-10-lineup-de-colecao.html"
            html.write_text("<html></html>", encoding="utf-8")

            # regra 1: nota ausente
            erros = valida.rodar(raiz)
            assert any("nota ausente" in e for e in erros), erros

            # tudo certo: zero erros
            nota.write_text(nota_completa(CORPO_CERTO), encoding="utf-8")
            erros = valida.rodar(raiz)
            assert erros == [], f"nota fiel devia passar, veio: {erros}"

            # regra 5: prosa divergente
            nota.write_text(
                nota_completa(CORPO_CERTO.replace("Foto de teste.", "Foto ALTERADA.")),
                encoding="utf-8",
            )
            erros = valida.rodar(raiz)
            assert any("direcao_fotografica" in e for e in erros), erros

            # regra 6: prosa presente não pode ser sem-julgamento
            nota.write_text(
                nota_completa(CORPO_CERTO, status="sem-julgamento"), encoding="utf-8"
            )
            erros = valida.rodar(raiz)
            assert any("não pode ser sem-julgamento" in e for e in erros), erros

            # correção A: frontmatter quebrado vira erro, não traceback
            nota.write_text(
                "---\nchave: [nao fechado\n---\n\n" + CORPO_CERTO, encoding="utf-8"
            )
            erros = valida.rodar(raiz)
            assert any("frontmatter ilegível" in e for e in erros), erros
        finally:
            valida.FONTE = fonte_original

    print("ok: modo completo cobre as regras 1, 5, 6 e o frontmatter ilegível")


if __name__ == "__main__":
    main()
    testa_modo_completo()
