# Dynamic Optimizer
> The system that optimizes itself. Nothing is static.

---

## 🎯 Core Principle

Every protocol, metric, and threshold is a hypothesis — not a truth.
Everything is continuously tested. Everything can be improved.

```
OBSERVE → DIAGNOSE → ADJUST → VERIFY → REPEAT
    ↑                                    │
    └──────── feedback loop ─────────────┘
```

---

## 📊 Metrics Dashboard

### Context Layer Health Metrics

| Metric | Definition | Ideal Range | Alert Threshold |
|--------|-----------|-------------|-----------------|
| `context_volatility_rate` | Volatile facts discarded vs. total created | < 60% discard | > 80% discard |
| `identity_drift_score` | Discrepancy between IDENTITY.md and observed behavior | < 0.1 | > 0.3 |
| `layer3_recall_precision` | Layer 3 sources recalled that were actually useful | > 0.75 | < 0.50 |
| `layer3_recall_recall` | Useful Layer 3 sources that were actually recalled | > 0.70 | < 0.45 |
| `conflict_rate` | Sessions with context conflicts / total sessions | < 0.10 | > 0.25 |
| `context_satisfaction` | Post-task rating: "context felt complete" (1-5) | > 4.0 | < 3.0 |
| `redundant_injection_rate` | Injected context that was never referenced / total injected | < 0.40 | > 0.60 |
| `missed_context_rate` | Useful context that existed but wasn't recalled / total useful | < 0.20 | > 0.35 |

### Memory System Metrics

| Metric | Definition | Ideal Range | Alert Threshold |
|--------|-----------|-------------|-----------------|
| `kg_fact_count` | Total active KG facts | growing | sudden drop |
| `kg_stale_rate` | Facts past valid_until not invalidated | < 0.05 | > 0.15 |
| `kg_orphaned_count` | KG facts with no links to other facts | < 0.10 | > 0.25 |
| `drawer_orphaned_rate` | Drawers with no incoming links | < 0.10 | > 0.20 |
| `memory_write_consistency` | Writes following protocol / total writes | > 0.90 | < 0.75 |
| `conflict_detection_rate` | Pre-write conflicts caught / total conflicts | > 0.85 | < 0.70 |
| `recall_miss_rate` | Failed recalls / total recall attempts | < 0.20 | > 0.40 |

### Skill Layer Metrics

| Metric | Definition | Ideal Range | Alert Threshold |
|--------|-----------|-------------|-----------------|
| `skill_usefulness_rate` | Skill outputs used downstream / total outputs | > 0.65 | < 0.40 |
| `skill_context_leak_rate` | Sessions where skill context polluted global | < 0.05 | > 0.15 |
| `skill_load_frequency` | Sessions using skill X / total sessions | > 0.20 | < 0.05 (→deprecate) |

### External Layer Metrics

| Metric | Definition | Ideal Range | Alert Threshold |
|--------|-----------|-------------|-----------------|
| `external_data_value_rate` | External fetches that changed output / total fetches | > 0.35 | < 0.20 |
| `fetch_cost_per_useful` | Token cost / useful external result | minimize | spike = optimize |

---

## 🔍 Diagnostic Engine

### Automated Diagnosis Triggers

**Every Heartbeat (8-12h):**
- Check all metrics against alert thresholds
- If any threshold breached → log diagnosis

**Every Session End:**
- Calculate session-level metrics
- Log to `memory/YYYY-MM-DD.md`
- Update running averages

**Every Week (cron, Sunday 21:00 PDT):**
- Full metric deep-dive
- Generate diagnosis report
- Propose adjustments (if needed)

---

## 🛠️ Adjustment Protocols

### Adjustment Type Matrix

| Root Cause | Adjustment Type | Protocol |
|-----------|---------------|---------|
| Recall algorithm wrong | Algorithm update | Update `SessionBoot.py` |
| Taxonomy wrong | Taxonomy update | Update `Taxonomy.md` |
| Memory protocol wrong | Protocol update | Update `MemoryProtocol.md` |
| Threshold too strict/loose | Threshold recalibration | Update this file |
| Metric definition wrong | Metric redefinition | Update this file |
| External data source bad | Source blacklist | Update `context_engine/ExternalSources.md` |

### Adjustment Severity Levels

