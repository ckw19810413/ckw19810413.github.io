---
date: '{{ .Date }}'
draft: true
title: '{{ replace .File.ContentBaseName "-" " " | title }}'
description: ''
slug: ''
tags: []
categories: []
---

<!--
5語言發文工作流程：

# 預設 zh-tw（繁體中文）
hugo new content post/my-post/index.md

# 新增其他語言翻譯
cp content/post/my-post/index.md content/post/my-post/index.zh.md
cp content/post/my-post/index.md content/post/my-post/index.ja.md
cp content/post/my-post/index.md content/post/my-post/index.es.md

# 英文放 content/en/posts/
hugo new content content/en/posts/my-post.md
-->
