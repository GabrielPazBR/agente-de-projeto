# Linguagem e texto voltado ao usuário

Aplique esta política a interfaces, mensagens, documentação destinada ao usuário, acessibilidade, notificações, e-mails, metadados e materiais de apresentação. Código, identificadores internos, logs técnicos e documentação para desenvolvedores podem usar a terminologia necessária.

## Princípio

Escreva para ajudar o usuário a compreender uma ação, um estado ou uma consequência. Use linguagem direta, concisa, neutra e compatível com o vocabulário do projeto.

Antes de adicionar um texto, verifique se ele comunica informação necessária. Remova frases, subtítulos, ícones e descrições que apenas repetem o que a interface já demonstra.

## Redação

- Comece pela informação ou ação principal.
- Use frases curtas, voz ativa e verbos concretos.
- Use o mesmo termo para o mesmo conceito em toda a interface.
- Preserve o idioma e a variante regional definidos pelo projeto.
- Respeite traduções existentes e parâmetros explícitos de idioma.
- Explique termos técnicos somente quando forem necessários para a decisão do usuário.
- Em instruções, apresente os passos na ordem de execução.
- Em confirmações, informe o que aconteceu e, quando relevante, o próximo passo.
- Em erros, informe o problema, seu efeito e uma ação possível sem culpar o usuário.
- Em estados vazios, explique o que está ausente e apresente uma ação quando ela existir.
- Use verbos objetivos em botões, como `Salvar`, `Importar`, `Excluir` e `Tentar novamente`.
- Use substantivos ou expressões curtas em labels, como `Nome do projeto` e `Data de início`.

## Evitar aparência de texto gerado

Evite:

- introduções genéricas antes do conteúdo solicitado;
- conclusões que apenas repetem o conteúdo anterior;
- explicações sobre decisões evidentes na própria interface;
- frases promocionais sem informação verificável;
- linguagem excessivamente entusiasmada;
- personificação desnecessária do sistema ou da IA;
- metáforas vagas para ações comuns;
- sequências artificiais de adjetivos;
- títulos seguidos por subtítulos que repetem a mesma ideia;
- listas criadas apenas para fragmentar uma mensagem curta;
- pedidos de desculpas automáticos em erros rotineiros;
- afirmações absolutas sobre qualidade, segurança, desempenho ou disponibilidade.

Não use expressões como `experiência incrível`, `solução poderosa`, `resultado inteligente`, `processo revolucionário`, `ultra-rápido`, `simples e intuitivo`, `leve seu projeto ao próximo nível`, `desbloqueie todo o potencial`, `100% seguro` ou `totalmente garantido`. Substitua por fatos, ações ou resultados verificáveis.

## Terminologia

Em textos apresentados ao usuário:

- não use `operacional`, `operativo`, `tático` ou `tática`;
- evite jargões arquiteturais como `Client-Side`, `Serverless`, `Worker Thread` e `Local Processing`, salvo quando o público precisar deles;
- não acrescente traduções técnicas entre parênteses sem necessidade;
- preserve nomes oficiais de produtos, bibliotecas, comandos e formatos;
- não altere identificadores técnicos por motivos de estilo.

## Pontuação e formatação

- Não use travessão longo.
- Para separar ideias, use ponto, dois-pontos, vírgula ou hífen com espaços.
- Evite exclamações em mensagens rotineiras.
- Evite títulos inteiramente em maiúsculas.
- Não use emojis como substitutos de informação.
- Use negrito apenas quando facilitar a localização de informação importante.
- Não transforme prosa simples em vários níveis de títulos ou listas.

## Segurança e privacidade na interface

Apresente informações sobre segurança ou privacidade somente quando elas alterarem a decisão ou o comportamento do usuário. Descreva comportamentos concretos e verificáveis, sem promessas amplas como `Seus dados estão 100% seguros` ou `Processamento completamente privado`.

## Acessibilidade

Todo texto de interface deve:

- possuir nomes acessíveis claros;
- fazer sentido sem depender apenas de cor, posição ou ícone;
- identificar campos, erros e ações de forma específica;
- manter legibilidade em temas claro e escuro;
- evitar textos alternativos redundantes;
- descrever a finalidade de imagens funcionais;
- deixar imagens decorativas fora da navegação assistiva.

Ao modificar uma interface, verifique contraste, foco visível, ordem de navegação e associação entre labels, campos e mensagens de erro.

## Revisão

Antes de concluir, confirme:

1. A informação ajuda o usuário a agir ou compreender o estado atual.
2. O texto não repete elementos próximos.
3. Os termos são consistentes com o projeto.
4. Não há superlativos, autoelogios ou promessas absolutas.
5. Não há jargão desnecessário.
6. Erros indicam uma ação possível quando ela existir.
7. O texto continua compreensível fora do contexto visual imediato.
8. A redação respeita o idioma e o tom definidos para o projeto.