**Level 1 (Minor, immediate):**
- Threshold recalibration
- Metric formula fine-tuning
- No protocol structure change
- Example: "context_satisfaction threshold 4.0 → 3.8 based on 30-day data"

**Level 2 (Moderate, 7-day trial):**
- Algorithm changes
- Protocol rule changes
- Runs parallel with old version for 7 days
- If new version performs better → full switch
- If worse → revert + diagnose

**Level 3 (Major, 30-day trial):**
- Taxonomy restructuring
- New memory system integration
- Changes to Layer 2 (identity)
- Requires explicit user approval before trial
- 30-day trial with weekly check-ins

---

## 📋 Optimization Execution Log

### Log Format

```
## [YYYY-MM-DD] Optimization Entry

### Metrics Summary
| Metric | Value | Status |
|--------|-------|--------|
| context_satisfaction | 3.8 | ⚠️ below threshold |
| conflict_rate | 0.12 | ⚠️ above threshold |

### Diagnosis
Root cause: Layer 3 recall too conservative → high missed_context_rate
Evidence: 30% of "useful context" was scored < 0.5 and excluded

### Adjustment Proposed
Level: 2
Change: Raise injection threshold from 0.5 to 0.6
Trial: 7 days parallel

### Verification Plan
- Track context_satisfaction daily
- Track missed_context_rate daily
- If both improve → full adoption
- If either degrades → revert

### Status: [PROPOSED / APPROVED / RUNNING / COMPLETED / REVERTED]
```

### Where to Log

- Active optimization entries → `memory/optimization/YYYY-MM-DD.md`
- Summarized to → `MEMORY.md` (optimization_summary section)
- Metrics raw data → `context_engine/metrics_history.jsonl`

---

## 🔄 Self-Referential Optimization

**The Optimizer Itself Can Be Optimized.**

```
If optimization process is inefficient (cost > value):
  → Diagnose: wrong triggers? too many false positives?
  → Adjust: raise alert thresholds, reduce check frequency
  → Verify: cost-per-optimization improved?
```

**Optimization of optimization = meta-optimization.**

This creates a recursive self-improvement loop:
```
Level 0: Task execution
Level 1: Task optimization (am I doing tasks well?)
Level 2: Context optimization (is context management good?)
Level 3: Optimizer optimization (is my optimization working?)
```

---

## 🚦 Threshold Calibration Guide

### How to Calibrate

**context_satisfaction:**
```
1. Collect 30 sessions of ratings (1-5)
2. Calculate mean + std dev
3. Threshold = mean - 1 std dev
4. Review quarterly
```

**conflict_rate:**
```
1. Target: low conflict rate + quick resolution
2. If conflicts are being resolved same-session → acceptable
3. If conflicts persist across sessions → threshold too high
```

**missed_context_rate:**
```
1. Track "would have been useful" via post-task review
2. If rate > threshold → expand recall search
3. If rate << threshold → tighten threshold (reduce noise)
```

---

## 🧪 Experimental Features Registry

New optimization strategies are tested before full adoption:

```
context_engine/experiments/
├── experiment_log.md
└── active/
    ├── [experiment_name]/
    │   ├── hypothesis.md
    │   ├── parameters.json
    │   ├── trial_start.md
    │   └── trial_results.md
```

**Experiment Lifecycle:**
1. Hypothesis: "If we change X, metric Y will improve"
2. Trial: Run for 14-30 days
3. Analysis: Did metric improve? Side effects?
4. Decision: Adopt / Reject / Modify
5. Log: Always log result (even negative = learning)

---

## 📊 Current System Status

*Auto-updated by heartbeat. Last updated: 2026-04-20*

| Metric | Current | Threshold | Status |
|--------|---------|-----------|--------|
| context_satisfaction | — | 3.0 | 📊 collecting baseline |
| conflict_rate | — | 0.25 | 📊 collecting baseline |
| missed_context_rate | — | 0.35 | 📊 collecting baseline |
| kg_stale_rate | — | 0.15 | 📊 collecting baseline |
| layer3_recall_precision | — | 0.50 | 📊 collecting baseline |

**Note:** Baseline collection in progress (first 7 days). Thresholds are starting estimates.

---

**Version:** 1.0
**Last Updated:** 2026-04-20
**Owner:** Luna (Self-Optimizing System)
**Status:** ACTIVE — monitoring + dynamic adjustment enabled
**Next Review:** 2026-04-27 (first weekly audit)
