# Unified Memory Protocol
> One truth, multiple views. Every memory has exactly one source of truth.

---

## 🏛️ Memory Architecture

Three systems, one protocol. No duplication without annotation.

```
┌─────────────────────────────────────────────────────┐
│                  SOURCE OF TRUTH                     │
│                                                      │
│  ┌───────────────┐                                  │
│  │ memory/*.md   │ ← Raw logs (daily, unstructured) │
│  └───────┬───────┘                                  │
│          │                                           │
│          ▼                                           │
│  ┌───────────────────┐                              │
│  │  MemPalace KG     │ ← Structured facts (entity, │
│  └───────┬───────────┘    predicate, object, time) │
│          │                                          │
│          ▼                                          │
│  ┌───────────────────┐                              │
│  │  MemPalace Drawers │ ← Semantic memories        │
│  └───────┬───────────┘    (full content, indexed)  │
│          │                                          │
│          ▼                                          │
│  ┌───────────────────┐                              │
│  │  MEMORY.md         │ ← Long-term index (entry    │
│  └───────────────────┘    points, NOT raw content)  │
│                                                      │
│  KG ──→ Drawers: KG fact can point to drawer       │
│  Drawers ──→ KG: Drawer can contain structured fact │
│  Both ──→ MEMORY.md: Index updated on any write    │
│  MEMORY.md ──→ Both: Index points to both          │
└─────────────────────────────────────────────────────┘
```

---

## 📥 Memory Write Protocol（写入协议）

**Trigger:** Any new information that should persist beyond the current session.

**Step 1: Classify**

```
INFORMATION TYPE → DESTINATION

┌──────────────────────────────────┬────────────────────────────┐
│ Type            │ Description     │ Destination               │
├─────────────────┼─────────────────┼────────────────────────────┤
│ RAW_LOG         │ 日志/事件/对话   │ memory/YYYY-MM-DD.md      │
│ FACT            │ 可结构化的三元组 │ MemPalace KG              │
│ SEMANTIC        │ 完整语义内容    │ MemPalace Drawers         │
│ DECISION        │ 决定+理由       │ KG (fact) + daily log     │
│ LESSON          │ 教训+洞察       │ KG (fact) + daily log     │
│preference_update│ 用户偏好变更   │ USER.md + KG (fact)       │
│ PROJECT_UPDATE  │ 项目进展        │ memory/projects/*.md + KG  │
│ RELATIONSHIP    │ 实体间关系      │ KG                        │
│ IDENTITY_CHANGE │ Luna自我认知变更│ SOUL.md + KG (fact)       │
└─────────────────┴─────────────────┴────────────────────────────┘
```

**Step 2: Check for Conflicts**

Before writing to KG, check if contradicting fact exists:
```
query KG: same subject + same predicate?
  → If exists with different object:
      FLAG CONFLICT
      Write BOTH with [CONFLICT] annotation
      Do NOT overwrite — user must resolve
      → After resolution, write resolved version with supersedes link
  → If no conflict:
      Write new fact with valid_from = today
```

**Step 3: Write to All Relevant Systems**

```
Example: "Rishon decided to focus 60% on OpenClaw"

KG Write:
  subject: Rishon
  predicate: energy_allocation
  object: OpenClaw 60%
  valid_from: 2026-04-20
  source: USER.md (direct)
  confidence: verified
  supersedes: [previous energy_allocation fact if exists]

MEMORY.md Update:
  → Add index entry: "energy_allocation: OpenClaw 60% (2026-04-20) → see KG"

memory/YYYY-MM-DD.md:
  → "14:32 Rishon: 60% energy to OpenClaw. Decision rational: [reason from conversation]"
```

**Step 4: Cross-System Link**

After any write, update the index:
```
In the relevant MEMORY.md section:
  Last updated: 2026-04-20
  KG facts: [count]
  Latest: [entity] → [predicate] → [object] ([date])
```

---

## 📤 Memory Recall Protocol（召回协议）

**Trigger:** When context assembly needs to find relevant information.

### Recall Path by Information Type

**Structured Fact (entity relationship):**
```
→ MemPalace KG query
→ If found: return with source + confidence + time bounds
→ If not found: log "KG miss" for optimization
```

**Semantic Content (concepts, discussions, narratives):**
```
→ MemPalace semantic search (top-K by relevance)
→ If found: return drawer content + room/wing metadata
→ If not found: try KG semantic search
→ If still not found: log "semantic miss" for review
```

