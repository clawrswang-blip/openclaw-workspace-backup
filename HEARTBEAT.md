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

## 重要日期提醒（提前一周）：
- 2026年10月：PR 结果出炉 → 提前 1 个月开始检查 Rishon 的 Plan B 预案
- 2026 Q3/Q4：Sungiven App 第二版完成节点

## 不需要检查的（已稳定）：
- gog email/calendar：目前没有配置主动推送，gog OAuth 虽已授权但还未做过深度集成
- 天气：温哥华天气对 Rishon 的日程暂无重大影响
```

---

# Keep this file non-empty to enable heartbeat mode.
# If empty or only comments, heartbeat is disabled.
