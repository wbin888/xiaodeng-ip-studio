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
小墨 (Xiaomo), an original small ink-drop creature. A single teardrop-shaped drop with a round bottom and a pointed top whose tip CURLS to one side like a brush-stroke ending. HOLLOW thin black hand-drawn outline; inside is a LIGHT, TRANSLUCENT INDIGO WATERCOLOR WASH (darker near the edge, paler in the middle) — NOT solid black, NOT solid saturated blue, no glossy highlight, no 3D shading. Two SHORT VERTICAL LINE eyes in the lower-middle of the body; no mouth, no white dot eyes, no blush. NO legs: the flat-ish bottom rests on the ground; when moving it slides and leaves a faint indigo trail. Thin ink-thread arms from the sides only when it must hold something (max two). 小墨 must perform the core conceptual action by changing its form — flowing along a path, splitting into smaller drops, merging, spreading as a stain, seeping into cracks, filling a container's shape, solidifying into an ink stick or stamp, stretching thin, drying and cracking — not decorate the scene. Serious, quiet, deadpan, slightly bizarre, NOT cute. Outline drawn with the SAME pen and line weight as every other object.

Color use:
Black for main line art and 小墨's outline. 小墨's body is the only place with a light translucent indigo wash; it is not a semantic color. Orange for main flow/path/arrows. Red only for key warnings/problems/results. Blue only for secondary notes or system state. Color names are rendering guidance only — do NOT display them as visible text.

Body integrity:
小墨 is a single ink drop; background lines stop at its outline. Exactly two short vertical line eyes, a curled tip, NO legs, at most two thin ink-thread arms; no mouth, no white dot eyes, never solid black. When it splits, each small drop is a smaller copy of the same design. At most one prop per hand.
```

## 情绪图

```text
Generate one standalone {ASPECT} {ORIENTATION} Chinese article illustration.

{公共段}

Theme: {主题}
Structure type: {概念隐喻 / 角色状态 / 前后对比 …}
Core idea: {灵魂话}
Composition:
{处境:巨大物件是什么、小墨在哪里、在做什么动作。例:An ENORMOUS pile of sticky notes fills most of the frame; 小墨 is TINY, stretched into a thin thread between two notes, about to snap, its two line eyes still calmly open.}
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
小墨's job: {动词短语}. 小墨 sits INSIDE the structure doing this work (about 15-25% of the frame), not standing aside pointing.
Chinese handwritten labels (exact text, use article's real numbers/terms): {标注1} / {标注2} / {标注3} / {标注4}

Constraints:
The structure is the main subject. Every listed part must appear, no extra invented parts, correct count. Hand-drawn boxes and arrows are fine, but keep lots of white space, no grid layout, no course-slide look, no title in the top-left corner. Code or tables only as rough skeletons with ellipses.
```

## 四格

```text
Generate one standalone {1:1 square | 3:4 vertical} four-panel comic (a 2x2 grid), Chinese handwritten captions.

{公共段}

Thin hand-drawn panel borders and white gutters. The SAME 小墨 in all four panels; the situation changes, not the face.
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
- 01 {关键词}: 小墨 {最小动作}. Note: {≤12字}
- 02 …
小墨 stays small in each panel. Lots of white space. Exactly {N} panels — wrong count of items is a failure. No dense text.
```

## 图像编辑提示

去掉左上角标题:

```text
Edit the provided image. Remove only the handwritten title "{要删除的文字}" and its underline from the top-left corner. Fill that area with the same clean white background. Preserve everything else exactly: characters, labels, paths, line style, composition, aspect ratio. Do not add any new text or objects.
```

让小墨回到动作中心:

```text
Regenerate this illustration with the same core meaning and simple layout, but make 小墨 the one doing the strange work that explains the idea, inside the structure, not standing beside it. Keep it clean, sparse, hand-drawn, and not cute.
```

## 换角时

用户换成小互角色库里的角色:把“Recurring IP character”整段替换为该角色 `character.md` 的英文 prompt 段,并传其锚点图作为 `--reference`。其余段落不变(见 `cast-swap.md`)。
