# KG Fact Catcher — Pattern Evolution Log

## Pattern Refinement History

### 2026-04-20 — Initial Deployment
**Patterns defined:**
- DECISION: "decided to", "chose", "going with", "I think we should", "best option is"
- PREFERENCE: "I prefer", "I don't like", "my style is", "remember that I"
- CONSTRAINT: "I can't", "the problem is", "limitation is", "blocked by"
- MILESTONE: "status of", "update on", "milestone:", "achieved", "completed"
- INSIGHT: "I realized", "the key insight is", "lesson learned", "pattern I see"
- ENTITY: "there's X", "I met X", "new tool called X"

**Detection thresholds:**
- High confidence: direct statement
- Medium confidence: inferred from behavior
- Low confidence: speculative (log only, don't write to KG)

---

## Tuning Log

*No tuning entries yet — log patterns as they are discovered.*

### [DATE] — Pattern Update
**Change:** Added/Removed [keywords]
**Reason:** [why]
**Result:** [what improved or degraded]

---

## Missed Fact Log

*Record facts that should have been captured but weren't.*

| Date | Session | Missed Fact | Root Cause | Fixed? |
|------|---------|------------|------------|--------|
| | | | | |

---

## False Positive Log

*Record captures that were not actually meaningful facts.*

| Date | Session | False Positive | Root Cause | Fixed? |
|------|---------|---------------|------------|--------|
| | | | | |

---

## Detection Rate Metrics

| Week | Facts Detected | Facts Missed | False Positives | Precision | Recall |
|------|--------------|-------------|----------------|-----------|--------|
| 2026-04-20 | 33 KG writes | — | — | — | — |
| | | | | | |

## Session Log — 2026-04-20

| Time | Session | Facts Captured | Trigger | Notes |
|------|---------|--------------|---------|-------|
| 22:05 | Context Engineering deployment | 11 facts | Manual KG writes | SessionBootTemplate, KG_FactCatcher, session_boot fixes |
| 22:23 | Harness Engineering deployment | 11 facts | Manual KG writes | 5 harness components + scores |
| 22:50 | Three Engineering review | 7 facts | Manual KG writes | Overall scores + key insights |

**Total KG writes today: 29 facts across 3 sessions**

*Metrics start collecting after first week of deployment.*
