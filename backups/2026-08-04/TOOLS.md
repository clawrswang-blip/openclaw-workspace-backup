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
- **ima-skill** → IMA 笔记 + 知识库（腾讯ima）
  - 安装路径：`skills/ima-skill/`
  - 触发关键词：`笔记`、`知识库`、`添加到知识库`、`搜索知识库`、`上传到知识库`、`新建笔记`、`追加到笔记`
  - 能力：笔记管理（搜索/列表/读取/新建/追加）+ 知识库管理（上传文件/添加网页/添加笔记/搜索/浏览）
  - 配置：API Key 已写入 `~/.config/ima/`（Client ID + API Key）
  - 依赖：node ≥18.0.0 ✅（v24.14.0）
  - 验证：✅ 已测试 list_notebook / search_knowledge_base 均正常
  - Rishon 的知识库：Rishon Wang王瑞盛的知识库 / 6大平台探索 / 中小企业调研
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
- **finesse-ui** → 高端界面制作 skill（mouse-lin/finesse-skill）
  - 安装路径：`skills/finesse-ui/SKILL.md`
  - **所有 HTML 制作任务的强制标准**；brand 路线（落地页/品牌站）+ product 路线（仪表盘/后台）全覆盖
  - 核心流程：Design Read → 三档旋钮（SOUL·SPECTACLE·DENSITY）→ 高级感物理层 → Hero Engine / 组件系统
  - 反廉价黑名单 + 起飞前自检，交付前必过
  - 触发词："make this look premium"、"landing page"、"dashboard"、"admin panel"、"give it a soul"、"/finesse"
  - 仓库：`https://github.com/mouse-lin/finesse-skill`

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

### DashiAI PPT Skill（dashiai-ppt）
| 项目 | 值 |
|---|---|
| 触发关键词 | `PPT`、`演示文稿`、`幻灯片`、`汇报材料`、`做 ppt` |
| 安装路径 | `skills/dashiai-ppt/` |
| 核心脚本 | `scripts/render_goal_deck.sh` |
| 主题数量 | 12种（theme01-12）|
| 输出格式 | HTML PPT（默认）+ PPTX / PDF（需导出）|
| 端口 | 5200-5999 段（`DASHI_PPT_PREVIEW_PORT` env var）|
| 版本检查 | `node <skill-root>/scripts/check_latest_version.mjs`（静默）|
| 依赖 | Node.js 18+，npm（已满足 v24.14.0）|

> ⚠️ **PPTX 导出**: 需要本机 HTTP 预览服务，不能用 `file://` 直接导出

### cangjie-skill（蒸馏 skill）
| 项目 | 值 |
|---|---|
| 触发关键词 | `蒸馏`、`拆书`、`把xx做成skill`、`distill`、`蒸馏成skill` |
| 安装路径 | `skills/cangjie-skill/` |
| 核心定位 | 把书/视频/播客/课程的方法论蒸馏成可执行的 agent skills |
| 核心方法 | RIA-TV++：5阶段 + 并行提取 + 三重验证 + darwin 兼容测试 |
| 输入要求 | **必须提供文本来源**（PDF/EPUB/TXT/字幕/转写稿），不凭记忆蒸馏 |
| 产出结构 | `books/<slug>/` → SKILL.md + candidates/ + verified.md + INDEX.md + GLOSSARY.md + DIGEST.md |
| 生态位 | nuwa-skill（蒸馏人）× cangjie-skill（蒸馏书）× darwin-skill（进化skill） |
| 工作流程 | 阶段0整书理解 → 阶段1五并行提取 → 阶段1.5三重验证 → 阶段2构造skill → 阶段3链接 → 阶段4压力测试 → 阶段5交付 |

> **注意**：必须先拿到内容文本才能开始；首次建议只蒸馏1本验证流程。

## 🎬 视频创作 Skill 绑定规则（强制执行）⭐2026-07-09 新增

**触发条件：** 任何涉及视频创作、视频生成、TVC广告、短剧、MV、广告片、导演工作的请求

**强制技能链：**
```
用户请求 → seedance-2.0（导演层/决策层）→ tvc-director（执行层）→ video_generate（生成层）
```

**各层职责：**
| 层级 | Skill | 作用 |
|------|-------|------|
| 导演层 | `seedance-2.0`（本目录 `skills/emily-seedance/`） | 理解创意意图 → 制定拍摄方案 → 分镜/Shot List → Prompt 设计 → 质量把控 |
| 执行层 | `tvc-director` | 宫格图 → 视频脚本 → Hailuo 生成 → 首帧对齐 |
| 生成层 | `video_generate` | 调用 MiniMax Hailu API 实际生成视频 |

