import urllib.request
import re
import json

urls = [
    "https://slashmaster6.gumroad.com/l/etf-dashboard",
    "https://slashmaster6.gumroad.com/l/diwoc",
    "https://slashmaster6.gumroad.com/l/vzalgb",
    "https://slashmaster6.gumroad.com/l/feishu-templates",
    "https://slashmaster6.gumroad.com/l/cowork-pro",
    "https://slashmaster6.gumroad.com/l/ship-with-ai",
    "https://slashmaster6.gumroad.com/l/kuvajr",
    "https://slashmaster6.gumroad.com/l/bppdqp",
    "https://slashmaster6.gumroad.com/l/xohjh",
    "https://slashmaster6.gumroad.com/l/xfhfps",
    "https://slashmaster6.gumroad.com/l/mgtpcn"
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
        match = re.search(r'"price":(\d+(?:\.\d+)?)', html)
        if match:
            print(f"{url}: ${match.group(1)}")
        else:
            print(f"{url}: PRICE NOT FOUND")
    except Exception as e:
        print(f"{url}: ERROR {e}")
