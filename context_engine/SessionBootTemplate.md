# Session Boot Template
> In-session Context Assembly Protocol — uses MCP tool calls directly.
> Follow this template at session start (or before major task switches).

---

## 🎯 Purpose

This template replaces the CLI `session_boot.py` for actual agent sessions.
The agent reads this template and executes MCP calls to assemble real context.

**Key difference:**
- `session_boot.py` → CLI for testing/standalone (no MCP access)
- `SessionBootTemplate.md` → Protocol for in-session MCP calls

---

## 📋 Session Boot Protocol

### STEP 0: Before Starting

Read these files (always, full load):
```
→ SOUL.md (identity + cognitive framework)
→ USER.md (user profile + current context)
→ IDENTITY.md (Luna's identity card)
```

These are Layer 2 — always loaded, never filtered.

---

### STEP 1: Classify Current Task

Based on user's latest message:

```
Task Type: DECISION / ANALYSIS / CREATIVE / EXECUTION / RESEARCH / REVIEW / CHAT
Project Tags: [list relevant projects]
Time Sensitivity: low / medium / high
```

**Task Classification Keywords:**

| Type | Keywords |
|------|----------|
| DECISION | should, decision, choose, prioritize, which option, worth it, better |
| ANALYSIS | analyze, data, trend, compare, evaluate, understand, why |
| CREATIVE | create, generate, design, write, brainstorm, concept |
| EXECUTION | do, execute, run, build, implement, send, schedule, find |
| RESEARCH | research, search, find information, look up, investigate, what is |
| REVIEW | review, critique, improve, optimize, refine, assess |
| CHAT | [anything else] |

**Project Tag Detection:**

| Project | Keywords |
|---------|----------|
| sungiven | sungiven, grocery, membership, uber eats, 饭团, 馋猫, vancouver, sfc |
| ai-consulting | ai consulting, 信誉楼, enterprise ai, 4a, marketing ai, ai转型 |
| openclaw | openclaw, luna, agent, context, prompt, skill, memory, kg, drawer, mcp |
| pr-plan | pr, canada pr, immigration, permanent resident, visa, 枫叶卡 |
| life | family, wife, baby, hong kong, vancouver, move, relocate |

---

### STEP 2: Dynamic Layer 3 Recall (MCP Calls)

Execute these MCP calls in sequence:

#### A. MemPalace Semantic Search (Top-K relevant drawers)

```
mempalace_search(
  query: "<task_type> <project_tags[0]> <project_tags[1]> ...",
  limit: 5,
  max_distance: 1.2
)
```

**Example:** Task = "analyze sungiven membership growth"
```
query: "analysis sungiven membership growth"
limit: 5
```

**Scoring Rule:**
- similarity > 0.7 → FULL INJECT
- similarity 0.5-0.7 → SUMMARY INJECT
- similarity < 0.5 → SKIP (can recall on-demand)

#### B. KG Entity Query (for each project tag)

```
mempalace_kg_query(entity: "<ProjectName>")
mempalace_kg_query(entity: "<Rishon>")  # Always include user entity
```

**Example:** For sungiven task:
```
mempalace_kg_query(entity: "Sungiven Foods")
mempalace_kg_query(entity: "Rishon")
```

#### C. KG Timeline (for recent facts across all entities)

```
mempalace_kg_timeline(entity: null)  # null = all entities
```

Returns chronological facts — useful for understanding recent changes.

---

### STEP 3: Project File Check

For each detected project, check if `memory/projects/<project>.md` exists:

```
File: memory/projects/<project>.md

If exists AND relevant:
  → Determine relevance score based on task keywords
  → score > 0.5 → INJECT (summary or full based on score)
  → score > 0.8 → FULL INJECT
  → score 0.5-0.8 → SUMMARY INJECT
  → score < 0.5 → SKIP (not discarded, just not pre-loaded)
```

---

### STEP 4: Daily Log Check (recent 2-3 days)

Check for recent daily logs:
```
memory/YYYY-MM-DD.md (today)
memory/YYYY-MM-DD.md (yesterday)
memory/YYYY-MM-DD.md (2 days ago)
```

Only inject if:
- Log contains keywords matching current task
- OR log was referenced in semantic search results

---

### STEP 5: Conflict Detection

After collecting all sources, check for conflicts:

```
If multiple sources state different facts about the same entity:
  → Annotate: [CONFLICT: source A says X, source B says Y]
  → Do NOT resolve automatically
  → Surface to user in response
```

---

