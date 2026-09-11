# Agente de Projeto para Codex

Skill em português para criar a base persistente de um agente de projeto no Codex. Automatiza a configuração inicial do workspace, memória local com MemPalace, Graphify, RTK, servidores MCP, catálogos de skills, `AGENTS.md` e perfil funcional do agente.

> Feito por: [Gabriel Paz](https://github.com/GabrielPazBR/)

Nome exibido no Codex: **[AGENT] Implantação de agente de projeto by Paz**

## Implantação automatizada do agente

- MemPalace com palace individual armazenado dentro do projeto;
- RTK instalado, habilitado e testado;
- Graphify instalado no ambiente, registrado no projeto, indexado e testado;
- Context7, Playwright MCP e Gemini MCP Tool;
- catálogos de skills previstos pela implantação;
- perfil funcional persistido em `.agent/profile.yaml`;
- manifesto de instalação em `.agent/manifest.yaml`;
- instruções do projeto em `AGENTS.md`, preservando o conteúdo existente;
- testes finais e registro das pendências que exigirem intervenção do usuário.

A skill é executada por solicitação explícita. Depois de uma implantação concluída, novas execuções servem para diagnosticar ou reparar componentes, sem reinstalar toda a estrutura automaticamente.

## Requisitos para instalação

- Codex com suporte a skills;
- Git, Python e acesso à internet durante a instalação dos componentes;
- permissão para alterar o workspace e instalar dependências no escopo do usuário;
- credenciais somente quando algum serviço selecionado realmente exigir autenticação.

Alguns componentes podem exigir Node.js, navegadores do Playwright ou outras bibliotecas. A própria implantação verifica o ambiente, instala o que estiver ausente dentro do escopo autorizado e informa qualquer ação manual necessária.

## Instalar a skill no Codex

Peça ao Codex para instalar a skill a partir deste repositório:

```text
Use $skill-installer para instalar a skill do repositório
https://github.com/GabrielPazBR/agente-de-projeto
```

O instalador salva a skill em `$CODEX_HOME/skills/agente-de-projeto`. Quando `CODEX_HOME` não estiver definido, o destino padrão é `~/.codex/skills/agente-de-projeto`.

A skill ficará disponível no turno seguinte do Codex.

## Instalação manual da skill

Clone o repositório dentro do diretório de skills:

### PowerShell

```powershell
$destinoSkills = if ($env:CODEX_HOME) {
    Join-Path $env:CODEX_HOME "skills"
} else {
    Join-Path $HOME ".codex\skills"
}

New-Item -ItemType Directory -Force -Path $destinoSkills | Out-Null
git clone https://github.com/GabrielPazBR/agente-de-projeto.git `
    (Join-Path $destinoSkills "agente-de-projeto")
```

### Linux ou macOS

```bash
destino_skills="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$destino_skills"
git clone https://github.com/GabrielPazBR/agente-de-projeto.git \
  "$destino_skills/agente-de-projeto"
```

Se o Codex já estiver aberto, inicie um novo turno depois da instalação para que a skill seja descoberta.

## Criar um agente para o projeto

Abra no Codex o projeto que receberá o agente e solicite:

```text
Use $agente-de-projeto para implantar a base e especializar o agente deste projeto.
```

Durante a execução, a skill:

1. confirma o workspace e inspeciona o que já existe;
2. instala ou repara os componentes comuns;
3. testa os serviços configurados;
4. faz perguntas para definir a função, os objetivos e os limites do agente;
5. registra o perfil e atualiza as instruções persistentes do projeto;
6. apresenta o que foi concluído e o que ainda depende do usuário.

Execute a implantação no diretório do projeto que será configurado. Não a execute no diretório global de skills nem em uma pasta que reúna vários projetos.

## Atualizar a skill

Em uma instalação feita com Git:

```bash
git -C "/caminho/para/agente-de-projeto" pull --ff-only
```

Se a skill tiver sido instalada pelo `skill-installer`, remova a versão instalada e peça uma nova instalação a partir do repositório. Antes disso, preserve alterações locais que você queira manter.

## Arquivos e funcionamento

```text
agente-de-projeto/
|-- SKILL.md
|-- agents/openai.yaml
|-- assets/
|-- references/
`-- scripts/
```

- `SKILL.md` define o fluxo principal e os limites da implantação.
- `references/` contém as etapas detalhadas carregadas conforme a fase atual.
- `assets/` contém modelos usados nos arquivos persistentes do projeto.
- `scripts/` reúne inspeção, atualização e validação determinísticas.

## Limites da implantação

Esta skill cobre somente a base comum e o perfil funcional do agente. Integrações de negócio, políticas específicas de segredos, fontes externas e permissões próprias de cada projeto devem ser definidas separadamente.

## Autor

Feito por: [Gabriel Paz](https://github.com/GabrielPazBR/)
