#!/usr/bin/env python3
"""Run quick benchmarks with 1000 operations for faster results"""
import sys
import asyncio
import os

sys.path.insert(0, 'sqlalchemy1x')
from main_async import main

async def run_quick_benchmarks():
    patterns = [
        {"name": "balanced", "c": 0.25, "r": 0.25, "u": 0.25, "d": 0.25},
        {"name": "create_heavy", "c": 0.5, "r": 0.2, "u": 0.2, "d": 0.1},
        {"name": "read_heavy", "c": 0.1, "r": 0.6, "u": 0.2, "d": 0.1},
        {"name": "write_intensive", "c": 0.4, "r": 0.1, "u": 0.4, "d": 0.1},
    ]

    print("\n## New Benchmark Results (Quick Test - 1000 operations)")
    print("\n| Stack | Method | Status | Round | Diff | Initial | Final | Ops | C | R | U | D |")
    print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")

    for pattern in patterns:
        # Clean database between patterns
        for fname in ['sqlalchemy1x/test.db', 'sqlalchemy1x/test.db-journal']:
            if os.path.exists(fname):
                os.remove(fname)

        for round_num in range(1, 4):  # Only 3 rounds for speed
            result = await main(
                num_operations=1000,  # Reduced from 10000
                create_ratio=pattern['c'],
                read_ratio=pattern['r'],
                update_ratio=pattern['u'],
                delete_ratio=pattern['d'],
            )

            print(f"| sqlalchemy1x_async | {pattern['name']}_quick | ✅ | {round_num} | "
                  f"{result['memory_diff']} | {result['initial_memory']} | "
                  f"{result['final_memory']} | {result['num_operations']} | "
                  f"{result['create_ratio']} | {result['read_ratio']} | "
                  f"{result['update_ratio']} | {result['delete_ratio']} |")

    print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")

if __name__ == "__main__":
    asyncio.run(run_quick_benchmarks())
