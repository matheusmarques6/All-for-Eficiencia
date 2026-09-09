---
tipo: julgamento
status: aprovada
---

Como a casa decide um e-mail antes de o [[_protocolo-de-selecao]] rodar: o que nunca entra, o que se pergunta à loja antes de escolher, quem vence quando as fontes discordam e quando a resposta certa é recusar.

# O que nunca fazemos

- Segurar o incentivo prometido ou entregá-lo com condição nova — entra inteiro no toque 1 ([[_flow]] regra 1; [[welcome-1]]).
- Aumentar, sinalizar melhora ou mexer no incentivo em qualquer toque — insistir não pode pagar ([[_flow]] regra 2; [[welcome-2]], [[welcome-3]], [[welcome-4]], [[welcome-6]], [[welcome-7]]).
- Código, valor ou prazo só dentro de imagem — existem em texto real, ou o bloco é descartado ([[incentivo-precisa-existir-em-texto]]).
- Inventar incentivo, depoimento, prazo, selo ou número de escassez — alegação sem lastro operacional é removida, não suavizada ([[cada-alegacao-e-uma-promessa-operacional]]; [[welcome-5]], [[welcome-6]]; [[numeros-de-escassez-precisam-de-backing]]; [[prazo-real]], [[selo-compra-verificada]]).
- Prazo com hora fora do fechamento do ciclo, ou urgência antes do toque que a pede — hora fechada existe uma vez, no toque 6, e o 7 só a repete no mesmo dia; antes, no máximo "por tempo limitado" ([[_flow]] regra 3; [[welcome-1]], [[welcome-2]], [[welcome-3]]; [[cadencia-decide-fechamento-ou-farsa]]).
- Prazo que o toque seguinte não vá honrar, ou fingir que não venceu — a credibilidade do prazo se decide no e-mail seguinte ([[_flow]] regra 4; [[welcome-6]], [[welcome-8]]; [[deadline-falso-queima-o-proximo]]).
- Estender duas vezes, estender sem admitir que venceu, ou deixar o flow virar campanha permanente — a extensão é explícita, justificada, única e final ([[_flow]] regras 5 e 6; [[welcome-8]]; [[extensao-declarada-quatro-condicoes]]).
- Segunda objeção no toque de uma só — o 1 e o 3 atacam uma, bem; quem varre é o 2 (objeções) e o 5 (medos do canal) (`n_objecoes` em [[welcome-1]], [[welcome-3]]).
- Repetir o argumento ou o registro do toque anterior — cada toque assume que o anterior falhou e a voz rotaciona ([[_flow]]; [[welcome-2]], [[welcome-4]], [[welcome-5]], [[welcome-7]]).
- Gastar prova social antes do toque que a pede — no 1 é uma voz secundária, no 2 é vetada, no 4 é o texto inteiro; o depoimento que espelha o cético vai onde o cético domina ([[welcome-2]], [[welcome-4]]; [[ausencia-de-prova-social-assume-abertura]]).
- Bloco defensivo (comparação, FAQ) antes de a dúvida existir — cedo, cria a dúvida que queria curar ([[posicao-muda-o-efeito-do-dispositivo]]; [[welcome-5]]).
- Nomear concorrente ou usar superlativo vazio — comparar contra a categoria, com compromissos contra medos nomeados ([[welcome-5]]).
- Argumento, prova, catálogo ou história nos toques de fechamento ([[welcome-6]], [[welcome-7]], [[welcome-8]]).
- Mais de um CTA dominante, ou um segundo pedido (rede social, preferências) — um pedido, o principal ([[um-cta-dominante-em-email-curto]]; [[welcome-1]]).

# O que perguntamos antes de decidir

O passo 4 do protocolo em perguntas de sim/não. Só 3 das 52 têm campo na loja; as outras são respondidas pela pesquisa da loja ou pelo humano — e a resposta é declarada, nunca presumida. A lista completa, uma pergunta por requisito, está em [[_parametros-da-loja]] (Parte 2).

