---
tipo: padrao
status: aprovada
versao: 2
escrito_em: 2026-09-13
fonte: email_vault_docs, email_intents, email_structure_refs, email_learnings (banco em 13/09), vault-parser.ts, vault-sync.service.ts, curador-vault.ts
---

# Padrão do vault de e-mail

Única nota que descreve como as outras são escritas. Quem cria ou edita
nota lê este arquivo antes; quem muda o código que consome o vault
atualiza este arquivo no mesmo commit.

**Parte A** é o padrão. **Parte B** é o que ainda falta — só código: o
lado vault foi executado em 13/09 (commits `B1`–`B12` deste repo).

---

## Parte A — o padrão

### A1. O que o vault é e o que ele não é

- É a fonte de decisão do Estruturador e do Curador. O runtime nunca lê o
  Obsidian nem o Git: lê as tabelas que o sync popula (webhook de push,
  cron de 30 min, botão na aba Conhecimento). Env: `VAULT_REPO`,
  `VAULT_BRANCH`, `VAULT_BASE_PATH` (default `Admin Convertfy/Emails`).
- Nota inválida não derruba o sync: vira `skipped_invalid` em
  `vault_sync_runs` e a versão anterior continua servindo. Arquivo
  removido do repo → `is_active=false`, nunca DELETE.
- **Regra de ouro:** o que está em frontmatter é contrato e é aplicado
  por código; o que está no corpo é julgamento e é lido por LLM. Nunca
  escrever uma regra dura só em prosa, e nunca escrever prosa dentro de
  um campo de frontmatter.

### A2. Pastas → tabelas → quem lê

| Pasta | Arquivo | Tabela | Lê |
|---|---|---|---|
| `intencoes/{flow}/` | `{flow}-{n}.md`, `_flow.md`, `_progressao.md` | `email_intents` | Seletor, Estruturador |
| `estruturas/{flow}/` | `{slug}.md` | `email_structure_refs` | Estruturador, Curador (ordem e papel das seções) |
| `aprendizados/{flow|_global}/` | `{slug}.md` | `email_learnings` | Estruturador, Curador |
| `componentes/` | `_protocolo-de-selecao.md`, `_julgamento.md`, `_parametros-da-loja.md`, `_catalogo.md`, `_inventario.md`, `_casos-de-teste.md` | `email_vault_docs` (kind = nome da nota) | Curador |
| `componentes/secoes/` | `_{secao}.md` | `email_vault_docs` kind=`secao` | Curador |
| `componentes/variantes/{secao}/` | `{secao}-{n}-{slug}.md` | `email_vault_docs` kind=`variante` | Curador (e código: contrato) |
| `componentes/eixos/{eixo}/` | `{valor}.md` | `email_vault_docs` kind=`eixo` | Curador (vocabulário) |
| `componentes/requisitos/` | `{valor}.md` | `email_vault_docs` kind=`requisito` | **código** (eliminação por `exige`) |
| `componentes/convivencia/` | `{valor}.md` | `email_vault_docs` kind=`convivencia` | **código** (pares proibidos) + Curador |
| `componentes/lacunas/` | `{slug}.md` | `email_vault_docs` kind=`lacuna` | Curador (só as da seção), painel |
| `componentes/doutrina/` | `{slug}.md` | `email_vault_docs` kind=`doutrina` | Curador (≤3 por seção) |
| `_html/`, `.obsidian/`, `_INDEX.md`, `_PADRAO-DO-VAULT.md`, templates | — | ignorados / doc | — |

Nomes de arquivo em kebab-case ASCII, sem acento, sem espaço. O `slug` é
o nome do arquivo sem `.md`, único no vault inteiro (é o que `[[links]]`
resolvem e o que a telemetria cita). Arquivos em UTF-8 **NFC** (acentos
pré-compostos — o vault mistura NFC/NFD silenciosamente se não se
policiar; grep byte a byte falha em NFD).

### A3. Frontmatter comum

- `status: proposta` não é servido a agente nenhum. `superada` fica no
  repo para histórico e sai do sync. Só `aprovada` é lida.
- **Data não é regra.** Nota não carrega "(07/09) isto foi aposentado"
  nem "SUPERADO: ignore". Regra que mudou é reescrita; a anterior vira
  `status: superada` em arquivo próprio ou some. O histórico é o Git.
- **Sem comentários na linha de um campo YAML.** O parser atual é
  line-based: `exige: []  # nota` vira string e o campo morre.
  Comentário de linha inteira (`# --- bloco ---`) é tolerado.
