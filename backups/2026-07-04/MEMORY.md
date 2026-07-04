# MEMORY.md — 长期记忆索引

_Last updated: 2026-04-23_

---

## 🔍 记忆查询方法（MemPalace）

**优先使用 MemPalace**（语义搜索，更准确）：
```
mempalace_search <关键词>           # 全局语义搜索
mempalace_kg_query <实体>           # 查实体关系事实
mempalace_list_wings                # 查看所有 wings
mempalace_diary_read Luna           # 读 Luna 的日记
mempalace_diary_read Rishon         # 读 Rishon 的日记（如有）
```

**fallback**（文件层）：
- `memory/projects/sungiven.md` → Sungiven 详细笔记
- `memory/projects/ai-consulting.md` → AI咨询详细笔记
- `memory/projects/pr-plan.md` → PR规划详细笔记

---

## 🧠 MemPalace Palace 结构

| Wing | 内容 | 关键 Room |
|---|---|---|
| rishon | Rishon 的 profile/偏好/项目 | profile, projects, preferences, life-plan |
| luna | Luna 的身份/技能/成长日记 | identity, skills, diary |
| sungiven | Sungiven 项目 | overview |
| ai-consulting | AI咨询项目 | overview |
| workspace | 工作区文件索引 | memory, analysis, skills, scripts |

**关键 KG 事实**（永久生效）：
- Rishon → lives_in → Vancouver
- Rishon → family_location → Hong Kong
- Rishon → primary_focus → OpenClaw AI tools
- Rishon → works_on → Sungiven membership
- Rishon → pending_decision → Canada PR result
- Canada PR → result_expected → October 2026

---

## 👤 用户基本信息

- **时区**: America/Vancouver ( PDT )
- **飞书账号**: ou_13d5de76e62912757cd56fa20b10a358
- **GitHub账号**: clawrswang-blip
- **Gmail**: clawrswang@gmail.com（gog OAuth 已配置）

## 🎯 核心项目

| 项目 | 状态 | 关键文件 |
|---|---|---|
| Sungiven 会员体系 | C$9,000/月稳定 | `memory/projects/sungiven.md` |
| Sungiven Uber Eats 分析 | **每周例行，已固化工作流** | `memory/projects/sungiven.md` |
| **SFC 团队重组（Team SFC）** | **2026-05-11 启动，与 Paul+Franco+投资人** | `memory/projects/sfc-restructuring.md` |
| **SFC RDC 转型（Franco执行体系）** | **90天倒推，5/12→8/10，51任务+10 KPI+8 SOP** | `memory/projects/sfc-rdc-transformation.md` |
| **Team SFC Rules 草稿 v0.3** | **Franco+Rishon，31页PDF已生成** | `memory/projects/sfc-team-rules-draft.md` + PDF |
| **SFC PMO & Transformation Lead** | **CEO Office；Paul对接；Q3绩效评估正式依据** | `memory/projects/sfc-role-pmo-transformation-lead.md` |
| 国内AI咨询 | 信誉楼跟进中 | `memory/projects/ai-consulting.md` |
| OpenClaw | 核心侧重点60% | `SOUL.md` + `USER.md` |
| PR规划 | 10月出结果 | `memory/projects/pr-plan.md` |

## 🔑 已配置服务

| 服务 | 状态 | 备注 |
|---|---|---|
| GEMINI_API_KEY | ✅ | AIzaSyDWL4... |
| MATON_API_KEY | ✅ | GitHub OAuth 已连接 |
| gog OAuth | ✅ | clawrswang@gmail.com |
| 飞书机器人 | ✅ | Webhook 已配置 |
| 飞书配对 | ✅ | ou_13d5de76e... |
| auto-updater | ✅ | 已安装 |

## 🆕 2026-04-30 libtv-skill 安装
- 来源：https://github.com/libtv-labs/libtv-skills
- 安装路径：`.agents/skills/libtv-skill/`
- 触发关键词：`libtv`
- 能力：文生图/视频、图生视频、编辑修改、风格迁移、短剧/MV/广告生成
- 状态：**⚠️ 需要配置 `LIBTV_ACCESS_KEY`**

## 🆕 2026-06-11 Engineering Loop 完整指南
- 研究来源：Addy Osmani (Loop Engineering)、Anthropic (Context Engineering)、Antigravity Lab (Validation Loops)
- 产出1：`memory/projects/engineering-loop-guide.md` — 完整理论+实践指南
- 产出2：`skills/universal-engineering-loop/SKILL.md` — 可立即使用的模板 Skill
- 核心：6大组件 + 9-Section /goal Template + Maker-Checker 分离 + 验证循环设计

## 🆕 2026-06-10 GSAP Skills 安装
- 来源：https://github.com/greensock/gsap-skills
- 路径：`~/.openclaw/workspace/skills/gsap-*/`
- 8个skills：gsap-core, gsap-timeline, gsap-scrolltrigger, gsap-plugins, gsap-react, gsap-frameworks, gsap-utils, gsap-performance
- 性质：纯指令型skill，无额外系统依赖
- 触发：问动画、滚动效果、React/Vue动画时自动激活

