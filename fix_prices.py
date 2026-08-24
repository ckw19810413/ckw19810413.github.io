import os
import re

dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content/page/reviews")

replacements = [
    (r'\[(.*?)\]\(https://slashmaster6\.gumroad\.com/l/etf-dashboard\)\s*\|\s*\$\d+\s*\|', r'[\1](https://slashmaster6.gumroad.com/l/etf-dashboard) | $29 |'),
    (r'\[(.*?)\]\(https://slashmaster6\.gumroad\.com/l/diwoc\)\s*\|\s*\$\d+\s*\|', r'[\1](https://slashmaster6.gumroad.com/l/diwoc) | $39 |'),
    (r'\[(.*?)\]\(https://slashmaster6\.gumroad\.com/l/vzalgb\)\s*\|\s*\$\d+\s*\|', r'[\1](https://slashmaster6.gumroad.com/l/vzalgb) | $69 |'),
    (r'\[(.*?)\]\(https://slashmaster6\.gumroad\.com/l/xohjh\)\s*\|\s*\$\d+\s*\|', r'[\1](https://slashmaster6.gumroad.com/l/feishu-templates) | $29 |'),
    (r'\[(.*?)\]\(https://slashmaster6\.gumroad\.com/l/xfhfps\)\s*\|\s*\$\d+\s*\|', r'[\1](https://slashmaster6.gumroad.com/l/cowork-pro) | $59 |'),
    (r'\[(.*?)\]\(https://slashmaster6\.gumroad\.com/l/mgtpcn\)\s*\|\s*\$\d+\s*\|', r'[\1](https://slashmaster6.gumroad.com/l/ship-with-ai) | $39 |'),
    (r'\[(.*?)\]\(https://slashmaster6\.gumroad\.com/l/kuvajr\)\s*\|\s*\$\d+\s*\|', r'[\1](https://slashmaster6.gumroad.com/l/kuvajr) | $99.99 |'),
    (r'\[(.*?)\]\(https://slashmaster6\.gumroad\.com/l/bppdqp\)\s*\|\s*\$\d+\s*\|', r'[\1](https://slashmaster6.gumroad.com/l/bppdqp) | $49 |'),
]

for filename in os.listdir(dir_path):
    if filename.endswith(".md"):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content
        for pattern, replacement in replacements:
            new_content = re.sub(pattern, replacement, new_content)
            
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
