---
tipo: indice
status: aprovada
---

# Comece aqui

Biblioteca de componentes de e-mail (Convertfy). O cérebro é
[[_protocolo-de-selecao]] — 9 passos para escolher variante por seção,
eliminar antes de rankear. Tudo o mais existe para servir esse protocolo.

# Caminho de seleção (o fluxo do agente)

0. [[_PADRAO-DO-VAULT]] — como as notas deste vault são escritas. Quem
   cria ou edita nota lê antes; quem muda o código que consome o vault
   atualiza o padrão no mesmo commit.
1. [[_protocolo-de-selecao]] — as regras. Leia primeiro, sempre.
2. `intencoes/<flow>/<n>.md` — o que ESTE toque deve fazer (objeção-alvo,
   papel de cada bloco). Só existe `welcome` hoje.
3. `estruturas/<flow>/` — referência concreta, se houver.
4. [[_catalogo]] — frontmatter das 44 variantes em uma tabela; filtra e
   rankeia (passos 3–8) em uma única leitura.
5. Nota da variante finalista em `componentes/variantes/<secao>/` — prosa
   de julgamento, copy, design system, direção fotográfica.
6. `secoes/_<secao>.md` — chave de desempate (passo 9).

Zero candidata sobrevivendo não é erro: declare e registre em
`componentes/lacunas/` (ver o protocolo, "Quando nenhuma variante sobrevive").

# Mapa

| Pasta / nota | O que é |
|---|---|
| [[_PADRAO-DO-VAULT]] | O padrão das notas: frontmatter é contrato (código), corpo é julgamento (LLM). |
| [[_protocolo-de-selecao]] | Como escolher. As regras, na ordem. |
| [[_julgamento]] | O que nunca fazemos, precedência entre fontes, quando recusar. |
| [[_catalogo]] | Gerado — tabela única com o frontmatter das variantes. |
| [[_parametros-da-loja]] | Ponte vault ↔ código: o que o Montador recebe e o que falta. |
| [[_inventario]] | Números e proveniência da biblioteca (fonte Supabase, md5). |
| [[_casos-de-teste]] | O protocolo reproduzindo decisões já validadas. |
| `componentes/variantes/<secao>/` | 44 notas de variante: frontmatter máquina + prosa julgamento. |
| `componentes/secoes/_*.md` | Cobertura e chave de decisão por seção. |
| `componentes/eixos/` | Vocabulário controlado: momento, objecao, registro, paleta, papel-na-peca. Uma nota por valor. |
| `componentes/requisitos/` | Uma nota por requisito, com `classe` (gate elimina; diretiva_imagem vira brief; reviews aguarda o banco) e `fonte_resolucao` — como o código resolve. |
| `componentes/convivencia/` | Regras de coexistência entre variantes na mesma peça. |
| `componentes/lacunas/` | O que falta — zero-elegíveis, duplicatas, campos mortos. Cidadã de primeira classe. |
| `componentes/_html/` | O HTML real das variantes, conferido por md5 contra o banco. |
| `intencoes/<flow>/` | O que cada toque do flow deve fazer + `_flow` (doutrina) e `_progressao` (observado). |
| `estruturas/<flow>/` | Referências concretas catalogadas (Medicube, Avelmore…). |
| `aprendizados/` | Princípios extraídos de observação; `_global/` vale para tudo. |

# Convenções

- Valores de frontmatter são slugs simples, não wikilinks: `consideracao`
  em `momento` = `componentes/eixos/momento/consideracao.md`. Todo valor
  tem nota; valor sem nota é bug (validar com `python .tools/valida.py`).
- Lista vazia (`momento: []`) significa "não discrimina", nunca "não serve
  a nenhum" — ver passo 5 do protocolo.
- `_catalogo.md` é gerado: rodar `python .tools/gera_catalogo.py` após
  qualquer mudança de frontmatter de variante, nunca editar à mão.
- `aprendizados` e `serve_estruturas` no frontmatter de variante são fios
  **comprovados**, preenchidos só quando a relação foi julgada (hoje 11 e
  1 de 44). Vazio significa "ainda não mapeado", não "não existe" — a
  camada de doutrina (intenções, estruturas, aprendizados) não referencia
  variantes; o fio canônico corre na direção intenção → estrutura → seção
  → variante, via protocolo.
- Cobertura atual de flows: só `welcome` tem intenções, estruturas e
  aprendizados. Os demais momentos existem como eixo, sem camada de
  intenção.
