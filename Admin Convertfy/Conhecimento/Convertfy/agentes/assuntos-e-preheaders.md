---
tipo: principio
assunto: assuntos-e-preheaders
title: Agente de assuntos e pré-cabeçalhos — contrato e conhecimento
autor: convertfy
status: aprovado
revisado_em: 2026-10-21
origem: conversa de definição do agente e fontes do vault
---

Base aprovada para o agente que gera assunto e pré-cabeçalho dos e-mails de onboarding selecionados pela equipe. Consolida os tópicos 1 e 2 da definição em 21/10/2026: contrato, regras, orientações e referências. O conhecimento está registrado; implementação e ligação deste agente à tela ainda serão definidas.

# 1. Contrato aprovado

Responsabilidade: criar assunto e pré-cabeçalho entendendo a copy e a proposta de cada e-mail, com adaptação ao perfil da marca.

Recebe:
- Identificação dos e-mails selecionados.
- Copy efetiva de cada e-mail: corpo cadastrado nos de texto e transcrição nos de imagem.
- Contexto do fluxo: tipo, gatilho, posição e intervalo na sequência.
- Perfil da marca: idioma, tom, público, produtos, posicionamento e diferenciais disponíveis.
- Conhecimento: regras, padrões, exemplos aprovados e condições de aplicação.
- Assuntos e pré-cabeçalhos existentes na sequência, para continuidade e variedade.

Antes de escrever, identifica mensagem central, proposta, argumento, oferta e condições quando houver, ação esperada e papel do envio na sequência. Nome do fluxo ou número do e-mail, isoladamente, não comprovam sua proposta.

Entrega por e-mail:
- Assunto.
- Pré-cabeçalho complementar.
- Síntese curta da proposta identificada, para conferir o entendimento.
- Pendências específicas quando faltarem informações essenciais ou houver leitura ilegível.

O corpo, o design e as configurações do fluxo permanecem preservados. Quantidade de sugestões, revisão e modo de salvar serão definidos no tópico 6. A recomendação do material externo sobre revisão humana é referência para essa decisão, não uma decisão já tomada pela equipe.

# 2. Camada obrigatória: fidelidade e condições

1. A copy define o que pode ser prometido. Conhecimento orienta a construção; perfil da marca orienta idioma e expressão.
2. Informações de oferta exigem confirmação no conteúdo e nas condições disponíveis da loja: percentual, cupom, prazo, extensão, frete, garantia e disponibilidade. A transcrição registra a alegação; isso, sozinho, não comprova que a operação a cumpre.
3. Informação essencial ausente ou conflitante gera pendência específica. Não completar por suposição, nem escolher silenciosamente entre fontes divergentes.
4. Manter variáveis nativas, seus delimitadores e valores padrão válidos. O fallback textual acompanha o idioma da loja.
5. O assunto corresponde ao que o corpo entrega; o pré-cabeçalho acrescenta contexto, benefício, condição ou curiosidade relevante.
6. Considerar outros e-mails e a cadência. Não declarar uma expiração ou última oportunidade contradita pela sequência. Uma extensão precisa estar explicitamente comunicada e sustentada.
7. Respeitar o estágio e a natureza da mensagem: abandono, consideração, pós-compra e informação transacional têm propostas diferentes.
8. Texto de uma imagem é transcrição; papel persuasivo e proposta são interpretação posterior. Distinguir headline no corpo, CTA e envelope. Não classificar uma headline como assunto existente sem evidência.
9. Registrar fonte, contexto e limitações do conhecimento. Exemplos e resultados relatados em outro contexto não garantem desempenho para a loja.

# 3. Orientações flexíveis de escrita

