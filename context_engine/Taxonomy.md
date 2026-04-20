# Context Layer Architecture
> All context management must follow this taxonomy. Every context source has a home — and a protocol.

---

## 🏗️ Context Taxonomy（上下文分类法）

Every piece of information that enters the system belongs to exactly one layer. No unlayered context.

```
Layer 1: VOLATILE          → session-internal, session-end discarded or archived
Layer 2: PERSISTENT-ID     → identity core, session-start full load, never modified mid-session
Layer 3: PERSISTENT-PROJ  → project memory, dynamic recall, not fully loaded at boot
Layer 4: EPHEMERAL-SKILL  → skill-scoped, loaded on skill call, released on skill exit
Layer 5: EXTERNAL          → real-time fetch, never pre-loaded, result discarded after use unless archived
```

---

### Layer 1: VOLATILE（会话级易失）

**What belongs here:**
- Full session history (current conversation)
- Runtime state (channel, model, OS, last tool result)
- Task state (current subtask progress)
- Ephemeral decisions made during session

**Lifecycle:**
```
Session Start → Load nothing (session history starts empty)
Session Running → Accumulate here
Session End → Selective archive:
  - Archive decision log → Layer 3 (MemPalace)
  - Archive lesson learned → Layer 3 (memory/YYYY-MM-DD.md)
  - Discard conversation noise
```

**Optimization feedback:** Track "useful recall rate" — how often a volatile fact gets used later. If < 20%, flag for discard protocol.

---

### Layer 2: PERSISTENT-IDENTITY（身份层）

**What belongs here:**
- `SOUL.md` — cognitive framework, decision logic, growth system
- `IDENTITY.md` — Luna's identity card
- `USER.md` — user base profile (updated quarterly or on explicit trigger)

**Lifecycle:**
```
Session Start → FULL LOAD (always, no filtering — it's the identity baseline)
During Session → READ ONLY (never modified mid-session)
Modification → Explicit instruction from user required
```

**Versioning:** Each file tracks `Last Updated` and `Version`. On update, old version archived with reason.

**Dynamic Optimization:**
- Quarterly audit: does identity still reflect current state?
- Monthly check: any outdated preferences in USER.md?
- Each session: am I acting consistently with identity layer?

---

### Layer 3: PERSISTENT-PROJECT（项目层）

**What belongs here:**
- `MEMORY.md` — long-term memory index (NOT the raw memories themselves)
- `memory/projects/*.md` — project deep-dives
- `memory/YYYY-MM-DD.md` — daily raw logs
- MemPalace KG — structured facts with timestamps
- MemPalace Drawers — semantic memories

**Lifecycle:**
```
Session Start → NOT loaded (too large, too noisy)
Task Classification → Determine which project contexts are relevant
Dynamic Recall → Assemble relevant subset (see Context Assembly Protocol)
Post-Session → New learnings archived here
```

**Memory Write Protocol（写入时分类）:**

```
NEW INFORMATION
       │
       ▼
┌──────────────────┐
│ 信息分类          │
├──────────────────┤
│ raw log?          │ → memory/YYYY-MM-DD.md
│ semantic memory?  │ → MemPalace Drawers
│ structured fact?  │ → MemPalace KG
│ long-term index?  │ → MEMORY.md
│ decision?         │ → KG + memory/YYYY-MM-DD.md both
│ lesson learned?   │ → KG (fact) + memory/YYYY-MM-DD.md (narrative)
└──────────────────┘
       │
       ▼
CROSS-SYSTEM CONSISTENCY CHECK
- Does this contradict existing KG facts? → Flag conflict, don't overwrite
- Does this supersede existing drawer? → Update with version reference
```

**Dynamic Optimization:**
- Weekly: scan for expired KG facts (valid_until passed)
- Monthly: compress old daily logs into themed summaries
- Quarterly: full project context review, archive outdated material

---

### Layer 4: EPHEMERAL-SKILL（技能层）

**What belongs here:**
- Current skill's `SKILL.md`
- Skill-specific temp memory
- Skill input/output contracts

**Lifecycle:**
```
Skill Called → Load SKILL.md + relevant context from Layer 2/3
Skill Running → All context lives here, isolated from global context
Skill Done → Output archived:
  - Execution summary → Layer 1 (volatile, for session continuity)
  - Key learnings → Layer 3 (persistent)
  - Context released, SKILL.md unloaded
```

**Context Contract（每个 SKILL.md 必须声明）:**
```markdown
## Context Contract
- My load trigger: [what situation loads me]
- I need from global context: [explicit list]
- I will NOT touch: [explicit boundary]
- I produce: [output schema]
- After me: [where output goes]
```

**Dynamic Optimization:**
- Track skill usage frequency → if < quarterly, flag for merge/deprecate
- Track "context pollution" rate → how often skill leaves unwanted residue
- Track "useful output" rate → how often skill output gets used by downstream

---

### Layer 5: EXTERNAL（外部层）

**What belongs here:**
- Web search results
- API call results (gog, GitHub, Feishu)
- File reads (documents, spreadsheets)
- Third-party data

**Lifecycle:**
```
On-demand fetch → Use in context → Results:
  - Worth keeping → Archive to Layer 3 (MemPalace or file)
  - One-time use → Discard after use
  - Noise (failed fetch, irrelevant) → Discard immediately
```

