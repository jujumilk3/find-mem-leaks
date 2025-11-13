#!/usr/bin/env python3
"""Run a single benchmark test"""
import sys
import asyncio

sys.path.insert(0, 'sqlalchemy1x')

from main_async import main

async def run_test():
    print("Running sqlalchemy1x async session - balanced workload...")
    results = []

    for round_num in range(1, 6):  # 5 rounds
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

        results.append(result)

    return results

if __name__ == "__main__":
    asyncio.run(run_test())
