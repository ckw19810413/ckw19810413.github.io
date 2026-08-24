import os
from deep_translator import GoogleTranslator

LANG_MAP = {
    'en': 'en',
    'es': 'es',
    'ja': 'ja',
    'zh-cn': 'zh-CN',
    'zh-tw': 'zh-TW'
}

missing = [
    ("content/post/automate-your-workflow-5-ai-workflows-2026", "zh-tw", ["en", "es", "ja"]),
    ("content/post/digital-product-launch-strategy-1000-users", "zh-tw", ["es"]),
    ("content/post/local-ai-infrastructure-guide", "zh-tw", ["es"]),
    ("content/post/multi-agent-business-solo-to-agency", "zh-tw", ["es", "ja"]),
    ("content/post/no-code-business-build-digital-product-ai", "zh-tw", ["ja"]),
    ("content/post/no-code-website-builder-comparison-2026", "zh-tw", ["en", "es", "ja"]),
    ("content/post/obsidian-cellar-hnsw", "zh-cn", ["zh-tw"]),
    ("content/post/one-hundred-years-of-solitude", "md", ["en", "es", "ja", "zh-cn", "zh-tw"]),
    ("content/post/priority-inversion-fable", "zh-cn", ["zh-tw"]),
    ("content/post/solopreneur-ai-tool-stack-2026", "zh-tw", ["es", "ja"]),
    ("content/post/speculative-decoding-fable", "zh-cn", ["zh-tw"]),
]

def safe_translate(translator, text):
    try:
        res = translator.translate(text)
        return res if res is not None else text
    except Exception:
        return text

def translate_markdown(content, target_lang, source_lang='auto'):
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    
    parts = content.split('---\n', 2)
    if len(parts) >= 3:
        frontmatter = parts[1]
        body = parts[2]
    else:
        frontmatter = ""
        body = content

    new_frontmatter = ""
    for line in frontmatter.split('\n'):
        if line.startswith('title:') or line.startswith('description:') or line.startswith('summary:'):
            key, val = line.split(':', 1)
            val = val.strip().strip('"').strip("'")
            if val:
                translated_val = safe_translate(translator, val)
                new_frontmatter += f'{key}: "{translated_val}"\n'
            else:
                new_frontmatter += line + '\n'
        else:
            new_frontmatter += line + '\n'

    paragraphs = body.split('\n\n')
    for i, p in enumerate(paragraphs):
        if not p.strip() or p.startswith('```') or p.startswith('<') or p.startswith('!['):
            continue
        if len(p) < 4500:
            paragraphs[i] = safe_translate(translator, p)

    new_body = '\n\n'.join(paragraphs)
    
    if frontmatter:
        return f"---\n{new_frontmatter}---\n{new_body}"
    return new_body

for folder, src_ext, missing_exts in missing:
    src_file = f"{folder}/index.{src_ext}.md" if src_ext != "md" else f"{folder}/index.md"
    if not os.path.exists(src_file):
        src_file = f"{folder}/index.md"
    
    if not os.path.exists(src_file):
        continue
        
    with open(src_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for ext in missing_exts:
        target_file = f"{folder}/index.{ext}.md"
        # Only translate if not already translated by previous script or it's empty
        if os.path.exists(target_file) and os.path.getsize(target_file) > 100:
            continue
        print(f"Translating {src_file} -> {target_file}")
        
        target_lang = LANG_MAP.get(ext, 'en')
        translated = translate_markdown(content, target_lang)
        
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(translated)

print("Done translating missing files!")
