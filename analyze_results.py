#!/usr/bin/env python3
"""
Analyze benchmark results to identify memory leaks and patterns.

This script parses benchmark output and provides statistical analysis to help
identify memory leak patterns across different scenarios.
"""

import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class BenchmarkResult:
    """Single benchmark result"""

    stack: str
    method: str
    status: str
    round: int
    diff: float
    initial: float
    final: float
    ops: int
    create_ratio: float
    read_ratio: float
    update_ratio: float
    delete_ratio: float


def parse_markdown_table(content: str) -> List[BenchmarkResult]:
    """Parse markdown table format results"""
    results = []

    # Pattern to match markdown table rows
    pattern = r"\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(\d+)\s*\|\s*([-\d.]+)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|\s*(\d+)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|"

    for line in content.split("\n"):
        if match := re.match(pattern, line):
            try:
                result = BenchmarkResult(
                    stack=match.group(1).strip(),
                    method=match.group(2).strip(),
                    status=match.group(3).strip(),
                    round=int(match.group(4)),
                    diff=float(match.group(5)),
                    initial=float(match.group(6)),
                    final=float(match.group(7)),
                    ops=int(match.group(8)),
                    create_ratio=float(match.group(9)),
                    read_ratio=float(match.group(10)),
                    update_ratio=float(match.group(11)),
                    delete_ratio=float(match.group(12)),
                )
                results.append(result)
            except ValueError:
                continue

    return results


def analyze_memory_leaks(results: List[BenchmarkResult]) -> Dict:
    """Analyze results to identify memory leak patterns"""
    analysis = {
        "total_tests": len(results),
        "scenarios": defaultdict(list),
        "leak_suspects": [],
        "stable_scenarios": [],
        "statistics": {},
    }

    # Group by scenario and method
    grouped = defaultdict(lambda: defaultdict(list))
    for result in results:
        key = f"{result.stack}_{result.method}"
        grouped[result.stack][result.method].append(result)

    # Analyze each group
    for stack, methods in grouped.items():
        for method, rounds in methods.items():
            if len(rounds) < 3:
                continue

            # Sort by round
            rounds = sorted(rounds, key=lambda x: x.round)

            # Calculate statistics
            diffs = [r.diff for r in rounds]
            avg_diff = sum(diffs) / len(diffs)
            first_round_diff = rounds[0].diff
            subsequent_diffs = diffs[1:]
            avg_subsequent = sum(subsequent_diffs) / len(subsequent_diffs) if subsequent_diffs else 0

            # Memory leak indicators
            is_leak_suspect = False
            reasons = []

            # 1. Consistently positive growth after first round
            if avg_subsequent > 2:  # More than 2MB average growth
                is_leak_suspect = True
                reasons.append(f"Consistent growth: {avg_subsequent:.2f} MB/round")

            # 2. No stabilization
            if all(d > 0 for d in subsequent_diffs[-3:]) if len(subsequent_diffs) >= 3 else False:
                is_leak_suspect = True
                reasons.append("No stabilization in last 3 rounds")

            # 3. Large total growth
            total_growth = rounds[-1].final - rounds[0].initial
            if total_growth > 50 and len(rounds) >= 5:
                is_leak_suspect = True
                reasons.append(f"Large total growth: {total_growth:.2f} MB")

            # Record findings
            scenario_info = {
                "stack": stack,
                "method": method,
                "rounds": len(rounds),
                "avg_diff": avg_diff,
                "avg_subsequent": avg_subsequent,
                "first_round_diff": first_round_diff,
                "total_growth": total_growth,
                "final_memory": rounds[-1].final,
                "diffs": diffs,
            }

            if is_leak_suspect:
                scenario_info["reasons"] = reasons
                analysis["leak_suspects"].append(scenario_info)
            elif abs(avg_subsequent) < 1:  # Stable if less than 1MB variation
                analysis["stable_scenarios"].append(scenario_info)

            analysis["scenarios"][stack].append(scenario_info)

    return analysis


