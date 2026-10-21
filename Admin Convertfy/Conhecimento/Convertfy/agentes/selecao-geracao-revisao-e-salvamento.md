---
tipo: principio
assunto: selecao-geracao-revisao-e-salvamento
title: Agente de assuntos — seleção, geração, revisão e salvamento
autor: convertfy
status: aprovado
revisado_em: 2026-10-21
origem: tópico 6 e prévia interativa aprovados na conversa; opção somente vazios solicitada pela equipe
---

Contrato de funcionamento nas telas do agente de assuntos e pré-cabeçalhos. Complementa [[assuntos-e-preheaders]], [[leitura-e-transcricao-dos-emails]], [[interpretacao-da-copy-e-da-proposta]] e [[geracao-e-validacao-dos-assuntos-e-preheaders]].

# 1. Entrada na tela atual

Manter o workspace de configurações do onboarding: navegação entre fluxos à esquerda, conteúdo e sequência no centro, conferência e aprovação à direita.

Adicionar “Criar com IA” ao cabeçalho de “Sequência e e-mails”. Abrir um modal com duas etapas: “Selecionar e-mails” e “Revisar e salvar”. Identificar a loja e o idioma da geração. Preservar o editor manual existente e o scroll da tela.

A prévia aprovada demonstra navegação e sugestões ilustrativas. Não comprova leitura de uma copy real, disponibilidade de ofertas nem geração ou salvamento em produção.

# 2. Selecionar e-mails

Mostrar código, nome, fluxo, assunto e pré-cabeçalho atuais, disponibilidade do conteúdo e campos que serão gerados.

Abrir no fluxo atual, com os e-mails incompletos pré-selecionados. Permitir ampliar a seleção para outros fluxos da mesma loja e escolher e-mails individualmente.

Disponibilizar duas ações distintas:
- “Selecionar incompletos”: selecionar e-mails com pelo menos um dos dois campos vazio.
- “Somente e-mails sem assunto e sem pré-cabeçalho”: selecionar exclusivamente os que têm os dois campos vazios. Esta ação substitui a seleção anterior no escopo mostrado; retira e-mails preenchidos ou parcialmente preenchidos. Espaços em branco contam como vazio.

A segunda opção é a forma de criar somente para os e-mails que ainda não têm nada. Não considerar corpo, imagem ou headline do design como assunto ou pré-cabeçalho já cadastrado.

Escopo das ações: fluxo atual ou todos os fluxos da loja, conforme o seletor. Ao trocar o escopo, mostrar o total selecionado e quantos ficam fora da lista visível, se houver. Não gerar para itens ocultos sem sinalização.

Deduplicar pela identidade do e-mail na loja. Um CAR compartilhado por carrinho e checkout aparece uma vez, com a indicação dos dois fluxos, e recebe uma única geração e gravação.

# 3. Preservar campos existentes

- Ambos vazios: gerar assunto e pré-cabeçalho.
- Só um vazio: preservar o preenchido e gerar o complemento levando o par em consideração.
- Ambos preenchidos: não selecionar automaticamente.
- Recriação de campos preenchidos: exigir a escolha explícita “Recriar os dois campos” naquele e-mail.

A ação “Somente e-mails sem assunto e sem pré-cabeçalho” não ativa recriação. Um e-mail sem conteúdo utilizável não pode ser gerado; mostrar o motivo e o que falta corrigir.

# 4. Geração e progresso

Gerar uma sugestão de par por e-mail selecionado. Usar o conteúdo efetivo, a interpretação, o perfil da marca, o contexto da sequência e o conhecimento aprovado.

Exibir progresso por e-mail: leitura da copy, interpretação da proposta, geração, validação e resultado. Distinguir sucesso, pendência e falha técnica. Falha de um item não impede a revisão dos demais. Repetir apenas os itens solicitados, sem refazer os já concluídos.

Reutilizar a leitura enquanto o conteúdo não mudar. Regenerar redação não implica retranscrever a mesma imagem.

