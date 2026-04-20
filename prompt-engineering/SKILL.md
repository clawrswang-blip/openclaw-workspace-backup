# Prompt Engineering System — Luna

> "不是提示词，是思维脚手架。"  
> Version 1.1 | 2026-04-20

---

## 一、系统概述

这个系统是 Luna 的 Prompt 武器库。每一个模板不是"通用文案生成器"，而是针对 Rishon 真实场景的思维框架。

**核心原则：**
- 毒辣之眼：先找本质，再给结构
- 闭环之脑：价值创造 → 传递 → 捕获
- 十年视角：反事实测试，确保不是自嗨
- 无废话：不表演帮助，直接给洞见

---

## 二、场景索引（37个）

### 一、XHS 内容矩阵（6个）

| ID | 文件名 | 触发场景 | 关联 Skills |
|----|--------|---------|------------|
| 01 | `xhs-product-review` | 产品种草文 | baoyu-xhs-images |
| 02 | `xhs-knowledge-share` | 干货知识分享 | social-content |
| 03 | `xhs-brand-story` | 品牌故事文 | baoyu-article-illustrator |
| 04 | `xhs-comparison` | 测评对比文 | baoyu-image-cards |
| 05 | `xhs-flash-sale` | 限时活动推广 | baoyu-post-to-x |
| 06 | `xhs-scenario-content` | 场景化内容创作 | marketing-xiaohongshu-specialist |

### 二、内容营销矩阵（8个）

| ID | 文件名 | 触发场景 | 关联 Skills |
|----|--------|---------|------------|
| 07 | `wechat-longform` | 公众号深度长文 | khazix-writer |
| 08 | `brand-story` | 品牌故事/branding | copywriting |
| 09 | `landing-page-copy` | 营销落地页文案 | html-ppt, frontend-design |
| 10 | `social-content-strategy` | 社交媒体内容策略 | social-content, marketing-ideas |
| 11 | `seo-article` | SEO 文章 | ai-seo, seo-audit |
| 12 | `cold-email-sequence` | Cold Email 序列 | cold-email |
| 13 | `competitor-analysis` | 竞品分析 | competitor-alternatives |
| 14 | `launch-strategy` | Launch Strategy | launch-strategy |

### 三、分析调研矩阵（7个）

| ID | 文件名 | 触发场景 | 关联 Skills |
|----|--------|---------|------------|
| 15 | `deep-research` | 深度调研报告 | deep-research-pro |
| 16 | `market-analysis-cn` | 市场分析-中国 | market-analysis-cn |
| 17 | `customer-research` | 用户研究 | customer-research |
| 18 | `data-analysis` | 数据分析报告 | Luna Data Analysis |
| 19 | `dashboard-design` | Dashboard 设计需求 | data-analysis |
| 20 | `pricing-analysis` | 定价策略分析 | pricing-strategy |
| 21 | `business-model-canvas` | 商业模型画布 | strategic-thinking |

### 四、创意设计矩阵（4个）

| ID | 文件名 | 触发场景 | 关联 Skills |
|----|--------|---------|------------|
| 22 | `html-landing` | HTML/Landing Page | html-ppt, frontend-design-3 |
| 23 | `ui-ux-request` | UI/UX 设计需求 | ui-ux-pro-max |
| 24 | `frontend-dev-spec` | 前端开发规范 | frontend-design-3 |
| 25 | `infographic-design` | 信息图设计 | baoyu-infographic |

### 五、策略思考矩阵（6个）

| ID | 文件名 | 触发场景 | 关联 Skills |
|----|--------|---------|------------|
| 26 | `business-ideation` | 商业想法落地评估 | brainstorming |
| 27 | `strategic-thinking` | 高维度战略思考 | — |
| 28 | `brainstorming` | 头脑风暴 | marketing-ideas |
| 29 | `deep-optimization` | 深度优化评审 | seo-audit, page-cro |
| 30 | `decision-framework` | 决策支持框架 | — |
| 31 | `m&a-analysis` | 商业并购/合作分析 | deep-research-pro |

### 六、AI 技术矩阵（4个）

