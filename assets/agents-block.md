<!-- agente-de-projeto:start -->
## Agente do projeto

Leia `.agent/profile.yaml` para função, responsabilidades, limites e capacidades ativas. Consulte `.agent/manifest.yaml` para o estado da implantação e versões verificadas.

### RTK

Use RTK nos comandos de terminal suportados. Quando a saída compactada não contiver detalhes suficientes, repita o comando pelo modo de saída integral do RTK.

### MemPalace

Antes de responder sobre decisões anteriores, consulte o palace deste projeto. Ao encerrar uma tarefa, registre fatos verificados, decisões, comandos úteis, erros, correções, pendências e próximos passos. Obtenha primeiro as instruções atuais com `mempalace instructions <operação>`.

### Graphify

Use a skill Graphify deste workspace para compreender a base de código, investigar fluxos e dependências, localizar arquivos e símbolos, avaliar impacto e responder perguntas cobertas pelo grafo. Prefira consultar o Graphify antes de percorrer o repositório manualmente; complemente com leitura direta quando o grafo não trouxer evidência suficiente. Depois de qualquer modificação nos arquivos do workspace, execute `$graphify . --update` antes de concluir a tarefa e verifique que o grafo foi atualizado.

### Encerramento de navegadores de agentes

- Cada agente ou subagente deve fechar Chromium/Chrome e outros navegadores que iniciar assim que terminar de utilizá-los, antes de entregar ou seguir para trabalho sem navegador, inclusive em falhas, desistências e interrupções controladas.
- Use uma sessão exclusiva por tarefa/subagente e registre seu identificador e, quando disponível, os PIDs sob sua responsabilidade. Reutilize-a durante a validação e mantenha somente as páginas necessárias.
- No Playwright CLI, execute o comando de fechamento para cada sessão própria, por exemplo `playwright-cli --session <sessao-da-tarefa> close` (ou o wrapper do projeto), e confirme o resultado. No MCP, feche o navegador da própria sessão. Em scripts programáticos, use `finally` para fechar contextos e executar `await browser.close()`; em sessões interativas, execute e verifique a limpeza explicitamente.
- Confirme que a sessão e seus processos Chromium encerraram; fechar uma aba ou perder o terminal/REPL não basta. Em caso de falha, tente novamente pelo mecanismo da sessão e informe qualquer recurso que permaneça aberto. Encerre por PID somente após comprovar propriedade e ausência de uso.
- Ao delegar navegação, inclua essa obrigação e exija confirmação de fechamento na devolutiva. Se um subagente for interrompido antes da limpeza, o coordenador deve recuperar somente os recursos dele após confirmar que não estão em uso. Saídas abruptas podem impedir `finally` e traps; não presuma limpeza automática.
- Preserve sessões humanas e de outras tarefas; não use encerramento global, `pkill chrome` ou PPID 1 como prova de abandono. Só deixe uma sessão aberta após a entrega por pedido explícito do usuário, informando seu identificador e a responsabilidade pelo encerramento.

### Gemini

Para pesquisa exploratória, revisão de literatura, descoberta de fontes, comparação de ferramentas, análise extensa ou segunda opinião, leia e aplique `.agent/instructions/gemini.md`.

### Linguagem voltada ao usuário

Ao escrever interface, acessibilidade, mensagens, notificações, documentação para usuários ou metadados, leia e aplique `.agent/instructions/linguagem-usuario.md`.

__UPLOADS_POINTER__

### Capacidades do perfil

__ACTIVE_CAPABILITIES__

Conclua tarefas somente após executar as verificações relevantes e registrar limitações que não puderam ser resolvidas.
<!-- agente-de-projeto:end -->