## 🆕 2026-06-16 Agent Reach 安装
- 来源：https://github.com/Panniantong/agent-reach
- 路径：`~/.agent-reach-venv` + `~/.openclaw/skills/agent-reach/`
- 安装方式：venv（pipx 不可用）
- 状态：7/13 渠道已激活（零配置）
- 已激活：网页(Jina)、YouTube字幕、GitHub、RSS、Exa搜索、V2EX、B站搜索
- 待配置：Twitter、小红书、Reddit、雪球、小宇宙、LinkedIn

## ⚙️ Skills 状态

| 类别 | Skills |
|---|---|
| ✅ 开箱即用 | word-docx, powerpoint-pptx, ui-ux-pro-max, deep-research-pro, data-analysis, frontend-design-3, market-research, marketing-skills, seo, self-improving, skill-vetter, ontology, humanizer, agent-browser-clawdbot, polymarket-trade |
| 🔑 需Key | brave-search, youtube-api-skill, n8n |
| 📦 需安装 | mcporter |
| 🔧 已配置 | gog, nano-banana-pro, github-api, feishu-evolver-wrapper |
| 🆕 2026-04-23 | karpathy-coding-principles | Andrej Karpathy LLM coding 纠偏指南；**所有 coding 操作前必读** |
| 🆕 2026-04-27 | fireworks-tech-graph | 技术图表生成（SVG+PNG）；自然语言→图表；支持13种图表类型+7种视觉风格；需 librsvg ✅ |
| 🆕 2026-04-28 | diagram-design | Editorial品牌长文图表skill；14种图表类型（architecture/flowchart/quadrant/pyramid等）；品牌URL onboarding提取颜色字体；3种变体（minimal light/dark/full editorial）；输出自包含HTML/SVG |
| 🆕 2026-05-23 | mattpocock/diagnose | 硬 Bug 诊断 loop：Reproduce → Minimise → Hypothesise → Instrument → Fix → Regression-test |
| 🆕 2026-05-23 | mattpocock/tdd | TDD red-green-refactor loop；垂直切片 tracer bullet；反模式：横向切片 |
| 🆕 2026-05-23 | mattpocock/grill-with-docs | 开发前对齐 session；建立统一语言（Ubiquitous Language）；更新 CONTEXT.md + ADR |
| 🆕 2026-05-23 | mattpocock/grill-me | 非代码场景的 grilling session；彻底理解需求再动手 |
| 🆕 2026-05-23 | mattpocock/prototype | 快速原型开发流程 |
| 🆕 2026-05-23 | mattpocock/improve-codebase-architecture | 代码架构持续改进 |
| 🆕 2026-05-23 | mattpocock/triage | Issue 分类 + 优先级排序 |
| 🆕 2026-05-23 | mattpocock/zoom-out | 从细节中抽离，审视整体设计 |
| 🆕 2026-05-23 | mattpocock/to-prd | 将方案转化为产品需求文档 |
| 🆕 2026-05-23 | mattpocock/to-issues | 将需求转化为具体 issue/ticket |

## 🔒 Coding 工作流强制约定

**每次 coding 操作前（按顺序执行）：**
1. **Step 1 — 对齐（grill）**：先用 `mattpocock/grill-me` 或 `mattpocock/grill-with-docs` 做需求对齐
   - 还没清楚要做什么 → `/grill-me`
   - 有代码库、需要对齐项目语言 + 建 ADR → `/grill-with-docs`
2. **Step 2 — 框架（karpathy）**：加载 `karpathy-coding-principles`，应用 4 大原则
3. **Step 3 — 执行**：根据任务类型选对应 skill
   - 写代码 / 改代码 / build / 跑 coding agent → 其他执行类 skill
   - Bug 调试 → `mattpocock/diagnose`
   - 新功能开发 → `mattpocock/tdd`（tracer bullet 垂直切片）
   - 架构问题 → `mattpocock/improve-codebase-architecture`
   - 快速原型 → `mattpocock/prototype`

**触发条件：** 写代码、改代码、build、跑 coding agent、任何产生 `.py/.js/.ts/.sh` 的任务

**Matt Pocock Skills 安装来源：** `https://github.com/mattpocock/skills`
**安装路径：** `~/.openclaw/workspace/skills/mattpocock/`

## 📝 快捷触发约定

| 指令 | Skill | 说明 |
|---|---|---|
| `横纵分析法` | hv-analysis | 数字生命卡兹克横纵分析法深度研究，产PDF报告 |
| `cz` | khazix-writer | 数字生命卡兹克风格写公众号长文 |
| `Uber 端 Uber 数据分析` | `uber-echarts-dashboard` | Uber Eats CSV → ECharts Dashboard + GitHub Pages |
| `门店端 Uber 数据分析` | `sfc-weekly-report` | SFC Excel → 品类周对比报告 + GitHub Pages |

## ⚠️ 重要教训

- SOUL.md 曾丢失（v4.3之后内容未找回）→ 已建立 memory/ 备份体系
- 信誉楼跟进半年未签 → 尽人事听天命，不过度消耗

## 🗂️ 外置记忆文件树