**No pre-loading:** Never fetch external data before it's needed.

**Dynamic Optimization:**
- Track source reliability scores (e.g., web search: which domains are trusted?)
- Track "useful external data" rate → if < 30%, improve query strategy
- Track fetch cost vs. value → high cost, low value = reframe or skip

---

## 🔄 Context Assembly Protocol（动态组装协议）

**When:** Every session boot (for Layer 3), and before every major task switch.

**Inputs:**
- User's latest message (intent classification)
- User's active projects (from MEMORY.md index)
- Last session's context summary (if exists)

**Steps:**

```
STEP 1: TASK CLASSIFICATION
┌────────────────────────────────────────┐
│ Type: DECISION / ANALYSIS / CREATIVE  │
│       EXECUTION / RESEARCH / CHAT     │
│ Project tags: [which projects apply]  │
│ Time sensitivity: [low / medium / high]│
└────────────────────────────────────────┘
         │
         ▼
STEP 2: RECALL RELEVANT LAYER 3 SOURCES
For each project tag:
  - KG query: entities related to this project
  - MemPalace semantic search: top-5 relevant drawers
  - memory/projects/*.md: check for direct mentions
Score each source: relevance_score 0.0–1.0

         │
         ▼
STEP 3: INJECTION DECISION
┌────────────────────────────────────────┐
│ Score > 0.8 → FULL INJECT             │
│ Score 0.5–0.8 → SUMMARY INJECT        │
│ Score < 0.5 → DO NOT INJECT           │
│                 (can recall on-demand) │
└────────────────────────────────────────┘

         │
         ▼
STEP 4: CONFLICT DETECTION
If multiple sources disagree on the same fact:
  - Annotate ALL versions with [CONFLICT: source A vs source B]
  - Do NOT resolve automatically — surface to session
  - User resolves → update KG with resolved version

         │
         ▼
STEP 5: OUTPUT: PRIORITIZED CONTEXT BUNDLE
{
  "session_type": "...",
  "project_tags": [...],
  "injected_sources": [
    { "source": "...", "score": 0.92, "mode": "full" },
    { "source": "...", "score": 0.67, "mode": "summary" }
  ],
  "conflicts": [...]
}
```

**Self-Monitoring Metrics:**
- `recall_precision`: Of sources recalled, how many were actually used?
- `recall_recall`: Of sources that would have been useful, how many were recalled?
- `conflict_rate`: How often do assembled sources conflict?
- `context_satisfaction`: Post-task survey — did context feel complete? (tracked in memory)

---

## 📊 Dynamic Optimization Loop（动态优化循环）

**Principle:** Every protocol above has a feedback loop. Nothing is static.

```
OPTIMIZATION CYCLE: Every heartbeat (8-12h) + Weekly deep review

┌─────────────────────────────────────────┐
│ METRICS COLLECTION                       │
│                                          │
│ Context Layer Health:                    │
│  - Layer 1: volatile_discard_rate       │
│  - Layer 2: identity_drift_score        │
│  - Layer 3: recall_precision / recall    │
│  - Layer 4: skill_usefulness_rate        │
│  - Layer 5: external_data_value_rate     │
│                                          │
│ Assembly Quality:                        │
│  - conflict_rate                         │
│  - context_satisfaction_score           │
│  - redundant_injection_rate             │
│  - missed_context_rate                  │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│ DIAGNOSIS                                 │
│                                          │
│ If metric < threshold → Flag root cause │
│  - Is the taxonomy wrong?                │
│  - Is the assembly algorithm off?        │
│  - Is the underlying memory stale?      │
│                                          │
│ → Generate diagnosis report              │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│ ADJUSTMENT                                │
│                                          │
│ Taxonomy drift? → Update taxonomy.md      │
│ Assembly bias? → Update assembly logic   │
│ Stale memory? → Trigger refresh cycle   │
│ Skill context leak? → Tighten contract   │
│                                          │
│ → All changes versioned + logged        │
└──────────────────────────────────────────┘
```

**Optimization Triggers:**
- `context_satisfaction < 0.7` → Immediate review of recent assembly runs
- `conflict_rate > 0.15` → Check KG freshness + recall strategy
- `missed_context_rate > 0.25` → Audit recall algorithm
- Weekly: full metric review + protocol adjustment if needed

**Self-Referential Optimization:**
The Dynamic Optimizer itself is subject to optimization. If the optimization process is inefficient, it adjusts itself.

---

## 🔧 Implementation Files

| File | Role |
|------|------|
| `context_engine/Taxonomy.md` | This file — protocol definitions |
| `context_engine/DynamicOptimizer.md` | Metrics, thresholds, adjustment logic |
| `context_engine/MemoryProtocol.md` | Unified memory write/recall/invalidation |
| `context_engine/SessionBoot.py` | Context assembly script |
| `context_engine/MetricsLogger.py` | Metric collection utilities |
| `HEARTBEAT.md` | Trigger point for optimization checks |

---

**Version:** 1.0
**Last Updated:** 2026-04-20
**Owner:** Luna (Context Layer Architect)
**Status:** ACTIVE — subject to dynamic optimization per section above
