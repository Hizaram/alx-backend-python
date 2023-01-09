#!/usr/bin/env python3
"""Module that contains the async coroutine that measure the runtime"""
from asyncio import run
from time import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Function that computes the average runtime of wait_n
        Args:   n (int): start threshold for number of delayed secs
                max_delay (int): end threshold for number of delayed secs

        Returns: Average of wait_n
    """
    start_time = time()
    run(wait_n(n, max_delay))
    end_time = time()
    return (end_time - start_time) / n
