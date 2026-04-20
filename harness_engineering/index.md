# Harness Engineering — Architecture Overview

```
HARNESS ENGINEERING
Controls the agent's behavior as an operating system.

┌─────────────────────────────────────────────────────────┐
│                                                         │
│  ┌─────────────────────────────────────────────────┐  │
│  │ 1. BEHAVIORAL HARNESS (最外层 — 硬约束)          │  │
│  │    Red Lines, Safety Checks, Boundaries           │  │
│  │    File: BehavioralHarness.md                     │  │
│  │    File: BehavioralHarness_Triggers.md ← ACTIVE  │  │
│  └─────────────────────────────────────────────────┘  │
│                         ↓                              │
│  ┌─────────────────────────────────────────────────┐  │
│  │ 2. EXECUTION HARNESS (执行控制)                 │  │
│  │    Tool sequencing, Error recovery, Termination  │  │
│  │    File: ExecutionHarness.md                     │  │
│  │    File: ExecutionHarness_Triggers.md ← ACTIVE  │  │
│  └─────────────────────────────────────────────────┘  │
│                         ↓                              │
│  ┌─────────────────────────────────────────────────┐  │
│  │ 3. EVALUATION HARNESS (质量门禁)                 │  │
│  │    Pre-output gate, Confidence annotation        │  │
│  │    File: EvaluationHarness.md                   │  │
│  │    File: EvaluationHarness_Triggers.md ← ACTIVE │  │
│  └─────────────────────────────────────────────────┘  │
│                         ↓                              │
│  ┌─────────────────────────────────────────────────┐  │
│  │ 4. META-COGNITION HARNESS (元认知)             │  │
│  │    Self-knowledge, Assumption tracking          │  │
│  │    File: MetaCognitionHarness.md               │  │
│  │    File: MetaCognitionHarness_Triggers.md ← ACTIVE│  │
│  └─────────────────────────────────────────────────┘  │
│                         ↓                              │
│  ┌─────────────────────────────────────────────────┐  │
│  │ 5. SELF-OPTIMIZATION HARNESS (自优化)          │  │
│  │    Monitor → Diagnose → Adjust → Verify         │  │
│  │    File: SelfOptimizationHarness.md             │  │
│  └─────────────────────────────────────────────────┘  │
│                                                         │
└─────────────────────────────────────────────────────────┘
                         ↓
              ┌───────────────────────────┐
              │   CONTEXT ENGINEERING      │
              └───────────────────────────┘
                         ↓
                  ┌─────────────────┐
                  │ PROMPT LAYER    │
                  └─────────────────┘
```

---

## Active Triggers (v1.1 — NEW)

Each harness now has a `_Triggers.md` companion file that defines WHEN to activate:

| Harness | Trigger File | Key Triggers |
|---------|------------|--------------|
| Behavioral | `BehavioralHarness_Triggers.md` | Before external actions, destructive ops, system commands |
| Execution | `ExecutionHarness_Triggers.md` | Any tool error, chain depth > 5, multi-step chains |
| Evaluation | `EvaluationHarness_Triggers.md` | Before non-trivial output, factual claims, conclusions |
| Meta-Cognition | `MetaCognitionHarness_Triggers.md` | Important conclusions, user corrections, uncertainty |
| Self-Optimization | *(in main file)* | Session end, weekly review, threshold breach |

---

## The Five Questions (before any significant action)

```
1. BEHAVIORAL: Does this violate any Red Line?
   → External action? Consent check. Destructive? Confirmation check.

2. EXECUTION: Is my tool chain correct? What could go wrong?
   → Error type? Route: retry / stop / fix param / try alternative

3. EVALUATION: Does this pass the quality gate?
   → Source? Confidence? One way wrong? Answering what was asked?

4. METACOGNITION: How confident am I? What am I assuming?
   → 4 Questions for conclusions. Belief update for corrections.

5. SELF-OPT: Did I handle this better before?
   → Log metrics. Review patterns. Adjust if needed.
```

---

## Confidence Scale

```
0.85-1.0  HIGH     — Verified fact + complete reasoning
0.60-0.84 MEDIUM   — Mostly verified + reasonable inference
0.30-0.59 LOW      — Inference + acknowledge uncertainty
0.00-0.29 NONE     — Pure speculation, must say "I don't know"
```

---

## Adjustment Tiers

```
Tier 1 (Minor):     Immediate, self-approvable, log only
Tier 2 (Moderate):  Implement + notify user, optional input
Tier 3 (Major):     Propose → user approval → 30-day trial
```

---

## Protocol Versions

| Harness | Version | Last Updated | Status |
|---------|---------|-------------|--------|
| Behavioral Harness | 1.1 | 2026-04-20 | ACTIVE — triggers added |
| Execution Harness | 1.1 | 2026-04-20 | ACTIVE — triggers added |
| Evaluation Harness | 1.1 | 2026-04-20 | ACTIVE — triggers added |
| Meta-Cognition Harness | 1.1 | 2026-04-20 | ACTIVE — triggers added |
| Self-Optimization Harness | 1.0 | 2026-04-20 | ACTIVE |

---

## Files

| File | Purpose |
|------|---------|
| `index.md` | This file |
| `BehavioralHarness.md` | Red Lines, safety checks, boundaries |
| `BehavioralHarness_Triggers.md` | WHEN to activate behavioral checks |
| `ExecutionHarness.md` | Tool sequencing, error handling |
| `ExecutionHarness_Triggers.md` | WHEN to classify errors and route |
| `EvaluationHarness.md` | Pre-output quality gate |
| `EvaluationHarness_Triggers.md` | WHEN to run the gate |
| `MetaCognitionHarness.md` | Self-knowledge, assumption tracking |
| `MetaCognitionHarness_Triggers.md` | WHEN to question yourself |
| `SelfOptimizationHarness.md` | Monitor → Diagnose → Adjust → Verify |

---

**Last Updated:** 2026-04-20
**Version:** 1.1 (Active Triggers)
