"""Parser do inventário de componentes de e-mail.

Lê componentesinventario.md e devolve um registro por variante.

NÃO extrai HTML: 9 variantes têm o base64 truncado no markdown
(43 ocorrências de "[base64 de ~N KB omitido]"). O HTML íntegro vem do
banco — ver .tools/gera_notas.py.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

CAMPOS_PROSA = [
    ("descricao_curta", "#### Descrição curta"),
    ("descricao_detalhada", "#### Descrição detalhada"),
    ("quando_usar", "##### Quando usar"),
    ("quando_nao_usar", "##### Quando NÃO usar"),
    ("copy_ia", "##### Orientações de copy para a IA"),
    ("design_system", "##### Design system"),
    ("direcao_fotografica", "##### Direção fotográfica"),
]

VAZIO = {"", "—", "_(vazio)_"}


@dataclass
class Variante:
    ordem: str
    nome_no_banco: str
    ativa: bool
    variant_id: str
    secao: str
    product_slots: int
    densidade: str | None
    tags: list[str]
    schema_campos: int
    prosa: dict[str, str | None]


def _bloco(texto: str, cabecalho: str) -> str | None:
    padrao = r"(?m)^" + re.escape(cabecalho) + r"\n(.*?)(?=\n#{3,5} |\Z)"
    m = re.search(padrao, texto, re.S)
    if not m:
        return None
    corpo = m.group(1).strip()
    return None if corpo in VAZIO else corpo


def _celula(texto: str, rotulo: str) -> str:
    m = re.search(r"\| \*\*" + re.escape(rotulo) + r"\*\* \| (.*?) \|", texto)
    return m.group(1).strip() if m else ""


def parse(caminho: str) -> list[Variante]:
    with open(caminho, encoding="utf-8") as fh:
        bruto = fh.read()

    variantes: list[Variante] = []
    for bloco in re.split(r"\n(?=### )", bruto)[1:]:
        titulo = bloco.split("\n", 1)[0]
        m = re.match(r"### (\d+\.\d+) · (.+) — `(Ativa|INATIVA)`\s*$", titulo)
        if not m:
            continue
        ordem, nome, status = m.groups()

        tipo = _celula(bloco, "Tipo de seção")
        secao_m = re.search(r"\(`(\w+)`\)", tipo)
        if not secao_m:
            raise ValueError(f"{ordem}: não achei a chave da seção em {tipo!r}")

        tags_raw = _celula(bloco, "Tags")
        densidade = _celula(bloco, "Densidade")
        schema_m = re.search(r"#### Schema de output \((\d+) campos\)", bloco)
        if not schema_m:
            raise ValueError(f"{ordem}: sem cabeçalho de schema")

        variantes.append(
            Variante(
                ordem=ordem,
                nome_no_banco=nome.strip(),
                ativa=(status == "Ativa"),
                variant_id=_celula(bloco, "ID").strip("`"),
                secao=secao_m.group(1),
                product_slots=int(_celula(bloco, "Slots de produto") or 0),
                densidade=None if densidade in VAZIO else densidade,
                tags=[] if tags_raw in VAZIO else [t.strip() for t in tags_raw.split(",")],
                schema_campos=int(schema_m.group(1)),
                prosa={chave: _bloco(bloco, cab) for chave, cab in CAMPOS_PROSA},
            )
        )
    return variantes
