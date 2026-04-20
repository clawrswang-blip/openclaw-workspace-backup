# Execution Harness
> Tool execution control: sequencing, error recovery, iteration termination.

---

## 🎯 Purpose

Controls HOW tools are called — in what order, with what error handling,
when to retry, and when to stop.

---

## 📐 Execution Flow

```
┌─────────────────────────────────────────────────────────┐
│ PHASE 1: PRE-EXECUTION                                   │
│                                                          │
│ 1. VALIDATE goal: Is the objective clear?                │
│ 2. SELECT tool: Is this the right tool for the job?     │
│ 3. CHECK dependencies: Any tool that must run before?    │
│ 4. VERIFY permissions: Do I have access?                │
│ 5. ESTIMATE cost: Token/compute budget check            │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ PHASE 2: EXECUTION                                       │
│                                                          │
│ 1. CALL tool with parameters                             │
│ 2. MONITOR initial response                              │
│ 3. IF error → classify → route                          │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ PHASE 3: POST-EXECUTION                                 │
│                                                          │
│ 1. VERIFY output: Format/content/completeness           │
│ 2. IF invalid → retry or escalate                      │
│ 3. IF valid → proceed to next step or conclude         │
│ 4. LOG execution for optimization harness               │
└─────────────────────────────────────────────────────────┘
```

---

## 🔧 Tool Selection Protocol

### Tool Selection Matrix

```
TASK TYPE → APPROPRIATE TOOLS → USAGE RULES

┌─────────────────────────────────────────────────────────┐
│ INFORMATION RETRIEVAL                                       │
│ Tools: web_search, web_fetch, mempalace_search,         │
│        mempalace_kg_query, read, memory_search           │
│                                                          │
│ Rules:                                                    │
│ - web_search before web_fetch (check before deep dive)   │
│ - MemPalace before web (internal memory first)           │
│ - Limit web_fetch to top 3 results unless specified      │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ FILE OPERATIONS                                            │
│ Tools: read, write, edit, exec, trash                    │
│                                                          │
│ Rules:                                                    │
│ - read before write (always check existing content)       │
│ - write with backup (keep old version in memory/)        │
│ - exec: always explain what command will do              │
│ - trash > rm (recoverable over permanent)               │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ CODE GENERATION / EXECUTION                               │
│ Tools: write, exec, sessions_spawn                        │
│                                                          │
│ Rules:                                                    │
│ - Explain plan before writing code                        │
│ - Read existing code before modifying                     │
│ - Test in isolation before integration                    │
│ - Never run code that modifies system state without       │
│   explicit confirmation                                   │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ COMMUNICATION / MESSAGING                                  │
│ Tools: sessions_send, cron (for scheduling)            │
│                                                          │
│ Rules:                                                   │
│ - Draft before sending (user confirms)                   │
│ - Check recipient list twice                             │
│ - For groups: respect context boundaries                 │
│ - Never send half-baked replies                          │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ SUBAGENT / SPAWN MANAGEMENT                               │
│ Tools: sessions_spawn, subagents, sessions_yield         │
│                                                          │
│ Rules:                                                   │
│ - sessions_spawn: isolate heavy tasks                     │
│ - subagents: monitor and collect results                  │
│ - sessions_yield: after spawning, wait for results       │
│ - Always define success criteria before spawning          │
└─────────────────────────────────────────────────────────┘
```

---

## ⚠️ Error Classification & Routing

Every tool error falls into one of these categories:

```
ERROR CLASSIFICATION MATRIX:

┌────────────────┬───────────────┬────────────────────────┐
│ ERROR TYPE     │ DESCRIPTION   │ HANDLING              │
├────────────────┼───────────────┼────────────────────────┤
│ TRANSIENT     │ Network timeout│ Retry 1-2x with       │
│               │ / rate limit   │ exponential backoff    │
│               │               │ Break if 3 failures    │
├────────────────┼───────────────┼────────────────────────┤
│ PERMISSION    │ Access denied  │ Stop. Log. Notify     │
│               │ / auth failed  │ user explicitly.      │
│               │               │ Do not retry silently  │
├────────────────┼───────────────┼────────────────────────┤
│ PARAM         │ Wrong args     │ Fix params. Retry 1x  │
│               │ / bad input   │ If fails again → stop │
├────────────────┼───────────────┼────────────────────────┤
│ LOGIC         │ Tool returned  │ STOP chain. Analyze.  │
│               │ unexpected     │ May need different    │
│               │ result type    │ tool entirely        │
├────────────────┼───────────────┼────────────────────────┤
│ NOT_FOUND     │ Resource missing│ Check path. Try      │
│               │ / 404         │ alternative. Stop     │
│               │               │ if essential          │
├────────────────┼───────────────┼────────────────────────┤
│ UNKNOWN       │ Unclassified  │ Stop. Log. Ask user  │
│               │ error         │ for clarification     │
└────────────────┴───────────────┴────────────────────────┘
```

