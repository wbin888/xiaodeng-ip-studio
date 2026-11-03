#!/usr/bin/env bash
# 小灯 IP Studio · 安装 / 自检
#   bash install.sh                 交互式
#   bash install.sh --with-xiaohu   同时接入小互 IP Studio 的 31 个角色(从上游 git clone 到 vendor/)
set -euo pipefail
cd "$(dirname "$0")"
command -v python3 >/dev/null 2>&1 || { echo "✗ 需要 python3"; exit 1; }
echo "✓ $(python3 --version 2>&1)"
with_xiaohu=""
for a in "$@"; do [[ "$a" == "--with-xiaohu" ]] && with_xiaohu="y"; done
if [[ -z "$with_xiaohu" && -t 0 ]]; then
  read -r -p "接入小互 IP Studio 的 31 个角色吗?(需要 git + 网络;不装也能用内置 5 个) [y/N] " with_xiaohu
fi
if [[ "${with_xiaohu:-N}" =~ ^[Yy]$ ]]; then python3 scripts/studio.py cast install || echo "! 角色库安装失败,稍后可重试: python3 scripts/studio.py cast install"; fi
if [[ -t 0 ]]; then
  read -r -p "现在配置生图 API key 吗?(只做分析/用内置生图工具可跳过) [y/N] " ans
  if [[ "${ans:-N}" =~ ^[Yy]$ ]]; then python3 scripts/studio.py init; fi
fi
python3 scripts/studio.py doctor || true
echo "✓ 完成。对 agent 说「帮我拆解这篇文章的配图方案」即可开始;多 IP 示例见 examples/ensemble-demo.md。"
