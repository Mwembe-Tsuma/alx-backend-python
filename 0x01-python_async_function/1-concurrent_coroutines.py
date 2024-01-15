#!/usr/bin/env python3
"""Asynchronous coroutine"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Implementation for the wait_n asynchronous routine"""
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
