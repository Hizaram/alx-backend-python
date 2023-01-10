#!/usr/bin/env python3
"""Module that contains the coroutine that creates a list of 10 generated
numbers from async_generator
"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Creates a List of 10 numbers from a a 10-number generator."""
    return [num async for num in async_generator()]
