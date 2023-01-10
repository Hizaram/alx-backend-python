#!/usr/bin/env python3
"""Module that contains the coroutine that measures the total execution
time"""
import asyncio
from time import time


async_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension four times and measures the total
    execution time.
        Returns: total execution time
    """
    start_time = time()
    await asyncio.gather(*(async_comp() for _ in range(4)))
    return time() - start_time
