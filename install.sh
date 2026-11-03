#!/usr/bin/env bash
# 小煤球 IP Studio(xiaomeiqiu-ip-studio)· 安装 / 自检
#   bash install.sh                 交互式
#   bash install.sh --with-xiaohu   额外拉取上游最新版小互角色库到 vendor/(仓库已自带 cast-xiaohu/,可不装)
set -euo pipefail
cd "$(dirname "$0")"
command -v python3 >/dev/null 2>&1 || { echo "✗ 需要 python3"; exit 1; }
echo "✓ $(python3 --version 2>&1)"
with_xiaohu=""
for a in "$@"; do [[ "$a" == "--with-xiaohu" ]] && with_xiaohu="y"; done
if [[ -z "$with_xiaohu" && -t 0 ]]; then
  read -r -p "拉取上游最新版小互角色库吗?(仓库已自带 31 个,一般不需要)  [y/N] " with_xiaohu
fi
if [[ "${with_xiaohu:-N}" =~ ^[Yy]$ ]]; then python3 scripts/studio.py cast install || echo "! 角色库安装失败,稍后可重试: python3 scripts/studio.py cast install"; fi
if [[ -t 0 ]]; then
  read -r -p "现在配置生图 API key 吗?(只做分析/用内置生图工具可跳过) [y/N] " ans
  if [[ "${ans:-N}" =~ ^[Yy]$ ]]; then python3 scripts/studio.py init; fi
fi
python3 scripts/studio.py doctor || true
echo "✓ 完成。对 agent 说「帮我拆解这篇文章的配图方案」即可开始;多 IP 示例见 examples/ensemble-demo.md。"
