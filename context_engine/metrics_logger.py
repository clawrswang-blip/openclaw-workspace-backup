#!/usr/bin/env python3
"""
metrics_logger.py

Tracks context layer and memory system metrics.
All metrics written to: context_engine/metrics_history.jsonl

Usage:
  python metrics_logger.py --log metric_name value
  python metrics_logger.py --report weekly
  python metrics_logger.py --check threshold
"""

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

# --- Paths ---
WORKSPACE = Path.home() / ".openclaw" / "workspace"
METRICS_FILE = WORKSPACE / "context_engine" / "metrics_history.jsonl"
MEMORY_METRICS = WORKSPACE / "context_engine" / "memory_metrics.jsonl"

METRICS_DIR = METRICS_FILE.parent
METRICS_DIR.mkdir(parents=True, exist_ok=True)


# --- Metric Definitions ---
METRIC_THRESHOLDS = {
    # Context Layer
    "context_satisfaction": {"threshold": 3.0, "direction": "above", "severity": "high"},
    "conflict_rate": {"threshold": 0.25, "direction": "below", "severity": "high"},
    "missed_context_rate": {"threshold": 0.35, "direction": "below", "severity": "high"},
    "redundant_injection_rate": {"threshold": 0.60, "direction": "below", "severity": "medium"},
    "layer3_recall_precision": {"threshold": 0.50, "direction": "above", "severity": "high"},

    # Memory System
    "kg_stale_rate": {"threshold": 0.15, "direction": "below", "severity": "high"},
    "kg_orphaned_count": {"threshold": 10, "direction": "below", "severity": "medium"},
    "memory_write_consistency": {"threshold": 0.75, "direction": "above", "severity": "medium"},
    "recall_miss_rate": {"threshold": 0.40, "direction": "below", "severity": "high"},

    # Skill Layer
    "skill_context_leak_rate": {"threshold": 0.05, "direction": "below", "severity": "high"},
    "skill_output_useful_rate": {"threshold": 0.65, "direction": "above", "severity": "medium"},
    "skill_success_rate": {"threshold": 0.85, "direction": "above", "severity": "high"},

    # External Layer
    "external_data_value_rate": {"threshold": 0.20, "direction": "above", "severity": "medium"},
}


def log_metric(metric_name: str, value: float, tags: dict = None):
    """Log a single metric observation."""
    if metric_name not in METRIC_THRESHOLDS:
        print(f"Warning: unknown metric '{metric_name}'", file=sys.stderr)

    record = {
        "timestamp": datetime.now().isoformat(),
        "metric": metric_name,
        "value": value,
        "tags": tags or {},
    }

    with open(METRICS_FILE, "a") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

    return record


def log_memory_metric(category: str, metric_name: str, value, detail: str = ""):
    """Log memory system specific metric."""
    record = {
        "timestamp": datetime.now().isoformat(),
        "category": category,
        "metric": metric_name,
        "value": value,
        "detail": detail,
    }

    with open(MEMORY_METRICS, "a") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

    return record


def get_recent_metrics(metric_name: str, days: int = 7) -> list:
    """Get recent values for a metric."""
    if not METRICS_FILE.exists():
        return []

    cutoff = (datetime.now() - timedelta(days=days)).isoformat()
    results = []

    with open(METRICS_FILE) as f:
        for line in f:
            try:
                record = json.loads(line)
                if record["metric"] == metric_name and record["timestamp"] > cutoff:
                    results.append(record)
            except json.JSONDecodeError:
                continue

    return results


def calculate_average(metric_name: str, days: int = 7) -> Optional[float]:
    """Calculate average value for a metric over N days."""
    values = get_recent_metrics(metric_name, days)
    if not values:
        return None
    return sum(v["value"] for v in values) / len(values)


