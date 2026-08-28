# Upload e gerenciamento de arquivos de usuários

Ao implementar ou manter uploads em uma aplicação web:

- armazene arquivos enviados fora dos arquivos da aplicação e, quando possível, fora do diretório público;
- use diretórios dedicados e as permissões mínimas necessárias;
- gere nomes aleatórios ou UUIDs, preserve o nome original apenas como metadado e impeça path traversal;
- imponha limites de tamanho, quantidade, processamento e armazenamento;
- bloqueie execução de scripts em diretórios que recebem uploads;
- valide o tipo real do arquivo e aplique `X-Content-Type-Options: nosniff`;
- trate formatos que podem executar conteúdo ativo, como HTML e SVG, antes de disponibilizá-los;
- registre usuário, data, nome original, nome gerado, tamanho e tipo validado quando o projeto exigir auditoria;
- mantenha uploads fora do controle de versão e dos artefatos de publicação;
- verifique autorização, isolamento entre usuários, download, retenção e exclusão.

Arquivos públicos devem usar um controlador de acesso ou um diretório isolado sem execução de scripts.