# 5. Revisão

Manter a lista de e-mails e seus estados ao lado do detalhe do item ativo. Exibir:
- Proposta entendida, em poucas palavras.
- Assunto e pré-cabeçalho atuais e sugeridos.
- Campos sugeridos editáveis e contagem de caracteres.
- Situação da validação, observações e motivo específico de pendência.
- Acesso à copy usada e, quando disponível, ao conteúdo original.

Permitir incluir ou retirar um e-mail do salvamento, editar os campos gerados e gerar outra versão apenas daquele item. Descartar uma sugestão não altera o texto já salvo.

A confirmação de salvamento é sempre humana. Campos bloqueados para preservação não se tornam editáveis ou substituíveis sem escolha explícita de recriação.

Depois de uma edição manual, sinalizar “Confirmar edição”; repetir as verificações determinísticas e não apresentar a redação alterada como validada pela IA anterior. A confirmação humana não libera placeholders, variáveis inválidas, limites excedidos ou pendências essenciais não resolvidas.

O histórico de navegação dentro do modal não apaga a seleção nem as edições não salvas. Sair ou voltar para uma ação que descarte sugestões exige aviso de alterações não salvas.

# 6. Pendências e erros

Uma pendência essencial, como oferta ilegível ou prazo conflitante, fica identificada e fora do salvamento. Informar o motivo e permitir corrigir a fonte e tentar novamente.

E-mails prontos continuam disponíveis para revisão e salvamento. Falhas técnicas podem ser repetidas individualmente e não devem aparecer como pendência de conteúdo.

Os avisos da conferência do fluxo continuam sendo calculados pelas regras existentes. Gerar ou salvar um assunto não aprova automaticamente o fluxo nem resolve um marcador pendente no corpo.

# 7. Salvamento

O botão informa a quantidade efetivamente gravável, por exemplo “Salvar 6 e-mails”. Considerar apenas itens incluídos, completos, confirmados quando editados e sem bloqueio.

Salvar no cadastro da loja, nas mesmas informações consumidas pelo editor e pela montagem. Não salvar apenas em um estado visual nem publicar diretamente na Omnisend.

Preservar corpo, design, configurações e campos preexistentes protegidos. Ao confirmar, comparar com a versão usada na geração: se outra pessoa alterou o mesmo e-mail ou o conteúdo de origem mudou, mostrar conflito e pedir revisão do item atualizado, sem sobrescrever silenciosamente.

Cada e-mail pode ser salvo com resultado independente. Em falha parcial, mostrar quais foram salvos e quais falharam; manter as sugestões não salvas e repetir somente as falhas. E-mail compartilhado é gravado uma vez.

Depois de salvar, atualizar a sequência, o editor e as conferências afetadas. Não reapresentar como pendentes sugestões já salvas.

# 8. Critérios de aceite da experiência

- O botão abre o modal dentro do onboarding existente.
- Há geração no idioma da marca e indicação desse idioma.
- Seleção individual, incompletos e somente ambos vazios têm comportamento distinto e previsível.
- A opção somente vazios exclui e-mails com qualquer um dos dois campos preenchido.
- Recriação de campos preenchidos depende de escolha explícita.
- Compartilhados contam e salvam uma vez.
- Uma sugestão por item, com proposta entendida e acesso à copy.
- Pendência essencial não pode ser salva; os demais itens continuam funcionando.
- Edição manual exige nova confirmação e as validações obrigatórias.
- Fechar não perde alterações sem aviso.
- Conflitos e falhas parciais não apagam trabalho.
- Sequência e conferências refletem o que foi efetivamente salvo.
- Modal e conteúdo têm rolagem acessível em zoom normal e em telas menores.

# Próximo tópico

O tópico 7 definirá o plano de implementação: reutilização do projeto, contratos, persistência, chamadas aos modelos, testes e validação com e-mails reais. A aprovação desta experiência não significa que o agente já está implementado.
