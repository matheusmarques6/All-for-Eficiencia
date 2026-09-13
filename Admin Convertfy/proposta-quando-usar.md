# Proposta — seções "Quando usar" e campo `exige_da_loja`

> **Não está em `Emails/`** de propósito: é rascunho, não deve ser ingerido pelo
> sync. Aprovando, eu movo o conteúdo para as notas; reescrevendo, eu aplico a
> sua versão.

Duas lacunas do lote P4/P6, ambas texto novo derivado por inferência — por isso
não gravei direto. O que já era transporte de texto existente (`objecao_alvo`,
`mecanismo`) já está aplicado nas 8 estruturas.

---

## Parte 1 — "Quando usar" nas 5 que só têm "Quando NÃO usar"

### `avelmore-mecanismo-e-origem` (#3)

**Usar quando:** toque intermediário, depois que tese (#1) e varredura (#2) já
foram gastas; a loja tem **origem real** e um **mecanismo descritível** — o que
faz o produto ser o que é, em três parágrafos; existe **economia explicável** (por
que o preço é esse e não outro); a objeção dominante é ceticismo de sustentação
("como isso se sustenta?") e não desconfiança do canal; existe **prova física
fotografável** (fachada, oficina, bancada) num flow que até ali só mostrou
produto.

*Complemento ao "Quando não usar", que hoje está como "não determinado":* não usar
quando a loja não tem história própria (marca-etiqueta, dropshipping) — mecanismo
inventado é a alegação mais cara do flow, e cada alegação é promessa operacional.

### `avelmore-prova-social-cirurgica` (#4)

**Usar quando:** a marca já fez três alegações próprias seguidas e precisa sair da
frente; existem **≥2 depoimentos reais com nome que fecham objeções DIFERENTES**,
um deles espelhando literalmente o cético ("eu desconfiava de comprar de uma marca
que não conhecia"); há **agregado numérico verificável**; existe bloco reusável de
um toque anterior para servir de âncora de familiaridade.

*Complemento ao "não determinado":* não usar com depoimento genérico de elogio, nem
com um só — o dispositivo é a **curadoria por objeção**, não a presença de prova.
Um depoimento que não fecha objeção nomeada é enchimento.

### `medicube-escassez-com-prova-de-demanda` (#6)

**Usar quando:** e-mail que **encerra o ciclo da oferta** (regra transversal 3 do
`_flow`: hora fechada existe uma vez); existe **prazo real com hora que será
honrado no ESP**; existem **números de uso auditáveis** (quantos usaram, quantos
restam) — ver [[numeros-de-escassez-precisam-de-backing]]; existem depoimentos que
fechem objeções do canal, para colar na pressão.

### `medicube-ultima-batida` (#7)

**Usar quando:** mesmo dia do toque de fechamento, **intervalo medido em horas**;
o prazo já foi anunciado e **não muda** (repetir a mesma hora, nunca renovar); não
há nenhum argumento novo a dar — se ainda houver, o registro certo é outro.

### `carta-plain-text-extensao` (#8)

**Usar quando:** toque de encerramento, **depois de o prazo ter vencido de fato**;
o flow acumulou toques desenhados suficientes para existir cegueira a atravessar
(o valor do formato pelado cresce com esse número); a extensão cabe nas **quatro
condições** de [[extensao-declarada-quatro-condicoes]]; existe caixa monitorada —
o convite a responder é parte do mecanismo, não enfeite.

---

## Parte 2 — `exige_da_loja` nas 6 que não declaram

Proposta de valor para o frontmatter, no formato validável pelo guard de
construtibilidade. As duas que já declaram em prosa (`avelmore-deadline-objecao`,
`avelmore-inspecao-antecipada`) só precisam de transporte.

| Estrutura | `exige_da_loja` proposto |
|---|---|
| `avelmore-mecanismo-e-origem` (#3) | história de origem real · mecanismo descritível · justificativa de preço · prova física fotografável · grade ≥4 produtos |
| `avelmore-prova-social-cirurgica` (#4) | ≥2 depoimentos com nome fechando objeções distintas · agregado numérico verificável · garantias já apresentadas em toque anterior |
| `medicube-comparacao-categoria` (#5) | ≥4 diferenciais reais do canal · ≥6 medos reais da categoria · incentivo ativo · grade ≥4 produtos |
| `medicube-escassez-com-prova-de-demanda` (#6) | prazo real com hora honrável no ESP · números de uso auditáveis · ≥3 depoimentos de objeção de canal · garantias à vista |
| `medicube-ultima-batida` (#7) | prazo já anunciado no mesmo dia · incentivo ativo até a hora declarada |
| `carta-plain-text-extensao` (#8) | capacidade de estender o prazo uma vez · caixa monitorada para respostas · nenhuma extensão prévia neste flow |

**Nota de implementação:** vários desses pré-requisitos não são campos de
`client_stores` — "prazo honrável no ESP", "números auditáveis", "caixa
monitorada" são fatos operacionais que hoje ninguém registra. O guard só consegue
checar o que existe em banco. Sugestão: o campo entra como **declaração legível**
(o agente lê e decide) antes de virar validação em código — e o que for
promovido a validação depois é só o subconjunto que tem coluna.
