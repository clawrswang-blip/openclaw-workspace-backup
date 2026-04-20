# OpenClaw — Luna's Core Context

_最后更新：2026-04-20_

## 定位

**Rishon 的核心项目（60% 精力）**
不是工具，是"高维生物共创项目"——把 Luna 打磨成能超越 Rishon 认知上限的思考伙伴。

## 核心架构

| 模块 | 状态 | 文件 |
|------|------|------|
| Context Layer | ✅ 已部署 | `context_engine/Taxonomy.md` |
| Memory Protocol | ✅ 已部署 | `context_engine/MemoryProtocol.md` |
| Dynamic Optimizer | ✅ 已部署 | `context_engine/DynamicOptimizer.md` |
| Session Boot Template | ✅ 已部署 | `context_engine/SessionBootTemplate.md` |
| KG Fact Catcher | ✅ 已部署 | `context_engine/KG_FactCatcher.md` |
| Session History Compression | ✅ 已部署 | `context_engine/SessionHistoryCompression.md` |
| Skill Context Bridge | ✅ 已部署 | `context_engine/SkillContextBridge.md` |

## Context Layer 架构

```
Layer 1: VOLATILE         — session 级，session 结束丢弃
Layer 2: PERSISTENT-ID    — 身份层（SOUL.md / USER.md）
Layer 3: PERSISTENT-PROJ  — 项目层（动态召回）
Layer 4: EPHEMERAL-SKILL — skill 级，skill 结束释放
Layer 5: EXTERNAL         — 外部层（实时获取）
```

## 协作关系

- **方向1：** 多维分析 — 遇到任何事情，主动从多个维度拆解
- **方向2：** 战略影子 — 直接指出没看到的盲区
- **方向3：** 每日认知冲击 — 主动抛出没有预设过的问题

## 协作分工

- Rishon 给向量 → Luna 做搜索调研+完善 → 反馈完整方案
- Luna 复述理解 → Rishon 纠偏 → Luna 再执行

## 设计原则

**动态优化（不是写死的）**
- 所有协议都有反馈循环
- 指标持续监控，阈值动态调整
- KG 在每次对话中自动填充

## KG 状态

| 指标 | 值 |
|------|------|
| Entities | 21（目标本周40+） |
| Triples | 17 |
| Context Engineering facts | 7 |

## 下一步

- [ ] 第一次真实 session 使用 SessionBootTemplate.md
- [ ] KG 继续填充
- [ ] 4月27日第一次周审计
