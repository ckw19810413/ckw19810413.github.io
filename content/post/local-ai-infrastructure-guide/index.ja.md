---
title: "ローカルAIインフラ構築ガイド：ゼロから vLLM + ComfyUI まで"
description: "2026年にローカルAIインフラを構築する完全ガイド。LLM推論のための vLLM、画像生成のための ComfyUI をデプロイし、GPUメモリを管理し、サービスを自動化し、Cowork MCP マルチエージェントフレームワークと統合します。"
slug: "local-ai-infrastructure-guide"
layout: "single"
summary: "単一GPUマシン上にローカルAIインフラを構築する完全実践ガイド。vLLM のデプロイ、ComfyUI のインストール、メモリ管理、サービスの自動化、マルチエージェントフレームワークとの統合を網羅します。"
publishDate: 2026-07-27
updatedDate: 2026-07-27
categories:
  - "AIインフラ"
  - "実践チュートリアル"
tags:
  - "ローカルAI"
  - "vLLM"
  - "ComfyUI"
  - "AIデプロイ"
  - "GPU最適化"
  - "機械学習"
  - "AIツールチェーン"
  - "Docker"
draft: false
---

## なぜローカルAIインフラを構築するのか？

2026年、AIツールは開発者・クリエイター・企業にとって不可欠なインフラになりました。しかし、多くの人は依然としてクラウドAPIに依存しています——呼び出しごとに課金され、データプライバシーのリスクを負い、レート制限に突き当たっています。

ローカルAIインフラは、あなたに3つのものを与えます。**完全な制御、無制限の利用、そしてゼロの限界費用**です。

構築すれば、次のことができます。
- LLMを制限なく使う。API料金なし
- 機密データをマシンの外に出さずに処理する
- 複数のサービスを同時に実行する。レート制限なし
- Cowork MCP のようなフレームワークと統合し、真のマルチエージェントシステムを構築する

このガイドは、GPU 搭載のマシン（DGX GB10、RTX 4090、あるいはそれ以上を推奨）をお持ちであることを前提とします。ゼロから完全なローカルAI環境を構築する流れを案内します。

**このガイドで学べること：**

- ローカルLLMサービング（vLLM）のインストールと設定
- 画像生成のための ComfyUI のデプロイ
- GPUメモリとサービスの起動順序の管理
- サービス管理の自動化（systemd）
- マルチエージェントAIチームのための Cowork MCP との統合

さっそく始めましょう。

---

## 前提条件

始める前に、次を用意してください。

| 項目 | バージョン | 確認コマンド |
|------|---------|---------------|
| **Linux** | Ubuntu 22.04+ または Arch | `uname -a` |
| **GPU** | NVIDIA RTX 3090+/4090/GB10 | `nvidia-smi` |
| **CUDA** | ≥ 12.4 | `nvcc --version` |
| **Docker** | ≥ 24.0 | `docker --version` |
| **Node.js** | ≥ 20 | `node --version` |
| **Python** | ≥ 3.10 | `python3 --version` |

GPUのメモリが24GB未満の場合は、開始前に不要なGUIアプリやサービスを閉じることを検討してください。

---

## ステップ1：Docker と NVIDIA Container Toolkit のインストール

Docker はローカルAIサービスをデプロイする推奨手段です。依存関係を分離し、バージョン衝突を避け、システムの汚染を防ぐからです。

```bash
# Docker のインストール
sudo apt update
sudo apt install -y docker.io docker-compose-v2

# NVIDIA Container Toolkit のインストール（Docker 内での GPU アクセスを有効化）
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt update
sudo apt install -y nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

GPU が利用可能か検証します。

```bash
docker run --rm --gpus all nvidia/cuda:12.4.0-base-ubuntu22.04 nvidia-smi
```

GPU 情報とメモリ使用量が表示されれば、環境は正しく設定されています。

---

## ステップ2：vLLM ローカル言語モデルのデプロイ

vLLM は現在、最も効率的なローカルLLM推論フレームワークで、複数のモデル形式（GGUF、GPTQ、AWQ）をサポートしています。

### 2.1 Docker でデプロイ

```bash
docker run -d \
  --name vllm-server \
  --gpus all \
  -p 8000:8000 \
  -v ~/.cache/huggingface:/root/.cache/huggingface \
  vllm/vllm-openai:latest \
  --model "nvidia/Llama-3.1-Nemotron-70B-Instruct" \
  --gpu-memory-utilization 0.9 \
  --max-model-len 8192