**Project Context:**
```
→ memory/projects/[project].md (if exists)
→ Also: KG query for project-related entities
→ Also: MemPalace semantic search for project name
```

**Decision History:**
```
→ KG query: all facts with predicate "decided" or "chose"
→ Filter by date range / project tag
→ Return with decision rationale (if stored in drawer)
```

**User Preference:**
```
→ USER.md first (authoritative)
→ KG as secondary (for time-sensitive preferences)
→ If conflict: prefer USER.md but flag KG discrepancy
```

---

## 🔄 Memory Invalidation Protocol（失效协议）

**Principle:** Old facts don't disappear — they're marked as ended.

### Invalidation Triggers

```
┌─────────────────────────────────────────────┐
│ TRIGGER TYPE           │ ACTION               │
├────────────────────────┼──────────────────────┤
│ valid_until passed     │ Auto-mark expired    │
│ Time-sensitive event   │ KG update + notification│
│ User correction        │ Mark superseded + new│
│ External contradiction │ Mark conflict + warn │
│ Explicit delete        │ Soft delete (trash)  │
└────────────────────────┴──────────────────────┘
```

### KG Invalidation Procedure

```
For fact (subject, predicate, object):
  1. Query: any newer fact with same subject+predicate?
     → If yes: this fact is now superseded
     → Mark: ended = today
     → Set supersedes link to newer fact
  2. If explicit correction:
     → Add new fact with supersedes link to old
     → Old fact marked: [SUPERSEDED by: new_fact_id]
```

### Auto-Expiration Rules

| Fact Type | valid_until Default | Example |
|-----------|-------------------|---------|
| Project milestone | Project end date | "App v2 launch: 2026-Q4" |
| Temporary decision | 3 months | "Pilot program: ends 2026-07-01" |
| Pending event | Event date + 7 days | "PR result: 2026-10-XX + 7d" |
| Preference | None (permanent) | Unless explicitly updated |
| Structural fact | None | "Rishon → lives_in → Vancouver" |

---

## 📊 Memory Optimization Metrics

**Per-Write Metrics:**
- `write_consistency_score`: Did write follow protocol? (self-audit)
- `cross_link_success_rate`: Were all systems updated?
- `conflict_detection_rate`: How often did we catch conflicts pre-write?

**Per-Recall Metrics:**
- `kg_recall_precision`: KG hits / total KG queries
- `drawer_recall_precision`: Drawer hits / total drawer queries
- `miss_rate`: Total misses / total recall attempts

**Cross-System Metrics:**
- `index_accuracy`: Is MEMORY.md index correct? (audit bi-weekly)
- `stale_fact_rate`: KG facts past valid_until that weren't invalidated
- `orphaned_drawer_rate`: Drawers with no incoming links

**Optimization Triggers:**
- `stale_fact_rate > 0.05` → Run KG cleanup cycle
- `orphaned_drawer_rate > 0.10` → Run drawer audit
- `miss_rate > 0.30` → Review recall algorithm

---

## 🔧 Implementation

| File | Role |
|------|------|
| `context_engine/MemoryProtocol.md` | This file |
| `context_engine/SessionBoot.py` | Implements recall + assembly |
| `context_engine/MetricsLogger.py` | Tracks recall/write metrics |
| `HEARTBEAT.md` | Weekly KG cleanup trigger |

**Tool Usage:**
- `mempalace_kg_add` — write structured facts
- `mempalace_kg_invalidate` — end old facts
- `mempalace_search` — semantic recall
- `mempalace_kg_query` — structured recall
- `memory_search` + `memory_get` — file-based recall

---

## 🌀 Dynamic Self-Optimization

Every week, the memory system reviews its own performance:

```
WEEKLY MEMORY AUDIT:
1. Count KG facts: total / expired / superseded / active
2. Count orphaned drawers
3. Calculate miss_rate by type
4. Identify top-3 recall failures → analyze root cause
5. If root cause is taxonomy issue → propose update to Taxonomy.md
6. If root cause is recall algorithm → update SessionBoot.py
7. Log all changes to memory/YYYY-MM-DD.md
```

**Protocol Versioning:**
- Protocol changes versioned in file header (v1.0 → v1.1)
- Each version logs what changed and why
- 30-day trial: new protocol runs parallel before full switch

---

**Version:** 1.0
**Last Updated:** 2026-04-20
**Owner:** Luna (Memory Architect)
**Status:** ACTIVE — self-optimization loop running
