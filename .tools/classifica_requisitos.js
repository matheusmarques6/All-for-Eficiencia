// B1 — classifica os 52 requisitos: classe, fonte_resolucao, default_quando_desconhecido
// Remove verificavel_hoje; plataforma -> status: superada; renomeia secao do corpo.
const fs = require('fs');
const path = require('path');

const DIR = path.join(__dirname, '..', 'Admin Convertfy', 'Emails', 'componentes', 'requisitos');

const MAP = {
  // gate · outline/flow
  'cupom-ativo': ['gate', 'outline'],
  'desconto-percentual': ['gate', 'outline'],
  'prazo-real': ['gate', 'outline'],
  'desconto-automatico-sem-cupom': ['gate', 'outline'],
  'desconto-escalonado': ['gate', 'outline'],
  'duas-ofertas-simultaneas': ['gate', 'outline'],
  // gate · products_json
  'gift-card-digital': ['gate', 'products_json'],
  'catalogo-de-variantes': ['gate', 'products_json'],
  'grade-de-tamanho-real': ['gate', 'products_json'],
  'produtos-com-pagina-propria': ['gate', 'products_json'],
  'colecao-ou-kit': ['gate', 'products_json'],
  'produto-com-composicao-relevante': ['gate', 'products_json'],
  'destinos-de-navegacao': ['gate', 'products_json'],       // collections.json
  'produto-de-entrada-definido': ['gate', 'products_json'], // store_top_products
  // gate · brand_identity
  'cor-de-acento-definida': ['gate', 'brand_identity'],
  'duas-ou-tres-cores-de-identidade': ['gate', 'brand_identity'],
  'serif-ou-script-display': ['gate', 'brand_identity'],
  'wordmark-tipografico': ['gate', 'brand_identity'],
  // gate · pesquisa
  'manifesto-de-marca-escrito': ['gate', 'pesquisa'],
  'tres-diferenciais-concretos': ['gate', 'pesquisa'],
  'quatro-criterios-objetivos': ['gate', 'pesquisa'],
  'tres-provas-verificaveis': ['gate', 'pesquisa'],
  'motivo-sazonal': ['gate', 'pesquisa'],
  'duas-acoes-de-suporte': ['gate', 'pesquisa'],
  'valores-articulados': ['gate', 'pesquisa'],
  // diretiva_imagem (pipeline gera; nao elimina)
  'terco-superior-liso': ['diretiva_imagem', 'nenhuma'],
  'foto-estudio-fundo-claro': ['diretiva_imagem', 'nenhuma'],
  'canto-livre-para-selo': ['diretiva_imagem', 'nenhuma'],
  'corredores-livres-nas-laterais': ['diretiva_imagem', 'nenhuma'],
  'macro-de-produto': ['diretiva_imagem', 'nenhuma'],
  'packshot-vertical': ['diretiva_imagem', 'nenhuma'],
  'packshot-recortado': ['diretiva_imagem', 'nenhuma'],
  'foto-monocromatica': ['diretiva_imagem', 'nenhuma'],
  'foto-de-cena-ambiente': ['diretiva_imagem', 'nenhuma'],
  'ativo-composto-faixa-inteira': ['diretiva_imagem', 'nenhuma'],
  'fragmentos-de-contorno': ['diretiva_imagem', 'nenhuma'],
  'foto-com-pessoas': ['diretiva_imagem', 'nenhuma'],
  'foto-de-campanha-propria': ['diretiva_imagem', 'nenhuma'],
  'acervo-por-angulo': ['diretiva_imagem', 'nenhuma'],
  'embalagem-colorida': ['diretiva_imagem', 'nenhuma'],
  'ornamento-grafico-de-identidade': ['diretiva_imagem', 'nenhuma'],
  // plataforma -> superada
  'estoque-integrado': ['plataforma', 'nenhuma'],
  'bloco-dinamico-de-carrinho': ['plataforma', 'nenhuma'],
  'preference-center-na-esp': ['plataforma', 'nenhuma'],
  // reviews (fora de escopo ate o banco expor metadados)
  'reviews-curtos': ['reviews', 'reviews_bank'],
  'reviews-longos': ['reviews', 'reviews_bank'],
  'foto-de-uso-real': ['reviews', 'reviews_bank'],
  'depoimento-com-credencial': ['reviews', 'reviews_bank'],
  'foto-do-depoente': ['reviews', 'reviews_bank'],
  'selo-compra-verificada': ['reviews', 'reviews_bank'],
  'tres-reviews-distintos': ['reviews', 'reviews_bank'],
  'ugc-autorizado': ['reviews', 'reviews_bank'],
};

const files = fs.readdirSync(DIR).filter(f => f.endsWith('.md'));
let missing = files.map(f => f.replace(/\.md$/, '')).filter(s => !MAP[s]);
let extra = Object.keys(MAP).filter(s => !files.includes(s + '.md'));
if (missing.length || extra.length) {
  console.error('sem classe:', missing, '| no mapa sem arquivo:', extra);
  process.exit(1);
}

for (const f of files) {
  const slug = f.replace(/\.md$/, '');
  const [classe, fonte] = MAP[slug];
  const p = path.join(DIR, f);
  let s = fs.readFileSync(p, 'utf8');
  const eol = s.includes('\r\n') ? '\r\n' : '\n';

  // frontmatter = primeiro bloco --- ... ---
  const m = s.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!m) { console.error('sem frontmatter:', f); process.exit(1); }
  let fmLines = m[1].split(/\r?\n/);

  // remove verificavel_hoje e campos que vamos reescrever (idempotente)
  fmLines = fmLines.filter(l => !/^(verificavel_hoje|classe|fonte_resolucao|default_quando_desconhecido):/.test(l));

  // plataforma -> status: superada
  if (classe === 'plataforma') {
    fmLines = fmLines.map(l => l.startsWith('status:') ? 'status: superada' : l);
  }

  // insere depois de familia: (ou no fim)
  const novo = [
    `classe: ${classe}`,
    `fonte_resolucao: ${fonte}`,
    `default_quando_desconhecido: false`,
  ];
  const idx = fmLines.findIndex(l => l.startsWith('familia:'));
  if (idx >= 0) fmLines.splice(idx + 1, 0, ...novo);
  else fmLines.push(...novo);

  let out = s.replace(m[0], '---' + eol + fmLines.join(eol) + eol + '---');
  // renomeia secao do corpo
  out = out.replace(/^# Como o agente verifica\s*$/m, '# Como se resolve');
  fs.writeFileSync(p, out, 'utf8');
}
console.log('ok:', files.length, 'requisitos classificados');
