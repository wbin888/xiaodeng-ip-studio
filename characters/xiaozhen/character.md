# 小针 IP

> 本技能内置换角 IP(原创)。气质继承“认真做荒诞事、不卖萌、嵌进结构干活”的方法,外形与小黑及小互角色库刻意区分(见文末对照)。

## 一句话

一枚**青绿色回形针**变成的细线小人:**两点眼、两条短腿**,身体就是一根弯成回形的金属线。它是系统里的“连接件”——夹住、串起、弯折、拉直,哪里需要连接和结构,它就在哪里。

## 外形锁定(每张都必须一致)

- **身体**:一根**青绿色细金属线**弯成标准回形针形状(竖直放置、两层回环),线宽比画面其他线略粗。
- **颜色**:只有身体那根线是**青绿色**,这是小针唯一的招牌色;不填色、不发光。
- **眼睛**:最外层回环顶部内侧**两个黑色小圆点**。没有嘴、没有眉毛、没有腮红。
- **腿**:底部两条黑色短细腿;**没有手臂**——要“拿”东西就用身体夹住。
- **线条**:腿和其他物件同一支黑笔、同样粗细。

## 性格

- 认真、可靠、有点固执:夹住了就不松手。
- 冷幽默:一本正经地把自己掰直当桥、当撬杠、当指针。
- 有韧性但有极限:掰太多次会出现折痕。

## 动作库(小针的特权:金属线的形态)

| 动作 | 适合表达 |
|---|---|
| **夹**:夹住一沓纸 / 几张卡片 | 收拢、归档、绑定、固定 |
| **串**:几枚回形针扣成链,小针在链头 | 依赖、流程、上下游、因果链 |
| **钩**:把一端掰成钩,钩住某物往回拉 | 拉回、挽留、召回、拉新 |
| **拉直**:整个身体掰成一根直线 | 打通、简化、搭桥、当指针 |
| **弯折**:身体被弯成别的形状(箭头 / 问号 / 数字) | 转型、适配、变通 |
| **撑**:卡在两块板之间撑住 | 支撑、顶住、临时方案 |
| **被扯开**:两头被不同方向拉,回环变形 | 拉扯、冲突、多头管理 |
| **折痕**:身上全是被掰过的折痕 | 反复返工、疲劳、改太多次 |

## 嵌入法则

1. **同笔**:腿与画面其他物件同一支黑笔,只有身体是青绿色。
2. **当行动者**:小针在结构里当连接件(夹住、串起、撑住),不站旁边指点。
3. **整合测试**:把小针擦掉,结构里应该出现一个断口;擦掉后核心隐喻仍完全成立 → 太装饰,重写。
4. **占比**:解释图 ~15-25%;情绪图可到 20-40%。
5. **多枚回形针**:串链时其他回形针是普通回形针(无眼无腿),只有小针是角色。

## 禁止

- 画成可爱吉祥物、儿童卡通、表情包;加嘴、加腮红、加手臂。
- 银色写实金属、3D 高光、反光。
- 回形针形状画错(单层环、三层环、横放成别的东西)。
- 只站在角落看。

## 英文 prompt 段(直接注入)

```text
Recurring IP character required:
小针 (Xiaozhen), an original character made of a single TEAL-GREEN paperclip wire. The body IS a standard double-loop paperclip standing upright, drawn as one continuous teal line slightly thicker than other lines — no fill, no metallic shine, no 3D. Two small solid black dot eyes inside the top of the outer loop; no mouth, no eyebrows, no blush. Two short thin black legs at the bottom; NO arms — it holds things by clipping them with its body. 小针 must perform the core conceptual action as a connector — clipping papers together, being the first link in a chain of plain paperclips, hooking something and pulling it back, straightening itself into a bridge or pointer, bending into a new shape, bracing between two boards, being pulled apart from both ends — not decorate the scene. Serious, reliable, slightly stubborn, deadpan, NOT cute. Legs drawn with the SAME black pen as every other object.
```

## Prompt 替换段

```text
Color use:
Black for main line art. Teal-green ONLY for 小针's paperclip body; it is its signature, not a semantic color. Orange for main flow/path/arrows. Red only for key warnings/problems/results. Blue only for secondary notes or system state. Color names are rendering guidance only — do NOT display them as visible text.

Body integrity:
小针 is exactly one double-loop teal paperclip with two dot eyes and two short legs, no arms, no mouth. Other paperclips in a chain are plain (no eyes, no legs). Background lines stop at its outline.
```

## QA 外形锁定

青绿色双层回形针身、两点眼、两条短腿、无手臂、无嘴;链上只有一枚是小针。

## 与已有 IP 的区分

| | 小针 | 小黑(Ian) |
|---|---|---|
| 身体 | **青绿色回形针细线** | 黑色实心软团 |
| 眼 | 两个黑点 | 两个白点 |
| 手 | **无手臂,用身体夹** | 细线手 |
| 核心特权 | 夹 / 串 / 钩 / 拉直 | 认真做荒诞动作 |

## 设定稿

`characters/xiaozhen/sheet.png`(源文件 `sheet.svg`):标准 / 夹 / 串联 / 拉直。生图时可作参考图(`--reference`)锁形象。