### Error Response Templates

**TRANSIENT (retry with backoff):**
```
[Attempt 1/3] Tool call failed (transient). Retrying in 2s...
[Attempt 2/3] Tool call failed again. Retrying in 4s...
[Attempt 3/3] Tool call failed after 3 attempts. 
→ Stopping chain. Logging error. Moving to alternative approach.
```

**PERMISSION (hard stop):**
```
Tool call blocked: Permission denied
Error: [specific error]
This operation requires [required permission].
I'm stopping this task and will notify you of the issue.
```

**LOGIC (analyze and reconsider):**
```
Tool returned unexpected result.
Expected: [type/schema]
Got: [actual]
Analysis: [what this means]
Decision: [reassess approach]
```

---

## 🔄 Retry Protocol

```
RETRY DECISION TREE:

Tool call fails?
    │
    ├─ Is TRANSIENT?
    │   └─ YES → Retry with backoff (2s → 4s → 8s)
    │           └─ Still fails after 3x → Stop chain
    │
    ├─ Is PERMISSION?
    │   └─ YES → Hard stop. Log. Notify user.
    │
    ├─ Is PARAM?
    │   └─ YES → Fix params → Retry 1x
    │           └─ Still fails → Stop chain
    │
    ├─ Is LOGIC?
    │   └─ YES → Analyze. Reassess. May need different tool.
    │
    └─ Is UNKNOWN?
        └─ YES → Stop. Log error. Ask user.
```

---

## 🛑 Iteration Termination Conditions

**Stop the current execution chain when ANY of:**

```
┌─────────────────────────────────────────────────────────┐
│ TERMINATION CONDITIONS (ANY triggers stop)               │
│                                                          │
│ 1. Max retries exceeded (3x for TRANSIENT)               │
│ 2. PERMISSION error (cannot proceed)                     │
│ 3. LOGIC error (tool behavior unexpected)                 │
│ 4. Output exceeds reasonable size (alert user)           │
│ 5. Task explicitly cancelled by user                     │
│ 6. Token budget exceeded (>75% of session budget)        │
│ 7. Chain depth > 10 steps (likely looping)              │
│ 8. Negative progress (same error 3x in a row)           │
└─────────────────────────────────────────────────────────┘
```

---

## 📊 Execution Metrics

| Metric | Definition | Target |
|--------|-----------|--------|
| `tool_success_rate` | Successful calls / total calls | > 0.90 |
| `retry_rate` | Retries needed / total calls | < 0.10 |
| `error_classification_accuracy` | Errors correctly classified / total errors | > 0.85 |
| `chain_completion_rate` | Chains completed / chains started | > 0.80 |
| `premature_termination_rate` | Stops without user intent / total stops | < 0.05 |

---

## 🔧 Tool-Specific Execution Notes

### mempalace_* tools
```
- Always handle empty results gracefully (not errors)
- semantic search: use max_distance threshold to filter noise
- KG queries: handle "no facts found" as valid result
- Don't assume DB exists — handle connection errors
```

### exec (shell)
```
- Prefer && over ; (stop on first failure)
- Always explain what the command does before running
- For destructive commands: echo the command, ask for confirmation
- Capture stderr in output, not just stdout
```

### web_search / web_fetch
```
- web_search: first, get overview
- web_fetch: only on specific URLs, not raw search dumps
- Limit fetch size to avoid token bloat
- Handle 403/robots.txt as "unavailable", not error
```

### sessions_spawn
```
- Define clear success criteria before spawning
- Set reasonable timeout
- Always collect results (sessions_yield)
- Don't spawn and forget — monitor
```

---

## 🔗 Integration Points

```
BEFORE TOOL CALL:
1. BehavioralHarness — check Red Lines + Boundaries
2. ExecutionHarness — verify tool selection + dependencies

AFTER TOOL CALL:
1. ExecutionHarness — classify error, route
2. EvaluationHarness — verify output quality
3. SelfOptimizationHarness — log for metrics

DURING CHAIN:
- After each step: check termination conditions
- Every 5 steps: progress checkpoint (log to memory)
```

---

**Version:** 1.0
**Last Updated:** 2026-04-20
**Status:** ACTIVE
