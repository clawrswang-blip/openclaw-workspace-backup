#!/usr/bin/env python3
"""
session_boot.py — Context Assembly for OpenClaw

IMPORTANT: This script runs as a CLI tool. It provides Context Assembly Protocol
guidance for use WITHIN an agent session. For actual runtime, the agent follows
the SessionBootTemplate.md which contains the same logic but uses MCP tool calls.

This CLI is for:
- Testing Context Assembly logic standalone
- Debugging recall quality
- Manual context queries

For real session boot, see: context_engine/SessionBootTemplate.md
"""

import argparse
import json
import sys
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

WORKSPACE = Path.home() / ".openclaw" / "workspace"
MEMORY_DIR = WORKSPACE / "memory"
PROJECTS_DIR = MEMORY_DIR / "projects"

# --- KG Entity Registry ---
# This is the authoritative list of what SHOULD be in KG.
# In production, KG_PROJECT_ENTITIES is queried via MCP.
# This file provides fallback + documents expected KG structure.

KG_PROJECT_ENTITIES = {
    "sungiven": [
        "Sungiven Foods",
        "Uber Eats integration",
        "饭团 delivery",
        "馋猫外送",
        "membership system",
        "C$9,000/month revenue",
        "5.8万会员",
        "10万会员目标",
    ],
    "ai-consulting": [
        "信誉楼",
        "enterprise AI transformation",
        "4A consulting",
        "AI tools development",
    ],
    "openclaw": [
        "Luna agent",
        "context layer",
        "prompt engineering",
        "MemPalace",
        "SOUL.md",
        "Dynamic Optimizer",
    ],
    "pr-plan": [
        "Canada PR",
        "October 2026",
        "immigration process",
        "Plan B: Hong Kong",
        "Plan B: 杭州",
    ],
    "life": [
        "family",
        "wife",
        "baby",
        "Hong Kong",
        "Vancouver",
    ]
}


TASK_TYPES = {
    "DECISION": ["should", "should we", "decision", "choose", "prioritize", "which option", "worth it", "better"],
    "ANALYSIS": ["analyze", "analysis", "data", "trend", "compare", "understand", "why", "how does", "evaluate"],
    "CREATIVE": ["create", "generate", "design", "write", "brainstorm", "concept", "ideate", "concept"],
    "EXECUTION": ["do", "execute", "run", "build", "implement", "send", "schedule", "find", "get it done"],
    "RESEARCH": ["research", "search", "find information", "look up", "investigate", "what is", "how does x work"],
    "REVIEW": ["review", "critique", "improve", "optimize", "refine", "assess"],
    "CHAT": []
}

PROJECT_KEYWORDS = {
    "sungiven": ["sungiven", "sungiven foods", "grocery", "membership", "uber eats", "饭团", "馋猫", "vancouver", "sfc"],
    "ai-consulting": ["ai consulting", "信誉楼", "enterprise ai", "4a", "marketing ai", "ai转型"],
    "openclaw": ["openclaw", "luna", "agent", "context", "prompt", "skill", "memory", "kg", "drawer", "mcp", "dynamic"],
    "pr-plan": ["pr", "canada pr", "immigration", "permanent resident", "visa", "枫叶卡"],
    "life": ["family", "wife", "baby", "hong kong", "vancouver", "move", "relocate", "香港", "温哥华"]
}


def classify_task(user_message: str) -> dict:
    msg_lower = user_message.lower()

    task_type = "CHAT"
    for ttype, keywords in TASK_TYPES.items():
        if any(kw in msg_lower for kw in keywords):
            task_type = ttype
            break

    project_tags = []
    for proj, keywords in PROJECT_KEYWORDS.items():
        if any(kw in msg_lower for kw in keywords):
            project_tags.append(proj)
    if not project_tags:
        project_tags = ["openclaw"]

    time_sensitivity = "low"
    if any(w in msg_lower for w in ["urgent", "asap", "quick", "today", "tonight", "immediately"]):
        time_sensitivity = "high"
    elif any(w in msg_lower for w in ["this week", "soon", "deadline"]):
        time_sensitivity = "medium"

    return {
        "task_type": task_type,
        "project_tags": project_tags,
        "time_sensitivity": time_sensitivity,
        "original_message": user_message
    }


