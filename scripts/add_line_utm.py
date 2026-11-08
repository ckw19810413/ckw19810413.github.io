#!/usr/bin/env python3
"""Append bridge UTM params to every outbound line.me URL in content/ and config/.

utm_source=ghpages, utm_medium=bridge, utm_campaign=5s-hook, utm_content=<sticker-slug>.
Existing query strings are preserved; URLs that already carry utm_source are left alone,
so the script is idempotent. Slugs come from data/line_sticker_slugs.yaml.
Usage: python3 scripts/add_line_utm.py [--check]
"""
import pathlib, re, sys
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

ROOT = pathlib.Path(__file__).resolve().parent.parent
SLUGS = dict(re.findall(r'^"(\d+)":\s*([A-Za-z0-9_-]+)\s*$',
                        (ROOT / 'data/line_sticker_slugs.yaml').read_text(), re.M))
URL_RE = re.compile(r'https?://(?:[a-z0-9-]+\.)*line\.me(?:/[^\s"\'<>)\]]*)?')


def slug_for(parts):
    m = re.search(r'/(?:S/sticker|stickershop/product)/(\d+)', parts.path)
    if m:
        return SLUGS.get(m.group(1), 'sticker-' + m.group(1))
    m = re.search(r'/author/(\d+)', parts.path)
    if m:
        return 'author-' + m.group(1)
    if parts.hostname == 'creator.line.me':
        return 'creator-market'
    return re.sub(r'[^A-Za-z0-9_-]+', '-', parts.path.strip('/')) or 'line-store'


def tag(url):
    parts = urlsplit(url)
    q = parse_qsl(parts.query, keep_blank_values=True)
    if any(k == 'utm_source' for k, _ in q):
        return url
    q += [('utm_source', 'ghpages'), ('utm_medium', 'bridge'),
          ('utm_campaign', '5s-hook'), ('utm_content', slug_for(parts))]
    return urlunsplit(parts._replace(query=urlencode(q)))


def main():
    check = '--check' in sys.argv
    files = list((ROOT / 'content').rglob('*.md')) + list((ROOT / 'config').rglob('*.toml'))
    changed = n = 0
    for p in files:
        text = p.read_text(encoding='utf-8')
        new = URL_RE.sub(lambda m: tag(m.group(0)), text)
        if new != text:
            changed += 1
            n += sum(1 for _ in URL_RE.finditer(text)) - sum(
                1 for m in URL_RE.finditer(text) if 'utm_source=' in m.group(0))
            if not check:
                p.write_text(new, encoding='utf-8')
    print(f"{'would tag' if check else 'tagged'} {n} URLs in {changed} files")
    return 1 if check and changed else 0


if __name__ == '__main__':
    sys.exit(main())
