# Especialização do agente

Converta o objetivo do usuário em um perfil funcional claro depois que a base estiver disponível.

## 1. Preparar o contexto

Use os fatos da inspeção, leia a documentação principal do projeto e consulte o MemPalace. Identifique o que já pode ser inferido sobre finalidade, usuários, domínio, stack, estágio e entregáveis.

Não pergunte informações observáveis no workspace.

## 2. Entrevistar por decisões

Construa uma árvore de decisões e pergunte somente a fronteira atual. Faça rodadas curtas, com recomendação e impacto quando houver alternativas reais.

Obtenha o suficiente para definir:

- resultado esperado do projeto;
- função principal do agente;
- responsabilidades recorrentes;
- atividades fora de escopo;
- entregáveis e critérios de conclusão;
- domínio e termos canônicos;
- tecnologias e ambientes relevantes;
- tipos de pesquisa e validação esperados;
- grau de autonomia e pontos que exigem decisão humana;
- capacidades adicionais desejadas.

Aceite respostas informais. Converta-as para linguagem consistente sem alterar o sentido. Quando um termo estiver vago ou conflitar com o workspace, apresente a diferença e peça uma decisão.

## 3. Pesquisa assistida pelo Gemini

Use o Gemini MCP como segunda perspectiva para explorar metodologias, skills, MCPs e plugins adequados ao perfil. Peça uma lista estruturada com fonte original, contribuição, aplicação e limitações.

Verifique itens relevantes nas fontes oficiais. Marque como não confirmada qualquer referência que não possa ser localizada. Não apresente disponibilidade, licença ou compatibilidade como fato sem confirmação.

Compare as sugestões com capacidades já instaladas e elimine duplicatas. Prefira uma capacidade existente quando ela atender ao mesmo objetivo.

Quando a capacidade de gestão de plugins estiver disponível, use-a para confirmar existência, estado, dependências e permissões dos plugins candidatos. Uma menção do Gemini não comprova que o plugin está disponível no ambiente.

## 4. Apresentar o perfil

Mostre ao usuário:

- síntese da função;
- responsabilidades e limites;
- capacidades já disponíveis;
- skills sugeridas;
- MCPs ou plugins adicionais sugeridos;
- justificativa e custo de cada adição;
- itens não confirmados ou incompatíveis.

Solicite confirmação antes de instalar componentes adicionais ao conjunto comum.

## 5. Implantar capacidades aprovadas

Para cada capacidade adicional confirmada:

1. use a skill, ferramenta de plugins ou procedimento MCP apropriado quando estiver disponível;
2. instale no menor escopo compatível com o projeto;
3. configure somente o necessário à função confirmada;
4. execute uma operação mínima real;
5. atualize o perfil, o manifesto e o registro de origem das skills;
6. mantenha como pendente qualquer capacidade não testada.

Não registre uma sugestão como habilitada antes dessa verificação.

## 6. Registrar

Crie `.agent/profile.yaml` a partir de `assets/profile-template.yaml`. Registre fatos observados, decisões confirmadas, hipóteses e pendências em campos distintos.

O perfil deve usar termos consistentes com o domínio do projeto. Não copie a conversa literalmente quando uma formulação estruturada for mais precisa.

## Critério de conclusão

A fase termina quando o usuário confirmar o perfil, as capacidades adicionais selecionadas estiverem instaladas e testadas ou marcadas como pendentes, e o arquivo não contiver decisões silenciosamente assumidas.
