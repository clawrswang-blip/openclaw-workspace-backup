# Self-Optimization Harness
> Monitor → Diagnose → Adjust → Verify. Always improving.

---

## 🎯 Purpose

Not just "do tasks" but "improve at doing tasks."
Track performance, detect patterns, trigger adjustments,
and verify they worked.

---

## 🔄 The Optimization Loop

```
        ┌─────────────────────────────┐
        │         MONITOR              │
        │  Collect metrics continuously │
        └──────────────┬──────────────┘
                       ↓
        ┌─────────────────────────────┐
        │         DIAGNOSE             │
        │  Detect patterns and issues  │
        └──────────────┬──────────────┘
                       ↓
        ┌─────────────────────────────┐
        │         ADJUST               │
        │  Minor / Moderate / Major   │
        └──────────────┬──────────────┘
                       ↓
        ┌─────────────────────────────┐
        │         VERIFY              │
        │  Did the adjustment work?   │
        └──────────────┬──────────────┘
                       ↓
               ← back to MONITOR
```

---

## 📊 Metrics Collection

### Harness-Level Metrics

```
BEHAVIORAL HARNESS:
- red_line_violation_count: [target: 0]
- boundary_breach_count: [target: <3/session]
- safety_check_triggered: [target: >0 when needed]

EXECUTION HARNESS:
- tool_success_rate: [target: >0.90]
- retry_rate: [target: <0.10]
- chain_completion_rate: [target: >0.80]
- premature_termination_rate: [target: <0.05]

EVALUATION HARNESS:
- gate_pass_rate: [target: >0.90]
- gate_fix_rate: [target: >0.80]
- correction_rate: [target: <0.10]
- hallucination_claims: [target: <0.02]

METACOGNITION HARNESS:
- assumption_declared_rate: [target: >0.70]
- belief_update_transparency: [target: 1.00]
- adversarial_exercise_rate: [target: >0.50]
```

### Context Layer Metrics (from Context Engineering)

```
- context_satisfaction: [target: >3.0]
- conflict_rate: [target: <0.25]
- missed_context_rate: [target: <0.35]
- kg_stale_rate: [target: <0.15]
- kg_growth_rate: [target: >5 entities/week]
- recall_precision: [target: >0.75]
```

### Integration Metrics

```
- session_outcome_quality: [subjective 1-5 from user or self-assessment]
- user_correction_rate: [user corrections / total outputs]
- task_completion_rate: [tasks completed / tasks started]
- goal_alignment: [outputs matching user intent / total]
```

---

## 🔍 Diagnostic Patterns

### Pattern 1: Degraded Performance

```
TRIGGER: Any metric below threshold for 3+ consecutive days

DIAGNOSIS STEPS:
1. Which specific metric degraded?
2. When did it start degrading?
3. What changed around that time?
   - New tools added?
   - Context changes?
   - User behavior changes?
4. Is this a one-off or systematic?

OUTPUT:
┌─────────────────────────────────────────┐
│ DIAGNOSIS REPORT                           │
│ Metric: [name]                             │
│ Current: [value] / Target: [threshold]     │
│ Duration: [N days]                         │
│ Probable cause: [hypothesis]              │
│ Recommended fix: [action]                  │
└─────────────────────────────────────────┘
```

### Pattern 2: Error Clustering

```
TRIGGER: Same error type occurs 3x in 1 hour

DIAGNOSIS STEPS:
1. Classify the error type
2. Is it tool-specific?
3. Is it context-specific?
4. Is it user-specific?
5. Is it time-specific (late night, etc.)?

OUTPUT:
┌─────────────────────────────────────────┐
│ ERROR CLUSTER REPORT                       │
│ Error type: [classification]              │
│ Frequency: [N] times in [time window]     │
│ Pattern: [what's common]                  │
│ Fix: [recommended action]                 │
└─────────────────────────────────────────┘
```

### Pattern 3: User Correction Spike

```
TRIGGER: correction_rate increases by >30% week-over-week

DIAGNOSIS STEPS:
1. What type of corrections? (factual / tone / depth / format)
2. Is it concentrated in specific task types?
3. Is it concentrated in specific harness areas?
4. What's the trend over 4 weeks?

OUTPUT:
┌─────────────────────────────────────────┐
│ CORRECTION ANALYSIS                        │
│ Correction type breakdown: [...]           │
│ Affected task types: [...]               │
│ Likely root cause: [hypothesis]         │
│ Adjustment: [recommended]                │
└─────────────────────────────────────────┘
```

---

## ⚙️ Adjustment Tiers

### Tier 1: Minor (Self-Approvable)

```
WHAT: Threshold fine-tuning, wording changes, protocol tweaks
TIME: Immediate
NOTIFICATION: Log to optimization file only
REVERT: If metrics don't improve in 7 days

EXAMPLES:
- Increase gate_pass_rate threshold from 0.90 to 0.92
- Change "I believe" to "I think" in LOW confidence outputs
- Adjust retry backoff from 2s/4s/8s to 1s/2s/4s
```

### Tier 2: Moderate (User Notification)

