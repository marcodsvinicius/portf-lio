# Revisão de produção — 8 de novembro de 2026

Foram corrigidos o menu em telas baixas, restauração de foco, rolagem após redimensionamento, tratamento de falhas de armazenamento/criptografia no acesso, acessibilidade de senha e feedback de cópia de e-mail.

20 arquivos preservados localmente: 19 imagens e o currículo. Links internos e âncoras revisados; URLs canônicas/sitemap apontam ao domínio oficial. As quatro páginas antigas de case na raiz redirecionam para as atuais.

## Imagens restauradas do backup

As sete imagens pendentes foram recuperadas do backup All-in-One WP Migration fornecido pelo proprietário e salvas em `assets/img/`. As imagens, os comparadores e as galerias originais foram restaurados nas páginas em português e inglês. Não há avisos temporários de indisponibilidade. Todos os 20 arquivos de mídia usados pelo site estão versionados localmente, incluindo o currículo. O backup completo e seu conteúdo privado não integram o repositório.

## Hospedagem

A Hostinger ainda entrega páginas antigas em algumas respostas de cache. É necessário limpar o cache LiteSpeed/CDN no hPanel; alterar arquivos no Git não remove uma resposta já armazenada na borda.

## Verificação

Navegação PT/EN, menu em mobile/landscape/desktop, resumo, galeria, falhas de armazenamento/clipboard/criptografia, foco e rolagem foram testados em navegador. LinkedIn e Medium bloqueiam verificadores automáticos; isso não comprova link quebrado. Certificados no Drive/Coursera e GitHub responderam normalmente.

## Nova rodada de QA

As 10 páginas passaram na verificação de imagens, links locais e largura em 320, 768 e 1440px. A análise automatizada axe-core não encontrou violações nas regras WCAG 2 A/AA e 2.1 AA testadas. Testes PT/EN verificaram falhas de armazenamento, criptografia e cópia de e-mail, acesso ao Hub, galeria e resumo.

Foram corrigidos: Shift+Tab escapando do resumo a partir do título; foco após “Ver cases”; estado acessível da miniatura do comparador; visibilidade do conteúdo com JavaScript desativado. Os testes de regressão desses comportamentos passaram em português e inglês.

A verificação do domínio confirmou que os endereços / e /en/ ainda podem retornar a página WordPress antiga pelo cache da hospedagem, enquanto /index.html e /en/index.html entregam a versão atual. A limpeza do cache da Hostinger/CDN continua dependente do hPanel.
