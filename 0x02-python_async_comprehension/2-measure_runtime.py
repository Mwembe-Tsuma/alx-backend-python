#!/usr/bin/env python3
"""Async Generator"""

import asyncio
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Iimplementation of the measure_runtime coroutine"""
    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    total_time = asyncio.get_event_loop().time() - start_time
    return total_time