```

**パラメータの説明：**
- `--model`：デプロイするモデル（任意の HuggingFace モデルに置き換え可能）
- `--gpu-memory-utilization`：使用するGPUメモリの割合（0.9 は 90% を意味する）
- `--max-model-len`：最大コンテキスト長

> **注意：** GPUのメモリが80GB未満の場合は、より大きなモデルを試す前に、まず小さなモデル（7B や 13B）から始めてください。

### 2.2 API エンドポイントのテスト

```bash
curl -X POST http://localhost:8000/v1/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "nvidia/Llama-3.1-Nemotron-70B-Instruct",
    "prompt": "Explain what a multi-agent AI system is",
    "max_tokens": 200
  }'
```

応答が返ってくれば、vLLM のデプロイは成功です。

### 2.3 システムサービスとして設定（自動起動）

systemd サービスファイルを作成します。

```bash
sudo tee /etc/systemd/system/vllm.service << 'EOF'
[Unit]
Description=vLLM Local LLM Server
After=docker.service
Requires=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/usr/bin/docker start vllm-server
ExecStop=/usr/bin/docker stop vllm-server

[Install]
WantedBy=multi-user.target
EOF
```

サービスを有効化して起動します。

```bash
sudo systemctl daemon-reload
sudo systemctl enable vllm.service
sudo systemctl start vllm.service
```

---

## ステップ3：ComfyUI 画像生成のデプロイ

ComfyUI は最も強力なローカル画像生成ツールで、Flux、Stable Diffusion、LTX、その他さまざまなモデルをサポートしています。

### 3.1 Docker でデプロイ

```bash
docker run -d \
  --name comfyui \
  --gpus all \
  -p 8188:8188 \
  -v ~/.cache/huggingface:/root/.cache/huggingface \
  -v ~/comfyui-output:/output \
  ghcr.io/ai-forest/comfyui:latest
```

これで ComfyUI が `http://localhost:8188` で起動します。

### 3.2 手動インストール（上級者向けの選択肢）

より細かい制御が必要なら、手動でインストールできます。

```bash
# ComfyUI リポジトリのクローン
cd ~/comfyui
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI

# 依存関係のインストール
pip install -r requirements.txt

# カスタムノードのインストール（任意）
git clone https://github.com/Fannovel16/ComfyUI-Frame-Interpolation.git custom_nodes/
git clone https://github.com/laksjdjoy/deforum-comfy.git custom_nodes/

# サービスの起動
python main.py --listen 0.0.0.0 --port 8188
```

### 3.3 よく使うモデルのダウンロード

```bash
# HuggingFace CLI でモデルをダウンロード
pip install huggingface_hub
huggingface-cli download stabilityai/stable-diffusion-xl-base-1.0 --local-dir ~/models/sdxl
huggingface-cli download stabilityai/stable-diffusion-3.5-large --local-dir ~/models/sd3.5
```

---

## ステップ4：GPUメモリ管理の戦略

ローカルでAIサービスを実行するとき、GPUメモリが最大のボトルネックになります。実戦で鍛えられたプラクティスをいくつか紹介します。

### 4.1 利用可能なメモリの確認

```bash
free -h
nvidia-smi --query-gpu=memory.used,memory.free,temperature.gpu --format=csv
```

### 4.2 推奨されるサービスの起動順序

1. **まず vLLM を起動する**（言語モデルは通常、メモリ要件が固定されている）
2. **次に ComfyUI を起動する**（画像生成はメモリ使用量を動的に調整できる）
3. **不要なGUIアプリを閉じる**（ブラウザ、Discord など）

### 4.3 メモリ監視スクリプト

シンプルな監視スクリプトを作成します。

```bash
#!/bin/bash
# monitor-gpu.sh
while true; do
    echo "=== $(date) ==="
    nvidia-smi --query-gpu=memory.used,memory.free,temperature.gpu --format=csv
    docker ps --filter "name=vllm\|name=comfyui" --format "table {{.Names}}\t{{.Status}}"
    sleep 30
done
```

---

## ステップ5：Cowork MCP マルチエージェントフレームワークの統合

ローカルAIインフラが整ったら、それを Cowork MCP に接続してマルチエージェントシステムを構築します。

### 5.1 vLLM をブレインとして登録

```bash
# Hermes Agent を使う場合
hermes register-cowork

# または MCP エンドポイントを手動で設定
# Agent の設定ファイルに：
{
  "mcpServers": {
    "cowork": {
      "url": "http://localhost:6868/mcp",
      "transport": "streamable-http"
    },
    "vllm": {
      "url": "http://localhost:8000/v1",
      "transport": "streamable-http"
    }
  }
}
```

### 5.2 実践応用：ローカルAIコンテンツパイプライン

