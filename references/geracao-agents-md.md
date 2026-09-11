# Geração do AGENTS.md

Crie instruções persistentes com baixa carga de contexto. Use `AGENTS.md` na raiz do workspace, como solicitado por esta skill.

## Preservação

- Leia o arquivo inteiro antes de editar.
- Renderize `assets/agents-block.md` em um arquivo temporário, substitua todos os placeholders e use `scripts/update_agents_block.py <workspace> <bloco-renderizado>` para aplicar o bloco.
- O script calcula o SHA-256 do conteúdo fora do bloco e o grava em `.agent/agents-unmanaged.sha256` antes da edição.
- Preserve conteúdo fora do bloco gerenciado.
- Use os marcadores de `assets/agents-block.md`.
- Se os marcadores já existirem, substitua somente o conteúdo entre eles.
- Se não existirem, acrescente um único bloco em posição coerente.
- Não crie blocos duplicados.
- Mantenha cada regra em uma única fonte.
- Após a edição, execute `scripts/validate_project_setup.py` para confirmar que o conteúdo fora do bloco mantém o mesmo hash.

## Instruções auxiliares

Copie para `.agent/instructions/`:

- `assets/instructions/gemini.md` como `gemini.md`;
- `assets/instructions/linguagem-usuario.md` como `linguagem-usuario.md`;
- `assets/instructions/uploads-web.md` como `uploads-web.md` somente quando o perfil confirmado incluir aplicação web que recebe arquivos de usuários.

O `AGENTS.md` deve conter ponteiros claros para essas instruções, com a condição que exige sua leitura. Não incorpore as políticas extensas no bloco sempre carregado.

## Conteúdo do bloco

Preencha o modelo com:

- caminho do manifesto e do perfil;
- regra de uso do RTK;
- recall e registro do MemPalace;
- uso do Graphify para compreender, investigar e localizar código, e atualização incremental depois de qualquer modificação nos arquivos do workspace;
- gatilhos do Gemini;
- gatilhos da política de linguagem;
- política de uploads, quando aplicável;
- skills e MCPs ativos no perfil;
- critérios gerais de conclusão do agente.

Use instruções positivas e verificáveis. Remova frases que apenas descrevam capacidades já evidentes no ambiente.

## Critério de conclusão

O `AGENTS.md` termina quando o bloco está presente uma única vez, todos os ponteiros resolvem para arquivos existentes e as instruções correspondem ao perfil confirmado.
