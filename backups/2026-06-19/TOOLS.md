# TOOLS.md - Local Notes

## ⚠️ 工具使用铁律（经验沉淀）

| 场景 | 工具 | 说明 |
|------|------|------|
| **10KB 以上的文件写入** | `write` | exec heredoc 无法可靠处理多行字符串，语法错误率极高 |
| 小文件写入（< 5KB） | `write` 或 `exec echo` | 都可以 |
| 执行系统命令 | `exec` | 日常命令、CLI 调用 |
| 语法检查 | `python3 -c "import ast; ast.parse(open(f).read())"` | exec 里做 |

> 教训来源：2026-04-20，exec heredoc 写 generate.py（40KB）产生不可见语法错误，花了 15+ 次修复。

## Rishon 的工具配置

### 已配置好的服务

| 服务 | 状态 | 备注 |
|------|------|------|
| gog (Google Workspace) | ✅ 已授权 | clawrswang@gmail.com，OAuth完成 |
| GitHub (Maton OAuth) | ✅ 已连接 | clawrswang-blip |
| Gemini API | ✅ 已配置 | GEMINI_API_KEY |
| MiniMax Hailu AI | ✅ 已配置 | MINIMAX_API_KEY（海螺AI视频生成专用）|
| 飞书机器人 | ✅ 已测试 | Webhook + App ID 已配置 |
| OpenClaw Auto-updater | ✅ 已安装 | 自动每日 cron job |

### Skills（已安装）

**无需配置：**
- word-docx, powerpoint-pptx, ui-ux-pro-max, deep-research-pro
- data-analysis, frontend-design-3, market-research, marketing-skills, seo
- self-improving, skill-vetter, ontology, humanizer
- agent-browser-clawdbot, polymarket-trade

**需要 API Key：**
- brave-search → 需 BRAVE_API_KEY
- youtube-api-skill → 需 Maton API Key
- mcporter → 需 npm install -g mcporter
- n8n → 需 N8N_API_KEY + N8N_BASE_URL

**🆕 新安装/更新：**
- taste-skill（Leonxlnx）→ 反 slop 设计/内容品味框架
  - 安装路径：`.agents/skills/design-taste-frontend/SKILL.md`
  - **内容文案创作时第一步必须激活**，读取 brief → 输出 Design Read → 设定三个 Dial
  - 核心规则：anti-default（反 AI 紫 gradient/center bias/generic glassmorphism）、copy self-audit、AI tells 黑名单
  - 链接：`https://github.com/Leonxlnx/taste-skill`
- content-creation-workflow → 内容文案创作工作流
  - 安装路径：`skills/content-creation-workflow/SKILL.md`
  - **所有内容文案创作任务的入口 skill**，第一步激活 taste-skill → 第二步委托 khazix-writer/copywriting/humanizer 等执行 skill
  - 触发词：写文章、写稿子、帮我写、文案创作、创意物料、品牌文案、营销文案、活动文案
- tvc-director → TVC广告一站式生成（全MiniMax：图片image-01，视频Hailuo）
  - **一张宫格图**作为完整故事板 + 视频首帧
  - **视频3段生成**：始终以同一宫格图为首帧，按格顺序生成
  - **自动优先/Fallback**：Hailuo-2.3 → Fast → 等30s
  - **零确认**：用户只需给产品描述+图片，AI自主完成所有判断
  - 视频生成脚本：`~/.openclaw/workspace/skills/tvc-director/scripts/generate_video.py`
  - 知识库保留：`references/`（treatment/storyboard/shot-language等）
- fireworks-tech-graph → 技术图表生成（SVG + PNG）
  - 用自然语言描述系统 → 生成 publication-ready 技术图表
  - 支持 13 种图表类型：架构图、流程图、时序图、UML、Mind Map 等
  - 支持 7 种视觉风格：Flat Icon / Dark Terminal / Blueprint / Notion / Glassmorphism / Claude / OpenAI
  - 依赖：`brew install librsvg`（已安装 `rsvg-convert` ✅）
  - 快速参考 JSON 模板：`references/quick-rag.json`、`references/quick-multi-agent.json`

### 沟通渠道
- **WhatsApp:** +8618822096032（当前活跃会话）
- **飞书:** ou_13d5de76e62912757cd56fa20b10a358（已配对）

### libtv-skill（LibLib.tv AI 视频创作）
| 项目 | 值 |
|---|---|
| 触发关键词 | `libtv` |
| 安装路径 | `.agents/skills/libtv-skill/` |
| 核心脚本 | `create_session.py` / `query_session.py` / `upload_file.py` / `download_results.py` |
| 依赖 | `LIBTV_ACCESS_KEY`（未配置 ⚠️） |
| 能力 | 文生图、文生视频、图生视频、编辑修改、风格迁移、短剧生成、MV生成等 |

> ⚠️ **使用前需要设置 `LIBTV_ACCESS_KEY`**：联系 Rishon 获取 LibLib.tv 的 Access Key，然后配置到环境变量或 gateway config。

### markitdown（文件 → Markdown 转换）
| 项目 | 值 |
|---|---|
| 触发关键词 | `转换 markdown`、`markitdown`、`PDF转markdown`、`文档转markdown` |
| 安装方式 | `pip3 install markitdown[all]`（已完成） |
| Skill 路径 | `skills/markitdown/SKILL.md` |
| 支持格式 | PDF、Word、Excel、PPT、图片、音频、HTML、CSV、JSON、XML、ZIP、YouTube字幕、EPub |

### Rishon 的关键日期
- **2026年10月：** 加拿大PR结果出炉（最大分水岭）
- **2026 Q3/Q4：** Sungiven App 第二版电商功能完成

### Rishon 的家庭
- 太太 + 孩子在香港
- 每月 2-3 万港币开支

---

## Luna 的工具偏好

- TTS（语音）: 未配置，但 saga（ElevenLabs）在技能里有
- 浏览器自动化: agent-browser-clawdbot（已安装）

---

### Matt Pocock Skills（工程技能集）
| Skill | 用途 |
|---|---|
| `mattpocock/diagnose` | 硬 Bug 诊断 loop |
| `mattpocock/tdd` | TDD red-green-refactor |
| `mattpocock/grill-with-docs` | 开发前对齐 + 建统一语言 |
| `mattpocock/grill-me` | 非代码场景 grilling |
| `mattpocock/improve-codebase-architecture` | 架构改进 |
| `mattpocock/prototype` | 快速原型 |
| `mattpocock/triage` | Issue 分类 |
| `mattpocock/zoom-out` | 整体设计审视 |
| `mattpocock/to-prd` | 方案→PRD |
| `mattpocock/to-issues` | 需求→ticket |
| `mattpocock/caveman` | 极简原型 |
| `mattpocock/handoff` | 交接协议 |
> **Coding 任务触发顺序**：grill 对齐 → karpathy-coding-principles → 执行 skill

---

Add whatever helps you do your job. This is your cheat sheet.
