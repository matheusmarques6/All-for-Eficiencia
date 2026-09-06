# -*- coding: utf-8 -*-
import io, re

CRIT = """Critério: **idioleto** ([[_autoria]] §2.1) — ausência de "I recommend", "my favorite"
e "I like to", presença de "at the end of the day" e "obviously", e o fecho coletivo
"thank you guys… see you in the next one". **A saudação de abertura não é critério e
não pode ser citada como evidência:** o laudo testou e ela caiu — o walkthrough de
Figma abre com "Hello, hello" e é comprovadamente Max, que em L7817 digita `@max` e
diz "tags me" ([[_autoria]] §5)."""

PROVAVEL = """Sem prova nominal. A classificação é **estilométrica**: o bloco pertence ao aglomerado
do único bloco `outro-provado` e não traz um só marcador do idioleto de Max.
`outro-provavel` não é `outro-provado` — não está provado que a voz não é dele, está
estabelecido que é muito improvável ([[_autoria]] §7.3)."""

PROVADO = """**Prova nominal — a única do corpus.** Em L5753 o narrador fala de Max em terceira
pessoa: "So we have a email marketing brain, something that **Max had put together
himself**". Não é inferência estilométrica: é o falante se distinguindo de Max.
Ressalva registrada no laudo — L5753 vem de ASR ([[_autoria]] §4.1)."""

def edit(path, registro=None, aviso=None, subs=(), anchor=None):
    with io.open(path, encoding='utf-8') as f:
        t = f.read()
    orig = t
    if registro is not None:
        new = 'registro: ' + registro
        if re.search(r'^registro: .*$', t, re.M):
            t = re.sub(r'^registro: .*$', new, t, count=1, flags=re.M)
        else:
            t = re.sub(r'^(autor: .*)$', r'\1\n' + new, t, count=1, flags=re.M)
    if aviso is not None:
        block = "# Aviso de autoria\n\n" + aviso.strip() + "\n"
        if anchor:
            assert anchor in t, "ANCHOR MISS %s" % path
            t = t.replace(anchor, block, 1)
        else:
            m = list(re.finditer(r'^---\s*$', t, re.M))
            assert len(m) >= 2, path
            i = m[1].end()
            t = t[:i] + "\n\n" + block + "\n" + t[i:].lstrip('\n')
    for a, b in subs:
        assert a in t, "MISS in %s: %r" % (path, a[:80])
        t = t.replace(a, b)
    if t != orig:
        with io.open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(t)
        print("ok   " + path)
    else:
        print("NOOP " + path)