- Listas como listas (`[a, b]`), mapas como mapas
  (`{ min: 2, max: 3 }`). Atenção: até o parser virar YAML de verdade
  (Parte B), mapas inline chegam ao banco como string — o formato certo
  nas notas já está adotado; o conserto é no código, não nas notas.

### A4. Variante — `componentes/variantes/{secao}/{secao}-{n}-{slug}.md`

Campos que o código aplica (todos presentes, mesmo vazios):

```yaml
tipo: componente            # legado do parser; muda para "variante" junto com o parser novo
slug: hero-2-pergunta-comparativa
secao: hero                 # hero | body | products | reviews | offer | footer | header | cta
nome_no_banco: "welcome - hero section 2"
variant_id: <uuid>          # um por nota, uma nota por id
ativa: true
schema_campos: 4            # 0 = não é candidata (sem endereço para a copy)
momento: []                 # vazio = não discrimina; não vazio = elimina fora da lista
momento_vetado: []
objecao: []                 # vazio só em footer/header
registro: []
registro_vetado: []
paleta: []
papel_na_peca: [abre]       # obrigatório, ≥1
exige: []                   # SÓ requisitos com classe: gate
diretivas_de_imagem: []     # requisitos com classe: diretiva_imagem — não eliminam, viram brief
requisitos_de_reviews: []   # (opcional) requisitos classe reviews — desempate, não gate
product_slots: 0
itens: { min: null, max: null }
peso: { altura_px: 727, classe: medio, fonte: medido }
                            # classe: leve <600 · medio 600-1200 · pesado 1200-2000 · peca-inteira >2000
                            # fonte: medido (soma do HTML) | declarado (prosa); nunca estimado
convivencia: []
aprendizados: []
serve_estruturas: []
```

Corpo, nesta ordem: `## Descrição curta` · `## Descrição detalhada` ·
`## Quando usar` · `## Quando NÃO usar` · `## Orientações de copy para a
IA` · `## Design system` · `## Direção fotográfica`.

Regras:

- **Uma nota por `variant_id`.** Renomear variante é renomear o arquivo
  (Git guarda o nome antigo), não criar segunda nota.
- **Espelhamento:** `Quando NÃO usar` e frontmatter dizem a mesma coisa.
  Se a prosa veta "campanha promocional", `momento_vetado` contém
  `campanha-promocional`. O código aplica o frontmatter; a prosa explica
  por quê. Prosa sem espelho não elimina nada.
- Nome por **dispositivo**, não por campanha de origem:
  `body-3-pitch-de-gift-card` está certo; "bridge features cards" não diz
  nada. `nome_no_banco` pode ser o que for; o `slug` diz o que a variante
  faz.
- Cor em `Direção fotográfica`: por papel ("cor de fundo do e-mail",
  "cinza neutro, papel: piso"), nunca hex de marca de origem. Hex é
  permitido só em `Design system`, citando o HTML base, com a ressalva
  "a marca troca pela paleta dela".

### A5. Eixo — `componentes/eixos/{eixo}/{valor}.md`

Vocabulários fechados. Um valor só existe se tem nota. Variante que cita
valor sem nota é rejeitada no sync (quando o parser validar — Parte B).

| Eixo | Valores | Usado por |
|---|---|---|
| `objecao` (11) | adesao-social, amplitude-de-catalogo, composicao-formulacao, confianca-no-canal, disponibilidade-urgencia, escolha-variedade, pertencimento, preco-valor, qualidade-eficacia, suporte-duvida, uso-aprendizado | Seletor (alvo), Estruturador, Curador (ranking 1º) |
| `papel-na-peca` (6) | abre, apoio, fecha, meio, peca-inteira, ponte | Estruturador, Curador (ranking 4º) |
| `momento` (21) | ver `eixos/momento/` | **código** (`momentoDoEmail(flow, n)` → filtro, passo 5) |
| `registro` (10) | ver `eixos/registro/` | Curador (veto e ranking 2º) |
| `paleta` (8) | ver `eixos/paleta/` | Curador (ranking 3º) |

`momento` é derivado por código de `flow_type` + `email_number`; o mapa
está em `curador-vault.ts:momentoDoEmail`. Mudou o vocabulário, muda o
mapa **no mesmo commit** — e o sync deve validar que as 21 notas e o mapa
coincidem (Parte B). Valor novo: nota do valor + pelo menos uma variante
que o declare no mesmo commit; valor sem variante é `status: proposta`.