```
WHAT: Strategy changes, new protocols, tool behavior changes
TIME: Implement + notify user
USER INPUT: Optional (unless major change)
REVERT: If user objects

EXAMPLES:
- Add new tool to selection matrix
- Change EvaluationHarness checklist criteria
- Add new error classification type
- Modify Meta-Cognition self-check questions
```

### Tier 3: Major (User Approval Required)

```
WHAT: Structural changes, new harnesses, fundamental protocol changes
TIME: Propose → wait for approval → implement
USER INPUT: Required
TRIAL PERIOD: 30 days with weekly check-ins

EXAMPLES:
- Add new harness layer
- Change BehavioralHarness Red Lines
- Restructure Context Layer taxonomy
- Change fundamental execution flow
```

---

## ✅ Verification Protocol

```
AFTER ADJUSTMENT:

STEP 1: MONITOR (7 days post-adjustment)
- Watch the affected metrics daily
- Watch for side effects in related metrics

STEP 2: EVALUATE
- Improved: metric back above threshold?
- Unchanged: adjustment didn't work
- Degraded: adjustment caused harm

STEP 3: DECIDE
┌─────────────────────────────────────────┐
│ IF improved:                              │
│   → Keep adjustment                       │
│   → Update thresholds if justified         │
│   → Document in optimization log           │
│                                           │
│ IF unchanged:                             │
│   → Revert to previous state              │
│   → Log as "attempted, did not work"     │
│   → Try alternative approach              │
│                                           │
│ IF degraded:                             │
│   → REVERT IMMEDIATELY                   │
│   → Log as "caused regression"            │
│   → Diagnose why it made things worse     │
└─────────────────────────────────────────┘
```

---

## 📋 Optimization Log

```
LOCATION: memory/optimization/YYYY-MM-DD.md

FORMAT:
## [Date] Optimization Entry

### Metric Snapshot
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| ...    | ...     | ...    | ...    |

### Issue Detected
[Description of problem]

### Diagnosis
[Root cause analysis]

### Adjustment
[What was changed, tier level]

### Verification (7-day post-adjustment)
[Results]

### Status: [SUCCESSFUL / REVERTED / ONGOING]
```

---

## 🎯 Priority Framework

```
WHEN MULTIPLE ISSUES COMPETE FOR ATTENTION:

Priority = Impact × Urgency × Confidence

┌─────────────────────────────────────────┐
│ IMPACT: How much does this affect?        │
│   High: Affects core task quality        │
│   Medium: Affects specific task types    │
│   Low: Minor annoyance                  │
├─────────────────────────────────────────┤
│ URGENCY: How time-sensitive?            │
│   High: Degrading fast, user impacted    │
│   Medium: Known issue, stable           │
│   Low: Nice to have                     │
├─────────────────────────────────────────┤
│ CONFIDENCE: How sure are we?            │
│   High: Clear cause-effect, easy fix     │
│   Medium: Good hypothesis, needs test  │
│   Low: Unclear, exploratory            │
└─────────────────────────────────────────┘

Priority Score = Impact × Urgency × Confidence
Focus on highest scores first.
```

---

## 🔗 Harness Integration

```
EACH SESSION:
┌─────────────────────────────────────────┐
│ POST-SESSION:                              │
│ 1. Log key metrics for this session      │
│ 2. Note any issues encountered            │
│ 3. Flag any adjustments to consider      │
└─────────────────────────────────────────┘

EACH HEARTBEAT:
┌─────────────────────────────────────────┐
│ HEALTH CHECK:                              │
│ 1. Review last session metrics           │
│ 2. Check for threshold breaches          │
│ 3. Flag any diagnostic patterns          │
│ 4. Decide: Tier 1 adjust or defer?      │
└─────────────────────────────────────────┘

EACH WEEK:
┌─────────────────────────────────────────┐
│ WEEKLY REVIEW:                            │
│ 1. Full metrics report                    │
│ 2. Diagnostic deep-dive (if issues)      │
│ 3. Tier 1 adjustments (if needed)       │
│ 4. Tier 2 proposals (if needed)          │
└─────────────────────────────────────────┘

EACH MONTH:
┌─────────────────────────────────────────┐
│ MONTHLY AUDIT:                            │
│ 1. Trend analysis                        │
│ 2. Major adjustments review              │
│ 3. User feedback integration             │
│ 4. Protocol version updates               │
└─────────────────────────────────────────┘
```

---

## 📊 Self-Optimization Metrics

| Metric | Definition | Target |
|--------|-----------|--------|
| `tier1_adjustment_success_rate` | Tier 1 adjustments that improved metrics / total | > 0.70 |
| `tier2_rollback_rate` | Tier 2 adjustments reverted / total | < 0.15 |
| `optimization_cycle_completion` | Issues that reached resolution / issues started | > 0.85 |
| `false_positive_diagnosis` | Diagnoses that were wrong / total | < 0.20 |
| `user_initiated_adjustment_rate` | Adjustments proposed by user / total | > 0.10 |

---

**Version:** 1.0
**Last Updated:** 2026-04-20
**Status:** ACTIVE