```
memory/
├── YYYY-MM-DD.md          # 每日日记（自动创建）
├── MEMORY_INDEX.md        # 记忆索引
├── registry/              # 记忆标签注册
├── optimization/          # 动态优化日志
│   └── YYYY-MM-DD.md      # 每周优化报告
└── projects/
    ├── sungiven.md
    ├── ai-consulting.md
    └── pr-plan.md

context_engine/            # Context Layer 架构
├── Taxonomy.md            # 5层分类法 + Context Assembly Protocol
├── MemoryProtocol.md      # 统一记忆协议
├── DynamicOptimizer.md    # 指标 + 阈值 + 动态优化循环
├── SessionHistoryCompression.md
├── SkillContextBridge.md
├── session_boot.py        # Context 组装脚本
├── SessionBootTemplate.md # In-session MCP 协议
├── KG_FactCatcher.md     # 会话内事实捕获协议
├── metrics_logger.py      # 指标记录工具
└── metrics_history.jsonl  # 指标历史

harness_engineering/      # Harness Layer 架构
├── BehavioralHarness.md   # Red Lines + Safety Checks
├── ExecutionHarness.md    # Tool Sequencing + Error Recovery
├── EvaluationHarness.md  # Pre-Output Quality Gate
├── MetaCognitionHarness.md # Self-Knowledge + Assumption Tracking
├── SelfOptimizationHarness.md # Monitor → Diagnose → Adjust → Verify
└── index.md
```

---

## 🏗️ Context Layer 架构状态

| 模块 | 版本 | 状态 |
|------|------|------|
| Context Taxonomy | 1.0 | ACTIVE |
| Memory Protocol | 1.0 | ACTIVE |
| Dynamic Optimizer | 1.0 | ACTIVE |
| Session Compression | 1.0 | ACTIVE |
| Skill Context Bridge | 1.0 | ACTIVE |

详见：`context_engine/index.md`

## ⚙️ Harness Layer 架构状态

| 模块 | 版本 | 状态 |
|------|------|------|
| Behavioral Harness | 1.0 | ACTIVE |
| Execution Harness | 1.0 | ACTIVE |
| Evaluation Harness | 1.0 | ACTIVE |
| Meta-Cognition Harness | 1.0 | ACTIVE |
| Self-Optimization Harness | 1.0 | ACTIVE |

详见：`harness_engineering/index.md`

---

_详细记忆用 memory_search 查询；完整文件用 memory_get 读取指定路径_

## 🆕 2026-06-28 新安装 Skills

| 名称 | 来源 | 状态 |
|---|---|---|
| vibe-portrait | dadwadw233/VibePortrait (GitHub) | ✅ 已安装 |
| caveman | juliusbrussee/caveman (GitHub) | ✅ 已安装（7个子skill） |
| mattpocock/* | mattpocock/skills (GitHub) | ✅ 已存在，跳过 |
| create-plan (adityasanka) | smithery.ai | ❌ Repo不存在，无法安装 |
| tool-advisor-1 | mcpmarket.com | ❌ Repo不存在，无法安装 |

**caveman 子skills:**
- caveman, caveman-commit, caveman-compress, caveman-help, caveman-review, cavecrew, caveman-stats

**vibe-portrait 功能:** 读取对话历史生成 HTML Portrait（MBTI 16型人格颜色主题）+ 开发者画像分析

## Promoted From Short-Term Memory (2026-07-01)

<!-- openclaw-memory-promotion:memory:memory/2026-06-26.md:17:20 -->
- 监控备注: Rishon 沉默持续约43天（May 14 → Jun 26）; May 14 之后无任何消息; 这是有记录以来最长的一次沉默（远超之前任何一次）; 可能原因：SFC Stage 1全力启动 / 极度忙碌 / PR结果等待期（10月） [score=0.893 recalls=0 avg=0.620 source=memory/2026-06-26.md:17-20]
<!-- openclaw-memory-promotion:memory:memory/2026-06-26.md:26:26 -->
- 监控备注: _Luna @ 2026-06-26 08:42 PDT — Rishon 沉默约43天_ [score=0.883 recalls=0 avg=0.620 source=memory/2026-06-26.md:26-26]

## Promoted From Short-Term Memory (2026-07-03)

<!-- openclaw-memory-promotion:memory:memory/2026-06-29.md:12:14 -->
- 备注: 这是 Luna Weekly PM Digest cron job 的首次运行; postmortem/logs/ 目录下无新的 .jsonl 日志; 下次运行时将有 7 天数据可供分析 [score=0.833 recalls=0 avg=0.620 source=memory/2026-06-29.md:12-14]
<!-- openclaw-memory-promotion:memory:memory/2026-06-29.md:5:8 -->
- 本周 PM 汇总: **PM记录：** 0 条（无新 session 日志）; **原因：** cron job 首次运行，无历史数据积累；上次记录为 2026-04-20; **现有错误模式：** 3 条（te/je/sl），均来自 2026-04-20; **下周重点：** 继续积累 PM 数据；验证 error_patterns 等文件是否需更新 [score=0.815 recalls=0 avg=0.620 source=memory/2026-06-29.md:5-8]
