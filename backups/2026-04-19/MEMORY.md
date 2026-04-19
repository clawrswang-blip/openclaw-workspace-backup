# MEMORY.md — 长期记忆索引

_Last updated: 2026-04-16_

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

## ⚙️ Skills 状态

| 类别 | Skills |
|---|---|
| ✅ 开箱即用 | word-docx, powerpoint-pptx, ui-ux-pro-max, deep-research-pro, data-analysis, frontend-design-3, market-research, marketing-skills, seo, self-improving, skill-vetter, ontology, humanizer, agent-browser-clawdbot, polymarket-trade |
| 🔑 需Key | brave-search, youtube-api-skill, n8n |
| 📦 需安装 | mcporter |
| 🔧 已配置 | gog, nano-banana-pro, github-api, feishu-evolver-wrapper |

## 📝 快捷触发约定

| 指令 | Skill | 说明 |
|---|---|---|
| `cz` | khazix-writer | 数字生命卡兹克风格写公众号长文 |

## ⚠️ 重要教训

- SOUL.md 曾丢失（v4.3之后内容未找回）→ 已建立 memory/ 备份体系
- 信誉楼跟进半年未签 → 尽人事听天命，不过度消耗

## 🗂️ 外置记忆文件树

```
memory/
├── YYYY-MM-DD.md          # 每日日记（自动创建）
├── MEMORY_INDEX.md        # 记忆索引
├── registry/              # 记忆标签注册
└── projects/
    ├── sungiven.md
    ├── ai-consulting.md
    └── pr-plan.md
references/
└── (skill 大型参考文档)
```

---

_详细记忆用 memory_search 查询；完整文件用 memory_get 读取指定路径_
