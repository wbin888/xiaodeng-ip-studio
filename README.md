# 小灯 IP Studio · 拆解式配图

> 小黑的拆法(怎么拆) + 小互的工具箱(拆得全、画得准、生得出) + 原创 IP 小灯(谁来演)。

一个给 AI agent(Claude Code / Codex / Copilot 等)用的中文正文配图技能,融合了:

- [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations):怪诞手绘风格、**认知锚点 → shot list → 原创隐喻**的拆解方式(小黑方法)。
- [xiaohuailabs/xiaohu-ip-studio](https://github.com/xiaohuailabs/xiaohu-ip-studio):逐节枚举、深层提炼、三轨分流、隐喻对照、比例规则、生图脚本、角色库。

## 它做什么

1. **像小黑一样拆解**:读透文章 → 定全文主张 → 逐节判“配 / 不配” → 挑认知锚点 → 每张图写出灵魂话、小灯动作、隐喻对照和必现内容 → 输出一份配图拆解方案。
2. **按需生成**:你说“生成”,它直接按方案逐张出图(小灯出演,纯白手绘、少量红橙蓝批注、大量留白)。
3. **自检迭代**:按 QA 清单检查选点、机制准确性、小灯是否在干活、是否像 PPT。

## IP:小灯

![小灯设定稿](assets/xiaodeng-sheet.png)

一个**灯泡头的细线小人**:无眼无嘴,**灯丝就是表情,亮度就是状态**——想通就亮、卡住就灭、拿不准就闪。会接线、拔插头、调光、照亮盲点、串成一串灯标进度。认真、有点轴、不卖萌。完整设定见 `references/xiaodeng-ip.md`。

## 两种用法

| 你说 | 它做 |
|---|---|
| “帮我拆解这篇的配图方案” / “分析哪里需要配图” | 只输出拆解方案(逐节判定 + shot list),停下 |
| “给这篇生成配图” / “帮我做图” | 内部拆解后直接逐张生成并交付 |

## 和两个原技能的区别

| | 小黑原版 | 小互原版 | 本技能 |
|---|---|---|---|
| 拆解口径 | 简洁、决断 | 详尽、多道闸门 | 小黑口径输出,小互闸门在草稿里跑 |
| 防漏配 | 凭判断挑锚点 | 逐节枚举 | 逐节枚举 + 锚点清单 |
| 防画错 | — | 深读 Q4 + 隐喻对照 | 保留 |
| 图类型 | 8 种结构 | 三轨 + 海报 | 10 种结构 × 三轨 + 可选海报 |
| 演员 | 小黑 | 31 个角色(需选) | 默认原创 IP 小灯,可选换角 |
| 生成前确认 | 不停 | 必停选角选风格 | 分析就停,生成就不停 |
| 比例 | 16:9 | 按内容形状,封顶 4:3 | 按渠道:桌面 16:9,移动端按形状 |
| 生图 | 内置 `image_gen` | 自带脚本 | 内置工具优先,脚本兜底,另加比例校验与 `--dry-run` |

## 安装

```bash
git clone https://github.com/wbin888/xiaodeng-ip-studio ~/.claude/skills/xiaodeng-ip-studio
cd ~/.claude/skills/xiaodeng-ip-studio && bash install.sh
```

只做分析、或 agent 自带生图工具时,不需要配置 API key。

## 目录

```text
SKILL.md                     流程骨架
references/
  analysis-playbook.md       拆解方法本体
  plan-template.md           方案输出格式 + 示例
  metaphor-method.md         现编隐喻 + 对照表 + 反复刻
  xiaodeng-ip.md              小灯 IP + 嵌入法则
  style-dna.md               风格、颜色语义、比例
  tracks.md                  情绪 / 解释 / 四格 / 海报
  prompt-template.md         各轨 prompt 骨架
  qa-checklist.md            自检与迭代
  cast-swap.md               换角与角色包安全
  backends.md                生图后端
scripts/
  generate.py                生图(OpenAI 兼容端点,纯标准库)
  studio.py                  init / doctor
agents/openai.yaml           Codex agent 元数据
```

## 换角

默认小灯。想让小互角色库里的角色出演,先安装 [xiaohu-ip-studio](https://github.com/xiaohuailabs/xiaohu-ip-studio)(放在同级目录或设置 `XIAOHU_STUDIO_DIR`),再说“这篇用牛马出演”。详见 `references/cast-swap.md`。

## 许可与署名

MIT。小灯为本技能原创 IP;拆解方法源自 Ian 小黑;小互角色与画风 © 小互(本仓库不含角色图)。详见 `NOTICE.md`。