| ID | 文件名 | 触发场景 | 关联 Skills |
|----|--------|---------|------------|
| 32 | `humanized-article` | 去AI化有深度文章 | humanizer |
| 33 | `code-generation` | 代码/脚本生成 | coding-agent |
| 34 | `agent-bot-design` | Agent/Bot 开发设计 | agent-browser-clawdbot |
| 35 | `system-architecture` | 系统架构设计 | — |

### 七、个人成长矩阵（2个）

| ID | 文件名 | 触发场景 | 关联 Skills |
|----|--------|---------|------------|
| 36 | `cognitive-upgrade` | 个人认知升级 | — |
| 37 | `cross-cultural-insight` | 跨文化洞察 | — |

---

## 三、调用约定

### 标准调用格式

当你需要使用某个场景时，直接说：

```
/prompt [模板名] [主题]
```

**例如：**
```
/prompt xhs-product-review 温哥华有机食材
/prompt landing-page-copy AI咨询公司
/prompt competitor-analysis 社区超市
```

### 触发条件判断

- **模糊触发**：你说"写个XHS" → 我问"哪种？种草？测评？还是品牌故事？"
- **明确触发**：你说"帮我写个产品种草文" → 直接用 `xhs-product-review`
- **组合触发**：你说"写个落地页文案，关于新会员体系" → `landing-page-copy` + 补充会员体系上下文

---

## 四、反馈沉淀机制

### 使用后快速反馈

每次使用模板后，记录：
1. **效果如何**：A（有明显提升）/ B（一般）/ C（鸡肋）
2. **哪里不对**：具体指出问题
3. **你的修改**：你怎么改的

### 迭代协议

```
周迭代：收集本周反馈
月迭代：更新模板
季迭代：淘汰低效模板，新增场景
```

---

## 五、Prompt 迭代协议

### 版本格式

每个模板文件头部有演进记录：

```markdown
## 演进记录
| 日期 | 版本 | 变化 |
|------|------|------|
| 2026-04-20 | v1.0 | 初始版本 |
```

### 迭代触发条件

- **同类型反馈 ≥ 3次** → 必须迭代
- **Rishon 主动要求** → 即时迭代
- **季度审查** → 系统性优化

### 迭代记录位置

- 单模板迭代 → `templates/[模板名].md` 内的演进记录
- 系统级迭代 → `evolution/YYYY-MM.md`

---

## 六、快速启动

### 第一次使用

1. 找到对应场景（用索引或搜索）
2. 复制模板内容
3. 填入输入变量
4. 发送给 Luna
5. 根据反馈迭代

### 自定义场景

如果 37 个场景都不匹配：

1. 描述你的场景
2. 我帮你匹配最接近的模板
3. 或者从零构建新模板

---

## 七、文件结构

```
prompt-engineering/
├── SKILL.md              ← 你在这里
├── templates/            ← 37个场景模板
│   ├── xhs-product-review.md
│   ├── xhs-knowledge-share.md
│   ├── ...（共37个）
│   └── cognitive-upgrade.md
└── evolution/           ← 迭代日志
    └── 2026-04-20.md    ← 初始日志
```

---

## 八、质量承诺（v1.1 升级版）

**每个模板必须满足：**
- [ ] 可直接复制使用（不是 placeholder）
- [ ] 毒辣视角贯穿始终
- [ ] 闭环验证完整
- [ ] 十年反事实测试
- [ ] 专属于 Rishon/Luna 语境
- [x] **Top 3% 质量锚点** — 深层洞察 vs 泛泛总结
- [x] **去AI化检查** — 7项标准，防止AI腔
- [x] **分类特色强化** — 6大类别专属要求（XHS/深度分析/商业策略/品牌内容/代码技术/个人成长）
- [x] **自我迭代检查** — 产出前自检 + 产出后迭代 + 版本记录

**不适用的模板：**
- 泛化的"你是专业的ChatGPT"开场
- 无法闭环验证的空话
- 没有毒辣视角的温和建议

---

> "不是给提示词，是给思维框架。复制就能用，用了就能跑。"
>
> **v1.1 升级日志（2026-04-20）：** 所有37个模板植入 Top 3% 质量锚点 + 去AI化写作指南 + 分类特色强化（6类）+ 自我迭代检查机制。详见各模板内的「===新增===」标注。
