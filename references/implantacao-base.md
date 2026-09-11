# Implantação da base

Instale somente o que estiver ausente ou comprovadamente inválido. Consulte a documentação oficial atual de cada fonte quando os comandos ou requisitos tiverem mudado.

## Registro

Crie `.agent/manifest.yaml` a partir de `assets/manifest-template.yaml` e atualize-o ao término de cada componente. Registre origem, versão, escopo, configuração, teste e resultado.

## 1. RTK

Fonte: `https://github.com/rtk-ai/rtk`.

1. Execute `rtk --version` e `rtk gain`.
2. Confirme que o executável é o RTK da `rtk-ai`, evitando o pacote homônimo Rust Type Kit.
3. Se estiver ausente, use o método oficial compatível com o sistema. No Windows, instale o binário oficial em um caminho persistente incluído no `PATH`.
4. Habilite o RTK para o agente atual com o modo indicado pela versão instalada, como `rtk init -g --codex`, `--gemini` ou `--agent <nome>`.
5. Execute `rtk init --show` quando suportado, um comando real por meio do RTK e novamente `rtk gain`.
6. Registre como obter a saída integral quando a compactação ocultar dados necessários.

O componente termina quando binário, integração e execução real forem comprovados.

## 2. MemPalace local

Fonte: `https://github.com/MemPalace/mempalace`.

1. Se a skill `mempalace` estiver disponível, leia-a integralmente.
2. Antes de cada operação, execute `mempalace instructions <operação>` e siga a saída atual. Use pelo menos `init`, `mine` e `status` nesta implantação.
3. Quando a CLI estiver ausente ou inválida, prefira instalação isolada com `uv tool install mempalace`. Se não houver um gerenciador isolado compatível, instale e verifique o `uv` pela origem oficial; use outro método oficial isolado somente quando isso não for possível.
4. Inicialize um palace exclusivo do projeto e configure sua persistência sob `<workspace>/.agent/memory/`. Não reutilize o palace de outro projeto.
5. Para conteúdo em português, escolha um modelo de embeddings multilíngue oferecido pela versão instalada.
6. Faça uma prova de persistência: grave um item identificável, reinicie o processo, recupere o item e remova ou invalide a prova.
7. Obtenha `mempalace instructions mine` e execute uma mineração inicial idempotente do workspace.
8. Quando a versão instalada oferecer hooks ou mineração periódica, configure o modo escopado a este workspace, sem duplicar hooks existentes, e verifique uma execução. Se não houver suporte compatível, registre a limitação e mantenha a mineração no encerramento das tarefas.
9. Registre origem, modo, categorias, contagem fornecida, avisos e itens ignorados. Quando a CLI não informar contagem, declare a limitação.

Configure o agente para consultar a memória antes de decisões dependentes de histórico e registrar fatos, decisões, hipóteses, correções e pendências ao encerrar tarefas.

## 3. Graphify

Fonte: `https://github.com/Graphify-Labs/graphify`.

1. Execute `graphify --version` e confirme que o executável pertence ao pacote oficial `graphifyy` (com dois `y`). Não confunda o nome do pacote com o comando `graphify` nem instale pacotes homônimos.
2. Se estiver ausente ou inválido, prefira `uv tool install graphifyy`. Reuse `pipx` apenas quando já for o gerenciador isolado adotado no ambiente. Garanta que o diretório de binários esteja no `PATH` persistente do agente.
3. No diretório raiz do workspace, registre a integração no escopo do projeto com `graphify install --project --platform codex`. Confirme a criação de `.agents/skills/graphify/SKILL.md` e dos recursos referenciados por ela. Preserve uma instalação de projeto válida e não crie cópia global duplicada.
4. Leia a skill Graphify instalada antes de construir o grafo. Execute `$graphify .` pelo agente para indexar o workspace. Para um repositório que contenha somente código, ou quando não houver backend autorizado para documentos e mídia, use a extração local de código indicada pela versão instalada, como `graphify extract . --code-only`.
5. Confirme a existência e a leitura de `graphify-out/graph.json`. Execute ao menos uma consulta pertinente ao workspace com `graphify query`, `graphify explain` ou `graphify path` e confira se a resposta cita símbolos e caminhos reais do projeto.
6. Registre no manifesto a origem, a versão, o método de instalação, o caminho da skill, o caminho do grafo, o modo de extração e a consulta usada como prova.

