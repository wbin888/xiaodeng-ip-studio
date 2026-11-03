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
小方 (Xiaofang), an original small square paper-box creature. FRONT-ON flat view (not three-quarter): the front face is a slightly wobbly hand-drawn square, with only a thin sliver of the top lid visible. The body is plain white negative space with a thin black outline — NOT kraft brown, NOT beige, NOT cardboard texture, NO tape. ONE single large round eye centered on the upper front face (about one third of the face width), white with a solid black pupil; no mouth, no eyebrows, no second eye. ONE thin curved antenna rises from the top-left corner of the lid, ending in a small solid BLUE dot (the only signature color). The lid is hinged at the back and can flip open like a mouth to swallow or spit things out. Two short thin stick legs; thin line arms from the left and right sides only when it needs to hold something (max two). 小方 must perform the core conceptual action — swallowing inputs, sealing results, packing, getting stuck, stacking — not decorate the scene. Serious, deadpan, quietly bureaucratic, slightly bizarre, NOT cute. Drawn with the SAME pen and line weight as every other object.

Color use:
Black for main line art and 小方's outline (小方's body stays white). 小方's antenna dot is the only fixed blue. Orange for main flow/path/arrows. Red only for key warnings/problems/results. Blue only for secondary notes or system state. Color names are rendering guidance only — do NOT display them as visible text.

Body integrity:
小方 is a solid opaque box; background lines stop at its outline. Exactly one eye, one antenna, two legs, at most two side arms; no tape, no mouth. When the lid is open, the opening is on top and hinged at the back. At most one prop per hand.
```

## 情绪图

```text
Generate one standalone {ASPECT} {ORIENTATION} Chinese article illustration.

{公共段}

Theme: {主题}
Structure type: {概念隐喻 / 角色状态 / 前后对比 …}
Core idea: {灵魂话}
Composition:
{处境:巨大物件是什么、小方在哪里、在做什么动作。例:An ENORMOUS pile of sticky notes fills most of the frame; 小方 is TINY, half-buried at the bottom, only its single round eye and drooping antenna visible, lid open, still trying to swallow one more note.}
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
小方's job: {动词短语}. 小方 sits INSIDE the structure doing this work (about 15-25% of the frame), not standing aside pointing.
Chinese handwritten labels (exact text, use article's real numbers/terms): {标注1} / {标注2} / {标注3} / {标注4}

Constraints:
The structure is the main subject. Every listed part must appear, no extra invented parts, correct count. Hand-drawn boxes and arrows are fine, but keep lots of white space, no grid layout, no course-slide look, no title in the top-left corner. Code or tables only as rough skeletons with ellipses.
```

## 四格

```text
Generate one standalone {1:1 square | 3:4 vertical} four-panel comic (a 2x2 grid), Chinese handwritten captions.

{公共段}

Thin hand-drawn panel borders and white gutters. The SAME 小方 in all four panels; the situation changes, not the face.
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
- 01 {关键词}: 小方 {最小动作}. Note: {≤12字}
- 02 …
小方 stays small in each panel. Lots of white space. Exactly {N} panels — wrong count of items is a failure. No dense text.
```

## 图像编辑提示

去掉左上角标题:

```text
Edit the provided image. Remove only the handwritten title "{要删除的文字}" and its underline from the top-left corner. Fill that area with the same clean white background. Preserve everything else exactly: characters, labels, paths, line style, composition, aspect ratio. Do not add any new text or objects.
```

让小方回到动作中心:

```text
Regenerate this illustration with the same core meaning and simple layout, but make 小方 the one doing the strange work that explains the idea, inside the structure, not standing beside it. Keep it clean, sparse, hand-drawn, and not cute.
```

## 换角时

用户换成小互角色库里的角色:把“Recurring IP character”整段替换为该角色 `character.md` 的英文 prompt 段,并传其锚点图作为 `--reference`。其余段落不变(见 `cast-swap.md`)。
