#!/usr/bin/env bash
# 小灯 IP Studio · 安装 / 自检
set -euo pipefail
cd "$(dirname "$0")"
command -v python3 >/dev/null 2>&1 || { echo "✗ 需要 python3"; exit 1; }
echo "✓ $(python3 --version 2>&1)"
read -r -p "现在配置生图 API key 吗?(只做分析/用内置生图工具可跳过) [y/N] " ans
if [[ "${ans:-N}" =~ ^[Yy]$ ]]; then python3 scripts/studio.py init; fi
python3 scripts/studio.py doctor || true
echo "✓ 完成。对 agent 说「帮我拆解这篇文章的配图方案」即可开始。"
