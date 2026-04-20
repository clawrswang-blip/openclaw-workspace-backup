# KG Fact Catcher
> Inline capture protocol — runs during every conversation to populate KG in real-time.

---

## 🎯 Purpose

KG is empty because there's no mechanism to populate it during conversation.
KG Fact Catcher solves this by detecting key information patterns as they appear
in conversation and triggering KG writes automatically.

**Principle:** Don't wait for session end. Capture facts when they're fresh.

---

## 🔍 Fact Pattern Detection

### Type 1: DECISION Facts 🔴 (High Priority)

**Trigger:** User expresses a choice or conclusion.

```
Keywords:
  - "decided to", "chose", "going with", "let's go with"
  - "I think we should", "best option is", "I'll go with X"
  - "the answer is", "conclusion:", "so we"

Capture:
  - What was decided?
  - What was the alternative? (if mentioned)
  - What was the rationale? (if mentioned)
  - When was it decided? (today's date)
  - Related to which project?

KG Write:
  subject: Rishon
  predicate: decided
  object: "<decision>"

  [Optional facts:]
  subject: Rishon
  predicate: rejected
  object: "<alternative>"
```

### Type 2: PREFERENCE Facts 🟠 (High Priority)

**Trigger:** User expresses a personal preference or working style.

```
Keywords:
  - "I prefer", "I don't like", "I always do X when"
  - "my style is", "I tend to", "I hate"
  - "remember that I", "important to me"
  - "it works better if", "I've found that"

Capture:
  - What is the preference?
  - Is it a pattern or one-time?
  - Related to what domain? (communication / work / tools)

KG Write:
  subject: Rishon
  predicate: prefers
  object: "<preference>"
  confidence: high  # if direct statement
  confidence: medium  # if inferred from behavior
```

### Type 3: CONSTRAINT Facts 🟠 (High Priority)

**Trigger:** User mentions a limitation, blocker, or requirement.

```
Keywords:
  - "I can't", "the problem is", "limitation is"
  - "constraint:", "requirement:", "need to", "have to"
  - "blocked by", "stuck on", "the issue is"

Capture:
  - What is the constraint?
  - Is it temporary or permanent?
  - Is it within Rishon's control?

KG Write:
  subject: Rishon
  predicate: constrained_by
  object: "<constraint>"

  OR project-level:
  subject: <project>
  predicate: blocked_by
  object: "<constraint>"
```

### Type 4: PROJECT/MILESTONE Facts 🟢 (Medium Priority)

**Trigger:** User mentions progress, achievements, or changes to projects.

```
Keywords:
  - "status of X", "update on", "progress on"
  - "milestone:", "achieved", "completed", "finished"
  - "launched", "released", "deployed"
  - "X is done", "just finished"

Capture:
  - What project?
  - What milestone?
  - Date achieved (today or specified)

KG Write:
  subject: <project>
  predicate: achieved
  object: "<milestone>"
  valid_from: <date>

  OR update:
  subject: <project>
  predicate: status
  object: "<current status>"
```

### Type 5: INSIGHT/LEARNING Facts 🟢 (Medium Priority)

**Trigger:** User shares a realization, lesson, or new understanding.

```
Keywords:
  - "I realized", "the key insight is", "what I learned"
  - "pattern I see", "it turns out", "lesson learned"
  - "mistake I made", "found out that"

Capture:
  - What was the insight?
  - What domain is it about?
  - Is it actionable?

KG Write:
  subject: Rishon
  predicate: learned
  object: "<insight>"
  valid_from: <today>
```

### Type 6: ENTITY Introduction Facts 🔵 (Low Priority)

**Trigger:** New person, company, tool, or concept mentioned for first time.

```
Keywords:
  - "there's X", "I met X", "X is a company"
  - "new tool called X", "discovered X", "using X now"

Capture:
  - Entity name
  - Entity type (person / company / tool / concept)
  - Relationship to existing entities

KG Write:
  subject: <entity>
  predicate: type
  object: <entity_type>

  subject: <entity>
  predicate: related_to
  object: <related_entity or project>
```

---

## ⚡ Inline Capture Flow

