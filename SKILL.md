---
name: agente-de-projeto
description: "Cria, implanta ou repara um agente de projeto no Codex, com MemPalace local, RTK, servidores MCP, skills, perfil funcional e AGENTS.md persistente. Use na configuração inicial de um workspace ou para diagnosticar uma implantação existente."
---

# [AGENT] Implantação de agente de projeto

Feito por: [Gabriel Paz](https://github.com/GabrielPazBR/)

Prepare um workspace para uso recorrente por agentes. Execute a implantação completa uma vez; em reexecuções, inspecione e repare somente componentes ausentes, incompatíveis ou incompletos.

## Limites

- Use apenas o workspace confirmado como destino dos artefatos do projeto. A invocação autoriza instalações no escopo do usuário e ajustes na configuração do agente estritamente necessários aos componentes comuns listados nesta skill; não use o diretório pessoal inteiro, raízes de disco ou a pasta global de skills como destino do projeto.
- Implante somente a base comum e o perfil funcional. Não configure integrações de negócio, serviços do projeto ou políticas específicas que não tenham sido selecionadas na especialização.
- Preserve arquivos e configurações existentes. Atualize blocos próprios no lugar e não duplique instalações.
- Descubra fatos no ambiente antes de perguntar ao usuário.
- Registre versões e resultados observados. Não trate presença de arquivo ou término sem erro como prova suficiente.
- Use versões identificadas e preserve lockfiles. Não faça atualizações principais sem uma necessidade confirmada.

## Estado da implantação

Use `.agent/manifest.yaml` como registro da implantação.

- **Novo:** o manifesto não existe ou não identifica uma implantação concluída.
- **Retomada:** o manifesto registra passos pendentes ou falhos. Continue do primeiro passo incompleto.
- **Reparo:** a implantação foi concluída, mas um diagnóstico demonstra falha. Altere somente o componente afetado.
- **Concluído:** a implantação e os testes estão registrados como aprovados. Apresente o estado e não reinstale sem solicitação explícita.

## Fluxo

Leia uma referência por vez. Termine e registre a fase atual antes de carregar a próxima.

1. Leia [references/inspecao-inicial.md](references/inspecao-inicial.md). Confirme o workspace, detecte o estado existente e classifique a execução.
2. Para uma implantação nova ou retomada, leia [references/implantacao-base.md](references/implantacao-base.md). Configure RTK, MemPalace, MCPs e os dois catálogos de skills.
3. Quando a base estiver testada, leia [references/especializacao-agente.md](references/especializacao-agente.md). Entreviste o usuário, pesquise opções quando necessário e produza `.agent/profile.yaml`.
4. Leia [references/geracao-agents-md.md](references/geracao-agents-md.md). Gere as instruções persistentes e preserve o conteúdo preexistente.
5. Leia [references/validacao-final.md](references/validacao-final.md). Execute diagnósticos reais, registre resultados e apresente pendências.

## Autorização e perguntas

A invocação desta skill autoriza as alterações no workspace, instalações no escopo do usuário e ajustes na configuração do agente necessários a RTK, MemPalace, Context7, Playwright MCP, Gemini MCP Tool e catálogos de skills previstos. Elevação, autenticação, aceite de licença, instalação para todos os usuários ou uma escolha com efeitos diferentes devem parar no ponto exato e solicitar a ação do usuário.

Na especialização, apresente recomendações antes de instalar capacidades adicionais. A implantação comum não autoriza automaticamente integrações externas sugeridas durante a pesquisa.

## Resultado esperado

A conclusão exige:

- palace persistido dentro do workspace e mineração inicial verificada;
- RTK instalado, habilitado para o agente atual e testado;
- Context7, Playwright MCP e Gemini MCP configurados e testados;
- skills das fontes previstas importadas, traduzidas, deduplicadas e validadas;
- perfil funcional confirmado pelo usuário;
- `AGENTS.md` e instruções auxiliares atualizados;
- manifesto com versões, testes, falhas e pendências.

Se um requisito não puder ser comprovado, finalize como implantação parcial e informe o bloqueio. Não marque a implantação como concluída.