def score_source(source_name: str, source_content: str, task: dict) -> float:
    """Score a source 0.0-1.0 on relevance to current task."""
    msg_lower = task["original_message"].lower()
    combined_lower = (source_name + " " + source_content).lower()

    # Keyword match scoring
    keyword_hits = 0
    for proj in task["project_tags"]:
        proj_keywords = PROJECT_KEYWORDS.get(proj, [])
        keyword_hits += sum(1 for kw in proj_keywords if kw.lower() in combined_lower)

    # Task type relevance
    task_keywords = TASK_TYPES.get(task["task_type"], [])
    task_hits = sum(1 for kw in task_keywords if kw.lower() in combined_lower)

    # Base score
    score = min(1.0, (keyword_hits * 0.08) + (task_hits * 0.05))

    # Filename match boost
    for proj in task["project_tags"]:
        if proj.lower() in source_name.lower():
            score += 0.30

    # Content density boost (longer relevant content is better)
    if keyword_hits >= 3:
        score += 0.10

    return min(1.0, score)


def assemble_context_bundle(task: dict) -> dict:
    """Assemble context bundle with real sources."""
    project_tags = task["project_tags"]
    sources = []

    # --- Project Files ---
    for proj in project_tags:
        proj_file = PROJECTS_DIR / f"{proj}.md"
        if proj_file.exists():
            content = proj_file.read_text(errors='ignore')
            score = score_source(str(proj_file), content, task)
            mode = "full" if score > 0.8 else "summary" if score > 0.5 else "skip"
            # Extract meaningful preview
            preview = extract_preview(content, task)
            sources.append({
                "source": str(proj_file.relative_to(WORKSPACE)),
                "type": "project_file",
                "score": round(score, 3),
                "mode": mode,
                "content_preview": preview
            })

    # --- Daily Logs (recent 5 days) ---
    today = datetime.now()
    for days_ago in range(5):
        date = (today - timedelta(days=days_ago)).strftime("%Y-%m-%d")
        daily_file = MEMORY_DIR / f"{date}.md"
        if daily_file.exists():
            content = daily_file.read_text(errors='ignore')
            score = score_source(str(daily_file), content, task)
            if score > 0.45:  # Lower threshold for daily logs
                preview = extract_preview(content, task)
                sources.append({
                    "source": f"memory/{date}.md",
                    "type": "daily_log",
                    "score": round(score, 3),
                    "mode": "summary",
                    "content_preview": preview
                })

    # --- KG Entities (reference list — actual KG queried via MCP in-session) ---
    kg_entities = []
    for proj in project_tags:
        entities = KG_PROJECT_ENTITIES.get(proj, [])
        for entity in entities:
            score = score_source(entity, "", task)
            if score > 0.4:
                kg_entities.append({
                    "source": f"KG: {entity}",
                    "type": "kg_entity",
                    "score": round(score, 3),
                    "mode": "full" if score > 0.7 else "summary",
                    "content_preview": f"[实体] {entity} — 需通过 MCP mempalace_kg_query 获取完整关系"
                })

    sources.extend(kg_entities)

    # --- Sort ---
    sources.sort(key=lambda x: x["score"], reverse=True)
    injected = [s for s in sources if s["mode"] != "skip"]
    skipped = [s for s in sources if s["mode"] == "skip"][:5]

    # --- Conflict detection (basic) ---
    conflicts = detect_basic_conflicts(sources, task)

    # --- Metrics ---
    precision_est = len([s for s in injected if s["score"] > 0.6]) / max(1, len(injected))
    noise_est = len([s for s in injected if s["score"] < 0.55]) / max(1, len(injected))

    return {
        "session_id": datetime.now().strftime("%Y%m%d%H%M%S"),
        "task": task,
        "assembly_timestamp": datetime.now().isoformat(),
        "total_sources_found": len(sources),
        "injected_sources": injected,
        "skipped_sources": skipped,
        "conflicts": conflicts,
        "optimization_data": {
            "recall_precision_estimate": round(precision_est, 3),
            "noise_estimate": round(noise_est, 3),
            "kg_entity_count": len(kg_entities),
            "file_source_count": len([s for s in sources if s["type"] in ["project_file", "daily_log"]])
        }
    }


