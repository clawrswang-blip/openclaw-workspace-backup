# Skill Context Bridge
> Skills are not silos. Every skill call is a context transaction.

---

## 🔗 Context Handoff Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    GLOBAL CONTEXT                       │
│  (Layer 2: Identity + Layer 3: Project)                │
└───────────────────────┬─────────────────────────────────┘
                        │
                        │ SESSION CONTEXT SNAPSHOT
                        │ (what skill needs to know)
                        ▼
┌─────────────────────────────────────────────────────────┐
│                    SKILL EXECUTION                      │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │ SKILL.md                                         │   │
│  │ ## Context Contract                              │   │
│  │ - My load trigger: [X]                          │   │
│  │ - I need from global: [list]                    │   │
│  │ - I won't touch: [boundary]                      │   │
│  │ - I produce: [schema]                            │   │
│  │ - After me: [where output goes]                 │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
│  Skill-local context (isolated)                         │
└───────────────────────┬─────────────────────────────────┘
                        │
                        │ SKILL OUTPUT REINTEGRATION
                        │ (executive summary + learnings)
                        ▼
┌─────────────────────────────────────────────────────────┐
│                 GLOBAL CONTEXT UPDATED                   │
│                                                         │
│  - Execution summary added to volatile                  │
│  - Key learnings → Layer 3 (persistent)                │
│  - Resources released                                   │
└─────────────────────────────────────────────────────────┘
```

---

## 📋 Context Contract Template

Every SKILL.md must include this block:

```markdown
## Context Contract

### Load Trigger
When does this skill activate?
- Explicit: [user says "X"]
- Implicit: [pattern detected: Y]

### Required Context
What the skill MUST receive from global context before starting:
- [ ] Current task goal
- [ ] Any constraints or preferences
- [ ] Relevant project background (if applicable)

### Provided Context
What the skill guarantees to the global context:
- Execution summary (one paragraph)
- Key findings (bullet list)
- Next steps or recommendations
- Output schema: [what format the output is in]

### Boundary
What this skill will NOT do:
- [ ] Will not modify global context
- [ ] Will not access other skills' outputs
- [ ] Will not retain context after completion

### Post-Execution
After skill completes:
1. Write execution summary → Layer 1 (volatile)
2. Write key learnings → Layer 3 (persistent, if significant)
3. Release all skill-local context
4. Unload SKILL.md from memory
```

---

## 🔄 Handoff Protocol

### BEFORE Skill Call

```
1. CREATE SESSION CONTEXT SNAPSHOT
   {
     "task_goal": "...",
     "constraints": [...],
     "relevant_background": [...],
     "skill_specific_context": {...}
   }

2. LOAD SKILL.md
   - Read context contract
   - Validate required context is available
   - If missing required context → ask before proceeding

3. INJECT BOUNDARY REMINDER
   "You are now running [SKILL_NAME].
    You have access to: [context snapshot].
    You will NOT: [boundary list].
    Output format required: [schema]"
```

### DURING Skill Execution

```
Context usage rules:
- Only access context in snapshot
- Do not read other SKILL.md files
- Do not access MemPalace directly (use global context)
- If you need additional context → ask, don't assume

Error handling:
- If context insufficient → pause + ask
- If boundary violation attempted → refuse + explain
- If skill fails → log failure + partial output to volatile
```

### AFTER Skill Completion

```
REINTEGRATION STEP 1: Execution Summary
   Write to Layer 1 (volatile):
   ```
   [SKILL_NAME] completed:
   - Output: [summary]
   - Quality: [self-assessment: complete/partial/failed]
   - Next: [what should happen next]
   ```

REINTEGRATION STEP 2: Persistent Learnings
   If skill discovered something worth remembering:
   - New fact → KG via proper protocol
   - New insight → MemPalace Drawer
   - New preference → USER.md update (if changed)

REINTEGRATION STEP 3: Context Cleanup
   - Discard skill-local context
   - Unload SKILL.md from working memory
   - Mark skill execution complete
```

---

## 🔍 Skill Isolation Enforcement

### Context Leak Detection

```
Metric: skill_context_leak_rate
Definition: Sessions where skill context contaminated global context

