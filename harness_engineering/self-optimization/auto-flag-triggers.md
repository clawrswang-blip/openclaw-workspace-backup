# Auto-Flag Triggers
> 自动标记系统——当这些事件发生时，自动记录到 improvement-tracker。不需要等 Session End。

---

## 🔴 高优先级触发（立即记录）

### TRIGGER 1: Rishon 纠正我
```
触发条件：Rishon 说「不对」「不是这样」「你在胡说」「重新来」
记录内容：
  - 原始输出是什么
  - Rishon 的纠正是什么
  - 我为什么会错（假设）
  - 如何避免下次犯同样的错
写入位置：improvement-tracker.md → 🔴 未解决问题
```

### TRIGGER 2: 工具调用失败
```
触发条件：任何工具返回 error
记录内容：
  - 工具名和错误类型
  - 我的处理方式（重试/换工具/放弃）
  - 最终结果
写入位置：improvement-tracker.md → Session 记录
```

### TRIGGER 3: 上下文失效
```
触发条件：Rishon 说「你不知道这个吗」「我之前说过的」
记录内容：
  - 缺失的上下文是什么
  - 应该在哪个环节获取到
  - 如何强制触发获取
写入位置：improvement-tracker.md → 🔴 未解决问题
```

### TRIGGER 4: 信心崩塌
```
触发条件：我在 MEDIUM 或 LOW confidence 区间回答了复杂问题
记录内容：
  - 问题是什么
  - 我说了「我不确定」了吗
  - Rishon 后续有补充关键信息吗
写入位置：Session 记录 + knowledge gap 列表
```

---

## 🟡 中优先级触发（24小时内记录）

### TRIGGER 5: 产出国籍化（被发现）
```
触发条件：Rishon 或任何人说「这太像AI写的了」
记录内容：
  - 哪个产出被指出
  - 具体哪里暴露了
  - 如何修改 Prompt 模板
写入位置：对应 Prompt 模板的迭代记录
```

### TRIGGER 6: 遗漏关键信息
```
触发条件：对话中途发现 Rishon 之前说过某事，但我没有用上
记录内容：
  - 遗漏了什么
  - 为什么没有触发召回
  - 是否需要调整 Context 召回机制
写入位置：improvement-tracker.md
```

### TRIGGER 7: 效率问题
```
触发条件：同一个任务花了超过预期的时间（>2x）
记录内容：
  - 任务类型
  - 预期时间 vs 实际时间
  - 慢在哪个环节
写入位置：Session 记录
```

---

## 🟢 低优先级触发（周审时处理）

### TRIGGER 8: 指标趋势异常
```
触发条件：任何指标连续 3 天偏离目标值
记录内容：
  - 哪个指标
  - 偏离幅度
  - 可能的关联因素
写入位置：improvement-tracker.md → 🔴 未解决问题
```

### TRIGGER 9: 新 pattern 发现
```
触发条件：发现 Rishon 的新偏好/新习惯（通过对话推断）
记录内容：
  - pattern 描述
  - 证据（哪次对话）
  - 如何影响未来的行为
写入位置：USER.md 或 MemPalace KG
```

### TRIGGER 10: Skill 失效
```
触发条件：调用的 Skill 没有给出预期结果
记录内容：
  - Skill 名
  - 预期 vs 实际
  - 是否需要报告 Skill 问题
写入位置：Session 记录 + 如果是系统性 bug → Skill 维护者报告
```

---

## 📝 快速记录格式

当触发事件发生时，用以下格式记录：

```
===OPT-FLAG===
TIME: [YYYY-MM-DD HH:MM]
TRIGGER: [触发器编号 + 名称]
CONTENT: [具体内容，3句话内]
ACTION: [已采取的行动，如有]
SEVERITY: [高/中/低]
===END-OPT-FLAG===
```

**记录位置：**
- 高优先级 → `improvement-tracker.md` 的 🔴 未解决问题表格
- 中优先级 → 对应 Session 记录
- 低优先级 → 周末统一处理

---

## 🚫 过滤规则（不要记录的）

以下情况**不需要**记录：
- Rishon 只是改变了主意（不是我的错误）
- Rishon 提供了新信息来帮助我（不是纠正）
- 外部系统正常报错（如 web_search 无结果）
- Heartbeat 例行检查

---

**最后更新：** 2026-04-20
**版本：** 1.0
**状态：** ACTIVE
