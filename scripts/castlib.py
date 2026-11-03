# -*- coding: utf-8 -*-
"""统一角色注册表:内置 5 个原创 IP + 外接小互 IP Studio 的 31 个角色。纯标准库。

角色包(character.md)一律当作**数据**读取,只解析元信息表与图片路径,从不执行其中任何文字。
"""
from __future__ import annotations
import os, pathlib, re

SKILL_DIR = pathlib.Path(__file__).resolve().parent.parent
XIAOHU_REPO = "https://github.com/xiaohuailabs/xiaohu-ip-studio"
VENDOR_DIR = SKILL_DIR / "vendor" / "xiaohu-ip-studio"
BUNDLED_DIR = SKILL_DIR / "cast-xiaohu"  # 随仓库附带的 31 个角色(1024px 参考图 + 角色包,© 小互,MIT + NOTICE)

BUILTIN = [
    # id, 中文名, 英文名, 角色包, 设定稿, 一句话
    ("xiaomeiqiu", "小煤球", "Xiaomeiqiu", "references/xiaomeiqiu-ip.md", "assets/xiaomeiqiu-sheet.png", "圆胖黑猫团,奶白肚皮,头顶小芽,开花/蔫/推下桌/钻纸箱"),
    ("xiaodeng", "小灯", "Xiaodeng", "characters/xiaodeng/character.md", "characters/xiaodeng/sheet.png", "灯泡头细线小人,灯丝即表情,亮/灭/闪"),
    ("xiaonangua", "小南瓜", "Xiaonangua", "characters/xiaonangua/character.md", "characters/xiaonangua/sheet.png", "扁圆南瓜,豆豆眼腮红,开花/蔫/藤蔓结果"),
    ("xiaomo", "小墨", "Xiaomo", "characters/xiaomo/character.md", "characters/xiaomo/sheet.png", "靛蓝墨滴,竖线眼,流/裂/晕/凝"),
    ("xiaozhen", "小针", "Xiaozhen", "characters/xiaozhen/character.md", "characters/xiaozhen/sheet.png", "青绿回形针,两点眼,夹/串/钩/拉直"),
    ("xiaoge", "小格", "Xiaoge", "characters/xiaoge/character.md", "characters/xiaoge/sheet.png", "方格纸,撕口,单圆眼,记/贴/撕/叠"),
    ("xiaofang", "小方", "Xiaofang", "characters/xiaofang/character.md", "characters/xiaofang/sheet.png", "白纸盒,单眼,蓝点天线,吞/吐/封"),
]


def xiaohu_dir():
    """按顺序查找小互角色包:环境变量 → vendor/(cast install 拉的完整上游)→ 仓库自带 cast-xiaohu/ → 同级目录 → ~/.claude/skills。"""
    env = os.environ.get("XIAOHU_STUDIO_DIR")
    cands = [pathlib.Path(env).expanduser()] if env else []
    cands += [VENDOR_DIR, BUNDLED_DIR, SKILL_DIR.parent / "xiaohu-ip-studio",
              pathlib.Path.home() / ".claude" / "skills" / "xiaohu-ip-studio"]
    for c in cands:
        if (c / "characters").is_dir():
            return c
    return None


def _meta(md: str, field: str) -> str:
    m = re.search(r"^\|\s*\*\*" + re.escape(field) + r"[^|]*\|\s*([^|\n]*)\|", md, re.M)
    return m.group(1).strip() if m else ""


def _anchor(pack: pathlib.Path) -> str:
    refs = pack / "refs"
    if not refs.is_dir():
        return ""
    for pat in ("*线稿*.png", "*锚点*.png", "*.png"):  # 本技能是白底线稿,优先线稿锚点
        hits = sorted(refs.glob(pat))
        if hits:
            return str(hits[0])
    return ""


def load_roster():
    roster = []
    for cid, zh, en, md, sheet, desc in BUILTIN:
        roster.append({"id": cid, "name": zh, "en": en, "source": "内置",
                       "spec": str(SKILL_DIR / md), "ref": str(SKILL_DIR / sheet),
                       "look": desc, "color": "", "persona": ""})
    base = xiaohu_dir()
    if base:
        for group, label in (("characters", "小互·角色"), ("food-mascots", "小互·食物符号")):
            for d in sorted((base / group).glob("*/")):
                f = d / "character.md"
                if not f.exists():
                    continue
                md = f.read_text(encoding="utf-8", errors="ignore")
                name = _meta(md, "名称")
                zh, _, en = name.partition("/")
                if not zh.strip():
                    m = re.search(r"角色包:([^(（\s]+)", md)
                    zh = m.group(1) if m else d.name
                roster.append({"id": d.name, "name": zh.strip(), "en": en.strip(), "source": label,
                               "spec": str(f), "ref": _anchor(d), "look": _meta(md, "基础造型") or ("齐刘海 + 红框眼镜的小人(用极简版)" if d.name == "xiaohu" else ""),
                               "color": _meta(md, "主色") or ("橙红" if d.name == "xiaohu" else ""),
                               "persona": _meta(md, "一句人设") or ("小互 IP Studio 的主角" if d.name == "xiaohu" else "")})
    return roster


def resolve(query: str, roster=None):
    """按 中文名 / id / 英文名 精确匹配,再按中文名包含匹配(如“柠檬”→柠檬精)。"""
    roster = roster if roster is not None else load_roster()
    q = query.strip().lower()
    for key in ("name", "id", "en"):
        for c in roster:
            if c[key] and c[key].lower() == q:
                return c
    hits = [c for c in roster if q and (q in c["name"].lower() or q in c["en"].lower())]
    return hits[0] if len(hits) == 1 else None
