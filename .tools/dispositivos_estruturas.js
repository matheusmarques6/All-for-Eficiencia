// B9 — loja no frontmatter + tabela "Dispositivos (objecao x papel)" no corpo
const fs = require('fs');
const path = require('path');
const DIR = path.join(__dirname, '..', 'Admin Convertfy', 'Emails', 'estruturas', 'welcome');

const NR = ' — **não realizável hoje** ([[header-sem-variante]])';
const NRC = ' — **não realizável hoje** ([[cta-sem-variante]])';

const D = {
  'avelmore-deadline-objecao': { loja: 'avelmore', rows: [
    ['header', 'apoio', 'barra-de-logo' + NR, '—'],
    ['hero', 'abre', 'oferta-na-frente', 'preco-valor'],
    ['body', 'meio', 'varredura-de-objecoes', 'varredura (todas)'],
    ['offer', 'apoio', 'custo-de-adiar-em-faixa', 'disponibilidade-urgencia'],
    ['products', 'apoio', 'grade-com-oferta-no-titulo', 'amplitude-de-catalogo'],
    ['footer', 'fecha', 'menu-de-saida', '—'],
  ]},
  'avelmore-inspecao-antecipada': { loja: 'avelmore', rows: [
    ['header', 'apoio', 'logo-sobreposto-ao-hero' + NR, '—'],
    ['hero', 'abre', 'entrega-imediata-da-promessa', 'preco-valor'],
    ['body', 'meio', 'tese-que-nomeia-a-objecao', 'qualidade-eficacia'],
    ['body', 'apoio', 'faixa-de-garantias-3-icones', 'confianca-no-canal'],
    ['products', 'apoio', 'grade-2x2-com-avaliacao-e-preco', 'amplitude-de-catalogo'],
    ['cta', 'ponte', 'botao-isolado' + NRC, '—'],
    ['reviews', 'fecha', 'depoimento-unico-que-fecha-a-tese', 'adesao-social'],
    ['footer', 'fecha', 'menu-de-saida', '—'],
  ]},
  'avelmore-mecanismo-e-origem': { loja: 'avelmore', rows: [
    ['header', 'apoio', 'barra-de-logo' + NR, '—'],
    ['body', 'abre', 'historia-de-origem-com-prova-fisica', 'confianca-no-canal'],
    ['body', 'meio', 'mecanismo-verificavel-com-cupom', 'qualidade-eficacia'],
    ['products', 'apoio', 'grade-como-demonstracao-da-tese', 'amplitude-de-catalogo'],
    ['footer', 'fecha', 'menu-de-saida', '—'],
  ]},
  'avelmore-prova-social-cirurgica': { loja: 'avelmore', rows: [
    ['header', 'apoio', 'barra-de-logo' + NR, '—'],
    ['hero', 'abre', 'reabertura-em-pergunta', 'preco-valor'],
    ['body', 'apoio', 'garantias-reusadas-do-toque-1', 'confianca-no-canal'],
    ['reviews', 'meio', 'dois-depoimentos-com-agregado', 'adesao-social'],
    ['cta', 'fecha', 'faixa-de-cta' + NRC, '—'],
    ['footer', 'fecha', 'menu-de-saida', '—'],
  ]},
  'carta-plain-text-extensao': { loja: 'carta', rows: [
    ['body', 'peca-inteira', 'carta-de-extensao-plain-text', 'preco-valor'],
  ]},
  'medicube-comparacao-categoria': { loja: 'medicube', rows: [
    ['header', 'apoio', 'logo-com-tagline-de-categoria' + NR, '—'],
    ['body', 'peca-inteira', 'comparacao-contra-categoria-com-cupom', 'confianca-no-canal'],
    ['products', 'apoio', 'grade-2x2-com-rating-e-preco', 'amplitude-de-catalogo'],
    ['footer', 'fecha', 'menu-de-saida', '—'],
  ]},
  'medicube-escassez-com-prova-de-demanda': { loja: 'medicube', rows: [
    ['hero', 'abre', 'prazo-como-noticia', 'disponibilidade-urgencia'],
    ['body', 'meio', 'escassez-com-prova-de-demanda', 'disponibilidade-urgencia'],
    ['reviews', 'apoio', 'tres-depoimentos-colados-na-pressao', 'adesao-social'],
    ['offer', 'fecha', 'prazo-por-extenso-com-garantias', 'disponibilidade-urgencia'],
    ['footer', 'fecha', 'menu-de-saida', '—'],
  ]},
  'medicube-ultima-batida': { loja: 'medicube', rows: [
    ['header', 'apoio', 'logo-com-tagline' + NR, '—'],
    ['offer', 'peca-inteira', 'contagem-final-comprimida', 'disponibilidade-urgencia'],
    ['footer', 'fecha', 'menu-de-saida', '—'],
  ]},
};

for (const [slug, cfg] of Object.entries(D)) {
  const p = path.join(DIR, slug + '.md');
  let s = fs.readFileSync(p, 'utf8');
  const eol = s.includes('\r\n') ? '\r\n' : '\n';

  // loja no frontmatter
  if (/^loja:\s*$/m.test(s)) s = s.replace(/^loja:\s*$/m, 'loja: ' + cfg.loja);
  else if (!new RegExp('^loja: ' + cfg.loja, 'm').test(s)) s = s.replace(/^loja: .*$/m, 'loja: ' + cfg.loja);

  if (s.includes('# Dispositivos (objecao')) { console.log('ja tem:', slug); continue; }

  const table = [
    '# Dispositivos (objecao × papel)',
    '',
    'Vocabulário para o Estruturador emitir `requisitos.dispositivo` em vez de prosa.',
    '',
    '| Seção | Papel | Dispositivo | Objeção |',
    '|---|---|---|---|',
    ...cfg.rows.map(r => `| ${r[0]} | ${r[1]} | ${r[2]} | ${r[3]} |`),
    '', ''
  ].join(eol);

  // insere antes de "**Fio narrativo:**" se existir; senao antes do primeiro heading depois de "# A estrutura"
  const fio = s.indexOf('**Fio narrativo:**');
  if (fio >= 0) {
    s = s.slice(0, fio) + table + s.slice(fio);
  } else {
    s += eol + table;
  }
  fs.writeFileSync(p, s, 'utf8');
  console.log('ok:', slug);
}