Não marque este componente como aprovado somente porque o executável, a skill ou `graph.json` existe. Instalação, registro no Codex, indexação e consulta devem funcionar no workspace.

## 4. Context7

Fonte: `https://github.com/upstash/context7`.

1. Reuse uma instalação válida.
2. Garanta Node.js compatível com a versão atual do Context7.
3. Configure o Context7 MCP para o cliente de agente utilizado. Não mantenha CLI e MCP duplicados quando cumprirem a mesma função, salvo necessidade demonstrada.
4. Execute uma consulta real sobre uma biblioteca e versão presentes no projeto. Se o projeto ainda não tiver dependências, resolva e consulte uma biblioteca conhecida apenas como prova de diagnóstico e registre que ela não representa uma escolha do projeto.
5. Registre o ID resolvido, a versão consultada e o resultado.

## 5. Playwright MCP

Fonte: `https://github.com/microsoft/playwright-mcp`.

1. Reuse Node.js e o gerenciador existentes.
2. Instale ou configure `@playwright/mcp` conforme o cliente atual.
3. Instale o navegador exigido, incluindo Chromium quando não houver outra escolha do projeto.
4. Use perfil isolado por padrão e mantenha o acesso a arquivos restrito ao workspace.
5. Inicie o MCP, confirme o handshake, liste ferramentas, abra uma página neutra ou local e leia sua estrutura.
6. Encerre navegadores e processos iniciados pelo teste.

## 6. Gemini MCP Tool

Fonte: `https://github.com/jamubc/gemini-mcp-tool`.

1. Verifique a documentação atual e detecte os backends disponíveis, incluindo Gemini CLI e `agy`.
2. Instale o servidor e os requisitos oficiais que estiverem ausentes.
3. Selecione explicitamente o backend compatível com a conta e o ambiente.
4. Execute uma solicitação curta, confirme a resposta e registre backend e versão.
5. Trate o resultado como apoio exploratório. O parâmetro `sandbox` do backend `agy` não comprova isolamento.

Quando autenticação for necessária, conclua primeiro todas as etapas independentes e então solicite a ação do usuário.

## 7. Catálogos de skills

Fontes:

- `https://github.com/mattpocock/skills`
- `https://github.com/joshuadavidthomas/agent-skills`

1. Se `instalar-skill` estiver disponível, leia-a e aplique suas regras.
2. Inspecione cada origem e compare com as skills locais antes de importar.
3. Não instale simultaneamente uma versão gerenciada por plugin e outra cópia local da mesma skill.
4. Importe as skills compatíveis, registrando as incompatíveis, duplicadas ou omitidas.
5. Traduza para pt-BR descrições, títulos, subtítulos, legendas e instruções textuais. Preserve comandos, código, caminhos, parâmetros, URLs, schemas e identificadores técnicos.
6. Registre cada skill em `.agent/skill-sources.lock.yaml`, usando `assets/skill-sources-template.yaml`, com repositório, caminho de origem, commit ou versão, data, idioma, estado da tradução e hash.
7. Valide frontmatter, referências, scripts e descoberta pelo agente.

As skills podem ser instaladas no catálogo, mas o perfil funcional deve destacar somente as capacidades pertinentes ao projeto.

## Critério de conclusão

A base termina quando todos os sete componentes tiverem uma operação real aprovada ou um bloqueio registrado. Só então inicie a entrevista de especialização.
