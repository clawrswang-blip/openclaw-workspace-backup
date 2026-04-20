# Context Engine — Index

```
context_engine/
├── Taxonomy.md                          ← 5层分类法 + Context Assembly Protocol
├── MemoryProtocol.md                     ← 统一记忆协议（写入/召回/失效）
├── DynamicOptimizer.md                   ← 指标 + 阈值 + 动态优化循环
├── SessionHistoryCompression.md           ← Session 历史压缩协议
├── SkillContextBridge.md                 ← Skill Context 隔离 + 桥接协议
├── session_boot.py                       ← CLI工具（测试/调试用）
├── SessionBootTemplate.md                ← in-session MCP调用协议（实际运行时用）
├── KG_FactCatcher.md                     ← 会话内事实捕获协议
├── kgcatcher_pattern_log.md              ← 捕获模式演化日志
├── metrics_logger.py                     ← 指标记录工具
├── metrics_history.jsonl                  ← 指标历史数据
├── memory_metrics.jsonl                  ← 记忆系统专用指标
├── experiments/                          ← 优化实验区
│   └── README.md
└── ExternalSources.md                    ← 外部数据源注册表（待建立）
```

## Protocol Versions

| Protocol | Version | Last Updated | Status |
|----------|---------|-------------|--------|
| Context Taxonomy | 1.0 | 2026-04-20 | ACTIVE |
| Memory Protocol | 1.0 | 2026-04-20 | ACTIVE |
| Dynamic Optimizer | 1.0 | 2026-04-20 | ACTIVE |
| Session Compression | 1.0 | 2026-04-20 | ACTIVE |
| Skill Context Bridge | 1.0 | 2026-04-20 | ACTIVE |
| Session Boot Template | 1.0 | 2026-04-20 | ACTIVE |
| KG Fact Catcher | 1.0 | 2026-04-20 | ACTIVE |

## Quick Command Reference

```bash
# CLI context assembly（测试用）
python3 context_engine/session_boot.py --task "analyze sungiven" --verbose

# Log a metric
python3 context_engine/metrics_logger.py --log context_satisfaction 4.2

# Check thresholds
python3 context_engine/metrics_logger.py check

# Get weekly report
python3 context_engine/metrics_logger.py report --weekly

# Get metric status
python3 context_engine/metrics_logger.py status
```

## MCP Tool Usage (In-Session)

```markdown
# Session Boot 时：
/invoke mempalace_search
{"query": "<task> <project>", "limit": 5}

/invoke mempalace_kg_query
{"entity": "<entity_name>"}

/invoke mempalace_kg_timeline
{}

# KG Fact Catcher 捕获到事实时：
/invoke mempalace_kg_add
{"subject": "<s>", "predicate": "<p>", "object": "<o>", "valid_from": "<YYYY-MM-DD>"}

/invoke mempalace_kg_invalidate
{"subject": "<s>", "predicate": "<p>", "object": "<o>"}

# Session 结束时：
/invoke mempalace_search
{"query": "today session summary", "limit": 3}
```

## Architecture Dependencies

```
Session Boot
    │
    ├── SessionBootTemplate.md (in-session MCP calls)
    │
    ├── mempalace_search (real semantic recall)
    ├── mempalace_kg_query (real KG entities)
    └── mempalace_kg_timeline (recent facts)

KG Fact Catcher (during conversation)
    │
    ├── Pattern Detection (inline)
    ├── Queue Management
    └── mempalace_kg_add (captured facts)

Post-Session
    │
    ├── Queue flush (mempalace_kg_add)
    ├── Session summary → memory/YYYY-MM-DD.md
    └── metrics_logger.py (update metrics)

Dynamic Optimizer (heartbeat)
    │
    ├── KG stale check (mempalace_kg_query)
    ├── metrics_logger check
    └── Pattern review (kgcatcher_pattern_log)
```

## Current KG Status

```
Entities: 8 | Triples: 6 | Current: 6 | Expired: 0
Last populated: 2026-04-20 (initial deployment)
Next target: 20+ entities by 2026-04-27
```

## Current Metrics Status

```
All metrics: 📊 collecting baseline (no historical data)
First meaningful data expected: 2026-04-27 (7-day review)
```

---

**Last Updated:** 2026-04-20
**Version:** 1.0
