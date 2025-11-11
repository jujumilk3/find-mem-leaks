#!/usr/bin/env python3
"""
Comprehensive benchmark runner for memory leak testing across various scenarios.

This script automatically runs benchmarks for all SQLAlchemy + framework combinations
with different operation scales and CRUD ratios.
"""

import asyncio
import subprocess
import sys
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class BenchmarkConfig:
    """Configuration for a benchmark scenario"""

    name: str
    num_operations: int
    create_ratio: float
    read_ratio: float
    update_ratio: float
    delete_ratio: float


# Define various CRUD ratio combinations
CRUD_RATIOS = {
    "balanced": BenchmarkConfig(
        name="balanced",
        num_operations=10000,
        create_ratio=0.25,
        read_ratio=0.25,
        update_ratio=0.25,
        delete_ratio=0.25,
    ),
    "create_heavy": BenchmarkConfig(
        name="create_heavy",
        num_operations=10000,
        create_ratio=0.5,
        read_ratio=0.2,
        update_ratio=0.2,
        delete_ratio=0.1,
    ),
    "read_heavy": BenchmarkConfig(
        name="read_heavy",
        num_operations=10000,
        create_ratio=0.1,
        read_ratio=0.6,
        update_ratio=0.2,
        delete_ratio=0.1,
    ),
    "update_heavy": BenchmarkConfig(
        name="update_heavy",
        num_operations=10000,
        create_ratio=0.2,
        read_ratio=0.2,
        update_ratio=0.5,
        delete_ratio=0.1,
    ),
    "delete_heavy": BenchmarkConfig(
        name="delete_heavy",
        num_operations=10000,
        create_ratio=0.1,
        read_ratio=0.2,
        update_ratio=0.2,
        delete_ratio=0.5,
    ),
    "write_intensive": BenchmarkConfig(
        name="write_intensive",
        num_operations=10000,
        create_ratio=0.4,
        read_ratio=0.1,
        update_ratio=0.4,
        delete_ratio=0.1,
    ),
    "read_only": BenchmarkConfig(
        name="read_only",
        num_operations=10000,
        create_ratio=0.05,
        read_ratio=0.85,
        update_ratio=0.05,
        delete_ratio=0.05,
    ),
    "mixed_workload": BenchmarkConfig(
        name="mixed_workload",
        num_operations=10000,
        create_ratio=0.3,
        read_ratio=0.4,
        update_ratio=0.2,
        delete_ratio=0.1,
    ),
}

# Define operation scales
OPERATION_SCALES = {
    "small": 10000,
    "medium": 100000,
    "large": 1000000,
}

# Define all scenarios
SCENARIOS = {
    "sqlalchemy1x": {
        "name": "SQLAlchemy 1.x Standalone",
        "scripts": ["main_async.py", "main_async_scoped_session.py", "main_sync.py", "main_sync_scoped_session.py"],
    },
    "sqlalchemy1x_fastapi": {
        "name": "SQLAlchemy 1.x + FastAPI",
        "scripts": ["main_async.py", "main_async_scoped.py", "main_sync.py", "main_sync_scoped.py"],
    },
    "sqlalchemy1x_fastapi_dependency_injector": {
        "name": "SQLAlchemy 1.x + FastAPI + DI",
        "scripts": ["main_async.py", "main_async_scoped.py", "main_sync.py", "main_sync_scoped.py"],
    },
    "sqlalchemy2x": {
        "name": "SQLAlchemy 2.x Standalone",
        "scripts": ["main_async.py", "main_async_scoped_session.py", "main_sync.py", "main_sync_scoped_session.py"],
    },
    "sqlalchemy2x_fastapi": {
        "name": "SQLAlchemy 2.x + FastAPI",
        "scripts": ["main_async.py", "main_async_scoped.py", "main_sync.py", "main_sync_scoped.py"],
    },
    "sqlalchemy2x_fastapi_dependency_injector": {
        "name": "SQLAlchemy 2.x + FastAPI + DI",
        "scripts": ["main_async.py", "main_async_scoped.py", "main_sync.py", "main_sync_scoped.py"],
    },
}


def generate_benchmark_script(scenario: str, script: str, config: BenchmarkConfig, rounds: int = 5) -> str:
    """Generate a temporary Python script to run benchmarks"""
    return f"""
import sys
sys.path.insert(0, '{scenario}')

from {script.replace('.py', '')} import main
import asyncio

async def run_benchmark():
    results = []
    for round_num in range(1, {rounds + 1}):
        result = await main(
            num_operations={config.num_operations},
            create_ratio={config.create_ratio},
            read_ratio={config.read_ratio},
            update_ratio={config.update_ratio},
            delete_ratio={config.delete_ratio},
        )
        result['round'] = round_num
        results.append(result)

        # Print in markdown table format
        print(f"| {scenario} | {config.name} | ✅ | {{round_num}} | {{result['memory_diff']}} | "
              f"{{result['initial_memory']}} | {{result['final_memory']}} | {{result['num_operations']}} | "
              f"{{result['create_ratio']}} | {{result['read_ratio']}} | {{result['update_ratio']}} | "
              f"{{result['delete_ratio']}} |")

    return results

if __name__ == "__main__":
    asyncio.run(run_benchmark())
"""