```
ローカル vLLM（コンテンツ生成） → ComfyUI（画像生成） → ffmpeg（後処理）
```

このパイプラインの各ステップは、異なるAIエージェントによって連携できます。

1. **リサーチエージェント**：vLLM を使ってコンテンツのアウトラインを生成する
2. **ライティングエージェント**：vLLM を使って完全な記事に展開する
3. **画像エージェント**：ComfyUI を使って対応するイラストを生成する
4. **統合エージェント**：コンテンツと画像を最終出力にまとめる

---

## ステップ6：自動化とバックアップ

### 6.1 コンテナのバックアップ

```bash
# ComfyUI コンテナの状態をバックアップ
docker commit comfyui comfyui-backup:$(date +%Y%m%d)

# イメージをエクスポート
docker save comfyui:latest | gzip > ~/backups/comfyui-$(date +%Y%m%d).tar.gz
```

### 6.2 モデルのバックアップ

```bash
# HuggingFace キャッシュを定期的にバックアップ
rsync -avh ~/.cache/huggingface ~/backups/huggingface-cache/

# または rclone でクラウドにバックアップ
rclone sync ~/.cache/huggingface remote:backup-huggingface --progress
```

### 6.3 ヘルスチェックスクリプト

ヘルスチェックの cron ジョブを作成します。

```bash
# 5 分ごとにサービスの状態を確認
*/5 * * * * curl -f http://localhost:8000/v1/models || echo "vLLM is down at $(date)" | mail -s "vLLM Alert" admin@example.com
```

---

## トラブルシューティング

### Q1：Docker が GPU を使えない

```bash
# NVIDIA Container Toolkit がインストールされているか確認
nvidia-ctk runtime verify

# Docker サービスを再起動
sudo systemctl restart docker
```

### Q2：GPUメモリが不足する

```bash
# vLLM のメモリ使用率を下げる
# docker run コマンドに追加：
--gpu-memory-utilization 0.7

# または不要なサービスを停止
sudo systemctl stop bluetooth
```

### Q3：ComfyUI が起動しない

```bash
# Docker のログを確認
docker logs comfyui

# 再起動を試す
docker restart comfyui
```

### Q4：モデルのダウンロードが遅い

```bash
# HuggingFace ミラーを使う（中国本土のユーザー向け）
export HF_ENDPOINT=https://hf-mirror.com
```

---

## 次に来るもの

これで完全なローカルAIインフラが手に入りました。

**今日：**
- vLLM と ComfyUI が稼働していることを確認する
- API エンドポイントをテストし、コンテンツと画像の生成が機能することを検証する

**今週：**
- 起動時に自動起動するよう systemd サービスを設定する
- バックアップと監視の仕組みを作成する
- 少なくとも一つのLLMバックエンドを Cowork MCP に接続する

**今月：**
- より多くのAIエージェントチームのために [Cowork MCP フレームワーク](https://github.com/slashman413/cowork) を探索する
- さまざまなモデルを試し、自分のニーズに最適な構成を見つける
- 自分だけのAIコンテンツ制作パイプラインを構築する

---

## FAQ

**Q：これらのサービスを実行するにはどの程度のGPUが必要ですか？**
A：少なくとも24GBのメモリを推奨します（RTX 3090/4090）。メモリがそれより小さい場合は、より小さなモデル（7B〜13B）を実行するか、Docker のメモリ制限を使えます。

**Q：GPUのないマシンでも実行できますか？**
A：はい、ただし遅くなります。CPU 推論は可能ですが、大規模モデル（70B以上）には実用的ではありません。

**Q：モデルはどう更新しますか？**
A：HuggingFace CLI を使います：`huggingface-cli download <model-name> --local-dir <path>`。Docker コンテナは更新されたローカルモデルを自動的に使用します。

**Q：vLLM と Ollama の違いは？**
A：vLLM は高スループット推論に最適化されており、より多くのモデル形式と高度な機能をサポートします。Ollama はより軽量で使いやすいものの、機能は少なめです。ローカルAIインフラには vLLM を推奨します。

**Q：ComfyUI は Automatic1111 とどう違いますか？**
A：ComfyUI はノードベースのワークフローを採用しており、より柔軟で効率的です。Automatic1111 は初心者に優しいGUIを備えています。どちらもよく機能しますが、本番環境では ComfyUI のほうが人気です。

---

*読了時間：約15分 | 公開：2026-07-27*

*このガイドが役に立ちましたか？[Slashman Tools](/en/) でさらに多くのガイドを見るか、すぐ使える構成は [AIツールチェーンテンプレートライブラリ](https://gumroad.com/l/diwoc) をチェックしてください。*

[[- ホームに戻る](/en/)]
