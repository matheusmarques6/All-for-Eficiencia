---
tipo: lacuna
sobre: conteudo
descoberta_em: 2026-08-31
status: aberta
---

# O que falta

[[hero-8-lineup-com-lembrete-de-oferta]] e [[hero-10-lineup-de-colecao]] são
um segundo par de conteúdo praticamente idêntico no banco — o mesmo padrão
já registrado em [[reviews-3-duplicado]], desta vez na seção `hero`. As
sete seções de prosa, os eixos (`momento`, `objecao`, `registro`, `paleta`,
`papel_na_peca`), `exige`, `product_slots` e `convivencia` são o mesmo
texto (a formatação markdown diverge levemente — negrito em `hero-10`,
ausente em `hero-8` — mas o conteúdo é idêntico). `variant_id` distintos
(`43f9b0ec-...` vs. `dc6c363c-...`), ambas `ativa: true`. Diferem em
`schema_campos` (7 em `hero-8`, 4 em `hero-10`) e `peso.altura_px` (1151 vs.
883) — únicos dois campos onde as notas não coincidem.

# Por que importa

O mesmo mecanismo de `reviews-3-duplicado` se repete: uma peça duplicada
dobra a chance estatística de ser sorteada frente às outras oito variantes
de `hero`, sem que nenhum critério de ranking tenha decidido que ela deve
pesar o dobro. A lacuna 4 do plano original (`reviews-3-duplicado`) cobria
só um par de duplicatas — a execução encontrou um segundo, confirmando que
não é caso isolado no banco.

# O que se perde hoje

Entre as nove variantes de `hero`, `hero-8` e `hero-10` juntas ocupam duas
vagas com uma peça só, distorcendo a distribuição de escolha das outras
sete. A divergência de `schema_campos` (7 vs. 4) é mais preocupante que a
de `reviews-3`: se as duas são a mesma peça, uma delas está com o schema de
copy incompleto ou incorreto — e não há como saber qual das duas é a
versão certa só olhando o vault.

# Mitigação no protocolo

A escolha entre as duas deixou de ser sorteio: o "desempate final" de
[[_protocolo-de-selecao]] manda usar a menos usada no histórico de envios
(fallback: menor número no slug — hero-8). Isso neutraliza a distorção
estatística descrita acima, mas não resolve a duplicata em si.

# Fora do escopo desta entrega

Decidir qual `variant_id` sobrevive, reconciliar `schema_campos` entre as
duas e desativar/remover a redundante no banco — mexe em dado vivo de
produção. Ver também [[tags-do-banco-contradizem-a-prosa]], que documenta
uma segunda divergência entre este par que reforça a suspeita de cadastro
inconsistente.
