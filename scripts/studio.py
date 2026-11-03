#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""xiaofang-ip-studio CLI:init(填 key) / doctor(自检)。纯标准库。改编自 xiaohu-ip-studio 的 illo.py(MIT)。"""
from __future__ import annotations
import getpass, os, pathlib, sys

CONFIG_DIR = pathlib.Path(os.environ.get("XDG_CONFIG_HOME", str(pathlib.Path.home() / ".config"))) / "xiaofang-ip-studio"
CONFIG_PATH = CONFIG_DIR / "config.yaml"
SKILL_DIR = pathlib.Path(__file__).resolve().parent.parent

REQUIRED_REFS = [
    "analysis-playbook.md", "plan-template.md", "metaphor-method.md", "xiaofang-ip.md",
    "style-dna.md", "tracks.md", "prompt-template.md", "qa-checklist.md", "cast-swap.md", "backends.md",
]


def cmd_init():
    print("=== xiaofang-ip-studio 配置生图 ===")
    print(f"配置将写到: {CONFIG_PATH}\n支持任何 OpenAI 兼容图像端点;key 只存本地、永不上传。\n")
    base = input("图像 API base_url [https://api.openai.com/v1]: ").strip() or "https://api.openai.com/v1"
    model = input("图像模型 model [gpt-image-2]: ").strip() or "gpt-image-2"
    key = getpass.getpass("API key (输入时不回显): ").strip()
    if not key:
        print("[中止] 没输入 key。")
        sys.exit(2)
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_text(
        f'base_url: "{base}"\nmodel: "{model}"\napi_key: "{key}"\nimage_size: "1024"\n',
        encoding="utf-8",
    )
    os.chmod(CONFIG_PATH, 0o600)
    print(f"\n✅ 已写入 {CONFIG_PATH} (mode 600)\n  自检: python3 scripts/studio.py doctor")


def _cast_pack_dir():
    env = os.environ.get("XIAOHU_STUDIO_DIR")
    candidates = [pathlib.Path(env)] if env else []
    candidates += [SKILL_DIR.parent / "xiaohu-ip-studio", pathlib.Path.home() / ".claude" / "skills" / "xiaohu-ip-studio"]
    for c in candidates:
        if (c / "characters").is_dir():
            return c
    return None


def cmd_doctor():
    ok = True
    print("=== doctor 自检 ===")
    print(f"[*] python: {sys.version.split()[0]}")
    if CONFIG_PATH.exists():
        txt = CONFIG_PATH.read_text(encoding="utf-8")
        has_key = ("api_key" in txt) and ('api_key: "<' not in txt) and ('api_key: ""' not in txt)
        print(f"[{'OK' if has_key else '*'}] config: {CONFIG_PATH} {'(key 已填)' if has_key else '(缺 key;用脚本生图前跑 init)'}")
    else:
        print(f"[*] 未配置生图脚本: {CONFIG_PATH}(只做分析 / 用内置生图工具可忽略;用脚本生图前跑 init)")
    missing = [r for r in REQUIRED_REFS if not (SKILL_DIR / "references" / r).exists()]
    print(f"[{'OK' if not missing else '!!'}] references: {'齐全' if not missing else '缺 ' + ', '.join(missing)}")
    ok = ok and not missing
    gen = SKILL_DIR / "scripts" / "generate.py"
    print(f"[{'OK' if gen.exists() else '!!'}] 生图脚本: {'在' if gen.exists() else '缺'}")
    ok = ok and gen.exists()
    pack = _cast_pack_dir()
    if pack:
        n = sum(1 for sub in ("characters", "food-mascots") if (pack / sub).is_dir()
                for d in (pack / sub).iterdir() if d.is_dir())
        print(f"[OK] 可选换角包: {pack}({n} 个角色)")
    else:
        print("[*] 可选换角包: 未安装(默认小方出演,不影响使用;见 references/cast-swap.md)")
    print("=== " + ("✅ 就绪" if ok else "❌ 有问题,见上") + " ===")
    sys.exit(0 if ok else 1)


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "doctor"
    if cmd == "init":
        cmd_init()
    elif cmd == "doctor":
        cmd_doctor()
    else:
        print("用法: python3 scripts/studio.py [init|doctor]")
        sys.exit(2)


if __name__ == "__main__":
    main()
