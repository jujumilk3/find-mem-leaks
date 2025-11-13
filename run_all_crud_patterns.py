#!/usr/bin/env python3
"""Run all CRUD patterns for sqlalchemy1x async"""
import sys
import asyncio
import os

sys.path.insert(0, 'sqlalchemy1x')
from main_async import main

async def run_all_patterns():
    patterns = [
        {"name": "balanced", "c": 0.25, "r": 0.25, "u": 0.25, "d": 0.25},
        {"name": "create_heavy", "c": 0.5, "r": 0.2, "u": 0.2, "d": 0.1},
        {"name": "read_heavy", "c": 0.1, "r": 0.6, "u": 0.2, "d": 0.1},
        {"name": "update_heavy", "c": 0.2, "r": 0.2, "u": 0.5, "d": 0.1},
        {"name": "delete_heavy", "c": 0.1, "r": 0.2, "u": 0.2, "d": 0.5},
        {"name": "write_intensive", "c": 0.4, "r": 0.1, "u": 0.4, "d": 0.1},
        {"name": "read_only", "c": 0.05, "r": 0.85, "u": 0.05, "d": 0.05},
        {"name": "mixed_workload", "c": 0.3, "r": 0.4, "u": 0.2, "d": 0.1},
    ]

    print("| Stack | Method | Status | Round | Diff | Initial | Final | Ops | C | R | U | D |")
    print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")

    for pattern in patterns:
        # Clean database between patterns
        for fname in ['test.db', 'test.db-journal']:
            if os.path.exists(fname):
                os.remove(fname)

        for round_num in range(1, 6):
            result = await main(
                num_operations=10000,
                create_ratio=pattern['c'],
                read_ratio=pattern['r'],
                update_ratio=pattern['u'],
                delete_ratio=pattern['d'],
            )

            print(f"| sqlalchemy1x_async | {pattern['name']} | ✅ | {round_num} | "
                  f"{result['memory_diff']} | {result['initial_memory']} | "
                  f"{result['final_memory']} | {result['num_operations']} | "
                  f"{result['create_ratio']} | {result['read_ratio']} | "
                  f"{result['update_ratio']} | {result['delete_ratio']} |")

        print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")

if __name__ == "__main__":
    asyncio.run(run_all_patterns())