**决策树：**
```
收到视频创作请求
    ↓
读取 seedance-2.0 SKILL.md（导演层决策）
    ↓
读取 seedance-sequence / seedance-prompt（多镜头/单镜头）
    ↓
应用 directing-engine / capability-map（能力校准）
    ↓
委托 tvc-director 执行层（生成宫格图+视频脚本）
    ↓
调用 video_generate（MiniMax Hailu）
    ↓
seedance retake-protocol 进行质量检阅
```

**关键 binding：**
- `seedance-2.0` 的 `SKILL.md` 是**导演层入口**，所有视频创作先读它
- `tvc-director` 已有完整视频生成 pipeline（宫格图→视频→首帧对齐），两者深度整合
- `seedance-pipeline` 处理 API 路由（Runway/Seedance/MiniMax 等多模型支持）
- 已有 `MINIMAX_API_KEY` 配置，`video_generate` 工具可用

---

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

### cheat-on-content（社交媒体内容创作闭环系统）
| Skill | 用途 | 触发词 |
|---|---|---|
| `cheat-on-content` | 主入口 + 路由 | `初始化` |
| `cheat-learn-from` | 拆解对标账号 + 派生 rubric 信号 | `找对标` / `learn from` |
| `cheat-seed` | Cold-start 选题启动器 | `找选题` / `seed` |
| `cheat-score` | 单稿打分（不写文件） | `打分这篇` |
| `cheat-predict` | 盲预测 + immutable 日志 | `启动预测` |
| `cheat-shoot` | 登记拍摄（buffer +1） | `拍了` / `shot it` |
| `cheat-publish` | 发布元数据登记（buffer -1） | `已发布` / `shipped` |
| `cheat-retro` | T+3d 数据回收 + 复盘 | `复盘` / `retro` |
| `cheat-persona` | 受众画像派生 | `构造受众画像` |
| `cheat-bump` | rubric 升级（含跨模型审） | `升级rubric` |
| `cheat-recommend` | 候选池排序推荐 | `推荐选题` |
| `cheat-trends` | 热点抓取（多 adapter） | `抓热点` |
| `cheat-status` | 状态看板（含 buffer 警戒） | `状态` / `status` |
| `cheat-migrate` | schema 升级迁移 | `迁移` |

> **social media 内容制作时自动调用**：打分→预测→发布→复盘→进化 rubric 完整闭环

---

## 中文 PDF 生成完整方案（经验沉淀 2026-07-28）

### 核心结论
**WeasyPrint + NotoSansCJKsc 是 macOS 中文 PDF 的唯一可靠方案。**

ReportLab 的 CID 字体注册极复杂且易失败；fonttools 解析 OTF 容易遇到 `postscript outlines are not supported` 报错。

### 完整工作流（v7+ 标准）

**Step 1 — 预处理 markdown（必须，防止渲染 Bug）**
```python
# 1. 处理代码块内的列表标记（Markdown 会把 "1. xxx" 当有序列表解析）
lines = md_text.split('\n')
processed_lines = []
in_code = False
for line in lines:
    if line.strip().startswith('```'):
        in_code = not in_code
        processed_lines.append(line)
    elif in_code:
        # 把行首的 "数字. " 替换为空格，防止被解析为列表
        processed = re.sub(r'^(\d+)\. (\S)', r'  \2', line)
        processed_lines.append(processed)
    else:
        processed_lines.append(line)
md_text = '\n'.join(processed_lines)

# 2. 清理零宽字符
md_text = md_text.replace('\u200b', '').replace('\u200c', '').replace('\u200d', '').replace('\ufeff', '')
```

**Step 2 — Markdown → HTML（禁止使用 codehilite）**
```python
import markdown
html_body = markdown.markdown(
    md_text,
    extensions=["tables", "fenced_code"],  # ⚠️ 禁止 codehilite！
    extension_configs={}
)

# 清理空 span 标签（codehilite 产生的）
html_body = html_body.replace('<span></span>', '')
html_body = re.sub(r'<span class="[^"]*"></span>', '', html_body)
```

**Step 3 — CSS 字体声明**
```css
/* @font-face family name 必须是 OTF 文件的真实名字 */
@font-face {
  font-family: "Noto Sans CJK SC";  /* ⚠️ 不是 "NotoSansSC"！ */
  src: url("/Users/clawrs/Library/Fonts/NotoSansCJKsc-Regular.otf");
  font-weight: normal;
}
@font-face {
  font-family: "Noto Sans CJK SC";
  src: url("/Users/clawrs/Library/Fonts/NotoSansCJKsc-Bold.otf");
  font-weight: bold;
}

