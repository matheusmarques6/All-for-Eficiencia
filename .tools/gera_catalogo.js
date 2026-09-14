// Porta Node de gera_catalogo.py (sem Python nesta maquina).
// Gera componentes/_catalogo.md — frontmatter das variantes em uma tabela.
// Uso: node .tools/gera_catalogo.js
const fs = require('fs');
const path = require('path');

const VAULT = path.resolve(__dirname, '..');
const VARIANTES = path.join(VAULT, 'Admin Convertfy', 'Emails', 'componentes', 'variantes');
const SAIDA = path.join(VAULT, 'Admin Convertfy', 'Emails', 'componentes', '_catalogo.md');
const ORDEM = ['hero', 'body', 'products', 'reviews', 'offer', 'footer'];

function parseFm(txt) {
  const bloco = txt.replace(/^---\r?\n/, '').split(/\r?\n---/)[0];
  const fm = {};
  for (const l of bloco.split(/\r?\n/)) {
    if (!l.trim() || l.trim().startsWith('#')) continue;
    const m = l.match(/^([\w_]+):\s*(.*)$/);
    if (!m) continue;
    const [, k, raw] = m;
    let v = raw.trim().replace(/^"|"$/g, '');
    if (v.startsWith('[')) {
      v = v.replace(/^\[|\]$/g, '').split(',').map(x => x.trim()).filter(Boolean);
    } else if (v.startsWith('{')) {
      const o = {};
      for (const kv of v.replace(/^\{|\}$/g, '').split(',')) {
        const [kk, vv] = kv.split(':').map(x => x.trim());
        if (kk) o[kk] = vv === 'null' ? null : (isNaN(vv) ? vv : Number(vv));
      }
      v = o;
    } else if (v === 'true') v = true;
    else if (v === 'false') v = false;
    else if (v !== '' && !isNaN(v)) v = Number(v);
    fm[k] = v;
  }
  return fm;
}

const lista = v => (v && v.length ? v.join(', ') : '—');
const celItens = v => (!v || typeof v !== 'object') ? '—' :
  `${v.min == null ? '?' : v.min}–${v.max == null ? '?' : v.max}`;
const celPeso = v => (!v || typeof v !== 'object') ? '—' :
  `${v.classe || '?'} · ${v.altura_px || '?'}px`;

const fms = [];
for (const d of fs.readdirSync(VARIANTES)) {
  const dir = path.join(VARIANTES, d);
  if (!fs.statSync(dir).isDirectory()) continue;
  for (const f of fs.readdirSync(dir).filter(x => x.endsWith('.md'))) {
    fms.push(parseFm(fs.readFileSync(path.join(dir, f), 'utf8')));
  }
}
if (!fms.length) throw new Error('nenhuma variante');
fms.sort((a, b) => (ORDEM.indexOf(a.secao) - ORDEM.indexOf(b.secao)) || a.slug.localeCompare(b.slug));

const hoje = new Date().toISOString().slice(0, 10);
const cab = 'variante | secao | ativa | schema | momento | momento_vetado | objecao'
  + ' | registro | registro_vetado | paleta | papel_na_peca | exige | diretivas_de_imagem'
  + ' | slots | itens | peso | convivencia';

const linhas = [
  '---',
  'tipo: catalogo',
  `gerado_em: ${hoje}`,
  `variantes: ${fms.length}`,
  'status: gerado',
  '---',
  '',
  '**Gerado por `.tools/gera_catalogo.js` — não editar à mão.**',
  'Uma linha por variante, todos os campos de decisão do frontmatter.',
  'Serve os passos 3–8 de [[_protocolo-de-selecao]] em uma única leitura;',
  'a prosa de julgamento continua nas notas de variante.',
  'Legenda: — = lista vazia (não discrimina) · ✓/✗ = `ativa`.',
  '`exige` = gates (eliminam) · `diretivas_de_imagem` = brief da foto (não elimina).',
  '',
  '| ' + cab + ' |',
  '|' + '---|'.repeat(17),
  ...fms.map(fm => '| ' + [
    `[[${fm.slug}]]`, fm.secao, fm.ativa ? '✓' : '✗', String(fm.schema_campos ?? '?'),
    lista(fm.momento), lista(fm.momento_vetado), lista(fm.objecao),
    lista(fm.registro), lista(fm.registro_vetado), lista(fm.paleta),
    lista(fm.papel_na_peca), lista(fm.exige), lista(fm.diretivas_de_imagem),
    String(fm.product_slots ?? 0), celItens(fm.itens), celPeso(fm.peso),
    lista(fm.convivencia),
  ].join(' | ') + ' |'),
  '',
];
fs.writeFileSync(SAIDA, linhas.join('\n'), 'utf8');
console.log(`_catalogo.md: ${fms.length} variantes`);