def check_thresholds() -> list:
    """Check all metrics against thresholds. Returns list of violations."""
    violations = []

    for metric, config in METRIC_THRESHOLDS.items():
        avg = calculate_average(metric)
        if avg is None:
            continue

        threshold = config["threshold"]
        direction = config["direction"]

        if direction == "below" and avg < threshold:
            violations.append({
                "metric": metric,
                "current": avg,
                "threshold": threshold,
                "severity": config["severity"],
                "message": f"{metric}: {avg:.3f} < {threshold} (threshold)"
            })
        elif direction == "above" and avg > threshold:
            violations.append({
                "metric": metric,
                "current": avg,
                "threshold": threshold,
                "severity": config["severity"],
                "message": f"{metric}: {avg:.3f} > {threshold} (threshold)"
            })

    return violations


def generate_weekly_report() -> dict:
    """Generate weekly metrics summary."""
    report = {
        "generated_at": datetime.now().isoformat(),
        "period": "7 days",
        "metrics_summary": {},
        "violations": [],
        "recommendations": []
    }

    # Collect metric summaries
    for metric in METRIC_THRESHOLDS:
        values = get_recent_metrics(metric, days=7)
        if values:
            avg = sum(v["value"] for v in values) / len(values)
            report["metrics_summary"][metric] = {
                "count": len(values),
                "average": round(avg, 4),
                "min": round(min(v["value"] for v in values), 4),
                "max": round(max(v["value"] for v in values), 4),
                "recent": values[-1]["value"] if values else None
            }

    # Check violations
    violations = check_thresholds()
    report["violations"] = violations

    # Generate recommendations
    for v in violations:
        if v["severity"] == "high":
            report["recommendations"].append(
                f"[HIGH] {v['message']} → Requires immediate review"
            )
        else:
            report["recommendations"].append(
                f"[MEDIUM] {v['message']} → Monitor closely"
            )

    return report


# --- CLI ---
def main():
    parser = argparse.ArgumentParser(description="Context Metrics Logger")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Log command
    log_parser = subparsers.add_parser("log", help="Log a metric")
    log_parser.add_argument("metric", help="Metric name")
    log_parser.add_argument("value", type=float, help="Metric value")
    log_parser.add_argument("--tag", action="append", dest="tags", help="Tags: key=value")

    # Report command
    report_parser = subparsers.add_parser("report", help="Generate report")
    report_parser.add_argument("--weekly", action="store_true", help="Weekly report")
    report_parser.add_argument("--output", help="Output file")

    # Check command
    check_parser = subparsers.add_parser("check", help="Check thresholds")

    # Status command
    status_parser = subparsers.add_parser("status", help="Current metric status")

    args = parser.parse_args()

    if args.command == "log":
        tags = {}
        if args.tags:
            for t in args.tags:
                if "=" in t:
                    k, v = t.split("=", 1)
                    tags[k] = v
        record = log_metric(args.metric, args.value, tags)
        print(f"Logged: {record['metric']} = {record['value']}")

    elif args.command == "report":
        report = generate_weekly_report()
        output = json.dumps(report, indent=2, ensure_ascii=False)
        if args.output:
            Path(args.output).write_text(output)
            print(f"Report written to {args.output}")
        else:
            print(output)

    elif args.command == "check":
        violations = check_thresholds()
        if violations:
            print("⚠️  Threshold Violations:")
            for v in violations:
                print(f"  [{v['severity'].upper()}] {v['message']}")
            sys.exit(1)
        else:
            print("✅ All metrics within thresholds")

    elif args.command == "status":
        print("=== Current Metric Status (7-day average) ===")
        for metric in METRIC_THRESHOLDS:
            avg = calculate_average(metric)
            config = METRIC_THRESHOLDS[metric]
            if avg is not None:
                status = "✅" if (
                    (config["direction"] == "below" and avg < config["threshold"]) or
                    (config["direction"] == "above" and avg > config["threshold"])
                ) else "⚠️"
                print(f"{status} {metric}: {avg:.3f} (threshold: {config['threshold']})")
            else:
                print(f"📊 {metric}: no data")

    else:
        parser.print_help()


if __name__ == "__main__":
    sys.exit(main())
