#!/usr/bin/env python3
"""Run benchmark and collect results"""
import sys
import asyncio
import os

# Clean up any existing database
if os.path.exists('test.db'):
    os.remove('test.db')
if os.path.exists('test.db-journal'):
    os.remove('test.db-journal')

sys.path.insert(0, 'sqlalchemy1x')

from main_async import main

async def run_benchmark():
    print("| Stack | Method | Status | Round | Diff | Initial | Final | Ops | C | R | U | D |")
    print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")

    for round_num in range(1, 6):
        result = await main(
            num_operations=10000,
            create_ratio=0.25,
            read_ratio=0.25,
            update_ratio=0.25,
            delete_ratio=0.25,
        )

        print(f"| sqlalchemy1x_async | balanced_small | ✅ | {round_num} | "
              f"{result['memory_diff']} | {result['initial_memory']} | "
              f"{result['final_memory']} | {result['num_operations']} | "
              f"{result['create_ratio']} | {result['read_ratio']} | "
              f"{result['update_ratio']} | {result['delete_ratio']} |")

if __name__ == "__main__":
    asyncio.run(run_benchmark())
