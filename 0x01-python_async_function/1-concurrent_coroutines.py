#!/usr/bin/env python3
"""Module that contains the async coroutine that returns a list of all
delay_times in ascending order
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function that executes wait_random n times
        Args:   n(int): number of times to execute wait_random
                max_delay(int): number of secs to delay the program

        Returns: a List of all the delay_times
    """
    delay_time = [asyncio.create_task(wait_random(max_delay))
                  for _ in range(n)]
    return [await task for task in asyncio.as_completed(delay_time)]