```
Every user message:
       │
       ▼
┌──────────────────────┐
│ Pattern Scanner       │
│                       │
│ Scan for DECISION     │──YES──→ Queue KG write: Rishon → decided → X
│ Scan for PREFERENCE   │──YES──→ Queue KG write: Rishon → prefers → X
│ Scan for CONSTRAINT   │──YES──→ Queue KG write: Rishon → constrained_by → X
│ Scan for MILESTONE   │──YES──→ Queue KG write: Project → achieved → X
│ Scan for INSIGHT     │──YES──→ Queue KG write: Rishon → learned → X
│ Scan for NEW ENTITY   │──YES──→ Queue KG write: Entity → type → X
└──────────────────────┘
       │
       NO NEW FACTS?
       │
       ▼
   Continue normally
```

**KG writes are queued — executed in batch at:**
1. End of significant topic shift
2. End of session
3. When queue reaches 5 items

---

## 📋 Capture Template

When a fact is detected, capture this structured info:

```
FACT DETECTED: [Type]
  Subject: <who or what>
  Predicate: <relationship type>
  Object: <what>
  Context: <surrounding conversation for nuance>
  Confidence: high / medium / low
  Source: this conversation
  Date: <today>
  Related entities: <any other entities mentioned>
```

**Confidence Calibration:**
- **High:** User directly stated it
  - "I decided to focus on X" → high
  - "My preference is Y" → high

- **Medium:** Inferred from behavior or context
  - "User keeps mentioning X" → medium
  - "User seems to struggle with Y" → medium

- **Low:** Speculative, needs verification
  - "Maybe user prefers X but not confirmed" → low (don't write to KG, just note in daily log)

---

## 🚫 What NOT to Capture

```
DO NOT write to KG:
- Casual comments ("weather is nice")
- One-off emotional reactions
- Questions without answers
- Hypothetical statements ("if I were to do X...")
- Information about third parties without Rishon's interpretation
- Anything explicitly marked as "not important" or "forget this"
```

---

## 🔄 Post-Session Write-Back

**At session end, execute all queued KG writes:**

```
For each queued fact:
  1. Validate: still accurate? context still valid?
  2. Check for conflicts with existing KG facts
  3. If conflict: mark old fact as superseded, write new
  4. Execute: mempalace_kg_add for new facts
  5. Log: write to memory/YYYY-MM-DD.md what was captured
```

**Session Summary Write:**
```
memory/YYYY-MM-DD.md:
  ## Session Summary — <time>
  - Task: <what we worked on>
  - Decisions made: [list]
  - Facts captured to KG: [list]
  - Next steps: [list]
```

---

## 🎓 Self-Training the Catcher

**Improve detection accuracy over time:**

```
Weekly review (via heartbeat):
1. Read last 7 days of memory/YYYY-MM-DD.md
2. Identify facts that WERE captured vs. should have been captured
3. If missed facts pattern detected → update pattern keywords in this file
4. If false positive pattern detected → add negative keywords
5. Update this file with refined patterns
6. Log: "KG Catcher updated — added [X] patterns, removed [Y] patterns"
```

**Pattern Evolution Log** → `context_engine/kgcatcher_pattern_log.md`

---

## 🧪 Testing the Catcher

```
After any significant conversation, verify:

□ How many facts were captured from this session?
□ How many were actual KG writes vs. just noted?
□ Were any important facts missed? (missed context rate)
□ Were there any false positives? (captured things that weren't really facts)
□ Did KG confidence calibration match reality?
□ Were new entities properly registered?
```

---

## 🔗 Integration Points

| Point | Action |
|-------|--------|
| **Session Boot** | Clear previous queue, load SessionBootTemplate |
| **During Conversation** | Fact Catcher active, queue builds |
| **Topic Shift** | Flush queue if >3 items |
| **Session End** | Full queue flush + session summary |
| **Weekly Heartbeat** | Pattern review + KG stale check |

---

**Version:** 1.0
**Last Updated:** 2026-04-20
**Status:** ACTIVE — runs during every conversation
**Next Pattern Review:** 2026-04-27