def print_analysis_report(analysis: Dict):
    """Print formatted analysis report"""

    print("\n" + "=" * 80)
    print("MEMORY LEAK ANALYSIS REPORT")
    print("=" * 80 + "\n")

    print(f"Total tests analyzed: {analysis['total_tests']}\n")

    # Leak suspects
    if analysis["leak_suspects"]:
        print("⚠️  POTENTIAL MEMORY LEAKS DETECTED\n")
        print(f"Found {len(analysis['leak_suspects'])} suspect scenarios:\n")

        for suspect in sorted(analysis["leak_suspects"], key=lambda x: x["avg_subsequent"], reverse=True):
            print(f"Stack: {suspect['stack']}")
            print(f"Method: {suspect['method']}")
            print(f"Average growth per round: {suspect['avg_subsequent']:.2f} MB")
            print(f"Total growth: {suspect['total_growth']:.2f} MB")
            print(f"Final memory: {suspect['final_memory']:.2f} MB")
            print(f"Rounds: {suspect['rounds']}")
            print("Reasons:")
            for reason in suspect["reasons"]:
                print(f"  - {reason}")
            print(f"Memory diffs by round: {[f'{d:.2f}' for d in suspect['diffs']]}")
            print()
    else:
        print("✅ No obvious memory leaks detected\n")

    # Stable scenarios
    if analysis["stable_scenarios"]:
        print(f"✅ STABLE SCENARIOS ({len(analysis['stable_scenarios'])})\n")
        print("These scenarios show minimal memory growth after initialization:\n")

        for stable in sorted(analysis["stable_scenarios"], key=lambda x: abs(x["avg_subsequent"]))[:10]:
            print(f"- {stable['stack']} / {stable['method']}")
            print(f"  Average growth: {stable['avg_subsequent']:.2f} MB/round")
            print(f"  Final memory: {stable['final_memory']:.2f} MB")
            print()

    # Comparative analysis
    print("\n" + "=" * 80)
    print("COMPARATIVE ANALYSIS")
    print("=" * 80 + "\n")

    # Compare by scenario type
    scenario_stats = defaultdict(lambda: {"count": 0, "avg_growth": []})

    for scenario in analysis["scenarios"].values():
        for info in scenario:
            scenario_type = info["stack"].split("_")[0]  # sqlalchemy1x or sqlalchemy2x
            scenario_stats[scenario_type]["count"] += 1
            scenario_stats[scenario_type]["avg_growth"].append(info["avg_subsequent"])

    print("Average memory growth by SQLAlchemy version:\n")
    for scenario_type, stats in sorted(scenario_stats.items()):
        if stats["avg_growth"]:
            avg = sum(stats["avg_growth"]) / len(stats["avg_growth"])
            print(f"{scenario_type}: {avg:.2f} MB/round (across {stats['count']} tests)")

    print("\n" + "=" * 80)
    print()


def main():
    """Main analysis function"""
    import argparse

    parser = argparse.ArgumentParser(description="Analyze benchmark results for memory leaks")
    parser.add_argument("file", nargs="?", help="File containing benchmark results (or stdin)")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown", help="Output format")
    parser.add_argument("--threshold", type=float, default=2.0, help="Memory leak threshold in MB (default: 2.0)")

    args = parser.parse_args()

    # Read input
    if args.file:
        with open(args.file, "r") as f:
            content = f.read()
    else:
        content = sys.stdin.read()

    # Parse results
    results = parse_markdown_table(content)

    if not results:
        print("No results found in input", file=sys.stderr)
        return 1

    # Analyze
    analysis = analyze_memory_leaks(results)

    # Print report
    if args.format == "markdown":
        print_analysis_report(analysis)
    elif args.format == "json":
        import json

        print(json.dumps(analysis, indent=2, default=str))

    return 0


if __name__ == "__main__":
    sys.exit(main())
