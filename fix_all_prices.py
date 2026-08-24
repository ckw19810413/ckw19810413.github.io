import os
import re

content_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")

products = {
    "etf-dashboard": "29",
    "diwoc": "39",
    "vzalgb": "69",
    "feishu-templates": "29",
    "xohjh": "29",
    "cowork-pro": "59",
    "xfhfps": "59",
    "ship-with-ai": "39",
    "mgtpcn": "39",
    "kuvajr": "99.99",
    "bppdqp": "49",
}

def update_line(line):
    # check which product is in the line
    for prod, new_price in products.items():
        if f"gumroad.com/l/{prod}" in line:
            # We found a product link in this line. Replace prices.
            # Replace $XX or $XX.XX
            line = re.sub(r'\$[0-9]+(?:\.[0-9]{1,2})?', f'${new_price}', line)
            # Replace XX 美元
            line = re.sub(r'[0-9]+(?:\.[0-9]{1,2})?\s*美元', f'{new_price} 美元', line)
            # Replace XX USD
            line = re.sub(r'[0-9]+(?:\.[0-9]{1,2})?\s*USD', f'{new_price} USD', line)
    return line

changed_files = 0

for root, dirs, files in os.walk(content_dir):
    for filename in files:
        if filename.endswith(".md"):
            filepath = os.path.join(root, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            new_lines = []
            changed = False
            for line in lines:
                new_line = update_line(line)
                new_lines.append(new_line)
                if new_line != line:
                    changed = True
            
            if changed:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.writelines(new_lines)
                print(f"Updated {filepath}")
                changed_files += 1

print(f"Total files updated: {changed_files}")
