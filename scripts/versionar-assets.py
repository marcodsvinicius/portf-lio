#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Carimba ?v=<hash> nos links de CSS e JS das páginas.

Sem isso o navegador continua servindo a versão antiga do arquivo depois de um
deploy, porque a URL não mudou. Como o hash vem do conteúdo, o endereço só muda
quando o arquivo muda de verdade.

Rode na raiz do repositório depois de alterar qualquer CSS ou JS:

    python3 scripts/versionar-assets.py
"""
import hashlib, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = [ROOT / 'index.html'] + sorted((ROOT / 'pt').glob('*.html')) + sorted((ROOT / 'en').glob('*.html'))
REF = re.compile(r'(?P<attr>href|src)="(?P<path>(?:\.\./)?assets/(?:css|js)/[^"?]+\.(?:css|js))(?:\?v=[0-9a-f]+)?"')
cache = {}


def version(page: pathlib.Path, rel: str) -> str:
    target = (page.parent / rel).resolve()
    if target not in cache:
        cache[target] = hashlib.md5(target.read_bytes()).hexdigest()[:8] if target.exists() else None
    return cache[target]


changed = 0
for page in PAGES:
    html = page.read_text(encoding='utf-8')

    def stamp(m):
        v = version(page, m.group('path'))
        if v is None:
            print(f'  aviso: {page.name} aponta para {m.group("path")}, que não existe', file=sys.stderr)
            return m.group(0)
        return f'{m.group("attr")}="{m.group("path")}?v={v}"'

    new = REF.sub(stamp, html)
    if new != html:
        page.write_text(new, encoding='utf-8')
        changed += 1

print(f'{changed} página(s) atualizada(s); {len([v for v in cache.values() if v])} arquivo(s) versionado(s)')
