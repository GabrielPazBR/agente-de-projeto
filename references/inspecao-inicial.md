# Inspeção inicial

Conclua esta fase antes de instalar qualquer componente.

## 1. Confirmar o destino

Resolva o caminho absoluto do workspace e confirme que ele representa o projeto solicitado. Recuse como destino uma raiz de disco, o diretório pessoal inteiro ou uma pasta global de configuração.

Quando houver dúvida real sobre qual projeto deve ser alterado, pergunte antes de escrever.

## 2. Coletar fatos

Execute `scripts/inspect_project.py <workspace>` quando Python estiver disponível. Complete a inspeção manualmente quando algum item não puder ser detectado pelo script.

Use `--full-catalogs` somente durante a deduplicação de skills; a saída padrão mantém o inventário resumido.

Verifique:

- sistema, arquitetura e shell;
- Git, remote e estado do repositório;
- `AGENTS.md`, `CLAUDE.md` e instruções equivalentes;
- `.agent/`, `.agents/`, manifests e perfis anteriores;
- monorepo, gerenciadores e lockfiles;
- Python, `uv`, Node.js, npm e `npx`;
- RTK e configuração para o agente atual;
- MemPalace, palace e skills relacionadas;
- Graphify CLI, skill no escopo do projeto, `graphify-out/` e estado do grafo;
- Context7 em modo MCP ou CLI;
- Playwright MCP, pacote Playwright e navegadores;
- Gemini MCP Tool, Gemini CLI e `agy`;
- skills já instaladas e possíveis duplicatas das fontes Matt Pocock e Joshua David Thomas;
- configurações e catálogos no escopo do projeto, do cliente de agente e do usuário, incluindo cache de plugins quando acessível.

Não converta um fato verificável em pergunta.

## 3. Classificar o estado

Leia `.agent/manifest.yaml`, quando existir, e compare seu conteúdo com o ambiente observado.

- Use **novo** quando não houver implantação anterior identificável.
- Use **retomada** quando houver fases incompletas.
- Use **reparo** somente quando um teste demonstrar regressão ou componente ausente.
- Use **concluído** quando todas as fases e verificações continuarem válidas.

Arquivos presentes sem teste correspondente não comprovam conclusão.

## 4. Preservar o ambiente

Antes de alterar arquivos:

- registre arquivos existentes que serão tocados;
- preserve lockfiles e gerenciadores escolhidos pelo projeto;
- identifique configurações que pertencem ao usuário;
- planeje atualização no lugar para blocos já gerados;
- não substitua um modo funcional por outro apenas por preferência.

## Critério de conclusão

A fase termina quando o caminho do projeto, o estado da implantação, os componentes existentes e os arquivos que poderão ser alterados estiverem registrados. Apresente um resumo curto antes de iniciar a instalação.
