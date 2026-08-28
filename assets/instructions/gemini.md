# Uso do Gemini MCP

Use o Gemini MCP como apoio quando a tarefa se beneficiar de uma segunda perspectiva:

- explorar metodologias, abordagens e referências;
- localizar artigos, teses, preprints, normas e bibliografia;
- iniciar revisão de literatura e identificar trabalhos relacionados ou lacunas;
- descobrir bases de dados, provedores, APIs, fontes públicas e recursos técnicos;
- comparar bibliotecas, frameworks, ferramentas, padrões e práticas;
- analisar grandes conjuntos de arquivos, documentação ou código;
- obter uma segunda opinião sobre arquitetura, causa-raiz, riscos ou escolhas técnicas.

## Pesquisa

Peça fontes estruturadas com título, autores ou organização, ano, URL original ou DOI, tipo, contribuição, aplicação possível e limitações.

Verifique os itens relevantes em fontes primárias. A resposta do Gemini é exploratória e não confirma autores, datas, DOI, links, documentação, disponibilidade, licença, compatibilidade ou aplicabilidade. Marque como não confirmado o que não puder ser localizado na origem.

## Limites

Use testes, lint, comandos, consultas, validações de runtime e automação de navegador diretamente no ambiente. Uma resposta do Gemini não substitui essas provas e não autoriza mudanças externas ou destrutivas.

Não envie credenciais, tokens, cookies, dados pessoais desnecessários, dumps de produção ou conteúdo sensível.

Ao usar o backend `agy`, não trate o parâmetro `sandbox` como isolamento. A execução em modo de impressão não é necessariamente isolada.

## Prompt de pesquisa

```text
Faça uma pesquisa exploratória sobre [tema].
Busque metodologias, artigos, referências bibliográficas, bases de dados,
provedores, ferramentas e bibliotecas relevantes.

Para cada item, informe título, autores ou organização, ano, URL original
ou DOI, tipo de fonte, contribuição, aplicação possível e limitações.
Não invente referências. Marque como não confirmado o que não puder ser
verificado na fonte original.
```
