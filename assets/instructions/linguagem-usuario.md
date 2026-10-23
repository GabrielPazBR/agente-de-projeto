# Linguagem e texto voltado ao usuário

## Objetivo e escopo

Escreva para ajudar a pessoa a entender a situação, interpretar a informação e concluir sua tarefa. Cada texto deve ter uma função clara.

Aplique esta política a interfaces, notificações, mensagens, documentação para usuários, e-mails, apresentações, rótulos acessíveis, mensagens de leitores de tela e metadados. Código, identificadores internos, logs técnicos e documentação para desenvolvedores podem usar a terminologia necessária.

## Princípios

- Comece pela informação ou ação principal. Use palavras comuns, voz ativa e verbos concretos.
- Prefira frases curtas sem remover precisão ou contexto necessário. Mantenha o mesmo termo para o mesmo conceito no fluxo.
- Use linguagem direta, neutra e compatível com o público. Empregue termos técnicos quando ajudarem a interpretar a informação ou decidir.
- Remova slogans, autoelogios, entusiasmo artificial, personificação desnecessária da IA, metáforas vagas, sequências artificiais de adjetivos e promessas absolutas.
- Remova introduções genéricas, conclusões repetitivas e subtítulos ou dicas que apenas repetem o título, botão ou componente. Crie listas quando a estrutura ajudar a leitura.
- Substitua afirmações como `100% seguro`, `solução poderosa` ou `simples e intuitivo` por fatos, ações ou resultados verificáveis.

## Função de cada texto

- **Título:** identifica o conteúdo ou a etapa.
- **Botão:** descreve a ação ou seu resultado, com um verbo específico, como `Salvar`, `Importar` ou `Excluir arquivo`.
- **Rótulo:** identifica o campo ou controle; mantenha instruções e exemplos na ajuda quando necessários.
- **Ajuda:** esclarece uma dúvida necessária para agir. Apresente passos na ordem de execução.
- **Confirmação:** informa o que ocorreu de fato e, quando relevante, o próximo passo. Diferencie solicitação recebida, processamento e conclusão.
- **Estado vazio, parcial, desatualizado ou de erro:** informa o que aconteceu, o efeito na tarefa e a ação disponível. Mostre apenas as partes necessárias, sem culpar a pessoa nem inserir desculpas automáticas.
- **Ação com consequências relevantes:** apresente o efeito antes da decisão, no ponto em que ajuda a escolher. Mantenha o botão conciso e use texto de apoio quando necessário. Não acrescente diálogos de confirmação a ações rotineiras apenas por causa desta política.

## Verdade e contexto

- Diferencie falha, ausência de dados, valor zero e dado parcial. Não substitua silenciosamente uma falha por zero ou estado vazio.
- Preserve horários, fuso quando necessário, unidades, limites e critérios de cálculo que afetem a interpretação. Identifique dados desatualizados ou parciais quando isso alterar sua leitura.
- Não invente resultados, garantias, causas de erro ou ações indisponíveis. Se a causa for desconhecida, descreva o problema observado.
- Informe destino de arquivos, persistência, privacidade e segurança quando esses fatos alterarem a decisão da pessoa. Descreva somente comportamento comprovado, sem promessas amplas ou explicações defensivas.
- Traduza erros técnicos para o problema da tarefa. Mantenha códigos e detalhes de diagnóstico em área secundária quando forem úteis ao suporte.
- Ofereça recuperação ou nova tentativa somente quando a ação existir e for adequada ao estado atual.

## Preferências editoriais e restrições do ambiente

Concisão e estilo não justificam omitir informação necessária. Preferências editoriais admitem adaptação ao público e ao contexto; restrições explícitas do proprietário continuam obrigatórias.

Neste ambiente, em textos voltados ao usuário e suas traduções:

- Não use `operacional`, `operativo`, `tático` ou `tática`. Descreva o estado ou a ação concreta, como `Disponível`, `Ativo` ou `Não foi possível carregar os dados`, somente quando corresponder aos fatos.
- Não use travessão longo. Prefira frases independentes, ponto, dois-pontos ou vírgula; quando necessário, use hífen com espaços.
- Evite jargões arquiteturais como `Client-Side`, `Serverless`, `Worker Thread` e `Local Processing` quando não ajudarem o público. Não acrescente traduções técnicas entre parênteses sem necessidade.
- Preserve nomes oficiais de produtos, bibliotecas, comandos e formatos. Não renomeie identificadores técnicos internos por estilo.
- Evite exclamações rotineiras e títulos inteiramente em maiúsculas. Use negrito quando facilitar a localização de informação e nunca use emojis como substitutos dela.

## Acessibilidade e idiomas

- Garanta nomes acessíveis específicos para controles e associação entre campos, rótulos e mensagens de erro.
- O texto deve fazer sentido sem depender apenas de cor, posição ou ícone. Identifique a ação pelo nome do controle.
- Mensagens dinâmicas relevantes devem ser perceptíveis por tecnologia assistiva sem anúncios redundantes ou perda indevida de foco.
- Descreva a finalidade de imagens funcionais; evite texto alternativo redundante e mantenha imagens decorativas fora da navegação assistiva.
- Preserve idioma e variante regional do projeto. Mantenha significado, ação e precisão equivalentes em todos os idiomas, incluindo estados, fallbacks e metadados.
- Revise traduções na interface real; ajuste a redação e a quebra de linhas sem perder significado. Evite limites arbitrários de palavras que prejudiquem clareza.

## Revisão antes da entrega

1. Que decisão, ação ou interpretação cada texto ajuda a realizar? Há repetição, promessa não comprovada ou explicação técnica desnecessária?
2. O texto corresponde ao estado real? Distingue erro, vazio, zero, processamento, parcial e desatualização quando aplicável?
3. Preserva detalhes necessários para interpretar dados e consequências, incluindo horários, unidades e limites?
4. Termos, tom, idioma e variante regional são consistentes? As traduções preservam ação e precisão?
5. No fluxo alterado, o texto funciona com teclado, leitor de tela e telas pequenas, com foco visível, contraste e legibilidade nos temas suportados?
6. Os estados dinâmicos, fallbacks, erros e rótulos acessíveis seguem os mesmos critérios? Ações oferecidas existem e funcionam?

Verifique esses pontos na interface renderizada quando houver interface executável. Inspeção do texto não comprova comportamento com teclado ou leitor de tela; registre o que foi testado e qualquer limitação sem declarar validações não executadas.
