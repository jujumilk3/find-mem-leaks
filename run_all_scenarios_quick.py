#!/usr/bin/env python3
"""Run all scenarios with quick tests"""
import sys
import asyncio
import os

# Test configurations
patterns = [
    {"name": "balanced", "c": 0.25, "r": 0.25, "u": 0.25, "d": 0.25},
    {"name": "create_heavy", "c": 0.5, "r": 0.2, "u": 0.2, "d": 0.1},
    {"name": "read_heavy", "c": 0.1, "r": 0.6, "u": 0.2, "d": 0.1},
]

async def test_async():
    sys.path.insert(0, 'sqlalchemy1x')
    from main_async import main

    print("\n### sqlalchemy1x_async")
    print("| Stack | Method | Status | Round | Diff | Initial | Final | Ops | C | R | U | D |")
    print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")

    for pattern in patterns:
        for fname in ['sqlalchemy1x/test.db', 'sqlalchemy1x/test.db-journal']:
            if os.path.exists(fname):
                os.remove(fname)

        for round_num in range(1, 4):
            result = await main(
                num_operations=1000,
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

def test_sync():
    sys.path.insert(0, 'sqlalchemy1x')
    from main_sync import main

    print("\n### sqlalchemy1x_sync")
    print("| Stack | Method | Status | Round | Diff | Initial | Final | Ops | C | R | U | D |")
    print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")

    for pattern in patterns:
        for fname in ['sqlalchemy1x/test.db', 'sqlalchemy1x/test.db-journal']:
            if os.path.exists(fname):
                os.remove(fname)

        for round_num in range(1, 4):
            result = main(
                num_operations=1000,
                create_ratio=pattern['c'],
                read_ratio=pattern['r'],
                update_ratio=pattern['u'],
                delete_ratio=pattern['d'],
            )
            print(f"| sqlalchemy1x_sync | {pattern['name']} | ✅ | {round_num} | "
                  f"{result['memory_diff']} | {result['initial_memory']} | "
                  f"{result['final_memory']} | {result['num_operations']} | "
                  f"{result['create_ratio']} | {result['read_ratio']} | "
                  f"{result['update_ratio']} | {result['delete_ratio']} |")

    print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")

async def test_async_scoped():
    sys.path.insert(0, 'sqlalchemy1x')
    from main_async_scoped_session import main

    print("\n### sqlalchemy1x_async_scoped")
    print("| Stack | Method | Status | Round | Diff | Initial | Final | Ops | C | R | U | D |")
    print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")

    for pattern in patterns:
        for fname in ['sqlalchemy1x/test.db', 'sqlalchemy1x/test.db-journal']:
            if os.path.exists(fname):
                os.remove(fname)

        for round_num in range(1, 4):
            result = await main(
                num_operations=1000,
                create_ratio=pattern['c'],
                read_ratio=pattern['r'],
                update_ratio=pattern['u'],
                delete_ratio=pattern['d'],
            )
            print(f"| sqlalchemy1x_async_scoped | {pattern['name']} | ✅ | {round_num} | "
                  f"{result['memory_diff']} | {result['initial_memory']} | "
                  f"{result['final_memory']} | {result['num_operations']} | "
                  f"{result['create_ratio']} | {result['read_ratio']} | "
                  f"{result['update_ratio']} | {result['delete_ratio']} |")

    print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")

async def main_runner():
    print("\n## Quick Benchmark Results (1000 operations per test)")
    await test_async()
    test_sync()
    await test_async_scoped()

if __name__ == "__main__":
    asyncio.run(main_runner())
