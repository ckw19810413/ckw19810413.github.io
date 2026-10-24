#!/usr/bin/env python3
"""Move a blog post's mp4/zip files out of git and into a GitHub Release.

Rule: no *.mp4 / *.zip under content/ (CI enforces it, see
tools/check_no_media.sh). Run this on a post bundle before committing it:

  python3 tools/publish_post_media.py content/blog/2026-10-23-line-animated-sticker-savage-goose \
      [--extra /path/to/Pack.zip ...]

For every *.mp4 / *.zip in the bundle (and each --extra file) it uploads the
file to release `media-<slug>` (slug = folder name without the date prefix;
created if missing, never marked latest), rewrites references in index.md to
the release download URL, and deletes the local copy. Re-running is safe:
assets already on the release are skipped.

Token: $GH_TOKEN, else ~/.priv/ckw19810413-github-hermes-token.
"""
import argparse, json, os, pathlib, re, sys, urllib.error, urllib.request

REPO = 'ckw19810413/ckw19810413.github.io'
API = f'https://api.github.com/repos/{REPO}'
MEDIA = ('.mp4', '.webm', '.mov', '.mkv', '.zip', '.gz', '.7z', '.wav')  # keep in sync with check_no_media.sh


def token():
    t = os.environ.get('GH_TOKEN')
    return t or pathlib.Path('~/.priv/ckw19810413-github-hermes-token').expanduser().read_text().strip()


def gh(method, url, data=None, ctype='application/json'):
    body = json.dumps(data).encode() if isinstance(data, dict) else data
    req = urllib.request.Request(url, data=body, method=method, headers={
        'Authorization': f'Bearer {token()}', 'Accept': 'application/vnd.github+json',
        'Content-Type': ctype})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            raw = r.read()
            return json.loads(raw) if raw else None
    except urllib.error.HTTPError as e:
        if e.code == 404 and method == 'GET':
            return None
        sys.exit(f'GitHub {method} {url} -> {e.code} {e.read()[:300]!r}')


def ensure_release(slug):
    tag = f'media-{slug}'
    rel = gh('GET', f'{API}/releases/tags/{tag}')
    if rel:
        return rel
    return gh('POST', f'{API}/releases', {
        'tag_name': tag, 'target_commitish': 'main', 'name': f'Media: {slug}',
        'body': f'Video / zip media for https://ckw19810413.github.io/blog/{slug}/ (kept out of git).',
        'make_latest': 'false'})


def upload(rel, path, name):
    if any(a['name'] == name for a in rel.get('assets', [])):
        print(f'  = {name} (already on release)')
        return
    url = rel['upload_url'].split('{')[0] + f'?name={name}'
    ctype = 'video/mp4' if name.lower().endswith('.mp4') else 'application/octet-stream'
    gh('POST', url, path.read_bytes(), ctype)
    print(f'  + {name} ({path.stat().st_size} B)')


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('bundle', type=pathlib.Path)
    ap.add_argument('--extra', type=pathlib.Path, nargs='*', default=[],
                    help='files outside the bundle to publish too (e.g. a sticker pack zip)')
    args = ap.parse_args()

    bundle = args.bundle.resolve()
    slug = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', bundle.name)
    files = sorted(p for p in bundle.rglob('*') if p.suffix.lower() in MEDIA)
    names = {}
    for p in files + list(args.extra):
        name = p.name if p in args.extra else p.relative_to(bundle).as_posix().replace('/', '-')
        if name in names.values():
            sys.exit(f'duplicate asset name {name}')
        names[p] = name
    if not names:
        print('no mp4/zip to publish')
        return

    rel = ensure_release(slug)
    base = f'https://github.com/{REPO}/releases/download/media-{slug}'
    print(f'release {rel["html_url"]}')
    for p, name in names.items():
        upload(rel, p, name)

    index = bundle / 'index.md'
    if index.exists():
        text = index.read_text()
        for p, name in names.items():
            if p in args.extra:
                continue
            rel_path = p.relative_to(bundle).as_posix()
            # src="x.mp4" / (x.mp4) / 'x.mp4' — relative references only.
            text = re.sub(r'(?<=["\'(])' + re.escape(rel_path) + r'(?=["\')])', f'{base}/{name}', text)
        # Share buttons that build a clip URL from the page location.
        text = re.sub(r'window\.location\.origin\s*\+\s*window\.location\.pathname\s*\+\s*(?=["\'][^"\']*["\'][^\n]*\.mp4)',
                      f'"{base}/" + ', text)
        index.write_text(text)
    for p in files:
        p.unlink()
    print(f'moved {len(files)} file(s) out of {bundle.name}; commit the bundle now')


if __name__ == '__main__':
    main()
