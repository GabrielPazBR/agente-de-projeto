<!-- agente-de-projeto:start -->
## Agente do projeto

Leia `.agent/profile.yaml` para função, responsabilidades, limites e capacidades ativas. Consulte `.agent/manifest.yaml` para o estado da implantação e versões verificadas.

### RTK

Use RTK nos comandos de terminal suportados. Quando a saída compactada não contiver detalhes suficientes, repita o comando pelo modo de saída integral do RTK.

### MemPalace

Antes de responder sobre decisões anteriores, consulte o palace deste projeto. Ao encerrar uma tarefa, registre fatos verificados, decisões, comandos úteis, erros, correções, pendências e próximos passos. Obtenha primeiro as instruções atuais com `mempalace instructions <operação>`.

### Graphify

Use a skill Graphify deste workspace para compreender a base de código, investigar fluxos e dependências, localizar arquivos e símbolos, avaliar impacto e responder perguntas cobertas pelo grafo. Prefira consultar o Graphify antes de percorrer o repositório manualmente; complemente com leitura direta quando o grafo não trouxer evidência suficiente. Depois de qualquer modificação nos arquivos do workspace, execute `$graphify . --update` antes de concluir a tarefa e verifique que o grafo foi atualizado.

### Gemini

Para pesquisa exploratória, revisão de literatura, descoberta de fontes, comparação de ferramentas, análise extensa ou segunda opinião, leia e aplique `.agent/instructions/gemini.md`.

### Linguagem voltada ao usuário

Ao escrever interface, acessibilidade, mensagens, notificações, documentação para usuários ou metadados, leia e aplique `.agent/instructions/linguagem-usuario.md`.

__UPLOADS_POINTER__

### Capacidades do perfil

__ACTIVE_CAPABILITIES__

Conclua tarefas somente após executar as verificações relevantes e registrar limitações que não puderam ser resolvidas.
<!-- agente-de-projeto:end -->
