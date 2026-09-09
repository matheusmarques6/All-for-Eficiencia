---
tipo: indice
assunto: cobertura-e-lacunas
autor: max-sturtevant
status: aprovado
---

Mapa de quanta matéria o corpus Max tem sobre cada assunto: as dez pastas
modulares, quantas notas cada uma reúne, quantas palavras de fala e de slide a
sustentam, e a densidade resultante. Densidade baixa não significa "não
responda" — significa que a chance de a resposta exigir algo que não está lá é
alta, e que a cobertura precisa ser verificada antes de formular. Índice em
[[mapa-da-cobertura]].

# Mapa de densidade por assunto

**Como a densidade foi medida.** Por palavras, não por linhas — as linhas do
bruto variam de 3 a 300 palavras e a contagem de linha mente. Total do arquivo:
121.344 palavras ([[_fontes]]).

| Assunto | Pasta | Notas | Registro disponível | Densidade | Observação |
|---|---|---|---|---|---|
| Pilares, métricas-núcleo, glossário, escolha de ESP, estado do mercado | [[mapa-dos-fundamentos]] | 10 | ambos — 7.675 pal. fala + 2.490 slide | **média** | O glossário inteiro é slide **que ele declara não ter lido** (L217, L227). Três alvos existem só ali e não têm confirmação em lugar nenhum: bounce `<2%` (L437), list cleaning `60–90+ days` (L443), largura `600–700px` (L469). |
| Princípios transversais e processo de criação | [[mapa-da-doutrina]] | 13 | ambos, faixa de todos os módulos | **média** | Pasta derivada, não modular. **8 das 13 notas saem de faixa não-Max** — é a pasta mais exposta ao problema de autoria, porque doutrina é justamente o que o advisor parafraseia na voz dele. |
| Pop-up, oferta, tipos de form, captação | [[mapa-de-list-growth]] | 11 | ambos — 16.339 pal. fala + 1.486 slide | **alta** | Único módulo com **dois** walkthroughs de tela completos (Klaviyo mobile e desktop). Contrapeso: o deck tem duas seções de tutorial vazias, "Klaviyo Pop-Up Form Creation" (L1300) e "Alia Pop-Up Form Creation" com o placeholder `[need]` (L1302-1304). |
| Os 8 flows | [[mapa-dos-flows]] | 12 | ambos — 12.041 pal. fala + 4.921 slide | **alta para 7 flows · nula para o 8º** | Maior deck do corpus. **Filtro e saída existem em três flows e faltam em cinco** (ver cobertura parcial), e cart/checkout abandon não tem delay. O Sunset não tem aula. |
| Frequência, calendário, pilares de conteúdo, segmentação | [[mapa-das-campanhas]] | 9 | ambos — 13.319 pal. fala + 3.859 slide | **média-alta** | **A fala inteira do módulo (L4189-5154) é `outro-provavel`.** O que sobra de Max escrito é o deck. Um loop de ASR come o racional de testimonials (L4480-4488). |
| S.C.E., subject line, preview text, infográficos, prompt de IA | [[mapa-de-copy]] | 9 | ambos — 26.050 pal. fala + 2.111 slide | **enganosa: alta em palavra, média em doutrina** | 20.275 das 26.050 palavras são **dois teardowns de YouTube** (Gymshark, MrBeast) sobre emails de marcas específicas — narração, não doutrina. As aulas próprias somam 5.775 palavras. Agravante: o vídeo dos princípios de copy **não foi transcrito** (L5615, o único marcador de transcrição vazio do arquivo), e 30 rótulos de exemplo vieram sem imagem. |
| 3 princípios, doutrina por seção, transições, upload | [[mapa-de-design]] | 13 | ambos — 11.422 pal. fala + 1.976 slide | **alta em doutrina · baixa em exemplo** | A doutrina está completa e é dupla-registrada. Nenhum dos 13 exemplos visuais do deck sobreviveu (L8173-8300). A seção de transições promete métodos e não lista nenhum **no deck** (L8302-8307) — **os quatro métodos estão na fala** (L7550-7588). Não é lacuna, é lacuna do slide. |
| Setup técnico, warming, reparo, auditoria | [[mapa-de-deliverability]] | 9 | ambos — 6.818 pal. fala + 852 slide | **baixa** | Segundo menor módulo. **Toda a fala é `outro-provavel`** e o deck tem 113 linhas. É o único módulo com perda de áudio mensurável: dois cortes, 41s e 29s. Recusa provável. |
| Testes A/B | [[mapa-de-otimizacao]] | 7 | ambos — 3.123 pal. fala + 825 slide | **baixa** | **O menor módulo do corpus.** O deck é cópia quase verbatim do deck de flows (L4141-4176 ≡ L9151-9180) — não conta como confirmação cruzada. Fala inteira `outro-provavel`. Dos treze testes listados, **três têm vencedor declarado** — time delay de abandono (4h vence 30min, "10 to 15% higher placed order rate", ~$1.000 a mais, L8952-8962), send time (11h-12h, L9148) e gráfico vs texto ("text base sale winner", sem número, L8866). Os outros dez são só hipótese. |
| Doutrina de SMS, 5 flows, calendário, horários | [[mapa-de-sms]] | 8 | ambos — 3.851 pal. fala + 2.184 slide | **baixa** | **Módulo invertido: o slide carrega mais que a fala.** A fala é um único vídeo de YouTube de ~16 min. Nenhum flow de SMS tem metric, trigger, filtro ou exclusão. Recusa provável, e é o módulo com o pior problema de compliance (ver §4). |

**Total: 101 notas de conteúdo** em dez pastas, mais dez `_index.md` e as seis
notas de controle.

**Leitura operacional da coluna densidade.** Baixa não significa "não responda";
significa "a chance de a resposta exigir algo que não está lá é alta —
verifique a cobertura antes de formular". Os três módulos de densidade baixa
(deliverability, otimização, SMS) somam **17.653 palavras**, 14,5% do corpus,
e concentram desproporcionalmente as lacunas dos tipos abaixo.

---