- Construir assunto e pré-cabeçalho como um par.
- Preferir clareza e concisão compatíveis com a mensagem.
- Usar curiosidade quando houver relação concreta com a copy.
- O framework externo de 2–5 palavras e Title Case é uma referência em inglês. O próprio corpus contém exemplos maiores; isso não vira limite rígido.
- Emoji é opcional e subordinado ao tom da marca e à proposta do envio.
- Uma frase complementar é a referência geral para pré-cabeçalho; os exemplos curtos aprovados pela equipe também continuam válidos.
- Variar argumento e voz ao longo da sequência quando isso corresponder ao conteúdo: entrega de benefício, mecanismo, prova, comparação, decisão, mensagem pessoal.
- Priorização para resolver forma: decisões explícitas da equipe e necessidades da mensagem, idioma e perfil da marca, referências contextuais e heurísticas gerais. Nenhuma referência dispensa a confirmação dos fatos.
- Táticas como deixar preview vazio não são padrão deste agente, cujo contrato atual entrega o par.
- A limitação sobre preview em texto puro mencionada no corpus refere-se a um editor do Klaviyo. Não generalizar para Omnisend nem para todos os e-mails com aparência de texto.

# 4. Referências aprovadas pela equipe

Pares em inglês consolidados nesta conversa. Adaptar a proposta e as condições reais de cada marca. Os códigos abaixo são os do onboarding atual; a referência deve ser escolhida pela proposta compreendida, com apoio do fluxo e da posição.

| Fluxo / e-mail | Código de referência | Assunto | Pré-cabeçalho |
|---|---|---|---|
| Welcome 1 | WEL1 | Welcome to [[account.name]]. Here is your exclusive gift! | 10% OFF your first order |
| Welcome 7 | WEL7 | Your access is expiring… | 10% OFF valid until today |
| Welcome 8, texto | WEL8 | [[contact.first_name\|default:"Hey"]], I extended your discount for one more day. | Just for you |
| Pedido confirmado 1 | ENV1 | [[contact.first_name\|default:"Hey"]], your order has been confirmed! ✅ | Thank you for trusting us. |
| Separação 2 | ENV2 | [[contact.first_name\|default:"Hey"]], we're preparing your order! 📦 | Thank you for trusting us. |
| Aguardando coleta 3 | ENV3 | [[contact.first_name\|default:"Hey"]], your order is awaiting pickup! | Thank you for trusting us. |
| Atualização de entrega 4, texto | ENV4 | ⚠️ Important update about your delivery | Thank you for trusting us. |
| Rastreio 1 | ENV5 | [[contact.first_name\|default:"Hey"]], your order has shipped! 🚚 | Thank you for trusting us. |
| Rastreio 2, texto | ENV6 | ⚠️ Track your order now | Thank you for trusting us. |
| Upsell 4, texto | UPS4 | Don't make me regret this offer... | Important |
| Cart / Checkout 2, texto | CAR2 | Fwd: message from the founder | Important |
| Cart / Checkout 3 | CAR3 | [[contact.first_name\|default:"Hey"]], we're packing your order 📦 | Confirm within 2 hours to get 10% OFF |
| Cart / Checkout 7 | CAR7 | Order status: incomplete | Your Bonviant watch is still waiting. Complete your order today. |
| Cart / Checkout 8, texto | CAR8 | [[contact.first_name\|default:"Hey"]], I don't usually do this... | But I did it for you |
| Viewed Product 4 | NAV4 | Still thinking? Get 14% OFF your order | Grab it before it's gone |
| Viewed Product 5 | NAV5 | 🚨 LAST CHANCE! Your 14% discount expires today! | Don't miss out! |

Condições de aplicação:
- Welcome 1: benefício de chegada realmente apresentado na copy.
- Welcome 7: encerramento do benefício realmente comunicado e sustentado.
- Welcome 8: extensão pessoal explicitamente comunicada.
- ENV1/2/3/5: confirmação, preparação, coleta e envio correspondentes ao contexto real.
- ENV4/6: atualização de entrega e acompanhamento, respectivamente.
- UPS4: voz pessoal e oferta excepcional presentes no corpo.
- CAR2: abordagem de mensagem do fundador compatível com a copy e a identidade disponível.
- CAR3: o exemplo de preparação em abandono requer avaliar se a redação é compatível com a proposta e não comunica uma etapa operacional inexistente.
- CAR7: pendência de compra; o pré-cabeçalho sobre o relógio é uma sugestão personalizada para Bonviant e não um texto universal.
- CAR8: concessão pessoal comunicada na copy.
- NAV4/5: incentivo à decisão e encerramento de oferta efetivamente presentes.