def run_benchmark_for_scenario(scenario_dir: str, script: str, config: BenchmarkConfig, rounds: int = 5):
    """Run a benchmark for a specific scenario"""
    print(f"\n{'=' * 80}")
    print(f"Running: {scenario_dir}/{script} - {config.name}")
    print(f"{'=' * 80}\n")

    # Generate temporary script
    temp_script = generate_benchmark_script(scenario_dir, script, config, rounds)

    try:
        # Run the benchmark
        result = subprocess.run(
            [sys.executable, "-c", temp_script],
            capture_output=True,
            text=True,
            timeout=3600,  # 1 hour timeout
        )

        if result.returncode == 0:
            print(result.stdout)
            return True
        else:
            print(f"Error running benchmark: {result.stderr}")
            return False

    except subprocess.TimeoutExpired:
        print(f"Benchmark timed out after 1 hour")
        return False
    except Exception as e:
        print(f"Exception running benchmark: {e}")
        return False


def main():
    """Main benchmark runner"""
    import argparse

    parser = argparse.ArgumentParser(description="Run comprehensive memory leak benchmarks")
    parser.add_argument(
        "--scenarios",
        nargs="+",
        choices=list(SCENARIOS.keys()) + ["all"],
        default=["all"],
        help="Scenarios to run (default: all)",
    )
    parser.add_argument(
        "--configs",
        nargs="+",
        choices=list(CRUD_RATIOS.keys()) + ["all"],
        default=["all"],
        help="CRUD ratio configurations to test (default: all)",
    )
    parser.add_argument(
        "--scales",
        nargs="+",
        choices=list(OPERATION_SCALES.keys()) + ["all"],
        default=["small"],
        help="Operation scales to test (default: small)",
    )
    parser.add_argument("--rounds", type=int, default=5, help="Number of rounds per benchmark (default: 5)")
    parser.add_argument(
        "--quick", action="store_true", help="Run quick test with balanced config and small scale only"
    )

    args = parser.parse_args()

    # Handle 'all' selection
    scenarios_to_run = list(SCENARIOS.keys()) if "all" in args.scenarios else args.scenarios
    configs_to_run = list(CRUD_RATIOS.keys()) if "all" in args.configs else args.configs
    scales_to_run = list(OPERATION_SCALES.keys()) if "all" in args.scales else args.scales

    # Quick mode
    if args.quick:
        configs_to_run = ["balanced"]
        scales_to_run = ["small"]
        print("\n🚀 Quick mode: Running balanced config with small scale only\n")

    # Print summary
    print("\n" + "=" * 80)
    print("BENCHMARK CONFIGURATION")
    print("=" * 80)
    print(f"Scenarios: {', '.join(scenarios_to_run)}")
    print(f"CRUD Configs: {', '.join(configs_to_run)}")
    print(f"Operation Scales: {', '.join(scales_to_run)}")
    print(f"Rounds per benchmark: {args.rounds}")
    print("=" * 80 + "\n")

    # Print markdown table header
    print("\n## Benchmark Results\n")
    print("| Stack | Method | Status | Round | Diff | Initial | Final | Ops | C | R | U | D |")
    print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")

    success_count = 0
    failure_count = 0
    total_benchmarks = 0

    # Run benchmarks
    for scenario_key in scenarios_to_run:
        scenario = SCENARIOS[scenario_key]

        for script in scenario["scripts"]:
            for config_key in configs_to_run:
                config = CRUD_RATIOS[config_key]

                for scale_key in scales_to_run:
                    # Create a modified config with the selected scale
                    scaled_config = BenchmarkConfig(
                        name=f"{config.name}_{scale_key}",
                        num_operations=OPERATION_SCALES[scale_key],
                        create_ratio=config.create_ratio,
                        read_ratio=config.read_ratio,
                        update_ratio=config.update_ratio,
                        delete_ratio=config.delete_ratio,
                    )

                    total_benchmarks += 1

                    success = run_benchmark_for_scenario(scenario_key, script, scaled_config, args.rounds)

                    if success:
                        success_count += 1
                    else:
                        failure_count += 1

        # Add separator between scenarios
        print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")

    # Print summary
    print("\n" + "=" * 80)
    print("BENCHMARK SUMMARY")
    print("=" * 80)
    print(f"Total benchmarks: {total_benchmarks}")
    print(f"Successful: {success_count}")
    print(f"Failed: {failure_count}")
    print(f"Success rate: {success_count / total_benchmarks * 100:.1f}%")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
