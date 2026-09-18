#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baixa para assets/img/ todas as imagens e o PDF que os HTMLs ainda carregam do
WordPress (marcodsvinicius.com/wp-content e i0.wp.com) e troca os links pelos
caminhos relativos. Rode na raiz do repositório, em uma máquina com acesso à internet:

    python3 scripts/baixar-imagens.py

Depois confira o `git status`, teste o site e faça o commit.
"""
import pathlib, re, sys, urllib.parse, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
IMG = ROOT / 'assets' / 'img'
IMG.mkdir(parents=True, exist_ok=True)
PAGES = [ROOT / 'index.html'] + sorted((ROOT / 'pt').glob('*.html')) + sorted((ROOT / 'en').glob('*.html'))
URL_RE = re.compile(r'https?://(?:i0\.wp\.com/)?marcodsvinicius\.com/wp-content/uploads/[^"\')\s]+')

def local_name(url):
    path = urllib.parse.urlparse(url).path
    return urllib.parse.unquote(path.rsplit('/', 1)[-1])

def download(url, dest):
    if dest.exists():
        return
    print('baixando', url)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=60) as r, open(dest, 'wb') as f:
        f.write(r.read())

seen = {}
for page in PAGES:
    html = page.read_text(encoding='utf-8')
    urls = sorted(set(URL_RE.findall(html)))
    if not urls:
        continue
    # og:image e canonical continuam absolutos (precisam de URL pública)
    rel_root = '' if page.parent == ROOT else '../'
    for url in urls:
        name = local_name(url)
        dest = IMG / name
        try:
            download(url, dest)
        except Exception as e:  # noqa: BLE001
            print('  FALHOU', url, e, file=sys.stderr)
            continue
        seen[url] = name
        html = re.sub(r'(?<!content=")' + re.escape(url), rel_root + 'assets/img/' + name, html)
    page.write_text(html, encoding='utf-8')
    print('atualizado', page.relative_to(ROOT))

print(f'\n{len(seen)} arquivo(s) em assets/img/. Links absolutos restantes:')
for page in PAGES:
    for url in URL_RE.findall(page.read_text(encoding='utf-8')):
        print('  ', page.relative_to(ROOT), url)