def extract_preview(content: str, task: dict) -> str:
    """Extract the most relevant snippet from content."""
    lines = content.split('\n')
    relevant_lines = []

    task_keywords = []
    for proj in task["project_tags"]:
        task_keywords.extend(PROJECT_KEYWORDS.get(proj, []))
    task_keywords.extend(TASK_TYPES.get(task["task_type"], []))
    task_keywords = [kw.lower() for kw in task_keywords if len(kw) > 2]

    # Find lines with keyword matches
    for i, line in enumerate(lines):
        line_lower = line.lower()
        matches = sum(1 for kw in task_keywords if kw in line_lower)
        if matches > 0:
            relevant_lines.append((matches, line.strip()))

    relevant_lines.sort(key=lambda x: x[0], reverse=True)

    if relevant_lines:
        best_lines = [l[1] for l in relevant_lines[:3]]
        return " | ".join(best_lines)

    # Fallback: first non-empty, non-header line
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('---'):
            return line[:200]
    return content[:200]


def detect_basic_conflicts(sources: list, task: dict) -> list:
    """Basic conflict detection between sources."""
    conflicts = []
    # TODO: Implement real conflict detection against KG
    # For now: placeholder — real detection happens via MCP in-session
    return conflicts


def print_bundle(bundle: dict, verbose: bool = False):
    """Pretty print the bundle summary."""
    task = bundle["task"]
    print(f"\n=== Context Assembly: {task['task_type']} / {', '.join(task['project_tags'])} ===")
    print(f"Injected: {len(bundle['injected_sources'])} | Skipped: {len(bundle['skipped_sources'])} | Conflicts: {len(bundle['conflicts'])}")
    print(f"Quality: precision={bundle['optimization_data']['recall_precision_estimate']} | noise={bundle['optimization_data']['noise_estimate']}")

    if verbose:
        print("\n--- INJECTED SOURCES ---")
        for s in bundle["injected_sources"]:
            marker = "📦" if s["type"] == "project_file" else "📄" if s["type"] == "daily_log" else "🔗"
            print(f"  {marker} [{s['score']:.2f}] {s['source']}")
            print(f"       → {s['content_preview'][:120]}")

        if bundle["skipped_sources"]:
            print("\n--- SKIPPED (top 5) ---")
            for s in bundle["skipped_sources"]:
                print(f"  ⏭️  [{s['score']:.2f}] {s['source']}")

    print("\n📋 NOTE: KG entities show placeholder — in-session MCP calls return real KG data")


def main():
    parser = argparse.ArgumentParser(description="Context Assembler — Dynamic Layer 3 Recall")
    parser.add_argument("--task", "-t", type=str, help="Task description")
    parser.add_argument("--interactive", "-i", action="store_true", help="Interactive mode")
    parser.add_argument("--output", "-o", type=str, help="Output JSON file")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    args = parser.parse_args()

    if args.interactive:
        print("Context Assembler Interactive Mode")
        print("Enter task description (or 'quit' to exit):")
        tasks = []
        while True:
            line = input("> ")
            if line.lower() in ["quit", "exit"]:
                break
            if line.strip():
                tasks.append(line)
        user_message = " ".join(tasks)
    elif args.task:
        user_message = args.task
    else:
        print("Error: Provide --task or use --interactive")
        print(__doc__)
        sys.exit(1)

    task = classify_task(user_message)
    bundle = assemble_context_bundle(task)

    if args.output:
        Path(args.output).write_text(json.dumps(bundle, indent=2, ensure_ascii=False))
        print(f"Bundle written to {args.output}")
    else:
        print_bundle(bundle, verbose=args.verbose)

    return 0


if __name__ == "__main__":
    sys.exit(main())