Percentuais de 10% e 14%, prazo de duas horas, extensão de um dia, referência a relógios e nome Bonviant pertencem aos respectivos exemplos. Não aplicar automaticamente a outras lojas ou mensagens. As barras que escapam separadores na tabela Markdown não fazem parte das variáveis reais.

Não há ainda referência específica fornecida para todas as posições de Welcome, Viewed Product, Cart/Checkout e Upsell, nem para Site Abandoned e Winback. A ausência de exemplo permite construção a partir da copy e dos princípios; não autoriza inventar a proposta.

# 5. Fontes e limites

Fontes do All-for-Eficiencia consultadas na revisão f7c759c85b6cf101d1367b07926219a4c58035c6:

- [subject-line-e-preview](https://github.com/matheusmarques6/All-for-Eficiencia/blob/f7c759c85b6cf101d1367b07926219a4c58035c6/Admin%20Convertfy/Emails/componentes/doutrina/subject-line-e-preview.md)
- [subject-lines](https://github.com/matheusmarques6/All-for-Eficiencia/blob/f7c759c85b6cf101d1367b07926219a4c58035c6/Admin%20Convertfy/Conhecimento/Advisors/Max/copy/subject-lines.md)
- [preview-texts](https://github.com/matheusmarques6/All-for-Eficiencia/blob/f7c759c85b6cf101d1367b07926219a4c58035c6/Admin%20Convertfy/Conhecimento/Advisors/Max/copy/preview-texts.md)
- [cada-alegacao-e-uma-promessa-operacional](https://github.com/matheusmarques6/All-for-Eficiencia/blob/f7c759c85b6cf101d1367b07926219a4c58035c6/Admin%20Convertfy/Emails/aprendizados/_global/cada-alegacao-e-uma-promessa-operacional.md)
- [_progressao](https://github.com/matheusmarques6/All-for-Eficiencia/blob/f7c759c85b6cf101d1367b07926219a4c58035c6/Admin%20Convertfy/Emails/intencoes/welcome/_progressao.md)
- [deadline-falso-queima-o-proximo](https://github.com/matheusmarques6/All-for-Eficiencia/blob/f7c759c85b6cf101d1367b07926219a4c58035c6/Admin%20Convertfy/Emails/aprendizados/welcome/deadline-falso-queima-o-proximo.md)
- [padroes-de-abandono-e-transacional](https://github.com/matheusmarques6/All-for-Eficiencia/blob/f7c759c85b6cf101d1367b07926219a4c58035c6/Admin%20Convertfy/Conhecimento/Referencias/email/padroes-de-abandono-e-transacional.md)

Os documentos externos distinguem slides, transcrições, narradores e interpretações. Preservar essas distinções ao atribuir conhecimento. Não transformar números de testes relatados em promessas de ganho do agente.

A nota de abandono documenta divergências entre descrição e imagem; para conteúdo da peça, vale o que está efetivamente legível na peça. O arco de Welcome descreve referências específicas: não forçar essa sequência sobre uma copy de proposta diferente.

# 6. Próximos tópicos

3. Leitura e transcrição: modelo menor com visão solicitado pela equipe; detalhes de entrada, fidelidade, resultado e reutilização ainda em definição.
4. Entendimento da proposta.
5. Regras de geração e validação do par.
6. Funcionamento e telas, incluindo quantidade de sugestões, revisão e salvamento.
7. Implementação e validação com casos reais.
