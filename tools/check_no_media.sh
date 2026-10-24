#!/usr/bin/env bash
# Fail if git tracks a video/archive/audio file (mp4 webm mov mkv zip gz 7z wav,
# any case) under content/ that is not grandfathered in tools/media-allowlist.txt
# (files committed before the rule; history is not rewritten). Publish new media
# with tools/publish_post_media.py instead.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
exts=(mp4 webm mov mkv zip gz 7z wav)
specs=()
for e in "${exts[@]}"; do specs+=(":(icase)content/*.$e"); done
new=$(git ls-files -- "${specs[@]}" \
  | sort -u | comm -23 - <(sort -u tools/media-allowlist.txt))
if [ -n "$new" ]; then
  echo "::error::media files (${exts[*]}) under content/ must be Release assets, not git files:"
  echo "$new"
  echo "Run: python3 tools/publish_post_media.py <post bundle dir>"
  exit 1
fi
echo "OK: no new media files under content/"