- **Comercial.** Tem cupom ativo e válido para publicar? ([[cupom-ativo]] — 9 variantes dependem dele: hero-3/4/5/6, offer-3/4/5/6, reviews-7; sem a resposta, o welcome-1 fica com zero heroes, não com a "menos ruim": [[exige-cupom-sem-perfil-de-ativos]].) O desconto é automático, sem código? ([[desconto-automatico-sem-cupom]] — não convive com cupom.) A oferta tem data real de expiração? ([[prazo-real]].) É percentual puro, exibível como número? ([[desconto-percentual]].)
- **Dado operacional.** Tem produtos cadastrados no número que a variante pede (`product_slots`, `itens`), cada um com página própria para o CTA apontar? ([[produtos-com-pagina-propria]] — produto sem link não sustenta slot.) Estoque por SKU vem de API? ([[estoque-integrado]].)
- **Catálogo e argumento.** Tem três diferenciais concretos, em eixos distintos? ([[tres-diferenciais-concretos]].) Manifesto escrito e aprovado? ([[manifesto-de-marca-escrito]] — tem campo.) Há motivo sazonal real, agora? ([[motivo-sazonal]].) Política de troca ou devolução publicada, para a remoção de risco citar? (`remocao_de_risco` em [[welcome-1]]; [[cada-alegacao-e-uma-promessa-operacional]].)
- **Prova social.** Tem avaliação real, com nome e produto? Com credencial e foto da pessoa? ([[depoimento-com-credencial]], [[foto-do-depoente]].) Curtas ou longas — nunca as duas na mesma peça? ([[reviews-curtos]], [[reviews-longos]].) Selo de compra verificada real, não decorativo? ([[selo-compra-verificada]].) UGC com autorização? ([[ugc-autorizado]].)
- **Ativo visual.** Foto de estúdio em fundo claro, com terço superior liso? ([[foto-estudio-fundo-claro]], [[terco-superior-liso]] — hero-3/7/8/10.) Foto com pessoas? De campanha própria, não banco? Monocromática? ([[foto-com-pessoas]], [[foto-de-campanha-propria]], [[foto-monocromatica]].) Cor de acento além de preto/branco/cinza? ([[cor-de-acento-definida]] — tem campo.)

**Sem a resposta, o bloco que exige o ativo não é "pior" — é impossível, e o slot fica declarado.**

# Quem vence quando as fontes discordam

| Vence | O que é neste vault | Peso |
|---|---|---|
| Pesquisa da loja com evidência | o que a loja provou ter: perfil de marca, pesquisa dos cinco pilares, catálogo com link, respostas às perguntas acima ([[_parametros-da-loja]], Parte 1) | vence tudo; alvo que pede o que a loja não tem não é atendido — é declarado |
| Alvo do Seletor | a objeção, o risco e o aliviador fixados a partir do contrato do toque (`modo`, `riscos_elegiveis`, `aliviadores_admissiveis`, `proibicoes` em `intencoes/<flow>/<n>`) | vence estrutura e aprendizado: eles servem ao alvo, não o substituem |
| Aprendizado com origem | nota de `aprendizados/` com `origem_estrutura:` — observação de peça real promovida a regra | `tipo_regra: restricao-dura` elimina; o resto rankeia |
| Estrutura de referência | `estruturas/<flow>/` — peça real catalogada | mostra o que existe, não prova o que funciona; resolve ordem e papel das seções |
| Doutrina de curso | as pontes de `componentes/doutrina/` — regra do curso traduzida para seções, eixos e `papel_na_peca` | ensina o critério; é opinião, não medição |
| Preferência do modelo | o que o agente acharia bonito | não decide nada: empate vai para o desempate do protocolo, nunca para o gosto |

**Escolha a de cima e diga qual perdeu** — nunca resolver em silêncio.

# Quando recusar

Posição sem variante que sirva ao alvo não é "escolher a menos ruim". Overlap zero na objeção não é segunda opção, e ativo ausente não é desconto no ranking — os dois são lacuna. A recusa tem três partes: declarar o slot vazio, deixá-lo para o template global e registrar a lacuna em `componentes/lacunas/` com `status: aberta` ([[_protocolo-de-selecao]], "Quando nenhuma variante sobrevive").

A recusa bem feita diz qual posição, qual alvo, qual variante chegou mais perto e em que passo ela caiu. O modelo é [[welcome-5-sem-variante-ativa]]: body-5 é a única que serve `confianca-no-canal`, está inativa, e o resultado é zero elegíveis — não body-4 (Caso B de [[_casos-de-teste]]). O erro que esta seção proíbe está medido em [[reputacao-da-loja-sem-bloco-ativo]]: o alvo pediu `reputacao_da_loja` em 4 de 4 runs e a posição foi preenchida por um bloco que não o realiza. Zero-elegíveis recorrente é o sinal mais valioso que o sistema produz: diz exatamente o que falta comprar ou construir.
