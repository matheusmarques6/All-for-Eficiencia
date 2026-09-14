// B2.1/2.3/2.4 — particiona exige por classe do requisito:
//   gate -> exige | diretiva_imagem -> diretivas_de_imagem | reviews -> requisitos_de_reviews | plataforma -> some
// exige com comentario -> exige: [] e comentario vira bullet em "Quando NAO usar".
const fs = require('fs');
const path = require('path');
const BASE = path.join(__dirname, '..', 'Admin Convertfy', 'Emails', 'componentes');
const REQ = path.join(BASE, 'requisitos');
const VAR = path.join(BASE, 'variantes');

// classes dos requisitos
const classe = {};
for (const f of fs.readdirSync(REQ).filter(f => f.endsWith('.md'))) {
  const s = fs.readFileSync(path.join(REQ, f), 'utf8');
  classe[f.replace(/\.md$/, '')] = (s.match(/^classe: (\S+)/m) || [])[1];
}

let tot = 0, moved = 0, dropped = [], comments = 0;
for (const dir of fs.readdirSync(VAR)) {
  const d = path.join(VAR, dir);
  if (!fs.statSync(d).isDirectory()) continue;
  for (const f of fs.readdirSync(d).filter(f => f.endsWith('.md'))) {
    const p = path.join(d, f);
    let s = fs.readFileSync(p, 'utf8');
    const eol = s.includes('\r\n') ? '\r\n' : '\n';
    const m = s.match(/^exige: (.*)$/m);
    if (!m) { console.error('sem exige:', f); continue; }
    let raw = m[1].trim();
    let comment = null;
    const ci = raw.indexOf('#');
    if (ci >= 0) { comment = raw.slice(ci + 1).trim(); raw = raw.slice(0, ci).trim(); comments++; }
    const items = raw === '[]' || raw === '' ? [] :
      raw.replace(/^\[|\]$/g, '').split(',').map(x => x.trim()).filter(Boolean);

    const gates = [], dirs = [], revs = [];
    for (const it of items) {
      const c = classe[it];
      if (c === 'gate') gates.push(it);
      else if (c === 'diretiva_imagem') dirs.push(it);
      else if (c === 'reviews') revs.push(it);
      else if (c === 'plataforma') dropped.push(f + ':' + it);
      else { console.error('requisito desconhecido', it, 'em', f); process.exit(1); }
    }

    let nova = `exige: [${gates.join(', ')}]${eol}diretivas_de_imagem: [${dirs.join(', ')}]`;
    if (revs.length) nova += `${eol}requisitos_de_reviews: [${revs.join(', ')}]`;
    s = s.replace(m[0], nova);

    // comentario vira bullet em "Quando NAO usar" (ou apos o primeiro heading que exista)
    if (comment) {
      const h = s.match(/^# Quando N.O usar\s*$/mi);
      if (h) {
        const idx = s.indexOf(h[0]) + h[0].length;
        s = s.slice(0, idx) + `${eol}${eol}- (nota do cadastro) ${comment}` + s.slice(idx);
      } else {
        s += `${eol}- (nota do cadastro, ex-comentario de exige) ${comment}${eol}`;
      }
    }
    fs.writeFileSync(p, s, 'utf8');
    tot++; if (dirs.length || revs.length) moved++;
  }
}
console.log('variantes processadas:', tot, '| com campos movidos:', moved, '| comentarios movidos:', comments);
console.log('plataforma removidos:', dropped.join('; '));
