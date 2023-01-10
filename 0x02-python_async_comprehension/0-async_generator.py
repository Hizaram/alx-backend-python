#!/usr/bin/env python3
"""Module that contains the contains the async coroutine
named `async_generator`
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generates a sequence of ten numbers"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
