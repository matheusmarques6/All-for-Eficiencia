// B1 (parte 2) — troca o paragrafo "Nao verifica automaticamente hoje..."
// pela consulta exata de resolucao, por requisito. Matching ASCII-only.
const fs = require('fs');
const path = require('path');
const DIR = path.join(__dirname, '..', 'Admin Convertfy', 'Emails', 'componentes', 'requisitos');

const TXT = {
  'cupom-ativo': 'Resolvedor (código): `email_outline_templates` do flow → o toque tem\n`coupon_code` preenchido e válido. `false` → elimina.',
  'desconto-percentual': 'Resolvedor (código): `email_outline_templates` → a oferta do toque é\npercentual (não frete, não brinde). `false` → elimina.',
  'prazo-real': 'Resolvedor (código): `email_outline_templates` + cadência do flow → existe\nprazo com data/hora real (não "por tempo limitado" vago). `false` → elimina.',
  'desconto-automatico-sem-cupom': 'Resolvedor (código): `email_outline_templates` → oferta marcada como\nautomática no checkout, sem código. `false` → elimina.',
  'desconto-escalonado': 'Resolvedor (código): `email_outline_templates` → mais de um degrau de\ndesconto declarado (ex.: 10/15/20%). `false` → elimina.',
  'duas-ofertas-simultaneas': 'Resolvedor (código): `email_outline_templates` → dois incentivos distintos\nativos no mesmo toque. `false` → elimina.',
  'gift-card-digital': 'Resolvedor (código): `https://<loja>/products.json` → algum produto com\n`gift_card: true` ou `product_type`/`title` contendo "gift". `false` → elimina.',
  'catalogo-de-variantes': 'Resolvedor (código): `products.json` → produtos com mais de uma `variant`\ncom opções distintas (cor, sabor, tamanho). `false` → elimina.',
  'grade-de-tamanho-real': 'Resolvedor (código): `products.json` → alguma `option` de nome\ntamanho/size com ≥3 valores. `false` → elimina.',
  'produtos-com-pagina-propria': 'Resolvedor (código): `products.json` → produtos publicados com `handle`\n(URL própria acessível). `false` → elimina.',
  'colecao-ou-kit': 'Resolvedor (código): `products.json` → `product_type`/`tags` indicando\nkit/combo, ou `collections.json` com coleção temática. `false` → elimina.',
  'produto-com-composicao-relevante': 'Resolvedor (código): `products.json` → `body_html` cita\ncomposição/ingredientes/materiais de forma substantiva. `false` → elimina.',
  'destinos-de-navegacao': 'Resolvedor (código): `https://<loja>/collections.json` → coleções\npublicadas suficientes para um menu (≥3). `false` → elimina.',
  'produto-de-entrada-definido': 'Resolvedor (código): `store_top_products[0]` existe (mais vendido\nidentificado). `false` → elimina.',
  'cor-de-acento-definida': 'Resolvedor (código): `store_brand_identity` → existe cor com papel de\ndestaque/acento (não é `client_stores.cores`). `false` → elimina.',
  'duas-ou-tres-cores-de-identidade': 'Resolvedor (código): `store_brand_identity` → 2–3 cores com papéis\ndefinidos (fundo, texto, destaque). `false` → elimina.',
  'serif-ou-script-display': 'Resolvedor (código): `store_brand_identity` → fonte display serif ou\nscript cadastrada. `false` → elimina.',
  'wordmark-tipografico': 'Resolvedor (código): `store_brand_identity` → logo/wordmark tipográfico\ncadastrado como ativo. `false` → elimina.',
  'manifesto-de-marca-escrito': 'Resolvedor (código, com citação): pesquisa da marca → trecho literal de\nmanifesto/missão citável. Sem trecho citado, `false` → elimina.',
  'tres-diferenciais-concretos': 'Resolvedor (código, com citação): pesquisa da marca → três diferenciais\nconcretos com trecho literal de cada. Sem os três, `false` → elimina.',
  'quatro-criterios-objetivos': 'Resolvedor (código, com citação): pesquisa da marca → quatro critérios\nobjetivos e verificáveis com trecho literal. Sem eles, `false` → elimina.',
  'tres-provas-verificaveis': 'Resolvedor (código, com citação): pesquisa da marca → três provas\nverificáveis (números, certificações, testes) com trecho. Senão `false` → elimina.',
  'motivo-sazonal': 'Resolvedor (código, com citação): pesquisa/calendário → motivo sazonal\nreal e datado para esta loja. Sem ele, `false` → elimina.',
  'duas-acoes-de-suporte': 'Resolvedor (código, com citação): pesquisa da marca → duas ações de\nsuporte reais (troca fácil, atendimento X) com trecho. Senão `false` → elimina.',
  'valores-articulados': 'Resolvedor (código, com citação): pesquisa da marca → valores da marca\narticulados em texto citável. Sem trecho, `false` → elimina.',
};

const DIRETIVA = 'Não se resolve contra a loja: o pipeline **gera** a imagem com esta\npropriedade. Entra em `diretivas_de_imagem` da variante e no brief da foto\n(`photo_direction`); `image_format` confere por pixel o que der conferir.\n**Nunca elimina variante.**';
const REVIEWS = 'Depende do banco de reviews expor metadados (tamanho, foto, credencial).\nFora do escopo até lá: **não elimina**. Quando o banco expuser, o resolvedor\nconsulta `reviews_bank` da loja.';
const PLATAFORMA = 'Superado: isto é configuração de ESP/loja fora da geração, não uma\npergunta sobre a loja. A nota fica no repo como histórico\n(`status: superada`, fora do sync).';

const files = fs.readdirSync(DIR).filter(f => f.endsWith('.md'));
let n = 0;
for (const f of files) {
  const slug = f.replace(/\.md$/, '');
  const p = path.join(DIR, f);
  let s = fs.readFileSync(p, 'utf8');
  const classe = (s.match(/^classe: (\S+)/m) || [])[1];
  const novo = TXT[slug] || (classe === 'diretiva_imagem' ? DIRETIVA : classe === 'reviews' ? REVIEWS : classe === 'plataforma' ? PLATAFORMA : null);
  if (!novo) { console.error('sem texto:', slug); process.exit(1); }
  const anchor = s.indexOf('o verifica automaticamente hoje');
  if (anchor < 0) { console.error('boilerplate nao achado:', slug); continue; }
  const pStart = s.lastIndexOf('**N', anchor);
  let pEnd = s.length;
  for (const stop of ['\r\n\r\n', '\n\n', '\r\n#', '\n#']) {
    const j = s.indexOf(stop, anchor);
    if (j >= 0 && j < pEnd) pEnd = j;
  }
  s = s.slice(0, pStart) + novo + s.slice(pEnd);
  fs.writeFileSync(p, s, 'utf8');
  n++;
}
console.log('ok:', n, 'secoes reescritas');