### A6. Requisito — `componentes/requisitos/{valor}.md`

Um requisito é uma pergunta de sim/não sobre a loja. **Só entra em
`exige:` o que o pipeline não produz e a plataforma não resolve.**

```yaml
tipo: requisito
valor: cupom-ativo
familia: comercial | dado-operacional | catalogo | prova-social | ativo-visual
classe: gate | diretiva_imagem | plataforma | reviews
fonte_resolucao: outline | products_json | brand_identity | pesquisa | reviews_bank | nenhuma
default_quando_desconhecido: false
status: aprovada
procedencia: inventario | doutrina
```

| Classe | Significado | O que o código faz |
|---|---|---|
| `gate` (25) | a loja tem ou não tem; o pipeline não inventa | elimina a variante quando a resposta é `false` |
| `diretiva_imagem` (16) | o pipeline gera a foto com essa propriedade | não elimina; entra em `diretivas_de_imagem` e no brief; `image_format` confere por pixel |
| `reviews` (8) | depende do banco de reviews | fora do escopo até o banco expor metadados; não elimina; mora em `requisitos_de_reviews` |
| `plataforma` (3) | configuração de ESP/loja fora da geração | não é requisito; nota `status: superada` |

Fontes por gate: ver a tabela completa em [[_parametros-da-loja]]
(Parte 2). A consulta exata mora na própria nota, seção
`# Como se resolve`. Corpo: `# O que é` · `# Por que é eliminatório e
não preferência` · `# Como se resolve` · `# Variantes que exigem`.

### A7. Convivência · A8. Seção · A9. Lacuna

- **Convivência**: restrição entre dois blocos da mesma peça.
  `efeito: veta` é aplicado por código no passo 8; `avisa` vai ao QA.
- **Seção** (`secoes/_{secao}.md`): `# Cobertura` (contagens geradas) ·
  `# Chave de decisão` (a tabela de desempate do passo 9 — **sem coluna
  nem frase sobre `exige`**: gates rodam no passo 4, antes do ranking;
  isso mora nos requisitos) · `# Onde a seção não cobre` (dispositivos
  por `objecao × papel`, apontando para as lacunas).
- **Lacuna**: frontmatter com `secao`, `sobre: biblioteca | cadastro |
  codigo | loja`, `status: aberta | em-andamento | fechada`,
  `descoberta_em`, `fonte`, `pede:` (o dispositivo que faltou),
  `fecha_com`. Lacuna `sobre: cadastro`/`codigo` é tarefa, não
  conhecimento: fecha e sai do sync. Só `sobre: biblioteca` alimenta o
  gerador de anatomias.

### A10. Doutrina, aprendizado, estrutura, intenção

- **Doutrina**: `fonte` obrigatória com caminho e linhas do corpus;
  `secao` obrigatória (ou `geral`). Ensina critério; nunca contém regra
  dura (regras duras viram eixo, requisito ou convivência).
- **Aprendizado**: `origem_estrutura` obrigatória;
  `tipo_regra: restricao-dura | preferencia`;
  `aplica_a: [flow e/ou secao]` (hero|body|products|reviews|offer|footer|
  copy|cta e/ou welcome|abandoned_cart|…). `restricao-dura` só é aceita
  se a regra também está expressa em frontmatter de variante, eixo ou
  convivência; senão é `preferencia`. O Curador recebe só os aprendizados
  da seção.
- **Estrutura de referência**: `loja`, `flow_type`, `emails`, `secoes`,
  `performance` (se houver), `procedencia` — e a tabela
  `# Dispositivos (objecao × papel)` no corpo, que dá ao Estruturador o
  vocabulário para emitir `requisitos.dispositivo` em vez de prosa.
  Seção `header`/`cta` marcada "não realizável hoje" enquanto o código
  não as monta. Mostra o que existe; não prova o que funciona.
- **Intenção**: contrato rico (`modo`, `riscos_elegiveis`,
  `aliviadores_admissiveis`, `proibicoes`, `trabalhos_fixos`,
  `veiculos_exigidos`, `n_objecoes`) + `incentivo_obrigatorio: true|false`
  por toque. Fonte: `email_outline_templates`, **nunca inferido** — o
  outline atual tem cupom nos 8 toques do welcome, incluindo o #8
  (extensão), por isso todos são `true`.
- **Flows sem intenção não geram.** Só welcome tem contrato ativo; o
  gate de prontidão recusa gerar outro flow até a intenção existir.

