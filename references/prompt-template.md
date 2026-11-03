# 生图提示词模板

每张图单独生成,不拼图。`{ASPECT}` 与 `{ORIENTATION}` 必须同一行取值:

| ASPECT | ORIENTATION |
|---|---|
| 16:9 / 4:3 | horizontal |
| 3:4 / 9:16 | vertical |
| 1:1 | square |

使用 `scripts/generate.py` 时,prompt 文件需带 YAML 头,脚本会校验比例与方向词是否一致:

```text
---
aspect_ratio: "16:9"
---
Generate one standalone 16:9 horizontal Chinese article illustration.
...
```

## 公共段(每张都粘)

```text
Visual DNA:
Pure white background. Minimalist black hand-drawn line art. Slightly wobbly pen lines. Lots of empty white space. Sparse red/orange/blue handwritten Chinese annotations. Clean absurd product-sketch feeling. No gradients, no shadows, no paper texture, no complex background, no commercial vector style, no PPT infographic look, no cute mascot poster, no children's illustration, no realistic UI.

Recurring IP character required:
小灯 (Xiaodeng), an original thin stick-figure character whose head is a round LIGHT BULB. Thin black hand-drawn bulb outline, a small white screw base with two horizontal grooves under it, then a thin single-line body with thin line arms and legs (head much larger than body). NO eyes, NO mouth, NO eyebrows on the bulb — its only face is the FILAMENT inside, held by two thin support wires: lit = filament stands up as a sharp "M" zigzag; off = filament sags into a soft wave; flickering = filament broken into two pieces. Brightness is its state: lit = translucent warm yellow inside the bulb plus a few short yellow rays around it; off = pale grey inside, no rays; flickering = very faint yellow with dashed rays. Warm yellow appears ONLY on 小灯. Not an emoji idea bulb, not a 3D glass bulb, no glossy highlight, not solid black. 小灯 must perform the core conceptual action — plugging in a wire, lighting up a dark corner, being one bulb in a chain that lights up step by step, being unplugged, dimming its own knob, overheating in tangled wires — not decorate the scene. Serious, deadpan, slightly stubborn, slightly bizarre, NOT cute. Drawn with the SAME pen and line weight as every other object.

Color use:
Black for main line art and 小灯's outline. Warm translucent yellow appears ONLY inside 小灯's bulb (and its short rays) when lit; it is its state signal, not a semantic color. Orange for main flow/path/arrows. Red only for key warnings/problems/results. Blue only for secondary notes or system state. Color names are rendering guidance only — do NOT display them as visible text.

Body integrity:
小灯 has exactly one bulb head, one screw base, one thin line body, two thin arms, two thin legs; no eyes or mouth on the bulb; background lines stop at its outline. In a chain, only ONE bulb has a body; the rest are plain bulbs on the wire. At most one prop per hand.
```

## 情绪图

```text
Generate one standalone {ASPECT} {ORIENTATION} Chinese article illustration.

{公共段}

Theme: {主题}
Structure type: {概念隐喻 / 角色状态 / 前后对比 …}
Core idea: {灵魂话}
Composition:
{处境:巨大物件是什么、小灯在哪里、在做什么动作。例:An ENORMOUS wall of sticky notes fills most of the frame; 小灯 is TINY at the bottom, its bulb OFF and grey, filament sagging, still holding up a tiny plug toward a socket it cannot reach.}
Suggested elements: {物件1} / {物件2}
Chinese handwritten labels: {标注1} / {标注2} / {标注3}

Constraints:
One image explains only one core idea. Feeling comes from the situation and scale contrast, not from a face. Keep ≥35% blank white space. At most 5-8 short Chinese labels. No title in the top-left corner. Do not write the structure type. Invent a fresh metaphor for this article; do not copy prior examples. Strange but clean, interesting but not childish.
```

## 解释图

```text
Generate one standalone {ASPECT} {ORIENTATION} Chinese article explanatory sketch ({FLOW / STRUCTURE / COMPARISON / LADDER / RELATION}), hand-drawn, NOT a slide.

{公共段}

Core idea: {灵魂话}
Metaphor mapping (draw these exactly):
- {物件A} = {真实部件A}
- {物件B} = {真实部件B}
Steps / parts / nodes (from the article, must all appear):
- {1}: {内容}
- {2}: {内容}
Flow: {左→右 / 上→下 / 汇聚 / 分隔};main path in orange solid arrows; optional path in dashed lines.
小灯's job: {动词短语}. 小灯 sits INSIDE the structure doing this work (about 15-25% of the frame), not standing aside pointing.
Chinese handwritten labels (exact text, use article's real numbers/terms): {标注1} / {标注2} / {标注3} / {标注4}

Constraints:
The structure is the main subject. Every listed part must appear, no extra invented parts, correct count. Hand-drawn boxes and arrows are fine, but keep lots of white space, no grid layout, no course-slide look, no title in the top-left corner. Code or tables only as rough skeletons with ellipses.
```

## 四格

```text
Generate one standalone {1:1 square | 3:4 vertical} four-panel comic (a 2x2 grid), Chinese handwritten captions.

{公共段}

Thin hand-drawn panel borders and white gutters. The SAME 小灯 in all four panels; the situation changes, not the face.
- Panel 1 (起): {现状}. Caption: {≤8字}
- Panel 2 (承): {踩坑 / 卡住}. Caption: {≤8字}
- Panel 3 (转): {转机}. Caption: {≤8字}
- Panel 4 (合): {结局}. Caption: {≤8字}
Each panel clean and sparse, one caption each. No overall title.
```

## 总览海报

```text
Generate one standalone {3:4 vertical | 4:3 horizontal} hand-drawn Chinese overview sketch with {N} numbered panels, NOT a slide.

{公共段}

Large handwritten numbers 01–0{N}, connected by one thin orange flow line:
- 01 {关键词}: 小灯 {最小动作}. Note: {≤12字}
- 02 …
小灯 stays small in each panel. Lots of white space. Exactly {N} panels — wrong count of items is a failure. No dense text.
```

## 图像编辑提示

去掉左上角标题:

```text
Edit the provided image. Remove only the handwritten title "{要删除的文字}" and its underline from the top-left corner. Fill that area with the same clean white background. Preserve everything else exactly: characters, labels, paths, line style, composition, aspect ratio. Do not add any new text or objects.
```

让小灯回到动作中心:

```text
Regenerate this illustration with the same core meaning and simple layout, but make 小灯 the one doing the strange work that explains the idea, inside the structure, not standing beside it. Keep it clean, sparse, hand-drawn, and not cute.
```

## 换角时

换成其他单个角色:把 “Recurring IP character” 整段替换为该角色 `character.md` 的英文 prompt 段,`Color use` / `Body integrity` 换成它的替换段;生图时用 `--cast <角色名>` 自动带上参考图。其余段落不变(见 `cast-swap.md`)。

## 多 IP 同框

2-3 个角色同框时,把 “Recurring IP character required” 整段换成 `ensemble.md` 里的**多角色段**(Character 1/2/3 + Who does what + 合并的 Color use / Body integrity),用 `--cast 角色1 角色2 [角色3]` 生成,顺序与 Character 编号一致。四格可在每格写明本格出场的角色。
