# 多 IP 同框:一篇文章用 2-3 个角色

默认情况下,全篇只有一个主角。满足下面两种情况之一时,可以启用 2-3 个 IP:

- 用户明确要求「多个角色」或「用小灯 + 某某」;
- 拆解时发现文章本身就有**多个角色或视角**,一个演员演不清楚。

启用了也要克制。**多一个角色,就多一份理解成本。**

## 何时启用(先过判定)

| 文章信号 | 例子 | 建议 |
|---|---|---|
| 人 vs AI / 人 vs 工具 | 「AI 干活,人做判断」 | 2 个 |
| 旧方法 vs 新方法 | 「从手动整理到自动归档」 | 2 个 |
| 多环节流水线,每环性质不同 | 「记录 → 连接 → 输出」 | 3 个 |
| 多方关系 | 老板、员工、DDL | 2-3 个 |
| 单一视角的个人经验、纯概念 | 「我为什么坚持写作」 | **不启用**,一个主角就够 |

判定一句话:**能不能给每个角色写出一个全篇不变的「它代表什么」?** 写不出来,就不启用。

## 规则

### 1. 演员表全篇固定

方案开头先列演员表:

| 角色 | 身份 | 代表(语义) | 招牌动作 |
|---|---|---|---|
| 小格 | 主角之一 / 搭档 | 记录、输入 | 记、撕、贴 |
| 小针 | 搭档 | 连接、关联 | 夹、串、钩 |
| 小灯 | 主角 | 洞见、输出 | 亮、照、接电 |

- **主角**只有 1 个,出场比例 ≥50%。
- **搭档**有 1-2 个,每个至少出场 1 次,否则砍掉。
- 角色的「代表」**全篇不变**。小针是「连接」,就不能下一张又去演「记录」。
- 「小互 · 食物符号」只能当**龙套**:出现在单张里,不进演员表的主线。

### 2. 单张同框数量

- 默认一张图最多 **2 个** IP。
- **3 个**只在三种图里出现:总览海报、四格(每格可换人)、「交接」类解释图。
- 一张图只有 1 个 IP 很正常。不要为了「都出场」硬塞。

### 3. 每个 IP 都要干活(整合测试)

- 每个同框的 IP 都承担一个**不同的**动作,不准有人站旁边围观。
- 擦掉任意一个 IP,画面结构里都会少一块。少不了,说明它是装饰,删掉。
- 动作要符合肢体档位(见 `cast-roster.md`):被动角色不准写「它伸手拿」。

### 4. 互动模式(五选一,写进方案)

| 模式 | 画法 | 适用 |
|---|---|---|
| **交接** | A 把东西递 / 推 / 串给 B,orange 主箭头穿过两者 | 流水线、上下游 |
| **对照** | 左 A 右 B,同一件事两种做法,中间一条竖虚线 | 旧 vs 新、人 vs AI |
| **协作** | A 和 B 一起扛 / 拉 / 搭同一个结构的两端 | 人机分工、团队 |
| **冲突** | A 拽 B 推,或 A 堵住 B 的路 | 矛盾、阻力、拉扯 |
| **因果** | A 的动作直接导致 B 的状态变化(灭 → 亮、蔫 → 立) | 方法见效、转折 |

### 5. 外形可分,招牌色不撞

- 每个 IP 只保留**自己的**招牌色,别的 IP 不准染上。
- 同框的两个 IP 主色相近(如小格的淡蓝和问号人的淡蓝)→ 换掉其中一个,或者把龙套画成纯黑线。
- 剪影要能区分:不要让两个「方块 + 单眼」同框(小格 / 小方 / 方方)。
- **小互角色统一转成本技能画风**:白底、黑色手绘线稿,只在身体上保留一小块淡淡的主色,不用 3D 盲盒、不用厚涂。生图时传它的线稿锚点图(`--cast` 会自动选线稿锚点)。

### 6. 占比

- 解释图里所有 IP 加起来 **≤35%**,每个约 12-20%,结构才是主体。
- 情绪图可以让主角放大到 30%,搭档保持小。
- 不同 IP 的大小按身份来,不按「好看」来:主角稍大,龙套最小。

### 7. 一致性

- 同一角色在全篇每张图里外形一致。每张都通过 `--cast` 传同一组参考图。
- 角色之间不合体、不互换零件。小灯不长出回形针腿,小针不发黄光。

## 方案里怎么写

在 `plan-template.md` 的基础上多写两处:

1. 方案开头的**演员表**。
2. 每张 shot 多一个 `出演` 字段,写清**谁演、各自做什么、用哪种互动模式**。例如:

```markdown
- **出演**:小针(夹住三张纸条串成一串)→ 小灯(被串的最后一端接通、亮起)· 交接
```

## Prompt 怎么写

把公共段里的 `Recurring IP character required:` 整段换成**多角色段**:

```text
Recurring IP characters required ({2|3} different characters — keep them visually distinct, NEVER merge their features or swap their parts):

Character 1 — {名1}: {角色1 英文 prompt 段,去掉标题行}
Character 2 — {名2}: {角色2 英文 prompt 段,去掉标题行}
[Character 3 — {名3}: …]

Who does what in this image ({交接 / 对照 / 协作 / 冲突 / 因果}):
- {名1}: {动作}
- {名2}: {动作}
Every character performs a different part of the core action; nobody stands aside watching. All characters are drawn with the SAME black pen and line weight as the rest of the scene, small (together ≤35% of the frame).

Color use:
Each character keeps ONLY its own signature color: {名1} = {色1}; {名2} = {色2}. No character borrows another's color. Characters from other illustration styles are redrawn as plain black hand-drawn line art with only a light tint of their signature color — no 3D, no thick painting.
Orange for main flow/arrows, red for key problems, blue for secondary notes.
```

每个角色的 `Body integrity` 合并成一条 `Body integrity:` 写在后面,逐个角色列出。

用脚本生图:

```bash
python3 scripts/generate.py --prompt-file p.md --cast 小灯 小针 --out 03.png
```

`--cast` 的顺序就是 prompt 里 Character 1/2/3 的顺序。脚本会在 prompt 末尾自动追加「参考图 N 是哪个角色」的说明。

## 常见坑

| 症状 | 修法 |
|---|---|
| 两个角色长成一个(灯泡头 + 回形针身) | prompt 加 `NEVER merge`,并确认参考图顺序与 Character 编号一致;仍失败就分开生成成两张 |
| 一个干活、一个围观 | 回方案改互动模式,给围观的那个一个结构内动作,或删掉它 |
| 小互角色画成 3D / 厚涂 | 强调 `plain black hand-drawn line art`,传线稿锚点,不传 3D 锚点 |
| 每张都三人同框,画面挤 | 降到 2 人;第三人只在总览和交接图出现 |
| 搭档全篇只出现 1 次,还看不懂它是谁 | 首次出场时加一个手写名字标注,或者砍掉这个搭档 |
