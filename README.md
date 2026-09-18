# Portfólio — Marco Vinicius

Site estático (HTML + Tailwind CSS via CDN) do portfólio publicado em [marcodsvinicius.com](https://marcodsvinicius.com).

## Estrutura

```
index.html                 Home em português (fonte de verdade)
en/index.html              Home em inglês
pt/Case-*.html             Cases em português
en/Case-*.html             Cases em inglês
pt/index.html              Redireciona para a raiz (compatibilidade com /pt/)
assets/css/site.css        Estilos compartilhados (reveal, tilt, timeline, contato, reduced-motion)
assets/js/tailwind.config.js  Tokens do design system (cores, fontes, keyframes)
assets/js/site.js          Comportamentos comuns: menu, cabeçalho, scrollspy, reveal, transições
assets/js/home.js          Interações exclusivas da home
design.md                  Design system "Cyberpunk Glass & Neon Lime"
```

Toda página carrega, nesta ordem: Tailwind (versão fixa) → `tailwind.config.js` → Lucide (versão fixa) → `site.css` → `site.js` (defer).
As classes de cor usam os tokens `brand` (`#B7E500`), `lime` (`#CCFF00`), `ink` e `surface` em vez de valores arbitrários.

## Rodando localmente

Qualquer servidor estático funciona. Exemplo com Python:

```bash
python3 -m http.server 8080
# abra http://localhost:8080/
```

## Publicação

O repositório pode ser publicado direto no GitHub Pages ou clonado pela integração Git da Hostinger para dentro de `public_html`.
As imagens dos cases, a foto e o PDF do currículo ainda são carregados de `marcodsvinicius.com/wp-content/...`; para o site ficar 100% independente do WordPress, esses arquivos precisam ser copiados para `assets/img/` e os links atualizados.
