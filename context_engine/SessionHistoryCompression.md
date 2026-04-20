# Session History Compression Protocol
> Long sessions don't need full history. Keep signal, discard noise.

---

## 📐 Compression Architecture

```
Session History
      │
      ▼
┌─────────────────────────────────────┐
│ SEGMENTER                            │
│                                      │
│ Split by topic/task boundaries       │
│ Mark: [TOPIC_A], [TOPIC_B], [CHAT] │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│ CLASSIFIER                           │
│                                      │
│ PERMANENT: decisions, key insights   │
│ EPHEMERAL: chat, confirmations      │
│ BRIDGING: context needed for next   │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│ COMPRESSOR                           │
│                                      │
│ PERMANENT → compress (keep essence)  │
│ EPHEMERAL → discard (maybe log)     │
│ BRIDGING → keep full (low cost)     │
└──────────────────┬──────────────────┘
                   │
                   ▼
COMPRESSED SESSION
- Recent N messages: full
- Older messages: summaries only
- Key decisions: full preserved
- Topic transitions: marked
```

---

## 🎯 Classification Rules

### PERMANENT（永久保留）

```
Keep full message when:
- Contains a decision (chose X over Y because Z)
- Contains user preference update
- Contains a commitment ("I'll do X by Y")
- Contains a key insight or lesson
- Contains new project context
- Contains conflict resolution
- Contains constraint change

Keep as compressed summary:
- Long analysis/explanation (extract the conclusion)
- Research results (extract key facts only)
- Multiple similar messages (merge into one summary)
```

### EPHEMERAL（会话结束即丢弃）

```
Discard immediately when:
- Casual acknowledgment ("ok", "thanks", "sure")
- Simple confirmation ("yes", "no")
- Repetitive confirmation of same point
- Tangential banter (random topic changes)
- "Can you help me with X?" (already captured in topic tag)
- Test messages ("are you there?", "hello")
- Platform-specific noise (reactions, stickers, etc.)
```

### BRIDGING（跨 topic 桥接保留）

```
Keep for context continuity:
- Current task state ("continuing from above")
- Unfinished business ("we were discussing X")
- Pending user decisions
- Active subagent tasks in flight
- External system state (API calls in progress)
```

---

## 📊 Compression Thresholds

| Session Length | Keep Recent | Compress Older | Summary Frequency |
|---------------|-----------|----------------|------------------|
| < 20 messages | All | N/A | N/A |
| 20-50 messages | Last 10 full | Full history | One summary at midpoint |
| 50-100 messages | Last 15 | Compress to 20 | One summary per 25 |
| 100-200 messages | Last 20 | Compress to 30 | One summary per 30 |
| > 200 messages | Last 30 | Compress to 40 | Per topic block |

---

## 🔧 Compression Algorithm

### Step 1: Topic Segmentation

```
Signal markers for new topic:
- User message contains explicit topic shift: "moving on to X"
- Task type changes (analysis → creative)
- New project tag detected
- After 10+ messages of silence (>30min gap)

Each segment: [SEGMENT_ID] [TOPIC_TAG] [START_MSG_ID] [END_MSG_ID]
```

### Step 2: Per-Message Classification

```
For each message in segment:
  1. Check if matches EPHEMERAL patterns
     → If yes: mark EPHEMERAL
  2. Check if matches PERMANENT patterns
     → If yes: mark PERMANENT (full or compressed)
  3. If neither: mark EPHEMERAL by default
```

### Step 3: Summary Generation

```
For EPHEMERAL segments kept as summary:
  Generate one-line summary:
  "[TOPIC]: [key_point] [conclusion_if_any]"

Format:
  "User explored X, no decision made"
  "Discussed Y, agreed to revisit next session"
  "Quick clarification on Z, done"
```

### Step 4: Bridge Preservation

```
Detect bridges:
- If message references earlier content ("as we discussed")
- If task state is incomplete
- If user said "leave this for later"

Mark as BRIDGING with forward reference:
  "BRIDGING: unfinished X → revisit in next session"
```

---

## 🧠 Dynamic Optimization of Compression

### Metrics Tracked

| Metric | Definition | Target |
|--------|-----------|--------|
| `compression_ratio` | (compressed length) / (original length) | 0.3–0.6 |
| `recall_hit_rate` | Historical context successfully recalled / total recalls | > 0.80 |
| `important_miss_rate` | Important info was discarded / total important info | < 0.05 |
| `noise_reduction` | Ephemeral filtered / total ephemeral | > 0.70 |

