# HEARTBEAT.md

## Rishon 的心跳检查清单

```markdown
# 心跳模式：每 8-12 小时检查一次（白天活跃期）
# 深夜（23:00-08:00）除非紧急，静止

## 每周一：战略检查
- Sungiven 会员数据：上周增长情况，离 10 万目标还有多远？
- 国内 AI 咨询公司：新项目进展？信誉楼有新消息吗？
- OpenClaw：有没有值得记录的使用心得或迭代方向？

## 每日（可选）：
- Rishon 有没有给我新的方向或向量？（如果是，记录到 memory/YYYY-MM-DD.md）
- Rishon 最近问了什么新问题？（可以帮助我更新上下文）

## 🧠 MemPalace Recall 协议（每次心跳自动执行）：
收到 Rishon 消息时，如果涉及以下主题，立刻查询 Palace：
- 项目进展（Sungiven、AI咨询）→ `mempalace_search` 项目名
- 人物相关（信誉楼联系人、合伙人）→ `mempalace_kg_query` 实体名
- 决策时间点（PR日期、App上线节点）→ `mempalace_kg_query` 查 KG
- 偏好/习惯（沟通偏好、工作风格）→ `mempalace_search` 查 preferences room

## 🏗️ Context Layer 健康检查（每周二、四执行）
每次心跳时按如下检查：

### 1. KG Fact 检查
```
查询 KG 中所有 valid_until 在未来 30 天内的事实：
- 如果 today > valid_until → 调用 kg_invalidate 标记 expired
- 如果发现矛盾（same subject+predicate, different object）→ 写入 today memory 并提醒用户
```

### 2. 优化指标抽查
```bash
python context_engine/metrics_logger.py check
# 如果有 violation → 记录到 memory/YYYY-MM-DD.md + 写入 context_engine/optimization/
```

### 3. Context Assembly 质量抽检
```
回顾最近一次 session 的 context assembly：
- injected_sources 有多少真正被用到？（从对话中判断）
- skipped_sources 是否有重大遗漏？
- 如果发现遗漏 → 记录到 context_engine/metrics_history.jsonl
```

### 4. Stale Memory 检查
```
如果 memory/projects/*.md 或 MEMORY.md 超过 14 天未更新：
- 检查对应 KG 事实是否 still valid
- 标记需要 review 的文件
```

## ⚡ 动态优化触发条件（不在常规心跳里，遇到即执行）

| 触发条件 | 执行动作 |
|---------|---------|
| context_satisfaction < 3.0 | 立即生成诊断报告 → memory/optimization/ |
| conflict_rate > 0.25 | 检查 KG freshness + 回滚策略 |
| kg_stale_rate > 0.15 | 运行 KG cleanup cycle |
| skill_context_leak_rate > 0.05 | 立即 review 涉事 skill 的 Context Contract |
| 用户明确投诉 context 不完整 | 记录问题 + 回溯 assembly 过程 |

## 📊 Metrics 日志写入触发
```
每次 session 结束前，写入：
python context_engine/metrics_logger.py --log session_context_satisfaction <1-5>
python context_engine/metrics_logger.py --log session_conflict_rate <0-1>
```

## 重要日期提醒（提前一周）：
- 2026年10月：PR 结果出炉 → 提前 1 个月开始检查 Rishon 的 Plan B 预案
- 2026 Q3/Q4：Sungiven App 第二版完成节点

## 不需要检查的（已稳定）：
- gog email/calendar：目前没有配置主动推送，gog OAuth 虽已授权但还未做过深度集成
- 天气：温哥华天气对 Rishon 的日程暂无重大影响
```

---

# Context Layer Architecture — 执行入口

所有 Context 层协议定义在 `context_engine/` 目录：

| 文件 | 作用 |
|------|------|
| `context_engine/Taxonomy.md` | 5层 Context 分类法 + 组装协议 |
| `context_engine/MemoryProtocol.md` | 统一记忆写入/召回/失效协议 |
| `context_engine/DynamicOptimizer.md` | 指标定义 + 阈值 + 动态优化循环 |
| `context_engine/SessionHistoryCompression.md` | Session 历史压缩协议 |
| `context_engine/SkillContextBridge.md` | Skill Context 隔离+桥接协议 |
| `context_engine/session_boot.py` | Context 组装脚本（Layer 3 动态召回） |
| `context_engine/metrics_logger.py` | 指标记录工具 |

---

# Keep this file non-empty to enable heartbeat mode.
# If empty or only comments, heartbeat is disabled.
