# SESSION_END.md
> 每次 Session 结束前必须执行。不可跳过。

---

## 触发条件

以下任一情况发生时，执行本协议：
- `/end` 或 `/reset` 命令
- 对话出现明显终止信号（15分钟无响应 + Rishon 说"就这样"）
- Heartbeat 模式检测到 Session 静默 > 30 分钟

---

## 执行步骤

### STEP 1: 记录本次 Session 关键指标

```bash
python3 context_engine/metrics_logger.py --log session_context_satisfaction <1-5>
python3 context_engine/metrics_logger.py --log session_correction_rate <0-1>
python3 context_engine/metrics_logger.py --log tool_success_rate <0-1>
```

**评分标准（每次必须自评）：**

| 指标 | 1 | 2 | 3 | 4 | 5 |
|------|---|---|---|---|---|
| **session_context_satisfaction** | context 完全失效 | 多次缺失关键信息 | 基本满足，有疏漏 | 较好，偶尔多余信息 | 完美，按需精确 |
| **session_correction_rate** | >50% 输出被纠正 | 20-50% 被纠正 | 10-20% 被纠正 | <10% 被纠正 | 零纠正 |
| **tool_success_rate** | <60% | 60-75% | 75-90% | 90-95% | >95% |

---

### STEP 2: 捕获本次 Session 事实

**必须记录的字段：**

```
## [YYYY-MM-DD HH:MM] Session Summary

### 任务类型
[单次任务 / 多任务会话 / 深度讨论 / 系统构建 / 其他]

### 核心产出
[本次最重要的1-3个产出，用一句话描述]

### 问题记录（自动标记）
- ❌ 失败的工具调用：[工具名] - [错误原因]
- ⚠️ 上下文失效：[什么信息需要但没有获取到]
- 🔴 用户纠正：[Rishon 纠正了什么]（如果 correction_rate > 0）
- 💡 我意识到我不知道的：[我不确定但尝试回答了的问题]

### Rishon 的隐含反馈
[他说了什么暗示他不满意/满意的话？语气、措辞、提问方式]

### 本次学到的
[关于 Rishon 的新观察 / 关于任务的新理解 / 关于工具的新用法]
```

---

### STEP 3: 沉淀为改进输入

**写入 `self-optimization/improvement-tracker.md`：**

```
### [YYYY-MM-DD] 待处理问题
- [具体问题描述]
- 触发场景：[在什么情况下这个问题出现了]
- 影响评估：[高/中/低 - 影响的是核心产出质量还是只是小麻烦]

### [YYYY-MM-DD] 验证闭环
- [之前标记的问题] → [这次有没有改善？]
```

---

### STEP 4: KG Fact 刷新（如果有必要）

如果有新事实产生（关于 Rishon 的偏好、项目状态、决策），立即写入 MemPalace KG：

```bash
mempalace_kg_add <subject> <predicate> <object> [valid_from=YYYY-MM-DD]
```

---

### STEP 5: 更新今日 Memory

追加到 `memory/YYYY-MM-DD.md`：

```
## Session End：[HH:MM]
- 核心产出：[1-2句]
- 问题：[如有]
- 下次注意：[如有]
- 改进输入已沉淀至：self-optimization/improvement-tracker.md
```

---

## 快捷命令

在 OpenClaw 对话中，输入 `/session-end` 可手动触发本协议。

---

## ⚠️ 禁止行为

- ❌ 跳过 STEP 1（不记录指标 = 无法追踪改进）
- ❌ 只记录不沉淀（写了不看 = 浪费时间）
- ❌ 模糊描述问题（"有点问题" 不可接受，必须具体）

---

**最后更新：** 2026-04-20
**版本：** 1.0
**状态：** ACTIVE