### Self-Tuning

```
If recall_hit_rate < 0.75:
  → Review last 10 discards for false negatives
  → Add to PERMANENT rules: patterns that were wrongly discarded
  → Version bump compression_rules.md

If important_miss_rate > 0.10:
  → Audit: which categories are getting dropped?
  → Add specific patterns to PERMANENT rules
  → Version bump compression_rules.md

If compression_ratio < 0.2:
  → Too aggressive — losing context
  → Raise threshold, add more EPHEMERAL exceptions

If compression_ratio > 0.8:
  → Not aggressive enough — still too much noise
  → Lower threshold, expand EPHEMERAL patterns
```

---

## 🔄 Session-End Write-Back Protocol

**When session ends, compressed history writes back to memory:**

```
Session End Trigger:
  │
  ▼
COMPRESS
  │
  ▼
┌──────────────────────────────────────┐
│ SELECTIVE MEMORY WRITE                │
│                                       │
│ Extract from PERMANENT:                │
│  - Decisions → KG (structured fact)   │
│  - Key insights → MemPalace Drawer    │
│  - User preferences → USER.md + KG    │
│  - Lessons learned → memory/YYYY-MM-DD│
│                                       │
│ Discard:                               │
│  - All EPHEMERAL                      │
│  - Full message history               │
│                                       │
│ Archive:                               │
│  - Compressed summary → memory/sessions│
│  - Metrics → context_engine/metrics   │
└──────────────────────────────────────┘
```

**Compressed session archive format:**
```
memory/sessions/
  └── 2026-04-20/
      └── 143022_compressed.json
```

JSON structure:
```json
{
  "session_id": "2026-04-20_143022",
  "duration_minutes": 47,
  "task_type": "ANALYSIS",
  "project_tags": ["openclaw", "sungiven"],
  "topic_segments": [
    { "id": 1, "tag": "context_layer_design", "message_count": 12, "summary": "Discussed taxonomy..." },
    { "id": 2, "tag": "implementation", "message_count": 23, "summary": "Drafted context_engine/Taxonomy.md..." }
  ],
  "decisions": [
    { "decision": "Prioritize P0-1 before P0-2", "rationale": "Foundational first" }
  ],
  "key_insights": [
    "Context volatility rate is the key metric"
  ],
  "next_steps": [
    "Implement session_boot.py",
    "Test context assembly"
  ],
  "compression_ratio": 0.41,
  "important_missed": 0
}
```

---

## 🔧 Implementation

| File | Role |
|------|------|
| `context_engine/SessionHistoryCompression.md` | This protocol |
| `context_engine/compression_rules.md` | Pattern rules (PERMANENT/EPHEMERAL/BRIDGING) |
| `memory/sessions/` | Compressed session archives |
| `context_engine/metrics/` | Compression metrics |

---

## 📋 Compression Rules (Pattern Catalog)

### PERMANENT Patterns

```
DECISION patterns:
  - "decided to", "chose", "going with", "best option"
  - "I think we should", "let's go with"

PREFERENCE patterns:
  - "I prefer", "I don't like", "always do X when"
  - "remember that I", "my style is"

INSIGHT patterns:
  - "the key insight is", "what I realized", "pattern I see"
  - "lesson learned", "mistake I made"

CONSTRAINT patterns:
  - "I can't", "limitation is", "the problem with"
  - "constraint:", "requirement:"

PROJECT patterns:
  - "status of X", "update on", "progress on"
  - "milestone:", "deliverable:"
```

### EPHEMERAL Patterns

```
CASUAL patterns:
  - "ok", "thanks", "sure", "yeah", "yep", "nope"
  - "got it", "understood", "makes sense"
  - "lol", "haha", "interesting"

CONFIRMATION patterns:
  - "yes that's right", "exactly", "perfect"
  - "no that's wrong" (if followed by correction)

REACTION patterns:
  - "nice", "cool", "good", "great"
  - "I see", "oh", "hmm"

PLATFORM patterns:
  - [message contains only emoji]
  - [message contains only image/link]
  - [message is a reaction-only]
```

---

**Version:** 1.0
**Last Updated:** 2026-04-20
**Owner:** Luna (Context Layer)
**Status:** ACTIVE — compression running, metrics collecting
