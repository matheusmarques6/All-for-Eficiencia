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


def altura(html: str) -> int:
    html = MSO_SO_OUTLOOK.sub("", html)
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


def main() -> None:
    for arquivo in sorted(HTML.glob("*.html")):
        px = altura(arquivo.read_text(encoding="utf-8"))
        print(f"{arquivo.stem}\t{px}\t{classe(px)}")


if __name__ == "__main__":
    main()
