# Portfólio — Marco Vinicius

Site estático (HTML + Tailwind CSS via CDN) do portfólio publicado em [marcodsvinicius.com](https://marcodsvinicius.com).

## Estrutura

```
index.html                 Home em português (fonte de verdade)
en/index.html              Home em inglês
pt/Case-*.html             Cases em português
en/Case-*.html             Cases em inglês
pt/index.html              Redireciona para a raiz (compatibilidade com /pt/)
assets/css/tailwind.css    CSS do Tailwind compilado (gerado, não edite à mão)
assets/css/tailwind.src.css  Entrada do Tailwind
assets/css/site.css        Estilos compartilhados (reveal, tilt, timeline, contato, reduced-motion)
assets/js/site.js          Comportamentos comuns: menu, cabeçalho, scrollspy, reveal, transições
assets/js/home.js          Interações exclusivas da home
assets/js/case.js          Carrosséis, lightbox e trava de senha dos cases
assets/js/vendor/          Lucide (ícones) servido localmente
assets/img/                Favicon e, no futuro, as imagens dos cases
tailwind.config.js         Tokens do design system (cores, fontes, keyframes)
scripts/baixar-imagens.py  Traz as imagens do WordPress para assets/img
design.md                  Design system "Cyberpunk Glass & Neon Lime"
.htaccess                  Cabeçalhos de segurança, cache e redirecionamentos (Hostinger)
```

Toda página carrega `tailwind.css` → `site.css` → Lucide → `site.js` (defer) → `home.js` ou `case.js` (defer).
Não há script de terceiros em tempo de execução: tudo é servido do próprio domínio, e cada página declara uma
Content Security Policy que bloqueia scripts inline e de outras origens.
As classes de cor usam os tokens `brand` (`#B7E500`), `lime` (`#CCFF00`), `ink` e `surface` em vez de valores arbitrários.

## Editando

O CSS do Tailwind é compilado. Depois de mudar classes no HTML ou no JS, rode:

```bash
npm install      # só na primeira vez
npm run build    # compila o Tailwind e carimba ?v=<hash> nos links de CSS e JS
```

O carimbo de versão é o que faz o navegador buscar o arquivo novo depois de um deploy.
Sem ele, uma página nova pode acabar usando o CSS antigo que ficou no cache.

Se você editar direto no GitHub (pelo celular, por exemplo), não precisa rodar nada: o Action
`build-css.yml` recompila o CSS a cada push na `main` e faz o commit sozinho.

## Seção AI First

Os quatro cards vêm direto do HTML. O terminal ao lado digita o texto de `data-prompt` e mostra `data-out`
do card ativo, então basta editar esses atributos no card para mudar o que aparece no terminal.

Os artigos são lidos de um bloco JSON dentro da própria página (`<script type="application/json" id="ai-articles">`).
Para publicar um artigo, troque o `[]` por uma lista assim, em `index.html` e em `en/index.html`:

```json
[
  {
    "title": "Como usei agentes para gerar telas responsivas",
    "url": "https://medium.com/@marcodsvinicius/...",
    "source": "Medium",
    "date": "Set 2026",
    "summary": "O que testei, onde o agente acertou e onde precisei intervir.",
    "result": "3 telas revisadas em 40 min"
  }
]
```

Só `title` e `url` são obrigatórios. Com a lista vazia, aparece um único card levando ao perfil do Medium.

## Rodando localmente

```bash
npm run serve
# abra http://localhost:8080/
```

## Publicação

O repositório pode ser publicado direto no GitHub Pages ou clonado pela integração Git da Hostinger para dentro de `public_html`.
As imagens dos cases, a foto e o PDF do currículo ainda são carregados de `marcodsvinicius.com/wp-content/...`; para o site ficar 100% independente do WordPress, esses arquivos precisam ser copiados para `assets/img/` e os links atualizados.