/* 全局强制 Noto Sans CJK SC */
html, body, div, p, td, th, tr, li, ol, ul,
h1, h2, h3, h4, h5, h6, pre, code, blockquote {
  font-family: "Noto Sans CJK SC", "Noto Sans SC", sans-serif !important;
}

/* pre/code 区块绝对不要用 Menlo */
pre {
  font-family: "Noto Sans CJK SC", sans-serif !important;  /* ⚠️ 不要加 Menlo */
  font-size: 9.5pt;
  line-height: 1.75;
}
code {
  font-family: "Noto Sans CJK SC", sans-serif !important;  /* ⚠️ 不要加 Menlo */
}
```

**Step 4 — 生成 PDF**
```bash
export DYLD_LIBRARY_PATH=/opt/homebrew/lib
python3 ~/.openclaw/workspace/scripts/generate_mini_mba_pdf.py
```

### NotoSansCJKsc 字体路径
```
/Users/clawrs/Library/Fonts/NotoSansCJKsc-Regular.otf  (~16MB)
/Users/clawrs/Library/Fonts/NotoSansCJKsc-Bold.otf    (~17MB)
/Users/clawrs/Library/Fonts/NotoSansCJKsc-Light.otf
/Users/clawrs/Library/Fonts/NotoSansCJKsc-Black.otf
```

### 三类渲染 Bug 的根因与修复

| 现象 | 根因 | 修复 |
|------|------|------|
| 深色代码块里中文变黑色方块 | `codehilite` 扩展插入空 `<span></span>`，某些 PDF 阅读器渲染失败 | 移除 `codehilite`，改用 `extensions=["tables", "fenced_code"]` |
| `§ 1.1` 前出现黑色方块 | Markdown 把代码块里 `1. § 1.1` 当作有序列表，行首数字被解析为列表标记 | 预处理代码块，行首 `数字. ` 替换为空格 |
| 中文变方块，但浅色背景正常 | `pre/code` CSS 用 `Menlo` 字体做 fallback，Menlo 不支持中文 | `pre/code` 的 `font-family` 只用 `Noto Sans CJK SC`，去掉 Menlo |
| 字体文件找到了但仍显示方块 | CSS `font-family: "NotoSansSC"` 与 OTF 真名 `"Noto Sans CJK SC"` 不匹配，fontconfig fallback 到 PingFang-SC | CSS 使用 OTF 文件的真是 family name：`"Noto Sans CJK SC"` |
| PyMuPDF 提取 "缺失" 大量字符 | PyMuPDF 对 CJK Identity-H Type0 字体提取有 Bug，字符已正确嵌入只是提取失败 | 以 AI 视觉检查为准，不以 PyMuPDF 提取结果为准 |

### macOS Preview 渲染行为记录

macOS Preview 对 PDF 字体渲染要求最严格，以下组合会触发方块：
- 空 `<span></span>` 标签（即使 CSS 设为 `display:none` 也可能渲染）
- 字体子集缺少某些 CJK 字符（NotoSansCJKsc 无此问题）
- 字体 fallback 链中有不支持 CJK 的字体（如 Menlo）

**结论**：用 WeasyPrint + 本地完整 OTF（NotoSansCJKsc） + 无 codehilite + 预处理 markdown = macOS Preview 100% 通过。

### 历史踩坑全记录
- ❌ SimHei / PingFang：路径不存在或 OTF 不被 ReportLab 支持
- ❌ STHeiti / HeitiTC：繁体字体，简体字不全
- ❌ ReportLab CID 字体注册：需要 `cidRegistry` 等复杂字段，TTFontFace 无此属性
- ❌ Python str.format() 与 CSS {} 冲突：解决方法写外部 HTML 文件
- ❌ CSS `font-family: "NotoSansSC"`：与 OTF 真名不匹配，fontconfig 无法匹配
- ❌ `pre { font-family: Menlo }`：Menlo 不支持中文，导致深色代码块内中文变方块
- ❌ `markdown.extensions=[..., "codehilite"]`：插入空 `<span></span>`，触发 macOS Preview 渲染 Bug
- ❌ Markdown 代码块内 `1. § 1.1` 语法：被解析为有序列表，行首数字变成列表标记
- ✅ WeasyPrint + NotoSansCJKsc-Regular.otf：100% 简体字覆盖
- ✅ CSS `font-family: "Noto Sans CJK SC"`（真名匹配）
- ✅ 预处理代码块 + 移除 codehilite + 无 Menlo fallback：macOS Preview 100% 通过

---

Add whatever helps you do your job. This is your cheat sheet.
