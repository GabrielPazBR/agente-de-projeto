# Gemini MCP com Antigravity

Ao instalar, atualizar ou reparar o Gemini MCP Tool, conclua este procedimento na mesma implantação. Fonte do MCP: [jamubc/gemini-mcp-tool](https://github.com/jamubc/gemini-mcp-tool). Confira a [documentação oficial do Antigravity](https://www.antigravity.google/docs/cli/headless/#select-a-model-effort-or-agent) e as capacidades do CLI instalado antes de aplicar flags.

## Diagnóstico e instalação recuperável

O diagnóstico fornecido pelo proprietário em 2026-10-22 encontrou `GEMINI_MCP_BACKEND=agy`, Antigravity 1.4.4 e `gemini-mcp-tool` 1.1.8: o adaptador descartava `model` e a ajuda chamava `gemini --help`. Foram relatados testes `SUCCESS` com `gemini-3.8-flash-low` e `gemini-3.8-flash-high`. Esses dados são referência histórica, não prova do ambiente de destino nem versões a fixar para sempre. Atualizar apenas pelo npm não comprova correção.

1. Descubra executáveis, versões, entrada MCP ativa, código do adaptador, `agy --help` e `agy models`. Preserve Antigravity como backend quando compatível com a conta; configure explicitamente `GEMINI_MCP_BACKEND=agy`. Não troque para Gemini CLI para contornar o defeito.
2. Inspecione se o upstream já atende ao contrato e aos testes abaixo. Se ainda houver falhas, prepare uma cópia local versionada do MCP em diretório persistente do usuário, fora do projeto atendido, do NIMBUS e do cache temporário do `npx`. Registre origem, versão, revisão, patch, lockfile, comando de build e entrada compilada absoluta. Preserve a instalação atual e a configuração anterior para rollback.
3. Corrija e teste essa cópia antes de apontar o cliente MCP para sua entrada compilada. Preserve nomes, argumentos existentes e comportamento compatível das ferramentas, incluindo `ask_gemini`, `brainstorm`, `Help` e continuação por chunks. Adições de argumentos opcionais e consulta de modelos são compatíveis; renomear ferramentas existentes não é.
4. Atualize apenas a entrada desse MCP, preservando outros servidores, configurações e permissões. Recarregue o cliente e confira handshake e schemas efetivamente expostos. Se a ativação falhar, restaure a entrada anterior e registre o componente como falho ou bloqueado. Uma restauração não equivale a aprovação da correção.

## Contrato do adaptador

- Encaminhe `model` explicitamente solicitado para `agy --model <slug>` por argumentos separados, removendo descarte e restrição fixa a Flash. Sem `model`, omita `--model` e preserve o padrão do CLI.
- Disponibilize consulta dos modelos acessíveis pela conta por `agy models`. Valide seleções explícitas contra a listagem atual, incluindo modelos personalizados reconhecidos pelo CLI. Rejeite modelo desconhecido sem substituição silenciosa. Falha de enumeração é falha de descoberta/autenticação, não prova de modelo inválido; registre-a e não invente uma lista.
- Exponha `effort` opcional nas ferramentas que consultam modelos, incluindo `ask_gemini` e `brainstorm`, e encaminhe para a flag aceita pelo CLI instalado, como `--effort`. Descubra os valores e a compatibilidade com o modelo em vez de fixar um enum antigo.
- Oriente os consumidores a preferir `effort: high` quando suportado. A escolha explícita do usuário prevalece. Se o modelo representar esforço no slug, prefira a variante `high` disponível somente ao escolher um modelo, sem substituir um slug explícito ou impor modelo quando omitido. Evite combinar slug e esforço incompatíveis. Se `high` não for suportado, informe a limitação; preserve o padrão quando não houver esforço explícito. Esforço explicitamente solicitado e inválido deve produzir erro, sem degradação silenciosa. O adaptador não injeta `high` quando o argumento é omitido.
- Faça `Help` executar a ajuda do backend selecionado: com `agy`, use `agy --help`, mesmo sem `gemini` no PATH. Atualize descrições, exemplos e schemas para seleção real de backend, modelo e esforço; remova a alegação de padrão fixo Gemini 2.5.
- Solicite saída estruturada suportada, como `--output-format json`, e interprete código de saída, `status`, `response`, `error`, stdout e stderr. Diferencie resposta válida, autenticação, quota, timeout, modelo/esforço inválido e erro de protocolo. Saída malformada ou vazia não é sucesso; retorno zero sozinho não basta. Erros MCP devem ser reconhecíveis como erros pelos consumidores.
- Em timeout, encerre o processo iniciado e descarte saída parcial. Separe resultados por chamada e não devolva resposta ou chunks antigos após falha. Não reutilize conversa anterior sem continuação explicitamente solicitada.
- Registre backend, modelo e esforço solicitados separadamente dos confirmados. Confirme o modelo somente com metadados ou consulta diagnóstica do CLI; texto gerado dizendo qual modelo é não serve como prova. Na ausência de evidência, registre `não confirmado`.
- Preserve as permissões existentes e não habilite aprovação automática. O parâmetro `sandbox` de `agy` não comprova isolamento; modo de impressão não é sandbox.

## Provas obrigatórias

Execute testes do adaptador com CLI simulado antes das consultas reais:

| Caso | Evidência esperada |
| --- | --- |
| Modelo e esforço explícitos em `ask_gemini` e `brainstorm` | Argumentos corretos, sem descarte ou restrição a Flash; solicitação inválida recusada |
| Modelo e esforço omitidos | Flags ausentes, padrão do CLI preservado |
| Modelo inexistente e falha de enumeração | Erros distintos, sem fallback silencioso |
| Ajuda com backend `agy` e sem executável Gemini | `Help` retorna a ajuda correta |
| JSON válido, malformado, erro, autenticação e quota | Classificação coerente com saída e status |
| Timeout e falha após chamada bem-sucedida | Processo encerrado; nenhuma resposta ou chunk anterior devolvido |
| Regressão | `ask_gemini`, `brainstorm` e continuação existente continuam compatíveis |

Depois do handshake, faça pelo MCP uma consulta real curta com cada um de dois modelos distintos enumerados pela conta. Use esforço `high` quando suportado. Os slugs históricos acima são exemplos, não requisitos de disponibilidade. Use diretório de prova sem arquivos do projeto, ferramentas desabilitadas por mecanismo suportado e sem alterar permissões globais; um prompt pedindo para não usar ferramentas não comprova sua desativação. Verifique a resposta atual, ausência de ferramentas e alterações, status e evidência do modelo selecionado. Não solicite análise ou edição do workspace. Sem dois modelos, autenticação ou mecanismo de prova sem ferramentas, registre a limitação e mantenha a validação parcial.

Registre no manifesto versões observadas, caminho/revisão do adaptador, backend, modelos disponíveis, esforço suportado/preferido, solicitações e confirmações, provas, pendências e comando de rollback. Conclua somente com testes e consultas reais aprovados; ping ou presença de configuração não basta.
