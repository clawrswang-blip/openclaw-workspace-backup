# Execution Harness — Active Triggers
> Tool failures are only handled well if they're classified. This is WHEN and HOW to classify.

---

## 🚨 Trigger Points

### Trigger 1: ANY Tool Call Returns an Error

```
TOOL ERROR = any non-successful return from a tool call

WHEN THIS FIRES:
  Tool returns: error, empty result where content expected, permission denied,
  timeout, connection failed, etc.

IMMEDIATE RESPONSE: Stop. Classify. Route.
```

**Error Classification Decision Tree:**

```
STEP 1: What type of error?

Is it...
  A) TRANSIENT
     Signals: timeout, rate limit, connection reset, ETIMEDOUT, 429, 503
     → Retry with backoff

  B) PERMISSION
     Signals: access denied, unauthorized, forbidden, EACCES, permission denied
     → HARD STOP. Log. Notify user.

  C) PARAM
     Signals: invalid argument, wrong type, missing required param, EINVAL
     → Fix params. Retry 1x.

  D) NOT_FOUND
     Signals: file not found, path does not exist, 404, ENOENT
     → Check path. Try alternative. If essential: STOP.

  E) LOGIC
     Signals: tool returned unexpected type/schema, result doesn't match expectation
     → STOP chain. Analyze. May need different tool.

  F) UNKNOWN
     Signals: anything else
     → STOP. Log error. Ask user.

STEP 2: Route according to type (see below)

STEP 3: Log the classification for Self-Optimization Harness
```

**Routing by Type:**

```
A) TRANSIENT → RETRY PROTOCOL
┌─────────────────────────────────────────────────────┐
│ Attempt 1: Call tool                                  │
│ ↓ Failed (timeout/rate limit)                         │
│ Attempt 2: Wait 2s → Retry                          │
│ ↓ Failed again                                         │
│ Attempt 3: Wait 4s → Retry                          │
│ ↓ Failed again                                         │
│ STOP. Log: "TRANSIENT error after 3 retries."        │
│ Proceed with alternative approach or notify user.     │
└─────────────────────────────────────────────────────┘

B) PERMISSION → HARD STOP
┌─────────────────────────────────────────────────────┐
│ STOP immediately.                                     │
│ Log: "[TOOL] permission denied — [specific reason]"   │
│ Notify user: "I need [permission] to do this."        │
│ Do NOT retry silently.                                │
└─────────────────────────────────────────────────────┘

C) PARAM → FIX AND RETRY
┌─────────────────────────────────────────────────────┐
│ Identify: Which parameter is wrong?                   │
│ Fix the parameter.                                    │
│ Retry 1x.                                            │
│ ↓ Still fails                                        │
│ STOP. Log: "PARAM error persisted after retry."       │
└─────────────────────────────────────────────────────┘

D) NOT_FOUND → TRY ALTERNATIVE
┌─────────────────────────────────────────────────────┐
│ Check: Is this file/resource actually needed?         │
│ Try alternative path or method.                       │
│ If essential resource + not found:                   │
│   STOP. Notify user.                                 │
└─────────────────────────────────────────────────────┘

E) LOGIC → STOP AND ANALYZE
┌─────────────────────────────────────────────────────┐
│ STOP the current chain.                               │
│ Ask: "Did I use the right tool for this?"            │
│ Ask: "Is the tool's behavior what I expected?"      │
│ Consider: Different tool? Different approach?        │
│ If no good alternative:                             │
│   Notify user with what happened.                   │
└─────────────────────────────────────────────────────┘

F) UNKNOWN → STOP AND LOG
┌─────────────────────────────────────────────────────┐
│ STOP.                                                │
│ Log: "[TOOL] unknown error — [raw error message]"   │
│ Notify user: "Something unexpected happened."        │
│ Ask: "How would you like to proceed?"               │
└─────────────────────────────────────────────────────┘
```

---

### Trigger 2: Chain Depth > 5 Steps

```
WHEN: Any execution chain reaches 5+ steps

CHECK:
□ Is this chain still making progress?
□ Have I been repeating similar steps?
□ Is this a loop (same step trying same thing)?

IF LOOP DETECTED:
  → STOP. You're going in circles.
  → Log: "Chain stopped: loop detected at step N"
  → Explain to user: "I've been trying the same approach N times without progress."

IF NO PROGRESS AFTER 5 STEPS:
  → Pause. Report current state.
  → Ask: "Should I continue or try a different approach?"
```

---

### Trigger 3: Before Any Multi-Step Chain

```
WHEN: About to execute a sequence of 3+ tool calls

PRE-EXECUTION CHECK:
□ Is the goal clear? Can I state it in one sentence?
□ Do I have the right tool sequence?
  → Tool A must run before Tool B?
  → Any parallel calls possible?
□ Do I have success criteria?
  → How will I know if the chain succeeded?
□ What's the fallback if step N fails?
  → Have a plan before starting.
```

---

### Trigger 4: Session End — Execution Metrics

```
WHEN: Session ending (per Session End Protocol)

LOG THESE FOR EXECUTION HARNESS:
  - Tool calls this session: [count]
  - Successes: [count]
  - Errors: [count]
  - Error types encountered: [list]
  - Retries: [count]
  - Chains completed: [count]
  - Chains stopped: [count] + reasons

python3 context_engine/metrics_logger.py --log tool_success_rate [0-1]
python3 context_engine/metrics_logger.py --log execution_error_type [type]
```

---

## ✅ Execution Harness — Quick Reference

```
TOOL ERROR?

Is it...
  timeout/rate limit?     → RETRY (2s → 4s → 8s)
  permission denied?       → HARD STOP
  bad param?              → FIX → RETRY 1x
  not found?              → TRY ALTERNATIVE
  unexpected result?      → STOP CHAIN
  something else?         → STOP + LOG

CHAIN DEPTH > 5?
  Loop detected? → STOP
  No progress? → PAUSE + ASK

MULTI-STEP?
  Goal clear? Tools right? Fallback ready?
```

---

**Version:** 1.1 (active triggers added)
**Last Updated:** 2026-04-20