### A11. Precedência (a tabela viva está em [[_julgamento]])

Contrato do flow → fatos verificáveis da loja → alvo do Seletor →
aprendizado com origem → estrutura de referência → doutrina → pesquisa &
diagnóstico (contexto, nunca fatos operacionais) → preferência do modelo
(não decide nada).

### A12. O que o código aplica e o que o LLM lê

| Passo do protocolo | Quem | Campo |
|---|---|---|
| 3 candidatas | código | `ativa`, `schema_campos > 0` |
| 4 exige | **código** | `exige` × resolvedor de requisitos (A6) |
| 5 momento | **código** | `momento`, `momento_vetado`, `registro_vetado` × `momentoDoEmail` |
| 6 capacidade | código | `product_slots`, `itens` × `requisitos` do Estruturador |
| 8 convivência e peso | **código** (veta) + LLM (avisa) | `convivencia`, `peso` |
| 7 ranking, 9 desempate | LLM, com prosa das notas | `objecao`, `registro`, `paleta`, `papel_na_peca`, chave da seção |
| descartes do Estruturador | **código** | `descartes[].dispositivo` × `objecao`/`papel` da variante |

O LLM recebe só o que sobreviveu aos passos 3–6 e 8-veto, com a prosa das
finalistas. O que eliminou o quê vai à telemetria com o requisito e a
fonte.

### A13. Checklist antes de commitar uma nota

1. Slug único, kebab-case, sem acento; arquivo em UTF-8 NFC.
2. Frontmatter completo para o `tipo`, sem comentário na linha de campo,
   listas como listas, mapas como mapas.
3. Todo valor de eixo tem nota; todo `exige` tem requisito com
   `classe: gate`; diretivas em `diretivas_de_imagem`.
4. `Quando NÃO usar` espelhado em `momento_vetado` / `registro_vetado` /
   `exige`.
5. Sem data como regra, sem "aposentado", sem "ignore o acima".
6. Uma nota por `variant_id`; renomeou, moveu o arquivo.
7. `gera_catalogo.py` rodado (`_catalogo`, `_inventario`, cabeçalhos de
   `secoes/_*`).
8. Este arquivo atualizado se o padrão mudou.

---

## Parte B — o que falta (só código)

O lado vault foi executado em 13/09. Pendências, em ordem:

| # | O quê | Onde | Implicação |
|---|---|---|---|
| 1 | Parser YAML real em `vault-parser.ts` (lib `yaml`), com validação: `peso`/`itens` mapa, `exige` lista de gates existentes, `classe` obrigatória em requisito, valor de eixo existe | código | 40 `peso` e 24 `itens` que hoje chegam como string ao banco se corrigem sem tocar nota; o parser vira o fiscal do padrão |
| 2 | Resolvedor de requisitos por `fonte_resolucao` (outline, products.json/collections.json, store_brand_identity, pesquisa com citação) | código | passo 4 vira eliminação verificável; `default_quando_desconhecido: false` |
| 3 | Religar passos 4, 5 e 8-veto no Curador e no resgate; remover `semExige`; `diretivas_de_imagem` → brief da foto | código | o payoff: o funil elimina pelo frontmatter e a telemetria diz quem caiu por quê |
| 4 | Sync valida `momentoDoEmail` × notas de `eixos/momento/` | código | o vocabulário e o mapa não podem divergir em silêncio |
| 5 | Gate de prontidão: flow sem intenção não gera | código | elimina o cenário de 09/09 (outline genérico sem alvo) |
| 6 | Regerar `_catalogo`/`_inventario`/cabeçalhos com as colunas novas (`classe`, `diretivas_de_imagem`) — `gera_catalogo.py`; não há Python nesta máquina, rodar onde houver ou portar para Node | tooling | os índices gerados hoje citam o esquema antigo |
| 7 | Aba admin: `output_schema`/`rendered_html`/`photo_direction`; cupons por idioma + `incentivo_obrigatorio` em `/admin/outlines`; papéis da paleta em Identidade visual | admin | fora do Obsidian (era o B13) |

**Teste de aceite:** depois do item 3, a primeira geração da Hero Boxers
mostra na telemetria, por posição: quem foi eliminado por `momento`, quem
por `exige` (com a fonte), quem sobreviveu, e as lacunas de `body`
([[body-tese-3-itens-sem-cupom]], [[body-garantias-3-selos]]) e
`products` ([[products-grade-preco-cheio]]) com nome.
