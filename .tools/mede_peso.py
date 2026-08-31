"""Mede a altura aproximada de cada bloco somando as declarações do HTML.

Método: soma dos `height:Npx` (CSS, cobre `<td>`/`<div>`/`<img>`) e
`padding-top:Npx` / `padding:A B C D` das células. É proxy, não render —
serve para separar em quatro classes, não para pixel-perfect. Por isso a
classe é o que entra na decisão; a altura entra como rastro.

Três ajustes feitos sobre a primeira versão (calibrados contra o sanity
check da Task 12 — reviews-8 tem que sair peca-inteira, que é a única
variante com altura declarada na prosa):

1. `height:\\d+px` sem âncora casava substring de `line-height:`/
   `max-height:`, inflando a soma com valores de entrelinha de texto.
   Corrigido com lookbehind negativo de letra/hífen antes de "height:".
2. Todo `<img height="N">` do corpus também carrega `style="...
   height:Npx"` idêntico (conferido nos 44 HTMLs — nenhum caso isolado,
   nenhuma divergência) — contar os dois é contar a mesma imagem 2x.
   Removida a soma separada do atributo HTML; a CSS já cobre.
3. Os 44 HTMLs usam comentários condicionais MSO (`<!--[if mso]>` /
   `<!--[if gte mso 9]>`) para fallback VML de Outlook — um `<v:rect
   style="height:Npx">` repetindo a MESMA altura de um `<td style=
   "height:Npx">` real, alguns próximos ao dobro. Esses blocos são
   removidos antes de medir. `<!--[if !mso]>` NÃO é removido: é o
   padrão inverso (conteúdo real, visível em todo cliente exceto
   Outlook) — remover apagaria conteúdo de verdade.

Rodada de correção 1 (achado do revisor): o Bug 3 acima tratava TODO
bloco `[if mso]` como duplicata, mas há um segundo padrão no corpus —
o `<td>` de imagem de fundo (`background-image` + `background-size:
LARGxALTpx`, sem `height:` próprio) só tinha a altura real escrita
dentro do `<v:rect>` do bloco MSO. Removendo o bloco cegamente, essa
altura desaparecia (confirmado em ao menos 15 dos 44 arquivos — 3 no
`body`, 8 no `hero`, 2 no `offer`, 2 no `products`).

Rodada de correção 2 (achado do revisor): a correção 1 somava o
`background-size` contra o TOTAL GLOBAL do documento, sempre que o
`<td>` de fundo não tinha `height:` própria. Mas esse `<td>` costuma ter
conteúdo aninhado real por dentro (headline, pílulas, CTA) que já entra
na soma global — somar o `background-size` por cima conta essa altura
duas vezes (`body-9`: conteúdo aninhado 1055, fundo 1029, entrega errada
2084). O pedido original era `max(background-size, soma do PRÓPRIO
`<td>`)`, não soma+extra. Corrigido isolando a subárvore de cada `<td>`
de fundo (do `<td ...>` até o `</td>` correspondente, por profundidade)
e substituindo a contribuição dela por
`max(soma dentro da subárvore, background-size dela)` — em vez de somar
por cima do total. Os 15 `<td>` de fundo do corpus não se aninham nem se
sobrepõem entre si (conferido), então cada subárvore é processada uma
vez, isolada.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
HTML = VAULT / "Admin Convertfy" / "Emails" / "componentes" / "_html"

# Blocos condicionais só-Outlook (mso / gte mso N) — fallback VML que
# duplica altura já contada no HTML real. `[if !mso]` fica de fora do
# lookahead porque é o padrão oposto (conteúdo real, não duplicata).
MSO_SO_OUTLOOK = re.compile(r"<!--\[if\s+(?!!)[^\]]*\]>.*?<!\[endif\]-->", re.S)


def classe(px: int) -> str:
    if px < 600:
        return "leve"
    if px < 1200:
        return "medio"
    if px < 2000:
        return "pesado"
    return "peca-inteira"


def _soma_declaracoes(html: str) -> int:
    """Soma height:/padding declarados NESTE fragmento (sem tratar background-size)."""
    total = 0
    total += sum(int(n) for n in re.findall(r"(?<![-a-zA-Z])height:\s*(\d+)px", html))
    for corpo in re.findall(r"padding:\s*([^;\"']+)", html):
        valores = re.findall(r"(\d+)px", corpo)
        if len(valores) == 4:
            total += int(valores[0]) + int(valores[2])
        elif len(valores) == 2:
            total += int(valores[0]) * 2
        elif len(valores) == 1:
            total += int(valores[0]) * 2
    total += sum(int(n) for n in re.findall(r"padding-top:\s*(\d+)px", html))
    total += sum(int(n) for n in re.findall(r"padding-bottom:\s*(\d+)px", html))
    return total


def _fim_td(html: str, inicio: int) -> int:
    """Índice logo após o `</td>` que fecha o `<td ...>` que começa em `inicio`."""
    profundidade = 0
    for m in re.finditer(r"<td\b[^>]*>|</td\s*>", html[inicio:], re.I):
        profundidade += 1 if m.group(0).lower().startswith("<td") else -1
        if profundidade == 0:
            return inicio + m.end()
    raise ValueError("</td> correspondente não encontrado")


def altura(html: str) -> int:
    html = MSO_SO_OUTLOOK.sub("", html)
    total = _soma_declaracoes(html)

    # Padrão (b): <td> de imagem de fundo sem height próprio — a única
    # declaração textual da altura é o background-size, mas o <td> pode ter
    # conteúdo aninhado real (já contado em `total`). Isola a subárvore desse
    # <td> e troca a contribuição dela por max(soma da subárvore, fundo) —
    # nunca soma os dois.
    for m in re.finditer(r"<td\b[^>]*>", html):
        tag = m.group(0)
        bg = re.search(r"background-size:\s*\d+px\s+(\d+)px", tag)
        if not bg:
            continue
        tem_altura_propria = re.search(r"(?<![-a-zA-Z])height:\s*(\d+)px", tag) or re.search(r'\bheight="(\d+)"', tag)
        if tem_altura_propria:
            continue
        subarvore = html[m.start():_fim_td(html, m.start())]
        soma_subarvore = _soma_declaracoes(subarvore)
        contribuicao = max(soma_subarvore, int(bg.group(1)))
        total += contribuicao - soma_subarvore
    return total


def main() -> None:
    for arquivo in sorted(HTML.glob("*.html")):
        px = altura(arquivo.read_text(encoding="utf-8"))
        print(f"{arquivo.stem}\t{px}\t{classe(px)}")


if __name__ == "__main__":
    main()