### STEP 6: Build Prioritized Context Bundle

Assemble the final context for injection:

```json
{
  "session_boot": {
    "task_type": "ANALYSIS",
    "project_tags": ["sungiven"],
    "sources": [
      {
        "source": "mempalace_drawer: drawer_xxx",
        "type": "semantic_recall",
        "relevance_score": 0.82,
        "injection_mode": "full",
        "content_summary": "..."
      },
      {
        "source": "mempalace_kg: Rishon → works_on → Sungiven membership",
        "type": "kg_fact",
        "relevance_score": 0.91,
        "injection_mode": "full"
      },
      {
        "source": "memory/projects/sungiven.md",
        "type": "project_file",
        "relevance_score": 0.73,
        "injection_mode": "summary",
        "relevant_snippets": ["5.8万会员", "目标10万", "60%利润来自会员"]
      }
    ],
    "conflicts": [],
    "recall_stats": {
      "total_sources_found": 8,
      "full_inject": 3,
      "summary_inject": 4,
      "skipped": 1
    }
  }
}
```

---

## 🔄 Mid-Session Context Refresh

**When to refresh:**
- User switches task type significantly
- User mentions a new project
- Session is > 1 hour old
- You notice context feels stale

**How to refresh:**
1. Re-run Steps 1-6 with new task classification
2. Compare new bundle with current context
3. Inject new relevant sources
4. Mark stale sources as deprecated

---

## 📝 KG Fact Capture Protocol (During Session)

**IMPORTANT: KG must be populated during conversation, not just read.**

### Trigger: Key Information Detected

When any of these occur during conversation, immediately write to KG:

| Event | KG Write |
|-------|----------|
| User makes a decision | `mempalace_kg_add` — subject=Rishon, predicate=decided, object=<decision> |
| User expresses preference | `mempalace_kg_add` — subject=Rishon, predicate=prefers, object=<preference> |
| New project milestone | `mempalace_kg_add` — subject=<project>, predicate=achieved, object=<milestone> |
| Constraint revealed | `mempalace_kg_add` — subject=Rishon, predicate=constrained_by, object=<constraint> |
| Learning/insight | `mempalace_kg_add` — subject=Luna, predicate=learned, object=<insight> |
| User corrects previous info | `mempalace_kg_invalidate` old fact → `mempalace_kg_add` new fact |

### Post-Session KG Write (Every Session End)

Before session ends, execute:

```
For each significant thing discussed:
  → If worth remembering → KG add
  → If substantive insight → MemPalace Drawer add

For session overall:
  → Log session summary → memory/YYYY-MM-DD.md
  → Update MEMORY.md index if new facts
```

---

## 🔧 KG Entity Auto-Population

When you encounter a new entity (person, company, concept) during conversation:

```
1. Check: mempalace_kg_query(entity: "<new_entity>")
   → If exists: use existing facts
   → If not: create new entity with initial fact

2. New entity creation:
   mempalace_kg_add(
     subject: "<new_entity>",
     predicate: "first_mentioned",
     object: "Rishon conversation <date>",
     valid_from: "<today>"
   )

3. Tag the entity to relevant project:
   mempalace_kg_add(
     subject: "<new_entity>",
     predicate: "related_to_project",
     object: "<project_name>"
   )
```

---

## 📊 Post-Boot Quality Check

After assembly, self-verify:

```
□ Did I find at least 1 relevant KG fact?
□ Did I find at least 1 relevant project file or drawer?
□ Is the context directly answering the user's task?
□ Are there any obvious conflicts I should flag?
□ Did I update KG with any new facts from this conversation?
```

**If context feels incomplete:**
```
1. Re-run semantic search with different query
2. Check KG for related entities
3. Ask user: "Do you want me to search for X specifically?"
```

---

## 🚀 Quick Reference (Copy-Paste MCP Calls)

```
Semantic recall:
/invoke mempalace_search
{"query": "<task> <project>", "limit": 5}

KG entity:
/invoke mempalace_kg_query
{"entity": "<name>"}

KG timeline:
/invoke mempalace_kg_timeline
{}

Add fact:
/invoke mempalace_kg_add
{"subject": "<s>", "predicate": "<p>", "object": "<o>", "valid_from": "<YYYY-MM-DD>"}

Invalidate old fact:
/invoke mempalace_kg_invalidate
{"subject": "<s>", "predicate": "<p>", "object": "<o>"}
```

---

**Version:** 1.0
**Last Updated:** 2026-04-20
**Status:** ACTIVE — Use this template at every session boot
