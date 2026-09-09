---
tipo: registro
assunto: reorganizacao-do-vault
autor: convertfy
status: padrao
data: 2026-09-08
---

O que foi feito na reorganização de 2026-09-08, e o que ficou pendente. Esta nota não entra na base (`status: padrao`): é registro de manutenção.

Backup íntegro do estado anterior em `/Users/brunopinheiro/Documents/_backup-vault-2026-09-08-211509` — 359 notas. Nada aqui é irreversível.

# O que mudou, em números

| | Antes | Depois |
|---|---|---|
| Notas visíveis para a IA | 124 | **214** |
| Notas que truncavam na leitura | 12 | **0** |
| Maior nota | 130.770 chars (10x o limite) | 10.900 |
| Conteúdo inacessível atrás do corte de 12k | ~490.000 chars | 0 |
| Wikilinks quebrados | 19 (pré-existentes) | **0** |
| Persona | 14.928 / 18.000 | 17.292 / 18.000 |
| Corpora | 1 | 4 |

# As mudanças

**1. Os 11 mapas de pasta saíram da invisibilidade.** Eram `_index.md`, nome que o sincronizador descarta por padrão — o conteúdo mais rico de navegação do vault estava fora da base. Viraram `mapa-<assunto>.md`, com os 70 wikilinks atualizados.

**2. As 12 notas gigantes viraram 90 notas por assunto.** Corte pelas costuras que já existiam (os `# H1`), nunca por tamanho. Cada parte abre com prosa auto-explicativa, tem nome próprio, e as âncoras citadas por outras notas foram preservadas ou redirecionadas uma a uma — 467 links reescritos em 131 arquivos.

**3. Onze nomes de arquivo foram corrigidos.** Critério: ler só o nome, sem a pasta, e ainda saber do que trata. `o-que-e` → `o-que-e-deliverability`, `segmentacao` → `segmentacao-de-campanhas`, `mapa` → `mapa-do-corpus-do-max`, e mais oito.

**4. Arquitetura corpus-first.** `Advisors/Max/` (doutrina de curso) agora convive com `Convertfy/` (o que a casa mediu), `Referencias/` (peças reais) e `Pesquisas/` (dados com amostra). A precedência entre elas está em [[mapa-do-conhecimento]] e, porque é julgamento e precisa valer em toda resposta, também na §10 da persona.

**5. Padrão de escrita e modelos.** `como-escrever-uma-nota.md` mais quatro modelos em `_templates/` (anti-exemplo, decisão com número, referência, pesquisa).

# Três bugs que já existiam e foram corrigidos de passagem

- **``_INDEX`` apontava para lugar nenhum** — 18 ocorrências em 6 arquivos. Não existe `_INDEX.md` em `Conhecimento/`; o único do vault está em `Emails/`, o sistema que o próprio mapa declara que jamais deve se cruzar com este corpus. Redirecionado para `mapa-do-corpus-do-max`.
- **``_numeros-completo#Colisões de slug e veredictos arbitrados``** apontava para uma âncora que nunca existiu naquele arquivo — o título vive no registro de conflitos.
- **``_conflitos#Claims institucionais``** — mesma coisa, âncora inexistente.

# O que NÃO foi feito, de propósito

- **`Emails/` não foi tocada.** 223 notas de outro sistema, com contrato próprio. Renomear ali quebra a geração de e-mail em produção.
- **`persona.md` e `_protocolo.md` não foram renomeados.** São os dois arquivos carregados em toda resposta e podem estar referenciados por caminho na configuração do advisor.
- **As notas `arquitetura-*` não tiveram os nomes de arquivo corrigidos.** São registro datado: reescrever `\_casos-de-teste.md, 20.259 bytes` falsificaria uma medição. Receberam um aviso de datação no topo.

# Pendências

1. **`Convertfy/`, `Referencias/` e `Pesquisas/` estão vazias.** É a maior lacuna da base — enquanto não houver nota lá, a IA não sabe o que é "o jeito da casa" e vai improvisar se perguntada. Os mapas dessas pastas estão em `status: rascunho`; promova para `aprovado` quando cada uma tiver 3+ notas.
2. **Contagens envelhecidas em notas de registro.** Frases como "101 notas de conteúdo em dez pastas" e "os 126 slugs" descrevem o corpus anterior. O conteúdo não mudou, a contagem sim.
3. **Rodar "Re-sincronizar vault"** no admin (Custo de IA → ConvertIA · Saúde) e conferir se entram 214 notas. O mesmo card lista as buscas que voltaram vazias — é a melhor pauta do que escrever primeiro.


---

# Adendo de 2026-09-09

## Referências de e-mail: 29 peças da Well Copy

Entrou o primeiro corpus de peças montadas de verdade. 29 conceitos de e-mail extraídos de um arquivo Figma da agência Well Copy, organizados em nove notas por mecanismo mais um mapa, em `Referencias/email/`. Todas as 29 peças foram capturadas em imagem e a copy foi transcrita verbatim e conferida contra o original. O material bruto está em `CONTEUDO BRUTO/figma-best-performing-emails/`.

O achado que define como essa fonte deve ser usada: **os cartões de notas do autor são paráfrase, não descrição das peças.** Em doze comparações entre cartão e e-mail, a maioria diverge — inclusive um botão que o autor manda replicar e que não existe na peça, um e-mail vendido como "do fundador" que é assinado pelo VP de marketing, e um "post do Reddit" que é recriação visual feita pela própria marca. Nenhuma frase entre aspas dos cartões pode ser tratada como copy real.

Registrado também que **o corpus do Max e a coleção da Well Copy não são independentes**: o exemplo de Founder Check-In que ele narra em `post-purchase` (L3196-3208) é praticamente idêntico a uma peça da coleção. Concordância entre as duas fontes não é replicação.

## 49 notas tinham resumo de busca inútil

Defeito pré-existente, descoberto na verificação final e corrigido.

Uma unidade de trabalho anterior inseriu blocos `# Aviso de autoria` no topo do corpo de dezenas de notas. Como o resumo de busca é gerado da **primeira prosa** — e é por ele que a IA decide qual nota abrir —, o que a IA via era metadado de proveniência:

> `**Faixa L8381-8646 (toda a fala do módulo de deliverability) — outro-provavel.**`

Em vez do assunto da nota. Quarenta e nove notas estavam nessa condição, espalhadas por campanhas, copy, deliverability, doutrina, flows, list-growth, otimização e `_registro/`.

**A correção não removeu o aviso** — ele decide se a IA pode dizer "o Max diz" ou "o material do curso diz". Cada nota recebeu uma frase de abertura auto-explicativa acima dele, escrita a partir do conteúdo real da nota.

Nota de método, para quem for auditar isto depois: o defeito tem **pelo menos quatro formatos** no vault (`Faixa L`, `Faixas L`, `Sem exposição a faixa`, `Toda a fala deste módulo`, além de aberturas com pronome sem antecedente). Uma varredura que procure só um formato subconta. E o inverso também vale: buscar a palavra "faixa" gera falso positivo em notas cujo resumo é bom, como "quantas campanhas por semana, por faixa de faturamento". Vale conferir caso a caso antes de corrigir.

## Estado

| | |
|---|---|
| Notas na base | 227 |
| Vagas de catálogo | 173 de 400 |
| Links quebrados | 0 |
| Notas que truncam | 0 |
| Resumos de busca com metadado | 0 |
