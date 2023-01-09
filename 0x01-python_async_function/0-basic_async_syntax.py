#!/usr/bin/env python3
"""Python module that defines an async coroutine that waits for a random
number of seconds
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Python function that waits for a random number of secs
        Args: max_delay (int): threshold for max number of secs

        Return: number of secs that program delayed
    """
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
