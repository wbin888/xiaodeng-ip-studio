#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""xiaodeng-ip-studio CLI:init(填 key) / doctor(自检) / cast(角色库:list / show / install)。纯标准库。改编自 xiaohu-ip-studio 的 illo.py(MIT)。"""
from __future__ import annotations
import getpass, os, pathlib, shutil, subprocess, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import castlib  # noqa: E402

CONFIG_DIR = pathlib.Path(os.environ.get("XDG_CONFIG_HOME", str(pathlib.Path.home() / ".config"))) / "xiaodeng-ip-studio"
CONFIG_PATH = CONFIG_DIR / "config.yaml"
SKILL_DIR = pathlib.Path(__file__).resolve().parent.parent

REQUIRED_REFS = [
    "analysis-playbook.md", "plan-template.md", "metaphor-method.md", "xiaodeng-ip.md",
    "style-dna.md", "tracks.md", "prompt-template.md", "qa-checklist.md", "cast-swap.md", "backends.md",
    "cast-roster.md", "ensemble.md",
]


def cmd_init():
    print("=== xiaodeng-ip-studio 配置生图 ===")
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


def cmd_cast(argv):
    sub = argv[0] if argv else "list"
    if sub == "install":
        dest = pathlib.Path(argv[1]).expanduser() if len(argv) > 1 else castlib.VENDOR_DIR
        if not shutil.which("git"):
            print("[错误] 需要 git。也可手动下载 " + castlib.XIAOHU_REPO + " 并设置 XIAOHU_STUDIO_DIR。")
            sys.exit(2)
        if (dest / ".git").is_dir():
            print(f"[*] 已安装,更新: {dest}")
            r = subprocess.run(["git", "-C", str(dest), "pull", "--ff-only", "-q"])
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            print(f"[*] 下载小互角色库 → {dest}")
            r = subprocess.run(["git", "clone", "--depth", "1", "-q", castlib.XIAOHU_REPO, str(dest)])
        if r.returncode != 0:
            print("[错误] git 失败,检查网络后重试。")
            sys.exit(1)
        if dest != castlib.VENDOR_DIR:
            print(f"[提示] 装在非默认位置,请设置: export XIAOHU_STUDIO_DIR={dest}")
        n = sum(1 for c in castlib.load_roster() if c["source"] != "内置")
        print(f"✅ 小互角色库就绪({n} 个角色)。角色形象与画风 © 小互,仅按其 MIT + NOTICE 条款使用,本仓库不再分发。")
        return
    roster = castlib.load_roster()
    if sub == "list":
        cur = None
        for c in roster:
            if c["source"] != cur:
                cur = c["source"]
                print(f"\n[{cur}]")
            extra = f" · {c['persona']}" if c["persona"] else ""
            ok = "✓" if c["ref"] and pathlib.Path(c["ref"]).exists() else "·"
            print(f"  {ok} {c['name']:<6} ({c['id']}) {c['look']}{extra}")
        if not castlib.xiaohu_dir():
            print("\n[*] 小互角色库未安装:python3 scripts/studio.py cast install")
        return
    if sub == "show" and len(argv) > 1:
        for q in argv[1:]:
            c = castlib.resolve(q, roster)
            if not c:
                print(f"[!!] 找不到角色「{q}」(先 cast list;小互角色需先 cast install)")
                continue
            print(f"{c['name']} ({c['id']}) · {c['source']}\n  角色包: {c['spec']}\n  参考图: {c['ref'] or '无'}"
                  + (f"\n  主色: {c['color']}" if c["color"] else ""))
        return
    print("用法: studio.py cast [list | show <角色名...> | install [目录]]")
    sys.exit(2)


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
    roster = castlib.load_roster()
    builtin = [c for c in roster if c["source"] == "内置"]
    bad = [c["name"] for c in builtin if not (pathlib.Path(c["spec"]).exists() and pathlib.Path(c["ref"]).exists())]
    print(f"[{'OK' if not bad else '!!'}] 内置角色库: {len(builtin)} 个(" + "、".join(c["name"] for c in builtin) + ")" + (f" 缺文件: {bad}" if bad else ""))
    ok = ok and not bad
    pack = castlib.xiaohu_dir()
    if pack:
        ext = [c for c in roster if c["source"] != "内置"]
        noref = [c["name"] for c in ext if not c["ref"]]
        print(f"[OK] 小互角色库: {pack}({len(ext)} 个角色)" + (f";无参考图: {noref}" if noref else ""))
    else:
        print("[*] 小互角色库: 未安装(可选;python3 scripts/studio.py cast install)")
    print("=== " + ("✅ 就绪" if ok else "❌ 有问题,见上") + " ===")
    sys.exit(0 if ok else 1)


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "doctor"
    if cmd == "init":
        cmd_init()
    elif cmd == "doctor":
        cmd_doctor()
    elif cmd == "cast":
        cmd_cast(sys.argv[2:])
    else:
        print("用法: python3 scripts/studio.py [init | doctor | cast list | cast show <角色名...> | cast install [目录]]")
        sys.exit(2)


if __name__ == "__main__":
    main()
