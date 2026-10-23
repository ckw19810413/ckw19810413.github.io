#!/usr/bin/env bash
# Fail if git tracks an *.mp4 / *.zip under content/ that is not grandfathered in
# tools/media-allowlist.txt (files committed before the rule, 2026-10-23; history
# is not rewritten). Publish new media with tools/publish_post_media.py instead.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
new=$(git ls-files -- 'content/*.mp4' 'content/*.zip' \
  | sort -u | comm -23 - <(sort -u tools/media-allowlist.txt))
if [ -n "$new" ]; then
  echo "::error::mp4/zip files under content/ must be Release assets, not git files:"
  echo "$new"
  echo "Run: python3 tools/publish_post_media.py <post bundle dir>"
  exit 1
fi
echo "OK: no new mp4/zip under content/"