Detection:
- After skill execution, scan session for unexpected context
- Look for: skill-specific terms appearing in non-skill messages
- Look for: skill output bleeding into other skills

If leak detected:
1. Flag the skill (which part leaked?)
2. Update skill boundary in SKILL.md
3. Log to context_engine/skill_audit.md
4. If recurring → escalate to P2 review
```

### Skill-vs-Skill Interference Prevention

```
Rule: Two skills cannot run simultaneously
Rule: Skill B cannot read Skill A's outputs
Rule: Global context between skills = Layer 1 volatile only

If two skills need to share context:
- Go through Layer 3 (persistent) — explicit write/read
- Or go through user (explicit handoff)
```

---

## 📊 Skill Context Metrics

| Metric | Definition | Target |
|--------|-----------|--------|
| `skill_load_frequency` | Sessions using skill / total sessions | > 0.05 (else deprecate) |
| `skill_success_rate` | Completed / total calls | > 0.85 |
| `skill_context_leak_rate` | Sessions with leak / sessions using skill | < 0.05 |
| `skill_output_useful_rate` | Outputs used downstream / total outputs | > 0.65 |
| `skill_boundary_violation` | Attempted violations / total calls | 0 |
| `context_insufficient_rate` | Calls where required context was missing | < 0.10 |

---

## 🔧 Skill Quality Checklist

Before a skill is considered "production ready":

```
□ Context Contract declared in SKILL.md
□ Load trigger is specific and testable
□ Required context is documented
□ Boundary is clear and enforceable
□ Output schema is explicit
□ Post-execution cleanup is defined
□ No hardcoded context references (no "I know Rishon prefers...")
□ All context comes through snapshot injection
□ Metrics tracking is implemented
□ Skill has been tested with insufficient context (graceful failure)
```

---

## 🚀 Skill Lifecycle

```
SKILL STATES:
  PROPOSED → DRAFT → TESTING → PRODUCTION → DEPRECATED

PROPOSED:
  - Identified as needed (skill gap)
  - Context contract drafted
  - Owner assigned

DRAFT:
  - SKILL.md written
  - Context contract complete
  - Initial testing done

TESTING:
  - Running in parallel with existing solution
  - Metrics tracked: success_rate, context_leak, output_useful
  - Threshold for promotion: success_rate > 0.85, leak < 0.05

PRODUCTION:
  - Full deployment
  - Ongoing metrics monitoring
  - Quarterly review

DEPRECATED:
  - frequency < 0.05 for 60+ days
  - OR success_rate < 0.50
  - OR replaced by better skill
  - Archive SKILL.md, log deprecation reason
```

---

## 📁 Skill Registry

| Skill | Status | Last Used | Context Contract | Notes |
|-------|--------|-----------|-----------------|-------|
| khazix-writer | PRODUCTION | 2026-04-19 | ✅ Complete | Chinese content generation |
| seo | PRODUCTION | 2026-04-18 | ✅ Complete | SEO audit + content |
| deep-research-pro | PRODUCTION | 2026-04-17 | ✅ Complete | Research synthesis |
| data-analysis | PRODUCTION | 2026-04-15 | ✅ Complete | Data processing |
| market-research | PRODUCTION | 2026-04-12 | ✅ Complete | Market intelligence |
| coding-agent | TESTING | 2026-04-19 | ⚠️ Draft | Code generation |
| humanizer | PROPOSED | — | ❌ Missing | — |

---

## 🔄 Skill Context Self-Optimization

```
Weekly Skill Audit:
1. Check skill_load_frequency — flag < 0.05 for review
2. Check skill_context_leak_rate — flag any > 0.05
3. Check skill_output_useful_rate — flag < 0.65
4. Review any boundary violations
5. Update skill registry
6. Propose deprecations if needed
7. Identify new skill needs from usage patterns
```

---

**Version:** 1.0
**Last Updated:** 2026-04-20
**Owner:** Luna (Skill Architect)
**Status:** ACTIVE — context contracts required for all new skills
