# 生图后端

优先级:内置生图工具(如 `image_gen`)> `scripts/generate.py` > 只交付 prompt。

## 一次性配置(用脚本时)

```bash
python3 scripts/studio.py init     # 填 base_url / model / key,写入 ~/.config/xiaohei-ip-studio/config.yaml(mode 600)
python3 scripts/studio.py doctor   # 自检
```

| 字段 | 说明 |
|---|---|
| `base_url` | 任何 OpenAI 兼容图像端点 |
| `model` | 默认 `gpt-image-2` |
| `api_key` | 你自己的 key,只存本地 |
| `backend` | 可选:`openai-sync`(默认)/ `apimart-task`(异步任务网关,支持多张参考图) |

## 调用

```bash
# 先离线校验(不调 API):比例与方向词联动、参考图是否存在
python3 scripts/generate.py --prompt-file p.md --out out.png --dry-run

# 文生图(小黑无需参考图)
python3 scripts/generate.py --prompt-file p.md --out assets/slug-illustrations/01-topic.png

# 换角时锁形象
python3 scripts/generate.py --prompt-file p.md --reference <角色锚点图> --out out.png
```

- `aspect_ratio` 自动映射:横 `1536x1024` / 竖 `1024x1536` / 方 `1024x1024`。
- 输出 JSON 含实际宽高;比例跑偏就重生成。
- 失败最多重试 2 次。纯标准库,零依赖。
