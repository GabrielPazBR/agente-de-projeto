# Validação final

Execute verificações proporcionais ao componente. Não use apenas inspeção de arquivos como prova de funcionamento.

## Artefatos

Execute:

```text
python <skill>/scripts/validate_project_setup.py <workspace>
```

Corrija campos ausentes, ponteiros quebrados e marcadores duplicados antes de continuar.

## Provas obrigatórias

### RTK

- versão identificada;
- integração do agente exibida;
- comando real executado;
- `rtk gain` acessível.

### MemPalace

- caminho físico dentro do workspace;
- escrita e recuperação após reinício;
- `status` acessível;
- mineração inicial executada;
- origem e resultado registrados.

### Graphify

- pacote oficial `graphifyy` e versão identificados;
- skill registrada em `.agents/skills/graphify/` e descoberta pelo Codex;
- `graphify-out/graph.json` gerado para o workspace;
- consulta real retorna símbolos e caminhos existentes;
- `AGENTS.md` exige uso nas tarefas pertinentes e atualização incremental após modificações.

### Context7

- servidor acessível;
- ferramenta de resolução ou consulta disponível;
- documentação de uma biblioteca e versão do projeto recuperada.

### Playwright MCP

- handshake concluído;
- ferramentas listadas;
- navegador iniciado;
- página inspecionada;
- processos iniciados no teste encerrados.

### Gemini MCP Tool

Execute todas as [provas do adaptador Antigravity](gemini-antigravity.md#provas-obrigatórias), incluindo regressão, erros, timeout, ajuda sem Gemini e duas consultas reais pelo MCP. Confira o backend, a entrada local versionada quando houver patch, o rollback e a preferência por `high` nas instruções geradas. Registre modelo solicitado separadamente do confirmado; limitações mantêm o componente parcial.

### Skills

- origens e versões registradas;
- `.agent/skill-sources.lock.yaml` preenchido;
- frontmatter válido;
- traduções aplicadas sem alterar identificadores;
- referências e scripts existentes;
- ausência de duplicatas ativas.

### Perfil e instruções

- perfil confirmado pelo usuário;
- `AGENTS.md` preserva conteúdo anterior;
- bloco gerenciado aparece uma vez;
- ponteiros resolvem;
- políticas condicionais correspondem ao perfil.

## Manifesto

Atualize cada componente com `passed`, `failed`, `blocked` ou `skipped`, acompanhado de evidência curta e data. Use `complete` para a implantação somente quando todos os requisitos obrigatórios estiverem em `passed`.

## Relatório ao usuário

Informe:

- caminho do workspace e do palace;
- versões instaladas ou reutilizadas;
- perfil definido;
- skills, Graphify, MCPs e políticas habilitados;
- testes executados e resultados;
- itens ignorados e motivo;
- bloqueios e ações necessárias.

Uma autenticação pendente, handshake não testado ou persistência não comprovada mantém a implantação parcial.

## Texto voltado ao usuário

Confirme que `.agent/instructions/linguagem-usuario.md` contém a política atual e que o bloco de `AGENTS.md` aponta para sua leitura. Em reparos, atualize o conteúdo gerenciado sem apagar regras próprias do projeto. Ao entregar interface alterada, aplique a revisão dessa política ao fluxo e aos estados afetados; registre provas reais e limitações de acessibilidade, idiomas e estados não exercitados.
