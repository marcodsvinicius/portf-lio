# Revisão de SEO

O HTML estático atual já possuía descrição e links rastreáveis. As respostas em cache da Hostinger ainda podem servir o WordPress antigo em / e /en/; essa divergência impede validar os alertas do PageSpeed como falhas da versão atual. A limpeza da CDN/LiteSpeed no hPanel continua necessária.

## Melhorias publicadas

- Títulos e descrições das homes com nome, cargo e especialidades presentes no conteúdo.
- Títulos exclusivos dos cases públicos com tema e contexto UX/UI.
- JSON-LD: Person, WebSite e ProfilePage nas homes; WebPage, CreativeWork e BreadcrumbList nos cases públicos. Apenas informações já presentes no portfólio, sem métricas, avaliações ou datas inventadas.
- Sitemap com as oito URLs públicas, incluindo os alternates de português/inglês, autorreferência e x-default em todas elas. Hub restrito permanece noindex e fora do sitemap.
- Open Graph e Twitter completos, com imagem representativa de cada case público, dimensões e alternativa textual.
- Carregamento adiado do Lucide e preload da fonte de peso 800 usada nos títulos principais.
- Preview mantém noindex e canonical da produção.

## Validação

Lighthouse local, auditoria SEO mobile: homes PT/EN e Tour Guiado tinham 100/100 antes da revisão. O objetivo das alterações é melhorar a relevância e a interpretação do conteúdo, mantendo as verificações técnicas aprovadas. A pontuação não comprova posicionamento no Google. JSON-LD, arquivos de imagem social, títulos/descrições únicos, idioma e reciprocidade do sitemap foram verificados por script. Testes de navegação/imagens/responsividade conferem que defer e os metadados não interrompem o site.

## Acompanhamento

Depois de limpar o cache da hospedagem, enviar https://marcodsvinicius.com/sitemap.xml e inspecionar as páginas públicas no Google Search Console. Não há acesso configurado ao Search Console nesta sessão. Rankings e cliques devem ser acompanhados lá; o Clarity acompanha comportamento dentro do site.
